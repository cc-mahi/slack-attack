---
slug: argamon
refs:
  vibepulse: ../VibePulse/.claude/clients/argamon.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: argamon
  hosts: ../MahiProduct/data/client-hosts.json          # entry: argamon
  wiki: null                                             # ../MahiProduct/wiki/clients/argamon.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Elan (Argamon CEO/principal)", role: "Principal contact / decision-maker", confidence: low}
  - {name: "Levi Ulman", role: "Argamon ops / connectivity", confidence: low}
  - {name: "Tom (Argamon)", role: "Argamon ops / daily trading", confidence: low}
  - {name: "Jonah Ink", role: "Argamon reconciliation / back-office", confidence: low}
  - {name: "Alex (Karnadi)", role: "Argamon back-office / rec", confidence: low}
  - {name: "Joanna Theofanous", role: "Argamon ops (client-side contact in mahi-argamon-operations)", confidence: low}
  - {name: "William (Argamon)", role: "Argamon ops (client-side contact in mahi-argamon-operations)", confidence: low}
last_catchup: 2026-07-13T07:04:17Z
---

## Status

- Stage: live, actively growing (new LPs, platform migration in progress)
- Integration: retail + insti + crypto, NYC only; OneZero→Centroid migration underway (target before Aug 1)
- Relationship: active, operationally intensive; ongoing rec disputes and infra expansion; contract being restructured (Mahi=retail, Toa=crypto/B2B/RI)

## Recent issues

> [open] 2026-07-06 — Toa LDN position rec break: 101k AUDCAD out, suspected over-hedge on INST-34 trades
> Levi investigating a Toa LDN rec break (101k AUDCAD out, doesn't look like real risk). Flagged INST-34 trades that went via `MARKETMAKING_HRP_RETAIL` channel instead of the usual `MARKETMAKING_HRP_RETAIL_GMG` as a possible cause. Lee Butts confirmed party/market are identical across the four channels so nothing obvious explains the missing 101k; Levi troubleshooting further on Argamon's side. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1783309851586399)

> [resolved] 2026-06-22 — CP 90000580 switched back to internalised; going offside → all brokered XAUUSD reverted to LPs
> Daria switched CP 90000580 back to internalised at Elan's request (it had been forcibly brokered to Toa). Up $6k from 90000580's trading on 2026-06-22 but internalised flow was going offside within 2 minutes (vs. onside as brokered). 2026-06-25: Daria reverted ALL brokered XAUUSD flow back to going to LPs from the NY4 (retail) environment, at Elan's request. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1782092790487579) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1782352799253379)

> [resolved] 2026-06-21 — XAUUSD twilight base spread losses: TOB config fix approved
> Another $1.5k retail loss in the XAUUSD twilight window. NY4 retail model TOB was 100oz at 8c (had been matched to the Toa retail model, now 25oz at 25c). Daria reached out to Elan; approved fix: drop TOB quantity to 25oz or 50oz, increase TOB spread to 15c, then mirror NYC beyond. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1782081899504989)

> [watching] 2026-06-11 — USDCHF ~$1k PnL loss at NY roll: MAHI_BENCHMARK_LDN added as LP
> CP 90002035 (unclassified) bought USDCHF at favourable prices during a ~15-min window over NY roll where most LPs were unstable and distribution price dipped slightly below market. Buys hedged ~4 mins later; by then YP was negative. Shyam added MAHI_BENCHMARK_LDN to USDCHF LP set and CP received fast-hedge tag to prevent recurrence. Before/after backtest (Jenkins #655/#656) confirms distribution price would have stayed more aligned with market. No further action expected. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1781148840004809)

> [watching] 2026-06-09 — Centroid FIX UAT: credentials resolved, incremental MD refresh testing underway
> Argamon ops (Levi) flagged Centroid unable to connect to the FIX integration sessions (PROD vs UAT credential mix-up). Inald provided correct UAT creds 2026-06-10; Levi confirmed passing to Centroid at 14:17 BST. 2026-06-23: Centroid now doing UAT incremental MD refresh testing — Levi requested IP whitelist for 185.125.204.156; Isaac created pricing-only FIX credentials (SenderCompId Argamon-Centroid-UAT-Prices, host 192.81.110.53:9010) and confirmed IP whitelisted via Beeks. Levi confirmed all good. 2026-06-30: Argamon requested new IP 192.109.23.20 whitelisted for Centroid UAT session (replacing 185.125.204.156); Isaac acknowledged (✓ reaction). [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1781000635571119) [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1781003145893419) [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1782182611235909) [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1782799990703719)

> [resolved] 2026-05-27 — YP reval errors fixed: CLIENT_PRICE_NYC → CLIENT_PRICE_RETAIL_NYC
> Daria switched the default client price market from CLIENT_PRICE_NYC to CLIENT_PRICE_RETAIL_NYC after YP (yield profile) reval jobs were throwing `IllegalArgumentException: CLIENT_PRICE_NYC/GBPJPY unavailable`. CLIENT_PRICE_NYC is the legacy insti model — wrong reference for retail. Fix applied ~02:00 BST 2026-05-27. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1779843264602109)

> [open] 2026-05-25 — XAUUSD toxic-flow rehab-cycle risk: FX/metals classification split planned
> Daria flagged a structural rehab-cycle problem: toxic XAUUSD CPs brokered to Toa receive wider spreads + passive hedging, which improves their yield and causes them to lose their toxic classification, after which they get internalised on tight spreads and become toxic again until reclassified. Fix options: static blacklist or tighter rehab criteria for metals. Daria plans to split FX and metal classifications on 2026-05-26 (moving metals positions from CLIENTS to CLIENTS_NYC) so changes can be made independently for metals. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1779681392035259)

> [resolved] 2026-05-21 — CP 104719 dual-channel classification: internalised under A_CLIENTS, brokered under A_CLIENTS_TOA
> Tom querying why CP 104719 is sometimes internalised, sometimes brokered within 12 minutes of each other. Rory explained: A_CLIENTS_TOA falls under CATCHALL//Dynamic-Broker execution profile; A_CLIENTS falls under CATCHALL//Dynamic-Dont B Book. Isaac confirmed 2026-05-22: the classification flipped for one order because CP 104719's 28-day yield was hovering near the rehab threshold — a single agent cycle (~few hours) can flip it, and trade B landed in a 2.5-hour window where rehab had succeeded before reclassifying back to broker. Tom satisfied. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1779357670831129)

> [resolved] 2026-05-19 — Toa insti_light XAUUSD spread config GUI error
> Elan unable to open XAUUSD spread config for CLIENT_PRICE_INSTI_LIGHT stream in Toa GUI. James fixed — misconfigured JSON name (copy-paste error) on the Toa config. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1779186517949549)

> [open] 2026-05-19 — TOA_CHI 100% CPU / Aeron meltdown: ~10 min pricing dropout + toxic-flow LP reject spike
> ~10 min dropout from TOA_CHI at ~14:30 BST. Separately, during a period where toxic-flow CPs were being auto-brokered, the designated LP had no price — causing high cancel/retry volume (Tom flagged "things going crazy"). Kate: LP pricing dropped out, retries drove reject spike; LP pricing recovered same session. James Furness also flagged 100% CPU causing an Aeron meltdown in CHI around the same time; root cause not yet published. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1779199627807509) [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1779200915226979) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1779211745957959)

> [open] 2026-05-18 — New CP 90001948 XAUUSD scalp + all XAUUSD brokered flow migrated to Toa
> New CP 90001948 (first day on platform) sold 600oz in 10 × 300oz clips, left Mahi long through a drop — $4k retail PnL hit 2026-05-18. Picked up as SIGNAL_FOLLOW+BROKER; will auto-broker from here. Daria also consolidated: all XAUUSD brokered flow now routing to Toa (wider spreads, tougher LR, CME hedging). Planned follow-on: split metals and FX into separate tenant profiles early next week (moving positions from CLIENTS to CLIENTS_NYC) to prevent XAUUSD flow contaminating FX signal/broker classification. Several other CPs showing similar yield profiles flagged; RI flagged as option. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1779116545067019) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1779141857043039) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1779151965234289)

> [resolved] 2026-05-15 — HRP booking config missing on Toa (trades not sent to HRP)
> Tom flagged trades not being sent to HRP from Toa. James confirmed missing `connectivity.booking.bookingSystemRouting` config on Toa; HRP asked to book manually while fixed. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1778840217972969)

> [resolved] 2026-05-13 — XAUAUD scalping: $5.9k retail loss from arb-protection misconfiguration
> CPs 105988 and 105990 (both ~6 days on platform) executed 106 small XAUAUD round-trips over ~16 mins during FX twilight. Root cause: `pricing.arbProtectionParameters` had UBS (sole XAUAUD LP) in reference markets but not `referencePriceMarketSelectors`, causing published quote to be clamped into UBS's wide twilight spread rather than using clean triangulated price (XAUUSD × AUDUSD). Shyam removed XAUAUD from arbProtectionParameters; pricing now uses pure triangulated price. Both CPs under monitoring. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1778648027949039)

> [watching] 2026-05-08 — XAUUSD signal switched to synapse
> Shyam changed XAUUSD signal from current to synapse, motivated by simple skew analysis. Will monitor pricing impact next week; watching for CPs picking off the model post-change. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1778211684932129)

> [watching] 2026-05-08 — Weekly P&L: $7.5k from 402m (week to date)
> Daria's mid-week update: 222m internalised, 180m brokered. Brokered flow decays quickly but stays onside (3x spread of internalised: $14/M brokered vs $47/M internalised). Two counterparties (928986, 928994) blacklisted from broker for now — bad couple of weeks but aggregate yield acceptable for internalisation. Net brokered spread $3.4k; internalisation P&L $4.1k (RoS 130%); LR P&L $1.4k mostly on brokered. Skew P&L had initial EURUSD open loss from arb but has fully recovered. Focus on skew and mid improvements (Shyam reviewing). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1778199139811789)

> [open] 2026-05-04 — TOA_CHI/A_EXTERNAL_WASH XAUUSD reject spike (quantity too large) — analytics support question unanswered
> Alert at 11:59–12:00Z: 98% reject ratio (93/95 orders) on TOA_CHI/A_EXTERNAL_WASH for XAUUSD from 1 counterparty (90000580), error `FIELD_VALIDATION_ERROR: quantity=TOO_LARGE, maximumShowQuantity=TOO_LARGE`. Justin Young forwarded the ZD ticket to internal-argamon asking who's on analytics support today; two +1 reactions but no reply in thread. As of 2026-05-08 still no thread reply — unresolved. Zendesk ticket: https://mahifx.zendesk.com/agent/tickets/22907. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777898434100499)

> [open] 2026-04-30 — Retail pricing degradation: wide spreads on majors / LR on retail published rate
> 2025-05-01: client (Tom) flagged majors 20-tick wide for ~2 hours. Will Carter identified LR was kicking in on the published rate and removed it from published. Separately Amir bounced retail pricers to include FSS markets and replace MWMS/BMSL. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746108590467959)

> [open] 2026-04-28 — XAUUSD brokerage to Toa expansion
> Daria added party 104881 to brokered-to-Toa for XAUUSD on argamon.NYC; plan is to migrate the softest of 104881/105048/105153/105681/105773 progressively to see if hedging to CME helps yield. Starting with softest first. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777335260425589)

## Notable topics

- 2026-05-03 — XAUUSD retail NY4→CHI hedging disabled: retail achieving positive spreads; CHI giving negative spreads so hedging there turned off. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777845150173619)
- 2026-05-04 — EURUSD mid formation: Elan approved adding all LPs back into mid (NY now retail-only). Shyam added DB_RCTV_NWPB_1, EDGW_RCTV_NWPB_1, GTSX_RCTV_HRP_2 as supplementary LPs; backtests show reduced spiky pricing and arb opportunities. Adaptive mid logic also added to betaRetailPricer1 for EURUSD; FI/skew PnL review ongoing. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777855717442529) [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777869938380839)
- 2026-05-13 — Toa LD4 TOB signal data missing: Elan flagged signal data not showing in Echo TOB for toa_argamon.LDN XAUUSD. Daria found signals not persisted since last system reboot; fixed after restart. Backfill not possible. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1778634120272459)
- 2026-06-05 — Compass upgrade planned for weekend (06-07/08): Liam notified client in mahi-argamon-operations. Client acknowledged. Monitoring planned over market open. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1780673110439059)
- 2026-06-10 — Reference price market selector (LP set) changes for XAU/EUR/GBP: Shyam updated referencePriceMarketSelectors after lead-lag and TOB analysis over large price moves and opens. XAU: removed NWM_RCTV_HRP_1 + MAHI_BENCHMARK_LDN, added COMZ_RCTV_NWPB_1. EUR: removed GTSX_RCTV_HRP_2, added COMZ_RCTV_NWPB_1. GBP: added UBS_RCTV_HRP_1. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1781062155159539)
- 2026-06-12 — XAUUSD over-hedge investigation (26 May): Argamon ops (Levi) asked in mahi-argamon-operations how to narrow a search for a potential 1-lot XAUUSD over-hedge on 26 May. Shyam confirmed no over-hedge from Mahi's side; Levi noted they believe it's retail but lack data beyond EOD position rec to confirm. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1781234757662239)
- 2026-06-18 — JPY crypto hedging mechanism explained: Tom asked how BTCJPY client flow is hedged given Mahi hedges as BTCUSD — what happens to the JPY exposure? Isaac: USDJPY hedged through same HRP feeds as retail. Amir: Compass hedging is bucketed by asset (not 1-to-1 per client trade); there is no direct mapping between a specific client JPY crypto trade and a specific USDJPY hedge leg. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1750233313457629)
- 2026-06-23 — Centroid UAT incremental MD refresh testing: IP 185.125.204.156 whitelisted, new pricing-only FIX credentials created (Argamon-Centroid-UAT-Prices / MahiFX-Centroid-UAT-Prices on 192.81.110.53:9010). Centroid advancing UAT work ahead of OneZero→Centroid migration. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1782182611235909)
- 2026-07-03 — Toa Chicago deploy blocked pending release branch + regression: David Cooney requested pushing latest build to Toa Chicago to support options connectivity Lee Butts is writing. Lee replied it needs a new release branch cut and regression testing first — not ready to go. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1783049787092519)
- 2026-06-30 — Centroid UAT IP update: Argamon ops requested whitelist of new IP 192.109.23.20 for existing UAT session, replacing previously whitelisted IP. Isaac ✅. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1782799990703719)
- 2026-07-06 — NOMU_RCTV_NWPB_1 test-trade FIELD_VALIDATION_ERROR: needed UI enablement; Isaac fixed within the same exchange, client confirmed working. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1783315711421619)
