---
slug: basemarkets
refs:
  vibepulse: ../VibePulse/.claude/clients/basemarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: basemarkets
  hosts: ../MahiProduct/data/client-hosts.json          # entry: basemarkets
  wiki: null                                             # ../MahiProduct/wiki/clients/basemarkets.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Alex", role: "Base Markets — primary client contact (algo / flow)", confidence: low}
  - {name: "Kate B", role: "Base Markets — client contact (onboarding / MT4 setup queries)", confidence: low}
  - {name: "Aytugan Khafizov", role: "FastMT/Tegis — integration contact (Centroid setup, TEM config)", confidence: low}
  - {name: "Anatoly", role: "Base Markets / Tegis — sign-off contact for TEM switch", confidence: low}
last_catchup: 2026-06-12T07:12:02Z
---

## Status

- **Stage:** onboarding — blocked again as of 2026-06-09: Centroid give-up workflow broken (double-risk + MT5 zero-spread PnL issues); alternative MT4→MT5→Compass→LMAX workflow proposed by Kate Stagg; go-live target slipped further, no new date set; Compass upgraded to latest version weekend 2026-06-07/08 (Liam Cordelle).
- **Integration:** LDN trading + admin (LD5), Athena `basemarkets_ldn`, distribution via CLIENT_PRICE_LDN / CLIENT_PRICE_BETA_LDN / DISTRIBUTION_LDN / DISTRIBUTION_SYNAPSE_LDN. FIX API available; no margin / credit checking yet.
- **Relationship:** healthy — Alex (client) "super happy" with recent report; Nicola Perikhanyan owns commercial, Rory King / Kate Stagg client-facing.

## Recent issues

> [open] 2026-06-09 — Centroid give-up workflow broken; alternative MT4→MT5→Compass workflow proposed
> Kate Stagg post-call notes (2026-06-09): Centroid give-up has two showstopper issues: (1) Centroid sends zero-spread fill price to MT5 — PnL can't be tracked correctly; (2) Centroid sends one order from MT4 and one from MT5 to Compass — double execution risk. Alternative proposed: MT4 order (zero spreads) → passes to Base MT5 → STP'd to Compass → filled with spread → spread-paid fill confirmed in MT5 → client still sees zero-spread in MT4. Liam Cordelle noted a structural concern: previously Tegis P&L was against the market (STP to Scope); under the new model Base takes the other side, with Compass hedging to LMAX — mismatch risk due to internalisation and driver hedging. Kate to raise with Kate B (client); Liam signalled acceptable if there's no P&L share agreement between Tegis and Base. No resolution yet. Also discussed: separate Tegis pricing model with greater TOB quantity, aligned to LMAX (hedger) rather than Scope. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1780997666453149)

> [open] 2026-06-07 — Admin server did not come up after weekend restarts (Compass upgrade weekend)
> Liam Cordelle noted at 10:00 UTC 2026-06-07 that the admin server failed to come back up after weekend restarts. Beeks detected the issue but were awaiting Mahi permission to reboot; Liam asked Beeks to restart it. Follow-up planned: Liam to establish a procedure giving Beeks more autonomy on reboots. No resolution confirmation in channel yet. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1780822809497359)

> [open] 2026-05-28 — Centroid EURAUD TP order rejected: LIQUIDITY_VIOLATION
> Client (Tegis/Centroid) reported that a take profit order on EURAUD (2000 lots, tag 1 = "55", account BaseMarketsCentroidOrders) was rejected at 06:18 UTC 2026-05-28 with `LIQUIDITY_VIOLATION`. FIX Execution Report shows OrdStatus=4 (Cancelled), ExecType=4. Client asked for root cause investigation; no Mahi reply in channel as of run time. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779958441603849)

> [open] 2026-05-28 — C book limit order cancels: CLIENT_PRICE_LDN non-zero spread vs. 0.1 price check
> Daria Horton flagged that the new C book is seeing a significant number of order cancels. Root cause: `CLIENT_PRICE_LDN` (the internalisation market used for price checking) has non-zero spreads that are suppressed to choice by the WSS before publishing — good for client pricing, but means the 0.1 price check fires against the wider internalisation price, not the published choice price, cancelling valid limit orders as "off market". Three workarounds discussed: (1) raise the price check threshold (loses protection against genuinely off-market limit orders), (2) restrict client to market orders only (likely to breach limits), (3) switch the internalisation model itself to output choice (Daria's preferred path). No resolution or reply yet as of run time. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779931902776959)
> **2026-05-28 22:25 update:** Daria added that market orders are also filling against `CLIENT_PRICE_LDN` rather than the published price — though client is still getting the published price regardless. Daria flagged Cameron Hughes (who handled client comms on this today) via mention. No fix in place yet. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1780003555490009)

> [open] 2026-05-26 — Tegis Centroid test trades: tag 1 (tradingAccount) missing; flow misrouted to Scope A; hedger not clearing
> Client (Tegis/Centroid) hit `INVALID_ORDER FIELD_VALIDATION_ERROR {tradingAccount=MISSING_VALUE}` on FIX orders via BaseMarketsCentroidOrders session. Cameron Hughes diagnosed: Centroid wasn't sending tag 1 — Mahi needs it to route to the correct Compass trading account. Centroid team clarified they can pass the MT4 login or group as tag 1; Mahi (Cameron Hughes) confirmed any fixed value acceptable and suggested CENTROID/TEGIS_CENTROID. Test trade with tag 1 = "55" (MT4 account number) went through but initially hit LIQUIDITY_POOL_LDN (Scope A) instead of the Compass-managed Tegis book → LMAX — execution rules didn't recognise account 55. Cameron Hughes updated ERs to internalise in the Tegis book; flow then managed correctly. However the hedger failed to clear the small residual risk; Cameron Hughes asked client to close the test trade while investigating. Client closed trades ~19:00 BST 2026-05-26; client requested another test trade 06:48 UTC 2026-05-27 — Mahi not yet responded in channel as of run time. Open issues: (a) tag 1 value needs confirming for all future Tegis accounts beyond "55"; (b) hedger not clearing investigated but unresolved. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779785262352929) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779785464676889) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779860920465209)

> [resolved] 2026-05-25 — Trade routed to Scope A unexpectedly; execution rules fixed same day
> Client (anonymous guest) reported at ~09:44 UTC that a trade went through to Scope A. Daria Horton flagged to Kate Stagg at 20:15 UTC to investigate; by 20:38 UTC Daria confirmed Kate had "sorted the execution rules". No further detail in channel on which rule was misconfigured; likely related to the XAUUSD ER tightening applied the same day (max 10oz internalise). [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779702282678919) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779741510024939)

> [resolved] 2026-05-24 — BTCUSD pricing dropped after scheduled restarts (~04:45 UTC)
> Client reported BTCUSD stopped streaming on BaseMarkets MT5 from Mahi GW. Justin Young (Mahi analytics) initially flagged admin server procs down; separately noted BTCUSD feed from Scope hadn't recovered. Justin forced reconnect on the session; feed came back up same morning (~11:07 BST). [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779598899205419) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779617214773509)

> [resolved] 2026-05-25 — XAUUSD internalise execution rules tightened to max 10oz
> Daria Horton switched XAUUSD internalise ERs for both Rev share and A book to max 10oz, at Kate Stagg's request. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779681118400689)

> [open] 2026-05-06 — Tegis MT4/MT5 dual-platform: Centroid workaround adopted, MT5 drop-copy on roadmap with no ETA
> Originally: EA on MT4 requires zero-spread exact-fill; Scope MT5 handles real execution. Compass had no lever on fill price. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778162773664489) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778174905149009)
> **2026-05-11 update:** Kate Stagg proposed Tegis's Centroid as the workaround — Centroid handles MT4 zero-spread / MT5 standard-market-conditions split; Mahi receives market orders via FIX, hedges normally, Centroid translates fills to each platform. Andrew Morgan confirmed this is a valid "Compass broker workflow at a structural loss on the inbound by design" — MT4 accepts whatever limit price, Compass hedges to market, give-up feed into MT5 for real economics. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778494642.927869) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778258653.848549)
> Distribution FIX creds sent to client on 2026-05-11; infra deploying `clientDistGW1`. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778499833340869)
> Longer-term: Kate B (client) asked whether Centroid can be removed eventually — MT5 drop-copy (MTB-199, blocked since 2023 on acceptor/initiator architecture call) added to roadmap, no delivery commitment. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778517045666329) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778517127566459)
> Call with FastMT requested by client 2026-05-12 (12–2pm or after 5pm UK) to discuss Tegis setup — unanswered as of run time. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778570575730699)
> **2026-05-12 update:** Post-call recap from Aytugan (FastMT/Tegis) on 2026-05-12 — plan: Mahi creates taker FIX connection; creds passed to Centroid to create maker; Centroid bridge restart; TEM built in Centroid (MAHI1) to inherit zero spreads from Scope; dropcopy wired to Base MT5 netting account; test account on MT4 with new TEM for E2E testing; after Alex + Anatoly sign off, existing MT4 accounts switch from Scope TEM to MAHI1 TEM. Kate Stagg sent maker creds to Aytugan same day. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778587371610629) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778588623913609)
> **2026-05-15:** LMAX FIX session locked — client reported spamming incorrect password; Rory King turned off FIX connection; LMAX sent new password 2026-05-18; Rory reviewing. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778848988422949) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778849696126849)
> **2026-05-16:** Centroid restarted but Mahi maker offline — client asked Mahi to whitelist Centroid IPs (Primary: 192.109.17.181, Backup: 185.125.204.132). [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778914623299679)
> **2026-05-18:** Mahi maker now connected from Centroid side (Aytugan confirmed); Daria Horton confirmed whitelisting with Beeks; fixMD3 + fixOrders3 re-added (Rory King). [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779081321195119) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779120037227099)
> **2026-05-19:** Kate B clarified LMAX account split — Sub1 for Tegis account, Sub2 for Base flow. Kate Stagg to handle via round-robin tag management in orderServiceConfiguration. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779185342020389)
> **2026-05-18:** Kate Stagg internal note — Tegis book plan: keep existing flow (warehouse some, STP rest, no hedging) in separate book initially; view to move Tegis flow in over time except warehouse risk; also set up hedger on B Book to keep risk below 100k. Next steps: set up Tegis Book + Hedger (Compass managed book), set up hedger on B Book. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779111232980629)
> **2026-05-21:** LMAX EXPOSURE_CHECK_FAILURE on EURUSD — resolved by Mahi side; second attempt returned silent cancellation (no comment). Kate switched to market order; LMAX test trades (EURUSD + XAUUSD, buy+sell 1k/1 unit) confirmed successful both sides. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779361298941919) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779368034193409) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779368456085189)

> [resolved] 2026-05-07 — Client asking for FIX API test/sandbox instance
> Alex (Base Markets), relayed via Nicola Perikhanyan, asked whether Mahi has a test instance or sandbox for testing FIX API connectivity. Superseded by 2026-05-11 Centroid FIX credential setup — live Distribution FIX creds sent directly to client on 2026-05-11 as part of Tegis/Centroid onboarding. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1778164813309659)

> [watching] 2026-05-05 — Pre-flow readiness: cross skew + driver pair hedging workflow; Tegis book setup pending
> Will Carter flagged need to be ready for Monday (2026-05-11) — wants workflow testing to confirm skew is running on the crosses Base Markets trades, with hedging in driver pairs. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777983387923419)
> **2026-05-18 update:** Kate Stagg internal — separate Tegis Book to be set up (Compass managed), plus hedger on B Book capped at 100k risk. No completion signal in window yet.

> [open] 2026-04-29 — Client asking about direct API piping for rewritten algo
> Alex (Base Markets) is planning to rewrite their algo and asked whether they could pipe trades straight into our server (i.e. off MT4/MT5). Andrew Morgan confirmed FIX API connectivity exists, but margin and credit checking are not implemented — flagged as something he'd want to build. No reply yet to Alex. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470115067619) [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777470499867149)

> [resolved] 2026-05-12 — Rev share account 110291: partial close internalised instead of brokered to SCOPE_B
> Account 110291 opened 5 lots short, partially closed in ≤50oz increments — these hit the "internalise 50oz" execution rule rather than the REV_SHARE broker rule (which routes to SCOPE_B). Client closed remainder manually on SCOPE_B. Daria Horton confirmed cause (execution rule ordering), shifted Compass positions to rev share book to net out. Client chose to keep rule order as-is and reconsider separately. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778564784545149) [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778567380357959)

> [resolved] 2026-05-12 — MATUSD showing as indicative / no market data
> Nathan Burch queried whether MATUSD should be pricing. Kate confirmed it is not on the platform. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778547211274859)

## Notable topics

- 2026-06-10 — Infra deploying pricerVIP1/2 for new Tegis flow: Kate Stagg noted infra is adding pricerVIP1/2 processes for the Tegis flow — a forward step in getting the Tegis/Centroid integration ready for live traffic. No further detail or completion signal in window. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1781084659562139)
- 2026-06-05 — Compass upgrade applied over the weekend: Liam Cordelle notified the client channel that the system would be upgraded to the latest Compass version over the weekend (w/c 2026-06-05), with monitoring over market open for issues. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1780673119041699)
- 2026-06-05 — Fee tier under review: Nicola Perikhanyan noted volumes for Base are being monitored and asked whether growth from Tegis justifies moving up a fee tier (fees were reduced back to the intro offer due to slower-than-expected growth); Kate Stagg replied that MT4/5 teething issues mean they're not live yet, was hoping this week but now likely next week; Nicola resolved to evaluate again in July. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1780584640017199)
- 2026-06-05 — New group code requested: anonymous/guest user in #mahi-base-markets asked to add `real\USD-MU-SD-VIE-R`; Rory King confirmed "sure - we'll get that arranged". [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1780582922690779)
- 2026-06-03 — Kate Stagg restarted `clientDistGateway1`, noting only the Centroid connection is on this process and it is not live yet — confirms Tegis/Centroid integration remains in pre-live (test-only) state. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1780487432576579)
- 2026-05-29 — Sam Hewitt (Mahi NZ) notified channel that Monday 1 June is a NZ Bank Holiday; emergency support cover only; Slack not monitored normally; support email / LN/NZ phone lines available for urgent issues. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1780029447762379)
- 2026-05-21 — LMAX test trades (EURUSD + XAUUSD) confirmed successful both sides — first end-to-end LMAX validation completed. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779368456085189)
- 2026-05-18 — Centroid/Mahi maker session confirmed connected (Aytugan). [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779081321195119)
- 2026-05-13 — Client requested group codes added: real\USD-MU-SD-KAJ-X, real\USD-MU-SD-KAJ-R, real\USD-MU-SD-KAJ-S; Kate Stagg confirmed. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778666314632929)
- 2026-05-12 — Client requesting call with FastMT today (12–2pm or after 5pm UK) to discuss Tegis setup; unanswered as of run time. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1778570575730699)
- 2026-05-25 — New group code `real\USD-MU-RZ-020-X` added by Isaac Dann, confirmed mapped to B_CLIENTS book. [permalink](https://mahifx.slack.com/archives/C09D8V41JAG/p1779680278819859)
- 2026-05-24 — Justin Young (analytics) asked whether LMAX sessions are supposed to be down; Daria confirmed LMAX is still test-only (test trades run last week). [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1779612044805469)
- 2026-04-29 — Alex happy with report; Tegis onboarding underway, ~2 weeks until flow starts hitting Compass. [permalink](https://mahifx.slack.com/archives/C09D05EPCTV/p1777467956510609)
