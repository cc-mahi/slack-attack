# slack-attack — instructions for Claude

Personal Slack catch-up tool for one reader (me). Two things live here:

## Who "me" is

The reader / user is **Cameron Copland** (Slack user ID `U099FA0D7CP`, email `cameron.copland@mahimarkets.com`). Mahi staff and roles live in `../MahiProduct/.claude/org-chart.md` — consult it before naming anyone in a brief. Distinct people the brief is **not** addressed to: **Cameron Hughes** (Analyst, client-facing — appears across many client RACI rows), **Liam Cordelle** (Cameron Copland's manager). Don't confuse the brief's audience with another Cameron, and don't refer to the user by anyone else's name.

1. **Client / channel dossiers** (`clients/<slug>.md`, `channels/<name>.md`) — Slack-derived **current state** per target, read by agents in this repo (not humans): `## Now` (≤4 lines), `## Streams` (one `### <id> — <title>` per ongoing topic with status/since/last, a rewritten State, Next, 1–4 permalinks), `## Arc` (one line per relationship milestone), plus pointers to canonical data elsewhere. Git is the event log; the dossier holds only what's current.
2. **Skills**:
   - **`/catchup <target>`** — worker. Pulls Slack since `last_catchup` and updates one dossier's Now / Streams / Arc in place and commits it. Output is a structured confirmation, not a readable brief.
   - **`/slack-attack [slug]`** — reader-facing entrypoint. Dispatches `/catchup` in subagents (to keep main context clean), then synthesises a natural-language prose brief from the updated dossier(s) for me. With no slug it processes every due client (scripts/rank-clients --due) in waves of six parallel catchups and produces one brief.
   - **`/weekly-overview`** — Monday-morning higher-level digest. Reads the past week's catchup commits across all clients and synthesises a prose summary of the major stories. No fresh Slack pulls; sources strictly from in-repo commits. Runs after the daily `/slack-attack` on Monday.

## Source-of-truth boundary

`../MahiProduct` and `../VibePulse` are canonical. **Don't duplicate what they already hold; don't edit them from here.** This repo is only for Slack-derived state and overrides.

| Want... | Look in... |
|---|---|
| Per-client hosts, Slack channels, Athena DBs, party names, distribution markets, LP FIX, LR rules | `../VibePulse/.claude/clients/{slug}.yaml` |
| Who's internal at Mahi (for the "Mahi staff aren't in `contacts`" rule) | `../MahiProduct/.claude/org-chart.md` |
| Client commercial terms, fees, contract dates | `../MahiProduct/data/billing/clients.json` |
| Per-env Graphite hosts, s3 slugs | `../MahiProduct/data/client-hosts.json`, `../MahiProduct/data/infra-hosts.json` |
| External contacts (client/prospect/vendor) | `../MahiProduct/wiki/people/` |
| Full client relationship state | `../MahiProduct/wiki/clients/{slug}.md` (exists for some; not yet for most brokers) |

Each dossier points at its refs via `refs:` in frontmatter. If a ref is `null`, the upstream doesn't cover it yet and slack-attack content is the effective source until it does. If an upstream disagrees with slack-attack, **trust the upstream** and remove the override here — unless the override is deliberate (note why).

Rules:
- Prefer writing to this project over `../MahiProduct/` or `../VibePulse/`.
- `contacts` (frontmatter) holds only external people not in `../MahiProduct/wiki/people/`.
- Don't re-state hosts, commercial terms, party names, or distribution markets in the dossier body — the refs are authoritative.
- Never write to `../MahiProduct/` or `../VibePulse/` — read-only sources. This repo is for individual use and writes nowhere else.
- **Retiring a client**: add `status: retired`, `retired_at: <ISO date>`, `retired_reason: <free text>` to the dossier frontmatter. `/slack-attack` and `/catchup` then skip it (no-arg flow silently; explicit-slug flow short-circuits with a one-line note). To re-activate, remove `status: retired` from frontmatter and run `/catchup <slug>` — that's the whole flow, no separate command.

## Tone

- The brief (slack-attack output) is for one reader (me). Natural-language prose, terse, no preamble, lead with what's new/important. No bullet checklists of open/resolved — verbs handle that ("hit a snag", "got closed", "is still being debugged"). Embed technical names inside sentences rather than chaining them as keywords.
- catchup's output (to its caller) is structured, not prose. The dossier is the artefact; the readable form is slack-attack's job.
- "Notable" means: direct mention of me (Slack user `U099FA0D7CP`), a question awaiting reply, a decision, an escalation, a recurring issue, or something that contradicts the dossier. Routine bot noise is not notable.

## Slack MCP conventions

- Use `mcp__claude_ai_Slack__slack_search_public_and_private` with `channel_types: "public_channel,private_channel"` — many relevant channels are private.
- Use `slack_read_channel` (not search) when you need "everything since timestamp X" for a known channel — search has indexing lag.
- Use `slack_read_thread` with the real `message_ts` (requires `response_format: "detailed"`) to read thread replies.
- Skip channels: `*-notifications`, `*-bridge-alerts`, `#frontoffice-alerts`, `#dev-alerts`, `#dev-commits`, `#dev-status`. See `.claude/docs/slack-conventions.md`.
- Slack permalinks: `https://mahifx.slack.com/archives/<CHANNEL_ID>/p<TS_WITHOUT_DOT>`. Never fabricate — only construct from real result data.

## Dossier discipline

Format contract: `docs/superpowers/specs/2026-10-14-stream-dossiers-design.md`; enforced by `scripts/check-dossiers` (pre-commit). The `catchup` skill holds the working rules.

- `/catchup` edits one dossier and commits it itself, with a `streams:` trailer listing every stream touched (`new | updated | closed | watching | merged>ID | pruned`).
- Streams are rewritten in place, never appended to. Stream IDs are permanent. Open streams quiet >30d (watching >60d) must be explicitly reviewed each catchup. Closed streams are pruned by `scripts/prune-dossiers` 14 days after closing.
- `/slack-attack` probe-skips clients with zero human messages since `last_catchup`, committing `chore(catchup): bump <slug> (probe-skip, no activity)`.
- `last_catchup` is the source of truth for where we left off. Catchup refuses windows >90 days, so a client left untouched for 90 days needs a manual reset.
- Don't store anything one read of VibePulse / MahiProduct / Slack returns; store the synthesis plus permalinks.
- Bootstrap: `/catchup <slug>` creates a missing dossier from the template.

### Stream history

- `git log --grep='<id>' -- clients/<slug>.md` — every run that touched a stream.
- `git log -L '/^### <id> /,/^### /:clients/<slug>.md'` — how its text evolved.
- `git log -S'### <id> ' -- clients/<slug>.md` — when it was created / pruned.

## Brief output (slack-attack)

The brief is for me, in the terminal. Prose paragraphs, not bullet checklists. Each claim that's grounded in a Slack thread gets a numbered bare-URL reference (`[N]` inline, URL on its own line below the sentence). Per-client numbering, resets at each client header. Bare URLs only — no labelled markdown links (Ghostty + my ctrl+space,space picker can't open those).

## Brief output (slack-attack daily routine → Slack)

There's also a remote routine — `slack-attack-daily` — that runs the daily flow unattended on weekdays and posts the result to a private Slack channel (`#slack-attack`, channel_id `C0B5V56QACQ`). It maintains **two rolling canvases**:

- **Daily brief canvas** (`F0B4WEV00DV`) — rewritten each weekday morning with the full prose brief (headline summary, per-client sections, quiet/unprocessed lines, run-stats footer).
- **Weekly overview canvas** (`F0B55HJ7M7V`) — rewritten Monday mornings with the prose digest from `/weekly-overview`.

Each run posts one short summary message to the channel that links to the canvas plus a glance-level headline. Mondays add a second short message for the weekly canvas. An ntfy push fires after delivery so the channel update actually notifies (Slack doesn't notify on self-authored messages).

When the routine writes prose to a canvas it converts the skill's `[N]` + bare-URL refs into inline embedded links `[\[N\]](url)`. Bare URLs are the format for the **local terminal** brief only (Ghostty + my link picker need them); canvases land in Slack where embedded is neater.

## Remote routines

Routine prompt bodies are tracked in this repo under `.claude/routines/<name>.md` so changes are diffable in git. The file in git is the source of truth; the remote routine body is a deploy target. After editing a routine file, **push the body to the remote routine** so the next scheduled fire picks it up:

1. Read the routine file. Frontmatter has the `trigger_id`.
2. Fetch the current remote body with `RemoteTrigger get` (so you can preserve the rest of `job_config` while replacing just the prompt content).
3. `RemoteTrigger update` with a body that mirrors the existing `job_config`, replacing only `events[0].data.message.content` with the new prompt body (everything below the frontmatter and intro paragraph in the routine file).
4. Confirm by re-fetching and diffing.

Don't drop or edit other fields (cron, environment, MCP connections, etc.) unless that's the intent of the change.

## Layout

```
clients/     per-client dossiers (_template.md is the schema)
channels/    per-channel dossiers for non-client channels
scripts/     dossierlib.py, check-dossiers, prune-dossiers, rank-clients; tests in scripts/tests/
.claude/
  skills/
    catchup/          /catchup <target>         — worker, updates one dossier's streams + commits
    slack-attack/     /slack-attack [slug]      — orchestrator + reader-facing brief
    weekly-overview/  /weekly-overview          — Monday prose digest from the week's streams: trailers
  routines/
    slack-attack-daily.md   prompt body for the daily remote routine (push to remote after editing)
  docs/
    slack-conventions.md   channel patterns + skip rules
```

## Setup

After cloning, wire up the git hooks (one command enables both):

```
git config core.hooksPath .githooks
```

- **`commit-msg`** — enforces conventional commits (`feat|fix|docs|chore|refactor|test|ci|build|perf|style|revert`), 72-char subject, no trailing period.
- **pre-commit** — runs scripts/check-dossiers --staged: stream format, 20KB cap, stream-ID stability, and the year-off date guard. Tests: python3 -m unittest discover -s scripts/tests.

**The remote `slack-attack-daily` routine's checkout must also have `core.hooksPath=.githooks` set**, or the pre-commit guard won't fire there — and the routine is exactly where the corruption has been landing.
