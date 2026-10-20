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
last_catchup: 2026-10-20T07:16:32Z
status: active
retired_at: null
retired_reason: null
---

## Now
Healthy relationship; the live issue is commercial. Mahi proposed a $25k/mo fixed fee (Sep 2026), BF pushed back on 2026-10-06 that Mahi's measured payout reduction is below the proposed bill, and no agreement is visible. Sunday-open GBPUSD pricing was patched three times after a -$21k FI loss on 2026-09-20 (ladder, MWMS, half-tightest-LP floor live 2026-10-09); BF approved each and agreed to discount the PnL. Monthly call cadence; Cameron Hughes is the day-to-day Mahi owner.

## Streams

### fixed-fee-proposal — Move to a fixed monthly fee
status: open · since: 2026-09-07 · last: 2026-10-06
State: BF currently pays $12k + $1/user (~$15.5-16.2k/mo, trending down; users vs accounts was fought and lost in Dec 2025, billed on distinct counterparty since, with Syb open to renegotiating). After the 2026-09-01 call BF said they were happy to move to a fixed fee and Syb chased on 2026-09-08. Cameron Hughes proposed $25k/mo replacing it, 12-month term, banded on funded volume ($25k up to 10bn then 32/40/48/56/65k); sizing is ~$3,250 per funded bn at $25k vs Fintokei ~$3,700 ($50k) and FundingPips ~$560 ($60k), so $25-30k is "same rate as the network". Andrew Morgan called the first draft too generous: wants a reset toward network fair value (staged if needed), growth triggers (tier steps on active challenges, extra for new asset classes/sims), user definition left settled, and a pre-agreed mandate, floor and walk-away; he accepts ~$25k only with a growth ladder (free accounts counted 10:1) and a client-facing redraft. Cameron Hughes' worry is BF drops the fixed bill if the figure is well above expectation. Call with Syb planned for 2026-09-29 (Dubai week); its outcome is not in Slack. At the 2026-10-06 monthly call BF said the minimum measurable payout reduction is less than the proposed bill; Mahi replied it is only the easy-to-measure part and that the current price is far too cheap.
Next: Mahi to settle the growth metric and bands and respond; BF decision outstanding.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1788788372257979 https://mahifx.slack.com/archives/C084G40JXEE/p1788944104228899 https://mahifx.slack.com/archives/C084G40JXEE/p1789402518366149 https://mahifx.slack.com/archives/C084G40JXEE/p1791282278979729

### free-account-billing — Excluding free F1KC accounts from billing
status: open · since: 2026-06-01 · last: 2026-10-05
State: Free $1k Challenge (F1KC) accounts inflate the active-user count, so each month BF supplies a list of counterparties that only traded free accounts and Mahi excludes them. July came out 3,845 billable (of 32,887 raw), BF agreed on 2026-08-28; August 3,996 (of 51,695; BF's list arrived a week past period end after chasing, via Mio, Syb then Marcelo, and the bill went out at 3,996 on 2026-09-08); September 4,196 (of 35,985), BF confirmed 2026-10-05 and Cameron Hughes forwarded to finance. The count depends on BF's monthly list each time; the fixed-fee proposal is meant to remove that dependency.
Next: BF supplies the October free-account list after month end; closes if the fixed fee lands.
Refs: https://mahifx.slack.com/archives/C08473TFD7Z/p1780330801690039 https://mahifx.slack.com/archives/C08473TFD7Z/p1787911173849309 https://mahifx.slack.com/archives/C08473TFD7Z/p1788341931661869 https://mahifx.slack.com/archives/C08473TFD7Z/p1791214982915359

### payout-reduction — Monthly payout data and value-add report
status: open · since: 2026-07-07 · last: 2026-10-06
State: Each month BF sends the funded-payout spreadsheet and Cameron Hughes returns payout-reduction estimates inside the monthly report or microsite. August data came 2026-09-01 (estimates added the same day); September data came 2026-10-06 ahead of the monthly call and the report went out after it. BF's reaction to the size of the reduction is tracked under fixed-fee-proposal.
Next: BF sends October payouts around the first week of November; Cameron Hughes asks ahead of the call.
Refs: https://mahifx.slack.com/archives/C08473TFD7Z/p1783419861147459 https://mahifx.slack.com/archives/C08473TFD7Z/p1788260805308349 https://mahifx.slack.com/archives/C08473TFD7Z/p1791277130717089 https://mahifx.slack.com/archives/C08473TFD7Z/p1791281722217399

### pfm-ranking — Prop Firm Match spread ranking
status: open · since: 2026-05-26 · last: 2026-10-06
State: BF's position in the Prop Firm Match spread table drives how tight Mahi quotes (the reason GBPUSD sits at 0.1 pip most hours). On 2026-10-01 Cameron Hughes noted BF was less often at the top, reduced MWMS and changed widening signal parameters, then reported "back to the top". Will Carter asked about payout impact; Cameron Hughes said skew and LR counter it well and BF checks the table often and wants to be at the top. On 2026-10-06 he flagged that the PFM spreads table looked broken. Tight quoting is a standing trade-off against Sunday-open and other arb exposure.
Next: none beyond monitoring.
Refs: https://mahifx.slack.com/archives/C08473TFD7Z/p1779793894044729 https://mahifx.slack.com/archives/C084G40JXEE/p1790867729276549 https://mahifx.slack.com/archives/C084G40JXEE/p1791300507287019

### sunday-open-gbpusd — GBPUSD Sunday-open arbing and spread fixes
status: watching · since: 2026-09-21 · last: 2026-10-09
State: On 2026-09-20 counterparty 1008081 (small volumes before, then ~$300M arb volume) hit GBPUSD two-way with IoC limits for ~35 min after the open and ended flat in profit (-$21k FI loss); the classifier missed it (positive inception yield) so it was whitelisted as an arber. Reference feeds were 15+ pips wide and disagreeing while Mahi quoted 0.1 pip. Fixes: SINGAPORE_MONDAY ladder widened (GBPUSD 4 pips, EURUSD 1, USDJPY 2; Mio approved 2026-09-23), then MWMS prioritised over ROLL/TWILIGHT/SNGMON and relaxed in liquid hours (backtested). BF (Mio, Alfredo) raised it again on 2026-10-07; Cameron Hughes showed prices were not stale, but the same trader also hit after 22:00 on 27 Sep and 4 Oct when the front reverts to 0.1 pip (2M clips swept the book at 1-1.6 pips). BF agreed to discount the PnL, approved a floor of half the tightest LP on GBPUSD (Sunday open 0.5-1 pip at the top), live 2026-10-09, Alfredo thanked. Isaac Dann also said Mahi will review spread benchmarking.
Next: BF to flag any recurrence; Mahi to watch the next few Sunday opens for regressions and PFM rank impact; Isaac Dann's spread-benchmarking review has no owner or date.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1789964773380629 https://mahifx.slack.com/archives/C08473TFD7Z/p1791366009839959 https://mahifx.slack.com/archives/C08473TFD7Z/p1791389174262399 https://mahifx.slack.com/archives/C08473TFD7Z/p1791554147761909

### sol-ref-selector — SOLUSD pricing freeze on Binance reconnect
status: watching · since: 2026-10-07 · last: 2026-10-07
State: SOLUSD went indicative on CLIENT_PRICE_LDN 2026-10-03 until a pricer bounce 6 Oct: Binance is pulled by the latency filter after each websocket reconnect (~48h) and never returns, and OKX (the other source) dropped out 30 Sep. Change switched referencePriceMarketSelectors from BINANCE|OKX to BINANCE|MATCH_TRADE; Cameron Hughes approved and reported "change done" on 2026-10-07 (pricer restarts, ZD #23601). The underlying Binance triggerTime/latency-filter bug is not fixed: after a reconnect SOL prices off Match alone until the next restart.
Next: Confirm SOLUSD stays firm through Binance reconnects; revert selector and bounce pricers if SOL is indicative or the mid is off Binance/Match; ZD #23601 tracks the filter bug.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1791338442138609 https://mahifx.slack.com/archives/C084G40JXEE/p1791386487483589

### perps-interest — BF interest in perpetuals
status: watching · since: 2026-10-07 · last: 2026-10-07
State: At the monthly call BF raised the growth of perps and their interest in it. Cameron Hughes said Mahi can offer pricing for perps and the techniques apply equally; he flagged it as one to get ahead of for other props and prospects.
Next: Follow up with BF on scope if they pursue it.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1791385820262249

### pricing-config-fixes — Arb rules and indices reference panel clean-up
status: closed · since: 2026-08-27 · last: 2026-08-27 · closed: 2026-10-15
State: On 2026-08-27 Cameron Hughes added missing dynamic arbitrageur execution rules on three profiles (catchall and two unused), edited others to match the default arbitrageur rule so trades fail, and removed MAHI_LP_2 from the BrightFundedIndices reference price after bad pricing at market open when Match was flagged indicative. Done; no follow-up in window.
Refs: https://mahifx.slack.com/archives/C084G40JXEE/p1787823135634519 https://mahifx.slack.com/archives/C084G40JXEE/p1787847675442419

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
