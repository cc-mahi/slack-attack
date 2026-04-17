# slack-attack — instructions for Claude

Personal Slack catch-up tool + client reference. See `README.md` for the concept.

## Tone

- Digest output is for one reader (me). Be terse, skip preamble, lead with what's new/important.
- "Notable" means: direct mention of me (Slack user `U099FA0D7CP`), a question awaiting reply, a decision, an escalation, a recurring issue, or something that contradicts the dossier. Routine bot noise is not notable.

## Slack MCP conventions

- Use `mcp__claude_ai_Slack__slack_search_public_and_private` with `channel_types: "public_channel,private_channel"` — many relevant channels are private.
- Use `slack_read_channel` (not search) when you need "everything since timestamp X" for a known channel — search has indexing lag.
- Use `slack_read_thread` with the real `message_ts` (requires `response_format: "detailed"`) to read thread replies.
- Skip channels: `*-notifications`, `*-bridge-alerts`, `#frontoffice-alerts`, `#dev-alerts`, `#dev-commits`, `#dev-status`. See `.claude/docs/slack-conventions.md`.
- Slack permalinks: `https://mahifx.slack.com/archives/<CHANNEL_ID>/p<TS_WITHOUT_DOT>`. Never fabricate — only construct from real result data.

## Dossier discipline

- `/catchup` applies changes directly — I review via `git diff` and commit when happy. No accept step.
- `last_catchup` in frontmatter is the source of truth for "where did we leave off". Update it as part of the same `/catchup` edit.
- Keep the prose sections short. `Recent issues` is reverse chronological, trim entries older than ~90 days.
- Use `Edit`, not `Write`, for dossier updates — keeps diffs small and readable.
