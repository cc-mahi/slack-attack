---
name: catchup
description: Worker — pulls Slack activity since last_catchup for one client or channel and applies dossier updates in place. Writes the dossier; does not produce a readable digest. Use when the user says "/catchup <slug>" or "/catchup #<channel>". For the readable brief or a multi-client run, use /slack-attack instead.
---

`/catchup` is the worker. Its product is the dossier file on disk — it reads Slack and edits `clients/<slug>.md` or `channels/<name>.md`. It does **not** synthesise a readable brief; that's `/slack-attack`'s job. When invoked directly by Cameron it returns a terse structured summary of what changed; when invoked from a subagent (via `/slack-attack`) the subagent forwards the same summary back.

A target is required. If invoked with no arg, stop and point at `/slack-attack`.

If the resolved client dossier has `status: retired` in frontmatter, refuse and stop. Emit one line and exit — don't pull Slack, don't bump `last_catchup`:

```
catchup: <slug> — retired (<retired_at>); skipping. Remove `status: retired` from frontmatter to re-activate.
```

The dossier stays as a frozen record. Re-activation is a deliberate frontmatter edit by Cameron, not something to negotiate around.

## Source-of-truth recap

- Hosts / Slack channels / party names / distribution markets → `../VibePulse/.claude/clients/<slug>.yaml`.
- Commercial terms → `../MahiProduct/data/billing/clients.json`.
- Internal Mahi staff roster (for the "no Mahi staff in `key_people_overrides`" rule) → `../MahiProduct/.claude/org-chart.md`. If a name appears there, it's internal — don't add to `key_people_overrides`.
- External contacts worth persisting → `../MahiProduct/wiki/people/`. Never write there from here; if you find a new external contact worth keeping, add to `key_people_overrides` here with `confidence: low` and flag for promotion.

## Resolving the target

- `/catchup <slug>` → `clients/<slug>.md`. Channels resolve from (in order): `channels_override` on the dossier, then `slack:` in `../VibePulse/.claude/clients/<slug>.yaml`. The VibePulse `slack:` block is a dict `{internal: <name>, client: <name>}` — **scan both**. The internal channel typically has the actual root-cause diagnosis; skipping it loses load-bearing context. If VibePulse has multiple related yamls (e.g. `pepperstone` + `pepperstone-crypto`) and they share the same slack channels, they're one target — use either, they'll resolve to the same thing.
- `/catchup #<channel>` or `/catchup <channel-name>` → `channels/<name>.md`. If missing, create it from `channels/_template.md` and derive the frontmatter yourself (see "Bootstrap a channel dossier" below) — don't block.
- No-arg form is not supported. Tell Cameron to use `/slack-attack` for the multi-client batched flow.

### Bootstrap a client dossier

If `clients/<slug>.md` doesn't exist:

1. Check `../VibePulse/.claude/clients/<slug>.yaml`. If absent, try common variants (hyphen/underscore, with/without `-crypto`/`-cfd` suffix). If VibePulse has nothing and `../MahiProduct/data/billing/clients.json` has nothing, report the slug as unknown and stop.
2. Copy `clients/_template.md` → `clients/<slug>.md`.
3. Fill `refs:` — point `vibepulse` at the yaml(s), `billing`/`hosts` at the MahiProduct catalogues, `wiki` at `../MahiProduct/wiki/clients/<slug>.md` if it exists else `null`.
4. Leave `channels_override: null`, `key_people_overrides: []`, `last_catchup: null`.
5. Leave `Recent issues` and `Notable topics` empty — the current `/catchup` run will populate them.
6. **Status section:** if `wiki:` is set (MahiProduct has it), delete the `## Status` section entirely — the wiki is canonical. If `wiki: null`, keep the section and populate from VibePulse + the catchup window's signals (stage, integration, relationship — three bullets, one line each). Don't fabricate; if a field is unknown, write `unknown` and move on.
7. Note the bootstrap in the run summary ("bootstrapped `clients/<slug>.md` from VibePulse").

### Bootstrap a channel dossier

If `channels/<name>.md` doesn't exist:

1. `slack_search_channels` for the channel; seed `purpose` from its topic/purpose. If generic, skim ~20 recent messages to infer.
2. `scope` is a best-guess (`cross-cutting` / `team` / `announcements` / `other`) — Cameron will correct on review.
3. Record `channel_id` in `.claude/docs/slack-conventions.md`.

## Reading activity

For each target channel:

1. `oldest` = `last_catchup` on the dossier; if null (freshly bootstrapped or just-reset dossier), 30d ago; else 24h ago. The wider null-case window is so initial population picks up real history — 24h on a brand-new dossier produced empty `Recent issues` sections.
2. Resolve channel_id: prefer `.claude/docs/slack-conventions.md` cache; else `slack_search_channels` with `channel_types: "public_channel,private_channel"`. Write any newly-resolved ID back to the cache. If a client target's internal channel is missing from the cache, **don't skip it** — search for it and cache it on first sight. Absence-by-omission is the failure mode that cost us the axiory LD4 root-cause diagnosis on 2026-04-27.
3. `slack_read_channel` with `oldest`, `limit: 100`. Note if hit the limit — there's more.
4. For notable threads, `slack_read_thread` with the real `message_ts` (needs `response_format: "detailed"` when searching).

Skip channels matching the skip list in `.claude/docs/slack-conventions.md`.

## What counts as notable

In priority order:

1. **Direct mentions of Cameron** (`<@U099FA0D7CP>`) or DMs.
2. **Questions awaiting a reply** — unanswered `?` messages, especially in threads Cameron was in.
3. **Decisions** — "we're going to", "agreed", "let's do X".
4. **Escalations** — client dissatisfaction, outages, urgent language, specific incidents.
5. **Recurring issues** — topic already in the dossier's `Recent issues` that's flaring again.
6. **New external people** — client/prospect/vendor names that aren't yet in `../MahiProduct/wiki/people/` *and* aren't already in `key_people_overrides`.
7. **Dossier-contradicting facts** — e.g. VibePulse says `SI book` but messages discuss churn/pause; flag but don't edit VibePulse. If the contradiction is about longer-term state (stage / integration / relationship) on a `wiki: null` dossier, refresh the `## Status` section in the same run.

Routine bot pings, deployment notifications, and single-reaction chatter are not notable. Skip silently.

## Cross-channel signals — trigger, not truth

`slack_read_channel` is the authoritative read — scoped to the target's resolved channels (`channels_override` → VibePulse `slack:` block → cache). Anything from there can be written into the dossier directly.

`slack_search_public_and_private` for the slug across all channels is allowed and sometimes load-bearing (e.g. an offboarded client's `internal-<slug>` is archived; the only live signal is in `#sales` or `#internal-trading-daily-checks`). But search results are **triggers to investigate, not authoritative state**.

Rules for any cross-channel hit:

1. **Corroborate against the target's own channels before writing it as fact.** If a #sales message claims a client is offboarded, check `internal-<slug>` and `mahi-<slug>` activity in the same window — channels still live, recent client comms, live PnL or dashboards all contradict it. Mismatches are usually typos, scope confusion, or someone speaking about a specific product/contract rather than the whole relationship. (Real example: 2026-04-29 #sales note grouped Fintokei with Errante as offboarded; Errante checked out, Fintokei did not — channels live, B-book PnL active, FIX integration in flight.)
2. **Read the context, don't just keyword-match.** `slack_search_public_and_private` returns surrounding messages by default (`include_context: true`) — don't pass `include_context: false` for lifecycle hits, and don't collapse a hit to a one-line summary that throws the context away. The neighbouring messages often contain the correction or qualifier (real example: 2026-04-29 #sales note grouping Fintokei with Errante was a typo Nia self-corrected in a follow-up; the worker had access to it via search context but reported only the matching line). If the context didn't include enough to corroborate, `slack_read_channel` the source around the hit's `message_ts`, or `slack_read_thread` if it's threaded.
3. **If corroboration fails, write the contradiction, not the claim.** A `[open]` Recent issues entry naming both signals ("sales says X, target channels show Y") is more useful than picking one and being wrong.

This applies to lifecycle claims especially (offboarded, paused, churned, contract changes) — the kind of thing that drives `status: retired`. Don't retire a dossier on cross-channel signal alone.

## Updating the dossier

Apply edits with `Edit`, not `Write`, so diffs stay minimal (except when bootstrapping a new dossier).

- Append new entries to `Recent issues` (or `Recent topics` for channel dossiers).
- Promote pre-existing `[open]` entries whose threads had activity in the window to `[resolved]`, or refresh their summary line.
- Append `Notable topics` entries where appropriate.
- Update `key_people_overrides` for new external contacts (low confidence flag if you're unsure).
- Bump `last_catchup` to the run timestamp in frontmatter.

The dossier is the readable artefact — it can be detailed, jargon-dense, and contain everything `/slack-attack` will later need to summarise. Don't pre-summarise; write what you found.

## Output (to caller)

Catchup's output is a structured confirmation, not a prose digest. The caller (Cameron directly, or a `/slack-attack` subagent) uses this to know what changed. Keep it tight.

```
catchup: <target> — <ISO window>

Changes to <path>:
- bootstrapped from VibePulse  (only if applicable)
- Recent issues: +N appended (X open / Y resolved), Z promoted [open]→[resolved]
- Notable topics: +N appended
- key_people_overrides: +N (M flagged low-confidence)
- last_catchup → <new timestamp>

Channels read: <count>, messages scanned: <approx>, threads expanded: <count>
Quiet channels (no human discussion): <comma list or "none">
Hit channel limit on: <list or "none">
```

If the run produced zero changes (quiet window), output one line and stop:

```
catchup: <target> — quiet window (<N> bot pings, no human discussion). last_catchup bumped.
```

Do **not** produce paragraphs of prose. Do **not** synthesise a readable brief. The dossier is the artefact; `/slack-attack` reads it to write prose for Cameron.

## Action items

If anything in the window is addressed to Cameron (direct mention or DM awaiting reply), include a single `Action items:` line at the end of the output naming the items with permalinks. Otherwise omit. Don't speculate about other Camerons / Wills — Cameron Copland is `U099FA0D7CP`.

## Dossier conventions

### `Recent issues` entries

Every entry starts with a status marker and cites at least one real Slack permalink. If you don't have a real `message_ts`, search again with `response_format: "detailed"` to get one before writing the entry.

```
> [open] YYYY-MM-DD — short title
> 1–3 lines. [permalink](https://mahifx.slack.com/archives/<CID>/p<TS>)
```

Markers:
- `[open]` — unresolved, awaiting action, or active investigation with a plan ("hedger latency being tuned, further digging flagged").
- `[resolved]` — closed out (fix deployed, decision made, incident over).
- `[watching]` — passive observation of a pattern with no active work. If anyone is actively working on it, it's `[open]`, not `[watching]`. Use sparingly.

On each run, re-read existing `[open]` entries whose threads had activity in the window and promote to `[resolved]` or refresh the summary line.

### `Recent topics` entries (channels only)

Channel dossiers use `Recent topics` instead of `Recent issues`. Same permalink requirement, **no status markers**. If a channel thread escalates into a real tracked issue, it belongs in the relevant client's `Recent issues`, not the channel dossier.

```
- YYYY-MM-DD — short description. [permalink](https://mahifx.slack.com/archives/<CID>/p<TS>)
```

### `key_people_overrides` threshold

Only external people (client-side, consultants, LP/vendor). Never Mahi staff — check `../MahiProduct/.claude/org-chart.md` first. Never add a name already on a `../MahiProduct/wiki/people/` page; if one exists there, trust it and leave this list alone.

Add someone only if the role is known **and** you expect repeat interaction. One-off "new user added" events belong in `Recent issues`, not the people roster.

```yaml
- {name: "...", role: "...", confidence: low}
```

- `confidence: low` — uncertain role spelling, contradictory signals, or only seen once but plausibly recurring. Next `/catchup` flags these for verification.
- Default is high confidence — omit the field in that case.

Never inline `# comment` annotations into YAML values — parsers handle them inconsistently.

## Constraints

- Never fabricate a Slack permalink. Re-search with `response_format: "detailed"` instead of omitting it.
- Channel zero human messages in the window → one-line note, don't expand.
- Leave empty dossier sections blank — no placeholder text. Append cleanly when content exists.
- Don't re-state info that's in VibePulse / MahiProduct. If something appears in Slack that's *already true* per the upstream ref (e.g. a host FQDN), skip it.
- No prose digest in the output. Cameron reviews the dossier via `git diff` and gets the readable form via `/slack-attack`.
