---
name: slack-attack
description: Orchestrator and reader-facing entrypoint. Runs /catchup against one or more clients (in subagents to keep main context clean), then synthesises a readable natural-language brief from the updated dossiers. Use when the user says "/slack-attack" or "/slack-attack <slug>".
---

`/slack-attack` is the entrypoint Cameron uses to actually catch up. It does two jobs:

1. **Dispatch catchup.** Decide which client(s) to refresh, then run `/catchup <slug>` for each — in **subagents**, so the Slack reads don't pollute the main thread.
2. **Read and synthesise.** After each catchup finishes, read the updated dossier and produce a readable natural-language brief for Cameron. Bullet checklists are out; prose paragraphs are in.

The brief is the product Cameron reads. The dossier is the durable artefact behind it.

## Resolving the target

- `/slack-attack <slug>` → refresh and brief one client.
- `/slack-attack` (no arg) → batched flow across active clients, oldest `last_catchup` first, until the brief is substantial. Then prompt to continue.

## Active-client enumeration

For the no-arg flow, the universe of clients is the union of:

- `clients/*.md` (excluding `_template.md`) — anything that already has a dossier here.
- `../VibePulse/.claude/clients/*.yaml` — anything VibePulse considers a client.
- `../MahiProduct/data/billing/clients.json` — anything billed.

If a client appears in VibePulse or billing but has no dossier, it's eligible — `/catchup` will bootstrap on first contact.

(Future: a `status: retired` flag in dossier frontmatter will exclude clients from rotation. Not implemented yet — manually skip if asked.)

## Ranking

Order by `last_catchup` staleness, oldest first. `null` (never caught up) sorts oldest-of-all. Ties broken alphabetically.

That's it for v1. Don't try to weight by activity, dossier volume, or pinning — staleness alone is enough until proven otherwise.

## Dispatching catchup

Run catchups in **subagents** so the Slack reads stay out of the main thread. Use the `Agent` tool with `subagent_type: general-purpose`. Each subagent's job is small and well-scoped:

> Run the `catchup` skill for slug `<slug>` and return the structured summary it produces. Use the Skill tool: `Skill(skill="catchup", args="<slug>")`. After it completes, paste the catchup summary verbatim and stop. Do not add commentary, do not produce a prose digest — that's the orchestrator's job.

Default to **serial** dispatch (one client at a time). Cameron sees streaming progress and Slack rate-limit risk stays low. Parallel is fine if you have a reason — clients are independent — but don't bother by default.

After each subagent returns, the dossier on disk has been updated. Read it directly to synthesise the prose.

## Reading the updated dossier

For each client just refreshed:

1. `git diff clients/<slug>.md` to see exactly what catchup added or changed in this run. This is the authoritative window — frontmatter timestamps can lie if a previous run got interrupted, but the diff doesn't.
2. Read the full dossier for context (existing `[open]` entries the brief should reference, `key_people_overrides` for names, refs).
3. If the diff is empty (catchup reported a quiet window), the brief for that client is one line — see "Quiet weeks" below.

## Output — single client (`/slack-attack <slug>`)

Natural-language prose with **numbered bare-URL references on their own line** after the sentence they support. Numbering is **per-client**, resets at each client header. References go inline as `[N]` in the prose, with the corresponding URL on the next line.

Length is fuzzy: a quiet window gets one paragraph (or a one-liner); a heavy week gets three or four. Don't pad.

```
**<client>**

<Lead paragraph: the shape of the window — what dominated, what shifted. Skip if quiet.>

<Body paragraphs: what's happening, what's still rough, what just closed. Use natural-language verbs ("hit a snag", "got closed", "is still being debugged") rather than status markers. Embed `[N]` references inline at each claim.>
[N] https://mahifx.slack.com/archives/.../p...
[N] https://mahifx.slack.com/archives/.../p...

<Forward-looking paragraph if there's something coming up worth flagging.>
[N] https://mahifx.slack.com/archives/.../p...
```

Rules:

- **Bare URLs only.** No `[label](url)` markdown — Cameron's terminal can't open those. URLs go on their own line directly under the sentence whose claim they support.
- **`[N]` references inline in the prose**, matched to the URL line below. Cameron uses these to refer back ("what's [3]?").
- **Per-client numbering**, resets at each client section in a multi-client brief. Cameron disambiguates by client header ("amana [3]").
- **No bullet checklists** of open/resolved. The prose verb tense already signals status; the dossier carries the structured list for anyone who wants it.
- **Don't restate upstream refs.** Hosts, commercial terms, party names, distribution markets live in VibePulse / MahiProduct. Reference them by name where needed but don't expand.

### Quiet weeks

If the catchup window produced no notable activity, the client's section is one line:

```
**<client>** — quiet. (Last catchup: <date>. Status unchanged.)
```

That's it — no padding, no numbered refs.

## Output — batched (`/slack-attack` no-arg)

Run the same single-client format for each client in turn. Concatenate them with a blank line between, oldest-staleness first.

Stop accumulating clients when the brief **feels substantial** — roughly three to five paragraphs of real content total, not counting one-liners for quiet clients. The judgement is fuzzy on purpose: one heavy client can be enough on its own; five quiet ones plus one busy one might also be a natural stop.

Hard cap: 5 clients per batch regardless of volume, so Cameron always gets a chance to react.

After the brief, append a continuation table:

```
---

Remaining (oldest catchup first):

| Client      | Last catchup     | Days  | Note                |
|-------------|------------------|-------|---------------------|
| axiory      | 2026-04-22       | 8d    |                     |
| pepperstone | 2026-04-25       | 5d    |                     |
| equiti      | (never)          | —     | bootstrap on first  |
| ...         | ...              | ...   |                     |

Continue with next batch? (y/n)
```

If Cameron says yes, run the next batch picking up where you stopped (re-rank by current staleness — some clients you just refreshed have moved to the bottom).

## Tone

- Cameron is the only reader. Terse, no preamble, lead with what's hot.
- Natural-language prose, not Slack-quote vocabulary. Embed technical names (instruments, LPs, counterparty IDs) inside sentences rather than chaining them as keywords.
- Past-tense for what happened, present-tense for what's still rough, future-tense for what's coming up. The verbs do the open/closed signalling — don't add markers.
- Don't editorialise. If a thread didn't conclude, say so plainly; don't speculate.

## What this skill does NOT do

- Doesn't pull Slack itself — that's catchup's job, run in a subagent.
- Doesn't edit dossiers — catchup handles all writes. slack-attack is read-only against `clients/*.md` (and read-only against the VibePulse / MahiProduct refs, always).
- Doesn't bump `last_catchup` — catchup does that.
- Doesn't produce structured bullet output — that's catchup's terminal output, intended for the subagent caller, not for Cameron.

## Constraints

- Never fabricate a Slack permalink. If catchup didn't surface one for a claim, either drop the claim or surface the parent claim with the link catchup *did* provide.
- One client section per `**<client>**` header. Don't merge clients into a single super-paragraph.
- If a client's diff is empty AND the dossier has no recent activity worth referencing, it's a quiet one-liner. Don't pad with old `[open]` items unless they flared in this window.
- Match the response length to the activity. Three sentences for a quiet client beats three paragraphs of restated old issues.
