---
name: catchup
description: Worker — pulls Slack activity since last_catchup for one client or channel, updates its stream-based dossier in place, and commits. Writes the dossier; does not produce a readable digest. Use when the user says "/catchup <slug>" or "/catchup #<channel>". For the readable brief or a multi-client run, use /slack-attack instead.
---

`/catchup` is the worker. Its product is one dossier file (`clients/<slug>.md` or `channels/<name>.md`) and one commit. Dossiers are read by **agents in this repo**, not humans: keep them small, current and structured. Git is the event log — the dossier holds current state only. It does **not** write a readable brief; that's `/slack-attack`'s job.

A target is required. With no arg, stop and point at `/slack-attack`.

If the client dossier has `status: retired`, emit one line and stop — no Slack pull, no `last_catchup` bump:

```
catchup: <slug> — retired (<retired_at>); skipping. Remove `status: retired` from frontmatter to re-activate.
```

## Who the user is

The reader is **Cameron Copland** (Slack user ID `U099FA0D7CP`). Direct mentions / DMs that target this ID are notable; mentions of other Camerons (notably **Cameron Hughes**, an Analyst — see `../MahiProduct/.claude/org-chart.md`) are not. Match strictly on the Slack user ID — never infer audience from first names.

## Sources — read, never write

- Hosts / Slack channel names / party names / distribution markets → `../VibePulse/.claude/clients/<slug>.yaml`.
- Commercial terms → `../MahiProduct/data/billing/clients.json`.
- Internal Mahi staff → `../MahiProduct/.claude/org-chart.md`. Use it for attribution; never put staff in `contacts`.
- External contacts → `../MahiProduct/wiki/people/`. Only people *not* there go in the dossier's `contacts`.

Never write outside this repo. Never copy into a dossier anything one read of these sources returns (hosts, terms, party names, contact details). The dossier stores the synthesis — what is going on and where it stands — plus permalinks to dig further.

## Dossier format (the contract)

Enforced by `scripts/check-dossiers` (pre-commit runs it). Templates: `clients/_template.md`, `channels/_template.md`.

```markdown
---
slug, aliases, refs, channels (name: ID), contacts, last_catchup, status
---
## Now
≤4 lines: what matters with this client right now.

## Streams

### <id> — <title>
status: open|watching|closed · since: YYYY-MM-DD · last: YYYY-MM-DD[ · closed: YYYY-MM-DD]
State: current truth, 1–4 sentences, rewritten in place.
Next: who owes what (omit if nothing).
Refs: <origin permalink> <latest permalink>   (bare URLs, 1–4)

## Arc
- YYYY-MM-DD — one line per relationship-level milestone (≤~20 lines)
```

- **Stream** = one ongoing topic (an integration, a recurring pricing problem, a commercial thread), not one incident. Ten XAUUSD rejection incidents are one stream. Target 5–15 streams per client.
- **ID**: kebab-case, ≤24 chars, unique, **never renamed or reused**. The heading line is the stable anchor git history is queried by. Edit the title if needed, never the ID.
- **Meta line** is the first line under the heading, exact format above (separator ` · `). `since` = first Slack signal; `last` = date of the latest Slack message on the stream and **must match a permalink in Refs** (±1 day). Dates in UTC.
- **State** is rewritten, never appended to. No "2026-10-07 update —" lines; that history is in git.
- **Order**: open (newest `last` first), then watching, then closed.
- **Size**: ≤10KB target, 15KB hard cap. Over target → merge or close streams, tighten State.
- Never delete a stream by hand. Close it; `scripts/prune-dossiers` removes closed streams 14 days later.

## Resolving the target

- `/catchup <slug>` → `clients/<slug>.md`. Read channels from frontmatter `channels:` (name → ID); skip names matching the skip list in `.claude/docs/slack-conventions.md`.
- If `channels:` is missing a channel the client should have: resolve names from the VibePulse `slack:` block (it's `{internal: <name>, client: <name>}` — **use both**; the internal channel carries the root-cause diagnosis), get IDs with `slack_search_channels` (`channel_types: "public_channel,private_channel"`), and write `name: ID` into `channels:`. Never skip a missing internal channel — that omission cost the axiory LD4 root cause on 2026-04-27.
- `/catchup #<channel>` or `/catchup <channel-name>` → `channels/<name>.md`, reading `channel_id` from frontmatter.
- Dossier has no `## Streams` section → it's legacy: follow **Legacy conversion** below.

### Bootstrap a client dossier

If `clients/<slug>.md` doesn't exist:

1. Find the client: `../VibePulse/.claude/clients/<slug>.yaml` (try hyphen/underscore and `-crypto`/`-cfd` variants). Pre-live clients often have none — then check `../MahiProduct/data/client-hosts.json`, the "Signed but not yet live" section of `../MahiProduct/data/fleet.txt`, `../MahiProduct/data/onboarding/<slug>.json`, and `../MahiProduct/wiki/clients/`. Only if none know it, report unknown and stop.
2. Copy `clients/_template.md` to `clients/<slug>.md`; set `slug`, `refs` (unknown refs `null` with a short trailing comment), `aliases` if billing/onboarding use another slug, `channels` (resolve as above), `contacts: []`, `last_catchup: null`. Delete the template's example stream and Arc line.
3. This run populates Now / Streams / Arc. Use the 30d window (see Reading activity) and expand on ambiguity.
4. Commit subject `chore(catchup): bootstrap <slug> dossier`.

### Bootstrap a channel dossier

If `channels/<name>.md` doesn't exist: copy `channels/_template.md`; `slack_search_channels` for the ID and purpose (skim ~20 recent messages if the purpose is generic); `scope` is a best guess; delete the template example; populate from this run.

## Sanity-check the window — before reading Slack

Anchor every date to **bash output, not your own reasoning**. Three documented corruptions came from the agent miscalculating "today" by a year.

1. Run via Bash and use the output verbatim for the whole run:

   ```
   now_unix=$(date +%s)
   now_iso=$(date -u +%FT%TZ)
   ```

   Never infer "today" from the conversation, the dossier, commit dates or training context.

2. `oldest_unix` = Unix seconds of the dossier's `last_catchup` (`date -u -j -f %Y-%m-%dT%H:%M:%SZ <iso> +%s` on macOS, `date -u -d <iso> +%s` on Linux); for `last_catchup: null`, `now_unix - 30*86400`; for an ambiguity expansion, the wider anchor you chose. Decode it back (`date -u -r $oldest_unix +%FT%TZ` / `date -u -d @$oldest_unix +%FT%TZ`) and confirm it matches what you expected — a year off means abort.
3. If `now_unix - oldest_unix > 90*86400`, abort. The cap is both a cost bound and a year-off tripwire.
4. The `last_catchup` you will write must be ≤ `now_unix + 60`.

On any failure, abort before reading Slack:

```
catchup: <target> — ABORT: window sanity-check failed.

<one line per violation>

Inspect the dossier and your date conversions before retrying.
```

## Reading activity

1. `oldest` = `last_catchup`; if null, 30 days ago.
2. For each channel in `channels:` (minus skip list): `slack_read_channel` with `oldest`, `limit: 100`. If the response has a `next_cursor`, keep paginating until you reach `oldest`.
3. For notable threads, `slack_read_thread` with the real `message_ts` (searches need `response_format: "detailed"` to return it).
4. **Work budget** — so one client can't stall a parallel run: at most 3 pages per channel per 30 days of window (9 pages for 90d) and at most 15 thread expansions (30 in a legacy conversion). If you hit it, stop reading, write what you have, and report `Budget hit on: <channel>`.
5. **Discard out-of-window results.** Drop any message (from search or channel read) whose `ts` falls outside `[oldest_unix, now_unix]` — decode `ts`, don't eyeball it.

## Resolving ambiguity — expand the window

The windows are starting points. If in-window messages reference events you can't see, dig before writing: every stream's State must stand on its own, without "per an earlier event" or "pre-window".

Triggers: a message refers to an earlier event you lack context for; channels contradict each other on lifecycle; a new or converted dossier leaves you guessing about the client's status.

How, in order (expansions count against the work budget):

1. Widen channel reads to 60d, then 90d (never beyond — hard cap).
2. Search the slug across channels with `slack_search_public_and_private` (default context on), **always time-bounded** with `after`/`before` (or the `after:YYYY-MM-DD` / `before:YYYY-MM-DD` modifiers). Unbounded searches are the root of the year-off corruption. Use hits to decide where to read next, not as facts (see next section).
3. Read parent threads via `slack_read_thread`.
4. Follow the breadcrumb to the original message and read around it.

Stop when each stream's State is self-contained with dated permalinks, or at the 90d cap — then say so in State ("earliest signal in window; older context not searched").

## What counts as notable

In priority order:

1. **Direct mentions of the user** (`<@U099FA0D7CP>`) or DMs.
2. **Questions awaiting a reply** — unanswered `?`, especially in threads the user was in.
3. **Decisions** — "we're going to", "agreed", "let's do X".
4. **Escalations** — client dissatisfaction, outages, urgent language, incidents.
5. **Recurring issues** — something an existing stream covers flaring again → update that stream.
6. **New external people** with a known role and expected repeat contact, not in `../MahiProduct/wiki/people/` → `contacts`.
7. **Facts contradicting the dossier or upstream** — fix the stream/Now; don't edit upstream.

Routine bot pings, deployment notifications and single-reaction chatter are not notable.

## Cross-channel signals — trigger, not truth

`slack_read_channel` on the dossier's own channels is authoritative. Search hits from other channels (#sales, #frontoffice, #internal-trading-daily-checks) are **triggers to investigate**:

1. Corroborate against the client's own channels in the same window before writing a claim as fact. (2026-04-29: #sales grouped Fintokei with Errante as offboarded; Fintokei's channels were live — a typo.)
2. Read the search context, don't keyword-match; neighbouring messages often carry the correction. If context is thin, read the source channel or thread around the hit.
3. If corroboration fails, write the contradiction ("sales says X, client channels show Y") in the stream, not the claim.

Never retire a dossier on cross-channel signal alone.

## Updating the dossier

Use `Edit` (small diffs), except bootstrap and legacy conversion (`Write`).

1. **Map** each notable in-window item to a stream. Same topic, counterparty, project or recurring problem → existing stream. Prefer extending a stream over creating a sibling.
2. **Update** a stream that moved: rewrite `State` (current truth, not a log) and `Next`; set `last` to the date of its latest in-window message; in `Refs` keep the origin permalink and replace the previous "latest" with the newest one (max 4).
3. **Create** a new stream for a genuinely new topic: new ID, `since` = its first message date.
4. **Forced review**: run `scripts/check-dossiers --stale <file>` and decide every stream it lists — open >30d without activity: close it (State says how it ended, or "no activity since <date>; assumed resolved") or downgrade to `watching` with a reason; watching >60d: close it, or re-open with a `Next:` naming a concrete pending action. Never leave a listed stream untouched.
5. **Close**: `status: closed`, append `· closed: <today>` to the meta line, State gives the outcome. Relationship-level outcomes (go-live, decommission, contract change, key person change, major incident) also get an Arc line.
6. **Merge**: close the absorbed stream with `State: merged into <id>.`
7. **Now**: rewrite if the client's posture changed (≤4 lines).
8. **Order** streams: open (newest `last` first), watching, closed.
9. **contacts**: add per notability rule 6; `confidence: low` only when unsure.
10. Set `last_catchup` to `now_iso`.

## Legacy conversion (temporary — removed once every dossier is converted)

A dossier without `## Streams` was written by older, less capable models and may contain errors. Rebuild it:

1. Treat the old content (`Status`, `History`, `Recent issues`, `Notable topics`, `key_people_overrides`) as **leads, not facts**.
2. Read Slack for the normal window (`last_catchup` → now) per the sections above.
3. For each old `[open]`/`[watching]` entry: if in-window activity covers it, it's live. Otherwise read the thread of its newest permalink (`slack_read_thread`). No sign of life for >30 days → drop it as `stale` — unless it is an explicit unanswered commitment, which becomes a `watching` stream.
4. Group surviving items and new activity into streams (target 5–15).
5. **Arc**: from old `History` and significant resolved entries (go-lives, decommissions, contract events, major incidents, key people changes); ≤20 lines; exact dates where the source pins them, `YYYY-MM` otherwise.
6. **Frontmatter**: `channels:` from `channels_override` / the VibePulse `slack:` block plus IDs from the table in `.claude/docs/slack-conventions.md` (search for any missing); `contacts` from `key_people_overrides`, minus anyone in `../MahiProduct/wiki/people/` or the org chart; drop `channels_override` and `key_people_overrides`. Keep `slug`, `aliases`, `refs`, `status`/`retired_*`.
7. Write the whole file with `Write` from the template shape; no `Status`, `History`, `Recent issues` or `Notable topics` sections remain. Aim ≤10KB.
8. Commit with subject `refactor(dossiers): convert <slug> to streams` and body:

   ```
   Window <oldest_iso>..<now_iso>.
   streams: <id>(new) <id>(new) ...
   dropped: <N> old entries — <a> resolved, <b> stale, <c> merged
   stale: <short title>; <short title>; ...
   ```

   The `stale:` line lists the titles (≤60 chars each) of every entry dropped as stale, so the user can audit the risky drops.

## Sanity-check before commit

1. `scripts/prune-dossiers <file>` — note any `pruned <id>` lines for the trailer.
2. `scripts/check-dossiers <file>` must exit 0. Warnings: fix size/Arc/Refs warnings if cheap.
3. Every stream you created or updated has `last` within `[date(oldest_iso) - 1 day, date(now_iso)]`. Exception (legacy conversion only): a `watching` stream carried over from an old unanswered commitment (conversion step 3) keeps its real `last`, which may predate the window.

If 2 or 3 fails and you can't fix it from what you read, **abort**: leave the file dirty, don't commit, don't bump `last_catchup`:

```
catchup: <target> — ABORT: sanity-check failed before commit.

<check-dossiers output / violations>

Likely date-math bug. Inspect with `git diff` before committing manually.
```

The pre-commit hook re-runs the check as a backstop; a clean self-abort is the intended path. Never `--no-verify`.

## Committing

- Stage only the target dossier. Never `git add -A`. If the dossier already had unrelated uncommitted edits before this run, stop and report instead of guessing.
- Subject ≤72 chars (`.githooks/commit-msg` enforces it); dates `YYYY-MM-DD`:

  | Case | Subject |
  |---|---|
  | Refresh | `chore(catchup): refresh <slug> (<YYYY-MM-DD>..<YYYY-MM-DD>)` |
  | Quiet window | `chore(catchup): bump <slug> (quiet window)` |
  | Bootstrap | `chore(catchup): bootstrap <slug> dossier` |
  | Legacy conversion | `refactor(dossiers): convert <slug> to streams` |

- Body (refresh/bootstrap): `Window <oldest_iso>..<now_iso>.` then one trailer line listing every stream touched:

  ```
  streams: tegis-api(updated) mt4-decom(new) xau-hedging(closed) old-thing(pruned) fx-gaps(watching) ack-x(merged>xau-hedging)
  ```

  Verbs: `new | updated | closed | watching | merged>ID | pruned`. `/slack-attack` and `/weekly-overview` read this line; `git log --grep=<id>` depends on it.
- Other catchups commit to this repo in parallel and share one git index, so a plain `git commit` can sweep up another agent's staged dossier. Always commit by path: `git commit -m "<subject>" -m "<body>" -- <dossier path>`. If it fails on `.git/index.lock`, `sleep 3` and retry, up to 5 times.
- Don't push. The caller pushes.

## Output (to caller)

```
catchup: <target> — <oldest_iso>..<now_iso>

Commit: <short-sha>
streams: <same trailer line>
Stale review: <n> streams reviewed (<c> closed, <w> → watching, <o> re-opened)
Channels read: <n>, messages scanned: ~<m>, threads expanded: <t>
Budget hit on: <list or "none">
Quiet channels: <list or "none">
```

Quiet window (no notable human activity, nothing reviewed or pruned): bump `last_catchup` only, commit, and output one line:

```
catchup: <target> — quiet window (<N> bot pings, no human discussion). last_catchup bumped (commit <short-sha>).
```

If anything in the window is addressed to the user (direct mention or DM awaiting reply), add a final `Action items:` line with permalinks. Match strictly on `U099FA0D7CP`.

No prose digest. The dossier and commit are the artefact.

## Constraints

- Never fabricate a Slack permalink. Re-search with `response_format: "detailed"` for a real `message_ts`.
- Never rename a stream ID or delete a stream by hand.
- Never write outside this repo.
- Leave empty sections empty — no placeholder text (an empty `## Arc` is fine).
