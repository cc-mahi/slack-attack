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
6. **New external people** — client-side names/handles that aren't in `key_people` yet. (Mahi staff names aren't tracked in `key_people`.)
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

- Add to `key_people`: {name: "...", role: "..."}
- Append to `Recent issues`:
  > [open] 2026-04-17 — <title>
  > <1–3 lines>. [permalink](https://mahifx.slack.com/archives/<CID>/p<TS>)
- Set `last_catchup: <now>`
- Flag for verification: <list any low-confidence entries already in the dossier>

Accept / edit / reject?
```

Wait for me to accept before writing changes. Apply with `Edit`, not `Write`.

## Dossier conventions

### `Recent issues` entries

Every entry starts with a status marker and cites at least one Slack permalink. No exceptions — if you don't have a real `message_ts`, search again with `response_format: "detailed"` to get one before proposing the entry.

```
> [open] YYYY-MM-DD — short title
> 1–3 lines. [permalink](https://mahifx.slack.com/archives/<CID>/p<TS>)
```

Markers:
- `[open]` — unresolved, awaiting action, still under discussion. **Also** active investigations with a plan (e.g. "hedger latency being tuned, further digging flagged").
- `[resolved]` — closed out (deployed fix, decision made, incident over).
- `[watching]` — passive observation of a pattern, no active work (e.g. "USDILS toxic flow, NY first-hour, cf. prior NZD/CHF"). If anyone is actively working on it, it's `[open]`, not `[watching]`. Use sparingly.

On each run, re-read any existing `[open]` entries whose threads had activity in the window; propose promoting them to `[resolved]` or updating the summary line. Don't silently flip markers — propose the change.

### `key_people` threshold

**Only external people** — client-side staff, consultants, LP/vendor contacts. **Never Mahi employees.** Mahi is small enough that I know everyone; roster entries for Mahi folks are noise. Mahi names still appear naturally in `Recent issues` and `Notable topics` prose when relevant ("Rory investigating", "Kate scheduling the meeting") — that's the right place for them.

Add someone only if role is known **and** you expect repeat interaction. One-off "new user added" events belong in `Recent issues`, not the people roster.

Entry shape:
```yaml
- {name: "...", role: "...", confidence: low}
```

- `confidence: low` — uncertain role spelling, contradictory signals, only seen once but plausibly recurring. The next `/catchup` flags these for verification.
- `confidence: high` is the default — omit the field.
- If two roster entries look like they might be the same person under different spellings, or the same role at different times, propose flagging one as `confidence: low` rather than silently keeping both.

Never inline `# comment` annotations into frontmatter — YAML parsers handle them inconsistently. Use fields.

## Constraints

- Keep the digest short. A dense 15-line digest beats a 200-line one I won't read.
- Never fabricate a Slack permalink. If you don't have a real channel ID + `message_ts`, re-search with `response_format: "detailed"` rather than omitting the link.
- If a channel has zero human messages in the window, say so in one line — don't expand it into a section.
- Leave empty dossier sections (`Recent issues`, `Notable topics`, etc.) blank — no `_None recorded._` or similar placeholders. `/catchup` appends cleanly when a section has content to add.
