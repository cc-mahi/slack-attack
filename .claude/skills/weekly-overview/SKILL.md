---
name: weekly-overview
description: Weekly catchup overview. Synthesises a prose summary of the past week's catchup commits across all clients, written for Monday-morning reading. Use when the user says "/weekly-overview" or when the scheduled Monday routine fires.
---

`/weekly-overview` is a higher-level digest than the daily `/slack-attack` brief. It looks at what the daily catchups recorded across the past seven days and surfaces the major stories — the things worth carrying into the new week.

The reader is **Cameron Copland** (Slack `U099FA0D7CP`). Same audience and tone as `/slack-attack`: terse, no preamble, prose paragraphs, lead with what matters. The difference is scope and editorial weight — a week is longer than a daily window, so the overview prunes aggressively to the major stories rather than restating every per-client paragraph.

## Source

The overview sources strictly from this week's **catchup commits** on `main`. No fresh Slack pulls. The daily `/slack-attack` runs have already done the reading and the editorial first pass into the dossiers; this skill's job is to read across them and pick out what mattered.

1. Anchor the window from bash (see "Window-anchor sanity check" below). Default: the previous seven full days ending at today 00:00 UTC.
2. `git log --since="<window-start>" --until="<window-end>" --pretty=format:'%H %s' -- clients/ channels/` to enumerate the commits in scope.
3. For each commit, `git show <sha> -- clients/<slug>.md` (or the channel path) and extract what was added: new `Recent issues` entries, `Notable topics` entries, `[open]`→`[resolved]` promotions, summary refreshes, and any `key_people_overrides` additions. Ignore frontmatter-only `last_catchup` bumps — they're noise at the weekly level.
4. Group by slug. The result is "what each client recorded this week" — that's the editorial pool you then narrow.

If the window has zero substantive commits (only `last_catchup` bumps and quiet-window notes), the overview is one line ("Quiet week. No client recorded a notable story.") and you stop.

## What's "major"

Use editorial judgment — no rigid scoring rubric. Trust the daily catchups: they've already filtered for notability per their own rules (direct mentions, escalations, decisions, recurring issues). Your job is to read across clients and answer "what would I want a colleague to know about last week if they were back from leave."

Cues that something is major:

- **Relationship-shifting status changes** — go-live moved, contract movement, offboarding signal, integration milestone, churn risk.
- **Multi-day arcs** — the same issue or topic shows up across several commits in the week. One spike is a daily-brief paragraph; the same spike across three days is a weekly story.
- **Cross-client patterns** — if multiple clients hit the same LP issue, the same pricing-config tweak, the same infra change, name the pattern once at a higher level rather than repeating it per client.
- **Direct mentions of the user that haven't been actioned** — anything still hanging from `Action items` lines in the daily catchup outputs.
- **First-time signals** — new external contacts, a new integration mentioned, a new product topic that the dossier hadn't seen before.

Cues that something **isn't** worth elevating to the weekly:

- Routine LP / pricing / spread config changes that resolved cleanly inside the day they appeared.
- Single-thread incidents that resolved without follow-up.
- Quiet-week per-client paragraphs from the daily brief — by definition those don't escalate.
- Bot noise or deployment notifications that survived into a dossier entry.

If you're undecided about an item, leave it out. The overview is for the headline stories of the week; the daily briefs and dossiers carry the long tail.

## Output

Prose. Freeform. No fixed section structure, no per-client headers, no checklists. Read like a colleague's Monday-morning catch-up over coffee.

Open with a one-sentence shape-of-the-week if there's a dominant theme (a busy/quiet week, a thread that ran through multiple clients). Otherwise dive straight into the first story.

Then a small number of major-story paragraphs — typically 2–5. Each paragraph names the client(s) involved, what happened, and where it stands at the time of writing. Embed `[N]` inline references with bare URLs on the line directly under the paragraph, same convention as `/slack-attack`. **Numbering is per-overview** (a single global sequence top-to-bottom), not per-client — the reader is reading the overview as one narrative, not jumping between client sections.

If a story spans multiple clients, name them in one paragraph and use several `[N]` references for evidence from each. Don't split cross-client patterns into one paragraph per client — that defeats the point of zooming out.

Close with a brief tail only if there's a concrete forward-looking item from the week's commits — something pending an answer next week, a deadline, an action item carried over. If there's nothing concrete to flag, end with the last story; don't manufacture a sign-off.

Length is fuzzy: a busy week is ~4–5 paragraphs, a quiet week is one paragraph or a single line. Don't pad to hit a target.

Rules:

- **Every `[N]` URL must trace to a Slack permalink that appeared in this week's commits.** Same diff-touch principle as `/slack-attack`'s daily brief — overview content sources from this week's commits only, not from older dossier state. If a story arc began before the window but only escalated inside it, cite the in-window permalinks; you can mention the earlier event prose-wise without an `[N]` to it.
- **Bare URLs only.** No `[label](url)` markdown — the user's terminal can't open those.
- **No per-client checklists.** This is editorial prose, not a status report.
- **Don't restate things the daily brief already covered well** unless they grew into a multi-day story. The reader has already seen the daily briefs; the overview adds value by zooming out, not recapping.
- **Plain-English leads.** First sentence of every paragraph should make sense to someone who skipped the daily briefs. Acronyms can show up in the second clause once the topic is anchored, never as the lede.

## Window-anchor sanity check

Anchor every date to bash output, not your own reasoning — same year-off tripwire that catchup uses.

```
now_iso=$(date -u +%FT%TZ)
window_end_unix=$(date -u +%s)
window_start_unix=$((window_end_unix - 7 * 86400))
window_start_iso=$(date -u -r $window_start_unix +%FT%TZ)
window_end_iso=$(date -u -r $window_end_unix +%FT%TZ)
```

Sanity-check before reading any commits:

1. `window_end_unix - window_start_unix` must equal `7 * 86400` (± a few seconds). If it doesn't, abort.
2. `window_start_iso` and `window_end_iso` must both fall in the current calendar year you expect from `now_iso`. If either decodes a year off, abort — almost any year-off bug shows up here.
3. Before printing the brief, for every Slack permalink you cited (`[N]` URLs), decode the first 10 digits of `<TS>` in `/archives/<CID>/p<TS>` to Unix seconds and verify `window_start_unix - 60 ≤ entry_ts ≤ window_end_unix + 60`. If any cited permalink falls outside, drop the paragraph — don't paper over it by widening the language.

If any check fails, abort with one line per violation and stop. The reader sees the abort, not a corrupted overview.

## What this skill does NOT do

- Doesn't pull Slack. The daily catchups already did; the overview only reads commits.
- Doesn't edit dossiers. Read-only against the repo.
- Doesn't commit. The overview is a terminal output, not a durable artefact. (If you want to keep one, copy it into `~/repos/work-notes/` manually.)
- Doesn't replace the daily `/slack-attack` brief. The Monday routine runs the daily brief first, then the weekly overview immediately after — they're complementary.

## Tone

- Same as `/slack-attack` but more selective. A week is longer than a day, so the bar for "worth including" is higher.
- Past-tense for what happened, present-tense for what's still rough, future-tense for what's coming.
- Don't editorialise on speculation. If a story didn't conclude in the window, say so plainly.
- Don't address the brief to anyone but Cameron Copland (Slack `U099FA0D7CP`) — distinct from Cameron Hughes and others in `../MahiProduct/.claude/org-chart.md`.
