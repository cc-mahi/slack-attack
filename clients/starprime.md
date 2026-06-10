---
slug: starprime
refs:
  vibepulse: ../VibePulse/.claude/clients/starprime.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: starprime
  hosts: ../MahiProduct/data/client-hosts.json          # entry: starprime
  wiki: ../MahiProduct/wiki/clients/starprime.md
channels_override: null
key_people_overrides:
  - {name: "Shahid Afrid", role: "client ops / data integrations", confidence: low}
last_catchup: 2026-06-10T07:30:19Z
---

## Recent issues

> [open] 2026-05-27 — $30k skew P&L drop on XAUUSD market open; MAHI_LP_11 sole reference price $10 below client LPs
> Daria Horton reported a ~$30k skew P&L drop on XAUUSD at the LDN open. MAHI_LP_11 (retail feed from Toa Args LDN) was the sole reference price and was up to $10 below StarPrime's LPs for a period; prices eventually re-aligned. LP pricing was chaotic generally — spiky behaviour in early part attributed to CBOE_HR_LDN issues (Invast and Velocity affected similarly); later portion was smooth. Daria noted RBI_5182_60000 is now classified as an arbitrageur. No resolution or further action stated in thread; Daria posted top-of-book Echo links for context. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1779851154348779)

> [resolved] 2026-05-07 — Limit order cancellations due to Arbitrageur misclassification of counterparty RBI_5036_LIVE-97F5F2
> Umar Bin Aziz reported execution errors on limit orders (~11:20 BST). Rory King diagnosed: counterparty RBI_5036_LIVE-97F5F2 had been classified under the `BBOOK//Arbitrageurs` execution rule after a small number of trades; limit orders were being force-internalised on the continuity pool with markup, with fills breaching the limit price and cancelling. Umar requested removal; Rory blacklisted the counterparty from the Arbitrageurs profile at 12:03 BST. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1778151195430889)

> [resolved] 2026-05-07 — XAUUSD LIMIT order LIQUIDITY_VIOLATION on orders 2409798/2409799 (LP-side incident)
> Umar Bin Aziz posted logs showing orders 2409798 and 2409799 (XAUUSD limit) rejected with `LIQUIDITY_VIOLATION` on connector LIV_NRI_5036. Sam Hewitt investigated and confirmed the LP was returning liquidity violation rejects 06:35–06:40 UTC; 49 and 50 hedge legs retried respectively, all cancelled. LP-side issue self-cleared at 06:40, no recurrence. Umar acknowledged. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1778140090765839)

> [open] 2026-05-05 — Go-live timeline shifted to July; pre-go-live call notes
> Call with Samin (client ops lead) held 2026-05-05. Key points: go-live delayed due to operational issues on client side; Samin is heading to LDN then Madrid; target is July but wants to pull it sooner if packaging allows. Action items: prep Signals deck for Insti SI; PSM discussed — Dave confirmed feasible but chargeable. Testing underway with fixed spread values on gold to assess flow attracted. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777983798434859)

> [open] 2026-04-23 — REST API request for historical trade data
> Shahid asked about connecting to MFX via REST API for historical trade data; Cameron Hughes suggested Pulse (`houseorder_response`) first — Shahid to check with Sam internally and revert. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1776941638461559)

## Notable topics

- 2026-06-04 — Samin requested B2PRIME_RETAIL added to Echo TOB (routing via MFX-T4); Rory King added it to `persistedMarketsSelectors` and bounced `starfishFilePersisterExternalMarketData1`; confirmed done within a few minutes. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1780571748825339)
- 2026-06-04 — Cameron Hughes quoted Samin ("got a big meeting next weekend - selling the mahi product") in internal-starprime and noted Samin is looking for NOP docs. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1780572669949409)
- 2026-05-05 — Inald Gjoni performed rolling restart of pricers to load Timezone Conditions for BenchmarkMinimumSpreadLogic (no-restart component deploy). [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777981565638809)
- 2026-05-11 — Nathan Burch (Training) changed `price adjustment floor pips` on IFMS from 3 → 0.5 for XAUUSD on CLIENT_PRICE_INSTI; prior to this, price could not form because floor was greater than ceiling. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1778463918376889)
- 2026-05-13 — Andrew Morgan noted (internal-starprime) "apparently these guys are owned by vantage"; David Cooney confirmed. 3 open_mouth reactions. No further context in channel. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1778669482861249)
- 2026-05-19 — Isaac Dann posted in #internal-go: Kieran (Go Markets) was asking about StarPrime, noting their CEO was using "Mahi Terminology"; Isaac did not disclose either way. Khim (Go Markets) wants to talk to Dave Cooney about potentially onboarding StarPrime as an LP. Bonnie Cassidy offered to arrange the call; Dave said he'd reach out himself. [permalink](https://mahifx.slack.com/archives/CNF3WPNSK/p1779165368815299)
- 2026-05-19 — Cameron Hughes listed "Starprime B: signal-down fingerprint" as a standup priority in #internal-trading-operations. No further detail in the thread. [permalink](https://mahifx.slack.com/archives/C0A2K4TH090/p1779186201548519)
- 2026-05-27 — Will Carter and Cameron Hughes observed StarPrime has resumed sending B Book flow as of a few weeks ago (not much volume); Samin had not mentioned it. Will had believed they were fully off B Book. Echo yield-profile link posted. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1779869052796799)
- 2026-05-01 — Go-live prep: Cameron Hughes noted a call with Samin arranged for Tuesday to get everything ready pre go-live. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777625477346409)
