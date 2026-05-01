# slack-attack — instructions for Claude

Personal Slack catch-up tool for one reader (me). Two things live here:

1. **Client / channel dossiers** (`clients/<slug>.md`, `channels/<name>.md`) — Slack-derived state per target: `last_catchup`, `History` (long-horizon relationship arc), `Recent issues`, `Notable topics`, plus pointers to canonical data elsewhere. The dossier is the durable artefact and can be detailed / jargon-dense.
2. **Skills**:
   - **`/catchup <target>`** — worker. Pulls Slack since `last_catchup` and edits one dossier in place (Recent issues + Notable topics). Output is a structured confirmation, not a readable brief.
   - **`/slack-attack [slug]`** — reader-facing entrypoint. Dispatches `/catchup` in subagents (to keep main context clean), then synthesises a natural-language prose brief from the updated dossier(s) for me. With no slug it batches across active clients oldest-first, until the brief is substantial, then prompts to continue.
   - **`/backfill <slug>`** — one-shot lookback worker. Default 12m horizon; populates the dossier's `## History` section with the relationship arc. Suggests an extension run if older history is detected. Run once per client (or twice with `--since YYYY-MM-DD` to extend). Refuses if a wiki page exists upstream.

## Source-of-truth boundary

`../MahiProduct` and `../VibePulse` are canonical. **Don't duplicate what they already hold; don't edit them from here.** This repo is only for Slack-derived state and overrides.

| Want... | Look in... |
|---|---|
| Per-client hosts, Slack channels, Athena DBs, party names, distribution markets, LP FIX, LR rules | `../VibePulse/.claude/clients/{slug}.yaml` |
| Who's internal at Mahi (for the "Mahi staff aren't in `key_people`" rule) | `../MahiProduct/.claude/org-chart.md` |
| Client commercial terms, fees, contract dates | `../MahiProduct/data/billing/clients.json` |
| Per-env Graphite hosts, s3 slugs | `../MahiProduct/data/client-hosts.json`, `../MahiProduct/data/infra-hosts.json` |
| External contacts (client/prospect/vendor) | `../MahiProduct/wiki/people/` |
| Full client relationship state | `../MahiProduct/wiki/clients/{slug}.md` (exists for some; not yet for most brokers) |

Each dossier points at its refs via `refs:` in frontmatter. If a ref is `null`, the upstream doesn't cover it yet and slack-attack content is the effective source until it does. If an upstream disagrees with slack-attack, **trust the upstream** and remove the override here — unless the override is deliberate (note why).

Rules:
- Prefer writing to this project over `../MahiProduct/` or `../VibePulse/`.
- `key_people_overrides` holds only external contacts not yet in `../MahiProduct/wiki/people/`, plus low-confidence discoveries waiting for promotion.
- Don't re-state hosts, commercial terms, party names, or distribution markets in the dossier body — the refs are authoritative.
- The dossier's `## Status` section (Stage / Integration / Relationship) exists **only when `wiki: null`**. If a wiki page exists for the client, it is canonical for longer-term state and the dossier carries no Status section. When a wiki page later lands, delete the Status section and update the `wiki:` ref in the same change.
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

- `/catchup` applies changes and commits them itself (one commit per run, scoped to the dossier and any newly-cached channel ID). No review-then-commit step. Locally I `git pull`/inspect history to see what landed; remotely the routine pushes the commits at the end of the batch.
- `last_catchup` in frontmatter is the source of truth for "where did we leave off". Update it as part of the same `/catchup` edit.
- Keep dossier `Recent issues` reverse chronological, trim entries older than ~90 days. The dossier itself can be dense and detailed; readability is `/slack-attack`'s problem, not the dossier's.
- Use `Edit`, not `Write`, for dossier updates — keeps diffs small and readable.
- If a dossier doesn't exist for a client `/catchup` is asked about, auto-bootstrap a minimal one from the VibePulse yaml (hosts, slack channels) rather than blocking.

## Brief output (slack-attack)

The brief is for me, in the terminal. Prose paragraphs, not bullet checklists. Each claim that's grounded in a Slack thread gets a numbered bare-URL reference (`[N]` inline, URL on its own line below the sentence). Per-client numbering, resets at each client header. Bare URLs only — no labelled markdown links (Ghostty + my ctrl+space,space picker can't open those).

## Layout

```
clients/     per-client dossiers (_template.md is the schema)
channels/    per-channel dossiers for non-client channels
.claude/
  skills/
    catchup/       /catchup <target>            — worker, edits Recent issues + Notable topics
    slack-attack/  /slack-attack [slug]         — orchestrator + reader-facing brief
    backfill/      /backfill <slug>             — one-shot lookback, populates ## History
  docs/
    slack-conventions.md   channel patterns + skip rules
```

## Setup

After cloning, wire up the commit-msg hook:

```
git config core.hooksPath .githooks
```

Enforces conventional commits (`feat|fix|docs|chore|refactor|test|ci|build|perf|style|revert`), 72-char subject, no trailing period.
