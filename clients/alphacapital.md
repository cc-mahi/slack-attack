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
last_catchup: 2026-05-12T07:16:59Z
---

## Recent issues

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

- 2026-05-10 — clientDistributionGateway3 removal query. Nathan Burch noted the gateway does not appear to be in use and asked if it could be removed; Daria Horton tagged Cameron Hughes for a decision. No resolution visible in window. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778449279618189)

- 2026-05-07 — Compass UI: Execution Rule editor reworked for Arbitrageurs routing. Justin Young (release/26.3): (1) Recognised Arbitrageurs rules now show a plain-English banner instead of full config form (profile matched when targeting dynamically-classified arbitrageurs, routing to internal/continuity-pool, zero fees, no price improvement, last-look fills accepted regardless of price-check). Analytics invited to flag if matcher params need tightening. (2) Rules with no Arbitrageurs profile now flagged in pale orange with tooltip explaining consequence (arb-classified CPs won't route to Continuity Pool). (3) New LR P&L column in Execution Rules and Profiles tables alongside Spread and 30s P&L. A fleet-wide scan skill (for profiles missing Arbitrageurs rule) is forthcoming. Directly relevant to open XAGUSD skew-abuse issue (open item: Q1-Arbitrageurs execution profile, FORCE_INTERNALISATION + continuity-pool fills with no LR). [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778150187657269)

- 2026-04-02 — Alpha's alpha-signals lag fleet defaults. Andrew Morgan: "the alpha signals are not currently running the best and latest stuff" — neuron/synapse eclipsed by newer signals; signal-default-registry now exists for fleet-wide rollout. Tied to the XAG switch on Apr 23. Also flagged: should auto-handle skew abusers via an ER. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1775126095434959)

- 2025-09-15 — Tick data / Pulse licence opportunity flagged. George has repeatedly asked for tick data export; Justin Young: easy enough to export but could push a Pulse licence instead. Bonnie: will raise in call. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1757944918345499)

- 2025-09-10 — 250k accounts / 25k active traders: David Cooney disclosed Alpha's scale. George hired ex-IC + Eight Capital CEO to run broker entity; futures business growing fast. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1757479003869429)

- 2025-06-11 — Alpha integrating payout data via API (Swarnab). Cameron requesting payout CSVs (weekly/monthly, per-individual). Alpha confirmed they're connected via API and offered to send payout data in real time including account tags across stages. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1749635006602119)

- 2025-05-06 — Pass-rate analysis: Cameron ran sims showing 7% pass-rate uplift by dropping profit target from 10% to 8%. George asking for consistency-rule impact analysis on pro 8% channel (currently near break-even, wants to understand vs FundingPips). [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1746114914206789)
