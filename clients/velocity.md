---
slug: velocity
refs:
  vibepulse: ../VibePulse/.claude/clients/velocity.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: velocity
  hosts: ../MahiProduct/data/client-hosts.json          # entry: velocity
  wiki: null                                             # ../MahiProduct/wiki/clients/velocity.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Dan", role: "client ops — yield profile / Echo lookups", confidence: low}
  - {name: "Richard Holman", role: "VT — sets pricing/hedging policy expectations", confidence: low}
  - {name: "Jackson", role: "VT — ops/technical, sent GTC order credentials", confidence: low}
last_catchup: 2026-05-15T07:34:59Z
---

## Recent issues

> [open] 2026-05-11 — NWM_HSBC LP disconnection — "Credentials disabled"
> At 01:51 UTC 2026-05-11, Velocity's FIX session to NWM_HSBC (`VELBINT099HS-price`) logged out with "Credentials disabled, please contact support". Nathan Burch raised in the client channel at 02:54 BST. No thread replies; resolution unconfirmed. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1778464467.944329)

> [resolved] 2026-05-11 — hybridHedgerSITotal1 went down during Will Carter predicate test
> Inald Gjoni restarted `hybridHedgerSITotal1` after it went down at ~14:23 BST. Root cause: Will was testing a new `VAR-CLEARANCE-FASTER` predicate on `SI_BOOK_NET`; the party was not whitelisted, causing `IllegalStateException` on rule build for XAGUSD. Will asked Inald to revert to pre-change config and not touch `hybrid1`. Back up by 14:37 BST. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1778505824.369029)

> [open] 2026-05-08 — XAU crosses: client seeing no pricing (except XAUAUD)
> Client (Richard) reported at 09:31 BST: "on the xau crosses, I see a price in aud but none of the others?" William investigated; at 11:40 BST asked client to confirm whether they had sent FIX MD subscriptions for XAUCHF, XAUEUR, XAUGBP, XAUJPY, XAUNZD, XAUSGD — no subscription logs visible from client side. XAUAUD working; XAUCNH not yet priced on Mahi side. No resolution confirmed in window. Ties into existing [open] 2026-05-07 XAU crosses test trades item. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1778229098.287779) [William ask](https://mahifx.slack.com/archives/C05NB72AGR2/p1778236837.382589)

> [open] 2026-05-05 — Allow Top Up on A_CLIENTS_PREMIUM/Broker Everything Temp disabled after 350 XAU internalisation loss
> At 16:10 UTC 2026-05-04, counterparty 889 placed a 750 XAU order on DistributionLDN (A_CLIENTS_PREMIUM//Broker Everything Temp, execution rule: broker). Compass brokered 400 XAU; the remaining 350 XAU was internalised via Allow Top Up. Price moved against the book immediately — full 350 XAU hedged to cap further losses but loss already realised. Nathan Burch disabled Allow Top Up for this execution rule as a protective measure, noting counterparties in this classification trade directionally. He flagged this for review: Allow Top Up is currently on for all other execution rules — possibly intended to protect client fills — and the policy should be revisited. By 09:04 UTC+1 2026-05-05 Will confirmed "book has recovered somewhat so far this morning" and endorsed the disable ("that's the right call — thanks Nathan"). Policy review of Allow Top Up across other execution rules remains open. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1777957038011259) [recovery confirm](https://mahifx.slack.com/archives/CPDS0M2KF/p1777968282.241929)

> [open] 2026-05-05 — New connection for inventory skewed feed — status unconfirmed
> William Denny asked in the client channel at 11:59 BST: "can I check on the status of the new connection for the inventory skewed feed?" No reply in window. Context: client was asking about Compass sims and XAU crosses in the same conversation; the inventory skewed feed is a separate pending item. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777978746.882379)

> [open] 2026-05-05 — Client requesting hold-position analysis on internalised flow
> Richard (or another client-side contact) asked at 11:32 BST: "on the flow we've internalised can we run some analysis on that to see what the outcome would have been if we held onto the position at different intervals? vs where it was hedged." William pointed at the Echo yield profiles for A_CLIENTS_PREMIUM (2026-04-28–2026-05-05) as the relevant data source. Client acknowledged at 13:00. Analysis not delivered in window. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777977153.873319)

> [open] 2026-05-01 — Overnight losses, chunky position offside; LTD equity recovering
> Client (Richard) flagged at 09:12: "looks like we took a hit overnight / spreads too tight?". Will had already posted Echo yield-profile link at 08:24 and pinged William Denny "need to look into this asap". William confirmed checking at 09:13. Will's read at 09:37: position went offside quickly, "sort of locked in that loss at 10-15 seconds"; told client to "trust the process a bit today, hopefully the yield quality evens out". Root cause (too-tight spreads vs chunky directional flow) under investigation — no resolution in window. 2026-05-07 update (internal): Will Carter: "LTD equity down 5k. Considerably better than last time round with improvements to come." [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777624588186949) [2026-05-07 update](https://mahifx.slack.com/archives/CPDS0M2KF/p1778147786077159)

> [open] 2026-04-30 — Arb hedger reconfigured to breathe more; EOD hedger restart timed poorly
> Will put changes into arb hedger at 16:57 to "let initial risk breathe more" and slowed the hybrid down. Hedger restarted at EOD — Will noted "wrong time to restart the hedger", PnL expected to fluctuate more. Feeds into 2026-05-01 overnight losses above. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777564631716889)

> [open] 2026-04-29 — Premium channel rollout for tags 911 / 960 / 960a — initial losses, multiple rounds of tuning
> William Denny ran yield-profile analysis of the CSV client datasets (CELER, GNT, SQB, Royal still processing) and confirmed 911/960/960a suitable for fast hedge (10-30s yield curves). Premium feed switched from STP back to internalise+10-30s hedge. Day saw losses from "drip-feed" flow on premium with wide LP pool: Will flagged "can't see how we're going to monetise this drip feed of flow by risk managing it on premium spreads", "the LP pool is so much wider than our 15 currently". Richard Holman pushed back: "hedging spreads are going to be wider — that's kind of the whole point". Tweaks during the day: configured premium channel to widen to pool TOB over ROLL / TWILIGHT / SNGMON; doubled all time-delay triggers and bounced hedger; reduced TOB qty (1st layer 50oz @ 15c, 2nd layer 50oz @ 35c static); switched fill source from internal to published. By EOD pnl recovering. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777462632819049)

> [open] 2026-04-30 — Overnight overhedge + missing B pricing model
> Daria diagnosed early-morning losses: hybrid + arb both bought 50oz from GS, hybrid sold 46oz to XTX 100ms later with no client trades between (overhedge cost ~$18). Also flagged missing B pricing model in Echo — restarting `starfishFilePersisterExternalMD` to start persisting. Will: "to be expected with MWMS on ROLL and TL". [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1777520549312209)

> [open] 2026-04-30 — Internal strategy debate: license risk if flow doesn't grow
> Internal channel discussion (Andrew Morgan, David Cooney, Will): flow remains minimal, "strong danger of license petering out if we can't sort something". David suggested plugging into Argamon (tight client spreads, wide LP spreads, no flow diversity needs another ingredient — TOA-Argamon CME also raised). Andrew floated partitioning the book into "real retail vs dirt bags" (two models — one defensive, one skew aggressively); is also moving his mid-evaluation feature branch onto velocity as a playground. Will: 200/day is critical mass; last 24h roughly flat post-changes. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1777540196996579)

> [open] 2026-04-30 — Compass sims being rerun on combined client trade data
> William Denny: need to rerun Compass sims to pick up changed hedger + pricing config. Ready for tomorrow (2026-05-01). [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777547238227629)

> [resolved] 2026-04-30 — XAUUSD priceFormatPipRelative for LMAX — fixOrders2 restarted EOD
> Shyam: PagerDuty alert needed `priceFormatPipRelative` for XAUUSD & LMAX changed from 0.01 to 0.001. Config change already made; `fixOrders2` restarted at EOD (Will's hedger restart at ~17:08 confirms). LMAX re-added as LP for `hybridHedger1` post-restart. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1777520897089699)

> [resolved] 2026-04-28 — Dan's question on one-sided / risk-skewed pricing — discussed on call 2026-04-30
> Dan asked: can one API show a wide two-price and skew one side in when there's risk to get out? William Denny replied "our pricers won't go one-sided". Dan re-asked with refinement on 2026-04-29; Will Carter: asymmetric skewing possible (tighten one side via signals), teasing in from a wide price feasible — risk-skewing into VT's own pool needs design thought. Agreed to discuss on call; huddle held 2026-04-30 at 11:03. No follow-up outstanding. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777384240375059)

> [resolved] 2026-04-29 — CSV_CLIENTS drop-copy yield profiles backfilled
> William Denny backfilled missing yield profiles for the CSV_CLIENTS drop copies. Dan to do check-backs vs Horizon. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777471939461419)

> [open] 2026-04-23 — Xenfin (XF) CSV upload latency — moving to once-daily uploads
> Dan couldn't see yield profiles for counterparties 1009 / 851 in Echo. Daria diagnosed: Echo's counterparty field uses the obfuscated client ID (in `cpty_anon` column of the XF CSVs). Morning huddle (Will, Cameron Hughes, William Denny) agreed Mahi moves to once-a-day upload of all Xenfin CSVs until Xenfin fixes the latency. Will put a fix in for XF CSV lag — 60-min trade-to-yield-profile lag now (vs prior EOD). [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1776927890282329)

## Notable topics

- 2026-05-11 — Hybrid hedger PnL backstop + longer pull-away — design doc posted by Will Carter. Two-rule hybrid setup: (1) primary dynamic fasthedge with extended pull-away (`minPullAwayPeriodMs: 60000, maxPullAwayPeriodMs: 300000`, IFMS signal); (2) top-priority `VAR-CLEARANCE` backstop using `OwnTradingPerformancePredicate` (inverted: `maxPnlInBase: -1000`, 30s lookback) + `VarTrigger` to cannon-flatten when book is down ≥$1k in last 30s. Seven open questions before backtest (RelativeRisk JSON shape, VaR% reference, monitorParty value, realised-vs-unrealised PnL, IFMS signal direction, re-arm behaviour, backtest harness). Five-phase rollout: config verify → Compass backtest → shadow mode → live conservative → tune. James (MahiMain) offered to add `OwnTradingPerformanceTrigger` to HEDGING service type as Plan B. Pre-backtest, not yet deployed. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1778501713.503449)
- 2026-05-11 — Arb hedger bounced to increase clip size; Will noting possibility of RI. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1778502648.313889)
- 2026-05-10 — Nathan Burch removed USDCNH from SIGNAL-PROXY list and added `riskReportingExtended` override on marketInstruments reference config. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1778397244.340729)
- 2026-05-08 — Will Carter chatting with Richard about adding more instruments; reviewing hedging approach in `#hedging-design` (`hybrid hedger book pnl triggers` thread). [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1778225747.580269)
- 2026-05-07 — Will Carter internal planning note: mid changes going to beta; gold crosses to be activated (expected to make money hedging in drivers); signals approach — pull-away predicates of seconds not milliseconds with a 1k stop-loss cannon; theme of giving Velocity ownership of rate construction to market to clients continuing; no questions on the bill. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1778145258473989)
- 2026-05-06 — Pricers bounced: synapse → flow-price-thresh on XAUUSD adjustment signal params. William Denny bounced pricers at 17:33 BST to switch from synapse to flow-price-thresh on the XAUUSD adjustment signal parameters. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1778085235.796909)
- 2026-05-06 — Will Carter posted Echo yield-profile link (internal, no message text) covering 2026-05-03–2026-05-08, filtered on negative yield across all velocity parties. Indicates ongoing monitoring of loss-heavy flow post-Allow-Top-Up disable and arb hedger reconfig. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1778072376.401969)
- 2026-05-07 — XAU crosses test trades agreed; pending hedger setup completion on Mahi side. William Denny asked Richard: "Shall we arrange some test trades for the XAU crosses once the hedger setup is all done on our end?" — Richard replied "sure". Hedger setup still in progress. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1778161039114649)
- 2026-05-05 — XAU crosses setup believed done; client requesting hedger workflow test trades. Richard asked "are we done on the XAU crosses?"; William said "believe the setup is done"; Richard wants test trades per cross to verify hedger workflow. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777973517.232639)
- 2026-05-06 — Compass sims still pending; parameters being tweaked. Client asked "are we still waiting on the sim?" at 10:02 BST; William Denny replied at 10:39: "sorry for the delay, we've been tweaking the parameters of the config to get the best output from the sims so will keep you updated when these are ready to share." [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1778060398.191679)
- 2026-05-05 — Compass sims still pending as of 09:03 BST. Richard asked "hoping the sim has run now?"; William: "checking on the sims now". No confirmed outcome in window. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777968117.606539)
- 2026-05-01 — Bank holiday Monday 4 May: Mahi emergency-only coverage, Slack less monitored. Client channel notified; support email / phone numbers provided. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777622405037559)
- 2026-04-30 — GS hedging looking better $/M on XAU (small sample); GS spread flickering 18/36 then settling 35-40. Premium-channel widens to pool TOB on ROLL/TWILIGHT/SNGMON. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1777452886321469)
- 2026-04-30 — Pricing channel taxonomy clarified by Will: `CLIENT_PRICE_LDN` (wide spreads, matches pool via MWMS, channel `A_CLIENTS`, currently internalise+hedge); `CLIENT_PRICE_B_LDN` (premium spreads, stable 50oz XAU TOB ~15oz, channel `A_CLIENTS_PREMIUM`, internalise+hedge); party `CLIENTS_CSV` is the post-trade drop-copy from Xenfin used for whole-book yield profiles (last 2 weeks). [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1777540742930749)
- 2026-04-29 — Will floated the structural tension out loud: "How do we monetise this mofo with truck wide spreads at the LPs". SI flagged as best option but yields not there yet. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1777460625699159)
- 2026-04-23 — Huddle action items (recap): (1) once-daily Xenfin CSV upload; (2) VT working on hedge liquidity + cautious bank skew (can't be aggressive or it's lost); (3) Mahi to add pricing for XAU crosses + other majors (low-hanging fruit); (4) look at reducing XAU TOB; (5) VT has more prospect data to upload. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1776936723214169)
- 2026-04-23 — XAU triangulated crosses added (XAU/{AUD,CHF,CNH,EUR,GBP,JPY,NZD,SGD}); pricers + dashGW bounced. Action item #3 from huddle. [permalink](https://mahifx.slack.com/archives/CPDS0M2KF/p1776954962207129)
- 2026-04-23 — VEL000951 on-prem per chat. [permalink](https://mahifx.slack.com/archives/C05NB72AGR2/p1776936286728029)
