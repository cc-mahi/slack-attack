---
name: catchup
description: Daily Slack catch-up digest. Reads activity since last_catchup for a client, a channel, or everything, summarizes notable items, and proposes dossier updates. Use when the user says "/catchup", "/catchup <slug>", or "/catchup #<channel>".
---

Produce a focused digest of Slack activity and suggest dossier updates. Never update dossiers without confirmation.

## Resolving the target

- `/catchup <slug>` → `clients/<slug>.md`. Channels to read = `channels.internal` + `channels.client` + `channels.other` from its frontmatter.
- `/catchup #<channel>` or `/catchup <channel-name>` → `channels/<name>.md` (create from template if missing, ask me for `purpose` first).
- `/catchup` (no arg) → scan all `clients/*.md` and `channels/*.md`; rank by `last_catchup` staleness × recent-message-count (quick `slack_search_public_and_private` with `after:` and `in:`); digest the top 3–5. Report which ones you skipped and why.

If a client dossier doesn't exist for `<slug>`, stop and suggest running `/seed-client <slug>` first.

## Reading activity

For each target channel:

1. Determine `oldest` = `last_catchup` if set, else 24h ago.
2. Resolve channel_id:
   - Prefer `channel_id` from `channels/<name>.md` frontmatter or the "Known channel IDs" table in `.claude/docs/slack-conventions.md`.
   - Else `slack_search_channels` with `channel_types: "public_channel,private_channel"`.
   - Record the ID back into `.claude/docs/slack-conventions.md` when you find one.
3. `slack_read_channel` with `oldest`, `limit: 100`. If the channel hit the limit, note it — there's more.
4. Group messages into threads. For threads that look notable (see below), `slack_read_thread` with the real `message_ts` (requires `response_format: "detailed"` when searching).

Skip channels matching the skip list in `.claude/docs/slack-conventions.md`.

## What counts as notable

In priority order:

1. **Direct mentions of me** (`<@U099FA0D7CP>`) or DMs.
2. **Questions awaiting a reply** — unanswered `?` messages, especially in threads I was in.
3. **Decisions** — "we're going to", "agreed", "let's do X".
4. **Escalations** — client dissatisfaction, outages, urgent language, mentions of specific incidents.
5. **Recurring issues** — topic already in the dossier's "Recent issues" that's flaring again.
6. **New people** — names/handles that aren't in `key_people` yet.
7. **Dossier-contradicting facts** — e.g. dossier says `status: live` but messages discuss churn/pause.

Routine bot pings, deployment notifications, and single-reaction chatter are not notable. Skip them silently.

## Output shape

```
# Catch-up: <target> — <ISO window>

## Notable
- <one bullet per item>. Permalink if available. Who/what/why-it-matters in one line.

## Action items (for me)
- Anything that needs my reply or decision.

## Quiet
<1-line summary of routine traffic — "~30 bot pings, 2 deploy notices, no human discussion">

---

## Proposed dossier updates (for clients/<slug>.md)

- Add to `key_people`: {name: "...", role: "...", org: client}
- Append to `Recent issues`:
  > 2026-04-17 — <title>
  > <1–3 lines>
- Set `last_catchup: <now>`

Accept / edit / reject?
```

Wait for me to accept before writing changes. Apply with `Edit`, not `Write`.

## Constraints

- Keep the digest short. A dense 15-line digest beats a 200-line one I won't read.
- Never fabricate a Slack permalink. If you don't have a real channel ID + `message_ts`, cite as `#channel — Author, YYYY-MM-DD` without a link.
- Don't guess at `key_people` orgs — if unclear whether someone is client-side or Mahi, leave `org: unknown` and flag it.
- If a channel has zero human messages in the window, say so in one line — don't expand it into a section.
