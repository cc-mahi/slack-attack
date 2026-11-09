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
last_catchup: 2026-11-09T08:16:57Z
status: active
---
## Now
Amana is migrating everything onto Mahi in stages: live on A-book metals/indices/energies, crypto (fully on CMC since 11-04, GCEX stopped), SI energies and SI indices books, FX B-book (USD majors since 10-14, USDMXN 11-02, MXN SI go-live 11-05) with FX execution on LMAX+CMC. Nikos drives and escalates fast. Now: IG enabled 11-05 for XAU A-book hedging (NOP and commission-in-aggregation open), a manual-intervention process wanted after the 11-04 SI energies loss and risk transfer, CFD/crypto moving to new dist gateways 11-05. 11-06 NFP showed LR off and skew about -$16/M on gold (internal review, no owner yet); 11-09 Nikos hit resetting TRADEVOLUME in riskmetrics (dev ticket coming). Open pain points: A-book skew/yield value (Mahi bills mostly on FI and LR PnL), pricing load, recurring min-size reject storms, missing SI Indices PnL.

## Streams

### analytics-data-asks — Yield profiles, party IDs and data access
status: open · since: 2026-08-17 · last: 2026-11-09
State: On 11-09 Nikos found TRADEVOLUME in riskreportingmetrics restarting (Futures P on 07-21, and many small instruments at BOOK-INSTRUMENT level, e.g. AUDNZD no B-book trades 05-07 to 10-23) because a running total resets to zero after a quiet period plus a process restart; Nathan said no volume was lost, told him to use the parent books (FUTURES_P/W_CLIENTS, 1:1 with the _LDN child; _NET holds hedging volume) and gave a diff-summing SQL and a yieldprofiles_latest query (fill_status F, abs accounting_counter_quantity), which Nikos accepted for volume. Nikos wants it fixed as a bug and asked whether skew PnL (PRICINGBENCHMARKMIDLIFETIMEPNL, the riskmetrics skew key per Cameron Hughes 11-06) has the same issue; Nathan said it is a running total per client trade and is creating a dev ticket, but the skew question is not answered directly. Earlier asks: FUTURES_W volume baseline for his 7-day lookback script (10-30/11-02, unanswered), yield profile reading (Rory 10-19), spread per book (Isaac 10-26), XAUUSD trade 012dsh28ssy NULL markouts (analyticsProcess missing trade prices, Rory raising with dev), the 77026274_1 fill price, and account-summary P&L (disputed 09-29/30).
Next: Nathan to file the dev ticket on resetting TRADEVOLUME and answer whether skew PnL resets too (Nikos needs figures for a management model-performance report); Isaac to give Nikos a spread-per-book query; Rory to explain the 77026274_1 fill price and dev to fix analyticsProcess missing trade prices; Kate/Mahi to answer on NULL-markout trade 77664840_1 and the party ID, yield profile NULL and account-summary P&L questions.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786982712342769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792416966903439 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794200928174199

### ig-xau-hedging — IG_CENTROID as a metals hedge venue
status: open · since: 2026-11-03 · last: 2026-11-06
State: Amana is adding IG_CENTROID as a metals hedge LP. On 11-04 Rory set an IG quantityDefinition override (0.01/0.01) and bounced the gold hedgers; Nikos said IG is for the regular (non-swapfree) account only on metals. Isaac enabled IG for A-book XAU hedging 11-05 08:55 UTC (first fill 287.08oz); Mahi can set a max market position per instrument plus an overall NOP, and Omar gave a temporary XAUUSD max position pending IG's NOP and tier margin. IG min stays 0.01oz. Nikos (11-05) asked why the hedger rounds 0.01 below the client volume via IG (no reply seen). On 11-06 Omar asked whether per-LP commission can feed the aggregation (LMAX 9c + $5/M, IG 8c + $2.5/M, CMC 8c + $0); Daria said Mahi will check.
Next: Mahi (Daria) to answer Omar on LP commission in aggregation; Isaac/Rory to answer Nikos on the 0.01 IG hedge rounding and confirm the IG NOP/max position is set.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793784345213029 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793946769934689

### gateway-split — Distribution gateway split (dist3 / HP dist4)
status: open · since: 2026-10-23 · last: 2026-11-06
State: Plan (10-23, call 10-26): keep FX, Metals and Metals futures on dist1/HP dist2 and move Crypto, Indices, Energies and futures to two new gateways (dist3 and HP dist4); Fat and VIP feeds unaffected (change CHG-2610-TRFK). On 11-04 Karen tested the four new LP sessions (MAHI_A, A_HP, B, B_HP _CFDCRY_LIVE) with U30 trades; tag 109 came through as 222, routing and bookkeeping looked right, and Isaac agreed no need to test every index. Isaac said Mahi will switch CFDs and cryptos to the new dist gateways on 11-05. On 11-06 Karen moved BRENT, CrudeOilXX/YY, LCOXX/YY, NGXUSD, NGXX/YY and WTI to the new sessions; Isaac saw HP trades fine and Karen saw non-HP trades too, all good.
Next: Isaac to switch CFD and crypto symbols to the new gateways 11-05 and remove them from dist1/HP dist2 at an EOD restart; PagerDuty alerts for the new processes may need silencing.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792765304547529 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793972352903469

### futures-expiry-recs — Futures rolls, expiries and position adjustments
status: open · since: 2026-08-17 · last: 2026-11-06
State: Amana posts expiry and start notices and Mahi zeroes positions at EOD, re-subscribing new contracts on Mahi_CMC_FIX (Shyam did this 10-15 and 10-28). On 11-06 Andreas announced settlement on CC6Z and Rory acknowledged (no confirmation of a zero position seen). On 11-05 Andreas announced settlement on CT6Z, WS6Z and KC6Z and Shyam confirmed 20:47 UTC there were no open positions. On 11-03 Mohamad Malkani announced CT7H, WS7H, KC7H, CC7H, WM7H and CM7H start 11-04 (activate post EOD). Earlier: BrentOil6Z settled 10-28 (BrentOil7G, NG7F, GC7G started), CrudeOilX6 settled 10-15 (F7 started 10-16, brief CMC_CENTROID pricing gap), NG6X settled 10-25; SI IDX futures rolled U to Z 09-24, UKO 09-28; the 09-17 DOWFUT-U expiry spammed IG rejections (not set close-only).
Next: Mahi to confirm the 7H contracts were activated after EOD 11-04.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786993422025149 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793982518286169

### nfp-lr-review — NFP 11-06: LR off and negative skew on gold
status: open · since: 2026-11-06 · last: 2026-11-06
State: Internal (Will, 11-06): through the NFP release (13:30-13:33 UTC) Amana earned close to nothing while Infinox and IC made real LR. After a correction (volumes were overstated about 4x), B_CLIENTS_LDN had $28M with LR $0, CLIENTS_LDN $9M and SWAPFREE $8M, LR $42 in total, and skew about -$721 net (about -$16/M, worse than first read). PSM counters are absent from Graphite. Nobody has owned it yet; Nikos has not been told in the client channel.
Next: owner needed: confirm whether LR is off by design on the B and swapfree books or a gap (lr-health-check), sim a stronger or adaptive skew (skew-health-check), scope PSM for gold, and check the open XAUUSD A-book override issue CARTER-1000.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1793977507421709

### ng-depth-feed — Natgas client depth (TOB only) on the light feed
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 11-06 Karen and Hadeel reported NGXUSD (spot) and NG futures arrived at Centroid as top of book only on both old and new sessions, although Mahi pricing shows full depth. Rory said the fix would be applied by the weekend restarts; change CHG-2611-JMEA (natural gas publishes full client depth) was recorded for Sat 11-07 11:25-11:59 UTC. No client confirmation seen since.
Next: Amana (Karen/Hadeel) to confirm depth now arrives; Rory to confirm the change went through.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793972045779729 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793981700994789

### si-books — SI energies and SI indices books
status: open · since: 2026-08-17 · last: 2026-11-05
State: Energies SI live 09-11 (4h, 500K VaR); indices SI live 09-25 (4h, 100K VaR). SI PnL went blank repeatedly (VIX with no price, then no valid European index price after weekend restarts); permanent fix MahiMain#1203 (last client mid from Graphite after a riskReportingCore restart) deployed 10-29 (CHG-2610-TXKS). PnL drop alerts are alert-only since 10-07 and Nikos called them inaccurate. Since go-live (10-20): Energies SI $341M volume, 75.4% internalised, +$115.7k; Indices SI $2,823M, 89.9% internalised, +$83.8k. On 11-04 the energies book lost about $110k in minutes (see manual-intervention). On 11-05 Rory said an IDX_OFF_BOOK_NET PnLDropAlert (-182k) was a transfer between books. MXN SI go-live was set for 11-05 (CHG-2611-749Q, hedged at 50k VaR).
Next: confirm indices PnL shows at Monday's open and the riskReportingCore log shows the Graphite last-mids load line.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786981181951769 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869

### manual-intervention — Manual risk transfers and desk processes
status: open · since: 2026-11-04 · last: 2026-11-05
State: On 11-04 the SI energies book (CL) went from about +20k to -90k around 16:30 UTC on election/war headlines (not the EIA report, which was slightly bullish); the total VaR limit was breached and the total hedger cleared some risk, then Mahi triggered a manual risk transfer at 16:37 UTC because of the rate of losses. Mahi estimated about $177k saved and warned Nikos before the end-of-day report, which he thanked them for. On 11-05 Nikos asked whether the transfer came from the VaR limit or the timer and for the energies total VaR for 16:30-17:00 so he can review it against his backtests and likely lower it. Nikos also DM'd Isaac wanting a defined process for any manual intervention (probably for Amana's trading desk); Isaac and Will note the earlier B-book argument and plan to add a manual intervention protocol and failover runbooks to the register. Will also wants news rules added to the total hedger. Liam suggested a finding or routine proposing protective settings around events like US elections, with config-override expiry; a commodities and equities news calendar is a gap.
Next: Isaac to send Nikos the energies total VaR for 16:30-17:00 and the quantified saving; Mahi to draft the manual intervention protocol with Nikos.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1793811329971989 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793863061697369 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869

### min-size-rejects — Below-minimum reject storms after quantity-rule changes
status: open · since: 2026-11-01 · last: 2026-11-04
State: Night of 11-03 the hedger spammed CMC crypto rejects (BTCUSD rule 0.001 vs CMC 0.005; ADAUSD and LTCUSD 0.1 vs CMC step validation); Nathan disabled the hedger, then after Amana PH NOC supplied CMC's min sizes reverted to the earlier definitions and re-enabled it (stays reverted until Amana says otherwise). Amana will raise the recurring Step Volume Validation issue with CMC; CMC's true minimums and increments are unresolved. On 11-01 the crypto hedger sent 1,498 AVAXUSD 0.01 orders to GCEX, all rejected, because a 10-30 quantityDefinition rule overrode the real 0.1; Daria switched the crypto hedge book OFF and it stayed off (about 6k VaR unhedged) as hedging.startInOffState defaults true (UI idea filed). Also 11-01/02 XAUUSD sub-1oz orders to LMAX_CENTROID were rejected (min and increment set to 1 on 11-02), and Princess reported U30 rejections 11-02 (cause unknown). Same class as hp-indices-energies.
Next: Amana to get CMC's real crypto minimums and increments and update the LP settings (then Mahi re-applies); Isaac to confirm GCEX's real AVAX minimum and delete or set the 10-30 rule to 0.1; confirm the crypto hedge book is back ON; Mahi to answer Karen's request for what happened and how it won't recur; Daria to resolve the U30 rejects.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793545136210629 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793595854803639 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793747127837329

### crypto-rollout — Crypto go-live and hedging
status: open · since: 2026-08-17 · last: 2026-11-04
State: First cryptos live 09-04, BTC 09-21, seven GCEX coins 10-01. Amana's risk committee decided 10-21 to stop trading with GCEX. On 11-02 to 11-04 Cameron Hughes moved crypto hedging and pricing from GCEX to CMC_CENTROID; by 11-04 17:27 UTC crypto was fully on CMC_CENTROID (CMC quantity definitions set to Mohamad's values, GCEX positions traded out and flat, GCEX-PRIMARY removed from pools and mappings; fixOrdersCentroid and fixMarketDataCentroid restart at EOD). CMC is 24/7 with no maintenance window. B2C2 comes on later. Hybrid hedger crypto stopped 10-31 after no response to an order for 60s (ActiveMQ failover EOF, investigation pending); see min-size-rejects. Crypto pricer cycle times rose after restarts (ZD-23543, root cause open).
Next: Cameron Hughes to delete GCEX-PRIMARY from reference.lists.instrument.custom once the EOD restarts are clean; onboard B2C2 when Amana asks; Daria's ticket ZD-23543 root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793813241969279

### client-tag-passthru — Client login tag for CMC dynamic logins
status: open · since: 2026-09-28 · last: 2026-11-03
State: CMC needs dynamic FIX API client logins, so Amana wants to send them on tag 109 and have Mahi consume and echo them. Rory (09-28) said execution reports do not return 109 today and he would check; a call was being arranged 10-05/06. On 11-02 Karen asked for an update on the "tag 90017 plan" and Rory pointed her to the last thread on it (mid-October), unsure whether Amana had discussed it internally; no plan visible. On 11-03 Amana tested tag 58 (sub-login) with tag 109 unchanged: 12:06 UTC went live for one client (39000163, XAUUSD, mahi_cmcswapfree); Rory confirmed 58 is stored per order for analysis (visible in the Compass orders comments), is not passed on to CMC, and trading is unaffected.
Next: Mahi to say whether tag 109 (or 90017) can be consumed and returned; Amana to extend tag 58 to more clients/instruments.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790602136754039 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793702601646119

### dowusd-continuity-gap — DOWUSD price gap and continuity-pool failover
status: open · since: 2026-10-30 · last: 2026-11-02
State: Hadeel reported a 2s DOWUSD price gap on 10-30. Kate said it came from a Mahi process restart (dev looking; restarts to be EOD-only) and the published quote was from LMAX because the continuity pool included it at failover; she fixed the pool exclusions (old market names, e.g. CMC, were excluded instead of CMC_CENTROID) and bounced poolmd1/2. On 11-02 Nikos asked whether the pricer failed over to the continuity pool and insisted its LPs must match the main LP for CFDs (dow, ndx, oils) because mids between LPs can differ a lot.
Next: Mahi to answer Nikos on continuity-pool LP matching per CFD; dev to root-cause the restart gap.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793346104217759 https://mahifx.slack.com/archives/C08T42TMKU3/p1793375094071059 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793602301837479

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
State: 219 instruments on CLIENT_PRICE_LDN caused an XAU/XAG pricing gap on 08-20 (pre-live instruments moved to staging); CLIENT_PRICE_LDN is to be cut to XAU, XAG and futures. Nikos's 4ms complaints (09-29, 10-01) were normal; NUMA move plus BMSL 50ms cut worst pricer cycle from 16-17ms to 10-11ms. On 10-23 Nikos found a 10ms throttle on A_CLIENTS, objected that Amana was not told, and wants it removed or at 1ms; William will remove it, monitor, and explain a 40ms gap. 10-28 Karen asked for algo host details and a Centroid-to-algo tick measurement (Isaac offered a short capture; no reply seen).
Next: William to remove the 10ms A_CLIENTS throttle and explain the 40ms gap; Isaac to run the Centroid session capture for Karen and answer on algo host details; Isaac to complete the instrument reduction on CLIENT_PRICE_LDN.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787240208405969 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793198412378569

### hp-gateway-precision — High-precision (HP2) gateway and quantity precision
status: open · since: 2026-08-13 · last: 2026-10-23
State: HP2 gateway (HP clients up to 8dp) live after 08-18. The 08-23 XAU/XAG increment mismatch rejected ~120k orders (permanent fix unconfirmed 09-01). Amana still B-books the fraction of A-book HP trades (pending). Mahi can over-fill 1e-8 on internalised fills above ~1,000 (dev fix raised 10-07). Distribution supports only IoC/FoK, rejects GTC (10-23). Some HP accounts hit the regular gateway after the 10-08 rollover.
Next: Amana to fix HP vs non-HP account routing; Mahi dev to fix the 1e-8 over-fill, confirm the permanent quantityDefinition fix is live and send Nikos the (unsent) RCA response.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786632001568829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792769478527769

### gcex-indices-lp — GCEX as second LP for indices
status: open · since: 2026-10-16 · last: 2026-10-22
State: Amana wanted GCEX as backup indices LP (NDXUSD about 35pts apart from LMAX per Rory); 10-20 test trades passed on CFD and SI IDX books. Risk committee decided 10-21 to stop trading with GCEX, so the second-LP outcome and cash-indices aggregation are unclear.
Next: Amana to say what the GCEX stop means for indices and the second-LP policy; Isaac to hold cash-indices aggregation until clarified.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792148151058599 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792502815643379 https://mahifx.slack.com/archives/C08T42TMKU3/p1792664415225229

### outage-rcas — Outages with written RCAs
status: open · since: 2026-09-05 · last: 2026-10-16
State: Weekend crypto outage from the Centroid logon gate (09-05, RCA 09-07); 10-14 CMC froze SPX/NDX 12:18-12:34 UTC (A-book NDXUSD hedger could not route off CMC, about -$567). 10-16 Mahi LD networking incident hit Compass GUI; 17 XAUUSD B-book fills force-cancelled at 16:00 UTC because two dashboard users created in trading hours cost CPU in every JVM (distribution CEP threads share a cpuset). Isaac asked for no user creation at Amana in trading hours and an engineering ticket.
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
status: watching · since: 2026-08-26 · last: 2026-11-08
State: Mahi ships dashboard-only releases to Amana PROD roughly weekly. Compass release (performance/stability/UI) announced 10-16 and completed 10-17; Amana NOC ran pre/post UI checks clean on 10-18. Amana NOC reported clean pre/post Compass UI checks again on 10-25. Isaac asked to avoid mid-week riskReportingCore restarts until MahiMain #1203 lands. Fleetwide dashboard deploys ran 11-06 (Justin; Isaac's mid position adjustment was interrupted, Liam noted deploy skills check Slack but not Compass activity). Amana NOC reported clean pre/post Compass UI checks again 11-08.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787731205446379 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794175624367319

### friday-hedger-off — Weekly Friday gold B-book hedger switch-off
status: watching · since: 2026-11-06 · last: 2026-11-06
State: Amana turns the gold B-book hedgers off every Friday night. On 11-06 Andreas found the portal changed after the dashboard deploy; Cameron Hughes confirmed disabling the two gold B-book hedgers does it and that the book icon now reads On/Off, otherwise unchanged.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793996267458159 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793996894072789

### hedger-execution — Hedger partial-fill crashes and swapfree sizing
status: watching · since: 2026-08-18 · last: 2026-09-28
State: Duplicate tag 17 on Centroid partial fills crashed hybridHedger1 on 08-18/19 (fixed 08-23); LMAX NOP breaches recurred 09-08. 09-21: one 500oz CMC rejection trips a 30s stand-down (Rory halved the clip). The first hedge after a restart is labelled HOUSE (not configurable). After Nikos's 09-24 tiny-clip complaint Rory re-tuned the backstop and DTA rules; improved by 09-28.
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
State: Closed: resolved 10-29 (XETUSD set to 3dp after EOD restart). ETH INVALIDORDER on account 20142138 never reported closed.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792362536599479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793308099667769

### noc-stale-alerts — NOC stale-price alerts
status: closed · since: 2026-10-19 · last: 2026-10-19 · closed: 2026-11-04
State: Closed: 10-19 PH NOC stale-price alerts, pricing confirmed good, no recurrence.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792371686739019 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792372611989499

### hsi-hedger-stalls — HSIHKD hedger stalling and size mismatches
status: closed · since: 2026-09-09 · last: 2026-09-30 · closed: 2026-11-02
State: Closed: no activity since 2026-09-30; assumed resolved (root cause of the 09-30 Jump-pricing stall never reported).
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
