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
  - {name: "Hadeel Salah", role: "dealer / ops: go-lives, positions, spread config", confidence: low}
  - {name: "Mohamad El Masri", role: "ops: manual hedging, position adjustments, IP whitelisting", confidence: low}
  - {name: "Clifford Jay Cana / Jake Denley Alvaro / Maynard Notario / Riordan Bobis / John Carlo Desierto", role: "PH NOC: monitoring, rejections", confidence: low}
  - {name: "Andreas Kleanthous / Mohamad Malkani / Rafik Mansour", role: "ops: futures expiry and start notices, Echo access", confidence: low}
  - {name: "Omar Maatouk", role: "ops: pricing / hedging config requests, rejection reports", confidence: low}
  - {name: "Ali Wehbe", role: "ops: energy futures / oils product specs", confidence: low}
  - {name: "Ahmad Hashem", role: "ops: rejection reports on Mahi_B sessions", confidence: low}
last_catchup: 2026-11-11T08:16:36Z
status: active
---
## Now
Amana is migrating everything onto Mahi in stages: live on A-book metals/indices/energies, crypto (fully on CMC since 11-04, GCEX stopped), SI energies and SI indices books, FX B-book (USD majors since 10-14, USDMXN 11-02, MXN SI go-live 11-05) with FX execution on LMAX+CMC. Nikos drives and escalates fast. Now: IG enabled 11-05 for XAU A-book hedging (NOP and commission-in-aggregation open), a manual-intervention process wanted after the 11-04 SI energies loss and risk transfer, CFD/crypto moving to new dist gateways 11-05. 11-06 NFP showed LR off and skew about -$16/M on gold (internal review, no owner yet); 11-09 Nikos hit resetting TRADEVOLUME in riskmetrics (dev ticket coming) and asked for YTD fixed-price-fee figures; the Saturday restart reloaded weekend prices from Friday average, skewing the FX B-book roll PnL (-11.5k, raised internally); 11-10 he says DAXFUT-Z pricing was far wider than CMC (open); 11-10 CMC too wide on USDTRY left exposure so LMAX was added to the FX hedge pool with 5M NOP on MXN/TRY, and a blocking rule stopped a hedger firing until removed; 11-11 he asks whether Aug spread-widening protection is still enabled. Open pain points: A-book skew/yield value (Mahi bills mostly on FI and LR PnL), pricing load, recurring min-size reject storms, missing SI Indices PnL.

## Streams

### spread-widening-check — Is the illiquid-hours spread widening still enabled?
status: open · since: 2026-11-11 · last: 2026-11-11
State: 11-11 Nikos asked Mahi to investigate spread widening during illiquid hours back in August (XAUUSD report of 08-19 attached). He knows it is an algo feature protecting against arbers on sudden moves but does not remember whether it is still enabled or whether the maximum widening was reduced. Rory acknowledged and will look.
Next: Rory to check the current widening feature and its max-spread cap and reply to Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794384286346449 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794384343189959

### dax-spread-vs-cmc — DAXFUT-Z spread wider than CMC
status: open · since: 2026-11-10 · last: 2026-11-10
State: On 11-10 Nikos said CMC is the main LP for DAX futures but Mahi's client spread does not follow CMC; Rory saw a different comparison on his side, then Nikos posted a 06:45-07:00 UTC Light-vs-CMC spread CSV/HTML (Mahi significantly wider, now also seeing 60). Same morning he asked Mahi to act as clients are complaining about the spread (the image he forwarded is not readable).
Next: Rory to investigate the DAXFUT-Z spread config against CMC and reply.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794297408817199 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794297567238929

### fx-hedge-pool-nop — FX exotic hedging pool, NOP and hedger stalls
status: open · since: 2026-11-10 · last: 2026-11-10
State: 11-10 Amana saw USDTRY exposure on the A-book that should be flat: CMC was too wide so the hedger blocked trades. Isaac found LMAX was second LP for majors but not exotics; Nikos and Omar agreed LMAX for all FX with 5M NOP on both MXN and TRY (Omar talking to LMAX), actioned 13:40 UTC and TRY cleared. Nikos also asked for a max-spread alert in the amana notifications (Isaac looking; Mohamad added to the alerts channel). Same day CMC rejected many hedges (mostly XAUUSD swapfree), hybridHedger1 was briefly off after the FX change and came back, USDCHF W-book exposure (PnL conversion) was zeroed at Nikos's request, and at 16:37 Isaac restarted a hedger after removing a rule that stopped it firing.
Next: Isaac to add the max-spread alert; Mahi to confirm LMAX NOP limits for exotics once Omar hears back.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794312795036509 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794328624585339

### fx-bbook-roll-pnl — FX B-book PnL differs Friday close vs Sunday roll
status: open · since: 2026-11-09 · last: 2026-11-09
State: Nikos noted FX B-book at -28.9K from Friday close vs -17.4K at the Sunday 11-08 roll. Rory: Friday close is correct; the Saturday server restart reloaded weekend prices from Friday's average instead of the close, shifting the book about -11.5k on paper and so the roll figure. Raised internally for review.
Next: Mahi to decide whether to fix weekend price reload after restart and update Nikos.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794238430106659 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794240841128049

### ibxeur-precision — IBXEUR rejections at Jump (1dp prices)
status: open · since: 2026-11-09 · last: 2026-11-09
State: 11-09 Amana saw rejections on IBXEUR (E35EUR first reported); Rory found fills at JUMP_CENTROID; PH NOC said Jump accepts only 1dp prices (not 2dp). Rory agreed to change the config (min/step size 1) by EOD.
Next: Rory to confirm the IBXEUR precision change was applied.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1794228473570299 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794233939269029

### analytics-data-asks — Yield profiles, party IDs and data access
status: open · since: 2026-08-17 · last: 2026-11-09
State: On 11-09 Nikos found TRADEVOLUME in riskreportingmetrics restarting (Futures P on 07-21, many small instruments at BOOK-INSTRUMENT level) because a running total resets to zero after a quiet period plus a process restart; Nathan said no volume was lost, pointed him to the parent books and gave diff-summing and yieldprofiles_latest queries, which Nikos accepted for volume. Nikos wants it fixed as a bug and asked whether skew PnL (PRICINGBENCHMARKMIDLIFETIMEPNL) has the same issue; Nathan said it is a running total per client trade and is creating a dev ticket, skew question unanswered. Also 11-09 Nikos asked for the fixed-price (FP) fee figure YTD ($600,070.24 over $328.1B reset-aware volume = 1.83 RPM, 1 Jan-30 Oct; wants confirmation he is roughly right); Isaac said B_GOLD_CLIENTS_LDN double counts B_CLIENTS_LDN (split book) and will look. Older unanswered asks: FUTURES_W volume baseline, spread per book, NULL markouts (analyticsProcess missing trade prices), the 77026274_1 fill price, account-summary P&L.
Next: Isaac to confirm the FP YTD figure excluding B_GOLD double count and give a spread-per-book query; Nathan to file the TRADEVOLUME dev ticket and answer whether skew PnL resets too; Rory to explain the 77026274_1 fill price; Mahi to answer the NULL-markout, party ID and account-summary P&L questions.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1786982712342769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792416966903439 https://mahifx.slack.com/archives/C08SYSMP0EB/p1794221465833699

### ig-xau-hedging — IG_CENTROID as a metals hedge venue
status: open · since: 2026-11-03 · last: 2026-11-06
State: IG_CENTROID added as a metals hedge LP (regular account only, not swapfree). Rory set an IG quantityDefinition override 11-04; Isaac enabled IG for A-book XAU hedging 11-05 08:55 UTC (first fill 287.08oz); Mahi can set a max market position per instrument plus an overall NOP, and Omar gave a temporary XAUUSD max position pending IG's NOP and tier margin. IG min stays 0.01oz. Nikos (11-05) asked why the hedger rounds 0.01 below client volume via IG (no reply seen). 11-06 Omar asked whether per-LP commission can feed the aggregation; Daria will check.
Next: Mahi (Daria) to answer Omar on LP commission in aggregation; Isaac/Rory to answer Nikos on the 0.01 IG hedge rounding and confirm the IG NOP/max position is set.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793784345213029 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793946769934689

### gateway-split — Distribution gateway split (dist3 / HP dist4)
status: open · since: 2026-10-23 · last: 2026-11-06
State: Plan (CHG-2610-TRFK): FX and Metals stay on dist1/HP dist2; Crypto, Indices, Energies and futures move to dist3 and HP dist4. 11-04 Karen tested the new LP sessions with U30 trades; Mahi to switch CFDs and cryptos on 11-05. On 11-06 Karen moved the oils and gas symbols to the new sessions; trades fine.
Next: Isaac to remove migrated symbols from dist1/HP dist2 at an EOD restart; silence PagerDuty for the new processes if needed.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792765304547529 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793972352903469

### futures-expiry-recs — Futures rolls, expiries and position adjustments
status: open · since: 2026-08-17 · last: 2026-11-06
State: Amana posts expiry and start notices and Mahi zeroes positions at EOD, re-subscribing new contracts on Mahi_CMC_FIX (Shyam did this 10-15 and 10-28). On 11-06 Andreas announced settlement on CC6Z and Rory acknowledged (no confirmation of a zero position seen). On 11-05 CT6Z, WS6Z and KC6Z settled (Shyam confirmed no open positions); Earlier October expiries (BrentOil6Z, CrudeOilX6, NG6X) rolled with a brief CMC_CENTROID pricing gap 10-16.
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
State: Energies SI live 09-11 (4h, 500K VaR); indices SI live 09-25 (4h, 100K VaR). SI PnL went blank repeatedly (VIX with no price, then no valid European index price after weekend restarts); permanent fix MahiMain#1203 (last client mid from Graphite after a riskReportingCore restart) deployed 10-29 (CHG-2610-TXKS). PnL drop alerts are alert-only; Nikos called them inaccurate. Since 10-20: Energies SI +$115.7k, Indices SI +$83.8k. On 11-04 the energies book lost about $110k in minutes (see manual-intervention). On 11-05 Rory said an IDX_OFF_BOOK_NET PnLDropAlert (-182k) was a transfer between books. MXN SI go-live was set for 11-05 (CHG-2611-749Q, hedged at 50k VaR).
Next: confirm indices PnL shows at Monday's open and the riskReportingCore log shows the Graphite last-mids load line.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786981181951769 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869

### manual-intervention — Manual risk transfers and desk processes
status: open · since: 2026-11-04 · last: 2026-11-05
State: On 11-04 the SI energies book (CL) went from about +20k to -90k around 16:30 UTC on election/war headlines; the total VaR limit was breached and the total hedger cleared some risk, then Mahi triggered a manual risk transfer at 16:37 UTC because of the rate of losses. Mahi estimated about $177k saved and warned Nikos before the end-of-day report. On 11-05 Nikos asked whether the transfer came from the VaR limit or the timer and for the energies total VaR for 16:30-17:00 so he can review it against his backtests and likely lower it. Nikos also DM'd Isaac wanting a defined process for any manual intervention (probably for Amana's trading desk); Isaac and Will note the earlier B-book argument and plan to add a manual intervention protocol and failover runbooks to the register. Will also wants news rules added to the total hedger. Liam suggested protective event settings with config-override expiry; a news calendar is a gap.
Next: Isaac to send Nikos the energies total VaR for 16:30-17:00 and the quantified saving; Mahi to draft the manual intervention protocol with Nikos.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1793811329971989 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793863061697369 https://mahifx.slack.com/archives/C08T42TMKU3/p1793865062079869

### min-size-rejects — Below-minimum reject storms after quantity-rule changes
status: open · since: 2026-11-01 · last: 2026-11-04
State: Night of 11-03 the hedger spammed CMC crypto rejects (BTCUSD rule 0.001 vs CMC 0.005; ADAUSD and LTCUSD 0.1 vs CMC step validation); Nathan disabled the hedger, then after Amana PH NOC supplied CMC's min sizes reverted to the earlier definitions and re-enabled it (stays reverted until Amana says otherwise). Amana will raise Step Volume Validation with CMC; CMC's true minimums are unresolved. On 11-01 the crypto hedger sent 1,498 AVAXUSD 0.01 orders to GCEX, all rejected, because a 10-30 quantityDefinition rule overrode the real 0.1; Daria switched the crypto hedge book OFF and it stayed off (about 6k VaR unhedged; startInOffState defaults true). Also 11-02 XAUUSD sub-1oz LMAX rejects and U30 rejections (cause unknown).
Next: Amana to get CMC's real crypto minimums and increments and update the LP settings (then Mahi re-applies); Isaac to confirm GCEX's real AVAX minimum and delete or set the 10-30 rule to 0.1; confirm the crypto hedge book is back ON; Mahi to answer Karen's request for what happened and how it won't recur; Daria to resolve the U30 rejects.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793545136210629 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793595854803639 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793747127837329

### crypto-rollout — Crypto go-live and hedging
status: open · since: 2026-08-17 · last: 2026-11-04
State: First cryptos live 09-04, BTC 09-21, seven GCEX coins 10-01. Amana's risk committee decided 10-21 to stop trading with GCEX. On 11-02 to 11-04 Cameron Hughes moved crypto hedging and pricing from GCEX to CMC_CENTROID; by 11-04 17:27 UTC crypto was fully on CMC_CENTROID (CMC quantity definitions set to Mohamad's values, GCEX positions traded out and flat, GCEX-PRIMARY removed from pools and mappings; fixOrdersCentroid and fixMarketDataCentroid restart at EOD). CMC is 24/7 with no maintenance window. B2C2 comes on later. Hybrid hedger crypto stopped 10-31 after no response to an order for 60s (ActiveMQ failover EOF, investigation pending); see min-size-rejects. Crypto pricer cycle times rose after restarts (ZD-23543).
Next: Cameron Hughes to delete GCEX-PRIMARY from reference.lists.instrument.custom once the EOD restarts are clean; onboard B2C2 when Amana asks; Daria's ticket ZD-23543 root cause.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793513045608259 https://mahifx.slack.com/archives/C08T42TMKU3/p1793813241969279

### client-tag-passthru — Client login tag for CMC dynamic logins
status: open · since: 2026-09-28 · last: 2026-11-03
State: CMC needs dynamic FIX API client logins, so Amana wants to send them on tag 109 and have Mahi consume and echo them. Execution reports do not return 109 today (Rory 09-28); on 11-02 Karen asked about the "tag 90017 plan" and Rory pointed her to a mid-October thread, no plan visible. On 11-03 Amana tested tag 58 (sub-login) with tag 109 unchanged: 12:06 UTC went live for one client (39000163, XAUUSD, mahi_cmcswapfree); Rory confirmed 58 is stored per order for analysis (visible in the Compass orders comments), is not passed on to CMC, and trading is unaffected.
Next: Mahi to say whether tag 109 (or 90017) can be consumed and returned; Amana to extend tag 58 to more clients/instruments.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790602136754039 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793702601646119

### dowusd-continuity-gap — DOWUSD price gap and continuity-pool failover
status: open · since: 2026-10-30 · last: 2026-11-02
State: 10-30 2s DOWUSD price gap from a Mahi process restart (dev looking; restarts to be EOD-only); the quote was from LMAX because the continuity pool included it at failover. Kate fixed the pool exclusions (CMC vs CMC_CENTROID) and bounced poolmd1/2. On 11-02 Nikos asked whether the pricer failed over to the continuity pool and insisted its LPs must match the main LP for CFDs (dow, ndx, oils) because mids between LPs can differ a lot.
Next: Mahi to answer Nikos on continuity-pool LP matching per CFD; dev to root-cause the restart gap.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793346104217759 https://mahifx.slack.com/archives/C08T42TMKU3/p1793375094071059 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793602301837479

### fx-metals-rollout — FX B-book and XPT/XPD go-lives
status: open · since: 2026-09-25 · last: 2026-11-02
State: On 11-02 USDMXN flow moved onto Mahi (Rory imported A- and B-book positions at market with the A-book hedger off; USDMXN B-book unhedged for now); MXN then moves to SI on 11-05 (CHG-2611-749Q).  FX B-book live 10-14 (USD majors, no hedger by Amana's choice; other majors followed), FX quantity config HP 0.001 / Non-HP 1000 / LP 1000. 10-19 FX execution aggregation enabled (USD pairs to LMAX and CMC); 
Next: Rory to clarify the all-FX hedger execution config with Nikos; confirm FX qty config and spread aggregation.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1790335963373189 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793632582556009

### hp-indices-energies — Indices and energies onto Mahi_A_HP
status: open · since: 2026-10-20 · last: 2026-10-29
State: Amana went live on indices and energies on Mahi_A_HP from 10-20. Since then a run of minimum/increment problems: NDX futures INVALID_INCREMENT (Nikos: trade the HP feed), SPXUSD hedger min set to 0.1 on 10-21 after spam, E35EUR below minimum 10-29 (moved to Jump at min 0.01), D30 orders out of session because hybridHedgerIndicesSI1 kept hedging after CMC closed (Shyam asked to disable it 17:00-18:00 NY). Nikos (10-21) asked Mahi to disable trading when markets are closed for all indices and energies, and Hadeel asked for current min/step by venue; Hadeel's 10-26 Min/Step sheet unconfirmed.
Next: Mahi to apply Hadeel's 10-26 indices Min/Step sheet and answer Nikos on market-closed trading; Amana to answer Shyam on disabling hybridHedgerIndicesSI1 17:00-18:00 NY; Amana to say whether NDX futures need 0.01 on the regular feed.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792497820771659 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793285687915249

### pricing-load-latency — Pricing model load and latency
status: open · since: 2026-08-20 · last: 2026-10-28
State: 219 instruments on CLIENT_PRICE_LDN caused an XAU/XAG pricing gap on 08-20; it is to be cut to XAU, XAG and futures. NUMA move plus BMSL 50ms cut worst cycle from 16-17ms to 10-11ms. On 10-23 Nikos found a 10ms throttle on A_CLIENTS, objected that Amana was not told, and wants it removed or at 1ms; William will remove it, monitor, and explain a 40ms gap. 10-28 Karen asked for algo host details and a Centroid tick capture (no reply seen).
Next: William to remove the 10ms A_CLIENTS throttle and explain the 40ms gap; Isaac to run the Centroid session capture for Karen and answer on algo host details; Isaac to complete the instrument reduction on CLIENT_PRICE_LDN.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787240208405969 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793198412378569

### hp-gateway-precision — High-precision (HP2) gateway and quantity precision
status: open · since: 2026-08-13 · last: 2026-10-23
State: HP2 gateway (up to 8dp) live after 08-18. The 08-23 XAU/XAG increment mismatch rejected ~120k orders (permanent fix unconfirmed). Mahi can over-fill 1e-8 on internalised fills above ~1,000 (dev fix raised 10-07). Distribution rejects GTC (10-23). Some HP accounts hit the regular gateway after the 10-08 rollover.
Next: Amana to fix HP vs non-HP account routing; Mahi dev to fix the 1e-8 over-fill, confirm the permanent quantityDefinition fix is live and send Nikos the (unsent) RCA response.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1786632001568829 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792769478527769

### gcex-indices-lp — GCEX as second LP for indices
status: open · since: 2026-10-16 · last: 2026-10-22
State: GCEX as backup indices LP passed 10-20 tests, but the 10-21 risk committee decision to stop trading with GCEX leaves second-LP and cash-indices aggregation unclear.
Next: Amana to say what the GCEX stop means for indices and the second-LP policy; Isaac to hold cash-indices aggregation until clarified.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1792148151058599 https://mahifx.slack.com/archives/C08SYSMP0EB/p1792502815643379 https://mahifx.slack.com/archives/C08T42TMKU3/p1792664415225229

### outage-rcas — Outages with written RCAs
status: open · since: 2026-09-05 · last: 2026-10-16
State: 09-05 weekend crypto outage (Centroid logon gate, RCA 09-07); 10-14 CMC froze SPX/NDX 12:18-12:34 UTC (NDXUSD hedger could not route off CMC, about -$567); 10-16 17 XAUUSD B-book fills force-cancelled because dashboard users created in trading hours cost CPU in every JVM. Isaac asked for no user creation at Amana in trading hours and an engineering ticket.
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
State: Tag 17 duplicate on partial fills crashed hybridHedger1 in August (fixed 08-23); LMAX NOP breaches recurred 09-08. One 500oz CMC rejection trips a 30s stand-down (clip halved). After Nikos's 09-24 tiny-clip complaint Rory re-tuned backstop and DTA rules; improved by 09-28.
Next: Rory's targeted rule for the CMC roll window; answers to Nikos on which VaR targets changed and on raising the normal quantity.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787084603512219 https://mahifx.slack.com/archives/C08SYSMP0EB/p1790584111487529

### gold-24-7 — 24/7 XAU pricing
status: watching · since: 2026-08-24 · last: 2026-09-21
State: Amana wants 24h gold. Isaac was happy to pipe weekend pricing to clients on 09-21 and advised longer last looks at XAU opens; Nikos chased for another call.
Next: Will/Andrew to hold the follow-up call Nikos asked for.
Refs: https://mahifx.slack.com/archives/C08T42TMKU3/p1787559144038639 https://mahifx.slack.com/archives/C08T42TMKU3/p1789983776166919

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

### skew-yield-value — XAU skew, A-book yield and account value
status: closed · since: 2026-08-19 · last: 2026-09-10 · closed: 2026-11-10
State: No activity since 2026-09-10; closed (live concerns, skew value and insti-flow split, now surface under nfp-lr-review and analytics-data-asks). Background: 8007388 arbing skew, moved to internalisation-only (rollout unconfirmed).
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1787167725330769 https://mahifx.slack.com/archives/C08SYSMP0EB/p1789022349377719

### xaufut-booking — XAUFUT G/Z hedger and book routing
status: closed · since: 2026-10-29 · last: 2026-10-29 · closed: 2026-11-10
State: XAUFUT-G was wrongly under the Futures P hedger (hedged both contracts); Cameron Hughes moved it to FUTURES-W, Amana closed manually, the stray C Book override was removed and Nikos said nothing needs redoing. Isaac said XAUFUT-Z positions go to P; no activity since 10-29, assumed resolved.
Refs: https://mahifx.slack.com/archives/C08SYSMP0EB/p1793267301772479 https://mahifx.slack.com/archives/C08SYSMP0EB/p1793288312690919

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
