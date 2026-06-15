---
slug: alphacapital
refs:
  vibepulse: ../VibePulse/.claude/clients/alphacapital.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: ../MahiProduct/wiki/clients/alpha-capital-group.md
channels_override: null
key_people_overrides:
  - {name: "Gerry", role: "Analytics/risk, Alpha Capital (last name unknown)", confidence: low}
  - {name: "Jade", role: "Alpha Capital (last name and exact role unknown; raised statement of account request 2026-05-22)", confidence: low}
last_catchup: 2026-06-15T07:15:04Z
---

## Recent issues

> [open] 2026-06-10 — CLIENT_PRICE_LDN mass latency alerts: starfishFilePersister backpressure during tick bursts
> Cameron Copland: ~240 `distribution.marketDataLatency.CLIENT_PRICE_LDN.*` alerts fired in bursts since 11:03 UTC, recurring every ~15 min (worst ~9s staleness). LP feed latency stayed at ms-level throughout, but Aeron publish retries for CLIENT_PRICE_LDN exploded during each burst and `starfishFilePersisterExternalMarketData1` POOL-0 queue spiked from ~170 → ~26k at the same minutes (12:30 UTC = US data window). Hypothesis: persister falls behind on tick bursts and backpressures the full CLIENT_PRICE_LDN publication stream. Liam Cordelle replied: (1) check if alerts are busting through the summariser (should be low-priority — may have been changed); (2) look for allocation stalls on the box; (3) backgroundJobs may be under heavy memory pressure. No fix actioned yet. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1781100905794369) [pagerduty](https://mahifx.pagerduty.com/incidents/Q1CTD2XEHVAGWV)

> [open] 2026-06-01 — signalProcessCFDFI1 crash-loop: ADWeights counter lock (recurrence of 2026-05-15 pattern)
> Sam Hewitt: `signalProcessCFDFI1` has been crash-looping since ~2026-05-30 08:14 UTC on alphacapital-ln-trading-1. Cycle: process runs ~21 min, hangs on `ADWeights.*.counter` exclusive lock at startup, shutdown hook also hangs on same counter → SIGKILL → repeat (4/4 launches blocked). CFD CLIENT_PRICE (XAUUSD + other CFDs) cycling offline/online with spread whipsaw. Ruled out: Aeron infra (FX sibling `signalProcessFI1` stable ~41h), stale OS lock (ext4 flocks die with process; `lsof` shows no holder). Restart alone does not fix. Recommended: (1) stop wrapper to halt cycling; (2) quarantine/clear `ADWeights.*.counter` files under `…/signals/shared/var/` — resets signal weights, requires eng sign-off. Sam pinged Arun (who had the 2026-05-15 counter-lock incident). No reply yet. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1780278921326309)

> [open] 2026-05-28 — GBPUSD price spike (2026-05-27 14:20 UTC): bad Velocity ticks → TOBPN off-market → skew overamplified
> Nathan Burch: rogue price spike on GBPUSD at 14:20:13 UTC on 2026-05-27. Root cause: bad ticks from Velocity caused crossed bid/offer, which corrupted the TOBPN (top-of-book price node), causing mid formation to be off-market. SIGNPN config skews by 100% of benchmark, so the bad mid produced a disproportionately large skew magnitude. Nathan proposes reducing max skew from 10,000 pips to 2 pips — not yet actioned; awaiting further input. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1779945147921969)

> [open] 2026-05-22 — Statement of account request from Jade (Bonnie following up)
> Jade (Alpha Capital, external) posted in #mahi-alphacapitalgroup asking who to contact for a statement of account. Shyam Hari (Mahi Training) responded to Jade saying he'd sort it, and separately posted in #internal-alphacapitalgroup asking the team to create the statement / provide Jade with a contact. 2026-05-22 10:33 UTC: Bonnie Cassidy replied internally — "I'm not entirely sure what it is that she's requesting but will find out and follow up from there." No further update visible yet. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1779427327328109) [internal](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1779427896627129) [bonnie](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1779442392670229)

> [resolved] 2026-05-15 — signalProcessCFDFI1 down: counter file lock contention with signalProcessFI1
> Arun Patel: signalProcessCFDFI1 failed to start due to both FI1 and CFDFI1 contending for the same ADWeights counter file (NZDUSD IFMS). signalProcessFI1 held the exclusive lock, blocking CFDFI1. Arun had bumped `jvm_max_memory` on CFDFI1 as a prior workaround for allocation stalls; separately flagged whether some signals could be removed from signalProcessFI1/CFDFI1 to free compute and reduce downstream aeron subscriber latency spikes. Process was back up within ~1h. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778847108444079)

> [open] 2026-05-05 — XAGUSD skew abuse: arbitrageur classifier lag costing ~$35K/week
> Andrew Morgan (handover to Cameron): /skew-health-check run on alphacapital found 5 of 8 stage-c CPs inception-negative on 3–8 May (CPs: 2685507, 2696788, 2698331, 2697815, 2695337). Cohort detection-lag cost: $24.8K inception leakage across $555M volume in 5 days, ~$35K/week extrapolated. CP 2685507 alone accounts for 63% ($290M traded in single day before being caught, 4-day tag lag). 3 of 5 tagged on Qualifying FX.arbitrageurs.list (Bot wrote 2026-05-05 17:03 UTC); 2 still untagged (2696788, 2695337). Open items: (1) why offline classifier took 4 days on 2685507; (2) whether post-17:03Z trades on 2685507 route through Q1-Arbitrageurs vs Q1-Small-Tickets; (3) curation mechanism behind 13,120-CP arbitrageurs population (no arbitrageurs.badCheck configured); (4) analytics.realtimeArbDetection.* entirely unconfigured; (5) Q1-Arbitrageurs execution profile uses FORCE_INTERNALISATION + 200-300ms last-look with priceCheckThreshold: -1 (Andrew expected continuity-pool routing). Full report: docs/skew-health/alphacapital/2026-05-05-skew-health.md (commit cf26e5e). Context: Cameron Hughes had identified neuron signal as best-performing for XAG and promoted it; Andrew flagged this neuron-wins-while-all-flow-imbalance-signals-bleed pattern as a skew-abuse signature (CPs flipping positions to harvest skew, neuron lights up on reversal). Right fix is classifier auto-tagging, not signal tuning. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778009823301759)
> 2026-05-06 update — Andrew Morgan confirmed: continuity-pool fills on arbitrageur-classified flow do not apply LR (last-look/last-resort rules). Noted with grimacing reaction — no fix actioned yet. Directly addresses open item (5): the Q1-Arbitrageurs execution profile is routing via continuity pool as expected, but absence of LR is a further concern. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778057583339569)

> [open] 2026-05-05 — Velocity FX BMSL spread blowouts on GBPUSD/EURUSD/USDJPY (2026-05-04 21:10 UTC)
> Cameron Hughes: spread blowouts at 21:10 on 2026-05-04 across GBPUSD, EURUSD, USDJPY; Alpha reached out about GBPUSD. Backtest confirmed spike caused by BMSL. MAHI_BENCHMARK_LDN looks firm through each event; backtesting MAHI_BENCHMARK_LDN in BMSL to verify it would have prevented the blowouts. Investigation ongoing. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1777994333748779)

> [resolved] 2026-04-23 — XAG FI PnL bleed, signal switched to synapse
> Cameron Hughes: FI PnL decreasing for 3+ days on XAG, price signal performing badly. Switched XAGUSD signal param from neuron to synapse and bounced pricers. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1776939603625359)

> [resolved] 2026-04-20 — System notification processors bounced for alert-key fix
> Inald bounced system notification processors to pick up alert-key changes, mirroring the Infinox fix. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1776682157335539)

> [open] 2026-04-07 — CLIENT_PRICE_LDN latency alerts on pager
> Inald: latency alerts firing on CLIENT_PRICE_LDN, said "will take a look when i get a chance". No follow-up visible in this window — verify whether absorbed or still active. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1775571838771069)

> [watching] 2025-09-10 — Bridge contract expansion: +£10k/month, additional broker licence pending
> David Cooney: George wants to shift his bridge to Mahi for +£10k/month. 3rd Addendum to Compass Agreement prepared (Nicole Vivian). George hired an ex-IC/Eight Capital CEO to run his broker business who came partly because Mahi is in place; wants to organise tech/trading side around Mahi. Futures business "utterly going off." Another licence for the broker entity to follow. 250k accounts, ~25k active traders/day. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1757478607670689)

> [resolved] 2025-09-02 — Slippage/execution complaints; call held with George
> George's Gerry to collate all slippage complaints for the week; Mahi analytics to run instrument/classification/session analysis and make changes where necessary. DX direct connection set up (Mahi to verify flow received). TradeLocker flow expected via Tmix connection. Action: verify no DX duplicates between Tmix and direct connection. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1756808251453739)

> [open] 2025-08-06 — USOIL pricing dropouts causing spike on T4B fallback
> George: repeated USOIL pricing dropouts causing T4B to switch to backup LP mid, creating price spikes on the transition back. All previous fix attempts failed. T4B confirmed aware (it's our price dropping out). Amir: investigating root cause; suggested T4B use a failover LP with same mid. Argamon MD switch from OZ → Centroid (2025-08-27) may have helped — no follow-up confirmation in window. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1754466951005419)

> [resolved] 2025-05-22 — SI hedging to Argamon: testing complete, went live
> Amir: concluded full end-to-end testing 2025-05-22 — Alpha flow hitting SI books and hedging to Argamon verified. Blockers cleared: Beeks whitelisting (done Mon 2025-05-19), OZ whitelisting (done 2025-05-22). Spread predicate issue on hedger resolved (removed temporarily). $4k VaR briefly open; hedger cleared. First-ever client-to-client trading between Alpha Capital and Argamon (Argamon appearing as INST-26 counterparty). Proposed live date: Tuesday 2025-05-27. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747924833729009)

> [resolved] 2025-05-19 — Strategic review: George authorises bridge migration from T4B; Mahi to represent Alpha with TradeLocker
> Andrew Morgan/Amir met George: George bought in to using Mahi bridge; agreed sloppy TEMP_MIXED FIX connection for DX+TradeLocker in interim; George authorised Mahi to represent Alpha with TradeLocker directly. George noted DX doesn't send group/competition info via T4B (all DX flow warehoused in T4B). George has plug-ins to build before fully replacing T4B. Agreed platform rollout order: DX+TradeLocker → MT5+cTrader → AlphaTrader. Alpha described as "blue chip client" for direct platform integrations (bypassing T4B/PrimeXM). [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747660857701689)

> [resolved] 2025-05-12 — New platform integration: Alpha Trader FIX setup; SI processes deployed
> SI processes deployed FX-only (hybridHedgerSI1, fixMarketData/OrderArgamon1 via OZ, riskSplit on CUSTOM2). Connectivity blocker: Beeks/OZ whitelisting (resolved 2025-05-19/22). Alpha Trader: George building in-house platform (not a new competition); Mahi set up Alpha Trader FIX session pair via T4B. TEMP_MIXED FIX creds issued (DX+TradeLocker mixed, all stages). Direct DX FIX creds issued 2025-06-02. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747063818928149)

> [resolved] 2025-05-02 — NFP CLIENT_PRICE_LDN latency spike; riskPathQualifying moved to low-latency node
> Inald: 4s input latency on CLIENT_PRICE_LDN and CLIENT_PRICE_MAHI during NFPs. Root cause: riskPathQualifying on wrong node. Moved to low-latency node 0 same day. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1746190417423999)

## Notable topics

- 2026-06-05 — Compass version upgrade scheduled for weekend of 2026-06-07/08. Liam Cordelle notified client channel that the system would be upgraded to the latest Compass version over the weekend, with Mahi monitoring the open for issues. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1780673128888239)

- 2026-05-13 — Argamon LD Centroid bridge IP migration (2026-05-16 weekend). David Rapp (Argamon) notified that the LD Centroid bridge instance was migrating servers Saturday 16 May (downtime 2100 UTC Fri–2100 UTC Sat). Clients targeting the DNS `arguk.centroidsol.com` required no action; those with hardcoded IPs needed to update to `192.109.17.170`. Forwarded to Cameron Hughes and Maten Rehimi in client channel; Cameron Hughes confirmed changes actioned. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1778658472423589)

- 2026-05-10 — clientDistributionGateway3 removal query. Nathan Burch noted the gateway does not appear to be in use and asked if it could be removed; Daria Horton tagged Cameron Hughes for a decision. No resolution visible in window. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778449279618189)

- 2026-05-07 — Compass UI: Execution Rule editor reworked for Arbitrageurs routing. Justin Young (release/26.3): (1) Recognised Arbitrageurs rules now show a plain-English banner instead of full config form (profile matched when targeting dynamically-classified arbitrageurs, routing to internal/continuity-pool, zero fees, no price improvement, last-look fills accepted regardless of price-check). Analytics invited to flag if matcher params need tightening. (2) Rules with no Arbitrageurs profile now flagged in pale orange with tooltip explaining consequence (arb-classified CPs won't route to Continuity Pool). (3) New LR P&L column in Execution Rules and Profiles tables alongside Spread and 30s P&L. A fleet-wide scan skill (for profiles missing Arbitrageurs rule) is forthcoming. Directly relevant to open XAGUSD skew-abuse issue (open item: Q1-Arbitrageurs execution profile, FORCE_INTERNALISATION + continuity-pool fills with no LR). [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778150187657269)

- 2026-04-02 — Alpha's alpha-signals lag fleet defaults. Andrew Morgan: "the alpha signals are not currently running the best and latest stuff" — neuron/synapse eclipsed by newer signals; signal-default-registry now exists for fleet-wide rollout. Tied to the XAG switch on Apr 23. Also flagged: should auto-handle skew abusers via an ER. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1775126095434959)

- 2025-09-15 — Tick data / Pulse licence opportunity flagged. George has repeatedly asked for tick data export; Justin Young: easy enough to export but could push a Pulse licence instead. Bonnie: will raise in call. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1757944918345499)

- 2025-09-10 — 250k accounts / 25k active traders: David Cooney disclosed Alpha's scale. George hired ex-IC + Eight Capital CEO to run broker entity; futures business growing fast. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1757479003869429)

- 2025-06-11 — Alpha integrating payout data via API (Swarnab). Cameron requesting payout CSVs (weekly/monthly, per-individual). Alpha confirmed they're connected via API and offered to send payout data in real time including account tags across stages. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1749635006602119)

- 2025-05-06 — Pass-rate analysis: Cameron ran sims showing 7% pass-rate uplift by dropping profit target from 10% to 8%. George asking for consistency-rule impact analysis on pro 8% channel (currently near break-even, wants to understand vs FundingPips). [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1746114914206789)
