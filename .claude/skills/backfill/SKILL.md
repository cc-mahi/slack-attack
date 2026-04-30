---
name: backfill
description: One-shot lookback worker. Pulls a long horizon (default 12m) from a client's Slack channels and populates the dossier's `## History` section with the relationship arc, major status changes, and stakeholder evolution. Use when Cameron says "/backfill <slug>" or "/backfill <slug> --since YYYY-MM-DD".
---

`/backfill` is the lookback worker. Where `/catchup` keeps the rolling 24h-since-last view fresh, `/backfill` does the one-shot wide-horizon read that establishes the relationship's history. Its product is the `## History` section in `clients/<slug>.md`. It's not a recurring flow — run once per client, twice if the first pass surfaces older history worth extending into.

## When to refuse

- `status: retired` in dossier frontmatter — emit one line and stop, same shape as `/catchup`.
- `wiki:` set on the dossier — `../MahiProduct/wiki/clients/<slug>.md` is canonical for relationship history. Refuse:
  ```
  backfill: <slug> — wiki page exists at <path>. History belongs there, not in the dossier.
  ```
- No slug — always required.

## Resolving the target

- If `clients/<slug>.md` doesn't exist, bootstrap it (same rules as `/catchup`'s bootstrap-a-client-dossier flow: copy `clients/_template.md`, fill `refs:`, leave `last_catchup: null`, leave `Recent issues` / `Notable topics` empty). Then continue into the History population.
- Channel scope: `channels_override` if set on the dossier, else VibePulse yaml's `slack:` block — **scan both** `internal` and `client`. The internal channel typically holds the load-bearing decisions and RCAs.

## Window

Default: 12 months back from today. Override with `--since YYYY-MM-DD` for an extension run (or any user-specified earlier boundary).

## Mining recipe

Two-prong: targeted keyword searches for high-signal events, plus chronological channel-reads at the boundaries for foundation/closing context. Plus billing JSON for commercial anchors.

### Keyword searches (parallel)

Run against both internal and client channels with `after:<window-start> before:<today>`, `sort=timestamp` ascending, `limit=20` (max). Use `slack_search_public_and_private` with `channel_types: "public_channel,private_channel"`.

Default starter set, by event category:

- **Incidents / RCAs**: `PagerDuty`, `"root cause"`, `incident`, `outage`, `crashed`
- **Go-lives / launches**: `"go live"`, `"go-live"`, `"soft launch"`, `launched`
- **Sunset / decommission**: `decommission`, `sunset`, `"winding down"`, `"shutting down"`
- **Migrations / cutovers**: `migration`, `cutover`, `handover`
- **Commercial**: `signed`, `addendum`, `licence`, `contract`
- **Onboarding**: `onboarding`, `pentest`, `kickoff`
- **Personnel**: `joined`, `"new starter"`, `"transitioning"`, `"taking over"`

These aren't exhaustive — they're starting points. **Follow the names that surface.** Once a domain-specific term appears (an LP, a project codename, an instrument, an internal product like `Compass` / `Modulus` / `Echo`), run targeted searches against it. The first batch tells you what to mine in the second.

For very busy clients (Pepperstone-shape), the 12m window may exceed the 20-result-per-search cap on common terms. Sub-divide: run the same query with three quarterly sub-windows (`after:<window-start> before:<window-start+3m>`, etc.) to paginate across time.

### Chronological channel-reads at the boundaries

`slack_read_channel` with `oldest=0` and `latest=<window-start + 30d>`, `limit=100`. This gives you the channel's earliest 100 messages — channel-creation context (why it was opened, who joined first), origin-story narrative that keyword searches miss because the seminal messages have no useful keyword.

If the channel pre-dates the window meaningfully, the latest-end of this read also overlaps your window-start, anchoring continuity.

### Billing / contract anchors

Read `../MahiProduct/data/billing/clients.json` for the entry matching the slug. Extract: `contractDate`, `latestAddendum` + `addendumDate`, `termExpiry`, `feeModel`, `fixedFeeUSD`, `discountNote`. These give exact commercial milestones that aren't always discussed in Slack.

## Detecting "more history available"

After populating History on a default 12m run, evaluate three signals to decide whether to suggest extending:

1. **Billing record older than window.** If `contractDate` is before window-start, more is available.
2. **In-window references to prior events.** Phrases like `"X years in the making"`, `"back in YYYY"`, `"when we onboarded"`, `"originally"`, `"the previous attempt"`, explicit pre-window dates.
3. **Channel activity dense at oldest boundary.** If the boundary channel-read shows substantive activity (not just channel-joins), the channel pre-dates the window.

If any signal fires, append after the dossier write:

```
History extends further back. Detected:
  - <one bullet per fired signal, with the concrete reference>

Run `/backfill <slug> --since <suggested-date>` to extend.
```

Default suggested `--since`: contract-date minus ~6 months, or the earliest in-window date reference, whichever is older.

If no signals fire, note "history likely complete back to <date>" in the run summary.

## Output — the `## History` section

Place it between the frontmatter (or `## Status` section if present) and `## Recent issues`.

### Structure

```markdown
## History

<Preamble: one or two lines naming the lookback boundary. Include billing anchors (contract date, latest addendum) if load-bearing.>

### <Optional subheading: themed era>

> YYYY-Q[1-4] or YYYY-MM-DD — Short title
> 1–4 lines of dense prose. Major status changes, configuration milestones, commercial events. Use exact dates where the source pins them; quarter-buckets where dates are fuzzy.

### Stakeholders gained over the relationship   (optional)

#### <Client name>

- **Name** — Role + how they showed up in the timeline.

#### Mahi

- **Name** — Role + how they showed up.
```

### Format rules

- **Dates.** Exact (`2025-07-16`) when the source pins it; quarter-precision (`2025-Q3`) when fuzzy. Don't fabricate.
- **No permalinks.** History is narrative, not anchored claim — `Recent issues` plays the anchor role for the rolling window.
- **Subheadings optional.** Use `###` to chunk multi-year arcs into legible eras (Origin → Onboarding → Product expansion → Current). Skip for histories with one coherent thread or short relationships.
- **Stakeholders subsection optional.** Include when the cast has materially changed; skip for short relationships where the client roster is static. Split client/Mahi only when both sides have evolved.
- **Density is fine.** Once-per-client artefact for a dense reader — pack the lines, don't pad them.
- **Don't restate upstream refs.** Current hosts, commercial terms, party names live in VibePulse / MahiProduct — reference them by name where they're load-bearing for an event ("3rd Addendum signed, $115k/m kicking in 2025-08-01"), but don't reproduce the full ref.

## Re-run behaviour

If `## History` already exists and `--since` is **older** than the existing preamble's lookback boundary:

1. Read the existing section.
2. Mine the new earlier window only (no need to re-mine what's already covered).
3. Prepend new entries, keeping the section in chronological order (earliest-first).
4. Update the preamble's lookback boundary.
5. Don't touch existing entries — Cameron's manual edits are sticky.

If `--since` is the same or newer than the existing boundary, no-op:

```
History already covers from <date>. Pass an earlier --since to extend, or delete the section to regenerate.
```

For a full regenerate, Cameron deletes the section first.

## Cost expectations

Backfill is heavy. A 12m run on a busy client = ~10–15 keyword searches + 1–2 channel reads + billing JSON parse + synthesis. Expect 60–180s per run. An extension to 36m roughly doubles it.

**Single-target only — no batched / parallel form.** Don't invoke from inside `/slack-attack`.

## What this skill does NOT do

- Doesn't touch `Recent issues` or `Notable topics` — that's `/catchup`'s territory.
- Doesn't bump `last_catchup` — that's `/catchup`'s job.
- Doesn't write to `../MahiProduct/wiki/`. If a wiki page exists, refuse — Cameron migrates the History content manually if he wants it upstream.
- Doesn't run on retired clients.
- Not part of `/slack-attack`'s rotation.
