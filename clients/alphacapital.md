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
last_catchup: 2026-05-02T07:16:23Z
---

## Recent issues

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

- 2026-04-02 — Alpha's alpha-signals lag fleet defaults. Andrew Morgan: "the alpha signals are not currently running the best and latest stuff" — neuron/synapse eclipsed by newer signals; signal-default-registry now exists for fleet-wide rollout. Tied to the XAG switch on Apr 23. Also flagged: should auto-handle skew abusers via an ER. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1775126095434959)

- 2025-09-15 — Tick data / Pulse licence opportunity flagged. George has repeatedly asked for tick data export; Justin Young: easy enough to export but could push a Pulse licence instead. Bonnie: will raise in call. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1757944918345499)

- 2025-09-10 — 250k accounts / 25k active traders: David Cooney disclosed Alpha's scale. George hired ex-IC + Eight Capital CEO to run broker entity; futures business growing fast. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1757479003869429)

- 2025-06-11 — Alpha integrating payout data via API (Swarnab). Cameron requesting payout CSVs (weekly/monthly, per-individual). Alpha confirmed they're connected via API and offered to send payout data in real time including account tags across stages. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1749635006602119)

- 2025-05-06 — Pass-rate analysis: Cameron ran sims showing 7% pass-rate uplift by dropping profit target from 10% to 8%. George asking for consistency-rule impact analysis on pro 8% channel (currently near break-even, wants to understand vs FundingPips). [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1746114914206789)
