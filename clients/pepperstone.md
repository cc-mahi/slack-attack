---
slug: pepperstone
aliases: [pepperstone-crypto, pepperstone-cfd]
refs:
  vibepulse: [../VibePulse/.claude/clients/pepperstone.yaml, ../VibePulse/.claude/clients/pepperstone-crypto.yaml]
  billing: ../MahiProduct/data/billing/clients.json     # entry: pepperstone
  hosts: ../MahiProduct/data/client-hosts.json          # entries: pepperstone, pepperstone-cfd, pepperstone-crypto
  wiki: ../MahiProduct/wiki/clients/pepperstone.md
channels:
  internal-pepperstone: C033K2P0RPT
  mahi-pepperstone-vnd: C06AR8MT8NT
contacts:
  - {name: "Stephen Hendrie", role: "Pepperstone exchange/product lead; main FX+crypto counterpart, joined steer co 2026-07"}
  - {name: "Marianna Konstantinidi (MK)", role: "Pepperstone trading ops, CFD/crypto config requests, CFD licence sponsor"}
  - {name: "Reece Singh", role: "Pepperstone ops/counterparty admin; classification, YPs, hedger rejections"}
  - {name: "Ruby Wang", role: "Pepperstone OZ/exchange trading ops"}
  - {name: "Diego Arranz", role: "Pepperstone CFD ops, OZ config, IP whitelisting"}
  - {name: "Antonio Aguilar", role: "Pepperstone; Compass/Echo read-only access, roll-arb calls", confidence: low}
  - {name: "Mariapaz Bobadilla", role: "Pepperstone OZ; pricing/reject queries", confidence: low}
  - {name: "Gabriel Bignon", role: "Pepperstone; yield-profile and arb-classification queries", confidence: low}
  - {name: "Tom Smith", role: "Pepperstone tech/ops: DB/credentials/IP requests (distinct from Tom Williams, COO)", confidence: low}
  - {name: "Sebastian Andrews", role: "Pepperstone; DB access and cancelled-order queries", confidence: low}
  - {name: "James White", role: "Pepperstone data; joins Mahi data to OneZero by trade_id", confidence: low}
  - {name: "Georgios Voulgaropoulos", role: "Pepperstone OZ network/infrastructure", confidence: low}
  - {name: "Saemi Kim", role: "Pepperstone; pricing config changes 2026-10", confidence: low}
  - {name: "Sam Dammers", role: "Pepperstone security/Cloudflare IP policy", confidence: low}
  - {name: "Tom Williams", role: "Pepperstone COO since 2026-08"}
last_catchup: 2026-10-15T13:04:16Z
status: active
---

## Now
Live on FX, Crypto exchange (Modulus) and CFD (desk live since July), on a 3-year MSA to 2028-07. The client is shifting on three fronts: roll-time arbitrage across majors (Mahi raised roll LR 2026-10-15), FX B-book SI/inventory sims (Stephen persuaded, credit limit USD 200M the constraint) and crypto PSM scoping. A CPI-print gateway incident on 2026-10-14 is awaiting a full written response to Diego. Pepperstone is also moving spot crypto off Modulus (to "Polaris") with an SOW to come.

## Streams

### gateway-cpi-reject — NY gateway kill switch on CPI print, SYSTEM_CLOSED rejects
status: open · since: 2026-10-14 · last: 2026-10-15
State: On 2026-10-14 around 12:30 GMT a Mahi NY distribution gateway tripped its kill switch on the CPI print; XAUUSD orders on stream Mahi_B_NY_4 were rejected SYSTEM_CLOSED and the OZ hub retried ~25k orders on the London backup stream. Mariapaz asked why; Diego separately reported a ~20s LD price delay, and Rory replied 2026-10-15 that Mahi's distributed price was updating through (logs still being pulled). Nathan sent only a holding reply and wants a fuller incident response.
Next: Mahi (Rory/Nathan) owes Diego the log-backed explanation of the kill-switch trip and the LD delay.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791997243862479 https://mahifx.slack.com/archives/C033K2P0RPT/p1792043475375369 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792060740686789?thread_ts=1792018491.050639&cid=C06AR8MT8NT

### cfd-pricing-feeds — CFD feed gaps, reference-market changes and indicative alerts
status: open · since: 2026-09-22 · last: 2026-10-15
State: Recurring CFD price-feed questions: USDCLP only pricing from 12:31 GMT instead of 11:51 (Mariapaz, 2026-09-22), NAPN and USDCLP disabled by MK on 2026-09-24 for a QRT feed problem, indicative-pricing alerts and the ~20s LD delay above. On 2026-10-15 MK asked for the primary reference on ten indices (AUS200, UK100, EUSTX50, FRA40, CHINAH, NETH25, HK50, SWI20, CN50, SCI25) to move to Velocity in beta ahead of extended hours at the DST change.
Next: Mahi to make the Velocity reference change in beta; USDCLP root cause not confirmed in-window.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1790096194336949 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792061213615249

### roll-arb — Roll-time arbitrage on FX majors and Mahi's defensive LR/widening
status: open · since: 2026-07-17 · last: 2026-10-15
State: Arb at the NZD/SGD roll started on NZDUSD and spread to AUDNZD, EURCHF, USDCAD (USD 264M on 2026-10-05) and EURNZD (USD 90M, 2026-10-14). Mahi tightened roll LR, added defensive FM-T-0-30000 widening and cut NZDUSD roll volume 87% (35.5M/day to 4.7M/day by 2026-09-23). After a call with Stephen, Ruby and Antonio on 2026-10-15 the approach switched from per-instrument widening to an across-the-board roll LR increase (channel cap USD 25/M to 200/M, counterparty cap 200/M, tighter global bucket); Pepperstone want a walkthrough so they can tweak it themselves.
Next: Shyam to show Stephen's team the roll LR set-up.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1784250309662259 https://mahifx.slack.com/archives/C06AR8MT8NT/p1785799037959129 https://mahifx.slack.com/archives/C033K2P0RPT/p1792025561286759

### crypto-yield-psm — Crypto yields down; PSM scoping for XBTUSD/XETUSD
status: open · since: 2026-10-06 · last: 2026-10-15
State: Crypto spread yield fell to ~USD 200/M versus 350-450 historically; Isaac attributes about half to BTC's rally against a flat USD 15/BTC spread, the rest to lower volatility and B2C2/LMAX tightening. Isaac proposed PSM to MK (agreed 2026-10-08) and on 2026-10-15, after a call with MK and Andrew, screened configs: a "middle ground" widen/tighten gives about +9.2/M on XBTUSD and +48.5/M on XETUSD; full backtest and Compass sim verification is under way. Andrew also notes Claude RoS/PnL tracking does not match Compass Account Summary for crypto SI.
Next: Isaac to finish engine verification (5 variants on 8 and 11 Oct flow) and send MK PnL/spread numbers for PSM fully active / defensive only / 10% widening.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1791285982179839 https://mahifx.slack.com/archives/C033K2P0RPT/p1792068068772829

### fi-skew-tuning — FI/skew sizing and signals across FX, CFD and metals
status: open · since: 2026-08-18 · last: 2026-10-14
State: Reece flagged FI PnL slipping (2.9/M vs 4.0/M, early Aug) and requested flow-price-thresh on EURUSD (done 2026-09-22). On CFD, skew was raised from 20% of base spread after Nathan's beta shadow test (beta +USD 80k over 13-23 Sep); MK approved promoting the extra instruments and moving NDXUSD to the price signal on 2026-10-08, changes made, monitoring. Isaac moved EURUSD to IFM and on 2026-10-14 swapped FX majors to IFM-based benchmark FI adjustments and nudged the XAUUSD skew benchmark.
Next: Nathan to report on promoted CFD skew performance.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787060801310749 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791453538861039?thread_ts=1788929145.526369&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1791992133214739

### classification-upload — Pepperstone's own counterparty classification upload (SOW)
status: open · since: 2026-05-19 · last: 2026-10-13
State: MK/Reece have asked since May for an automated S3 upload of their external classifications. On 2026-10-13 Liam said MK has resurfaced and that Mahi will wrap the existing S3-based implementation in the SOW Pepperstone are expecting, aiming to be paid for it.
Next: Liam to issue the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919 https://mahifx.slack.com/archives/C033K2P0RPT/p1791904949863369

### cfd-hedging — CFD inventory hedger rejections, LP liquidity and risk controls
status: open · since: 2026-07-27 · last: 2026-10-13
State: The CFD inventory hedger keeps hitting LP limits: Velocity cancelled 241/250 HSTHKD hedges (2026-09-11, then price-precision rejects fixed via 2dp override 2026-09-17), NG1 clips reject on 26Degrees (2026-09-25, 2026-09-29, 2026-10-13) because the LP book resets to 20k after each fill while the hedger sizes off rolling fill ratios, and IG liquidity limits hit WHEAT. Andrew's analysis (2026-09-01) found NG1 hedging stopped on 2026-08-06 when the trigger was raised USD 2M to 3M and flagged hedge exit costs and unoptimised signals as the real bleed. Reece is asking Invast/OZ to publish remaining depth.
Next: Pepperstone to check with Invast/OZ on NG1 depth; Mahi to decide NG1 trigger appetite (USD 3M vs 2M) and the hedge venue review.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785164826669399 https://mahifx.slack.com/archives/C033K2P0RPT/p1788284401790649 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791898246094219

### crypto-hedging — Crypto spot hedger tuning and LP de-prioritisation
status: open · since: 2026-07-13 · last: 2026-10-08
State: After SI-vs-inventory debate in July, spot crypto hedgers were reworked in September (per-LP backstop rules, dynamic fill ratio) so LPs that keep cancelling/rejecting (LMAX EXPOSURE_CHECK_FAILURE 2026-09-03) are de-prioritised. MK moved the SI hedgers to counterparties 1001/1002 round-robin, reverted on 2026-10-05 after the tapaas change misbehaved, and asked for it back on 2026-10-08 (Rory restarting hedgers). Kraken is now an AUDUSD weekend fallback; B2C2 maintenance left USTAUD unpriceable on 2026-09-26/27.
Next: Rory to confirm the 1001/1002 config and hedger restart.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1783981698651339 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791443987998689

### echo-price-queries — Echo/Compass price and slippage discrepancy questions
status: open · since: 2026-10-07 · last: 2026-10-07
State: MK asked why a NDXUSD trade ticket's published price (30848.93/30854.10) differs from the chart (30859/30854); Isaac checking. Related unanswered-in-window queries: Reece's XAUUSD fills slipped to 4389.2 on 2026-09-08 (Rory to check) and Mariapaz's NETH25 jump (2026-08-20).
Next: Mahi to explain the NDXUSD ticket-vs-chart price.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791377823659449

### perps-pricing — Perp instruments: pricing, rollover and KRX
status: open · since: 2026-06-26 · last: 2026-10-07
State: Gold-i basis and Binance feed problems gave bad WTI (CL1USD-PERP) pricing on 2026-09-20, and Ruby found the Brent perp daily price adjustment not mirrored at rollover (clients capturing swaps). Isaac shipped a temporary fix (indicative 1 min before and 15 min after roll with continuity-pool failover incl. HRP_GOLDI, MahiMain PR 1168) and Binance was removed from non-XAU perp reference markets on 2026-09-25. KRXKRW-PERP was swapped to KRXUSD-PERP on 2026-10-07. XAGUSD-PERP is still unlaunched (Stephen asked 2026-09-02 about a Mahi-side blocker).
Next: Mahi to confirm the XAGUSD-PERP blocker.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782431997282909 https://mahifx.slack.com/archives/C033K2P0RPT/p1791389389028919

### infra-resilience — Crypto server reboots, failover sessions and patching
status: open · since: 2026-08-09 · last: 2026-10-05
State: Weekend crypto server restarts (an LDN reboot Aug 29 Beeks denied) led Mahi to move infra patches to weekday Monday windows (LDN 22:00 UTC, NYC 23:00 UTC, with advance notice). On 2026-10-05 Arun found the three NYC OZ failover MD/order sessions flapping every 7-8 minutes from TCP retransmits (packet loss; primary sessions healthy). Beeks cross-site link work is scheduled 17 Oct and 22 Oct.
Next: Arun to raise the packet loss with Beeks if it persists.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1786319051125299 https://mahifx.slack.com/archives/C033K2P0RPT/p1791213140868539

### data-access — Pepperstone DB, S3/Athena access and IP whitelists
status: open · since: 2026-06-29 · last: 2026-10-01
State: Tom Smith's London office IP was whitelisted on the CFD/FX/Crypto DBs on 2026-10-01 (Cloudflare egress IPs added 2026-09-03). Still open: Sebastian Andrews' request for PROD_LIVE_CLIENTDB access (2026-09-15, chased 09-28), James White's trade_id/client_order_id join outliers vs OneZero (2026-09-23, Sam Hewitt looking) and Reece asking whether the S3 bucket is backfilled before 2026-08-10.
Next: Mahi to answer Sebastian, James and Reece.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782731133990719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1790604196883929 https://mahifx.slack.com/archives/C06AR8MT8NT/p1790844572546109?thread_ts=1790686076.365529&cid=C06AR8MT8NT

### fx-a-book-hedging — FX A-book metals hedging and prime-broker limits
status: open · since: 2026-09-14 · last: 2026-09-28
State: A FX A-book loss in early September (all flow sent to ISPRIME at their request) exposed the hedger not being set up for that flow; PB LPs are off the table for metals (Standard Chartered refused after an XAGUSD run). Mahi widened metals hedging back to Finalto and Invast on 2026-09-17 and Daria's 2026-09-14 call with Stephen covered risk thresholds. A 2026-09-28 XAG short at ISP query was a Pepperstone-side position break.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619 https://mahifx.slack.com/archives/C06AR8MT8NT/p1790568412408529

### fx-si-sims — FX B-book SI/inventory sims for Pepperstone
status: open · since: 2026-08-27 · last: 2026-09-22
State: Stephen asked on 2026-08-27 for SI/inventory backtests for the FX B-book (pure warehousing, 17M January swings). Nathan's sims (2026-09-11) were reviewed by David Cooney (wanting NOP and margin metrics); on 2026-09-22 Stephen was happy and convinced pure B-booking is wrong, but his constraint is the prime-broker credit limit (USD 200M), which every simulated method exceeds.
Next: Nathan to rework artefacts toward risk within the USD 200M limit; Stephen to send exact credit numbers.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787786333971199 https://mahifx.slack.com/archives/C033K2P0RPT/p1790046562048089

### arb-classification — Dynamic arb classification false positives and realtime detection
status: watching · since: 2026-07-27 · last: 2026-09-02
State: Mahi tightened cycle badCheck yield (-1.5/M to -4/M) and enabled realtime arb detection on riskPathBBook (2026-08-21); the B-book arber list fell from ~700 to ~100 CPs by 2026-09-02 and trade-count thresholds went 10 to 30 at Reece's request. Gabriel still saw a new Chinese client (-8.87/M, 20M volume) missed on 2026-09-03. Watching: no activity since 2026-09-03.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785166480858439 https://mahifx.slack.com/archives/C033K2P0RPT/p1788388750800949

### margin-exploit-throttle — New-account margin exploits and order throttling
status: watching · since: 2026-07-30 · last: 2026-09-14
State: Pepperstone clients exploited margin validation (CPI-print bursts, small-deposit martingale). Diego asked for symbol-level throttling (2026-08-31); Daria proposed a realtime burst-trade classification (e.g. 100+ trades/min). Stephen promised more exploiting accounts (2026-09-14); Pepperstone would reject orders so false positives matter. Watching: nothing since.
Next: Stephen to send accounts; Mahi to decide on realtime classification.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785383994048729 https://mahifx.slack.com/archives/C06AR8MT8NT/p1788172536055649 https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### xau-spreads-toxic — XAUUSD spread algorithm and toxic gold flow
status: watching · since: 2026-08-13 · last: 2026-09-14
State: Shyam proposed a PSM-style XAUUSD spread algo (cap 18pt, avg near today's) that Stephen broadly liked (2026-08-24). On 2026-09-14 Stephen was talking about a 16c average next month and taking the proposal back internally; QQ EA signal detection is live and Pepperstone want its benefit quantified. Watching: waiting on Stephen.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1786664221546029 https://mahifx.slack.com/archives/C033K2P0RPT/p1787542551297439 https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### findings-athena-creds — Findings routine lacks Athena access
status: watching · since: 2026-09-01 · last: 2026-09-01
State: Andrew's findings routine has no credentials for the ring-fenced Pepperstone Athena account, so pepperstone-cfd findings ship unsized and skew/LR checks run config-only. Andrew calls this the highest-leverage fix on this client; no resolution seen. Watching.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1788284401790649

### polaris-migration — Spot crypto moving from Modulus to Polaris (SOW)
status: watching · since: 2026-08-21 · last: 2026-08-26
State: Stephen told Daria on 2026-08-21 that Pepperstone is dropping Modulus for spot crypto (new venue possibly Polaris); Liam argued for an SOW with an added-days clause or monthly exchange-MM fee and, after a call with the exchange team (2026-08-26), said the timeline is conservative and Stephen expects costs. No SOW seen in-window.
Next: Pepperstone to send integration info; Liam to scope the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1787289556446609 https://mahifx.slack.com/archives/C033K2P0RPT/p1787735062933889

## Arc
- 2021 — first (failed) negotiation; Mahi did ~3 months free goodwill work
- 2023-07-31 — Pepperstone board approves including CFDs
- 2023-12-21 — 3-year MSA signed (MFXEcho + Compass + Pulse, FX and metals)
- 2024-04 — Compass live in production for FX MM
- 2025-07-16 — 3rd Addendum: term to 2028-07-16, USD 115,088/mo from 2025-08-01, no termination for convenience
- 2025-Q4 — Modulus crypto exchange live with 6 AUD pairs
- 2026-Q1 — CFD licence signed; crypto SI profitable every week of 2026
- 2026-07-22 — CFD desk live (NY and LDN)
- 2026-08 — Tom Williams promoted to COO; Stephen Hendrie becomes main counterpart
- 2026-08-21 — Rob Bowen leaves Pepperstone; Pepperstone drops Modulus for spot crypto
- 2026-08-26 — Steven Reed (Modulus-side) no longer at Pepperstone
