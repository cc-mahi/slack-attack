---
name: slack-attack
description: Orchestrator and reader-facing entrypoint. Runs /catchup for every due client (or one slug) in parallel subagents, then synthesises a readable natural-language brief from the resulting commits. Use when the user says "/slack-attack" or "/slack-attack <slug>".
---

`/slack-attack` is what the user runs to catch up, and what the daily routine runs once per weekday. It:

1. **Dispatches catchup** for the target client(s) in **subagents**, so Slack reads stay out of the main thread.
2. **Synthesises a brief** from what each catchup committed. Prose, not checklists.

The brief is the product the user reads; dossiers are the durable state agents read.

## Who the brief is for

**Cameron Copland** (Slack `U099FA0D7CP`) — not Cameron Hughes (Analyst) or anyone else in `../MahiProduct/.claude/org-chart.md`.

## Targets

- `/slack-attack <slug>` → one client.
- `/slack-attack` → every **due** client: `scripts/rank-clients --due` (never-caught-up first, then oldest `last_catchup`). Don't reimplement the parse — the script handles frontmatter, aliases, billing and retired filtering.

Retired clients are excluded by the script. For `/slack-attack <slug>` on a retired client, print one line and stop:

```
<slug> — retired since <retired_at> (<retired_reason>). Edit frontmatter to re-activate.
```

## Probe-skip pre-flight

Most clients are quiet most days; a subagent just to discover that is the dominant waste. For each candidate:

1. Read frontmatter: `last_catchup`, `channels`. If `last_catchup` is null, the dossier lacks `## Streams` (legacy), or it has no `channels:` → **don't probe**; dispatch.
2. For each channel ID in `channels` (minus the skip list in `.claude/docs/slack-conventions.md`): `slack_read_channel(channel_id, oldest=<last_catchup unix>, limit=20)`. On any API error → dispatch.
3. Count messages with neither `subtype` nor `bot_id` set.
4. Total 0 → probe-skip; otherwise dispatch.

Probe-skip action (the only dossier write this skill makes): edit the `last_catchup:` line to the current UTC ISO time (from `date -u +%FT%TZ`), then

```bash
git add clients/<slug>.md && git commit -m "chore(catchup): bump <slug> (probe-skip, no activity)"
```

Retry on `.git/index.lock` (sleep 3, up to 5 times). Known acceptable miss: a notable bot-only message — alert channels are on the skip list anyway.

## Dispatch

Print one line up front: which slugs are dispatched, which probe-skipped.

Dispatch in **waves of up to 6** parallel subagents: all Agent calls for a wave in a single message, foreground (no `run_in_background` — background subagents previously returned before doing any work). `subagent_type: general-purpose`, `model: sonnet`. Prompt:

> Working directory: <repo root>. Run the `catchup` skill for `<slug>`: `Skill(skill="catchup", args="<slug>")`, following it exactly. Other catchups are committing to this repo in parallel; retry on `.git/index.lock` as the skill says. When done, paste the catchup output verbatim and stop. No prose digest.

Wait for the wave to finish, then dispatch the next. When all waves are done, synthesise.

If a subagent returns an ABORT or no `Commit:` line, record its output verbatim for the brief's failures paragraph; don't retry in this run.

## Reading results

For each dispatched client, from the subagent's `Commit:` SHA:

1. `git show <sha> --format=%B -s` → the `streams:` trailer: the **complete list** of what the brief may cover for that client.
2. `git show <sha> -- clients/<slug>.md` → the diff: the new State / Next / Refs for each listed stream, and Now/Arc changes.
3. Streams not in the trailer are **silent** in the brief, however open or recent.
4. Legacy conversions (`refactor(dossiers): convert …`) rebuild the whole file: brief only from the streams whose `last` falls inside the reported window, plus one sentence on the conversion itself (streams created, entries dropped as stale).

## Window-anchor sanity check

Use only the window the subagent reported (not your own date math, not the bumped `last_catchup`). For every permalink you cite as `[N]`, decode the first 10 digits of `p<TS>` to Unix seconds; it must be ≥ `window_oldest_unix - 60`. A link outside the window means drop the paragraph.

## Output

Per client, natural-language prose with numbered **bare-URL** references, one paragraph per stream that matters:

```
**<client>**

<Lead: the shape of the window — what dominated. Skip if one stream.>

<One paragraph per stream: who/what/status in plain English, then detail. [N] inline.>
[N] https://mahifx.slack.com/archives/.../p...
```

Rules:

- **One stream per paragraph.** Don't chain unrelated topics with "meanwhile".
- **Plain-English lead.** The first sentence of each paragraph must make sense to someone away for a week: who, what, status. Acronyms only after the topic is anchored, with the surrounding words making their role legible ("the LR throttle on B_CLIENTS_RA").
- **Status through verbs**, not markers: "got closed", "is still being debugged", "is waiting on Gerard".
- **Closed streams** get one sentence ("the MT4 bridge question closed when Base confirmed decommission").
- **Bare URLs only**, each on its own line under its paragraph. `[N]` inline. Numbering resets per client.
- **Don't restate upstream refs** (hosts, commercial terms, party names).
- Test: read each paragraph's first sentence in order — that alone should give the shape of the day.

Multi-client: order client sections by **significance**, not staleness — direct mentions of the user, escalations and real decisions first. Low-key clients get one short paragraph mid-brief. Truly quiet clients (probe-skipped or quiet window) collapse into one final line:

```
Quiet today (N): slug, slug, ...
```

Then, if any subagent aborted or failed, a closing paragraph with their output verbatim.

## Tone

Terse, no preamble, lead with what's hot. Past tense for what happened, present for what's still rough, future for what's coming. Don't speculate past what the thread says.

## What this skill does NOT do

- Pull Slack for content (the probe only counts messages).
- Edit dossier bodies — catchup owns them. The only write is the probe-skip `last_catchup` bump.
- Write outside this repo, or push (the routine pushes).

## Constraints

- Never fabricate a permalink; cite only links present in the commit diff.
- Every paragraph traces to a stream in that commit's `streams:` trailer.
- Match length to activity.
