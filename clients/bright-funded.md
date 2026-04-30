---
slug: bright-funded
aliases: [brightfunded]
refs:
  vibepulse: ../VibePulse/.claude/clients/brightfunded.yaml
  billing: ../MahiProduct/data/billing/clients.json
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Benjamin Galindo", role: "BrightFunded — primary client contact (product / new programs)", confidence: low}
  - {name: "Mio Knights", role: "BrightFunded — CC'd on weekly call coordination", confidence: low}
last_catchup: 2026-04-30T12:00:00Z
status: active
retired_at: null
retired_reason: null
---

## Status

- **Stage:** live
- **Integration:** prop firm running 2-Step (Bright + Classic) and 1-Step challenge programs on AWS eu-west-2; Mahi providing prop sims, skew + LR pricing, distribution via LDN.
- **Relationship:** healthy, bi-weekly call cadence with Cameron Hughes; client (Benjamin Galindo) actively engaging on prop sim outputs and a futures expansion ask.

## Recent issues

> [resolved] 2026-04-13 — log disk near-full from marketDataProxyTx spam
> Cameron Copland alerted on `/app/fx/log/mahifx` at 88% (and tickstore at 96%) on bright-funded-euwest2-prod-compass-1; Arun Patel matched the log spam pattern to a recent earlier incident, prescribed a rolling restart of `marketDataProxyTx*`. Restart done same hour, logs confirmed recovered. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1776092711480289)

> [resolved] 2026-04-13 — Benjamin Galindo locked out of admin tooling
> Client couldn't access (screenshot of error). Kate Stagg requested cookie clear, then IP whitelist for 94.204.181.52 once that didn't work; Kate confirmed whitelist request raised. No follow-up message confirms completion but no further complaints in window. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1776066492352719)

> [open] 2026-04-30 — futures prop sims for BrightFunded Futures launch
> On 2026-04-26 Benjamin specced four futures plans (A1/A2/B1/B2 — 6% PT with 4% or 3% MLL, EOD-trailing vs intraday-real-time-trailing drawdown, plus 25% / 40% consistency rule variants) and asked Cameron Hughes to replicate the existing 1-Step sim methodology. Cameron H confirmed feasible on 2026-04-27 and committed to a timeline. As of the 2026-04-30 bi-weekly the action item is still "give an ETA on the futures prop sims" — September is the outer deadline. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1777191630837849)

> [resolved] 2026-04-14 — new program launched off prop sim pricing
> Bi-weekly on 2026-04-14: client launched their new program the prior day, used the 2026-04-01 prop script results (2-Step Bright/Classic + 1-Step pass-rate + payout figures) to choose pricing. Happy with sim outputs; framing the prop script as useful for pricing future challenges. By 2026-04-30 bi-weekly Cameron H reports the new program is performing well, pass rates close to sim expectations and lower than the OG program, with LR changes recently improving execution across the board. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1776162017645809)

## Notable topics

- Bi-weekly client call cadence with Cameron Hughes; 2026-04-28 slot was missed (Cameron H had a clashing appointment), rescheduled to 2026-04-29. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1777370681451249)
- Prop simulation pipeline is now load-bearing for BrightFunded program design — sim outputs (with skew + LR assumed) are driving pricing decisions on both the existing 2-Step/1-Step and the upcoming Futures product. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1775056213954179)
