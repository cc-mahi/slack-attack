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
  - {name: "Clifford Jay Cana", role: "PH NOC: monitoring, slippage reports", confidence: low}
  - {name: "Jake Denley Alvaro", role: "PH NOC: Centroid tickets, contract specs", confidence: low}
  - {name: "Maynard Notario", role: "PH NOC: rejections / spread monitoring", confidence: low}
  - {name: "Riordan Bobis", role: "PH NOC: rejections, routing tags", confidence: low}
  - {name: "Andreas Kleanthous", role: "ops: futures expiry / settlement notices"}
  - {name: "Mohamad Malkani", role: "ops: futures contract start dates", confidence: low}
  - {name: "Rafik Mansour", role: "ops: futures expiry / settlement, Echo access", confidence: low}
  - {name: "Omar Maatouk", role: "ops: pricing / hedging config requests, rejection reports", confidence: low}
  - {name: "Ali Wehbe", role: "ops: energy futures / oils product specs", confidence: low}
  - {name: "Ahmad Hashem", role: "ops: rejection reports on Mahi_B sessions", confidence: low}
last_catchup: 2026-10-15T12:36:31Z
status: active
---
## Now
Amana is migrating everything onto Mahi in stages and is live on A-book metals/indices/energies, crypto, SI energies and SI indices books, with FX B-book going live this week (EURUSD/GBPUSD/USDJPY on 10-14, EURJPY/GBPJPY next). Nikos is the driver and escalates fast. Open pain points are skew/yield value on the A-book (Mahi bills mostly on FI and LR PnL), pricing-model load, and recurring missing PnL on the SI Indices book.
Window note: #mahi-amana was only sampled for 08-20..09-23 and 09-28..10-06 (budget), so those streams lean on #internal-amana.

## Streams

### fx-metals-rollout — FX B-book and XPT/XPD go-lives
status: open · since: 2026-09-25 · last: 2026-10-15
State: XPT/XPD went live 10-07 (pricing set to Jump only after CMC was ~$10 off; below-minimum rejections fixed by hedger restart; hedgers moved to Jump execution). FX B-book flow went live 10-14 for EURUSD/GBPUSD/USDJPY into B_OFF_BOOK_CLIENTS with no hedger by Amana's choice; Amana is moving EURJPY/GBPJPY pricing and B-book 10-15, asked for FX spread aggregation like XAUUSD (10-12), and for all FX quantity config HP 0.001 / Non-HP 1000 / LP 1000. Open questions in thread: unhedged USDJPY on A House (10-14, Mohamad El Masri) and a TOB showing 500K vs the 250K Amana defined (10-15).
Next: Mahi to answer the USDJPY exposure and TOB 500K vs 250K questions; confirm FX qty config and spread aggregation outcome.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790335963373189 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791794048047539 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792050663738809

### vip-feed — Third (VIP) pricing feed for XAU/XAG
status: open · since: 2026-10-08 · last: 2026-10-14
State: Nikos asked 10-08 for a third feed for VIP/A-book swapfree clients, XAU/XAG spot and futures only, starting at 500 with more depth; Rory approved after a capacity check. CLIENT_PRICE_VIP_LDN pricers were added 10-08 and on 10-14 Nikos could not select the model in the spread-config GUI and asked for CMC only instead of the LMAX+CMC aggregate (Rory removed LMAX from MWMS for XAU/XAG that day).
Next: Amana to say whether the VIP feed needs testing; Mahi to fix the spread-config selector.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1791457134754879 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791975764084889

### last-look-tuning — Last look and TP slippage
status: open · since: 2026-08-20 · last: 2026-10-14
State: Clients complain about slipped TP limits (filled after last look at a worse price) and Nikos wants to cut last look from 50ms to 25ms then 10-15ms via the execution profile; Nathan is checking for a lower limit. Mahi's idea (08-21) is to treat MT/app limits as TPs and give them better execution rules.
Next: Nathan to confirm minimum last-look setting.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787200767810479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791953832245899

### analytics-data-asks — Yield profiles, party IDs and data access
status: open · since: 2026-08-17 · last: 2026-10-13
State: Nikos and ops keep asking how to read yield profiles (default yield, client vs external markouts, NULL timeframes 10-07, B_OFF_BOOK_CLIENTS vs OFF_BOOK_CLIENTS party IDs 10-13) and for skew per client/trade data. Nikos also asked (10-06) for a live position stream for his data team, answered as DB access via a support ticket.
Next: Mahi to answer the party ID and yield profile NULL questions.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786982712342769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791375467369859 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791890549480249

### si-books — SI energies and SI indices books
status: open · since: 2026-08-17 · last: 2026-10-12
State: Amana's board chose time-based SI hedging for energies (4h, 500K VaR), ready for go-live 09-09/10 pending account-tag routing; indices SI went live 09-25 (1h then 4h transfer, 100K VaR total) after a position flatten and rebuild. SI Indices PnL keeps going missing (09-25, 09-28 Monday opens, 10-05, again 10-12): root cause so far is a VIX position with no pricing, partly patched by adding VIX to base spreads and CPL. Nikos also called the SI PnL drop alerts inaccurate (10-06); Isaac refactored them to alert-only on 10-07.
Next: Mahi to fix SI Indices PnL for good (Nathan looking 10-12).
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786981181951769 https://mahifx.slack.com/archives/C08T42TMKU3/p1790327663074889 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791774621350149

### hp-gateway-precision — High-precision (HP2) gateway and quantity precision
status: open · since: 2026-08-13 · last: 2026-10-09
State: HP2 distribution gateway (mobile/HP clients up to 8dp) went live after 08-18 testing. On 08-23 widening the XAU/XAG quantityDefinition rule from one to two distribution markets lost a specificity tie-break and rejected ~20 min of retail flow (about 120k rejections per Karen); Mahi's RCA (Will, 08-24) says neither explanation given on the night was right, production sat on a blunt workaround and the permanent fix was unconfirmed on 09-01. Since the 10-08 rollover some HP accounts again hit the regular gateway and were rejected for increment/min size (Shyam 10-09), and Hadeel reported a repeat 1e-8 over-fill on 10-05.
Next: Amana to fix HP vs non-HP account routing; Mahi to confirm the permanent quantityDefinition fix is live and send Nikos the (unsent) RCA response.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786632001568829 https://mahifx.slack.com/archives/C08T42TMKU3/p1787596107969419 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791511397779419

### pricing-load-latency — Pricing model load and latency
status: open · since: 2026-08-20 · last: 2026-10-08
State: 219 instruments on CLIENT_PRICE_LDN caused an XAU/XAG pricing gap on 08-20; crypto was pulled from the models and Liam sent Amana a staging-model explanation (08-21). A 09-30 NUMA move on trading-1 plus BMSL 5ms to 50ms cut worst pricer cycle from 16-17ms to 10-11ms. FAT feed now prices only XAU/XAG spot and futures (10-07/08), the default client price market moved to CLIENT_PRICE_ABOOK_LDN, and the plan is to reduce CLIENT_PRICE_LDN to XAU, XAG and their futures.
Next: Isaac to complete the instrument reduction on CLIENT_PRICE_LDN.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787240208405969 https://mahifx.slack.com/archives/C08T42TMKU3/p1791363667804489 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791451961676079

### crypto-rollout — Crypto go-live and hedging
status: open · since: 2026-08-17 · last: 2026-10-01
State: First cryptos (XRP, SOL, XET) went live 09-04, XETUSD/HSIHKD confirmed on a call 09-18, BTC activated 09-21 and AAVE/ADA/DOT/LTC/AVAX planned 09-29. hybridHedgerCrypto1 crashed three times on 09-21 because GCEX_CENTROID leaves partial IOC residuals; GCEX said it fixed the terminal message (09-28) and Amana reverted FOK to IOC. A weekend Centroid logon-gate outage (09-05) has an RCA; crypto pricer cycle times rose after restarts, narrowed to SHIUSD/PEPEUSD (ZD-23543, root cause open).
Next: Daria's ticket ZD-23543 root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786963129189029 https://mahifx.slack.com/archives/C08T42TMKU3/p1788507033723059 https://mahifx.slack.com/archives/C08T42TMKU3/p1790858011054809

### futures-expiry-recs — Futures rolls, expiries and position adjustments
status: open · since: 2026-08-17 · last: 2026-09-28
State: Amana posts expiry and start notices (CrudeoilU6, NG6V, BrentOil6X, BrentOil7F) and Mahi zeroes positions at EOD; SI IDX futures were rolled U to Z on 09-24 by CSV import, UKO futures rolled 09-28, and manual position adjustments continue (A-book trades sent to B-book reversed 09-28). Several recs are done by calls with Hadeel.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786993422025149 https://mahifx.slack.com/archives/C08T42TMKU3/p1790242271280259 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790597393973239

### tenant-classifier — Counterparty classifier on 8 of 18 tenant profiles
status: open · since: 2026-09-25 · last: 2026-09-25
State: Liam found (09-25) that a backgroundJobs-scoped compassTenantProfiles rule lists only 8 of 18 profiles since 09-18, so classification for the other 10 (including SI Indices) has been frozen since then. Outcome of the one reply in thread not read.
Next: Isaac to confirm whether the scoped rule was deliberate and fix it.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1790349871057129

### outage-rcas — Outages with written RCAs
status: watching · since: 2026-09-05 · last: 2026-10-14
State: Weekend crypto outage from the Centroid logon gate (09-05, RCA 09-07); 09-08 distribution processes down about 30 minutes after EOD restarts because riskSplitting referenced phantom channels; 10-14 CMC froze SPX/NDX (cash and futures) 12:18-12:34 UTC, so index futures stayed firm on stale prices (about -$85 on 6 B-book fills) and the A-book NDXUSD hedger could not route off CMC (about -$567 net).
Next: Mahi to decide whether to add non-CMC hedge routing for NDXUSD.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1788769386806729 https://mahifx.slack.com/archives/C08T42TMKU3/p1788821160873079 https://mahifx.slack.com/archives/C08T42TMKU3/p1791993005581759

### dashboard-releases — Dashboard deploys and fixes
status: watching · since: 2026-08-26 · last: 2026-10-08
State: Mahi ships dashboard-only releases to Amana PROD roughly weekly. ZD-23378 (Account Summary tiles showing lifetime P&L instead of day P&L, reported 08-25) was fixed 08-26. Isaac asked to avoid mid-week riskReportingCore restarts until MahiMain #1203 lands.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787731205446379 https://mahifx.slack.com/archives/C08T42TMKU3/p1791448225857199

### hedger-execution — Hedger partial-fill crashes and swapfree sizing
status: watching · since: 2026-08-18 · last: 2026-09-28
State: Duplicate tag 17 on Centroid partial fills crashed hybridHedger1 on 08-18/19 (Centroid ticket raised by Amana); LMAX was removed from XAU/XAG hedging, FOK was agreed, then LMAX added back (08-20), and NOP breaches via LMAX recurred 09-08. Nikos complained 09-24 that the swapfree book hedged in tiny clips at RPM around 20 USD/M; Rory re-tuned the backstop and DTA rules and by 09-28 Nikos said performance had improved dramatically.
Next: Rory's targeted rule for the CMC roll window; Nikos' question which VaR targets changed.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787084603512219 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790227336386789 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790584111487529

### gold-24-7 — 24/7 XAU pricing
status: watching · since: 2026-08-24 · last: 2026-09-21
State: Amana wants 24h gold; a call was booked for 08-26; plan is weekend LP feeds from Amana plus extra LPs in their env. Isaac was happy to start piping weekend pricing to clients on 09-21 and advised longer last looks at XAU opens; Nikos chased for another call.
Next: Will/Andrew to hold the follow-up call Nikos asked for.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787559144038639 https://mahifx.slack.com/archives/C08T42TMKU3/p1789983776166919

### skew-yield-value — XAU skew, A-book yield and account value
status: watching · since: 2026-08-19 · last: 2026-09-09
State: No Slack activity since 2026-09-09 (36d), so downgraded to watching pending the insti-flow split. Nikos questioned low A-book yield and flagged counterparties (8007388, a UAE FIX API broker) arbing the skew; Daria cut XAU skew, added alerting and a temp continuity-pool rule, and Nikos wants one skew for retail and a tamer one for insti/API flow. Isaac warned internally (08-25) that skew PnL fell from about 150k a month to little after Amana onboarded an insti client without telling Mahi, and Mahi is paid almost entirely on FI and LR PnL. On 09-09 Nikos asked whether to leave a broker client that lost 330K in July in A-book; Mahi's line is to separate insti flow onto its own model and frame it as PnL optimisation.
Next: Will/Isaac to agree the insti-flow model split with Nikos; Bonnie checking last month's invoice.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787167725330769 https://mahifx.slack.com/archives/C08T42TMKU3/p1787670516904379 https://mahifx.slack.com/archives/C08T42TMKU3/p1788966322574519

## Arc
- 2026-04-30 — Amana management very happy with Mahi performance; goal is all flow through Mahi, A-book index/futures onboarding under way
- 2026-06-29 — XAGUSD B-book hedger go-live; XAUUSD B-book first live trade 2026-07-01, mobile clients moved to Mahi B-book 2026-07-03
- 2026-07-21 — Nikos submits formal cross-asset migration roadmap (gold futures, indices, crypto, oils; FX deprioritised)
- 2026-08-17 — A-book live for all spot energies and indices except VIX; XAUUSD A-book execution aggregation on 2026-08-18
- 2026-08-23 — XAU/XAG precision reject incident (about 20 min of retail rejections); RCA 2026-08-24
- 2026-09-04 — First cryptos live (XRP, SOL, XET)
- 2026-09-25 — SI Indices book live; SI Energies book ready since 2026-09-10
- 2026-10-07 — XPT/XPD live
- 2026-10-14 — FX B-book flow live (EURUSD, GBPUSD, USDJPY)
