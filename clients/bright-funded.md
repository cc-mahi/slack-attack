---
slug: bright-funded
aliases: [brightfunded]
refs:
  vibepulse: ../VibePulse/.claude/clients/brightfunded.yaml
  billing: ../MahiProduct/data/billing/clients.json
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: ../MahiProduct/wiki/clients/bright-funded.md
channels:
  internal-brightfunded: C084G40JXEE
  mahi-brightfunded: C08473TFD7Z
contacts:
  - {name: "Benjamin Galindo", role: "BrightFunded — primary client contact (product / new programs, payout data)", confidence: low}
  - {name: "Jelle Dijkstra", role: "BrightFunded — co-founder, led commercial renegotiation May 2026"}
  - {name: "Syb Dijkstra", role: "BrightFunded — co-founder, billing / user-count counterpart"}
  - {name: "Mio Knights", role: "BrightFunded — trading-surveillance and pricing requests", confidence: low}
  - {name: "Alfredo", role: "BrightFunded — joined channel 2026-10-07, raised GBPUSD Sunday-open abuse review", confidence: low}
  - {name: "Marcelo", role: "BrightFunded — picks up counterparty / free-account (F1KC) data pulls; surname unconfirmed", confidence: low}
last_catchup: 2026-10-15T13:00:34Z
status: active
retired_at: null
retired_reason: null
---

## Now
Healthy relationship; the live issue is commercial. Mahi proposed a $25k/mo fixed fee (Sep 2026), BF pushed back on 2026-10-06 that Mahi's measured payout reduction is below the proposed bill, and no agreement is visible. Sunday-open GBPUSD pricing was patched twice after a -$21k FI loss on 2026-09-20; BF accepted the fix. Monthly call cadence; Cameron Hughes is the day-to-day Mahi owner.

## Streams

### sunday-open-gbpusd — GBPUSD Sunday-open arbing and spread fixes
status: open · since: 2026-09-21 · last: 2026-10-09
State: On 2026-09-20 one counterparty hit GBPUSD two-way with IoC limits for ~35 min after the open and ended flat in profit (-$21k FI loss). Reference feeds were 15+ pips wide and disagreeing while Mahi quoted 0.1 pip. Fixes: SINGAPORE_MONDAY ladder widened (GBPUSD 4 pips, EURUSD 1, USDJPY 2) from 2026-09-29, then MWMS off Match-Trade on GBPUSD/EURUSD/USDJPY in ROLL/TWILIGHT/SNGMON (backtested). BF (Mio, Alfredo) raised the same pattern on 2026-10-07, agreed to discount the PnL, and approved a half-the-tightest-LP floor for GBPUSD which Cameron Hughes confirmed live on 2026-10-09. Isaac Dann also said Mahi will review spread benchmarking.
Next: BF to flag any recurrence; Mahi to watch the next few Sunday opens for regressions and PFM rank impact.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1789964773380629 https://mahifx.slack.com/archives/C08473TFD7Z/p1791366009839959 https://mahifx.slack.com/archives/C084G40JXEE/p1791453695129159 https://mahifx.slack.com/archives/C08473TFD7Z/p1791554147761909

### fixed-fee-proposal — Move to a fixed monthly fee
status: open · since: 2026-09-07 · last: 2026-10-06
State: After the 2026-09-01 call BF said they were happy to move to a fixed fee. Cameron Hughes proposed $25k/mo replacing $12k + $1/user, 12-month term, banded on funded volume ($25k up to 10bn then 32/40/48/56/65k). Andrew Morgan called the first draft too generous, noted BF historically signed $30k + 10% FI, and accepted ~$25k only with a growth ladder (free accounts counted 10:1) and the proposal redrafted as client-facing. A call with Syb was planned for 2026-09-29; its outcome is not in Slack. At the 2026-10-06 monthly call BF said the minimum measurable payout reduction is less than the proposed bill; Mahi replied it is only the easy-to-measure part and that the current price is far too cheap.
Next: Mahi to settle the growth metric and bands and respond; BF decision outstanding.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1788788372257979 https://mahifx.slack.com/archives/C084G40JXEE/p1789399062031249 https://mahifx.slack.com/archives/C084G40JXEE/p1789402518366149 https://mahifx.slack.com/archives/C084G40JXEE/p1791282278979729

### free-account-billing — Excluding free F1KC accounts from billing
status: open · since: 2026-06-01 · last: 2026-10-05
State: Free $1k Challenge (F1KC) accounts inflate the active-user count, so each month BF supplies a list of counterparties that only traded free accounts and Mahi excludes them. July came out 3,845 billable (of 32,887 raw), BF agreed on 2026-08-28; August 3,996 (of 51,695); September 4,196 (of 35,985), BF confirmed 2026-10-05 and Cameron Hughes forwarded to finance. The count depends on BF's monthly list each time; the fixed-fee proposal is meant to remove that dependency.
Next: BF supplies the October free-account list after month end; closes if the fixed fee lands.
Refs: https://mahifx.slack.com/archives/C08473TFD7Z/p1780330801690039 https://mahifx.slack.com/archives/C08473TFD7Z/p1787911173849309 https://mahifx.slack.com/archives/C08473TFD7Z/p1788341931661869 https://mahifx.slack.com/archives/C08473TFD7Z/p1791214982915359

### payout-reduction — Monthly payout data and value-add report
status: open · since: 2026-07-07 · last: 2026-10-06
State: Each month BF sends the funded-payout spreadsheet and Cameron Hughes returns payout-reduction estimates inside the monthly report or microsite. August data came 2026-09-01 (estimates added the same day); September data came 2026-10-06 ahead of the monthly call and the report went out after it. BF's reaction to the size of the reduction is tracked under fixed-fee-proposal.
Next: BF sends October payouts around the first week of November; Cameron Hughes asks ahead of the call.
Refs: https://mahifx.slack.com/archives/C08473TFD7Z/p1783419861147459 https://mahifx.slack.com/archives/C08473TFD7Z/p1788260805308349 https://mahifx.slack.com/archives/C08473TFD7Z/p1791277130717089 https://mahifx.slack.com/archives/C08473TFD7Z/p1791281722217399

### pfm-ranking — Prop Firm Match spread ranking
status: open · since: 2026-05-26 · last: 2026-10-06
State: BF's position in the Prop Firm Match spread table drives how tight Mahi quotes (the reason GBPUSD sits at 0.1 pip most hours). On 2026-10-01 Cameron Hughes noted BF was less often at the top, reduced MWMS and changed widening signal parameters, then reported "back to the top". On 2026-10-06 he flagged that the PFM spreads table looked broken. Tight quoting is a standing trade-off against Sunday-open and other arb exposure.
Next: none beyond monitoring.
Refs: https://mahifx.slack.com/archives/C08473TFD7Z/p1779793894044729 https://mahifx.slack.com/archives/C084G40JXEE/p1790867729276549 https://mahifx.slack.com/archives/C084G40JXEE/p1791300507287019

### sol-ref-selector — SOLUSD pricing freeze on Binance reconnect
status: watching · since: 2026-10-07 · last: 2026-10-07
State: Change record proposed switching SOLUSD referencePriceMarketSelectors from BINANCE|OKX to BINANCE|MATCH_TRADE so client pricing does not freeze when Binance reconnects, applied at pricer restart before 2026-10-08 05:00 UTC. The thread shows approval reactions; no confirmation of the restart or of outcome in window.
Next: Confirm SOLUSD no longer freezes; revert selector if BF sees a mid shift.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1791338442138609

### perps-interest — BF interest in perpetuals
status: watching · since: 2026-10-07 · last: 2026-10-07
State: At the monthly call BF raised the growth of perps and their interest in it. Cameron Hughes said Mahi can offer pricing for perps and the techniques apply equally; he flagged it as one to get ahead of for other props and prospects.
Next: Follow up with BF on scope if they pursue it.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1791385820262249

### instant-funding-sims — Instant Funding Challenge prop sims
status: closed · since: 2026-08-03 · last: 2026-08-27 · closed: 2026-10-15
State: Sims for the nine Instant Funding variants were delivered 2026-08-20. Jelle spotted a 0% pass rate on variants 1-8 caused by a payout-request modelling bug; Cameron Hughes fixed it and re-sent, and Jelle confirmed the numbers made sense on 2026-08-27. Delivered.
Refs: https://mahifx.slack.com/archives/C08473TFD7Z/p1785767012079019 https://mahifx.slack.com/archives/C08473TFD7Z/p1787821962680079

### coordinated-trading — Coordinated-trading detection reports
status: closed · since: 2026-05-08 · last: 2026-08-07 · closed: 2026-10-15
State: Mahi delivered roughly weekly correlation CSVs through 2026-08-07. No requests or deliveries appear in Slack after that (window to 2026-10-15), so the cadence either lapsed or moved elsewhere. The sub-account format refresh and the false-positive filter BF said they would define were never confirmed as landed. No activity since 2026-08-07; assumed lapsed. Reopen if BF asks again.
Refs: https://mahifx.slack.com/archives/C08473TFD7Z/p1779380274437499 https://mahifx.slack.com/archives/C08473TFD7Z/p1786118154883169

## Arc
- 2026-04-14 — New BF program launched using Mahi prop-sim pricing; pass rates tracked sim expectations
- 2026-05 — Commercial renegotiation led by Jelle Dijkstra; BF founders attended Mahi anniversary party
- 2026-06-10 — Futures prop sims delivered (Express / Standard plans)
- 2026-07-18 — Compass upgrade completed in a Saturday maintenance window
- 2026-08-04 — Call cadence moved from bi-weekly to monthly; BF announced Instant Funding Challenge plan and free $1k accounts
- 2026-08-28 — July billable users agreed at 3,845 after excluding free F1KC accounts
- 2026-09-14 — $25k/mo fixed-fee proposal drafted and reviewed internally
- 2026-09-20 — -$21k GBPUSD FI loss at Sunday open; fixes rolled out through 2026-10-09
