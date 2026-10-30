---
slug: gomarkets
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/gomarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: gomarkets
  hosts: ../MahiProduct/data/client-hosts.json          # entry: gomarkets
  wiki: ../MahiProduct/wiki/clients/gomarkets.md
channels:
  internal-go: CNF3WPNSK
  mahi-gomarkets-2025: C09J1DP2QQH
contacts:
  - {name: "Erik Ogkanesian", role: "client ops — reconciliation / book splits / risk-splitting / blacklist asks", confidence: low}
  - {name: "Mac Nemeth", role: "client ops — hedging, price forensics, book adjustments", confidence: low}
  - {name: "Will Rozet", role: "client ops — LP connections (AU migration), hedger/arb-hedger usage, pricing config", confidence: low}
  - {name: "Kieran Hauenstein", role: "client principal-level ops — pricing/skew calls, inventory hedging, NOP limits", confidence: low}
  - {name: "Alexandros Paraskevopoulos", role: "client ops (Cyprus) — Compass/Echo read-only user, training calls", confidence: low}
  - {name: "Andreas Hatzimitsos", role: "client ops (Cyprus) — Compass/Echo read-only, training calls", confidence: low}
  - {name: "Orpheas Paphitis", role: "client — acknowledged channel/book changes 2026-08", confidence: low}
  - {name: "Regina", role: "client ops — Centroid bridge / FIX session incidents (older context)", confidence: low}
  - {name: "David", role: "client ops — execution-rule / pricing-model questions (older context)", confidence: low}
last_catchup: 2026-10-30T07:21:17Z
status: active
---

## Now
Active, metals-heavy broker client (XAUUSD) on a NYC Compass stack, hands-on and still learning the tooling (Cyprus staff in weekly training). Live threads: LP-entity migration to AU venues via *_HOLDING markets (cutover set for 2026-11-02; Finalto dropped, no automatic failover), Radex risk-splitting residue plus an incoming MeanFin flow, and Go's gateway saturation from ~20 channels. Pricing smoothness (flicker vs the MetaQuotes feed) and a suspicious MINT LP feed are the sensitive pricing items.

## Streams

### counterparty-blacklist — Blacklist / exclude counterparties on hedge cancels and rejections
status: open · since: 2026-10-12 · last: 2026-10-30
State: Erik asked on 2026-10-12 for account 81259604 to be excluded from iSAM hedging (Kate added it to the blacklist) and whether a background script could auto-blacklist counterparties reaching X rejections; no substantive answer seen. Since 2026-10-21 ISPRIME has cancelled hedges of a single counterparty within ~13ms nearly daily (HEDGING_MODEL_H1_NYC alerts); the H1 hedger retries ISPRIME every ~200ms with no fallback LP until the account is blacklisted. On 2026-10-29 Isaac blacklisted tag 95000689 from ISPRIME and told Go (Orpheas will investigate on Go's side; hedging cancels only, client execution unaffected). Isaac asked internally whether to make this a routine (flag the CP early) or product automation (auto-blacklist a CP on an LP after N zero-fill cancels and route elsewhere); Shyam replied it would be great automated in the product.
Next: Mahi to decide routine vs product automation (and answer Erik's auto-blacklist ask); Go to investigate the ISPRIME cancels.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1791819586672009 https://mahifx.slack.com/archives/C09J1DP2QQH/p1793266711610419 https://mahifx.slack.com/archives/CNF3WPNSK/p1793267765705429

### au-lp-migration — LP migration to Go's Australian entity via *_HOLDING markets
status: open · since: 2026-09-08 · last: 2026-10-27
State: Will announced LPs (ISPRIME, 26DEGREES, FINALTO, LMAX_LDN; LMAX and IG re-pointed at Go's end) move to Go's AU entity. Plan: Mahi keeps existing market names, Go builds AU connections mapped to *_HOLDING markets, Go switches pricing and execution routing on the existing channels on its side (no Mahi config change), Mahi then moves positions from the current LP books into the _HOLDING books and hedgers trade them out into the AU LPs. Nathan built the holding FIX sessions (2026-09-16); 26DEGREES_HOLDING test trade worked; ISAM_HOLDING and LMAX_HOLDING tests due next week. On 2026-10-22 Will set the cutover for Monday 2026-11-02 before the trading day (22:00 UTC, NY exits DST 11-01) for 26DEGREES, ISAM and LMAX; Finalto is delayed and not in that switch. IG becomes available as an LP afterwards. Nathan confirmed Mahi is ready. Go call 2026-10-27: Go will close out all Finalto positions and not re-open (trouble setting up its Finalto AU entity); no automatic OZ routing, Go switches manually with ISAM as failover LP; Kieran declined an automatic in-OZ failover and any extra Mahi failover unless free; if Mahi's servers went down Go's 24/7 support would switch flow manually (AU team knows how, Cyprus being trained), so some downtime is likely in that case. Follow-up call NZ Friday to confirm time and finalise the plan.
Next: Go to confirm ISAM_HOLDING and LMAX_HOLDING tests and message Mahi when the switch is done; Mahi to move positions into the HOLDING books on 11-02; Nathan to post a specific plan to Compass config this week and confirm time on the NZ Friday call.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1788907409824289 https://mahifx.slack.com/archives/C09J1DP2QQH/p1792703988337029 https://mahifx.slack.com/archives/CNF3WPNSK/p1793072238317139

### lr-benign-flow — Published LR also charged on benign counterparties
status: open · since: 2026-10-27 · last: 2026-10-27
State: Isaac noted that because Go runs published LR, LR also lands on benign flow: the lr-health check on 2026-10-02 flagged 57 benign counterparties charged about $4.6k in total (mostly a few hundred dollars each, largest ~$1.6k). He dismissed the cards as the expected cost of published LR. If Go asks about fills for good clients, a more targeted setup (Infinox approach: penalise toxic flow harder, benign less) could be offered, but it shows up mostly as slippage so needs client sign-off and probably ties into Go's colour-routing work; unclear Go would be interested.
Next: Nathan to decide whether to raise it with Go; no client action.
Refs: https://mahifx.slack.com/archives/CNF3WPNSK/p1793119374681369

### ig-demo-stream — New IG DEMO price stream for latency comparison
status: open · since: 2026-10-22 · last: 2026-10-22
State: Mac said Go will receive a new IG DEMO price stream with improved Spot Gold and Silver latency and asked for analysis over a couple of news events against Go's other LPs and the current IG stream; it must NOT be included in any models. Nathan will set up the market in Compass today, needs the FIX session details from Go, and data flows after the EOD restart. No historic data exists, so analysis waits for a few news events; Mac agreed. Nathan asked Go to say once the price stream is received.
Next: Go to send FIX session details and confirm the stream is received; Mahi to run the news-event latency comparison once data has accumulated.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1792629269396489 https://mahifx.slack.com/archives/C09J1DP2QQH/p1792636384267029

### open-latency-cancels — Weekend release and post-restart open latency cancels
status: open · since: 2026-10-16 · last: 2026-10-18
State: Compass 26.4 was announced to Go on 2026-10-16 (performance, stability, UI) and completed 2026-10-17 at the Saturday reboot. At the 2026-10-18 21:01 UTC open, 57 orders in the first second were cancelled by the internal latency safeguard ("excessive internal latency") because the order-handling process was still warming up after the weekend restart; normal by 21:01:02, no further cancels. Nathan raised a dev ticket on why the post-restart warm-up did not prepare the process; Will accepted, minimal impact.
Next: Mahi dev to review why warm-up failed to cover the open.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1792164137750009 https://mahifx.slack.com/archives/C09J1DP2QQH/p1792361497379359

### channel-refactor — Regional channel/book refactor and gateway latency
status: open · since: 2026-08-27 · last: 2026-10-15
State: Isaac created B_FX_20_METAL_50 and mirror A20_FX_20_METAL_50 markup channels (20 $/M FX, 50 $/M metals, 20% risk split to A) and recommended rolling regional books (e.g. B_CLIENTS_AU_NYC) back into B_CLIENTS_NYC before adding more; Erik is testing and will plan at scale, client sign-off on the cleanup plan was not seen. On 2026-10-14 Isaac and Nathan found Go's gateway saturated: ~20 channels make the single CEP thread on clientDistributionGateway1 recompute each tick per channel (~18k updates/s, ~52% from the 10 regional channels), pushing last-look releases past their window. Decision: raise distribution.node.advanced.numberOfCEPThreads first and hold off asking Go to decommission channels. On 2026-10-15 Isaac set numberOfCEPThreads to 2 (pending EOD restart) and, on Liam's suggestion, switched the sharding strategy to counterparty mode; longer plan is remapping by new trading accounts to markup channels, but riskSplitting cannot split by trading account.
Next: confirm effect on last-look release timing after the EOD restart; Nathan to chase Go on the markup/risk-splitting refactor afterwards.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1787846033418999 https://mahifx.slack.com/archives/CNF3WPNSK/p1792075782283879

### brokered-xau-markup — GO XAU brokering: internalisation trial and execution-rule markup
status: open · since: 2026-10-15 · last: 2026-10-15
State: Isaac corrected an earlier internalisation-trial uplift, which had kept the client's slipped brokered fill price. Re-priced at book VWAP with a 200ms last look, internalising Large XAU, Fast Hedge and Don't B Book shows no significant gain at 30s or 1m; Signal Follow clearly belongs brokered. No trial for now. Use case for the roadmapped execution-rule markup: brokered market orders slip at every venue while limit-order hedging is cheap, so markup would allow internalising toxic profiles and hedging via H1/arb.
Refs: https://mahifx.slack.com/archives/CNF3WPNSK/p1792069620138069

### radex-risk-split — Radex A/B risk splitting, residual hedges, MeanFin
status: open · since: 2026-07-21 · last: 2026-10-14
State: Radex flow (A_CLIENTS_RA) is soft-classified and risk-split A to B automatically, which ignores clients closing their own trades, so lumpy flow leaves residual LP hedges: XAU on 2026-09-04 (Isaac netted everything into B for now; he floated turning splitting off or fully A- or B-booking Radex; Erik floated re-splitting open exposure when classification changes), and NZDCAD 12m opened in A and closed in B (2026-09-25), resolved by Daria's options (A-to-B move triggers the hedger to unwind, or close via the trading hedger). Mac adjusted into B_CLIENTS_RA_NYC_SPLIT on 09-28; Daria said adjusting directly into B_CLIENTS_RA_NYC is the correct exception to the child-book rule. Go will onboard a new institutional client MeanFin on the Radex session (tag 1 = MEANFIN, same pricing and risk-splitting config); set up, no start ETA, not enabled without notice. On 2026-10-14 Mac asked why Radex skews more than regular clients; Nathan explained the signal config is identical and Radex's wider XAUUSD base spread (0.11 vs 0.07) scales skew, Mac accepted.
Next: Nathan to update the team when Go gives a MeanFin start date. The underlying split-versus-closes design problem is not formally decided.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1788528415870089 https://mahifx.slack.com/archives/C09J1DP2QQH/p1790301122048699 https://mahifx.slack.com/archives/CNF3WPNSK/p1791775388999269 https://mahifx.slack.com/archives/C09J1DP2QQH/p1791952706615519

### lp-hedging-limits — LP hedging behaviour, NOP limits, clearing positions
status: open · since: 2026-06-09 · last: 2026-10-06
State: Finalto hedging stopped from 2026-09-01 because its per-LP NOP limit (10m high / 8m low watermark) tripped and stayed tripped (not a config change); Will cut the position. On 2026-10-01 Go put Finalto reducing-only and Shyam adjusted NOP settings; Kate reverted them 10-02 at Mac's request. On 09-28 Mahi cleared a 14.49m over-hedged ISPRIME AUDUSD via arbHedgerSubTrading1 plus an adjustment from B_HEDGING_MANUAL (worked, hedger switched off). USDMXN residual LP positions (09-18): no auto reduce-exposure model, Daria suggested small internalise rules before brokering. On 2026-10-06 Will reported ~70% LMAX_LDN rejection and very little flow; Nathan said hedgers do not rank LPs (best aggregated quote wins; LMAX_LDN gold spread ~8x ISPRIME so rarely competitive) and is investigating the reject rate.
Next: Nathan to report back on why LMAX_LDN is rejecting ~70%.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1788419249269449 https://mahifx.slack.com/archives/C09J1DP2QQH/p1790556017984519 https://mahifx.slack.com/archives/C09J1DP2QQH/p1791253970054589

### xau-pricing-skew — Gold/FX pricing smoothness, skew and failover
status: watching · since: 2026-06-01 · last: 2026-09-17
State: 2026-08-18 call: Kieran happy with skew sizes and slippage complaints down but wants smoother price; Go publishes to MetaQuotes every ~80ms while fills use live Compass price, which flickers; Daria suggested throttling publishing, Nathan investigating flicker before skew goes up again. 08-19 Isaac cut benchmark spread skew weight on FX after Mac's AUDCAD jumps (flow-price-thresh). 09-15 call: client price went offline and failover to the continuity pool published huge spikes; Kieran wants no price unless the client-price LPs are online; Isaac removed MAHI_CONTINUITY_NYC from the continuity pool meanwhile. 09-17: USDJPY indicative for ~8 min at open was Wide Spread Suppression (max 0.25 vs 0.267). Downgraded to watching: no activity since 09-17.
Next: Nathan to follow up on throttle/flicker root cause and the no-failover pricing change; no outcome seen.
Refs: https://mahifx.slack.com/archives/CNF3WPNSK/p1787014679025069 https://mahifx.slack.com/archives/CNF3WPNSK/p1789447371722669 https://mahifx.slack.com/archives/C09J1DP2QQH/p1789626541976419

### mint-inventory-book — Gold inventory hedging and the MINT LP
status: watching · since: 2026-08-25 · last: 2026-09-21
State: Go wants Compass to automate hedging excess gold risk above internal limits (inventory book and hedger, possibly an SI-book, plus an unwind hedger); Nathan confirmed a B-book gold hedger to a specific LP is possible. Go onboarded LP MINT CFD (FIX sessions set 2026-09-16). On 09-21 Nathan found MINT's XAUUSD feed looks like a copy of Go's own client price (0.969 mid correlation vs 0.33-0.57 for real LPs, +$0.04 spread, ~6ms lag) and Kieran had described a special relationship where Go can broker at a price they decide; concerns are MINT benefiting from Go's skew and Mahi hedgers picking MINT off. Logged on the wiki; not seen raised with Go in channel. Downgraded to watching: no activity since 09-21.
Next: Mahi to decide whether to raise the MINT feed finding with Go; inventory book build status unknown.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1787628603910739 https://mahifx.slack.com/archives/CNF3WPNSK/p1789949763533859

### lr-attribution — LR not attributed on liquidity-reduced fill
status: watching · since: 2026-09-15 · last: 2026-09-15
State: Isaac saw an A-book PnL bump from brokered trades where published price differed one-sidedly from client model price (confirmed LR via binlogs) yet Compass and yield profiles show no LR attribution; question logged on the wiki, no answer seen in 31d, downgraded to watching.
Next: Mahi dev answer on whether LR attribution is expected to be missing.
Refs: https://mahifx.slack.com/archives/CNF3WPNSK/p1789461866412159

### cyprus-onboarding — Cyprus staff onboarding and training
status: watching · since: 2026-08-03 · last: 2026-09-02
State: Andreas H and Alexandros (Cyprus) asked for educational calls on Mahi components (2026-08-25); Isaac runs weekly training calls (yields, price forensics, automation, execution rules). Alexandros asked what half-life measures (09-02, William Denny checking, no outcome seen). Mac's price-forensics rendering problem 09-10 resolved after Nathan's relink.
Refs: https://mahifx.slack.com/archives/C09J1DP2QQH/p1787646846925519 https://mahifx.slack.com/archives/C09J1DP2QQH/p1788337952132509

## Arc
- 2026-04-23 — All Books tenant profile migration; execution rules use All Books
- 2026-06-10 — Metal crosses and gram gold (GAUUSD, GAUCNH) live; hedging shifted to LMAX_LDN
- 2026-07-21 — B-book risk splitting added for Radex
- 2026-08-27 — A20/B_FX_20_METAL_50 markup channels created
- 2026-09-16 — LP *_HOLDING connections and MINT CFD LP onboarded
