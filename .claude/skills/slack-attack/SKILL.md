---
name: slack-attack
description: High-level brief across all clients (or one) read from existing dossiers. Surfaces top open issues, flags stale catchups, and gives Cameron a status snapshot without hitting Slack. Use when the user says "/slack-attack" or "/slack-attack <slug>".
---

A higher-level cousin of `/catchup`. Reads `clients/*.md` dossiers and produces a status brief. **No Slack calls** — this is a pure dossier read. Only as fresh as the last `/catchup`; that's the point.

## Resolving the target

- `/slack-attack` (no arg) → cross-client brief from every `clients/*.md` (skip `_template.md`).
- `/slack-attack <slug>` → single-client deep brief from `clients/<slug>.md`. If missing, suggest `/catchup <slug>` (which auto-bootstraps) and stop.

## Reading

For each dossier:

1. Parse frontmatter: `slug`, `last_catchup`, `refs`, `key_people_overrides`.
2. Resolve longer-term status:
   - If `refs.wiki` is set, read that wiki page. The wiki is canonical — extract `status` from frontmatter and the most relevant of `Current workstreams` / `Open items` / `Commercial state` / `Interaction history` for the brief. Ignore any `## Status` section in the dossier (warn it should be removed — wiki has taken over).
   - If `refs.wiki` is `null`, read the dossier's `## Status` section. If absent or empty, flag the client as "no longer-term status recorded — run `/catchup <slug>` to populate".
3. Parse `## Recent issues` blockquote entries. Each starts with `> [open|watching|resolved] YYYY-MM-DD — title`. Capture status, date, title, body, permalink(s).
4. Parse `## Notable topics` entries (no status markers).

Don't open Slack. Don't update `last_catchup` — this skill never edits dossiers. Wiki reads are read-only.

## Ranking

For the cross-client brief, score each client:

- `[open]` issue → high priority. Most recent first.
- `[watching]` → medium.
- `[resolved]` in last 14 days → low (mention only if the client otherwise has nothing).
- `Notable topics` entries → medium, treat like `[watching]`.

A client's headline is its most recent `[open]` issue, falling back to `[watching]`, then most recent `Notable topic`. Clients with nothing in any of those go to "Quiet".

Freshness flag:

- `last_catchup` within 7 days → fresh.
- `last_catchup` 7–30 days old → stale (mention age).
- `last_catchup` >30 days old or `null` → cold (mention prominently — dossier is likely missing recent activity).

## Output — cross-client (`/slack-attack`)

```
# Slack-attack brief — <today's date>

## Hot
Clients with [open] issues, most recent first.

- **<client>** (open since <date>) — <one-line summary of headline issue>. [permalink](...)
  <one extra line if there's a second open issue worth flagging>

## Watching
Clients with no [open] but live [watching] entries or active Notable topics.

- **<client>** — <one-line summary>. [permalink](...)

## Stale
Catchups >7 days old, ordered by age. These clients may have unsurfaced activity.

- <client> — last catchup <date> (<N>d ago)

## Cold
last_catchup >30d or null. Likely missing real state.

- <client> — <reason>

## Quiet
<comma-separated list of clients with no open/watching/topics and a fresh catchup>
```

Drop empty sections rather than printing "(none)".

## Output — single client (`/slack-attack <slug>`)

```
# <client> — slack-attack brief

last_catchup: <date> (<Nd ago, fresh|stale|cold>)

## Status
<from wiki when set (Stage / Active workstreams / Open items — distilled to ~3-5 lines), else from dossier's ## Status section, else "no longer-term status recorded".>

## Open
- [<date>] <title> — <body, kept tight>. [permalink](...)

## Watching
- [<date>] <title> — <body>. [permalink](...)

## Recently resolved
Last 2 [resolved] entries only, for context.

- [<date>] <title>. [permalink](...)

## Notable topics
- <topic line>. [permalink](...)

## Key people (slack-attack overrides only)
- <name> — <role> (<confidence>)

## Refs
- VibePulse: <path or "—">
- Wiki: <path or "not yet">
- Billing: <path>

## Suggestion
If stale/cold: "Run `/catchup <slug>` — last catchup was <Nd ago>."
Otherwise omit.
```

## Tone

Same as `/catchup`: terse, one reader (Cameron), no preamble. Lead with what's hot. Don't restate anything that lives in upstream refs (hosts, commercial terms, party names) — the dossier already follows that rule, so just don't expand.

If a dossier has no Slack-derived content at all (just refs and an empty body), say so in one line under the client's section rather than padding.

## What this skill does NOT do

- No Slack API calls. If Cameron wants fresh data, that's `/catchup`.
- No dossier edits. No `last_catchup` bump. Pure read.
- No bootstrapping missing dossiers — for cross-client mode, just skip-and-list any clients in VibePulse without a slack-attack dossier under a "## Unbootstrapped" section. For single-client mode, point at `/catchup <slug>` and stop.
