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
last_catchup: 2026-10-30T07:19:48Z
status: active
---
## Now
Amana is migrating everything onto Mahi in stages and is live on A-book metals/indices/energies, crypto (7 more GCEX coins 10-01; Amana's risk committee decided 10-21 to stop trading with GCEX, cryptos shifting to CMC plus B2C2), SI energies (since 09-11) and SI indices books, with FX B-book live since 10-14 for the USD majors (all-FX pricing and B-book being enabled 10-22) and FX execution aggregation on LMAX+CMC enabled 10-19; indices/energies going onto Mahi_A_HP and GCEX indices tests passed 10-20 (now in doubt given the GCEX stop). Nikos drives and escalates fast. Open pain points: A-book skew/yield value (Mahi bills mostly on FI and LR PnL), pricing load, hedger stalls (HSI, swapfree) and recurring missing SI Indices PnL.

## Streams

### xet-price-rejects — XETUSD INVALID_INCREMENT order storm
status: open · since: 2026-10-18 · last: 2026-10-29
State: Resolved on the Mahi side 10-29: Hadeel asked (08:54 UTC) to set XET to 3dp while Amana cleans up (GCEX pricing already 3dp); Maynard asked again at 20:42 UTC for 3dp after the EOD restart, and Shyam completed the restarts at 21:08 UTC and will monitor that 3dp orders fill. Maynard also asked at 20:36 UTC about an ETH INVALIDORDER/FIELDVAL rejection on account 20142138 (Daria checking, no outcome seen). Earlier on 10-29 Shyam flagged account 20142138 sending ~490 XETUSD limit buys at 2319.906 (01:48-01:51 UTC), all rejected INVALID_INCREMENT; Amana PH NOC confirmed from Maker logs and will review the symbol configuration. Since 10-18 (account 8010705, ~1,200 orders in seven seconds; again 10-20) Amana accounts sent 3dp prices to XETUSD, which Mahi priced at 2dp (Rory 10-19); 3dp needed an EOD restart.
Next: Mahi to confirm 3dp XETUSD orders now fill; Daria to answer on the ETH rejection for account 20142138.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792362536599479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793308099667769


### xaufut-booking — XAUFUT G/Z hedger and book routing
status: open · since: 2026-10-29 · last: 2026-10-29
State: On 10-29 Nikos found XAUFUT-Z and -G both under the Futures P hedger, so Mahi hedged client flow against both contracts (about 2,956oz exposure on G that belonged on Z). Cameron Hughes moved XAUFUT-G from FUTURES-P to FUTURES-W with the hedgers bounced, Amana closed G manually and the algo rehedged on Z, and Amana closed the mirrored volume at the LP and give-up. Nikos then saw the manual G trades in the B book hedging portfolio: Cameron found a custom user override from earlier CBOOK test trades (tag 1 set to C Book), removed it, and Nikos said nothing needs redoing. Separately Nikos doubted an XAUFUT-Z client position hedged in the Futures W book; Isaac traced it to real fills from when Z sat in the W list and said Z now goes to P as before.
Next: Isaac to move the XAUFUT-Z positions from W into P once Amana gives the all clear.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793267301772479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793288312690919


### hp-indices-energies — Indices and energies onto Mahi_A_HP
status: open · since: 2026-10-20 · last: 2026-10-29
State: On 10-29 Princess reported E35EUR orders arriving below minimum (0.01 vs LMAX min 0.1 on the CBOOK account); William said a fix was going in, then at Mohamad's request moved E35EUR pricing and hedging to Jump at min 0.01 (confirmed 14:54 UTC; pricerA1/2 and the SI indices hedgers bounced to pick it up). On 10-27 Hadeel asked Nathan/team to confirm all definitions are reflected on Mahi's end (no reply seen). On 10-26 Hadeel asked Mahi to adjust the Min/Step for indices to an attached sheet of proposed Mahi settings (no reply yet). On 10-20 Princess asked to go live on indices and energies on the Mahi_A_HP connection; Amana listed the symbols and Rory confirmed the HP precision (energy futures 5dp, indices/energies spot 8dp) is set correctly. Isaac and Nikos then found NDX futures orders rejected INVALID_INCREMENT (qty 3.35 on the regular feed, configured 0.1 increment): Isaac asked whether to move to 0.01 and Nikos said clients should trade against the HP feed. Later Maynard saw D30 orders from account 555 rejected out of session; Shyam traced them to hybridHedgerIndicesSI1 still hedging after CMC's D30 close and asked to disable it 17:00-18:00 NY. On 10-21 Nikos asked Mahi to disable trading when the market is closed for all indices and energies (Will checking) and Hadeel asked for the current min/step for indices spot and futures on HP, non-HP and LP. That evening SPXUSD orders from account 555 hit the Amana bridge below minimum (min should be 0.1, not 0.04); Nathan set the SPXUSD hedger min and increment to 0.1 and the spam stopped.
Next: Mahi to apply Hadeel's 10-26 indices Min/Step sheet and answer Nikos on market-closed trading; Amana to answer Shyam on disabling hybridHedgerIndicesSI1 17:00-18:00 NY; Amana to say whether NDX futures need 0.01 on the regular feed.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792497820771659 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793285687915249


### si-books — SI energies and SI indices books
status: open · since: 2026-08-17 · last: 2026-10-29
State: Energies SI went live 09-11 (time-based, 4h, 500K VaR); indices SI went live 09-25 (1h then 4h transfer, 100K VaR total) after a position flatten and rebuild. SI PnL keeps going missing (Energies 09-28; Indices 09-25, 09-28, 09-30, 10-05, again 10-12): root cause so far is a VIX position with no pricing (VIX pricing put live 10-05, VIXUSD tested 10-06), partly patched by adding VIX to base spreads and CPL. On 10-19 Nikos reported the same again: indices showed no PnL until 06:00 UTC (no reply seen). Nikos called the SI PnL drop alerts inaccurate (10-01, 10-06); Cameron cut them to the TOTAL book with a shorter window and Isaac made them alert-only 10-07.
On 10-20 Isaac posted since-go-live stats (internal): Energies SI $341M client volume, 75.4% internalised, cash PnL +$115.7k; Indices SI $2,823M, 89.9% internalised, +$83.8k, open positions -$1.2M and -$0.4M. Isaac forwarded Nikos on 10-22 saying the SI books are doing really well. On 10-26 Nikos reported no indices PnL again; Shyam (03:44 UTC) said the same issue: after the weekend restart the book has no valid price for the European indices until they reopen, so the total shows blank until the ~07:00 UTC European open. Positions and hedging unaffected. On 10-27 Isaac announced the permanent fix merged (MahiMain#1203 on release/26.4): after a riskReportingCore restart with markets closed, trade-position books start from each instrument's last client mid in Graphite instead of NaN PnL. The analytics build was staged 10-29 (CHG-2610-TXKS, live at the weekly reboot, window to 10-31 11:45Z) and Isaac reported the deploy complete at 13:42 UTC, expecting indices PnL at the next open.
Next: confirm indices PnL shows at Monday's open and the riskReportingCore log shows the Graphite last-mids load line.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786981181951769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792984534176299 https://mahifx.slack.com/archives/C08T42TMKU3/p1793281365549599


### analytics-data-asks — Yield profiles, party IDs and data access
status: open · since: 2026-08-17 · last: 2026-10-28
State: Nikos and ops keep asking how to read yield profiles (client vs external markouts, NULL timeframes 10-07, B_OFF_BOOK_CLIENTS vs OFF_BOOK_CLIENTS party IDs 10-13) and for per-client skew data. Yield profile "external" is LP markouts against a reference mid (CMC_CENTROID for XAU). Nathan (10-02) pointed to the Compass positions tab and watchRiskBook for party-to-hedger mapping, which Nikos cannot open. On 10-19 Nikos asked how allocated yield is calculated in the yield-profiles view and why two accounts show it negative; Rory explained it is the P&L on the position a trade opens until opposite trades offset it (spread at fill plus the move before offset) and offered to look at the two counterparties. Hadeel also asked why an XAUUSD order (77026274_1, 10-14 12:30 UTC) filled at a different price from the one shown; Rory was checking. On 10-21 Nikos reported one XAUUSD trade (10-08 ~02:34 UTC) missing only its 100ms markout; Rory said analyticsProcess is not always receiving trade prices even while live pricing ticks, not an isolated issue, and is raising it with dev. On 10-26 Nikos asked for USD spread value per book from the Pulse risk-metrics tables; Isaac gave a yieldprofiles_latest SUM(inception_pnl) query, Nikos objected and asked about the regular yieldprofiles tables, and Isaac is checking (not deduplicated). On 10-28 Nikos asked why XAUUSD trade 012dsh28ssy (client 8007617, order 77664840_1, 10-27 08:29 UTC) has all markouts NULL and complete=False and whether they can be recovered; Kate said Mahi will look. Account-summary P&L was disputed 09-29/30 (WTD -426K; SI Indices -31K vs -8K by query).
Next: Isaac to give Nikos a spread-per-book query on the regular yieldprofiles tables; Mahi dev to fix analyticsProcess missing trade prices (Rory raising); Rory to explain the 77026274_1 fill price and, if Nikos wants, review the two negative-allocated-yield accounts; Kate/Mahi to answer Nikos on the NULL-markout trade 77664840_1; Mahi to answer the party ID, yield profile NULL and account-summary P&L questions.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786982712342769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792416966903439 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793028230830739 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793179180817269


### futures-expiry-recs — Futures rolls, expiries and position adjustments
status: open · since: 2026-08-17 · last: 2026-10-28
State: Amana posts expiry and start notices and Mahi zeroes positions at EOD. On 10-27 Amana announced BrentOil6Z settlement (Shyam flattened the positions 10-28 00:29 UTC) and that BrentOil7G, NG7F and GC7G start 10-28, activated after EOD; Mohamad Malkani asked 20:56 UTC whether Mahi subscribed those contracts, Shyam resubscribed at EOD and confirmed the symbol subscription looked accepted at 21:13. On 10-15 Amana announced CrudeOilX6 (Nov) settlement (zero all positions) and CrudeOilF7 (Jan) start 10-16; picking up F7 needed a re-subscribe on Mahi_CMC_FIX, done by Shyam that night with a brief CMC_CENTROID pricing gap and the feed confirmed. On 10-23 Amana announced NG6X settlement; Shyam zeroed those positions on 10-25. Earlier: SI IDX futures rolled U to Z on 09-24 by CSV import, UKO futures rolled 09-28, manual position adjustments continue, and the 09-17 DOWFUT-U expiry spammed IG rejections because Amana had not set it close-only.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786993422025149 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793131215829399


### pricing-load-latency — Pricing model load and latency
status: open · since: 2026-08-20 · last: 2026-10-28
State: 219 instruments on CLIENT_PRICE_LDN caused an XAU/XAG pricing gap on 08-20 (pre-live instruments moved to a staging model). Nikos's lead-lag/4ms publish complaints (09-29, 10-01) were judged normal by Mahi (+1ms median, p99 9ms), but Isaac removed three unused arb hedgers from trading-1; a 09-30 NUMA move plus BMSL 5ms to 50ms cut worst pricer cycle from 16-17ms to 10-11ms. FAT feed now prices only XAU/XAG spot and futures (10-07/08), the default client price market moved to CLIENT_PRICE_ABOOK_LDN, and CLIENT_PRICE_LDN is to be cut to XAU, XAG and their futures.
On 10-23 Nikos, investigating client slippage on the XAUUSD light feed (CLIENT_PRICE_ABOOK_LDN, two updates 40ms apart on 10-22 03:15 UTC), found Mahi throttles A_CLIENTS (Amana-A-Prices) to one update per 10ms; he objected that Mahi did not tell Amana and wants it removed or at 1ms (Amana throttles FIX clients at 1ms, Meta at 10-20ms). William will remove the throttle, monitor performance, and check why a 40ms gap occurred despite the 10ms throttle. On 10-28 Karen, documenting latency expectations, asked for algo host details and whether Mahi can measure tick travel time from Centroid to the Mahi algo; Isaac offered a short session capture (raw FIX logs saved for orders, pricing logging only temporary) and Karen asked for 1 day or at least 2 hours (no reply seen).
Next: William to remove the 10ms A_CLIENTS throttle and explain the 40ms gap; Isaac to run the Centroid session capture for Karen and answer on algo host details; Isaac to complete the instrument reduction on CLIENT_PRICE_LDN.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787240208405969 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793198412378569



### gateway-split — Distribution gateway split (dist3 / HP dist4)
status: open · since: 2026-10-23 · last: 2026-10-26
State: On 10-23 Isaac proposed spreading distribution load by keeping FX, Metals and Metals futures on dist1/HP dist2 and moving Crypto, Indices, Energies and their futures to two new gateways (dist3 and HP dist4), needing five new FIX sessions on Amana's side (dist3: A price, A orders, BBOOK orders; HP dist4: A-HP and BBOOK-HP orders). Rollout: Mahi sets up and sends credentials, Amana tests one instrument, moves symbols over, then Mahi removes them from the old gateways at an EOD restart; Fat and VIP feeds are unaffected. On 10-26 Isaac held the call with Karen, Hadeel and Nikos: plan to separate by asset confirmed and Amana happy with the proactivity. That afternoon Cameron saw clientDistributionGateway3 and clientDistributionGatewayHP4 not-running PagerDuty alerts; Isaac said they are new processes, and he raised change CHG-2610-TRFK (CFD FIX connections and instrument split, 14:10-14:40Z). At 16:08 UTC Isaac posted the four new session details (dist3 A price/orders and BBOOK orders, HP dist4 A-HP and BBOOK-HP orders) in #mahi-amana; Amana now tests one instrument and moves symbols over. A credential set was pasted in the client thread.
Next: Amana to connect, test and move Crypto/Indices/Energies symbols to the new sessions; Mahi then removes them from dist1/HP dist2 at an EOD restart; the PagerDuty alerts for the new processes may need silencing or alert-config.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792765304547529 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793030884166429 https://mahifx.slack.com/archives/C08T42TMKU3/p1793020492386999


### crypto-rollout — Crypto go-live and hedging
status: open · since: 2026-08-17 · last: 2026-10-26
State: On 10-26 Karen said she moved CMC crypto pricing to the specific crypto feed CMC created and would test shortly. On 10-21 Amana's risk committee decided to stop trading with GCEX (relayed internally by Rory 10-22); Nikos said cryptos move to CMC for now and B2C2 comes on too. Min/increments for CMC crypto had never been configured; Karen raised it 10-22, Hadeel supplied a minimums sheet and Isaac applied it that afternoon. First cryptos (XRP, SOL, XET) went live 09-04 and BTC 09-21. On 10-01 Amana went live with seven GCEX coins (ADA, AAVE, AVAX, DOG, DOT, LTC, TRX) after Mahi-side tests and a position import on a huddle, without telling Mahi it had enabled them (Rory asked for notice). hybridHedgerCrypto1 stopped itself three times on 09-21 on GCEX_CENTROID partial IOC residuals; Amana used FOK 09-22 to 09-28 until GCEX fixed the terminal message. On 10-16 Karen asked Mahi to enable and subscribe CMC crypto pricing from a mapping sheet, for price analysis only with no execution setup yet. Mahi's Compass 26.4 build (stops internalised fills exceeding order size) goes live at the 10-17 weekly reboots, pausing crypto pricing and fills 10-15 min at 11:25 and 11:45 UTC (CHG-2610-42GK). Crypto pricer cycle times rose after restarts (SHIUSD/PEPEUSD, ZD-23543, root cause open).
Next: Mahi to action the CMC crypto pricing subscription, wind GCEX crypto down and onboard B2C2 when Amana asks; Daria's ticket ZD-23543 root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786963129189029 https://mahifx.slack.com/archives/C08T42TMKU3/p1792664415225229 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793013778807299


### fx-metals-rollout — FX B-book and XPT/XPD go-lives
status: open · since: 2026-09-25 · last: 2026-10-23
State: XPT/XPD went live 10-07 (pricing set to Jump only after CMC was ~$10 off). FX B-book flow went live 10-14 for EURUSD/GBPUSD/USDJPY into B_OFF_BOOK_CLIENTS with no hedger by Amana's choice; Amana is moving EURJPY/GBPJPY pricing and B-book 10-15, asked for FX spread aggregation like XAUUSD (10-12), and for all FX quantity config HP 0.001 / Non-HP 1000 / LP 1000. On 10-16 Hadeel said Amana would enable pricing and B-book flow for AUDUSD, NZDUSD, USDCHF and USDCAD. On 10-19 Nikos asked to enable FX execution aggregation; Rory restarted hybridHedger1 (10:12 BST) with EURUSD/GBPUSD/USDJPY executing to both LMAX and CMC (only USD pairs have Mahi hedgers). Nikos wants a longer-term book-level setting for all FX without defining each instrument; Rory said it can be set for all FX instruments scoped to specific hedgers and was asking what Nikos meant when the thread ended. Nikos also asked whether PnL explains a EUR position in the FUTURES_W_CLIENTS_NET book and to zero it (no reply seen). On 10-22 Hadeel uploaded FX DOB spreads for all pairs on the A-book (light) feed, Rory bounced the A pricers at 11:25 BST (crosses move from triangulated to driver pricing), and Hadeel said Amana would enable FX B-book and pricing that day. On 10-23 Hadeel said Amana plans to move USDTRY to Mahi A and Mahi A HP. Open: unhedged USDJPY on A House (10-14) and a TOB showing 500K vs the 250K Amana defined (10-15).
Next: Rory to clarify the all-FX hedger execution config with Nikos; Mahi to answer the FUTURES_W EUR position question, and to answer the USDJPY exposure and TOB questions; confirm FX qty config and spread aggregation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790335963373189 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792742170063019


### hp-gateway-precision — High-precision (HP2) gateway and quantity precision
status: open · since: 2026-08-13 · last: 2026-10-23
State: HP2 distribution gateway (mobile/HP clients up to 8dp) went live after 08-18 testing. The 08-23 XAU/XAG increment mismatch rejected ~120k orders in ~20 min (permanent fix unconfirmed on 09-01). By 09-10 all B-book HP clients were moved, but Amana still B-booked the fraction of A-book HP trades and passed Mahi whole units only (change pending). Mahi can fill 1e-8 over the requested qty on internalised fills above ~1,000 (Sam 09-22; repeat 10-05; dev fix raised 10-07). On 10-23 Karen noticed GTC orders arriving; William confirmed Mahi distribution supports only IoC or FoK and rejects GTC. Since the 10-08 rollover some HP accounts again hit the regular gateway and were rejected for increment/min size (Shyam 10-09).
Next: Amana to fix HP vs non-HP account routing; Mahi dev to fix the 1e-8 over-fill, confirm the permanent quantityDefinition fix is live and send Nikos the (unsent) RCA response.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786632001568829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792769478527769


### gcex-indices-lp — GCEX as second LP for indices
status: open · since: 2026-10-16 · last: 2026-10-22
State: Amana wants GCEX as backup LP and aggregation source for indices (policy of at least two LPs per asset class). Rory warned that LP index CFDs have different bases (LMAX vs GCEX NDXUSD about 35pts apart). On 10-20 Rory ran NDXUSD buy/sell test trades against GCEX from the CFD book, then from the SI IDX book with the hedgers turned off; the first SI attempt hedged on account 558 instead of 555 and was rerun after a fix. Karen confirmed the trades reached the LP A-book, Mahi give-up and cbook accounts and Nikos confirmed the SI test good. Nikos said Amana would aim to turn on aggregation for cash indices on 10-21. Then on 10-22 Rory relayed Nikos that Amana's risk committee decided on 10-21 to stop trading with GCEX, so whether GCEX stays an indices LP (or the cash-indices aggregation went live) is unclear.
Next: Amana to say what the GCEX stop means for indices and the second-LP policy; Isaac to hold cash-indices aggregation until clarified.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792148151058599 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792502815643379 https://mahifx.slack.com/archives/C08T42TMKU3/p1792664415225229


### noc-stale-alerts — NOC stale-price alerts
status: open · since: 2026-10-19 · last: 2026-10-19
State: PH NOC reported stale-price alerts on 10-19 (sample symbols mostly futures: CO1USD, USOFUT-Z/F, UKOFUT-Z, NG1USD, XAGFUT-Z, XPD/XPTUSD, JPXJPY) while pricing looked fine; Nathan confirmed pricing is good and is still investigating the earlier alerts. Later 10-19 Princess asked Mahi to check BTCUSD; Isaac said it looked okay and she withdrew the request.
Next: Nathan to report the cause of the stale alerts.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792371686739019 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792372611989499


### outage-rcas — Outages with written RCAs
status: open · since: 2026-09-05 · last: 2026-10-16
State: Weekend crypto outage from the Centroid logon gate (09-05, RCA 09-07); 10-14 CMC froze SPX/NDX (cash and futures) 12:18-12:34 UTC, so index futures stayed firm on stale prices (about -$85 on 6 B-book fills) and the A-book NDXUSD hedger could not route off CMC (about -$567 net).
On 10-16 a Mahi LD networking incident (from 09:33 UTC) hit Compass GUI connectivity (Nikos asked whether pricing/hedging were affected; Liam said Amana looked less affected; resolved ~11:29 UTC). At 16:00:44-45 UTC 17 XAUUSD B-book fills were force-cancelled (CANCEL_SYSTEM_ERROR) for internal latency; Isaac traced it to two read-only dashboard users created in trading hours, which trigger an authorisation update costing CPU in every JVM while the distribution gateway CEP threads share a non-isolated cpuset, and has asked that no users be created at Amana in trading hours and for an engineering ticket on both points.
Next: Mahi to raise the user-create/CEP-core engineering ticket; Mahi to decide whether to add non-CMC hedge routing for NDXUSD.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1788769386806729 https://mahifx.slack.com/archives/C08T42TMKU3/p1792168920916789


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


### client-tag-passthru — Client login tag for CMC dynamic logins
status: open · since: 2026-09-28 · last: 2026-10-06
State: CMC needs dynamic FIX API client logins, so Amana wants to send them on tag 109 and have Mahi consume and echo them. Rory (09-28) said execution reports do not return 109 today and he would check; a call was being arranged 10-05/06, outcome not seen.
Next: Mahi to say whether tag 109 can be consumed and returned.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790602136754039 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791212038784569


### hsi-hedger-stalls — HSIHKD hedger stalling and size mismatches
status: open · since: 2026-09-09 · last: 2026-09-30
State: HSI hedging moved from CMC to Jump on 09-09; dealing wanted LMAX (09-21, pending Amana's confirmation: different price bases). The CFD hedger left exposure uncleared on 09-21 (max waves, fell to backstop), 09-28 and 09-30; on 09-30 it stopped after Jump pulled pricing at 04:59:59 and Nathan bounced it (root cause still open). Mahi allows HSIHKD fills to 0.01 against Amana's 0.1 min; Amana thinks the Jump cancellations are price digits.
Next: Amana to confirm the HSI min and the Jump cancellation reason; Nathan to report root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1789983849524539 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790744638304639


### dashboard-releases — Dashboard deploys and fixes
status: watching · since: 2026-08-26 · last: 2026-10-25
State: Mahi ships dashboard-only releases to Amana PROD roughly weekly. Compass release (performance/stability/UI) announced 10-16 and completed 10-17; Amana NOC ran pre/post UI checks clean on 10-18. Amana NOC reported clean pre/post Compass UI checks again on 10-25. Isaac asked to avoid mid-week riskReportingCore restarts until MahiMain #1203 lands.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787731205446379 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792963111278499


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
