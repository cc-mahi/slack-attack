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
last_catchup: 2026-11-05T08:13:26Z
status: active
---
## Now
Amana is migrating everything onto Mahi in stages: live on A-book metals/indices/energies, crypto (fully on CMC since 11-04, GCEX stopped), SI energies and SI indices books, FX B-book (USD majors since 10-14, USDMXN 11-02, MXN SI go-live 11-05) with FX execution on LMAX+CMC. Nikos drives and escalates fast. Now: IG to be added for XAU A-book hedging, a manual-intervention process wanted after the 11-04 SI energies loss and risk transfer, CFD/crypto moving to new dist gateways 11-05. Open pain points: A-book skew/yield value (Mahi bills mostly on FI and LR PnL), pricing load, recurring min-size reject storms, missing SI Indices PnL.

## Streams

### si-books — SI energies and SI indices books
status: open · since: 2026-08-17 · last: 2026-11-05
State: Energies SI live 09-11 (4h, 500K VaR); indices SI live 09-25 (1h then 4h, 100K VaR). SI PnL kept going blank (Energies 09-28; Indices 09-25 to 10-26): first a VIX position with no pricing (fixed 10-05/06), then after weekend restarts no valid price for European indices until the ~07:00 UTC open (positions and hedging unaffected). Permanent fix MahiMain#1203 (release/26.4: last client mid from Graphite instead of NaN PnL after a riskReportingCore restart) merged 10-27 and deployed 10-29 13:42 UTC (CHG-2610-TXKS). Nikos called the SI PnL drop alerts inaccurate; they are alert-only since 10-07. Since go-live (10-20, internal): Energies SI $341M volume, 75.4% internalised, +$115.7k; Indices SI $2,823M, 89.9% internalised, +$83.8k; Isaac told Nikos 10-22 they are doing really well. On 11-04 the SI energies book lost about $110k in minutes (see manual-intervention). MXN SI go-live was set for 11-05 (change CHG-2611-749Q, FX B-book hedged at 50k VaR, MXN moves to SI; hedgers hybridHedgerSIMXN1 and SIMXNTotal1 being set up).
Next: confirm indices PnL shows at Monday's open and the riskReportingCore log shows the Graphite last-mids load line.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786981181951769 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869

### ig-xau-hedging — IG_CENTROID as a metals hedge venue
status: open · since: 2026-11-03 · last: 2026-11-05
State: Amana is adding IG as a hedge LP for metals. On 11-03 Jake asked Mahi to subscribe IG_CENTROID for XAUUSD.r and XAGUSD.r (Rory acknowledged). On 11-04 Rory found IG_CENTROID XAU/XAG min and step at the default 1/1, and at Maynard's request added an IG quantityDefinition override (0.01/0.01) and bounced hybridHedger1, hybridHedgerBGold1 and hybridHedgerBGoldClose1; Nikos said IG is for the regular (non-swapfree) account only on metals, and potentially both A and B for other assets; Amana sent a test trade to IG_centroid via Compass. On 11-05 08:08 UTC Nikos asked Isaac to enable IG for hedging XAUUSD on the A book and the regular account, and Omar confirmed a NOP is needed on gold for IG. Isaac (internal) wants IG added to the A-book XAU hedging rota, which should unlock arb hedging.
Next: Isaac/Rory to enable IG for XAUUSD A-book (regular account) hedging and add the IG NOP on gold.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793784345213029 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793866134258549 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793866336173359

### manual-intervention — Manual risk transfers and desk processes
status: open · since: 2026-11-04 · last: 2026-11-05
State: On 11-04 the SI energies book (CL) went from about +20k to -90k around 16:30 UTC on election/war headlines (not the EIA report, which was slightly bullish); the total VaR limit was breached and the total hedger cleared some risk, then Mahi triggered a manual risk transfer at 16:37 UTC because of the rate of losses. Mahi estimated about $177k saved and warned Nikos before the end-of-day report, which he thanked them for. On 11-05 Nikos asked whether the transfer came from the VaR limit or the timer and for the energies total VaR for 16:30-17:00 so he can review it against his backtests and likely lower it. Nikos also DM'd Isaac wanting a defined process for any manual intervention (probably for Amana's trading desk); Isaac and Will note the earlier B-book argument and plan to add a manual intervention protocol and failover runbooks to the register. Liam suggested a finding or routine proposing protective settings around events like US elections, with config-override expiry; a commodities and equities news calendar is a gap.
Next: Isaac to send Nikos the energies total VaR for 16:30-17:00 and the quantified saving; Mahi to draft the manual intervention protocol with Nikos.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1793811329971989 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793863061697369 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869

### min-size-rejects — Below-minimum reject storms after quantity-rule changes
status: open · since: 2026-11-01 · last: 2026-11-04
State: Night of 11-03 (22:06 UTC on) the hedger spammed CMC crypto rejects (BTCUSD rule 0.001 vs CMC 0.005; ADAUSD and LTCUSD 0.1 vs CMC step volume validation); Nathan changed quantity definitions, disabled the hedger (about $6 VaR), then after Amana PH NOC supplied CMC's min sizes reverted to the earlier definitions and re-enabled it, and on 11-04 said the change stays reverted until Amana says otherwise. Amana will raise the recurring Step Volume Validation issue with CMC; CMC's true minimums and increments are unresolved. Isaac asked for a summary of hedger and quantity changes after long threads. On 11-01 (05:20-05:39 UTC) the crypto hedger sent 1,498 AVAXUSD 0.01 orders to GCEX, all rejected, because a 10-30 quantityDefinition rule overrode the real 0.1; Daria switched the crypto hedge book OFF and it stayed off (about 6k VaR unhedged) because hedging.startInOffState defaults true (Daria filed a UI idea). Weekend support is best-efforts, not in the contract. Also 11-01/02 XAUUSD sub-1oz orders to LMAX_CENTROID were rejected (Nathan set min and increment to 1 at 00:48 UTC 11-02), and Princess reported U30 rejections 11-02 (cause unknown). Same class as hp-indices-energies.
Next: Amana to get CMC's real crypto minimums and increments and update the LP settings (then Mahi re-applies); Isaac to confirm GCEX's real AVAX minimum and delete or set the 10-30 rule to 0.1; confirm the crypto hedge book is back ON; Mahi to answer Karen's request for what happened and how it won't recur; Daria to resolve the U30 rejects.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793545136210629 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793595854803639 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793747127837329

### crypto-rollout — Crypto go-live and hedging
status: open · since: 2026-08-17 · last: 2026-11-04
State: First cryptos live 09-04, BTC 09-21, seven GCEX coins 10-01 (Amana did not tell Mahi it had enabled them). Amana risk committee decided 10-21 to stop trading with GCEX. On 11-02 Cameron Hughes moved crypto hedging and pricing from GCEX to CMC_CENTROID and the GCEX positions were moved to CMC by manual hedging; DOGUSD, AVAXUSD and TRXUSD were briefly kept on GCEX for lack of CMC pricing. On 11-03 Amana aligned the CMC and GCEX naming; on 11-04 pricers and hedger were bounced and MWMS/BMSL moved to CMC, and by 17:27 UTC Cameron reported crypto fully on CMC_CENTROID for pricing and hedging (execution markets, spreads, selectors, DOG/AVAX/TRX fallback rules removed; CMC quantity definitions set to Mohamad's values; GCEX positions traded out and flat; GCEX-PRIMARY removed from pools and instrument list mappings; fixOrdersCentroid and fixMarketDataCentroid restart at EOD). Karen/Nikos said CMC is 24/7 with no maintenance window, so the weekend window (11:01-11:59 UTC) question Rory raised needs no Mahi change for GCEX. B2C2 comes on later. Hybrid hedger crypto stopped 10-31 11:45 UTC after no response to an order for 60s (ActiveMQ failover EOF, looked reboot related; investigation pending); see min-size-rejects for reject loops. Crypto pricer cycle times rose after restarts (ZD-23543, root cause open).
Next: Cameron Hughes to delete GCEX-PRIMARY from reference.lists.instrument.custom once the EOD restarts are clean; onboard B2C2 when Amana asks; Daria's ticket ZD-23543 root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793813241969279

### gateway-split — Distribution gateway split (dist3 / HP dist4)
status: open · since: 2026-10-23 · last: 2026-11-04
State: Plan (10-23, call 10-26): keep FX, Metals and Metals futures on dist1/HP dist2 and move Crypto, Indices, Energies and futures to two new gateways (dist3 and HP dist4); Fat and VIP feeds unaffected (change CHG-2610-TRFK). On 11-04 Karen tested the four new LP sessions (MAHI_A, A_HP, B, B_HP _CFDCRY_LIVE) with U30 trades; tag 109 came through as 222, routing and bookkeeping looked right, and Isaac agreed no need to test every index. Isaac said Mahi will switch CFDs and cryptos to the new dist gateways on 11-05.
Next: Isaac to switch CFD and crypto symbols to the new gateways 11-05 and remove them from dist1/HP dist2 at an EOD restart; PagerDuty alerts for the new processes may need silencing.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792765304547529 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793804656341439

### client-tag-passthru — Client login tag for CMC dynamic logins
status: open · since: 2026-09-28 · last: 2026-11-03
State: CMC needs dynamic FIX API client logins, so Amana wants to send them on tag 109 and have Mahi consume and echo them. Rory (09-28) said execution reports do not return 109 today and he would check; a call was being arranged 10-05/06. On 11-02 Karen asked for an update on the "tag 90017 plan" and Rory pointed her to the last thread on it (mid-October), unsure whether Amana had discussed it internally; no plan visible. On 11-03 Amana tested tag 58 (sub-login) with tag 109 unchanged: 12:06 UTC went live for one client (39000163, XAUUSD, mahi_cmcswapfree); Rory confirmed 58 is stored per order for analysis (visible in the Compass orders comments), is not passed on to CMC, and trading is unaffected.
Next: Mahi to say whether tag 109 (or 90017) can be consumed and returned; Amana to extend tag 58 to more clients/instruments.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790602136754039 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793702601646119

### futures-expiry-recs — Futures rolls, expiries and position adjustments
status: open · since: 2026-08-17 · last: 2026-11-03
State: Amana posts expiry and start notices and Mahi zeroes positions at EOD, re-subscribing new contracts on Mahi_CMC_FIX (Shyam did this 10-15 and 10-28). On 11-03 Mohamad Malkani announced CT7H, WS7H, KC7H, CC7H, WM7H and CM7H start 11-04 (activate post EOD). Earlier: BrentOil6Z settled 10-28 (BrentOil7G, NG7F, GC7G started), CrudeOilX6 settled 10-15 (F7 started 10-16, brief CMC_CENTROID pricing gap), NG6X settled 10-25; SI IDX futures rolled U to Z 09-24, UKO 09-28; the 09-17 DOWFUT-U expiry spammed IG rejections (not set close-only).
Next: Mahi to confirm the 7H contracts were activated after EOD 11-04.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786993422025149 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793733141297719

### dowusd-continuity-gap — DOWUSD price gap and continuity-pool failover
status: open · since: 2026-10-30 · last: 2026-11-02
State: Hadeel reported a 2s DOWUSD price gap on 10-30. Kate said it came from a Mahi process restart (dev looking; restarts to be EOD-only) and the published quote was from LMAX because the continuity pool included it at failover; she fixed the pool exclusions (old market names, e.g. CMC, were excluded instead of CMC_CENTROID) and bounced poolmd1/2. On 11-02 Nikos asked whether the pricer failed over to the continuity pool and insisted its LPs must match the main LP for CFDs (dow, ndx, oils) because mids between LPs can differ a lot.
Next: Mahi to answer Nikos on continuity-pool LP matching per CFD; dev to root-cause the restart gap.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793346104217759 https://mahifx.slack.com/archives/C08T42TMKU3/p1793375094071059 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793602301837479

### analytics-data-asks — Yield profiles, party IDs and data access
status: open · since: 2026-08-17 · last: 2026-11-02
State: On 10-30 Hadeel/Nikos reported FUTURES_P_CLIENTS_LDN had no opening volume; Cameron Hughes traced it to FUTURES_W_CLIENTS_LDN, whose volume counter is only published once the book trades (no W trades 09-25 to 10-30 10:28 UTC). On 11-02 Nikos said their 7-day-lookback script failed ("No valid snapshot") for that key, argued NULL should repeat the old value and asked what to do (no reply yet). Other open asks from Nikos: yield profile reading (client vs external markouts, NULL timeframes, party IDs, negative allocated yield; Rory explained 10-19), spread per book from Pulse risk-metrics (Isaac checking, 10-26), XAUUSD trade 012dsh28ssy with all markouts NULL (Kate looking, 10-28; Rory says analyticsProcess sometimes misses trade prices, raising with dev) and the 77026274_1 fill-price question. Account-summary P&L was disputed 09-29/30.
Next: Cameron/Mahi to answer Nikos on the W-book volume baseline (lookback or repeat-last-value); Isaac to give Nikos a spread-per-book query on the regular yieldprofiles tables; Mahi dev to fix analyticsProcess missing trade prices (Rory raising); Rory to explain the 77026274_1 fill price and, if Nikos wants, review the two negative-allocated-yield accounts; Kate/Mahi to answer Nikos on the NULL-markout trade 77664840_1; Mahi to answer the party ID, yield profile NULL and account-summary P&L questions.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786982712342769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792416966903439 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793028230830739 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793602717560999

### fx-metals-rollout — FX B-book and XPT/XPD go-lives
status: open · since: 2026-09-25 · last: 2026-11-02
State: On 11-02 USDMXN flow moved onto Mahi (Rory imported A- and B-book positions at market with the A-book hedger off; USDMXN B-book unhedged for now); MXN then moves to SI on 11-05 (CHG-2611-749Q). XPT/XPD live 10-07. FX B-book live 10-14 for EURUSD/GBPUSD/USDJPY into B_OFF_BOOK_CLIENTS, no hedger by Amana's choice; EURJPY/GBPJPY and other majors followed, with FX quantity config HP 0.001 / Non-HP 1000 / LP 1000 and spread aggregation as for XAUUSD. On 10-19 Nikos had FX execution aggregation enabled (EURUSD/GBPUSD/USDJPY to LMAX and CMC; only USD pairs have hedgers) and wants a book-level all-FX execution setting (Rory: scope per hedger). On 10-22 Hadeel uploaded FX DOB spreads and enabled FX B-book and pricing; USDTRY to move to Mahi A and A HP (10-23).
Next: Rory to clarify the all-FX hedger execution config with Nikos; confirm FX qty config and spread aggregation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790335963373189 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793632582556009

### xaufut-booking — XAUFUT G/Z hedger and book routing
status: open · since: 2026-10-29 · last: 2026-10-29
State: On 10-29 Nikos found XAUFUT-Z and -G both under the Futures P hedger, so Mahi hedged client flow against both contracts (about 2,956oz exposure on G that belonged on Z). Cameron Hughes moved XAUFUT-G from FUTURES-P to FUTURES-W with the hedgers bounced, Amana closed G manually and the algo rehedged on Z, and Amana closed the mirrored volume at the LP and give-up. Nikos then saw the manual G trades in the B book hedging portfolio: Cameron found a custom user override from earlier CBOOK test trades (tag 1 set to C Book), removed it, and Nikos said nothing needs redoing. Separately Nikos doubted an XAUFUT-Z client position hedged in the Futures W book; Isaac traced it to real fills from when Z sat in the W list and said Z now goes to P as before.
Next: Isaac to move the XAUFUT-Z positions from W into P once Amana gives the all clear.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793267301772479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793288312690919

### hp-indices-energies — Indices and energies onto Mahi_A_HP
status: open · since: 2026-10-20 · last: 2026-10-29
State: Amana went live on indices and energies on Mahi_A_HP from 10-20 (HP precision confirmed: energy futures 5dp, spot 8dp). Since then a run of minimum/increment problems: NDX futures INVALID_INCREMENT (Nikos: trade the HP feed), SPXUSD hedger min set to 0.1 on 10-21 after spam, E35EUR below minimum 10-29 (moved to Jump at min 0.01), D30 orders out of session because hybridHedgerIndicesSI1 kept hedging after CMC closed (Shyam asked to disable it 17:00-18:00 NY). Nikos (10-21) asked Mahi to disable trading when markets are closed for all indices and energies, and Hadeel asked for current min/step by venue; Hadeel sent a proposed Min/Step sheet 10-26 and asked 10-27 to confirm all definitions are reflected (no reply seen).
Next: Mahi to apply Hadeel's 10-26 indices Min/Step sheet and answer Nikos on market-closed trading; Amana to answer Shyam on disabling hybridHedgerIndicesSI1 17:00-18:00 NY; Amana to say whether NDX futures need 0.01 on the regular feed.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792497820771659 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793285687915249

### pricing-load-latency — Pricing model load and latency
status: open · since: 2026-08-20 · last: 2026-10-28
State: 219 instruments on CLIENT_PRICE_LDN caused an XAU/XAG pricing gap on 08-20 (pre-live instruments moved to a staging model). Nikos's 4ms publish complaints (09-29, 10-01) were judged normal, and a 09-30 NUMA move plus BMSL 50ms cut worst pricer cycle from 16-17ms to 10-11ms. The default client price market is CLIENT_PRICE_ABOOK_LDN and CLIENT_PRICE_LDN is to be cut to XAU, XAG and their futures. On 10-23 Nikos found Mahi throttles A_CLIENTS to one update per 10ms, objected that Amana was not told, and wants it removed or at 1ms; William will remove it, monitor, and explain a 40ms gap. On 10-28 Karen asked for algo host details and a Centroid-to-algo tick travel measurement; Isaac offered a short session capture and Karen asked for 1 day or at least 2 hours (no reply seen).
Next: William to remove the 10ms A_CLIENTS throttle and explain the 40ms gap; Isaac to run the Centroid session capture for Karen and answer on algo host details; Isaac to complete the instrument reduction on CLIENT_PRICE_LDN.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787240208405969 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793198412378569

### hp-gateway-precision — High-precision (HP2) gateway and quantity precision
status: open · since: 2026-08-13 · last: 2026-10-23
State: HP2 gateway (HP clients up to 8dp) live after 08-18. The 08-23 XAU/XAG increment mismatch rejected ~120k orders (permanent fix unconfirmed 09-01). Amana still B-books the fraction of A-book HP trades and passes whole units (pending). Mahi can over-fill 1e-8 on internalised fills above ~1,000 (dev fix raised 10-07). 10-23: distribution supports only IoC/FoK, rejects GTC. Some HP accounts hit the regular gateway after the 10-08 rollover (Shyam 10-09).
Next: Amana to fix HP vs non-HP account routing; Mahi dev to fix the 1e-8 over-fill, confirm the permanent quantityDefinition fix is live and send Nikos the (unsent) RCA response.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786632001568829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792769478527769

### gcex-indices-lp — GCEX as second LP for indices
status: open · since: 2026-10-16 · last: 2026-10-22
State: Amana wanted GCEX as backup indices LP (NDXUSD about 35pts apart from LMAX per Rory); 10-20 test trades passed on CFD and SI IDX books. Risk committee decided 10-21 to stop trading with GCEX, so the second-LP outcome and cash-indices aggregation are unclear.
Next: Amana to say what the GCEX stop means for indices and the second-LP policy; Isaac to hold cash-indices aggregation until clarified.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792148151058599 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792502815643379 https://mahifx.slack.com/archives/C08T42TMKU3/p1792664415225229

### outage-rcas — Outages with written RCAs
status: open · since: 2026-09-05 · last: 2026-10-16
State: Weekend crypto outage from the Centroid logon gate (09-05, RCA 09-07); 10-14 CMC froze SPX/NDX 12:18-12:34 UTC (about -$85 on 6 B-book fills; A-book NDXUSD hedger could not route off CMC, about -$567). 10-16 Mahi LD networking incident (09:33-11:29 UTC) hit Compass GUI; at 16:00 UTC 17 XAUUSD B-book fills were force-cancelled: two read-only dashboard users created in trading hours cost CPU in every JVM while distribution CEP threads share a cpuset. Isaac asked for no user creation at Amana in trading hours and an engineering ticket.
Next: Mahi to raise the user-create/CEP-core engineering ticket; Mahi to decide whether to add non-CMC hedge routing for NDXUSD.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1788769386806729 https://mahifx.slack.com/archives/C08T42TMKU3/p1792168920916789

### vip-feed — Third (VIP) pricing feed for XAU/XAG
status: open · since: 2026-10-08 · last: 2026-10-14
State: CLIENT_PRICE_VIP_LDN pricers added 10-08 for XAU/XAG VIP/swapfree flow (Rory approved); on 10-14 Nikos could not select the model in the spread-config GUI and asked for CMC only (Rory removed LMAX from MWMS for XAU/XAG).
Next: Amana to say whether the VIP feed needs testing; Mahi to fix the spread-config selector.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1791457134754879 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791975764084889

### last-look-tuning — Last look and TP slippage
status: open · since: 2026-08-20 · last: 2026-10-14
State: Clients complain about slipped TP limits (filled after last look at a worse price) and Nikos wants to cut last look from 50ms to 25ms then 10-15ms via the execution profile; Nathan is checking for a lower limit.
Next: Nathan to confirm minimum last-look setting.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787200767810479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1791953832245899

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

### xet-price-rejects — XETUSD INVALID_INCREMENT order storm
status: closed · since: 2026-10-18 · last: 2026-10-29 · closed: 2026-11-04
State: Closed: resolved 10-29 (XETUSD set to 3dp after EOD restart, Shyam monitoring); no later activity. Cause: Amana accounts sent 3dp prices to a 2dp XETUSD (10-18, 10-20, 10-29 INVALID_INCREMENT storms). ETH INVALIDORDER rejection on account 20142138 never reported closed.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792362536599479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793308099667769

### noc-stale-alerts — NOC stale-price alerts
status: closed · since: 2026-10-19 · last: 2026-10-19 · closed: 2026-11-04
State: Closed: 10-19 PH NOC stale-price alerts (mostly futures symbols) while Nathan confirmed pricing was good; no cause reported and no recurrence since 10-19.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792371686739019 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792372611989499

### hsi-hedger-stalls — HSIHKD hedger stalling and size mismatches
status: closed · since: 2026-09-09 · last: 2026-09-30 · closed: 2026-11-02
State: Closed: no activity since 2026-09-30; assumed resolved (root cause of the 09-30 stop never reported). HSI hedging moved from CMC to Jump on 09-09; dealing wanted LMAX (09-21, pending Amana's confirmation: different price bases). The CFD hedger left exposure uncleared on 09-21 (max waves, fell to backstop), 09-28 and 09-30; on 09-30 it stopped after Jump pulled pricing at 04:59:59 and Nathan bounced it (root cause still open). Mahi allows HSIHKD fills to 0.01 against Amana's 0.1 min; Amana thinks the Jump cancellations are price digits.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1789983849524539 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790744638304639

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
