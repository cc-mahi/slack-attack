---
slug: pepperstone
aliases: [pepperstone-crypto]
refs:
  vibepulse: [../VibePulse/.claude/clients/pepperstone.yaml, ../VibePulse/.claude/clients/pepperstone-crypto.yaml]
  billing: ../MahiProduct/data/billing/clients.json     # entry: pepperstone
  hosts: ../MahiProduct/data/client-hosts.json          # entries: pepperstone, pepperstone-cfd, pepperstone-crypto
  wiki: null                                             # ../MahiProduct/wiki/clients/pepperstone.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Stephen Hendrie", role: "exchange/product"}
  - {name: "Marianna", role: "trading ops", confidence: low}
  - {name: "Reece", role: "ops / counterparty admin", confidence: low}
  - {name: "Saif Nouri", role: "unknown — joined mahi-pepperstone-vnd 2026-05-11", confidence: low}
  - {name: "Ruby Wang", role: "ops / exchange trading", confidence: low}
last_catchup: 2026-06-16T07:23:28Z
---

## History

Extended lookback to relationship origin (2021). Underlying commercial arc anchored against billing (contract 2023-12-22, 3rd Addendum 2025-07-16). Slack channel `internal-pepperstone` created late June 2023 around board-approval; pre-2023 context is referenced rather than directly readable.

### Origin (~2021 → 2023)

> 2021–2022 — Initial conversations, first attempt lapses
> Earliest engagement traces back to ~2021. A prior negotiation went cold; by Aug 2023 the internal team referred to "the opportunity cost of not doing this 18 months ago". Mahi did ~3 months of work for free during the goodwill phase. April 2022: technical discussions on taker-group classifications; Beeks NY servers stood up around then. Chris Drummond (Pepperstone ops) and Marios (OZ-side ops) were the early counterparts.

> 2023-Q2/Q3 — Board approval, contract grind starts
> 2023-06-30: Mahi pitch crystallises — Zero-Spread MM in Japan, Flow-Imbalance signals, B-Book Timeboxed Internalisation, CFD normalisation/skew. 2023-07-04: Tom positive on new features + Indices add-on for board pitch. 2023-07-31: Pepperstone board approves (incl. CFDs). 2023-08-21: onboarding roadmap (Jira ANL-593) reused from the prior failed attempt. Commercial terms settled: $25k/m CFD risk-mgmt add-on, 1yr 5% / 3yr 10% discount, $3k setup waiver in exchange for a press release.

> 2023-Q4 — Legal back-and-forth
> Erin (Pepperstone procurement, ex IT-procurement at Microsoft) onboarded September; preferred 3yr term. Pepperstone legal revised OTC-Derivatives wording, changed auto-renewal from 3 → 12 months. November: internal leak investigation at Pepperstone (someone leaking LP arrangements / contract details) put the contract on lockdown briefly; tone shifted decisively in Mahi's favour ("desperate to get live"). Provisional Go-Live 1 Feb 2024 set.

> 2023-12-21 — Contract signed
> "2 years in the making". 3-year MSA covering MFXEcho + Compass + Pulse for FX and metals. AWS pass-throughs, Beeks managed by Mahi (no liability on Pepperstone). Targeted Go-Live 1 Feb 2024.

### Onboarding & Go-Live (2024)

> 2024-Q1 — Go-Live target slips
> Pentest (NCC) early Jan, training in London, Tapaas integration prioritised. Original 1 Feb target slipped to 4 March, then 25/26 March, then "before bank holiday". Marios (OZ ops) departed for Equiti early in this period without handover, blocking config — Chris and Evgeny detective-worked through it. Tapaas integration via REST API into Pulse. Daria Horton (Mahi) emerged as day-to-day ops lead. Beeks WAN capacity raised (2MBps → 15MBps; already saturated pre-go-live).

> 2024-Q2 — Live, then operational shakedown
> Live in production with Compass running FX MM by April 2024. May 2024 was bumpy: LP-vs-Compass position mismatches (SCB_NY AUDNZD out by ~$8M, traced to incorrect starting balances at go-live), OZ PTR running in parallel as safety net (removed at Tom's request late May), BAML_NY latency issues on USDJPY, position-allocation bugs between OZ and Compass. FI (Flow Imbalance) signal rollout discussions begin. LatAM/MXN marketing campaign timed against Mahi pricing; Chris used it to sell internally.

> 2024-Q3/Q4 — Compass FX matures, CFD reopens
> Hedger and signal optimisation ongoing through the year. Late 2024 / early 2025: Tom flags renewed interest in CFD licence ("once crypto is sorted") — re-opening the CFD conversation deferred since 2023.

### Crypto Exchange (2025)

> 2025-Q2 — Crypto Exchange (pcrypto.com) project starts
> Liam scoping with Tom for a Modulus-based crypto exchange where Mahi provides passive MM liquidity via FIX. Initial target end-July 2025, contingent on Pepperstone clearing regulatory hurdles. SOW 1 = Compass-side MM tooling; SOW 2 = Modulus integration. Acknowledged tension: risk-increasing passive MM isn't Mahi's traditional specialty.

> 2025-Q3 — Crypto A-Book hedging live
> 2025-07-07 planned spread cut + new symbols. A-Book test trades initially brokered (XBT excluded to avoid slippage), then internalisation. Hedged to B2C2 + LMAX; Wintermute initially rejected limits, later brought on as XETUSD benchmark market. UAT environment stood up in Pepperstone's own AWS account for FIX-integration shakedown.

> 2025-07-16 — 3rd Addendum signed
> 3-year term to 2028-07-16. New software fee $115,088/mo (was $127,876, 10% discount for term commitment), kicked in 2025-08-01. Covers MFXEcho + Compass + Pulse + Crypto. AWS capped $10k; Beeks $10k flat + GBP WAN/Crypto components. Cannot terminate for convenience during the 3yr term (clause 2.2.2).

> 2025-Q4 — Modulus exchange go-live (6 AUD pairs)
> BTC/AUD, ETH/AUD, XRP/AUD, SOL/AUD, USDT/AUD, USDC/AUD priced via B2C2_DIRECT in NYC; Crossover + LMAX direct feeds in LDN. propTrader deployed to NYC server. Volume ramps fast: ~40K trades/week in November, scaling to 1M+/week by Q1 2026.

> 2025-Q4 → 2026-Q1 — Operational pains during ramp
> Recurring failure modes: propTrader OOM-kills via fixOrders3, max-order-breach trips on propTraderCrypto1, cancel-reject loops triggered by Modulus FIX-server logout/reconnect cycles, disk pressure on `pepperstone-crypto-ny-admin-1`, USD/BCH position-reconciliation alerts. Drove the HRP passthrough gateway in LDN (Wintermute basis fallback when HRP cuts out) and tighter normalisation rules.

### CFD desk + Tokenised gold (2026)

> 2026-Q1 — Crypto SI hits profitability targets
> Every week in 2026 profitable. YTD through ~March: $2.84M ($2.46M trading + $378K skew). Skew (flow imbalance) consistently positive at ~$130K/month. Volume up ~25× since November.

> 2026-Q1 — CFD licence signed
> MK pushed early 2026 after years of "once crypto is sorted they'll be interested in CFDs". Negotiation: $50k/m full vs $15k/m hedging-only sub-component, settled on full package with discounted first 3 months. Volume guidance ~40bn (indices, commodities, futures; Exinity-style flow). David Cooney lead on Mahi commercial side.

> 2026-Q1/Q2 — CFD desk standup
> LDN CFD trading-server IPs delivered early April (public 149.5.84.149, OZ XC 10.74.101.142); NYC IPs follow (public 192.81.111.207/.240). Hedger-only initially; pricing layer planned ~3 months in. Diego Arranz (Pepperstone) coordinating OZ side.

> 2026-Q1 — Tokenised gold (tXAU)
> Pepperstone-branded tokenised gold product. Mahi normalises XAUT + PAXG into a single tXAU rate; passthrough gateways route tXAU orders to either underlying depending on flow. Open question on weekend XAUT/PAXG basis drift — dual-rate model (24/7 normalised vs primary B2C2+HRP PAXG-tracking) under review for XAU-close→XAU-open continuity.

### Stakeholders gained over the relationship

#### Pepperstone

- **Tom** — Exchange/product owner. Primary commercial/integration counterpart 2021–2025. Less visible post-Modulus go-live as Stephen takes over.
- **Stephen Hendrie** — Exchange/product lead since A-Book go-live (2025). Primary integration owner for crypto.
- **Marianna Konstantinidi (MK)** — Trading ops, ex-Exinity. CFD licence sponsor (2026-Q1), pushed the deal commercially.
- **Reece** — Ops / counterparty admin. Owns counterparty-classification and execution-rule conversations.
- **Chris Drummond** — Long-time ops/relationship contact. Core through 2023 contract grind and 2024 Go-Live; less visible 2025+ but still surfaces on long-running issues.
- **Diego Arranz** — CFD-side ops, OZ-configuration coordination (2026).
- **Erin** — Procurement/legal. Drove the 2023 contract signing; less visible since.

#### Mahi

- **Daria Horton** — Day-to-day Pepperstone ops lead since 2024 Go-Live. Single largest knowledge holder.
- **David Cooney** — Senior commercial. Lead on contract (2023), 3rd Addendum (2025), CFD licence (2026).
- **Nicola Perikhanyan** — Sales/relationship lead through the 2021–2024 contract grind. Less central post-Go-Live.
- **Andrew Morgan** — Analytics / business performance. Pitch deck author 2023, ongoing connection audits and revenue reporting.
- **Will Carter** — Onboarding lead 2023–2024. Less central post-Go-Live.
- **Liam Cordelle** — Crypto exchange integration lead 2025+. Wrote SOWs.
- **Isaac Dann** — Crypto pricing/normalisation lead 2025+. tXAU and Wintermute work.

## Recent issues

> [resolved] 2026-06-15 — Marianna: "allow top up = no" on exec rules reverts to yes; Rory confirmed intended for internalise rules
> Marianna flagged that selecting "allow top up: no" on execution rules in the Crypto env reverts back to yes. Rory investigated and confirmed this is intended behaviour for any execution rule where the execution style is set to internalise. Marianna accepted the explanation ("doesnt matter for internalised trades"). [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781522780871919)

> [open] 2026-06-15 — Echo Spread time zone plot broken for main session; Marianna flagged, Shyam investigating
> Marianna raised in `mahi-pepperstone-vnd` that the time zone spread plot in Echo Spread has been broken for the main session "for a while". Shyam replied he will look into it. No timeline yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781506074069289)

> [open] 2026-06-11 — Reece querying XAUUSD trades at max spread (150 cents); follow-on S3 bid/ask question unanswered
> Reece asked Mahi to pull all client trades executed while XAUUSD spreads were at max (150 cents), focusing on Friday 5 June (NFP day). Rory delivered a CSV by 16:32 UTC. Reece confirmed receipt then asked whether Mahi posts a bid/ask-at-execution table to S3 for self-querying — no reply yet in the thread. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781189767821629)

> [open] 2026-06-10 — FX A book XAUUSD losses ~$100k overnight; CPs 410114170 and 1289999 brokered; hedger config tightened
> Daria flagged FX A book down ~$35k at 23:16 BST on 2026-06-10 after 6 hours of drops from CP 410114170 (large 5000oz XAUUSD internalised orders — no LR active, flow going offside within 30s). By 04:49 BST 2026-06-11 Daria had mapped 7 individual drops totalling ~$100k (16:30 -$10.3k, 17:50 -$12.6k, 18:30 -$11k, 19:45 -$9k, 22:15 -$9k, 23:20 -$25k, 01:30 -$22k). CP 1289999 contributed to the 17:50 and 23:20 drops (8×300oz rapid scalp trades, buying open then closing a minute later with XAUUSD ~$5 higher). Root cause: XAUUSD internalised volume hit 1bn this week vs historic ~200mn — hedger calibrated for softer flow; INVAST averaging $156/M spread on hybrid fills; spread paid on the session ($71k) roughly matched spread received ($68k), so reval is the primary driver. Mitigations applied by Daria: (1) new Large Order + Fast Hedge execution rule with 30s time limit (was 60s), greedy orders; (2) CP 1289999 switched to brokered at 00:20 BST; (3) CP 410114170 added to temp broker rule at 02:24 BST. Pepperstone (Ruby) confirmed XAUUSD taken out of the equation from their side — FX still internalised. Daria planning call with Stephen tomorrow on XAUUSD spreads and LP count (only two hedging venues currently constraining hedger). Classification review of 1289999 flagged as needed. Both CPs under Pepperstone internal review. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1781129797578049) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781133654612349) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1781135290987619)

> [open] 2026-06-04 — BTCAUD / crypto AUD crosses ~$300 off vs external exchanges; Australian crypto premium suspected
> Stephen Hendrie flagged consistent pattern of OKX, Kraken, and BTCMarkets all showing materially higher BTCAUD than Mahi/Pepperstone — "constant arb on", clients noticed and were buying BTC then withdrawing to those exchanges. Daria confirmed Mahi's triangulated AUD rate is in line with B2C2 (AUDUSD spot-on vs FX env). Lee (internal) noted drift feels like spot vs perp contamination. Research (2026-06-05): Daria suspects an Australian crypto market premium (similar to Kimchi premium in Korea) — Echo data shows Pepper XBTAUD clients net-sold 4.92m USD equivalent vs bought only 626k USD over ~6 weeks, consistent with systematic arb. Kraken AUDUSD feed added to Crypto LDN env for reference; implied AUDUSD from Kraken rate is below FX-env AUDUSD by ~$15-20 (need $40-50 to fully close the gap). OKX XBTAUD also added (2026-06-07): Kraken and OKX periodically cross, suggesting inter-exchange arb. Daria's current thinking: AU premium is real and driven by barriers to closing it — not a Mahi pricing error. Daria proposing to proxy Kraken + OKX to NY and test pegging to them via placement profile in UAT; UAT testing scheduled next day. Also considering arb protection (opposite-side) at model level to reduce arb without moving mid away from Pepper's hedging venues. Daria: "needs a discussion with Pepperstone about where they want the price to sit." Will Carter and Kate Stagg tagged for input. Once Kraken integration (SOW #3) is live, Kraken becomes a hedging venue which should help. Unresolved. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780533895254089) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780550381630349) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780868965536179) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780872574615119)

> [resolved] 2026-06-03 — Arb CP 1042650 limit order rejections (continuity pool bid didn't reach limit)
> Reece queried a series of rejections on limit orders for CP 1042650. Rory confirmed analysis was correct: CP is classified as an arbitrageur, so limit orders are force-internalised on the continuity pool with markup — if the continuity pool bid doesn't reach the client's limit price the order cancels off-market. Reece asked if there's a way to fill at a worse price anyway; Rory confirmed no (can't fill a limit order at a price worse than the client submitted). [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780494472104379)

> [open] 2026-06-01 — Quantum Queen (QQ) EA comment-masking; signal-based detection requested
> Stephen flagged that QQ (a Gold EA previously banned by Pepperstone for sharp yield decay / ~70% win rate) can now bypass the comment-based reject by masking the comment field. Stephen wants to permit a small number of accounts to run QQ openly to generate a clean reference signal, then build a detection mechanism that recognises QQ by how it actually trades and adjusts pricing when it triggers — catching masked flow. Sam Hewitt escalated internally to assess feasibility and resourcing. No Mahi response yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780278118805469) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780278550368929)

> [open] 2026-05-29 — XAUUSD execution quality: OZ order 1124202715 filled at depth price vs TOB (arbitrageur classification)
> Mariapaz Bobadilla (Pepperstone OZ) flagged order 1124202715: XAUUSD SELL 100oz at 2026-05-28 10:26:24 UTC filled at 4,397.03 instead of TOB bid 4,397.72 (0.69 point worse), despite 100oz being available at TOB. Cameron Hughes confirmed the tag executed on the skew-free pool price with markup because the account is classified as an arbitrageur. No remediation discussed in-thread; explanation given to client. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780079346359669)

> [resolved] 2026-05-25/26 — XBT arb classification lag + false rehabilitations: CP 1350468 caught too late; goodCheck tightened
> Initial report (2026-05-22): CPs 1350472/1350482 arbing XBTUSD not caught in time; backgroundJobs cap bumped to 10k crypto/35k FX (was 1k). 2026-05-25: Gabriel flagged CP 1350468 had traded 7–8m BTC volume with yield -39.75 USD/M, only 1.5% routed to Dynamic Arbitrageurs. Shyam diagnosed root cause: CP was repeatedly being rehabilitated after arb classification — goodCheck was too loose, causing it to oscillate between Dynamic Arb and Catch-All. Shyam proposed tightening goodCheck (analysis window 1d→7d, minYields0ms $5/M→$50/M). Gabriel approved; Shyam implemented changes 2026-05-26 03:46 BST. Real-time arb detection still in dev for a future release. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779466071252189) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779724276226539) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779763599444849)

> [open] 2026-05-20 — Order 012dve37wwfin slippage under Dynamic Arbitrageurs; investigation ongoing
> Reece flagged order 012dve37wwfin appeared to slip more than the channel should allow. Rory confirmed the order executed under the Dynamic Arbitrageurs execution profile and is still investigating whether the fill price was materially worse than the continuity pool price at the time. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779269797499599)

> [open] 2026-05-19 — MK/Reece external classifier: automated S3 upload feature requested; Kraken SOW prioritisation tension
> MK and Reece have built their own counterparty classifier (incorporating upstream data Mahi can't see — fingerprinting, IPs, deposit patterns) after being unable to configure Mahi's classifier for persistent-yield AND logic. They're requesting an automated mechanism to push the resulting CP lists into Compass (proposed: Mahi polls an S3 bucket on a schedule). Andrew Morgan confirmed similar functionality was built for Zenfinex (unused). Liam to raise a Jira; Andrew recommends a meeting to signpost upcoming Mahi classification improvements (arb check skew profiles). Separately: MK wanted to prioritise this over the Kraken SOW #3 integration — Andrew pushed back, noting the SOW is contracted work and Tom/Tamas sign-off should be confirmed before swapping priority. Kraken integration stays current. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919)

> [resolved] 2026-05-18 — propTrader simultaneous NY+LDN restart causing thin liquidity spikes; LDN reboot time adjusted
> Stephen flagged that the "start in off state" config causes simultaneous downtime on both primary (NY) and backup (LDN) propTrader during weekend reboots, leaving only very thin residual liquidity. Daria confirmed NY reboot is 15:25 NY Sunday, LDN was 16:25 — only ~30 min window. Agreed: LDN reboot pushed to 17:25 NY Sunday to widen the coverage window. Nathan updated LDN crypto trading and admin server schedules and adjusted FIX connection start/end times accordingly. Diego flagged a potential conflict with existing Pepper FIX config (currently set to start 16:59); Diego confirmed internally and applied changes to both NY and LDN FIX connections by 2026-05-21. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779075264717449)

> [resolved] 2026-05-15 — XAG InvNY1 hedger off again after weekend restart
> Stephen flagged XAGUSD InvNY1 was off after restarts again (recurring; see 2026-05-06 entry). Daria switched it back on and noted she'll also review the notifications for this hedger. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778808580296939)

> [open] 2026-05-11 — USTUSD/XBTAUD hedger clip size; TOB refresh quantity extended to all pairs
> Stephen flagged that during a ~$500k AUD UST trade (382k units at 1.38), hedgers kept retrying B2C2 despite insufficient-balance errors rather than switching to Crossover/LMAX sooner, leaving the position partially exposed. Marianna clarified the LP wasn't deprioritised fast enough. Daria adjusted hedger config (further restricting B2C2, reordered rules so backstop can fire), increased liquidity layers; Stephen raised TOB to 10k UST. Separately, fills were slow (250 UST parcels) because only the first two layers were inside the client's limit price — Stephen gathering client feedback on acceptable fill timeframe. 2026-05-18: second large UST batch; clips upgraded to 1000 UST (was 250) but still too slow — Stephen requesting 10k–20k clip sizes. 2026-05-19: Daria set TOB layer to refresh full 10k every 500ms; Stephen confirmed. 2026-05-26: Ruby flagged the same fill-clip issue on XBTAUD (Modulus fill qty ranging 0.002–0.09 vs 0.2 TOB); Daria confirmed she already increased refresh quantity for all pairs after the USDT change — awaiting live confirmation on XBTAUD. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778489962714849) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778536863658599) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778560468492269) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779086987830109)

> [resolved] 2026-05-11 — Inventory hedger failed to auto-start after weekend restart
> MK reported that the inventory hedger (CFD desk) did not come up automatically after the weekend restarts. Kate Stagg added config to ensure auto-start and bounced systemStateMonitor to pick up the alerting config for expected on/off status. MK confirmed resolved. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778506644097019)

> [resolved] 2026-05-07 — XETUSD arbitrageur limit order rejections (continuity pool markup)
> Reece flagged high rejection volume on XETUSD from accounts 1353145/1353144/1353142 in mahi-pepperstone-notifications. Orders were being cancelled before eventually executing once price moved enough. Rory investigated: these accounts are labelled as arbitrageurs — their limit orders are force-internalised on the continuity pool with markup, but the resulting fill would breach the client's limit price, so orders cancel until the market price falls to the limit. Root cause identified; no config change noted yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778168234906839) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778172460768509)

> [resolved] 2026-05-06 — XAGUSD Inventory hedger go-live on CFD desk (NYC)
> Silver positions moved to Inventory hedger at ~10:07 UTC; hedgers restarted and live by 12:01 UTC. Pre-go-live: NOP config for Inventory book set in `risk.nop.perMarket` (reviewed by Kate via DM); VaR/P&L alert thresholds added to `multiTenant.compassTenantProfiles`; Kate bounced `systemStateMonitor` to pick up new thresholds (internal-pepperstone). Post-live: Stephen confirmed no A-book trades since rollover (2026-05-05 23:49:55 UTC) — expected. B-Book sharp was routing to `B_CLIENTS_NYC`; Stephen asked for same treatment as other B-Book (fill client, shift risk to Inventory) — Sam added config. B_BOOK_RAZOR stays in B-house on XAG only. Ruby moved hedges from Manual hedging NYC to Inventory hedging NY creating P&L/VaR noise; Daria adjusted positions. Resolved. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778065316604209) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778116381328159) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778118688509249) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1778071203112049)

> [open] 2026-05-06 — custom2 classification not triggering as expected; persistent-yield AND logic requested
> Reece asked to clear the `analytics.counterpartyClassification.B Book.custom2.badCheck` global list (193 entries); Rory cleared it. After refresh, Reece observed that CP 51397366 is not landing in custom2 despite what appear to be negative yields at 5s. Shyam (internal) reviewed: custom2 is configured as OR across horizons (5s/10s/30s/60s/2m/4m), not AND — but the aggregated yield profile for this CP shows no negative horizons, so classification seems correct yet Reece expected otherwise. Shyam flagged for further investigation. 2026-05-19: MK clarified the missing functionality is "persistent yield" — classify only if yield decay is offside at 30s AND remains offside at 4 mins (all conditions true). Mahi's classifier currently uses OR logic. MK/Reece have built their own external classifier and want an automated S3-based upload mechanism to push custom CP lists into Compass (see Notable topics). [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777984346581039) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778038180841259) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1778043575578009) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778047876914949) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779146841798919)

> [resolved] 2026-05-05 — Crossover enabled on spot hedging; NOP cap config reviewed
> Stephen requested Crossover LP be added to spot hedging; Daria enabled it same night. Stephen also asked for a NOP cap review — Daria confirmed the per-instrument and per-market NOP config looks reasonable. Stephen confirmed satisfied. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778020198535509)

> [resolved] 2026-05-04 — XAU/USDTHB/XAG indicative alerts (brief, investigated OK, Zendesk 22906)
> Stephen flagged indicative alerts on XAU, USDTHB, XAG at 03:42 UTC. Daria confirmed all processes and pricing looking okay by 04:34 UTC; raised Zendesk ticket 22906 for dev review. Stephen confirmed no ongoing issue by 04:47 UTC. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777862549479679)

> [watching] 2026-05-04 — XBT sanity-check params loosened; PSCN signal lag noted on large price move
> Isaac loosened sanity check params on XBTUSD to prevent indicative mid during large price moves where Compass tries to skew more aggressively. Separately noted that the crypto signal was substantially slower than primary LP (PSCN) over a recent XBT price move; PSCN direction volume would have improved P&L further. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1777861675208069)

> [open] 2026-04-30 — XETUSD B2C2 reject "buy price received is lower than our offer price" (spot crypto)
> Ruby flagged a B2C2 reject on XETUSD/ETHUSD.SPOT 02:46:09 UTC; FIX tag 58 = "Buy price received is lower than our offer price" (8002=504). Isaac digging — Compass TOB shows we were sending limits at B2C2's offer price. May need B2C2 query. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777527397662369)

> [open] 2026-04-30 — Reece: custom1 classification 0 min-dollars-per-million semantics + SHARP routing request
> Reece asked whether the 0 Minimum dollars per million in `analytics.counterpartyClassification.B Book.custom1.badCheck` is inception-only or tied to the 500Ms check now in place; Rory looking. 2026-05-04: Reece separately requested the `custom1` badCheck be set up and routed to the SHARP channel (NY BBook) — no reply yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777543336242789) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777895550879849)

> [open] 2026-04-28 — GBPNZD indicative for 1h at NY roll (WSS threshold)
> 20:58:59–22:00:00 UTC indicative on GBPNZD due to wide-spread suppression hitting threshold 0.00150 with mode=indicative; Pepperstone (Mariapaz/Diego) flagged as non-critical but avoidable. Nathan offered to widen the threshold or switch mode to cap during roll. Stephen asked Reece to review NZD crosses WSS settings. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777413142731729)

> [resolved] 2026-04-29 — XLCUSD B2C2 hedge rejects (price increment mismatch)
> Marianna flagged a slew of crypto-spot hedge rejects on XLCUSD with invalid increment. Rory: hedger generating limits at 3dp (e.g. 56.255), B2C2 LDN requires 2dp; pre-flight validator catches it internally. Added priceFormatPipRelative override to round XLCUSD to 2dp on B2C2 LDN+NY connections; EOD restart scheduled for fixOrders3/B2C2 and fixMD3/B2C2. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777474226517709)

> [resolved] 2026-04-29 — Inventory XAG Tapaas A/B reporting — tag 1 prefix solution
> Daria's call: only the new inventory hedgers needed the change. Set up round-robin tag strategy on the inventory hybrids with B-HEDGING and B-HEDGING-LDN trading accounts. MK testing; no dev change required. Supersedes the 2026-04-22 [open] entry. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1777447938640189)

> [open] 2026-04-27 — Cpty 2075077 not routed to Dynamic Arbitrageurs (root cause: fillAtWssPrice override); fix dev'd, deployment pending
> Reece's 6-Apr 22:00 UTC XAGUSD fill at 72.55 instead of 73.246: at 22:03:39.307 an LP bid collapse caused B_BOOK to publish a WSS-clamped bid=72.25/offer=72.55; 65ms later the SELL filled at exactly 72.55 — `fillAtWssPrice` was overriding the continuity-pool execution for Dynamic Arbitrageurs. WSS overrides continuity workflow when fired. Brokered workflow unaffected (only internalised orders). 2026-05-13: Daria confirmed dev have made a change to exclude forcibly internalised orders from `fillAtWssPrice` logic; proposed deploying to FX and Metals env during metal close the following morning using LDN/NY failover. Reece accepted, pending ARB-client-path update. 2026-05-14: FX env deploy hit an issue and was rolled back; LDN failover kept trading live. Daria expected the fix to land early next week (w/c 2026-05-18) — no confirmation in this window. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777305102439059) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778708983110969) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778797764931869)

> [open] 2026-04-24 — YTD list of counterparties removed from `reference.lists.counterparty.custom`
> Reece asked for a full YTD removal list beyond what Audit History surfaces; Kate investigating. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777024868051039)

> [open] 2026-04-21 — tXAUUSD post-normalisation-persistence review
> Weekend review: XAUT mids cluster better than PaxG (Wintermute drifts from B2C2/HRP). Isaac proposes dual-rate model — a 24/7 normalised rate (all XAUT+PAXG sources, single basis) included in tXAUUSD mid-formation during the week, with Primary tracking B2C2+HRP PAXG blend for XAU-close→XAU-open tracking. Beta prices ~10s above gold open at 7s into open, resolves quickly. Supersedes prior `[open] 2026-04-17` tXAUUSD entry. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1776743136995659)

> [open] 2026-04-14 — XAGUSD allocation blocked by minimum-lag qty mismatch
> dynamicOrderSpeeds config has XAGUSD minimum-lag normal-qty 0.5 vs normal-qty 5000, producing a 2500 minimum that blocks allocation. Thread active.

> [open] 2026-04-01 — Proposal: move crypto maintenance/reboots to weekdays
> Weekend volumes ≥ weekday; weekend reboots left traders off-state. Awaiting Liam + Pepper confirmation.

> [resolved] 2026-04-13 — Sebastian Andrews Compass access revoked (compromised device)
> Suspended same day by Rory King.

> [resolved] 2026-04-13 — Arb/XAUUSD crash ~11:02 UTC (PagerDuty Q1MAQYLK2ESYP8)

> [watching] 2026-04-10 — USDILS toxic flow (acct 51331195), NY first-hour pattern (cf. prior NZD/CHF)

> [resolved] 2026-03-24 — XAUUSD non-execution 11:00–11:02 UTC
> LP pricing flapping through sanity checks; Mahi pricing indicative during the period.

## Notable topics

- 2026-04-28 — Pepper exchange release planned 22:00 SGT; propTraderModulusUAT enabled in NY to catch issues pre-prod. Daria flagged a missed-fill on partial-fill-around-logout for monitoring. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1777361423971719)
- 2026-04-28 — Crypto cancel-reject loop on orders 012dzkfuvfl / 012dzkfupe6 — Pepper-side restart causing Failure_General rejects; not genuine, Daria switched it off. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1777364442933499)
- 2026-04-27 — Isaac flagged Pepper CFD signal process needs a subset instrument list (proposed "CFD-Majors"/"CFD-Signals": DOW, SPX, NDX, G30, CL1, CO1) — full instrument list too big; needs feedback on expected volumes. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1777328246477439)
- 2026-04-24 — Compass release weekend 04-25/26: performance, stability, UI improvements (Leo). [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777043833936419)
- 2026-04-22 — XRPAUD live on Pepperstone Crypto Exchange. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1776826778419749)
- 2026-04-23 — CFD NY IPs posted (trading-1 `192.81.111.207`, admin `192.81.111.240`); Nathan chasing LP handover ETA with Gordon/Martyna. Hardware updates done over weekend, handover imminent per Gordon. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1776904666370719)
- 2026-04-21 — Argamon want Tokyo JPY crypto crosses too (Lee bumping existing request). [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1776735210458109)
- Pepperstone CFD rollout — new desk being stood up. LDN servers in Mahi setup (IPs exchanged 2026-04-08/15). NY IPs now shared (see above). Hedgers for inventory-risk model; awaiting LP connection data + instrument specs from Pepper AU team.
- 2026-05-07 — Tom building an XAG position reconciliation script; requested access to INV_CLIENT_RISK_TRANSFER (DISTRIBUTION_NYC/LDN) and INV_HEDGING_WASHBOOK (NY/LDN) trade position tables, and asked whether a Compass API or S3 access exists. Daria added the parties for position persistence (INV_BOOK_NET + INV_HEDGING included) and confirmed Pulse access covers positions + tradepositions tables. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778158035567039)
- 2026-05-05 — LMAX Crypto CFD price/qty increment changes going live Sunday 2026-05-10; Stephen shared an xlsx with the new increments in `mahi-pepperstone-vnd`. Isaac acknowledged — will review and adjust Mahi config if needed; Stephen to confirm which symbols need published-pricing digit changes. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777941326564039)
- Pepperstone Crypto Exchange (pcrypto.com) — soft-launched 2026-03-Q1; rolling BNB/TRX/XRP-AUD on the exchange side. See Guru card T8xkG7nc.
- 2026-05-11 — Kraken SOW signed on Pepperstone's side; Nicola Perikhanyan handling GTC coordination. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1778489350508919)
- 2026-05-11 — Ruby Wang (Pepper) requested bulk update of 116 accounts to B-sharp execution profile; Nathan Burch applied, accidentally reverted, then re-applied. Resolved same session. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778473107934599)
- 2026-05-11 — MTM sim for Reece's YP check: initial run (sim #548) produced 41tn USD notional vs expected ~450m due to lot conversion issue. Re-ran as sim #553 with no lot conversion; Rory delivered Echo Yield Profiles link to Reece. Zendesk 22953. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1778472938471219)
- 2026-05-12/2026-06-05 — CFD NY/LDN OZ connectivity: LDN xconnect (10.74.101.142) set up by Beeks 2026-05-08; LDN taker connectivity working for IG (1 of 6 LPs) as of 2026-05-27; 5 LPs still pending OZ activation. NYC server provisioning had Beeks supply-chain delay. **2026-06-04/05: NYC FIX credentials now exchanged** — Isaac posted A_CLIENTS + B_CLIENTS orders/marketdata creds for NY OZ Hub→Compass NY (host 10.72.100.115, ports 9011/9010); LDN→NYC failover creds also shared (host 149.5.84.246). Diego confirmed and shared additional sessions via email. Instrument clarification: HRP Goldi taker connections (Crypto + FX envs) are for perps only; Jump Direct + LMAX 2 for cash indices. Isaac: if firewall change (10AM Melbourne) + NYC/LDN enabled today, pricing set up for review + test trades possible by EOD. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778566455574649) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779783268258179) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779855313496039) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780610527787349)
- 2026-05-14 — LMAX Digital crypto maintenance window moving from Friday evenings to Saturday mornings effective 2026-05-23 (first window: Sat 23 May 08:00–09:00 UTC). Daria confirmed no config changes needed on Mahi's side; multi-venue setup handles coverage. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778757837376979)
- 2026-05-14 — Traders restarted (rolling, region by region) to fix counterparty field capture on trades; Modulus counterparty tag fix deployed (Zendesk 22879). [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778796282049649)
- 2026-05-18 — Kraken SOW #3 FIX integration underway. Liam requested UAT test credentials; Pepperstone stipulated Kraken should not know Mahi is on the other side (Tom's ask). Reece registering a personal UAT account to provide credentials. As of 2026-05-21, Kraken UAT environment having issues — credentials not yet delivered. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779111036533119)
- 2026-05-19 — Liam flagged Pepperstone don't want Kraken to know Mahi is the counterparty in the SOW #3 FIX integration. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779188905427249)
- 2026-05-20 — USDC/USD (Compass symbol USCUSD) pricing added to OZ CFD spot feed (both LDN and NY B2C2 feeds); for conversion use only. Diego to subscribe after EOW. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779246233079129)
- 2026-05-21 — Weekly CFD crypto PnL review: MK queried low ROS (90k vs 152.2k spread PnL). Isaac identified abnormal flow yield decay to ~95k at 120 mins. MK and Isaac found culprits; one FI arbitrageur account racked up 15k trades before being caught by ARB classifier — now classified. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779329721629439) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779330345418129)
- 2026-05-22 — MK requested JMX IP whitelist for office IP 104.28.181.137; Nathan routing to Beeks (est. 10–30 min per Isaac). No confirmation yet in-thread. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779422554164899)
- 2026-05-22 — Tom requested 4 IPs (50.16.243.246, 52.45.193.177, 54.145.122.46, 54.175.203.47) whitelisted for astro worker automations (test + prod) against Mahi DB host 192.81.110.208; Rory whitelisted same day, Tom confirmed access. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779444503985319)
- 2026-05-22 — Isaac added `signalVariationPenalty: 4` to `flow-price-thresh` at crypto env to reduce spiky ticks on the flow signal. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779423087643319)
- 2026-05-25/26 — Perpetual contracts scoping call: Isaac catchup with MK, Stephen, Diego. Perps across three envs — Oil (CFD), Bitcoin (Crypto), Gold (FX), all 24/7 with Hyper Liquid as LP (CLOB). Open question on passive hedging via OZ vs direct connectivity. Failover/continuity design needed (Crypto env proposed as backup for FX/CFD restarts). NYC CFD servers still pending. S3/classifications feature flagged for MK — Isaac noted Liam is owner but is away; flagged to analytics subteam. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779758966828729)
- 2026-05-26 — MK requested Crypto JMX IP whitelisted (follow-up to 2026-05-22 FX JMX whitelist; no IP specified yet in thread). Daria acknowledged. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779752427539119)
- 2026-05-26 — MK requested decommission of B_BOOK_RAZOR and A_BOOK_RAZOR channels — not proceeding with the dual split. No reply yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779754125791069)
- 2026-05-26 — propTraderCrypto/propTraderCryptoBackup books briefly off (SPOT_CLIENTS_NYC and SPOT_CLIENTS_LDN). Maten flagged; Reece turned them back on via GUI at 14:30/14:31 UTC from Pepper side. Self-resolved. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779805107028709)
- 2026-05-26/27 — XBTUSD skew adjusted by Isaac: flow-price-thresh now secondary to IFMS (reduced benchmark contribution, active primarily over large price moves). Effect: more consistent skew in steady periods, stronger skew over large moves. Skew at $90/M post-change vs typical $45–60/M. 2026-05-29: Isaac confirmed still at $90/M; month was $47.97/M pre-change. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1779839829423179) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780027977213949)
- 2026-05-27 — MK requested USD/M markup cap raised from $500 to $1500/side for internal/brokering channels (context: perp exchange fees need baking in). Nathan passed to dev team. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779853365951359)
- 2026-05-27 — MK asked whether ROS stat can populate for the Inv book (without SI structure). Daria confirmed it will start populating shortly (spread-only this week so ROS inflated; normalises next week). [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779840671842489)
- 2026-05-27 — Crypto pricers restarted for a BMSL config change in PAXGUSD. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779869787021749)
- 2026-05-27 — Marianna asked Mahi to confirm HRP_PROXY is included in hedging for HYPEUSD on the SI hedgers. Rory confirmed HRP_PROXY exists in execution markets for both hybridHedgerSINYC1 and hybridHedgerSITotalNYC1 in the crypto env. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1779870724253409)
- 2026-05-29 — Perps go-live planned for next week: Marianna confirmed going live with XAUUSDC-PERP, BRENTOIL-USDC-PERP, WTOIL-USDC-PERP, BTC-USDC-PERP (Compass naming: XAUUSD-PERP, CL1USD-PERP, CO1USD-PERP, XBTUSD-PERP). Isaac set up Binance Futures pricing feed in LDN, proxied to NYC, awaiting HyperLiquid credentials (taker ready post-weekend). Feed available only via OZ NY HUB — Isaac confirmed workable via normalisation/proxying. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780015264487769) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780027351727259)
- 2026-05-29 — Shyam flagged Pepperstone B · NZDUSD FI PnL loss of -$2,114: price skewed down during large influx of House Sells (~21:09–21:11 UTC 2026-05-28). Internal monitoring note; no action visible in-thread. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780022042490849)
- 2026-05-29 — Marianna asked if Mahi has a USDH/USD rate to proxy; Isaac replied no. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780026918524119)
- 2026-05-29 — Sam Hewitt (NZ) advisory: Monday 1 June is a NZ bank holiday; emergency support only, reduced Slack monitoring. Contact support@mahimarkets.com or LN +44 203 397 1985 / NZ +64(3) 2880079. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780029525109529)
- 2026-06-03 — Isaac requested Diego get OZ to whitelist source IP `10.72.100.115` for inbound TCP ports 20063-20074 on the NY hub. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780533390829199)
- 2026-06-03 — Isaac asked Pepperstone whether HyperLiquid pricing and order credentials are ready for perps go-live; Diego checking. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780520842307509)
- 2026-06-04 — Isaac did a full stop-start on the London CFD env to pick up WAN config changes. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780540158588719)
- 2026-06-04 — Marianna asked for update on S3 bucket access progress (relates to the external classifier S3 upload feature request, see open issue 2026-05-19); Rory replied he'll check internally and revert. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780578395131549)
- 2026-06-04 — Leo Borsi deployed a Dash update for both pepperstone and pepperstone-crypto envs. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780581350155219)
- 2026-06-08 — Kraken SOW #3 UAT credentials still not delivered: Liam confirmed integration is blocked because Reece (Pepper) still hasn't provided test credentials. Liam chased last week with no response. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780905943418209)
- 2026-06-08 — XTX removed from referencePriceMarketSelectors (FX env): Marianna flagged XTX as a skew-sensitive feed that should only be used for hedging, not as a price reference. Rory removed all references and did rolling pricer restart same afternoon; confirmed complete. XTX was already absent from crypto pricing. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780912865095549)
- 2026-06-08 — New crypto cross pairs requested: HYPE/BTC, HYPE/ETH, XLM/BTC, XLM/ETH — triangulated crosses (no direct feed), 1x widening factor, SI 1 hour. Kate Stagg acknowledged; no ETA yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780916305071409)
- 2026-06-08 — Stephen queried whether XBTUSD in Crypto env should reference spot liquidity rather than CFD providers (currently referencing CFD referencePriceMarketSelectors). No Mahi reply yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780909069182079)
- 2026-06-07 — Daria asked internally for a rough ETA on the Kraken SOW #3 integration, framed as "considering options for the BTCAUD/AUD crosses pricing issue" — i.e. Kraken as a hedging venue is part of the resolution path. No reply yet. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1780869999127439)
- 2026-06-04/05 — CFD NYC FIX credentials exchanged (Isaac → Diego): A_CLIENTS + B_CLIENTS orders/marketdata on host 10.72.100.115 (NYC) and 149.5.84.246 (LDN→NYC failover). Instrument scope clarified: HRP Goldi connections for perps (both Crypto + FX envs); Jump Direct + LMAX 2 for cash indices. Isaac expects pricing available for review and possible test trades by EOD 2026-06-05 if Melbourne firewall change completes on schedule. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1780610527787349)
- 2026-06-09 — CFD go-live blockers status (Nathan): LDN taker connections logged in but no market data coming down; NYC taker connections not yet logged in (whitelisting of `10.72.100.115` ports 20063-20074 still pending on Pepper OZ side); LDN failover (LDN→NYC) maker connection not logged in — Beeks escalation may be needed. Nathan asked Pepperstone for updates on all three. No response in-window. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781068129644939)
- 2026-06-09/10 — Sam Hewitt requested a timing window from Pepperstone to deploy FX and Crypto environments (staggered by region, no trading interruption). Deploy picks up: new crypto crosses, WSS changes, raising markup limits. Awaiting Pepperstone confirmation of suitable window. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781048026643779)
- 2026-06-09/10 — Isaac posted XAUUSD signal update (QQ EA context, internal): 3 fires this week. Widening model live: 5 pips each side for 5 seconds post-signal. Sell-side (BID) predictivity 558 $/M at 5s, 12× baseline, still 11× at 10s. Buy side (OFFER) predictive early (5× at 1s) then fades and mean-reverts negative by 1m. Flow uplift: 21× normal at 1s. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781051878067659)
- 2026-06-09 — Internal: Isaac asking whether there is an implementation plan for the S3 classifier upload feature (MK's request, see open issue 2026-05-19) that can be shared as an update with Pepperstone. No reply in-window. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1781041799830899)
- 2026-06-11/12 — FX deploy completed (NY then LDN). Sam Hewitt kicked off NY at ~23:15 BST 2026-06-11, LDN complete by 00:01 BST 2026-06-12. Picks up new crypto crosses, WSS changes, markup limit raise. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781211942247609)
- 2026-06-12 — CFD LP feed clarifications (Daria, pre-go-live): (1) two Jump + LMAX feeds per region believed to be a mistake in the OZ request — Pepperstone checking; (2) IG LDN connection should be used in LDN env (IG prices from London, not NY). [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781237298527569) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781237631697269)
- 2026-06-12/14 — GldI perp pricing gap resolved: Pepperstone flagged no GldI price for perps in Compass (tried switching Gold subscription to Diego's name, bounced connection, no joy — asked whether OZ or Compass side). Isaac fixed perp market mapping and added remaining instruments by 2026-06-14 23:45 BST. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781258601251199) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781477146818009)
- 2026-06-15 — CFD instrument volume data exchanged for signal tuning: Daria requested approximate daily/weekly volumes per instrument for CFD env; Pepperstone provided an xlsx (Apr–Jun monthly volumes). Daria confirmed useful and requested a CSV of trades for ~2 weeks for the top 10 instruments to tune signals ahead of go-live. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781495714603579)
- 2026-06-10/11 — Crypto deploy completed (NYC then LDN); FX deploy deferred to tomorrow during Roll. Sam Hewitt executed Crypto NYC starting ~23:54 BST, LDN by 00:52 BST. FX deploy held back due to active incident (XAUUSD losses). [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781128821285299)
- 2026-06-09/10 — Internal: Isaac posted Q1 2026 Crypto spread stats (Jan–Mar, LDN+NYC): XBTUSD $14.56B vol 93.6% internalisation, spread earned +$265.63/M; XETUSD $1.25B 70.3% internalisation +$689.93/M. Notes spreads on everything bar BTC/ETH are very high; proposes spread tightening as a growth lever (more flow, maintain ROS via ROI + PSM). Flagged as bookmarked, not high priority given other SOWs. Daria added a note to prioritise a XAUUSD spread review — current spread formation mostly BMSL (base spread 0), Pepperstone has previously raised this on a quarterly. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1781047518323269) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1781048171828259)
- 2026-06-15 — Marianna triggered crypto NYC pricer restart (BMSL change, PEPPERSTONE-CRYPTO NYC), then a second restart for mwms; both acknowledged by Rory. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781532805604079)
- 2026-06-15 — Isaac notified team of rolling distribution gateway restart in crypto env to pick up Perp instruments into distribution (short failover between envs); Pepperstone +1'd. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781561780975949)
- 2026-06-16 — Daria asked whether LP1 is basis for pricing in CFD env (e.g. Velocity for WS30, Invast for SPX) and what LP2 is for; Pepperstone confirmed LP1 = primary pricing/normalisation peg, LP2 = backup if LP1 fails. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1781587712666549)
