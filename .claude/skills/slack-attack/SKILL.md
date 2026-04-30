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

## Active-client enumeration and ranking

Run `scripts/rank-clients` from the repo root. It enumerates the union of `clients/*.md`, `../VibePulse/.claude/clients/*.yaml`, and `../MahiProduct/data/billing/clients.json`, and returns tab-separated rows sorted oldest-`last_catchup`-first (with never-caught-up clients sorted to the very top, since they're effectively the most stale):

```
slug    last_catchup    days_since    note
```

- `last_catchup`: ISO string from frontmatter, or `never`.
- `days_since`: integer with `d` suffix, or `—` for `never`.
- `note`: `bootstrap` if there's no local dossier yet (catchup will create one on first contact), else blank.

Take the top N rows (start with N=3; that's also the hard cap on a batch). **Do not reimplement the parse inline** — the script handles frontmatter parsing, retired-client filtering, billing JSON shape, and date arithmetic in one place. Past attempts at inline shell hit zsh's reserved `status` variable and JSON-shape mismatches; that's why the script exists.

Retired clients (`status: retired` in dossier frontmatter) are excluded by default — the script handles this. They're silently dropped from the no-arg rotation and never appear in the continuation table. Pass `--include-retired` only for ad-hoc inspection.

If Cameron runs `/slack-attack <slug>` against a retired client, **short-circuit**: print one line and stop, no subagent, no Slack pull.

```
<slug> — retired since <retired_at> (<retired_reason>). Edit frontmatter to re-activate.
```

Re-activating is a deliberate edit: remove `status: retired` from frontmatter, then run `/catchup <slug>` normally. Don't try to make slack-attack do it for him.

That's the ranking — staleness alone, no activity weighting or pinning. If that proves wrong over time, change the script, not the skill.

## Dispatching catchup

Run catchups in **subagents** so the Slack reads stay out of the main thread. Use the `Agent` tool with `subagent_type: general-purpose` and `model: sonnet` — catchup is mechanical Slack-reading and dossier editing, doesn't need Opus, and Sonnet runs cheaper and faster in parallel. The orchestrator (this skill, doing synthesis) stays on whatever model the parent thread is on. Each subagent's job is small and well-scoped:

> Run the `catchup` skill for slug `<slug>` and return the structured summary it produces. Use the Skill tool: `Skill(skill="catchup", args="<slug>")`. After it completes, paste the catchup summary verbatim and stop. Do not add commentary, do not produce a prose digest — that's the orchestrator's job.

Dispatch is **parallel in the foreground**. The loop is:

1. Pick the top N clients from `scripts/rank-clients` (N ≤ 3 hard cap; fewer if there are fewer to do).
2. Dispatch all N catchup subagents at once — make N Agent tool calls **in a single message**, no `run_in_background` flag. The harness runs them concurrently in the foreground. (Print a single up-front line listing the N slugs so Cameron knows what's running; per-dispatch lines aren't shown anyway.)
3. Wait for all subagents to return. The orchestrator's main thread blocks until every one is done.
4. Once all returns are in, synthesise each client's section in turn — `git diff clients/<slug>.md`, full dossier read, prose paragraph(s), URL refs — and print as you go. With ~3 clients and ~5s synthesis each, the printing stage takes ~15s after the last subagent lands.
5. After the last section prints, print the continuation table.

Total wall time ≈ slowest-individual catchup + N × ~5s synthesis. With 3 catchups averaging 60–90s each, expect ~1.5 minutes end-to-end — versus 3–5 minutes if dispatched serially.

Trade-off versus true streaming: Cameron doesn't see prose appear as each catchup individually completes; he sees nothing until all N return, then a burst of synthesised sections. We accepted this because the prior attempt at parallel-background streaming (`run_in_background: true`) had the subagents return in 7–9s with only their opening narration as "result" — i.e. they bailed before doing any real work. Foreground parallel is documented to run concurrently and was empirically fine in serial form (the working serial-with-streaming runs in commits `a455cbb` / `b34c56f`); we keep that working dispatch shape and only add the multi-call-in-one-message wrapper.

Slack rate limits: tier-3 endpoints (`conversations.history`, `search.messages`) are typically lenient enough for 3-way concurrency. If you hit a 429, the subagent will surface it in its return; treat it as a bug to revisit rather than pre-throttle for.

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

- **One issue per paragraph.** Don't chain multiple distinct events into a single wall-of-text paragraph just because they all happened in the window. Each `[N]` reference belongs to its own short paragraph — typically a lead sentence, then one or two of supporting detail, then the URL line. If you find yourself joining two unrelated topics with "; meanwhile…" or "the same evening…", break the paragraph instead.
- **Plain-English lead.** The first sentence of each paragraph must be readable by someone who's been away from the desk for a week. Lead with the human shape — *who, what, status* — not internal jargon. ❌ "Erik reckons it's the expected LR effect plus LL PnL we recapture (PI is off on Radex's FX-crosses execution rules)" — opaque without prior context. ✅ "Radex (client) flagged slippage on three FX crosses; our take is it's expected behaviour from how we throttle pricing, and a sample trade actually netted us PnL despite the apparent loss." Acronyms can show up in the second clause once the topic is anchored, but never as the lede.
- **Glossary discipline.** When you use a Mahi-internal acronym (LR, LL, PI, PnL recapture, B_CLIENTS_RA, MAHI_CONTINUITY_NYC, etc.), the surrounding sentence should make the *role* of that thing legible — even if Cameron doesn't recall the exact definition cold. "the LR throttle on B_CLIENTS_RA" beats "LR on B_CLIENTS_RA" because the word *throttle* anchors the meaning. The dossier carries the deep technical detail; the brief gives Cameron enough to know whether to click the link.
- **Active voice, status via verbs.** "Radex flagged slippage." "We closed the XAGUSD spike." "The execution-rule flag is still under discussion." Past tense for what happened, present for what's still rough, future for what's coming. Don't add `[open]`/`[resolved]` markers; the verbs do that work.
- **Bare URLs only.** No `[label](url)` markdown — Cameron's terminal can't open those. URLs go on their own line directly under the paragraph that supports them.
- **`[N]` references inline in the prose**, matched to the URL line below. Cameron uses these to refer back ("what's [3]?").
- **Per-client numbering**, resets at each client section in a multi-client brief. Cameron disambiguates by client header ("amana [3]").
- **No bullet checklists** of open/resolved. The prose verb tense already signals status; the dossier carries the structured list for anyone who wants it.
- **Don't restate upstream refs.** Hosts, commercial terms, party names, distribution markets live in VibePulse / MahiProduct. Reference them by name where needed but don't expand.

Test for whether the brief is working: read the first sentence of each paragraph aloud, in order. If that read alone tells Cameron the shape of the window — what's hot, what closed, what's pending — the brief is good. If it's just a list of acronyms strung together, rewrite.

### Quiet weeks

If the catchup window produced no notable activity, the client's section is one line:

```
**<client>** — quiet. (Last catchup: <date>. Status unchanged.)
```

That's it — no padding, no numbered refs.

## Output — batched (`/slack-attack` no-arg)

Per-client sections are printed **after all subagents have returned** (see "Dispatching catchup"). With foreground-parallel dispatch the orchestrator can't synthesise mid-batch — it has to wait until the slowest one finishes — and then it prints sections back-to-back in staleness-rank order (oldest-staleness first), one paragraph per topic per client.

Batch size: pick the top N from `scripts/rank-clients`, capped at 3. All N are dispatched in parallel up front; there's no mid-batch stopping rule (with parallelism, the cost is fixed once dispatched, so let them all complete and print).

After the last section prints, append the continuation table:

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
