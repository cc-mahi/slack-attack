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
last_catchup: 2026-10-19T07:09:25Z
status: active
---

## Now
Live on FX, Crypto exchange (Modulus) and CFD (desk live since July), on a 3-year MSA to 2028-07. Three fronts: roll-time arbitrage across majors (Mahi raised roll LR 2026-10-15), FX B-book SI/inventory sims (credit limit USD 200M the constraint) and crypto PSM scoping. A CPI-print gateway incident on 2026-10-14 is awaiting a full written response to Diego. A London estate connectivity incident on 2026-10-16 resolved the same day; XBTUSD skew arbers (2026-10-18) and missing HRP data in London since 2026-10-18 are live. Pepperstone is also moving spot crypto off Modulus (to "Polaris") with an SOW to come.

## Streams

### roll-arb — Roll-time arbitrage on FX majors and Mahi's defensive LR/widening
status: open · since: 2026-07-17 · last: 2026-10-19
State: Arb at the NZD/SGD roll started on NZDUSD and spread to EURCHF, AUDNZD, EURUSD, USDCAD (USD 264M on 2026-10-05) and EURNZD (USD 90M, 2026-10-14). NZDUSD was closed out by Stephen after roll-window LR plus defensive FM-T-0-30000 widening cut roll volume 87% (35.5M/day to 4.7M/day by 2026-09-23); later pairs got per-instrument widening. After a call with Stephen, Ruby and Antonio on 2026-10-15 Mahi switched to an across-the-board roll LR on all majors (channel cap USD 25/M to 200/M, NZD/USD stay 600/M, counterparty cap 200/M, tighter global bucket) and reduced some widening; to be monitored over the next rolls, and Pepperstone want a walkthrough to tweak it themselves. On 2026-10-19 Shyam tightened the global roll LR further, agreed with Stephen (EUR, GBP, USD, AUD, JPY, CHF, CAD; roll and Singapore Monday: burst 250k to 0, refill 500k/s to 250k/s); Stephen is considering A-booking some of this flow for market impact. Stephen also changed the toxic NYC pool (PB instruments now to Invast_Defensive, not SCB), which needs a pool/SOR restart; the NYC SOR does not fail over to London and a restart rejects brokered orders for a few minutes, so Nathan scheduled it for just before 5pm NYT, ahead of roll.
Next: Shyam to show Stephen's team the roll LR set-up; Nathan to do the NYC SOR restart just before 5pm NYT on 2026-10-19.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1784250309662259 https://mahifx.slack.com/archives/C033K2P0RPT/p1792377289163719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792384520826769?thread_ts=1792384520.826769&cid=C06AR8MT8NT

### crypto-btc-arb — XBTUSD skew arbers hitting crypto pricing
status: open · since: 2026-10-18 · last: 2026-10-19
State: On 2026-10-18 Gabriel flagged ten accounts of one client (over USD 40M traded at about -55/M spread yield) plus another account (-8.41/M on 8.7M) hitting XBTUSD. Shyam says they were skew arbing so negative spread yield is expected; the automated classifier had already marked most as arbers (executed only from the continuity pool plus markup) and he offered to whitelist them against rehabilitation, which Stephen accepted. Shyam is reviewing the skew config (FI otherwise performing well). On 2026-10-19 MK asked for skew to be turned off or toned down a lot over the weekend and Isaac said he would look into it that day.
Next: Isaac to review crypto skew sizing and the weekend setting; Shyam to whitelist the arbing accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792355023754729?thread_ts=1792355023.754729&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C06AR8MT8NT/p1792391722703229?thread_ts=1792355023.754729&cid=C06AR8MT8NT

### hrp-ld-md — HRP market data missing in London after tag change
status: open · since: 2026-10-18 · last: 2026-10-19
State: From about 07:45 UTC on 2026-10-18, when HRP-Agg quotes on all symbols were cancelled, the PEP-LD4_Q feed resumed tagged HRP-2, while Mahi's HRP_LDN market mapping is still HRP-Agg, so no HRP data is reaching London. Shyam asked whether the change is expected or the mapping should move to HRP-2; Diego says it looks like an HRP-side change and at 03:44 BST on 2026-10-19 was still waiting on HRP. This overlaps the HRP hedging weight in crypto-hedging.
Next: Diego to get HRP's answer; Shyam to update the mapping to HRP-2 if confirmed.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792362092980019?thread_ts=1792362092.980019&cid=C06AR8MT8NT

### cfd-pricing-feeds — CFD feed gaps, reference-market changes and indicative alerts
status: open · since: 2026-09-22 · last: 2026-10-16
State: Recurring CFD price-feed questions. USDCLP root cause (Nathan, 2026-09-22): priced from QRT_NYC and FINALTO_LDN; Finalto starts ~12:30 UTC and QRT_NYC has sent no USDCLP since 17 Sep (also a gap 17-21 Aug) while its FIX session is healthy, so it is a QRT-side issue and Pepperstone were to raise it with OneZero; MK disabled NAPN and USDCLP on 2026-09-24 meanwhile. Also indicative-pricing alerts and the ~20s LD delay above. On 2026-10-15 MK asked for the primary reference on ten indices (AUS200, UK100, EUSTX50, FRA40, CHINAH, NETH25, HK50, SWI20, CN50, SCI25) to move to Velocity in beta ahead of extended hours at the DST change. On 2026-10-16 MK flagged clients exploiting latency on the IG feed (known, IG fixing; no other LP prices UKOUSD/USOUSD, so no backup); Isaac proposed a proxied mid of each forward pair's cash partner as primary mid with IG as secondary fallback and spreads kept in line with IG, MK agreed to put it in beta, pending a proxy restart so likely next week. Isaac also needs to deploy the latest 26.3 to the CFD pricers for a primary/secondary fix.
Next: Mahi to make the Velocity reference change in beta; Isaac to prepare the proxied-mid IG fallback for beta and deploy 26.3 to the CFD pricers; Pepperstone to chase OneZero/QRT on USDCLP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1790096194336949 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792061213615249 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792155095799099?thread_ts=1792155095.799099&cid=C06AR8MT8NT

### gateway-cpi-reject — NY gateway kill switch on CPI print, SYSTEM_CLOSED rejects
status: open · since: 2026-10-14 · last: 2026-10-15
State: On 2026-10-14 around 12:30 GMT a Mahi NY distribution gateway tripped its kill switch on the CPI print. Internally Liam traced it to a bad Last Look latency spike on clientDistributionGateway4 that had already recovered, so the four books were switched back on from the dashboard. XAUUSD orders on stream Mahi_B_NY_4 were rejected SYSTEM_CLOSED and the OZ hub retried ~25k orders on the London backup stream. Mariapaz asked why; Diego separately reported a ~20s LD price delay (Rory 2026-10-15: distributed price was updating through, logs being pulled). Nathan sent only a holding reply and wants a fuller incident response.
Next: Mahi (Rory/Nathan) owes Diego the log-backed explanation of the kill-switch trip (latency-spike cause not yet shared) and the LD delay.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791997243862479 https://mahifx.slack.com/archives/C033K2P0RPT/p1791981251222909 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792060740686789?thread_ts=1792018491.050639&cid=C06AR8MT8NT

### crypto-yield-psm — Crypto yields down; PSM scoping for XBTUSD/XETUSD
status: open · since: 2026-10-06 · last: 2026-10-15
State: Crypto spread yield fell to ~USD 200/M versus 350-450 historically; Isaac puts about half down to BTC's rally against a flat USD 15/BTC spread, the rest to lower volatility and LP tightening. Isaac proposed PSM to MK (agreed 2026-10-08) and on 2026-10-15, after a call with MK and Andrew, screened configs: a "middle ground" widen/tighten gives about +9.2/M on XBTUSD and +48.5/M on XETUSD; full backtest and Compass sim verification is under way. Andrew also notes Claude RoS/PnL tracking does not match Compass Account Summary for crypto SI.
Next: Isaac to finish engine verification (5 variants on 8 and 11 Oct flow) and send MK PnL/spread numbers for PSM fully active / defensive only / 10% widening.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1791285982179839 https://mahifx.slack.com/archives/C033K2P0RPT/p1792068068772829

### crypto-hedging — Crypto spot hedger tuning and LP de-prioritisation
status: open · since: 2026-07-13 · last: 2026-10-15
State: After SI-vs-inventory debate in July, spot crypto hedgers were reworked in September (per-LP backstop rules, dynamic fill ratio) so LPs that keep cancelling/rejecting (LMAX EXPOSURE_CHECK_FAILURE 2026-09-03) are de-prioritised. MK moved the SI hedgers to counterparties 1001/1002 round-robin on 2026-10-04 (timed with the tapaas change), reverted on 2026-10-05 when that misbehaved, and had it reinstated on 2026-10-08 (Rory bounced the hedgers). On 2026-10-15 MK noticed SI hedge volume to HRP falling while LMAX won most flow; Isaac found HRP was excluded from some hedger rules by legacy config (feared over-hedging on its crossed book), then added it to all the rules (to be reviewed). Kraken is now an AUDUSD weekend fallback; B2C2 maintenance left USTAUD unpriceable on 2026-09-26/27.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1783981698651339 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792071994735809?thread_ts=1792071994.735809&cid=C06AR8MT8NT

### fi-skew-tuning — FI/skew/LR sizing and signals across FX, CFD and metals
status: open · since: 2026-08-18 · last: 2026-10-14
State: Reece flagged FI PnL slipping (2.9/M vs 4.0/M, early Aug); Isaac moved XAUUSD to flow-price-thresh and FI PnL recovered to 4.2/M. EURUSD hit USD 9.17/M at a 0.5 pip skew cap, but Reece had the cap put back to 0.1 pip on flow-price-thresh alone (2026-09-22); On 2026-10-14 Isaac swapped FX majors (EURUSD included) to IFM-based benchmark adjustments. On CFD, skew was raised from 20% of base spread after Nathan's beta shadow test; MK approved promoting HSIHKD, JPXJPY and XAUUSD-F and moving NDXUSD to the price signal on 2026-10-08, changes made, monitoring. CFD LR was also reworked in September after LR-caused limit-order cancels: MK disabled channel LR, global default LR cap cut from USD 1000/M to 300/M, signals limited to oils, NDX, DOW, SPX (CAC at 40%).
Next: Nathan to report on promoted CFD skew performance.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787060801310749 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791453538861039?thread_ts=1788929145.526369&cid=C06AR8MT8NT https://mahifx.slack.com/archives/C033K2P0RPT/p1791992133214739

### classification-upload — Pepperstone's own counterparty classification upload (SOW)
status: open · since: 2026-05-19 · last: 2026-10-13
State: MK/Reece have asked since May for an automated S3 upload of their external classifications. On 2026-10-13 Liam said MK has resurfaced and that Mahi will wrap the existing S3-based implementation in the SOW Pepperstone are expecting, aiming to be paid for it.
Next: Liam to issue the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919 https://mahifx.slack.com/archives/C033K2P0RPT/p1791904949863369

### cfd-hedging — CFD inventory hedger rejections, LP liquidity and risk controls
status: open · since: 2026-07-27 · last: 2026-10-13
State: The CFD inventory hedger keeps hitting LP limits. Velocity cancelled 241/250 HSTHKD hedges (2026-09-11); price-precision rejects were fixed with hedger-only overrides (HSTHKD, softs at 1dp, 2026-09-17..22; indices pending review). NG1 clips reject on 26Degrees (2026-09-25, 09-29, 10-13): William advised smaller clips, Isaac raised VaR reduction per second (600 to ~2000-2500) on 2026-09-29, and Rory showed the LP book resets to 20k within ms of each fill while the hedger sizes off rolling fill ratios, so it cannot see what is left. IG liquidity limits hit WHEAT (limit raised temporarily, Reece wants 100k clips). Andrew's analysis (2026-09-01) found NG1 hedging stopped on 2026-08-06 when the trigger was raised USD 2M to 3M and flagged hedge exit costs and unoptimised signals as the real bleed.
Next: Reece to ask Invast/OZ whether NG1 depth is capped and whether the book can show remaining depth; Mahi to decide NG1 trigger appetite (USD 3M vs 2M) and the hedge venue review.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785164826669399 https://mahifx.slack.com/archives/C06AR8MT8NT/p1791898246094219

### perps-pricing — Perp instruments: pricing, rollover and KRX
status: open · since: 2026-06-26 · last: 2026-10-07
State: WTI (CL1USD-PERP) mispricing on 2026-09-20 was Goldi dropouts leaving a stale basis against Binance (price ~0.45 high until Goldi returned); Binance was removed from non-XAUUSD perp reference markets on 2026-09-25 (kept on XAUUSD). Ruby found the Brent perp daily price adjustment not mirrored at rollover (clients capturing swaps); Isaac added a 16-minute force-indicative (1 min before, 15 after) failing over to marked-up HRP_GOLDI, and the basis-jump fix (MahiMain PR 1168) deployed 2026-09-30, with force indicative off on the beta pricer only to compare at the next funding basis adjustment (MK wants prod left on). KRXKRW-PERP rejects were fixed by a 2026-09-29 release, then the perp was swapped to KRXUSD-PERP on 2026-10-07 and priced in NY and LD. XAGUSD-PERP is still unlaunched: Daria found no Mahi-side blocker on 2026-09-02, so Pepperstone had to finish config and test.
Next: Isaac to compare beta vs prod at the next funding basis adjustment; Pepperstone to launch XAGUSD-PERP.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782431997282909 https://mahifx.slack.com/archives/C06AR8MT8NT/p1789944667574059 https://mahifx.slack.com/archives/C033K2P0RPT/p1791389389028919

### infra-resilience — Crypto server reboots, failover sessions and patching
status: open · since: 2026-08-09 · last: 2026-10-05
State: Weekend crypto server restarts (LDN reboot Aug 29, Beeks denied) led Mahi to move infra patches to weekday Monday windows (LDN 22:00 UTC, NYC 23:00 UTC, with advance notice). On 2026-10-05 Arun found the three NYC OZ failover MD/order sessions flapping every 7-8 minutes from TCP retransmits (packet loss; primary sessions healthy). Beeks cross-site link work is scheduled 17 Oct and 22 Oct.
Next: Arun to raise the packet loss with Beeks if it persists.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1786319051125299 https://mahifx.slack.com/archives/C033K2P0RPT/p1791213140868539

### data-access — Pepperstone DB, S3/Athena access and IP whitelists
status: open · since: 2026-06-29 · last: 2026-10-01
State: Tom Smith's London office IP was whitelisted on the CFD/FX/Crypto DBs on 2026-10-01, though Pepperstone's Sam Dammers said only dedicated Cloudflare IPs should be used. Still open: Sebastian Andrews' PROD_LIVE_CLIENTDB access (2026-09-15) still fails on TCP 3306 from his Cloudflare WARP address after Mahi whitelisted two Cloudflare IPs and sent the failure to Beeks; he suspects his own Cloudflare, last chased 09-28. Also James White's trade_id/client_order_id join outliers vs OneZero (2026-09-23, Sam Hewitt looking) and Reece asking whether the S3 bucket is backfilled before 2026-08-10.
Next: Mahi to answer Sebastian, James and Reece.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1782731133990719 https://mahifx.slack.com/archives/C06AR8MT8NT/p1790844572546109?thread_ts=1790686076.365529&cid=C06AR8MT8NT

### fx-a-book-hedging — FX A-book metals hedging and prime-broker limits
status: open · since: 2026-09-14 · last: 2026-09-28
State: A FX A-book loss in early September (all flow sent to ISPRIME at their request) exposed the hedger not being set up for that flow; PB LPs are off the table for metals (Standard Chartered refused after an XAGUSD run). Mahi widened metals hedging back to Finalto and Invast on 2026-09-17 and Daria's 2026-09-14 call with Stephen covered risk thresholds. On 2026-09-18 ISPRIME cancelled many XAUUSD hedges (it dislikes certain client tags;) and Daria applied per-LP backstop logic and switched the A-book hedger to round-robin over 51 look-alike tags, agreed by Stephen and MK. A 2026-09-28 XAG short at ISP query was a Pepperstone-side position break.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619 https://mahifx.slack.com/archives/C06AR8MT8NT/p1790568412408529

### fx-si-sims — FX B-book SI/inventory sims for Pepperstone
status: open · since: 2026-08-27 · last: 2026-09-22
State: Stephen asked on 2026-08-27 for SI/inventory backtests for the FX B-book (pure warehousing, 17M January swings). Nathan's sims (2026-09-11; David Cooney wanted NOP and margin metrics) went to Stephen on 2026-09-22 and he was happy and convinced pure B-booking is wrong, but his constraint is the prime-broker credit limit (USD 200M), which every simulated method exceeds.
Next: Nathan to rework artefacts toward risk within the USD 200M limit; Stephen to send exact credit numbers.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1787786333971199 https://mahifx.slack.com/archives/C033K2P0RPT/p1790046562048089

### arb-classification — Dynamic arb classification false positives and realtime detection
status: watching · since: 2026-07-27 · last: 2026-09-02
State: Mahi tightened cycle badCheck yield (-1.5/M to -4/M) and enabled realtime arb detection on riskPathBBook (2026-08-21); the B-book arber list fell from ~700 to ~100 CPs by 2026-09-02 and trade-count thresholds went 10 to 30 at Reece's request. Realtime gates are USD 50M volume, 50 fills, worse than -5/M over a rolling hour (runs beside the cycle; rehabilitation stays on the cycle good checks), and the classified list was reset to 39 problem CPs, with Reece and Stephen happy. Gabriel still saw a new Chinese client (-8.87/M, 20M volume) missed on 2026-09-03. Watching: no activity since 2026-09-03.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1785166480858439 https://mahifx.slack.com/archives/C033K2P0RPT/p1788388750800949

### margin-exploit-throttle — New-account margin exploits and order throttling
status: watching · since: 2026-07-30 · last: 2026-09-14
State: Pepperstone clients exploited margin validation (CPI-print bursts, small-deposit martingale). Diego asked for symbol-level throttling (2026-08-31); Daria proposed a realtime burst-trade classification (e.g. 100+ trades/min). Stephen promised more exploiting accounts (2026-09-14); Pepperstone would reject orders so false positives matter. Daria: the existing 150 orders/1000ms per-counterparty throttle cannot be scoped to new accounts or symbols without a dev change; MK then asked for a per-timezone / NZDUSD override, which looks unanswered.
Next: Mahi to answer MK on a timezone/NZDUSD-scoped throttle override (and raise the dev change); Stephen to send accounts.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1788172536055649 https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### xau-spreads-toxic — XAUUSD spread algorithm and toxic gold flow
status: watching · since: 2026-08-13 · last: 2026-09-14
State: Shyam proposed a PSM-style XAUUSD spread algo (cap 18pt, avg near today's) that Stephen broadly liked (2026-08-24). On 2026-09-14 Stephen was talking about a 16c average next month and taking the proposal back internally; QQ EA signal detection is live and Pepperstone want its benefit quantified. Watching: waiting on Stephen.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1789365103971619

### findings-athena-creds — Findings routine lacks Athena access
status: watching · since: 2026-09-01 · last: 2026-09-01
State: Andrew's findings routine has no credentials for the ring-fenced Pepperstone Athena account, so pepperstone-cfd findings ship unsized and skew/LR checks run config-only. Andrew calls this the highest-leverage fix on this client; no resolution seen. Watching.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1788284401790649

### polaris-migration — Spot crypto moving from Modulus to Polaris (SOW)
status: watching · since: 2026-08-21 · last: 2026-08-26
State: Stephen told Daria on 2026-08-21 that Pepperstone is dropping Modulus for spot crypto (new venue possibly Polaris); Liam argued for an SOW with an added-days clause or monthly exchange-MM fee and, after a call with the exchange team (2026-08-26), said the timeline is conservative and Stephen expects costs. Daria thinks Pepperstone are already committed to Polaris, so alternatives (Toa, Adaptive accelerator) look moot. No SOW seen in-window.
Next: Pepperstone to send integration info; Liam to scope the SOW.
Refs: https://mahifx.slack.com/archives/C033K2P0RPT/p1787289556446609 https://mahifx.slack.com/archives/C033K2P0RPT/p1787735062933889

### ld-estate-incident — London estate inter-region connectivity incident
status: closed · since: 2026-10-16 · last: 2026-10-16 · closed: 2026-10-19
State: On 2026-10-16 around 09:30 UTC Pepperstone saw latency and disconnections on LD adapters to the NY hub and NY adapters to the LD hub; Liam confirmed Mahi's London estate was having issues and advised relying on NY-NY and LD-LD, which Georgios did from the maker controls. Only cross-connections were affected. Liam reported recovery at 12:16 BST and resolution at 12:29, and inter-region links were re-enabled. Arun separately saw a CFD London admin host go down that morning. No root cause was given in channel.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1792142815121549 https://mahifx.slack.com/archives/C06AR8MT8NT/p1792142873267079?thread_ts=1792142873.267079&cid=C06AR8MT8NT

### echo-price-queries — Echo/Compass price and slippage discrepancy questions
status: closed · since: 2026-10-07 · last: 2026-10-07 · closed: 2026-10-15
State: Answered. NDXUSD ticket-vs-chart gap: published price is the price at request (about 50ms before fill, start of the last look window), same as the blotter (Isaac, 2026-10-07). Reece's XAUUSD fills at 4389.2 on 2026-09-08 were a 50ms last-look price move plus global LR taken at fill; tick logs had rolled off and Pepperstone may send a fresher example.
Refs: https://mahifx.slack.com/archives/C06AR8MT8NT/p1791377823659449

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
