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
  - {name: "Nikos", role: "primary desk contact: skew, LR, roadmap, escalations"}
  - {name: "Princess Rosete", role: "test trading / ops liaison"}
  - {name: "Hadeel Salah", role: "dealer / ops: go-lives, positions, spread config, order queries", confidence: low}
  - {name: "Mohamad El Masri", role: "ops: manual hedging, position adjustments", confidence: low}
  - {name: "Jake Denley Alvaro / Clifford Jay Cana / Maynard Notario / Riordan Bobis / John Carlo Desierto", role: "PH NOC: monitoring, rejections, pre/post checks", confidence: low}
  - {name: "Andreas Kleanthous / Mohamad Malkani / Rafik Mansour", role: "ops: futures expiry/start notices", confidence: low}
  - {name: "Omar Maatouk", role: "ops: pricing / hedging config, LP NOP", confidence: low}
  - {name: "Ali Wehbe", role: "ops: energy futures specs", confidence: low}
  - {name: "Ahmad Hashem", role: "ops: Mahi_B rejection reports", confidence: low}
last_catchup: 2026-11-19T08:15:22Z
status: active
---
## Now
Amana is migrating everything onto Mahi in stages (A-book metals/indices/energies, crypto on CMC, SI books, FX B-book). Nikos drives and escalates fast.
11-19: Nikos is moving a large returning client onto the new A_CLIENTS_VIP channel (VIP feed, riskSplitting set up by Nathan, test under tag 222 starting now). 11-17: Nikos to decide LR profile A/B for a bursty client;
Still open: NFP LR-off review (no owner), TRADEVOLUME reset bug, NDXUSD price flip, DAXFUT-Z spread, IG NOP/commission, manual-intervention protocol.

## Streams

### vip-feed — Third (VIP) pricing feed for XAU/XAG, now A_CLIENTS_VIP channel
status: open · since: 2026-10-08 · last: 2026-11-19
State: CLIENT_PRICE_VIP_LDN pricers added 10-08; CMC only from 10-14. 11-19 Nikos wants to move one returning big-size client (a 2025 Amana client, large clip) onto the A_CLIENTS_VIP channel for a different execution experience: a pricing feed starting from 500 oz and tighter around 1000 and 3000 oz. Nathan: the channel shares the CLIENT_PRICE_VIP_LDN feed (depth/spread can't be changed per channel; a channel markup adds constant widening, or a new feed is needed); LR is in the published price. Nikos said to put the pipes in first; Nathan set riskSplitting on A_CLIENTS_VIP at 06:16 UTC (XAUUSD to Gold B, silver/XPD/XPT to their B book, index CFDs/futures to SI indices, FX to FX B with MXN to SI MXN, rest stays A). Nikos wants to test asap, copying the fat-feed DOB first. Princess to test under counterparty tag 222; William said ready for testing 08:14 UTC.
Next: Amana (Princess) to run the VIP channel test; Mahi to adjust depth/spread (new feed or markup) after Nikos's tuning.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1791457134754879 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795068985405289 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795076077232659

### si-books — SI energies and SI indices books
status: open · since: 2026-08-17 · last: 2026-11-18
State: Energies SI live 09-11 (4h, 500K VaR); indices SI 09-25 (4h, 100K VaR). SI PnL went blank repeatedly; permanent fix MahiMain#1203 deployed 10-29 (CHG-2610-TXKS). 11-04 energies lost about $110k in minutes (see manual-intervention); 11-05 an IDX_OFF_BOOK_NET PnLDropAlert (-182k) was a book transfer. MXN SI go-live 11-05 (CHG-2611-749Q, 50k VaR). 11-18 SI net book PnL stuck from the morning, believed due to a new oil futures contract; Rory bounced riskReportingCore1.
Next: confirm indices PnL shows at Monday's open and the riskReportingCore log shows the Graphite last-mids load line.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786981181951769 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869 https://mahifx.slack.com/archives/C08T42TMKU3/p1795014015075649

### client-tag-passthru — Client login tag for CMC dynamic logins
status: open · since: 2026-09-28 · last: 2026-11-18
State: CMC needs dynamic FIX API client logins, so Amana wants to send them on tag 109 and have Mahi consume and echo them. Execution reports do not return 109 today (Rory 09-28); 11-02 Karen asked about a "tag 90017 plan", none visible. 11-03 Amana tested tag 58 (sub-login) with 109 unchanged, live for one client from 12:06 UTC; Rory confirmed 58 is stored per order in Compass comments, not passed to CMC, trading unaffected. 11-18 Karen enabled tag 58 sublogin for Mahi to consume for analytics (only appears when the client passes it) and asked whether the new return tags are available yet; Rory was to test a trade with 109=222.
Next: Mahi to say whether tag 109 (or 90017) can be consumed and returned; Amana to extend tag 58 to more clients/instruments.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790602136754039 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795007759259589

### gold-hedger-params — Gold B-book hedge/unhedge parameters
status: open · since: 2026-11-18 · last: 2026-11-18
State: 11-18 Masri asked why gold B-book hedging and unhedging felt slow. Rory: hedging starts above 15M USD XAU notional and immediately above about 18M; unhedging starts once LP exposure exceeds client exposure, straight away if bigger by roughly 100-160 oz (moves with volatility), else after 5 minutes of staying bigger. Masri's screenshot net -136 oz meant nothing to unhedge; Masri accepted.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1795012985651829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1795016416372829

### cp-39001415-lr — Counterparty LR for a bursty XAUUSD client (39001415)
status: open · since: 2026-11-17 · last: 2026-11-17
State: 11-17 Nikos asked for a custom LR profile for client 39001415: aggressive limit-order flow with bad 5s markouts (the hedging window), worst in sustained bursts; he does not want anything added before discussing it. Rory offered two options: B (his ask) burst 2,000,000 then 2,000,000 per 10,000 ms, or A burst 1,000,000 then 125,000 per 500 ms; internally Rory recommends B, Will Carter notes it degrades the client's execution (could tell Nikos to speak to his LP). Nikos will discuss internally on 11-18. Context: swapfree book lost about 2.5K overnight, traced to this client.
Next: Nikos to choose A or B (or neither); Mahi implements only on his confirmation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794923308374639 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794943129736329

### ig-xau-hedging — IG_CENTROID as a metals hedge venue
status: open · since: 2026-11-03 · last: 2026-11-17
State: 11-17 Masri had IG_CENTROID adjusted -5,500 oz and CMC_CENTROID +5,500 oz in Compass only (nothing sent to IG; A-book hedgers off 16:04 UTC, back on 16:09). 11-16 Nikos asked to enable IG for XAGUSD aggregation on the non-swapfree account; Kate asked whether for hedging or price formation (unanswered). IG_CENTROID is a metals hedge LP (regular account only); Isaac enabled it for A-book XAU hedging 11-05 with a temporary max position pending IG NOP and margin. Omar asked whether per-LP commission can feed aggregation (Daria checking). 11-12 IG position in Compass was corrected to match the true 9,064.92 oz.
Next: Nikos to answer Kate (XAGUSD hedging vs pricing); Mahi (Daria) to answer Omar on LP commission in aggregation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793784345213029 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794928634090389

### futures-expiry-recs — Futures rolls, expiries and position adjustments
status: open · since: 2026-08-17 · last: 2026-11-17
State: Amana posts expiry and start notices and Mahi zeroes positions at EOD, re-subscribing new contracts on Mahi_CMC_FIX. 11-17 Andreas announced CrudeOilZ6 settlement (Daria: no open position) and Mohamad Malkani said CrudeOilG7 and SI7H start 11-18; Daria switched the subscriptions and scheduled EOD restarts to pick them up.
Next: Daria to confirm CrudeOilG7 and SI7H are live after the 11-17 EOD restarts.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786993422025149 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794950815047869

### hedger-offhours-rejects — Hedger sending orders outside session hours
status: open · since: 2026-11-13 · last: 2026-11-16
State: 11-13 PH NOC saw USDCHF orders rejected "symbol out of session"; 11-16 William found they were the hedger's orders to CMC_CENTROID and Nikos asked why they were sent at all. William filed change CHG-2611-Y8P9 (Mon 11-16 14:00-16:00Z, awaiting approval) so the B FX hedger stops sending G8 orders over the weekend.
Next: William to apply the change and report back to Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794607758054459 https://mahifx.slack.com/archives/C08T42TMKU3/p1794821719562689

### last-look-tuning — Last look and TP slippage
status: open · since: 2026-08-20 · last: 2026-11-16
State: Clients complain about slipped TP limits and Nikos wants last look cut from 50ms to 25ms then 10-15ms via the execution profile (Nathan checking for a lower limit, no answer seen). 11-16 Hadeel asked why an XBTUSD buy limit was cancelled at 150ms (William: offer moved past the threshold; 150ms is the ABOOK Cryptos execution rule value) and found the client price missing in price-forensics (VWAP-for-quantity fault, raised internally).
Next: Nathan to confirm minimum last-look setting; William to raise the VWAP price-generation issue internally.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787200767810479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794816870181589

### fx-hedge-pool-nop — FX exotic hedging pool, NOP and hedger stalls
status: open · since: 2026-11-10 · last: 2026-11-13
State: 11-10 USDTRY A-book exposure: CMC too wide so the hedger blocked; Nikos and Omar agreed LMAX for all FX with 5M NOP on MXN and TRY (Omar talking to LMAX), actioned and TRY cleared. Nikos asked for a max-spread alert; Rory bounced hybridHedger1 11-13 for faster EM FX. 11-13 residual TRY/MXN exposure explained by Nathan: A-book hedger clips 50k USD with a 50k minimum position, so the VaR trigger fired but sent no order.
Next: Mahi to decide whether to lower the 50k clip/minimum on USDTRY/USDMXN and finish explaining normal quantity to Nikos; Isaac to add the max-spread alert; Mahi to confirm LMAX NOP limits for exotics once Omar hears back.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794312795036509 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794546126185519

### ndx-price-flip — NDXUSD / NDXFUT price flipping, wrong client price
status: open · since: 2026-11-12 · last: 2026-11-12
State: 11-12 Nikos asked Mahi to look at an NDXUSD distribution-HP fill (yield-profile view) and said Mahi's price was wrong. Nathan found the price switching back and forth was unintentional and is hunting the root cause; Hadeel asked whether the previous day's move of all indices to the new Maker sessions is related and later said NDXFUT has the same issue (price-forensics view). Nikos is out most of the day; Hadeel is the contact.
Next: Nathan to report the root cause (and whether it relates to the 11-11 index session move) to Hadeel/Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794458187874679 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794468307057449

### spread-widening-check — Is the illiquid-hours spread widening still enabled?
status: open · since: 2026-11-11 · last: 2026-11-11
State: 11-11 Nikos asked Mahi to investigate spread widening during illiquid hours back in August. He knows it is an algo feature protecting against arbers on sudden moves but does not remember whether it is still enabled or whether the maximum widening was reduced. Rory acknowledged and will look.
Next: Rory to check the current widening feature and its max-spread cap and reply to Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794384286346449 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794384343189959

### xpt-xpd-exposure — XPT/XPD A-book exposure stuck (hedger blocked)
status: open · since: 2026-11-11 · last: 2026-11-11
State: 11-11 Masri flagged XPD/XPT exposure on the A House. Rory: it had built up since pricing moved to Jump-only on 10-07 because Jump's spread (about 2.4 on XPT, 6.7 on XPD) was wider than the hedger's max distance from mid, so it saw the risk but could not trade. After fixes and hedger restarts positions cleared at 10:42 UTC; Rory set a separate XPD/XPT hedging profile and raised minor-metals backstop spreads. Nikos's why-stuck question unanswered.
Next: Rory to answer Nikos's last question and add alerting for a persistently blocked hedger; further hedger-rule review.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794385645413669 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794400320702809

### gateway-split — Distribution gateway split (dist3 / HP dist4)
status: open · since: 2026-10-23 · last: 2026-11-11
State: Plan (CHG-2610-TRFK): FX and Metals stay on dist1/HP dist2; Crypto, Indices, Energies and futures move to dist3 and HP dist4. CFDs and cryptos switched 11-05, oils and gas 11-06, all indices and crypto 11-11 (Rory confirmed non-HP on dist3, HP on dist4; only metals and FX still use the originals). Karen asked about removing a Mahi-side pricing throttle and disabling CFD/crypto on old sessions (no answer seen). Hadeel suspects ndx-price-flip relates to the index move.
Next: Rory to answer Karen; Isaac to remove migrated symbols from dist1/HP dist2 at an EOD restart.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792765304547529 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794416099251529

### dax-spread-vs-cmc — DAXFUT-Z spread wider than CMC
status: open · since: 2026-11-10 · last: 2026-11-10
State: On 11-10 Nikos said CMC is the main LP for DAX futures but Mahi's client spread does not follow CMC; Rory saw a different comparison on his side, then Nikos posted a 06:45-07:00 UTC Light-vs-CMC spread CSV/HTML (Mahi significantly wider, now also seeing 60). Same morning he asked Mahi to act as clients are complaining about the spread.
Next: Rory to investigate the DAXFUT-Z spread config against CMC and reply.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794297408817199 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794297567238929

### fx-bbook-roll-pnl — FX B-book PnL differs Friday close vs Sunday roll
status: open · since: 2026-11-09 · last: 2026-11-09
State: Nikos noted FX B-book at -28.9K from Friday close vs -17.4K at the Sunday 11-08 roll. Rory: Friday close is correct; the Saturday server restart reloaded weekend prices from Friday's average instead of the close, shifting the book about -11.5k on paper and so the roll figure. Raised internally for review.
Next: Mahi to decide whether to fix weekend price reload after restart and update Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794238430106659 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794240841128049

### ibxeur-precision — IBXEUR rejections at Jump (1dp prices)
status: open · since: 2026-11-09 · last: 2026-11-09
State: 11-09 Amana saw rejections on IBXEUR (E35EUR first reported); Rory found fills at JUMP_CENTROID; Jump accepts only 1dp prices. Rory agreed to change the config (min/step size 1) by EOD.
Next: Rory to confirm the IBXEUR precision change was applied.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794228473570299 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794233939269029

### analytics-data-asks — Yield profiles, party IDs and data access
status: open · since: 2026-08-17 · last: 2026-11-09
State: 11-09 Nikos found TRADEVOLUME in riskreportingmetrics resetting after a restart; Nathan: no volume lost, gave workaround queries, creating a dev ticket; skew PnL (PRICINGBENCHMARKMIDLIFETIMEPNL) same-issue question unanswered. Nikos also asked to confirm fixed-price fee YTD (1.83 RPM, 1 Jan-30 Oct); Isaac said B_GOLD_CLIENTS_LDN double counts B_CLIENTS_LDN.
Next: Isaac to confirm the FP YTD figure excluding the B_GOLD double count; Nathan to file the TRADEVOLUME ticket and answer on skew PnL.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786982712342769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792416966903439 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794221465833699

### nfp-lr-review — NFP 11-06: LR off and negative skew on gold
status: open · since: 2026-11-06 · last: 2026-11-06
State: Internal (Will, 11-06): through the NFP release (13:30-13:33 UTC) Amana earned close to nothing while Infinox and IC made real LR. After a correction (volumes were overstated about 4x), B_CLIENTS_LDN had $28M with LR $0, CLIENTS_LDN $9M and SWAPFREE $8M, LR $42 in total, and skew about -$721 net. Nobody has owned it yet; Nikos has not been told in the client channel.
Next: owner needed: confirm whether LR is off by design on the B and swapfree books or a gap (lr-health-check), sim a stronger or adaptive skew (skew-health-check), scope PSM for gold, and check the open XAUUSD A-book override issue CARTER-1000.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1793977507421709

### ng-depth-feed — Natgas client depth (TOB only) on the light feed
status: open · since: 2026-11-06 · last: 2026-11-06
State: On 11-06 Karen and Hadeel reported NGXUSD (spot) and NG futures arrived at Centroid as top of book only on both old and new sessions, although Mahi pricing shows full depth. Rory said the fix would be applied by the weekend restarts; change CHG-2611-JMEA (natural gas publishes full client depth) was recorded for Sat 11-07 11:25-11:59 UTC. No client confirmation seen since.
Next: Amana (Karen/Hadeel) to confirm depth now arrives; Rory to confirm the change went through.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793972045779729 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793981700994789

### manual-intervention — Manual risk transfers and desk processes
status: open · since: 2026-11-04 · last: 2026-11-05
State: 11-04 the SI energies book (CL) went from +20k to -90k around 16:30 UTC on headlines; total VaR limit breached, total hedger cleared some risk, Mahi triggered a manual risk transfer 16:37 UTC (about $177k saved). 11-05 Nikos asked what triggered it and for energies total VaR 16:30-17:00 (likely lowering it), and wants a defined manual-intervention process; Isaac and Will plan a protocol and failover runbooks; a news calendar is a gap.
Next: Isaac to send Nikos the energies total VaR for 16:30-17:00 and the quantified saving; Mahi to draft the manual intervention protocol with Nikos.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1793811329971989 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793863061697369 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869

### min-size-rejects — Below-minimum reject storms after quantity-rule changes
status: open · since: 2026-11-01 · last: 2026-11-04
State: Night of 11-03 the hedger spammed CMC crypto rejects (BTCUSD rule 0.001 vs CMC 0.005); Nathan reverted definitions. Amana will raise Step Volume Validation with CMC; true minimums unresolved. 11-01 the crypto hedger sent 1,498 AVAXUSD 0.01 orders to GCEX, all rejected (10-30 quantityDefinition rule overrode the real 0.1); Daria switched the crypto hedge book OFF and it stayed off (about 6k VaR unhedged).
Next: Amana to get CMC's real crypto minimums/increments; Isaac to confirm GCEX's AVAX minimum, fix the 10-30 rule, and confirm the crypto hedge book is back ON.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793545136210629 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793595854803639 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793747127837329

### crypto-rollout — Crypto go-live and hedging
status: open · since: 2026-08-17 · last: 2026-11-04
State: First cryptos live 09-04, BTC 09-21, seven GCEX coins 10-01. Amana's risk committee decided 10-21 to stop trading with GCEX. On 11-02 to 11-04 Cameron Hughes moved crypto hedging and pricing from GCEX to CMC_CENTROID; by 11-04 17:27 UTC crypto was fully on CMC_CENTROID (GCEX positions flat, GCEX-PRIMARY removed from pools and mappings). CMC is 24/7 with no maintenance window. B2C2 comes on later. Pricer cycle times rose after restarts (ZD-23543).
Next: Cameron Hughes to delete GCEX-PRIMARY from reference.lists.instrument.custom once the EOD restarts are clean; onboard B2C2 when Amana asks; Daria's ticket ZD-23543 root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793813241969279

### dowusd-continuity-gap — DOWUSD price gap and continuity-pool failover
status: open · since: 2026-10-30 · last: 2026-11-02
State: 10-30 2s DOWUSD price gap from a Mahi process restart; the quote was from LMAX because the continuity pool included it at failover. Kate fixed the pool exclusions and bounced poolmd1/2. On 11-02 Nikos asked whether the pricer failed over to the continuity pool and insisted its LPs must match the main LP for CFDs (dow, ndx, oils).
Next: Mahi to answer Nikos on continuity-pool LP matching per CFD; dev to root-cause the restart gap.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793346104217759 https://mahifx.slack.com/archives/C08T42TMKU3/p1793375094071059 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793602301837479

### fx-metals-rollout — FX B-book and XPT/XPD go-lives
status: open · since: 2026-09-25 · last: 2026-11-02
State: On 11-02 USDMXN flow moved onto Mahi (Rory imported A- and B-book positions at market with the A-book hedger off; USDMXN B-book unhedged for now); MXN then moves to SI on 11-05 (CHG-2611-749Q).  FX B-book live 10-14 (USD majors, no hedger by Amana's choice; other majors followed), FX quantity config HP 0.001 / Non-HP 1000 / LP 1000. 10-19 FX execution aggregation enabled (USD pairs to LMAX and CMC); 
Next: Rory to clarify the all-FX hedger execution config with Nikos; confirm FX qty config and spread aggregation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790335963373189 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793632582556009

### hp-indices-energies — Indices and energies onto Mahi_A_HP
status: open · since: 2026-10-20 · last: 2026-10-29
State: Amana went live on indices and energies on Mahi_A_HP from 10-20. Since then a run of minimum/increment problems: NDX futures INVALID_INCREMENT (Nikos: trade the HP feed), SPXUSD hedger min set to 0.1 on 10-21 after spam, E35EUR below minimum 10-29 (moved to Jump at min 0.01), D30 orders out of session (hybridHedgerIndicesSI1 hedging after CMC closed). Nikos (10-21) asked Mahi to disable trading when markets are closed for all indices and energies, and Hadeel asked for current min/step by venue;
Next: Mahi to apply Hadeel's 10-26 indices Min/Step sheet and answer Nikos on market-closed trading; Amana to answer Shyam on disabling hybridHedgerIndicesSI1 17:00-18:00 NY; Amana to say whether NDX futures need 0.01 on the regular feed.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792497820771659 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793285687915249

### pricing-load-latency — Pricing model load and latency
status: open · since: 2026-08-20 · last: 2026-10-28
State: 219 instruments on CLIENT_PRICE_LDN caused an XAU/XAG pricing gap on 08-20; it is to be cut to XAU, XAG and futures. On 10-23 Nikos found a 10ms throttle on A_CLIENTS, objected that Amana was not told, and wants it removed or at 1ms; William will remove it, monitor, and explain a 40ms gap. 10-28 Karen asked for a Centroid tick capture.
Next: William to remove the 10ms A_CLIENTS throttle and explain the 40ms gap; Isaac to run the Centroid capture for Karen; Isaac to complete the instrument reduction on CLIENT_PRICE_LDN.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787240208405969 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793198412378569

### hp-gateway-precision — High-precision (HP2) gateway and quantity precision
status: open · since: 2026-08-13 · last: 2026-10-23
State: HP2 gateway (up to 8dp) live after 08-18. The 08-23 XAU/XAG increment mismatch rejected ~120k orders (permanent fix unconfirmed). 1e-8 over-fill above ~1,000 (dev fix raised 10-07).
Next: Amana to fix HP vs non-HP account routing; Mahi dev to fix the 1e-8 over-fill, confirm the permanent quantityDefinition fix is live and send Nikos the (unsent) RCA response.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786632001568829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792769478527769

### gcex-indices-lp — GCEX as second LP for indices
status: open · since: 2026-10-16 · last: 2026-10-22
State: GCEX as backup indices LP passed 10-20 tests, but the 10-21 risk committee decision to stop trading with GCEX leaves second-LP and cash-indices aggregation unclear.
Next: Amana to say what the GCEX stop means for indices and the second-LP policy; Isaac to hold cash-indices aggregation until clarified.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792148151058599 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792502815643379 https://mahifx.slack.com/archives/C08T42TMKU3/p1792664415225229

### dashboard-releases — Dashboard deploys and fixes
status: watching · since: 2026-08-26 · last: 2026-11-08
State: Mahi ships dashboard-only releases to Amana PROD roughly weekly. Compass release (performance/stability/UI) announced 10-16 and completed 10-17; Amana NOC pre/post UI checks clean through 11-15; fleetwide deploys ran 11-06.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787731205446379 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794175624367319

### friday-hedger-off — Weekly Friday gold B-book hedger switch-off
status: watching · since: 2026-11-06 · last: 2026-11-06
State: Amana turns the gold B-book hedgers off every Friday night. On 11-06 Andreas found the portal changed after the dashboard deploy; Cameron Hughes confirmed disabling the two gold B-book hedgers does it and that the book icon now reads On/Off, otherwise unchanged.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793996267458159 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793996894072789

### outage-rcas — Outages with written RCAs
status: watching · since: 2026-09-05 · last: 2026-10-16
State: (no activity since 10-16; downgraded pending the engineering ticket) 09-05 weekend crypto outage (Centroid logon gate, RCA 09-07); 10-14 CMC froze SPX/NDX 12:18-12:34 UTC (NDXUSD hedger could not route off CMC, about -$567); 10-16 17 XAUUSD B-book fills force-cancelled because dashboard users created in trading hours cost CPU in every JVM. Isaac asked for no user creation at Amana in trading hours and an engineering ticket.
Next: Mahi to raise the user-create/CEP-core engineering ticket; Mahi to decide whether to add non-CMC hedge routing for NDXUSD.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1788769386806729 https://mahifx.slack.com/archives/C08T42TMKU3/p1792168920916789

### hedger-execution — Hedger partial-fill crashes and swapfree sizing
status: watching · since: 2026-08-18 · last: 2026-09-28
State: Tag 17 duplicate on partial fills crashed hybridHedger1 in August (fixed 08-23); LMAX NOP breaches recurred 09-08. One 500oz CMC rejection trips a 30s stand-down (clip halved). After Nikos's 09-24 tiny-clip complaint Rory re-tuned backstop and DTA rules; improved by 09-28.
Next: Rory's targeted rule for the CMC roll window; answers to Nikos on which VaR targets changed and on raising the normal quantity.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787084603512219 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790584111487529

### gold-24-7 — 24/7 XAU pricing
status: watching · since: 2026-08-24 · last: 2026-09-21
State: Amana wants 24h gold. Isaac was happy to pipe weekend pricing to clients on 09-21 and advised longer last looks at XAU opens; Nikos chased for another call.
Next: Will/Andrew to hold the follow-up call Nikos asked for.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787559144038639 https://mahifx.slack.com/archives/C08T42TMKU3/p1789983776166919

### xau-spread-agg-q — How XAUUSD spread aggregation behaves under LP skew
status: closed · since: 2026-11-17 · last: 2026-11-17 · closed: 2026-11-18
State: Closed: answered 11-17. William: base spread is 4c either side of the CMC mid and the XAUUSD base spread is set to 8c for TOB 250oz, so aggregate book widening never goes below 8c; no shading from the skew is applied to the CMC mid.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794902050001049 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794908679108229

### xaufut-booking — XAUFUT G/Z hedger and book routing
status: closed · since: 2026-10-29 · last: 2026-10-29 · closed: 2026-11-10
State: XAUFUT-G was moved from the Futures P hedger to FUTURES-W and fixed manually; no activity since 10-29, assumed resolved.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793267301772479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793288312690919

### skew-yield-value — XAU skew, A-book yield and account value
status: closed · since: 2026-08-19 · last: 2026-09-10 · closed: 2026-11-10
State: No activity since 2026-09-10; closed (live concerns, skew value and insti-flow split, now surface under nfp-lr-review and analytics-data-asks).
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
