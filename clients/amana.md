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
last_catchup: 2026-05-05T07:19:55Z
---

## Recent issues

> [open] 2026-05-05 — XAUUSD limit order rejected LIQUIDITY_VIOLATION: off-market limit price
> Princess reported a sell limit order on XAUUSD rejected with `LIQUIDITY_VIOLATION`; tag1=ABOOK, order sent at 4550.95 sell-limit, published price was 4550.77/4550.89 at time of receipt — order was off-market. Daria explained the rejection. Princess followed up at 07:39 asking if resolved; Will replied at 08:06 that Mahi will look into it today. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777960089109199)

> [resolved] 2026-05-04 — monitoring.pnlDrop: false PnL drop alerts suppressed for futures books
> Nathan Burch enabled `useTradePositionPnl` in `monitoring.pnlDrop` config. XAGFUT (and other futures instruments) were triggering false PnL drop alerts because PnL was calculated by converting futures positions using the spot price — the inherent futures/spot price differential caused alerts to fire incorrectly. No book-specific override exists, so the change applies to all books. [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1777850060789949)

> [resolved] 2026-05-01 — DOWUSD tag1 routing: trades falling into CMCSWAPFREE instead of ABOOK
> Rory noticed DOWUSD index CFD trades for some counterparties assigned `trading_account = CMCSWAPFREE` in Pulse instead of `ABOOK`. Root cause: `tag1=CMCSWAPFREE` being applied beyond metals. 2026-05-04: Karen confirmed she will scope CMCSWAPFREE to spot metals only; Cameron Hughes clarified spot FX/metals can keep the tag, indices/CFDs should have it removed. Karen confirmed done at 10:05. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777885500546369)

> [open] 2026-05-01 — Index futures go-live blocked by TOO_SMALL quantity validation
> DOWFUT-M and NDXFUT-M test trading attempted 2026-05-01 morning; Princess test trade rejected with `DISTRIBUTION_LDN-maximumShowQuantity=TOO_SMALL, quantity=TOO_SMALL`. Root cause identified by Rory but requires weekend EOD restarts to take effect — US futures index go-live pushed to early next week. In the meantime: continuing setup for all other cash + futures equity indices (EU, Asia), collecting step/min sizes from Princess/Nikos. Princess provided min+step per LP at 13:46. Rory to revert with further items requiring EOD restarts. [permalink](https://mahifx.slack.com/archives/C08SYSMP0EB/p1777629657810339)

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
- 2026-04-20 — LP price-withdrawal handling: Centroid now passes through 0/empty MD updates when an LP withdraws price; Will confirmed OK to enable on Mahi side (hedger will keep retrying, client experience preserved). [permalink](https://mahifx.slack.com/archives/C08T42TMKU3/p1776681806903129)
