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
last_catchup: 2026-05-14T07:32:03Z
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

> [open] 2026-05-11 — USTUSD hedger B2C2 deprioritisation lag on large order; fill speed concern
> Stephen flagged that during a ~$500k AUD UST trade (382k units at 1.38), hedgers kept retrying B2C2 despite insufficient-balance errors rather than switching to Crossover/LMAX sooner, leaving the position partially exposed. Marianna clarified the LP wasn't deprioritised fast enough. Daria adjusted hedger config (further restricting B2C2, reordered rules so backstop can fire), increased liquidity layers; Stephen raised TOB to 10k UST. Separately, fills were slow (250 UST parcels) because only the first two layers were inside the client's limit price — Stephen gathering client feedback on acceptable fill timeframe. Daria still simulating the config change. NOP alignment between Compass and B2C2 limits also discussed — Stephen noted treasury deposits/withdrawals make Compass NOP not reflective of underlying. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778489962714849) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778536863658599) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778560468492269)

> [resolved] 2026-05-11 — Inventory hedger failed to auto-start after weekend restart
> MK reported that the inventory hedger (CFD desk) did not come up automatically after the weekend restarts. Kate Stagg added config to ensure auto-start and bounced systemStateMonitor to pick up the alerting config for expected on/off status. MK confirmed resolved. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778506644097019)

> [resolved] 2026-05-07 — XETUSD arbitrageur limit order rejections (continuity pool markup)
> Reece flagged high rejection volume on XETUSD from accounts 1353145/1353144/1353142 in mahi-pepperstone-notifications. Orders were being cancelled before eventually executing once price moved enough. Rory investigated: these accounts are labelled as arbitrageurs — their limit orders are force-internalised on the continuity pool with markup, but the resulting fill would breach the client's limit price, so orders cancel until the market price falls to the limit. Root cause identified; no config change noted yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778168234906839) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778172460768509)

> [resolved] 2026-05-06 — XAGUSD Inventory hedger go-live on CFD desk (NYC)
> Silver positions moved to Inventory hedger at ~10:07 UTC; hedgers restarted and live by 12:01 UTC. Pre-go-live: NOP config for Inventory book set in `risk.nop.perMarket` (reviewed by Kate via DM); VaR/P&L alert thresholds added to `multiTenant.compassTenantProfiles`; Kate bounced `systemStateMonitor` to pick up new thresholds (internal-pepperstone). Post-live: Stephen confirmed no A-book trades since rollover (2026-05-05 23:49:55 UTC) — expected. B-Book sharp was routing to `B_CLIENTS_NYC`; Stephen asked for same treatment as other B-Book (fill client, shift risk to Inventory) — Sam added config. B_BOOK_RAZOR stays in B-house on XAG only. Ruby moved hedges from Manual hedging NYC to Inventory hedging NY creating P&L/VaR noise; Daria adjusted positions. Resolved. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778065316604209) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778116381328159) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778118688509249) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1778071203112049)

> [open] 2026-05-06 — custom2 classification not triggering as expected; Shyam investigating
> Reece asked to clear the `analytics.counterpartyClassification.B Book.custom2.badCheck` global list (193 entries); Rory cleared it. After refresh, Reece observed that CP 51397366 is not landing in custom2 despite what appear to be negative yields at 5s. Shyam (internal) reviewed: custom2 is configured as OR across horizons (5s/10s/30s/60s/2m/4m), not AND — but the aggregated yield profile for this CP shows no negative horizons, so classification seems correct yet Reece expected otherwise. Shyam flagged for further investigation. Reece sent a follow-up "morning team- any update on this?" at 07:11 UTC with no reply yet. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777984346581039) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778038180841259) [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1778043575578009) [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778047876914949)

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

> [resolved] 2026-04-27 — Cpty 2075077 not routed to Dynamic Arbitrageurs (root cause: fillAtWssPrice override)
> Reece's 6-Apr 22:00 UTC XAGUSD fill at 72.55 instead of 73.246: at 22:03:39.307 an LP bid collapse caused B_BOOK to publish a WSS-clamped bid=72.25/offer=72.55; 65ms later the SELL filled at exactly 72.55 — `fillAtWssPrice` was overriding the continuity-pool execution for Dynamic Arbitrageurs. WSS overrides continuity workflow when fired. Brokered workflow unaffected (only internalised orders). Discussion ongoing on whether to switch to continuity / unwind the override; Reece wants to know plan before any change as it impacts client execution. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777305102439059)

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
- 2026-05-12 — CFD NY/LDN OZ connectivity stalled: LDN xconnect (10.74.101.142) set up by Beeks 2026-05-08 but OZ still can't locate it; LDN taker/LP credentials outstanding from OZ. NY server provisioning still pending new server provision (old servers had issues). Diego pinging Daria/Isaac/Liam for ETA; Daria escalating to Liam for OZ NY ETA; LDN taker side also blocked. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1778566455574649)
