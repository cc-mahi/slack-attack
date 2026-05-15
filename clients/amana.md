---
slug: amana
refs:
  vibepulse: ../VibePulse/.claude/clients/amana.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: amana
  hosts: ../MahiProduct/data/client-hosts.json          # entry: amana
  wiki: null                                             # ../MahiProduct/wiki/clients/amana.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Karen Montero", role: "ops / test trading liaison", confidence: low}
  - {name: "Nikos", role: "primary desk contact — skew config, LR tuning, futures onboarding"}
  - {name: "Princess Rosete", role: "test trading / ops liaison", confidence: low}
  - {name: "Mohamad El Masri", role: "ops — manual hedging / rec break liaison", confidence: low}
  - {name: "Andreas", role: "ops — commodity futures expiry / position management", confidence: low}
  - {name: "Hadeel Salah", role: "ops — reconciliation", confidence: low}
last_catchup: 2026-05-15T07:11:03Z
---

## Recent issues

> [open] 2026-05-12 — Nikos querying limit fill execution on XAUFUT-M / arber execution profile last-look tightening
> Nikos asked (06:35 BST) why cpty 5800055 was filled at $4685.71 when offer appeared at that price ~100ms before execution. Nathan explained: 500ms LL delay on ABOOK/Manual Arber Selection execution profile; limit price passed price check at both ends of the window; client filled at limit (not the moved offer). Nikos responded at 08:14 BST: "I will bring it down a bit as we have no interest to provide a good execution experience to those clients" — intends to tighten price check and/or mid distance on the arber execution profile. Change not yet applied. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1778564126787019)

> [open] 2026-05-11 — DAX/UKX futures: CMC pricing not arriving (only IG received)
> Rory flagged (11:15 BST) that DAXFUT-M and UKXFUT-M are only receiving pricing from IG; expected CMC as primary hedging venue per Nikos' LP mappings CSV (sent 10:16 BST). Amana ops checked and saw CMC sending prices — Maynard investigating at 17:12 BST. As of 07:06 BST 2026-05-12, CMC side reports prices being sent and queries whether Mahi is subscribing on symbols DX6M_ / FT6M_; Rory has not yet confirmed. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1778494554960779)

> [open] 2026-05-11 — IG latency on XAUUSD/CFDs: discussion on removing IG from price formation
> Nikos shared lead-lag analysis showing IG running 50–100ms behind on XAUUSD — "should absolutely not be used for price discovery anywhere." Cameron confirmed IG was already removed from CFD futures ref prices (normalisation divergence issue); IG currently in mid formation for CFDs (CMC, Jump, IG) and retained for DOW futures only. Nikos asked whether IG should be stripped from CFDs entirely; Cameron said filtering logic handles latent LPs but acknowledged consistently latent = better to remove. Call agreed for 2026-05-12 to decide. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1778511757782779)

> [resolved] 2026-05-07 — XAUFUT-M price spikes: IG/CMC divergence causing client-visible spikes
> Client-side contact Jake reported XAUFUT-M spikes at 19:02; logs showed MAHI_CMC vs CMC_CFD divergence. Root cause: IG_CENTROID and CMC_CENTROID diverging with no normalisation in place — model oscillated between them. Cameron Hughes had already added benchmarkNormalised config for index futures and XAU futures BMSL earlier in the day (13:08 BST); pricers bounced at 20:06 to pick it up. Cameron Hughes confirmed resolution to Jake at 22:01: "IG and CMC prices diverging, we've enabled normalization now to prevent this happening again." [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1778176934.167609)

> [open] 2026-05-07 — MAHI_B LP session decommission: FX flow moved off, credential/config changes pending
> Karen (Amana) moved all flow off the old MAHI_B LP session at ~15:29 BST; last BBOOK trade at 14:33 UTC. Karen asked Rory whether credentials need changing to convert MAHI_B to a MAHI_A-style session; Rory said he would check. No resolution confirmed in thread. Rory also confirmed at 12:50 that once FX is turned off on B-book, Amana wants positions flattened and deleted from Pulse. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1778164166.488739)

> [open] 2026-05-05 — XAUFUT LIQUIDITY_VIOLATION: off-market limit on futures (trade 68635742_1)
> Princess reported XAUFUT LIQUIDITY_VIOLATION on trade 68635742_1 at 13:31; Rory confirmed "same issue" (off-market limit price on futures) and was still investigating at 14:06. Separate from the XAUUSD spot limit rejection reported earlier same day. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777984308577199)

> [open] 2026-05-05 — XAUUSD limit order rejected LIQUIDITY_VIOLATION: off-market limit price
> Princess reported a sell limit order on XAUUSD rejected with `LIQUIDITY_VIOLATION`; tag1=ABOOK, order sent at 4550.95 sell-limit, published price was 4550.77/4550.89 at time of receipt — order was off-market. Daria explained the rejection. Princess followed up at 07:39 asking if resolved; Will replied at 08:06 that Mahi will look into it today. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777960089109199)

> [resolved] 2026-05-04 — monitoring.pnlDrop: false PnL drop alerts suppressed for futures books
> Nathan Burch enabled `useTradePositionPnl` in `monitoring.pnlDrop` config. XAGFUT (and other futures instruments) were triggering false PnL drop alerts because PnL was calculated by converting futures positions using the spot price — the inherent futures/spot price differential caused alerts to fire incorrectly. No book-specific override exists, so the change applies to all books. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777850060789949)

> [resolved] 2026-05-01 — DOWUSD tag1 routing: trades falling into CMCSWAPFREE instead of ABOOK
> Rory noticed DOWUSD index CFD trades for some counterparties assigned `trading_account = CMCSWAPFREE` in Pulse instead of `ABOOK`. Root cause: `tag1=CMCSWAPFREE` being applied beyond metals. 2026-05-04: Karen confirmed she will scope CMCSWAPFREE to spot metals only; Cameron Hughes clarified spot FX/metals can keep the tag, indices/CFDs should have it removed. Karen confirmed done at 10:05. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777885500546369)

> [open] 2026-05-01 — Index futures rollout: US live, EU/Asia/Russell in progress
> DOWFUT-M and NDXFUT-M test trading attempted 2026-05-01 morning; Princess test trade rejected with `DISTRIBUTION_LDN-maximumShowQuantity=TOO_SMALL, quantity=TOO_SMALL`. Root cause identified by Rory but requires weekend EOD restarts to take effect — US futures index go-live pushed to early next week. In the meantime: continuing setup for all other cash + futures equity indices (EU, Asia), collecting step/min sizes from Princess/Nikos. Princess provided min+step per LP at 13:46. Rory to revert with further items requiring EOD restarts. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777629657810339)
> 2026-05-05 update: root cause confirmed by test — hedger fires immediately at cumulative 0.1 NDX but fails to recognise sub-0.1 positions (e.g. 0.05 and 0.01 not hedged). DOWFUT-M routing to IG_CENTROID confirmed correct for ≥0.1 positions. Cameron Hughes bounced futsP1 hedger at 14:18 to clear a residual 0.01 NDXFUT-M position it wouldn't clear; Rory bounced hybridHedgerFutsP1 at 12:14. Further fix still required. Nikos asked 2026-05-06 07:59 whether ready to switch on EQ INDEX FUT — Daria said LDN team will update. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1778050766305989)
> 2026-05-06 update: NQ/DOW test trading continued with Karen. NQ hedger spam incident at 13:49 — hedger looped a BUY NQ generating 1212 rejections in ms; Rory killed futures hedger, Karen closed position, hedger re-enabled after hybridHedgerFutsP1 bounced with `riskQuantisationOverride` adjustment. Second test passed: DOW hedged at 0.05, NQ at 0.02 both confirmed. NQ minimum confirmed as 0.02 (Compass min/increment left at 0.01 — acceptable as internalisation floor is 0.02). Nikos confirmed go-live for LDN morning 2026-05-07. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1778071776.491909)
> 2026-05-07 update: NDX and DOW futures live 10:40 BST, SPX futures live 10:55 BST. RTY (Russell) futures excluded from hedger covariance matrix — Rory removed from instrumentToProfileMappings (error: `Cannot use MaxVar-relative quantity with non-covariance managed instrument`) and will set up non-VaR hedging rules as interim cover. EminiSPYY (SPX) enabled by Princess at 10:54. Hedger VaR threshold adjusted 300→2,500 and max wave quantity 15→45 to handle higher notionals for index futures vs metals. Further work: UKX/FTSE100, SWI/SMI, DAX pricing confirmed; RTY, DXY, VIX not yet receiving pricing. EU/Asian cash + futures indices (EU, Asia) next. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1778146858.490019)

> [resolved] 2026-04-29 — US index CFD go-live: NAS hedger not firing on test trades
> Resolved 2026-04-30: NDXUSD + DOWUSD CFDs went live; spreads uploaded by Rory, Amana switched on NAS + U30 by 16:03, SPX also enabled 2026-05-01. First CFD trade internalised + hedged by Rory at 17:16 (criticalHedgerBooks updated to include CFD hybrid hedger). [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777565764829549)

> [open] 2026-04-29 — XAU FUT mid formation: CMC dominates on tightness, IG often more market-correct
> Nikos: when CMC and IG cross, current mid formation prioritises tighter (CMC) but CMC is sometimes wrong (clients trade through, then CMC rejects our hedges). Isaac to set up adaptive pricing to add IG to mid formation. Nikos waiting on more details before enabling. Family of cross-uncrossing filters explained by David Cooney. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777443057933069)

> [open] 2026-04-29 — Silver futures expiry: Mahi position not auto-closed
> Silver expired; client closed coverage + LP positions but Mahi-side position remained on the Futures P book. Rory looking into adjustment / generating a closing entry in trades tables (Mahi-only, no market trade). Nikos: "we do not need to close them in the market, just in Mahi". [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777464929878949)

> [open] 2026-04-28 — SI K6 (silver futs) pricing missing on LMAX_CENTROID + CMC_CENTROID
> Shyam reported no pricing for SI K6 from either LP. Thread has 6 replies through 04-28 13:08. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777332485508629)

> [open] 2026-04-28 — Pricing/instrument-spec confirmation pending for index CFDs and futures
> NDX/DOW cash CFD spreads now uploaded and live as of 2026-04-30. Still outstanding: step size and minimum trade sizes for all index CFDs and futures (EU, Asia, and US futures variants). Princess provided per-LP min+step data 2026-05-01 13:46 for Rory to action; Rory also needs clarification on any futures index subscriptions still required. Default for all CFDs currently 0.01 min/step. Original 2dp confirmation and VIX/DXY exceptions still unresolved. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777377050982879)

> [resolved] 2026-04-29 — Manual hedge tag for ops disambiguation
> Cameron Hughes added `ui.orders.manualOrder.counterpartyOverride`; manual trades now come through with a counterparty tag (Mohamad/Karen agreed on tag `555`, also "MahiManual" alternative configured). Closes the futures-arb-hedger spot mismatch follow-up where Amana ops mistook Mahi manual hedges for test trades and booked offsets. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777305707752219)

> [resolved] 2026-04-28 — XAUUSD client-trade min increment moved 0.000001 → 0.01
> Compass distribution config was 0.000001oz on metals (cause of the 0.504562oz partial-fill residual). Karen confirmed CMC and Amana side use 0.01; Cameron Hughes set distribution min/step to 0.01oz on 04-28. Smaller trades will now be rejected. Closes the LR partial-fill follow-up. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777327460490989)

> [resolved] 2026-04-28 — Distribution config crash: duplicate `A_CFD_CLIENTS_LDN` riskControlProfile
> Justin flagged dist config broken with `Duplicate key A_CFD_CLIENTS_LDN`; Rory removed the duplicate same minute. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777393512087569)

> [resolved] 2026-04-28 — XAGUSD aggregation live (LMAX_CENTROID + CMC_CENTROID)
> Rory bounced hybridHedger1 to add CMC alongside LMAX for XAGUSD execution; first post-change client fill confirmed hedged to CMC_CENTROID. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777374338161209)

> [resolved] 2026-04-27 — IG + Jump LP test trades for XAU/XAG hedging
> All four LP connections validated with paired buy/sells: IG XAUFUT-M, XAGFUT-K, Jump XAUUSD, IG silver futs XAGFUT-K. Spread analysis: IG consistently wider than CMC for XAU/XAG futures, so even after adding IG_CENTROID to hedging markets the majority of risk would still cover at CMC. IG positioned as a backstop after CMC has been seen withdrawing price on futs. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777293198876179)

> [open] 2026-04-24 — Gold/silver futures contract rollover subscriptions (GC6Q_, SI6N_)
> April gold (GC6M_) expiring; GC6Q_ activation 2026-04-27 — Nikos asked Rory to prep the subscription. Silver SI6N_ first notice ~week out. CMC + IG pricing gold/silver futures but Jump still not pricing any futures — Rory following up. US index futures (NQ6M_ etc.) also being set up; Rory confirming sub-symbol convention and min/step sizes with Maynard. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1776958276713199)

> [open] 2026-04-23 — Gold skew post instant uplift
> Uplift 2x last week on volume, but skew predictiveness slipped since Wed's instant uplift. Isaac proposing: bump base spread proportion 0.5→1.0, double Twilight base/benchmark, new LDN overrides at 1.2, swap IFMS→IFM. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776976532606559)

> [open] 2026-04-23 — Silver skew pulled pending investigation
> Silver skew dragging FI PnL down; Will removed while investigating. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776934554832829)

> [open] 2026-04-23 — CMC XAUUSD latency review (Steerco ask)
> Steerco flagged CMC latency on XAUUSD; Mahi to pull stats. Also on the list: indexes next week, new futures books, start with 121 futures + 121 cash before normalisation. Karen still waiting on email re support. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776943121111249)

> [open] 2026-04-21 — Nikos requesting daily skew files
> Nikos asking for skew files daily (email or Pulse), wants an ETA even if ~2 weeks out. Awaiting Rory/Will reply. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776765921428599)

> [open] 2026-04-22 — XAU futs hedger timing on large positions
> Cpty 8004007 generated small PnL drop via XAU futs — hedger took ~30s to cover 512oz. Rory digging into decreasing timing for larger incoming positions. Supersedes prior XAG hedger-wait tuning. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776860083517709)

> [resolved] 2026-04-22 — XAU + XAG futures internalisation live
> XAU futs live 09:17 BST (first trade internalised + hedged), XAG futs live 13:53 BST. FI yield +10x day-on-day post-changes (2026-04-21). LR levers tuned for new arb cpty 8008699: 1.2 multiplier + 1s rate-limit period (max-reduction $200/M lifted earlier). Profile definitions copied from spot XAG/XAU to fix holding risk too long. Futures routed to CMC_CENTROID under separate per-instrument book structure; bridge maps `GC6{M,J}_→XAUFUT-{M,J}` / `SI6{K,N}_→XAGFUT-{K,N}` on tag 55. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776845875089209)

> [resolved] 2026-04-13 — dashboard snapshot outage
> Post-release regression from MahiMain commit 066fb9437 (addServiceInBackground race in `riskReportSnapshotRequestPublisher`) stopped AggregateReportStream snapshots; Amana couldn't use the Trading Overview. Justin rolled back the webstack change same day (`512a10b`). Followup on moving `brokerDashboard` to core component still open in #dev. [permalink](https://mahifx.slack.com/archives/C8568C6HG/p1776073126336049)

## Notable topics

- 2026-05-01 — Nikos requesting additional LPs enabled for mid-aggregation / pricing discovery; Rory to confirm config link once done. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777632975290609)
- 2026-05-01 — DOWFUT-M MWMS pricing blowing out wider than CMC_CENTROID (second layer in CMC_CENTROID 500pts wide vs TOB 25/50); Will bodged with BMSL, not blocking overall rollout. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777629122174899)
- 2026-04-30 — Will/Nikos call: management very happy with performance, "numbers are amazing", goal is all flow into Mahi. A-book onboarding expected done EOW. B-book pricing plan: 3 tiers (gold/silver/bronze rate formation); tagging strategies for LP-moaning-on-tag scenarios also discussed. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777549918317059)
- 2026-04-30 — Index CFD hybrid hedger added to criticalHedgerBooks; pricerA1/2 bounced to pick up MWMS change; futs hedger config updated for equity/index inclusion (pricing.filter.list fix). [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777624977789949)
- 2026-04-29 — Arb-er execution + LR profile additions for XAU FUT clients reacting to CMC skews. Nikos added cptys 5800049/53/54/55, 8009564, 8011740, 5800057, 5800048, 5800093, 5800092 to the "XAU, XAG - Futures Internalise" rule + LR profile (Isaac applied; 8008699 re-added after disappearing from one of the profiles). [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777447305075599)
- 2026-04-28 — Will speaking to Nikos about doing XAUUSD B-book pricing properly: 8c stable TOB with panic-stations MWMS + BMSL beyond 100oz; connectivity already in place. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777386952494079)
- 2026-04-28 — Nikos roll-out plan (call): A-book first across cash indices to prove workflow, then B-book once spreads agreed (IG call later this week on metals futures spreads); B-book index volume ~90mio/day vs A-book ~10mio. Granular: indices first, oil/gas after.
- 2026-04-21 — P&L Attribution KB article added (`kbPnlAttribution`) to Compass knowledge base, covering risk-path closed-system P&L, 0→120m/0→20m horizons, and reconciliation vs Account Summary. Driven by Nikos asking for per-client trading PnL attribution. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776760822802469)
- 2026-05-05 — XAUUSD skew bumped overnight by Isaac: IFMS `priceAdjustmentAsProportionOfBaseSpread` 0.5→0.8, `priceAdjustmentAsProportionOfBenchmarkSpread` 0.5→0.8; flow-price-thresh base 0.3→0.4, benchmark 0.2→0.4. Yield trajectory: 5.53→8.80→12.55 $/M this week. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777978361549719)
- 2026-05-05 — Direct-brokered/STP execution rule created by Rory for arbing DOW counterparty 8011825 (manually selected tag only, same structure as arber profile). Nikos requested at 10:17. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777972663980609)
- 2026-05-07 — Nikos call (Will/Rory/Cameron Hughes): next milestones are EU/Asian indices (cash + futures 20/30), then FX. FX: Karen to decommission MahiFX B, all FX flow to come down Mahi A — no rigorous testing needed, just spread agreement. B-book: repurpose existing feeds for "Corporate Retail" use case (requirements to follow from Muhammad/Sales). MT5 account 30001612 flagged as the index volume account — Nikos requested backtest analysis. Systematic internalisation keen for index flow. Yield profiles need fixing to correct LP. Most toxic tags are on indexes, EA-based arb seen in B-book. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1778153148.867759)
- 2026-05-07 — Index futures normalisation config actioned by Rory: referencePriceMarketSelectors (CMC_CENTROID + IG_CENTROID for index futures), signalReturnBenchmarkMarket (DOW→IG_CENTROID; NDX/SPX/RTY→CMC_CENTROID), benchmarkNormalised enabled for index futures. Risk paths for CFD normalisation added by Cameron Hughes; CFD futures normalisation to follow. FI on CFDs blocked pending review of `pricing.adjustmentSignalProcessFlowImbalanceOptimisationParties`. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1778160903.317459)
- 2026-05-07 — Fat Feed XAU spot + futures spreads: Nikos sent updated CLIENT_PRICE_LDN spreads for XAU spot and futures; Rory noted minor tier discrepancies (400oz, 1000oz, 2100oz, 7200oz) vs earlier CSV, queried. Nikos approved current version; Rory imported to CLIENT_PRICE_LDN. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1778157380.042039)
- 2026-04-20 — LP price-withdrawal handling: Centroid now passes through 0/empty MD updates when an LP withdraws price; Will confirmed OK to enable on Mahi side (hedger will keep retrying, client experience preserved). [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776681806903129)
