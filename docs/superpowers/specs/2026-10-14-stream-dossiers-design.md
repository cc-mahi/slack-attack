# Stream-based dossiers — design

Date: 2026-10-14. Status: draft for review.

## Goal

Restructure dossiers so the agents in this repo (catchup, slack-attack, weekly-overview) read a small, current-state document per client, with git as the event log. Make the daily routine substantially faster and cheaper, and rebuild every existing dossier once to shed accumulated errors and dead items.

## Constraints

- Readers are agents in this repo only. Optimise for them; repo-specific conventions live in the skills and `CLAUDE.md`, not in the dossiers.
- No writes outside this repo. `../VibePulse`, `../MahiProduct` and Slack are read-only sources. (Delivery to the private `#slack-attack` channel/canvases is the product and stays.)
- Don't store what one read can fetch: hosts, commercial terms, party names, contacts already in `../MahiProduct/wiki/people/`, Slack message text. Store the synthesis (expensive to recompute) plus pointers.

## Evidence behind the design (from repo history, 2026-10-14)

- 1,438 event-shaped entries; one incident per entry, so a topic fragments into many entries (amana: a dozen XAUUSD entries).
- 90 entries grew appended "YYYY-MM-DD update —" lines (42 with 2+): agents already want streams, the format forces a log.
- 604 `[open]` entries, ~50% with no mention in >45d of their own dossier's coverage. Open items only get revisited when their thread moves, so quiet ones never close.
- Active dossiers ~1.7MB (~426k tokens); 61% older than the unenforced 90d trim rule. Each catchup reads the whole file.
- Most post-launch fixes were date corruption (year-off). Fewer agent-written dates = less surface.
- `git log -L` can't follow an entry whose heading line changes (`[open]`→`[resolved]`); a stable heading fixes that.

## Dossier format

```markdown
---
slug: basemarkets
aliases: []                       # other slugs (billing etc.) mapping here
refs:                             # sources only — never copied into the body
  vibepulse: ../VibePulse/.claude/clients/basemarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: ../MahiProduct/wiki/clients/base-markets.md
channels:                         # resolved Slack IDs; catchup's read list
  internal-base-markets: C09D05EPCTV
  mahi-base-markets: C09D8V41JAG
contacts:                         # external people NOT in ../MahiProduct/wiki/people/
  - {name: "Alex", role: "Base Markets — primary contact (algo/flow)"}
last_catchup: 2026-10-14T09:00:57Z
status: active                    # or retired (+ retired_at, retired_reason)
---

## Now
≤4 lines. What matters with this client right now, written for the next agent.

## Streams

### tegis-api — Tegis direct integration
status: open · since: 2026-09-02 · last: 2026-10-14
State: Current state in 1–4 sentences, rewritten (not appended) every time the stream moves.
Next: What we're waiting on / who owes what. Omit if nothing.
Refs: https://mahifx.slack.com/archives/C09D8V41JAG/p1791952506021509 https://mahifx.slack.com/archives/…

## Arc
- 2026-06-29 — C Book with LMAX hedging live
- 2026-10-13 — Base decommissioned MT4
```

Rules:

- **Stream ID**: kebab-case, ≤24 chars, unique within the dossier, never renamed or reused. The `### <id> — <title>` line is the stable anchor; the title may be edited but the ID may not.
- **Meta line** (`status · since · last [· closed]`): `status` ∈ `open | watching | closed`. `since` = first Slack signal; `last` = latest Slack activity on the stream and must equal the date of a permalink in `Refs`. `closed: YYYY-MM-DD` added when status becomes `closed`.
- **State** is the current truth, rewritten in place. History of how it got here lives in git, not the body.
- **Refs**: 1–4 bare permalinks — origin and latest at minimum. Bare URLs (no markdown labels) to keep them greppable and cheap.
- **Ordering**: open streams first (most recent `last` first), then watching, then closed.
- **Arc**: one line per relationship-level milestone (go-live, decommission, contract change, key person change). Written when a significant stream closes or a milestone lands. Soft cap ~20 lines; when over, the catchup agent merges the oldest lines.
- **Size**: target ≤10KB; hard cap 20KB enforced at commit.
- No `Status`, `History`, `Recent issues`, `Notable topics`, or `key_people_overrides` sections. `channels_override` folds into `channels`.
- Channel dossiers (`channels/<name>.md`) use the same Now / Streams / Arc body; frontmatter keeps `channel_id`, `purpose`, `scope`.

## Stream lifecycle

- **New**: catchup creates a stream when a new topic appears that is notable per the existing notability rules. Before creating, check whether it belongs in an existing stream — prefer extending one over spawning a sibling.
- **Update**: any in-window activity → rewrite `State`/`Next`, bump `last`, swap the latest permalink in `Refs`.
- **Forced review (time as trigger)**: at each catchup, every `open` stream with `last` >30d before now must be explicitly decided: close (with reason in `State`) or downgrade to `watching`. Every `watching` stream with `last` >60d must be closed, or re-opened with a `Next:` naming a concrete pending action. The check script lists these; the agent decides.
- **Close (judgement)**: when the information is no longer current — resolved, superseded, abandoned. Final `State` says how it ended. If relationship-level, add an Arc line.
- **Merge**: absorbed stream is closed with `State: merged into <id>.`
- **Prune (mechanical)**: `scripts/prune-dossiers` deletes `closed` streams whose `closed` date is >14d old. Catchup runs it before every commit. The 14d lag lets the brief and weekly overview see closures in diffs; git keeps the text after.

## Git conventions

Catchup commit (subject unchanged, ≤72 chars):

```
chore(catchup): refresh basemarkets (2026-10-13..2026-10-14)

Window 2026-10-13T07:01:02Z..2026-10-14T07:02:11Z.
streams: tegis-api(updated) mt4-decom(new) xau-hedging(closed) xbt-cancels(pruned)
```

- `streams:` trailer lists every stream touched, with one of `new | updated | closed | merged>ID | pruned | watching`. Omit on probe-skip and quiet bumps.
- Stream history queries (documented in `CLAUDE.md`):
  - `git log --grep='tegis-api' -- clients/basemarkets.md` — every run that touched the stream.
  - `git log -L '/^### tegis-api /,/^### /:clients/basemarkets.md'` — how its text evolved.
  - `git log -S'### tegis-api ' -- clients/basemarkets.md` — find the commit that created/pruned it.

## Scripts

- **`scripts/check-dossiers`** (replaces `check-dossier-dates`; pre-commit runs it on staged dossiers):
  - Structure: required frontmatter keys; `## Now`, `## Streams`, `## Arc` present; each stream has a valid heading, meta line, `State:`, `Refs:` with ≥1 permalink.
  - Dates: `last` equals a cited permalink's UTC date (±1 day for timezone edges); `since` ≤ `last`; no date in the future. Keeps the year-off guard, now on two dates per stream instead of every entry.
  - IDs: unique; no stream that was `open`/`watching` in `HEAD` may disappear from the staged file (only `closed` streams can be removed).
  - Size: fail >20KB; warn >10KB.
  - `--stale` mode: list open streams with `last` >30d and watching >60d (non-blocking; for the catchup agent).
  - Legacy files (no `## Streams`) during migration: run only the old date check against them.
- **`scripts/prune-dossiers <files>`**: remove closed streams with `closed` >14d. Prints removed IDs for the commit trailer.
- **`scripts/rank-clients`**: unchanged behaviour; reads `channels`-era frontmatter without change (it only uses `last_catchup`, `status`, `aliases`). Gains `--due` to print only clients with `last_catchup` before today's UTC start.
- Tests: `scripts/tests/` with `unittest` fixtures for check and prune (`python3 -m unittest discover scripts/tests`).

## Skills

- **catchup**: rewritten around streams.
  - Reads `channels` from frontmatter (falls back to VibePulse + search only when bootstrapping or a channel is missing; writes the resolved ID back to frontmatter).
  - Keeps: bash-anchored dates, window sanity checks, 90d cap, cursor pagination, ambiguity expansion, cross-channel corroboration, notability rules.
  - New: forced stale review; prune before commit; `streams:` trailer; work budget (max ~3 pages per channel per 30d of window, max ~15 thread expansions) so one client can't stall a run.
  - Legacy conversion mode (temporary — removed once all dossiers are converted): if the dossier has no `## Streams`, treat the old content as leads, not facts; read Slack since `last_catchup`; verify each old `[open]`/`[watching]` item against its latest thread; write the new-format dossier from scratch (Write, not Edit). Old `History` and significant resolved entries become Arc lines. Commit subject `refactor(dossiers): convert <slug> to streams`; body lists streams created and old items dropped with a one-word reason (`resolved`, `stale`, `merged>ID`).
- **slack-attack**:
  - No-arg mode processes **all due clients** in one invocation: `rank-clients --due` → probe all → dispatch non-quiet catchups in waves of up to 6 parallel subagents → one globally ordered brief. Drop the 3-cap batches and continuation prompt.
  - Brief sources from each commit's diff + `streams:` trailer (replaces the diff-touch test: a stream is in the brief iff it's in the trailer).
  - Probe uses frontmatter `channels` directly.
- **weekly-overview**: enumerate the week's commits, group by `streams:` trailer IDs; a stream touched on 3+ days is a multi-day arc. Otherwise unchanged.
- **backfill**: removed. Arc replaces History; conversion seeds Arc from existing History/resolved entries.

## Routine (`slack-attack-daily`)

- Step 3 becomes a single `/slack-attack` invocation covering all due clients (no batch loop). Remove the per-batch capture/reorder instructions — slack-attack already returns one globally ordered brief.
- Run stats: count `streams:` trailer verbs instead of commit subjects.
- Everything else (canvas, message, Monday weekly, ntfy, `core.hooksPath`) unchanged.
- Push the updated prompt via `RemoteTrigger update` per `CLAUDE.md`; re-enable only after the conversion run lands.

## Other cleanup

- `.claude/docs/slack-conventions.md`: drop the channel-ID table (IDs live in dossiers); keep naming and skip-list conventions.
- `CLAUDE.md`: rewrite "Dossier discipline", layout, and setup sections for streams; add the git history queries; remove `/backfill`.
- Delete `todo.md` (items done or superseded).
- `clients/_template.md`, `channels/_template.md`: new format.

## Migration plan (the restart)

1. Land scripts, tests, skills, templates, CLAUDE.md (legacy mode enabled).
2. Convert one heavy (amana) and one light (axiory) dossier; review together before continuing.
3. Convert the rest via `/slack-attack` waves (each conversion is also the 58d catch-up). Must finish before ~2026-11-15, when 90d windows from 2026-08-17 start aborting.
4. Bootstrap `kama-capital`.
5. Remove legacy mode and the old date-check path; push; update and re-enable the routine.

## Out of scope

- Hard subagent timeouts (the Agent tool has none); mitigated by smaller dossiers and the catchup work budget.
- Writing to MahiProduct/VibePulse, or migrating content upstream.
- Cleaning up stale `origin/claude/epic-hawking-*` branches (separate one-liner).

## Success criteria

- Every active dossier passes `check-dossiers`, ≤20KB (most ≤10KB).
- No `open` stream with `last` >30d survives a catchup without an explicit decision.
- `git log --grep=<id>` reconstructs any stream's history.
- Full daily routine wall time well under the August 35–47 min (target ≤15 min on a typical day).
