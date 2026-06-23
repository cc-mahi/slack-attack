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
  - {name: "Alison Koay", role: "StarPrime — Echo/Compass access requested 2026-06-17", confidence: low}
  - {name: "Jay M", email: "jay@starprime.com", role: "CEO / co-founder", confidence: low}
  - {name: "Clarice Frost", email: "clarice.frost@startrader.com", role: "overnight ops", confidence: low}
  - {name: "Allan Maira", email: "allan.maira@startrader.com", role: "overnight ops", confidence: low}
last_catchup: 2026-06-23T07:34:50Z
---

## Recent issues

> [resolved] 2026-06-23 — PXM order-splitting causing spurious LR on second leg (machine-gun misclassification)
> Samin flagged that when a client trades a ticket larger than TOB volume, PXM splits it into legs (_1 and _2) before sending to MFX. MFX treats the rapid second leg as machine-gun behaviour and applies LR (15dpm observed on NDXUSD, counterparty RBI_5173_100142). Samin asked for base order IDs to be treated as a single ticket. Daria's resolution: ask PXM to send the order as "full" (not swept), so Compass receives the entire order and applies VWAP across published layers internally rather than the LR path. Samin applied the setting change in PXM ("Boosted"), confirmed a single ticket passed through. Daria validated the VWAP fill (4123.01) matched the stack. Resolved same session. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1782193030739099)

> [open] 2026-06-23 — Shahid Afrid asking how to self-investigate execution stacks
> Shahid asked Daria to guide them on how to investigate execution themselves to see the stack that got filled. No response captured in window — open and awaiting Daria's reply. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1782199529459729)

> [open] 2026-07-21 — FIX maker sessions posted; awaiting Starprime-B connection confirmation
> Daria Horton sent FIX maker session credentials for Starprime-B to Samin (2026-07-21). As of 2026-08-04 Daria chased again — no connection confirmation received from the client side. Blocking go-live. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1753107069000001)

> [open] 2026-07-28 — Beeks admin server accidentally cancelled; XC in progress (NOCINT-7250220)
> Justin Young flagged that Beeks had accidentally cancelled StarPrime's admin server (NOCINT-7250220). XC was requested to get it back. Status of XC resolution not confirmed in channel. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1753178166000001)

> [open] 2026-07-14 — Contract signed; onboarding underway on LD4 servers (B2B 3-tier Gold/Silver/Bronze)
> Contract signed ~2026-07-14; Amir Davies confirmed as onboarding lead. B2B 3-tier structure (Gold/Silver/Bronze). Liam Cordelle repurposed migration servers at LD4 to fast-track. Jay M (CEO) and Samin joined #mahi-starprime 2026-07-16. LP panel confirmed via PXM: Vantage, Kama Capital, ISPrime, ACN, Equiti, Finalto, Gain, Velocity, Invast, Edgewater, Alchemy. Compass distribution creds (FX/CFD/crypto A+B) and standard proxy pricing set up by Daria and Isaac by 2026-07-18; pending from client: MT manager creds, LP connection creds. FIX files MFX-T1/T2/T3 sent; tag 7533 stream setup resolved with Samin's guidance. EURUSD pricing confirmed on all LP feeds by 2026-07-31. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1752480597000001)

> [resolved] 2026-06-19 — MAHI_LP_11 dropout at market close; Samin queried continuity pool / WSS behaviour
> On 2026-06-18 ~22:00 UTC, MAHI_LP_11 dropped out causing CLIENT_PRICE_LDN to cut out. Samin asked why continuity pool and WSS ($0.25 cap he believed was set) didn't prevent the issue. William Denny investigated and clarified: continuity pool did kick in at the DISTRIBUTION layer (22:01:33–22:01:35) but Starprime-B-Prices only subscribed at 22:01 so no B_CLIENTS price existed before that point. The WSS cap during that session is $2 (not $0.25) as configured in DISTRIBUTION_WSS spread config; the $0.25 is a per-instrument value Samin saw but the $2 limit was not hit. William shared tick data excel for B_CLIENTS over the period and screenshotted the timezone session WSS settings. Samin confirmed satisfied. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1781861009556289)

> [open] 2026-06-15 — XAUUSD MFX-RETAIL spread flickering 5–26c; pillar liquidity spike triggering wide quotes
> Shahid Afrid flagged at ~20:06 BST with screen recording: spread oscillating 5–26c on MFX-RETAIL XAUUSD. Shyam Hari (Mahi) investigated. Samin diagnosed the spread widening as triggered when TOB liquidity jumped 100→200 around spread pillars. Samin tested by slightly widening 2nd/3rd/4th layer then reverted; reported stable at ~20:53 BST. However Samin also noted spread remained at 5c when TOB should be 3c before self-resolving ("sorted"). No Mahi-side root cause stated in channel. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1781550411644169)

> [open] 2026-05-27 — $30k skew P&L drop on XAUUSD market open; MAHI_LP_11 sole reference price $10 below client LPs
> Daria Horton reported a ~$30k skew P&L drop on XAUUSD at the LDN open. MAHI_LP_11 (retail feed from Toa Args LDN) was the sole reference price and was up to $10 below StarPrime's LPs for a period; prices eventually re-aligned. LP pricing was chaotic generally — spiky behaviour in early part attributed to CBOE_HR_LDN issues (Invast and Velocity affected similarly); later portion was smooth. Daria noted RBI_5182_60000 is now classified as an arbitrageur. No resolution or further action stated in thread; Daria posted top-of-book Echo links for context. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1779851154348779)

> [resolved] 2026-05-07 — Limit order cancellations due to Arbitrageur misclassification of counterparty RBI_5036_LIVE-97F5F2
> Umar Bin Aziz reported execution errors on limit orders (~11:20 BST). Rory King diagnosed: counterparty RBI_5036_LIVE-97F5F2 had been classified under the `BBOOK//Arbitrageurs` execution rule after a small number of trades; limit orders were being force-internalised on the continuity pool with markup, with fills breaching the limit price and cancelling. Umar requested removal; Rory blacklisted the counterparty from the Arbitrageurs profile at 12:03 BST. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1778151195430889)

> [resolved] 2026-05-07 — XAUUSD LIMIT order LIQUIDITY_VIOLATION on orders 2409798/2409799 (LP-side incident)
> Umar Bin Aziz posted logs showing orders 2409798 and 2409799 (XAUUSD limit) rejected with `LIQUIDITY_VIOLATION` on connector LIV_NRI_5036. Sam Hewitt investigated and confirmed the LP was returning liquidity violation rejects 06:35–06:40 UTC; 49 and 50 hedge legs retried respectively, all cancelled. LP-side issue self-cleared at 06:40, no recurrence. Umar acknowledged. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1778140090765839)

> [watching] 2026-05-05 — Go-live timeline: contract signed 2026-07-14; onboarding actively underway
> Call with Samin (client ops lead) held 2026-05-05. Go-live delayed due to operational issues on client side; target was July. Contract signed ~2026-07-14 and onboarding began on LD4 servers (see entry above). Pending: FIX maker session connection from client, MT manager creds. Hedging model discussed: SI delayed hedging (Exinity-style 5min/30min/1hr off-book), VaR walkthrough done. Samin raised % LP split requirement (not currently supported). Samin also wants to start making to hedge funds (as of 2026-08-01). [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777983798434859)

> [open] 2026-04-23 — REST API request for historical trade data
> Shahid asked about connecting to MFX via REST API for historical trade data; Cameron Hughes suggested Pulse (`houseorder_response`) first — Shahid to check with Sam internally and revert. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1776941638461559)

## Notable topics

- 2026-06-23 — PXM "Boosted" mode confirmed as the fix for order-splitting LR issue: Daria advised sending orders as "full" (not swept legs) so Compass VWAP fills correctly without triggering LR on the second leg. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1782193030739099)
- 2026-06-23 — Shahid Afrid asked Daria for guidance on self-service execution investigation (how to view the fill stack themselves). Unanswered in window. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1782199529459729)
- 2026-06-19 — Samin confirmed spread PnL includes FI and LR (William Denny answered yes). [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1781856637768089)
- 2026-08-01 — Samin asked whether StarPrime can start making prices to hedge funds (new distribution requirement); no resolution captured in channel. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1754341620000001)
- 2026-07-31 — EURUSD pricing confirmed live on all LP feeds (MFX-T1/T2/T3). [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1754173200000001)
- 2026-07-28 — Jay M raised % LP split as a requirement (not currently supported by Mahi); noted Martingale clients with $1M+ PnL swings in the book. Thursday "bumper" meeting planned to cover hedging model in depth. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1753178166000002)
- 2026-07-23 — VaR walkthrough held; hedging model agreed as SI delayed (Exinity-style: 5min/30min/1hr off-book). Trade size conditions discussed. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1752814331000002)
- 2026-07-22 — Tag 7533 stream (PXM LP feed) setup resolved: Samin confirmed correct setup after back-and-forth on symbol mapping; CSV of symbol mappings sent. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1753052134000001)
- 2026-07-18 — Compass setup complete for FX/CFD/crypto A+B distribution creds and standard proxy pricing; pending from client: MT manager creds and LP connection creds. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1752814331000001)
- 2026-07-16 — Jay M and Samin joined #mahi-starprime; Liam Cordelle repurposed LD4 migration servers to fast-track onboarding. LP panel confirmed via PXM (Vantage, Kama Capital, ISPrime, ACN, Equiti, Finalto, Gain, Velocity, Invast, Edgewater, Alchemy). [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1752480597000002)
- 2026-07-14 — Contract signed; Amir Davies confirmed as onboarding lead. B2B 3-tier structure: Gold/Silver/Bronze. Both Slack channels (#internal-starprime and #mahi-starprime) created. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1752480597000001)
- 2026-06-17 — Samin requested Echo & Compass credentials for alison.koay@starprime.com; Rory King confirmed provisioning. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1781701973081049)
- 2026-06-17 — Samin asked whether Echo can show how many times counterparties RBI_5182_60002 / RBI_5182_60004 have cycled through execution rules and what % of time in each ER. Shyam Hari pointed to Echo execution profile + order date grouping view; Samin confirmed helpful. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1781675765649179)
- 2026-06-15 — Samin requested Compass read access to `pricing.filter.list`; Daria Horton responded she'd raise with dev and noted the key only contains reduced filters for XAUUSD / CLIENT_PRICE_LDN. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1781557677597789)
- 2026-06-04 — Samin requested B2PRIME_RETAIL added to Echo TOB (routing via MFX-T4); Rory King added it to `persistedMarketsSelectors` and bounced `starfishFilePersisterExternalMarketData1`; confirmed done within a few minutes. [permalink](https://mahifx.slack.com/archives/C096422RPKK/p1780571748825339)
- 2026-06-04 — Cameron Hughes quoted Samin ("got a big meeting next weekend - selling the mahi product") in internal-starprime and noted Samin is looking for NOP docs. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1780572669949409)
- 2026-05-05 — Inald Gjoni performed rolling restart of pricers to load Timezone Conditions for BenchmarkMinimumSpreadLogic (no-restart component deploy). [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777981565638809)
- 2026-05-11 — Nathan Burch (Training) changed `price adjustment floor pips` on IFMS from 3 → 0.5 for XAUUSD on CLIENT_PRICE_INSTI; prior to this, price could not form because floor was greater than ceiling. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1778463918376889)
- 2026-05-13 — Andrew Morgan noted (internal-starprime) "apparently these guys are owned by vantage"; David Cooney confirmed. 3 open_mouth reactions. No further context in channel. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1778669482861249)
- 2026-05-19 — Isaac Dann posted in #internal-go: Kieran (Go Markets) was asking about StarPrime, noting their CEO was using "Mahi Terminology"; Isaac did not disclose either way. Khim (Go Markets) wants to talk to Dave Cooney about potentially onboarding StarPrime as an LP. Bonnie Cassidy offered to arrange the call; Dave said he'd reach out himself. [permalink](https://mahifx.slack.com/archives/CNF3WPNSK/p1779165368815299)
- 2026-05-19 — Cameron Hughes listed "Starprime B: signal-down fingerprint" as a standup priority in #internal-trading-operations. No further detail in the thread. [permalink](https://mahifx.slack.com/archives/C0A2K4TH090/p1779186201548519)
- 2026-05-27 — Will Carter and Cameron Hughes observed StarPrime has resumed sending B Book flow as of a few weeks ago (not much volume); Samin had not mentioned it. Will had believed they were fully off B Book. Echo yield-profile link posted. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1779869052796799)
- 2026-05-01 — Go-live prep: Cameron Hughes noted a call with Samin arranged for Tuesday to get everything ready pre go-live. [permalink](https://mahifx.slack.com/archives/C095MJHC68J/p1777625477346409)
