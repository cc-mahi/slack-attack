---
name: catchup
description: Daily Slack catch-up digest. Reads activity since last_catchup for a client, a channel, or everything, summarises notable items, and applies dossier updates. Use when the user says "/catchup", "/catchup <slug>", or "/catchup #<channel>".
---

Produce a focused digest of Slack activity and apply dossier updates directly. Cameron reviews via `git diff` and commits when happy — no accept step.

## Source-of-truth recap

- Hosts / Slack channels / party names / distribution markets → `../VibePulse/.claude/clients/<slug>.yaml`.
- Commercial terms → `../MahiProduct/data/billing/clients.json`.
- Internal Mahi staff roster (for the "no Mahi staff in `key_people_overrides`" rule) → `../MahiProduct/.claude/org-chart.md`. If a name appears there, it's internal — don't add to `key_people_overrides`.
- External contacts worth persisting → `../MahiProduct/wiki/people/`. Never write there from here; if you find a new external contact worth keeping, add to `key_people_overrides` here with `confidence: low` and flag for promotion.

## Resolving the target

- `/catchup <slug>` → `clients/<slug>.md`. Channels resolve from (in order): `channels_override` on the dossier, then `slack:` in `../VibePulse/.claude/clients/<slug>.yaml`. The VibePulse `slack:` block is a dict `{internal: <name>, client: <name>}` — **scan both**. The internal channel typically has the actual root-cause diagnosis; skipping it loses load-bearing context. If VibePulse has multiple related yamls (e.g. `pepperstone` + `pepperstone-crypto`) and they share the same slack channels, they're one target — use either, they'll resolve to the same thing.
- `/catchup #<channel>` or `/catchup <channel-name>` → `channels/<name>.md`. If missing, create it from `channels/_template.md` and derive the frontmatter yourself (see "Bootstrap a channel dossier" below) — don't block.
- `/catchup` (no arg) → rank all targets by `last_catchup` staleness × recent-message-count. For clients, use VibePulse + MahiProduct's active-client lists as the enumeration — if a slack-attack dossier is missing, **auto-bootstrap it** (see "Bootstrap a client dossier" below) rather than skipping. Digest the top 3–5. Report which ones you skipped and why.

### Bootstrap a client dossier

If `clients/<slug>.md` doesn't exist:

1. Check `../VibePulse/.claude/clients/<slug>.yaml`. If absent, try common variants (hyphen/underscore, with/without `-crypto`/`-cfd` suffix). If VibePulse has nothing and `../MahiProduct/data/billing/clients.json` has nothing, report the slug as unknown and stop.
2. Copy `clients/_template.md` → `clients/<slug>.md`.
3. Fill `refs:` — point `vibepulse` at the yaml(s), `billing`/`hosts` at the MahiProduct catalogues, `wiki` at `../MahiProduct/wiki/clients/<slug>.md` if it exists else `null`.
4. Leave `channels_override: null`, `key_people_overrides: []`, `last_catchup: null`.
5. Leave `Recent issues` and `Notable topics` empty — the current `/catchup` run will populate them.
6. **Status section:** if `wiki:` is set (MahiProduct has it), delete the `## Status` section entirely — the wiki is canonical. If `wiki: null`, keep the section and populate from VibePulse + the catchup window's signals (stage, integration, relationship — three bullets, one line each). Don't fabricate; if a field is unknown, write `unknown` and move on.
7. Note the bootstrap in the digest output ("bootstrapped `clients/<slug>.md` from VibePulse").

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

## Output shape

```
# Catch-up: <target> — <ISO window>

## Notable
- <one bullet per item>. Permalink if available. Who / what / why-it-matters in one line.

## Action items (for Cameron)
- Anything that needs his reply or decision.

## Quiet
<one line: "~30 bot pings, 2 deploy notices, no human discussion">

---

## Dossier changes applied (clients/<slug>.md)

- Added to `key_people_overrides`: <names>
- Appended to `Recent issues`: <count> entries
- Appended to `Notable topics`: <count> entries
- `last_catchup` → <now>
- Flagged for verification: <low-confidence entries that still need a real role>

Review with `git diff clients/<slug>.md`.
```

Action items: only mention someone by name if they're Cameron. Don't hedge by speculating whether another "Cameron" or "Will" might be him — his name is Cameron Copland (Slack `U099FA0D7CP`). If nothing is addressed to him, say "None" and move on.

Apply edits with `Edit`, not `Write`, so diffs stay minimal (except when bootstrapping a new dossier).

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

- Keep the digest short. A dense 15-line digest beats a 200-line one Cameron won't read.
- Never fabricate a Slack permalink. Re-search with `response_format: "detailed"` instead of omitting it.
- Channel zero human messages in the window → one-line note, don't expand.
- Leave empty dossier sections blank — no placeholder text. Append cleanly when content exists.
- Don't re-state info that's in VibePulse / MahiProduct. If something appears in Slack that's *already true* per the upstream ref (e.g. a host FQDN), skip it.
