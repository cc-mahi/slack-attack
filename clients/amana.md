---
slug: amana
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/amana.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: amana
  hosts: ../MahiProduct/data/client-hosts.json          # entry: amana
  wiki: ../MahiProduct/wiki/clients/amana.md
channels:
  internal-amana: C08T42TMKU3
  mahi-amana: C08SYSMP0EB
contacts:
  - {name: "Karen Montero", role: "ops / test trading liaison"}
  - {name: "Nikos", role: "primary desk contact: skew, LR tuning, migration roadmap, board-level asks"}
  - {name: "Princess Rosete", role: "test trading / ops liaison"}
  - {name: "Hadeel Salah", role: "dealer / ops: instrument go-lives, position updates, spread config uploads", confidence: low}
  - {name: "Mohamad El Masri", role: "ops: manual hedging, position adjustments, IP whitelisting", confidence: low}
  - {name: "Clifford Jay Cana / Jake Denley Alvaro / Maynard Notario / Riordan Bobis / John Carlo Desierto", role: "PH NOC: monitoring, rejections, slippage, contract specs", confidence: low}
  - {name: "Andreas Kleanthous / Mohamad Malkani / Rafik Mansour", role: "ops: futures expiry, settlement and start-date notices, Echo access", confidence: low}
  - {name: "Omar Maatouk", role: "ops: pricing / hedging config requests, rejection reports", confidence: low}
  - {name: "Ali Wehbe", role: "ops: energy futures / oils product specs", confidence: low}
  - {name: "Ahmad Hashem", role: "ops: rejection reports on Mahi_B sessions", confidence: low}
last_catchup: 2026-10-16T07:05:35Z
status: active
---
## Now
Amana is migrating everything onto Mahi in stages and is live on A-book metals/indices/energies, crypto (7 more GCEX coins 10-01), SI energies (since 09-11) and SI indices books, with FX B-book going live this week (EURUSD/GBPUSD/USDJPY on 10-14, EURJPY/GBPJPY next). Nikos drives and escalates fast. Open pain points: A-book skew/yield value (Mahi bills mostly on FI and LR PnL), pricing load, hedger stalls (HSI, swapfree) and recurring missing SI Indices PnL.

## Streams

### fx-metals-rollout — FX B-book and XPT/XPD go-lives
status: open · since: 2026-09-25 · last: 2026-10-15
State: XPT/XPD went live 10-07 (pricing set to Jump only after CMC was ~$10 off). FX B-book flow went live 10-14 for EURUSD/GBPUSD/USDJPY into B_OFF_BOOK_CLIENTS with no hedger by Amana's choice; Amana is moving EURJPY/GBPJPY pricing and B-book 10-15, asked for FX spread aggregation like XAUUSD (10-12), and for all FX quantity config HP 0.001 / Non-HP 1000 / LP 1000. Open: unhedged USDJPY on A House (10-14) and a TOB showing 500K vs the 250K Amana defined (10-15).
Next: Mahi to answer the USDJPY exposure and TOB questions; confirm FX qty config and spread aggregation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790335963373189 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792050663738809

### vip-feed — Third (VIP) pricing feed for XAU/XAG
status: open · since: 2026-10-08 · last: 2026-10-14
State: Nikos asked 10-08 for a third feed for VIP/A-book swapfree clients, XAU/XAG spot and futures only, starting at 500 with more depth; Rory approved. CLIENT_PRICE_VIP_LDN pricers were added 10-08; on 10-14 Nikos could not select the model in the spread-config GUI and asked for CMC only instead of the LMAX+CMC aggregate (Rory removed LMAX from MWMS for XAU/XAG).
Next: Amana to say whether the VIP feed needs testing; Mahi to fix the spread-config selector.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1791457134754879 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791975764084889

### last-look-tuning — Last look and TP slippage
status: open · since: 2026-08-20 · last: 2026-10-14
State: Clients complain about slipped TP limits (filled after last look at a worse price) and Nikos wants to cut last look from 50ms to 25ms then 10-15ms via the execution profile; Nathan is checking for a lower limit.
Next: Nathan to confirm minimum last-look setting.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787200767810479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791953832245899

### analytics-data-asks — Yield profiles, party IDs and data access
status: open · since: 2026-08-17 · last: 2026-10-13
State: Nikos and ops keep asking how to read yield profiles (client vs external markouts, NULL timeframes 10-07, B_OFF_BOOK_CLIENTS vs OFF_BOOK_CLIENTS party IDs 10-13) and for per-client skew data. Yield profile "external" is LP markouts against a reference mid (CMC_CENTROID for XAU). Nathan (10-02) pointed to the Compass positions tab and watchRiskBook for party-to-hedger mapping, which Nikos cannot open. Account-summary P&L was disputed 09-29/30 (WTD -426K; SI Indices -31K vs -8K by query).
Next: Mahi to answer the party ID, yield profile NULL and account-summary P&L questions.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786982712342769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791890549480249

### si-books — SI energies and SI indices books
status: open · since: 2026-08-17 · last: 2026-10-12
State: Energies SI went live 09-11 (time-based, 4h, 500K VaR); indices SI went live 09-25 (1h then 4h transfer, 100K VaR total) after a position flatten and rebuild. SI PnL keeps going missing (Energies 09-28; Indices 09-25, 09-28, 09-30, 10-05, again 10-12): root cause so far is a VIX position with no pricing (VIX pricing put live 10-05, VIXUSD tested 10-06), partly patched by adding VIX to base spreads and CPL. Nikos called the SI PnL drop alerts inaccurate (10-01, 10-06); Cameron cut them to the TOTAL book with a shorter window and Isaac made them alert-only 10-07.
Next: Mahi to fix SI Indices PnL for good (Nathan, 10-12).
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786981181951769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791774621350149

### hp-gateway-precision — High-precision (HP2) gateway and quantity precision
status: open · since: 2026-08-13 · last: 2026-10-09
State: HP2 distribution gateway (mobile/HP clients up to 8dp) went live after 08-18 testing. The 08-23 XAU/XAG increment mismatch rejected ~120k orders in ~20 min (permanent fix unconfirmed on 09-01). By 09-10 all B-book HP clients were moved, but Amana still B-booked the fraction of A-book HP trades and passed Mahi whole units only (change pending). Mahi can fill 1e-8 over the requested qty on internalised fills above ~1,000 (Sam 09-22; repeat 10-05; dev fix raised 10-07). Since the 10-08 rollover some HP accounts again hit the regular gateway and were rejected for increment/min size (Shyam 10-09).
Next: Amana to fix HP vs non-HP account routing; Mahi dev to fix the 1e-8 over-fill, confirm the permanent quantityDefinition fix is live and send Nikos the (unsent) RCA response.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786632001568829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791511397779419

### pricing-load-latency — Pricing model load and latency
status: open · since: 2026-08-20 · last: 2026-10-08
State: 219 instruments on CLIENT_PRICE_LDN caused an XAU/XAG pricing gap on 08-20 (pre-live instruments moved to a staging model). Nikos's lead-lag/4ms publish complaints (09-29, 10-01) were judged normal by Mahi (+1ms median, p99 9ms), but Isaac removed three unused arb hedgers from trading-1; a 09-30 NUMA move plus BMSL 5ms to 50ms cut worst pricer cycle from 16-17ms to 10-11ms. FAT feed now prices only XAU/XAG spot and futures (10-07/08), the default client price market moved to CLIENT_PRICE_ABOOK_LDN, and CLIENT_PRICE_LDN is to be cut to XAU, XAG and their futures.
Next: Isaac to complete the instrument reduction on CLIENT_PRICE_LDN.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787240208405969 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791451961676079

### client-tag-passthru — Client login tag for CMC dynamic logins
status: open · since: 2026-09-28 · last: 2026-10-06
State: CMC needs dynamic FIX API client logins, so Amana wants to send them on tag 109 and have Mahi consume and echo them. Rory (09-28) said execution reports do not return 109 today and he would check; a call was being arranged 10-05/06, outcome not seen.
Next: Mahi to say whether tag 109 can be consumed and returned.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790602136754039 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791212038784569

### futures-expiry-recs — Futures rolls, expiries and position adjustments
status: open · since: 2026-08-17 · last: 2026-10-15
State: Amana posts expiry and start notices and Mahi zeroes positions at EOD. On 10-15 Amana announced CrudeOilX6 (Nov) settlement (zero all positions) and CrudeOilF7 (Jan) start 10-16; picking up F7 needed a re-subscribe on Mahi_CMC_FIX, done by Shyam that night with a brief CMC_CENTROID pricing gap and the feed confirmed. Earlier: SI IDX futures rolled U to Z on 09-24 by CSV import, UKO futures rolled 09-28, manual position adjustments continue, and the 09-17 DOWFUT-U expiry spammed IG rejections because Amana had not set it close-only.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786993422025149 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792103701318669

### crypto-rollout — Crypto go-live and hedging
status: open · since: 2026-08-17 · last: 2026-10-01
State: First cryptos (XRP, SOL, XET) went live 09-04 and BTC 09-21. On 10-01 Amana went live with seven GCEX coins (ADA, AAVE, AVAX, DOG, DOT, LTC, TRX) after Mahi-side tests and a position import on a huddle, without telling Mahi it had enabled them (Rory asked for notice). hybridHedgerCrypto1 stopped itself three times on 09-21 on GCEX_CENTROID partial IOC residuals; Amana used FOK 09-22 to 09-28 until GCEX fixed the terminal message. Crypto pricer cycle times rose after restarts (SHIUSD/PEPEUSD, ZD-23543, root cause open).
Next: Daria's ticket ZD-23543 root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786963129189029 https://mahifx.slack.com/archives/C08T42TMKU3/p1790858011054809

### hsi-hedger-stalls — HSIHKD hedger stalling and size mismatches
status: open · since: 2026-09-09 · last: 2026-09-30
State: HSI hedging moved from CMC to Jump on 09-09; dealing wanted LMAX (09-21, pending Amana's confirmation: different price bases). The CFD hedger left exposure uncleared on 09-21 (max waves, fell to backstop), 09-28 and 09-30; on 09-30 it stopped after Jump pulled pricing at 04:59:59 and Nathan bounced it (root cause still open). Mahi allows HSIHKD fills to 0.01 against Amana's 0.1 min; Amana thinks the Jump cancellations are price digits.
Next: Amana to confirm the HSI min and the Jump cancellation reason; Nathan to report root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1789983849524539 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790744638304639

### outage-rcas — Outages with written RCAs
status: watching · since: 2026-09-05 · last: 2026-10-14
State: Weekend crypto outage from the Centroid logon gate (09-05, RCA 09-07); 10-14 CMC froze SPX/NDX (cash and futures) 12:18-12:34 UTC, so index futures stayed firm on stale prices (about -$85 on 6 B-book fills) and the A-book NDXUSD hedger could not route off CMC (about -$567 net).
Next: Mahi to decide whether to add non-CMC hedge routing for NDXUSD.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1788769386806729 https://mahifx.slack.com/archives/C08T42TMKU3/p1791993005581759

### dashboard-releases — Dashboard deploys and fixes
status: watching · since: 2026-08-26 · last: 2026-10-08
State: Mahi ships dashboard-only releases to Amana PROD roughly weekly. Isaac asked to avoid mid-week riskReportingCore restarts until MahiMain #1203 lands.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787731205446379 https://mahifx.slack.com/archives/C08T42TMKU3/p1791448225857199

### hedger-execution — Hedger partial-fill crashes and swapfree sizing
status: watching · since: 2026-08-18 · last: 2026-09-28
State: Duplicate tag 17 on Centroid partial fills crashed hybridHedger1 on 08-18/19 (Amana fixed it 08-23); LMAX NOP breaches recurred 09-08. On 09-21 the swapfree hedger sat on 700oz for minutes because one 500oz CMC rejection (5x the 100oz normal quantity) trips a 30s stand-down; Rory softened it to halve the clip. The first hedge after a hedger restart is labelled HOUSE (not configurable). After Nikos complained 09-24 of tiny clips, Rory re-tuned the backstop and DTA rules; by 09-28 performance had improved dramatically.
Next: Rory's targeted rule for the CMC roll window; answers to Nikos on which VaR targets changed and on raising the normal quantity.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787084603512219 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790584111487529

### gold-24-7 — 24/7 XAU pricing
status: watching · since: 2026-08-24 · last: 2026-09-21
State: Amana wants 24h gold (weekend LP feeds from Amana plus extra LPs in their env). Isaac was happy to start piping weekend pricing to clients on 09-21 and advised longer last looks at XAU opens; Nikos chased for another call.
Next: Will/Andrew to hold the follow-up call Nikos asked for.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787559144038639 https://mahifx.slack.com/archives/C08T42TMKU3/p1789983776166919

### skew-yield-value — XAU skew, A-book yield and account value
status: watching · since: 2026-08-19 · last: 2026-09-10
State: No client-channel activity since 2026-09-10 (35d), so watching pending the insti-flow split. Nikos flagged counterparties (8007388, a UAE FIX API broker) arbing the skew; Daria cut XAU skew and added a temp continuity-pool rule; Nikos wants a tamer skew for insti/API flow. On 09-10 Daria/Shyam proposed moving 8007388 to internalisation-only with regular price checks (the trades looked like latency arb); Nikos agreed, rollout unconfirmed. Isaac warned internally (08-25) that skew PnL fell from ~150k a month to little after an insti client was onboarded without telling Mahi, and Mahi is paid almost entirely on FI and LR PnL.
Next: Will/Isaac to agree the insti-flow model split with Nikos; Bonnie checking last month's invoice.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787167725330769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1789022349377719

### tenant-classifier — Counterparty classifier on 8 of 18 tenant profiles
status: closed · since: 2026-09-25 · last: 2026-09-27 · closed: 2026-10-15
State: Liam flagged (09-25) a rule covering 8 of 18 profiles; Isaac replied 09-27 it is intentional (skipped profiles are unused or subsets). No fix needed.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1790349871057129 https://mahifx.slack.com/archives/C08T42TMKU3/p1790501901800649

## Arc
- 2026-04-30 — Amana management happy with Mahi; goal is all flow through Mahi
- 2026-06-29 — XAGUSD B-book go-live; XAUUSD B-book 2026-07-01; mobile clients on Mahi B-book 2026-07-03
- 2026-07-21 — Nikos submits cross-asset migration roadmap (gold futures, indices, crypto, oils; FX deprioritised)
- 2026-08-17 — A-book live for all spot energies and indices except VIX; XAUUSD A-book execution aggregation on 2026-08-18
- 2026-08-23 — XAU/XAG precision reject incident (~20 min); RCA 2026-08-24
- 2026-09-04 — First cryptos live (XRP, SOL, XET)
- 2026-09-11 — SI Energies book live
- 2026-09-21 — BTC live
- 2026-09-25 — SI Indices book live
- 2026-10-01 — Seven GCEX cryptos live (ADA, AAVE, AVAX, DOG, DOT, LTC, TRX)
- 2026-10-07 — XPT/XPD live
- 2026-10-14 — FX B-book flow live (EURUSD, GBPUSD, USDJPY)
