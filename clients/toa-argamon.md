---
slug: toa-argamon
refs:
  vibepulse: ../VibePulse/.claude/clients/toa-argamon.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toa-argamon
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Tom McLean", role: "Argamon-side analyst — primary day-to-day contact in mahi-argamon-operations"}
  - {name: "Levi Ulman", role: "Argamon ops — give-up / rejection queries, Centroid migration lead"}
  - {name: "Joanna Theofanous", role: "Argamon-side ops — recurring contact in mahi-argamon-operations for alerts and client trade queries"}
  - {name: "Jonah Ink", role: "Argamon — escalation contact; involved in currency rec disputes and P&L attribution; departed Aug 2026", confidence: low}
  - {name: "Alexander Karnadi", role: "Argamon — analytics / reconciliation; participates in position rec and currency rec calls", confidence: low}
  - {name: "Elan Bension", role: "Argamon — senior contact / decision-maker; calls on insti model, LP config, retail contract renegotiation"}
  - {name: "Alex", role: "Argamon analytics — assists on Wintermute rec and crypto JPY position work (likely Alexander Karnadi)", confidence: low}
  - {name: "William", role: "Argamon ops — raised EURZAR/USDZAR LP dark event in mahi-argamon-operations 2026-05-25; surname unknown", confidence: low}
last_catchup: 2026-07-03T07:06:06Z
---

## Status

- **Stage:** live (Argamon is a client of Toa; LDN/APN1/CHI single-box setups). Contract split confirmed 2026-07-01: Mahi retains retail tenant; Toa takes B2B/Crypto/RI. Connectivity pipeline falls to Toa.
- **Integration:** NYC retail tenant primary. Centroid migration complete (from OneZero; test trades through July 2026). Reactive Markets in production — NatWest slow-consumer issue ongoing (Beeks escalation required). XTX-Algo live from 2026-07-08 (confirmed). Lucera for insti (NatWest maker session live). FSS markets decommissioned 2026-07-24. NatWest PB NOP limits set 2026-08-04. 26Degrees recurring brokering issues (stuck orders, duplicate trade IDs).
- **Relationship:** ops-heavy; multiple daily interactions. Jonah Ink departed Aug 2026. Elan considering switching off NY Insti routing around Mahi (suits both parties given Toa handles insti). Retail contract renegotiation (fixed-fee conversion) still pending.

## Recent issues

> [open] 2026-06-25 — HRP_CLIENTS_NET two PnL drop alerts (~$9k each); ~07:08 UTC; no resolution posted
> Arun (Toa ops) flagged two back-to-back PnLDropAlerts on TOA-ARG LDN HRP_CLIENTS_NET at 08:10 BST: −$8,961 over 20 minutes (06:48–07:08 UTC, raw 364,990→356,030) and −$9,018 over 8 minutes (06:59–07:07 UTC, raw 364,930→355,912). Eyes reaction only; no diagnosis or resolution in thread as of catchup. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1782371422081669)

> [resolved] 2026-06-23 — Centroid UAT IP whitelist + credentials issued for incremental MD refresh testing
> Levi (Argamon) requested 185.125.204.156 be whitelisted for Centroid's incremental MD refresh UAT testing. Isaac coordinated with Beeks to whitelist and issued UAT FIX credentials (MD: host 192.81.110.53, SenderCompID Argamon-Centroid-UAT-Prices / MahiFX-Centroid-UAT-Prices, port 9010). Later in thread Levi also requested Orders session — Isaac confirmed all good and asked whether orders should go into retail book or a separate unused book (unanswered as of catchup). [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1782182611235909)

> [resolved] 2026-06-21 — CLS-OFIMB removed from registry; 13 processes down at CHI/LDN; signal versioning issue; fixed by 12:11 BST
> Isaac removed CLS-OFIMB from the registry after 13 processes failed to come back up at Toa Args CHI and LDN. `propTrader1HrpLdn1` and `signalProcess1` also still down — identified as signal versioning related. James did a redeploy by 12:11 BST: CHI and LDN admin all running; only `propTrader1HrpLdn1` still down (expected). [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1782028930298559)

> [resolved] 2026-06-21 — Twilight XAUUSD TOB spread config approved: 25–50oz at 15c, mirror NYC beyond
> Daria raised $1.5k twilight XAUUSD loss and reached out to Elan. NY4 retail model TOB was 100oz at 8c (matched to Toa retail model at 25oz/25c). Proposed dropping TOB qty to 25oz or 50oz, increasing spread to 15c, then mirroring NYC beyond — Elan approved same night. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1782081899504989)

> [resolved] 2026-06-25 — All brokered XAUUSD flow reverted to LPs from NY4 (retail) — Elan's request
> Daria reverted all brokered XAUUSD flow back to go to LPs from the NY4 (retail) environment at Elan's request (02:59 BST). Closes out the CP 90000580 re-internalisation watch: flow was going offside within 2 minutes when internalised; now fully back on LP routing. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1782352799253379)

> [watching] 2026-06-22 — CP 90000580 re-internalised; flow going offside in 2 min vs onside when brokered
> Daria switched CP 90000580 back to internalised late last week (had been forcibly brokered per Elan's request). Up $6k from 90000580's trading on 2026-06-22 morning, but internalised flow is going offside within 2 minutes — opposite of the onside aggregate brokered trades over recent weeks. Reverted fully to LPs at Elan's request 2026-06-25 — see entry above. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1782092790487579)

> [open] 2026-08-27 — 26Degrees duplicate trade ID killed hybridHedger; ~$6k retail loss; dynamic-mid restart fix
> 26Degrees sent a duplicate trade ID which caused hybridHedger to crash. ~$6k retail loss during the ~10-min outage. Root cause of slow restart: dynamic mid subscribing too many markets. Liam changed mid style to PRICING_MID, reducing restart time from ~10 min to ~1 min. 26Degrees switched back GTC→IOC on 2026-08-29. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1756321563066389)

> [open] 2026-08-26 — 26Degrees brokering disabled; stuck order 012dr73mxzj; Zendesk 21328
> 26Degrees brokering had to be disabled due to a stuck order (012dr73mxzj) that was force-cancelled via JMX. Zendesk ticket 21328 opened. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1756197490495109)

> [open] 2026-08-11 — Elan considering switching off NY Insti routing around Mahi; Zendesk 21238
> Elan flagged he is considering switching off the NY Insti routing that goes around Mahi. Liam noted this probably suits Mahi given they aren't supposed to be doing Insti anymore (Toa is now the insti vehicle). Zendesk 21238. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1754902798818409)

> [resolved] 2026-08-04 — NatWest PB NOP limits set at 40m USD per Elan request
> Liam configured the market list and PB NOP config at 40m USD NOP limit per Elan's request. Only using Reactive NW markets. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1754304532621039)

> [open] 2026-07-29 — PB NOP UI dev work requested: HRP and NatWest users to see only their own NOP/kill-switch; Zendesk 21166
> Argamon requesting UI work so HRP users and NatWest users see only their own NOP/kill-switch in the GUI. Liam identified significant UI changes needed. Dave chatted with Elan — may be solvable with a hack to hide NatWest NOP from Hidden Road users. Zendesk 21166. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1753780318658499)

> [resolved] 2026-07-29 — Centroid broker-orders NPE (TradingAccount mapping); Liam fixed via config reload
> NPE on FIX.4.4:MahiFX-Centroid-Broker-Orders→Argamon-Centroid-Broker-Orders: `TradingAccount mapping: Account->TradingAccount`. Config had been added before the trading account existed. Liam tweaked and reverted config to force a reload; resolved. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1753779667961769)

> [resolved] 2026-07-24 — FSS markets decommissioned at Argamon (14 markets removed)
> Full FSS cull complete: COMMERZ_FSS, JPM, NATWEST_FSS, XTX_2, XTX_STD, DEUTSCHE_FSS, HSBC, JPM_INST, JUMP, UBS, XTX_DARK, XTX, HCTECH, LMAX all removed. RI hedgers not running post-release (expected per Will). Environment significantly cleaned up. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1753334480526809)

> [watching] 2026-07-21 — Argamon Crypto -$2.6k from $3.6m (-$729/M); CP 84004149 sharp FX+crypto risk
> Daria flagged CP 84004149 doing lots of FX + crypto risk, resulting in -$2.6k from $3.6m notional (-$729/M) on the crypto book. Will noted this is sharp risk. Flagged for investigation. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1753053359267329)

> [resolved] 2026-07-21 — MT4→OZ issue left -12.9m JPY open; position appreciated ~50 pips; closed via OZ→Compass hedges
> An MT4→OZ connection issue left a -12.9m JPY position open. The position appreciated approximately 50 pips before it was closed out via OZ→Compass hedges. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1753131641988199)

> [resolved] 2026-07-14 — Reactive slow-consumer recurrence; Beeks L2 escalation required; GTS markets added to non-LP-reducing rules
> Argamon raised Reactive connectivity issue again with Beeks — hour on the phone before L2 escalation, then fixed almost instantly on escalation. GTS Reactive markets added to hybridHedger1 non-LP-reducing rules following this event. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1752458081221389)

> [resolved] 2026-07-09 — Insti contract signed to Toa; Lucera credentials issued; pricing review before go-live
> Nicola confirmed insti contract is signed to Toa. Lucera credentials issued (production). Pricing review needed before going live with new Reactive feeds. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1752075272632989)

> [resolved] 2026-07-08 — XTX-Algo confirmed live; all test trades good
> fixOrdersXtxAlgo confirmed live on 2026-07-08; all test trades passed. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751978544253569)

> [resolved] 2026-07-07 — Reactive HRP/NatWest streams disconnected after Beeks weekend change; switched to OZ takers
> Reactive HRP and NatWest streams disconnected following a Beeks weekend change. Isaac switched hedgers back to OZ takers while Beeks investigated. NatWest slow consumption issue isolated but not yet fixed. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1751845142867209)

> [resolved] 2026-07-02 — Currency rec crisis resolved; adjustments applied; Argamon to submit regular rec reports going forward
> Multi-call resolution with Elan, Jonah, Alex, Levi, Isaac: adjustments applied to realign Compass positions. Going forward Argamon will regularly submit rec reports and Mahi will adjust Compass positions. Argamon had misread their rec (both client+LP out); retail book recovered to +$19k. Elan raised ~$125k attribution question; Mahi pushed back that attribution would need senior discussion. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751424351939279)

> [resolved] 2026-07-01 — Contract split confirmed: Mahi=retail tenant, Toa=B2B/Crypto/RI; connectivity pipeline to Toa
> Andrew Morgan formally confirmed the split: Mahi retains retail tenant; Toa takes B2B/Crypto/RI. Connectivity pipeline falls to Toa. Resourcing shuffle between teams pending meeting. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751381584552799)

> [resolved] 2026-06-27 — Lucera conformance completed; maker session via NatWest being set up
> Elan confirmed Lucera completed conformance. Isaac setting up maker session hedging via NatWest. FIX credentials issued 2026-07-04 in production. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1751005957276989)

> [resolved] 2026-06-22 — Spotex timeout + position break; client fill adjusted; hedgers closed position
> Elan flagged a Spotex timeout; client ended up long with HSBC fill. Daria adjusted the client fill out of book; hedgers closed the resulting position. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1750629998286959)

> [resolved] 2026-06-19 — Position break from Beeks outage (Mon 16 Jun); Argamon rec requested; books to be monitored
> Trades were dropped on reconnect following the Beeks outage on Monday 16 June, creating a position break. Daria asked Argamon for a rec to realign. Amir asked to monitor and adjust CLIENTS/HEDGING_MANUAL books. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1750316141620449)

> [resolved] 2026-06-12 — XAUUSD over-hedge query (26 May); Shyam confirmed no over-hedge from Mahi side
> Levi (Argamon) raised in mahi-argamon-operations that they were trying to investigate a potential over-hedge of 1 XAUUSD on 26 May and asked for help narrowing the search. Shyam asked whether it was retail; Levi confirmed yes (though no position rec data yet). Shyam investigated and confirmed no over-hedge from Mahi side. Resolved same morning. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1781234757662239)

> [resolved] 2026-06-11 — CHI signal process NPE (No classification store for HRP); tenant profile rename cause; process restarted; up by ~14:38 BST
> James (12:58 BST) spotted a PD alert for the CHI signal process killed with `NullPointerException: No classification store for HRP - available: [HRP-MM, NATWEST-M, HRP-PROP]`. James identified the root cause: renaming a tenant profile can take out models. Liam confirmed there's an NPE-safe version of the code but it wasn't changed everywhere (the Distribution subsystem had it but not here). Process went down again (~14:36 BST, PD Q0CHFO1JC1E7FN — had been down 2h at that point). James restarted and it was up by 14:38 BST. James @mentioned Cameron Copland to flag any further alerts he missed. Underlying NPE-safe fix not yet rolled out to all affected paths. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1781179106111309)

> [open] 2026-06-11 — HRP PnL firewall breach ($50k drop); CBOE/CME hedger toggle; Elan spread config interference; manual PnL adjustment applied
> Nathan (01:33 BST) reported HRP_CLIENTS_NET dropped ~$50k with hedgers tripping PnL firewall — attributed to big XAU PnL reval; risk cleared and hedgers re-enabled. Daria flagged −$2,000/M in 10s (01:40 BST). Lee investigated hedgers going back and forth far more than client volume justified; turned off CME hedger (01:44), then flipped to turn off new CBOE hedger and restore CME (01:54). Lee subsequently concluded it was not a hedging issue — "Elan has been mucking around in spread config" (02:47 BST). Lee applied a manual PnL adjustment to correct the earlier jump (04:43 BST). Root cause (Elan's spread config changes) identified but no config rollback confirmed in thread. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1781138037921729)

> [resolved] 2026-06-11 — USDCHF pricing gap at ROLL; MAHI_BENCHMARK_LDN added; CP fast-hedge tagged
> Shyam identified ~$1k PnL drop where CP 90002035 obtained favourable USDCHF buy prices over ROLL — distribution price was slightly below market because most LPs were unstable during that ~15-min erratic period. Shyam added `MAHI_BENCHMARK_LDN` as an LP for USDCHF price formation; the CP has since been tagged fast-hedge, which prevents this going forward. Before/after backtest confirms the LP addition keeps distribution price higher and more in line with market over roll. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1781148840004809)

> [resolved] 2026-06-10 — propTrader1HrpChi1 max-order-breach crash; ordersCOMEX1 party filter fix
> Cameron posted propTrader1HrpChi1 down on toa-argamon-ch-trading-1 due to maximum number of order breaches (08:58 BST) — brought back up, killed itself again. James fixed ordersCOMEX1 party filter; noted if it dies again leave it down — it's prop trading not hedging so doesn't need to run. (Updates/closes the open 2026-06-07 entry re: propTrader1HrpChi1 still unconfigured.) [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1781078300294379)

> [resolved] 2026-06-09 — Centroid HRP FIX logon not receiving response; resolved (Centroid live per July test trades)
> Levi (Argamon) reported in mahi-argamon-operations that Centroid cannot get a logon response on either the market session (HRP-CENTROID2Prices) or trading session (HRP-CENTROID2Orders) — Centroid sent FIX.4.4 Logon (tag 35=A) out but received no reply. Kate checked and asked Levi to netcat to 170.75.204.26 ports 9010 and 9011. Issue subsequently resolved — Centroid went live with HRP as test trades confirmed operational through July 2026. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1781000635571119)

> [resolved] 2026-06-09 — hedgerHrpCME1 PnL breach alert; self-resolved hedge fluctuation
> Cameron posted PD alert for PnL breach on `hedgerHrpCME1` at toa-argamon-ch-trading-1 (15:51 BST). James investigated: PnL was hedge-side fluctuation that matched from client flow — no real loss. `propTrader1HrpChi1` also flagged not running (confirmed not configured yet, consistent with open 2026-06-07 entry). James restarted the process. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1781016700103829)

> [resolved] 2026-06-09 — marketDataNado2 OOM; self-recovered
> Cameron posted PD alert for OOM on `marketDataNado2`; noted it appeared to have self-recovered. No further action taken. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1780991529998909)

> [open] 2026-06-08 — INST-34 orderRejectThrottle storm; off-market limit orders flooding TOA-ARGAMON-LDN
> Nathan (Toa ops) flagged counterparty INST-34 triggering `orderRejectThrottle` continuously throughout the day at TOA-ARGAMON-LDN — constant limit orders rejected for being off-market; worst PD alert was 27k orders in 5 min. Lee Butts raising with Argamon; Argamon responded (via quoted reply) that they're discussing withholding these orders with the client and pursuing a Centroid-side fix too. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1780889725278749)

> [resolved] 2026-06-07 — MARKETMAKING_HRP_INSTI-Channel processes down at CHI + LDN; gateway build mismatch; propTrader1HrpChi1 now configured
> Nathan flagged processes down at both argamon-chi and argamon-ldn related to MARKETMAKING_HRP_INSTI-Channel. Maten investigated: default counterparty LR rule had been removed (mid-week change); he restored defaults and clientDist processes came back up. Separately, gateways at LDN were crashing with `NoClassDefFoundError: connectionstatus/ConnectionStatusSource` — caused by a newer gateway build (20260605.090257) deployed without the matching core/distribution build. Maten rolled back gateway component to 20260529.164545 on CHI (copied from LDN); gateways back up. `propTrader1HrpChi1` configured 2026-06-10: James fixed ordersCOMEX1 party filter; process should be left down if it crashes again (prop trading, not hedging — see 2026-06-10 entry). [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1780814743280519)

> [resolved] 2026-06-05 — Compass upgrade this weekend; Argamon notified
> Liam notified Argamon in mahi-argamon-operations that their system will be upgraded to the latest Compass version over the weekend, with monitoring at open. Argamon acknowledged. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1780673110439059)

> [resolved] 2026-05-27 — CLIENT_PRICE_MARKET switched to CLIENT_PRICE_RETAIL_NYC; YP reval errors fixed
> Daria switched the default client price market from `CLIENT_PRICE_NYC` to `CLIENT_PRICE_RETAIL_NYC` after YP (yield profile) reval failures — `CLIENT_PRICE_NYC` is the old insti pricing model and was causing `IllegalArgumentException: CLIENT_PRICE_NYC/GBPJPY unavailable` during reval processing. Fix applied in the early hours (01:54 BST). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1779843264602109)

> [watching] 2026-05-26 — HRP_CLIENTS_NET PnL drop alert (-$7.7k in 20 min); XAUUSD main contributor
> PnLDropAlert fired on toa-argamon LDN HRP_CLIENTS_NET: PnL moved from $344,257 to $336,072 (−$7,686) between 11:19–11:39 UTC. Maten attributed to XAUUSD. No remediation action noted; monitoring only. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1779795816962169)

> [resolved] 2026-05-26 — hedgerCBOE1 added to toa-argamon LDN
> James added hedgerCBOE1 to the toa-argamon LDN configuration (alerts suppressed during change). [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1779805776124319)

> [open] 2026-05-25 — EURZAR/USDZAR pricing 25-min late start; all configured LPs dark 21:00–21:30 UTC; LP set expansion proposed
> William (Argamon) raised that EURZAR and USDZAR ticks were missing from 21:00–21:30 UTC on 2026-05-25, causing ~25-min delayed pricing start. Shyam confirmed all 5 configured LPs (LMAX_DIRECT_NY_RETAIL, XTXM_RCTV_HRP_2, GTSX_RCTV_HRP_1, NWM_RCTV_HRP_1, HSBC_RCTV_HRP_1) were dark for USDZAR during that window, making pricing indicative until ticks resumed at 21:30; EURZAR also affected (triangulated off USDZAR). Shyam proposed adding DB_RCTV_NWPB_1, COMZ_RCTV_NWPB_1, UBS_RCTV_HRP_1, UBS_RCTV_NWPB_1 to the formation — awaiting Argamon/William response. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1779745720146389)

> [open] 2025-07-09 — Retail contract conversion to fixed fee pending; Elan wants spread tightening
> Daria flagged that Elan wants to significantly tighten spreads, which would eat into retail P&L under current billing; pushing to get contract converted to fixed fee before moving reduced spreads to production. No resolution yet. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1752015694887489)

> [open] 2025-06-16 — Position breaks after Beeks outage; ongoing rec with Argamon
> Beeks outage 2025-05-25/26 (DNS/public connectivity broken on trading-1 and -2; fixed ~2h after ticket NOCINT-710359). Trades dropped on reconnection created position break. Daria asked Argamon for position rec 2025-06-16 to realign Compass. Subsequent rec work revealed deeper currency breaks (see 2025-06-23 entry). compassDB query performance also degraded — slow queries against HOUSE1TradePositionHistory taking >30s; Justin bumped `net_read_timeout` to 240s. Argamon also requesting Pulse or broader DB access for trade-by-trade rec. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1748216407505139)


> [resolved] 2026-05-08 — XAUUSD signal reverted neuron → synapse; skew-driven decision
> Shyam switched XAUUSD signal back to synapse (from neuron, which was set 2026-04-22) in response to skew analysis. Monitoring for CPs picking off pricing; pricing impact review planned for next week. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1778211684932129)

> [open] 2026-05-19 — TOA_CHI 10-min pricing dropout + 100% CPU / Aeron meltdown; LP pricing gap causing reject storm
> ~15:07 BST Tom flagged loads of XAUUSD rejects due to internalisation disabled; Kate confirmed LP pricing had dropped out — brokering attempted for toxic tags but no LP price received, causing high cancel/retry volume (yields -$950/M at 2 min). LP pricing recovered shortly after. Separately, James flagged 100% CPU and an Aeron meltdown in CHI around the same time (~18:29 BST message), with screenshots showing the degradation. Root cause not yet posted in thread. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1779199627807509)

> [resolved] 2026-05-19 — TOA GUI Insti_light spread config error (JSON copy issue)
> Elan raised the `CLIENT_PRICE_INSTI_LIGHT` spread config for XAUUSD failing to display in the TOA LDN GUI. James investigated and fixed — misconfigured `name` field in JSON (value copied incorrectly). Resolved same day. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1779186517949549)

> [resolved] 2026-05-21 — CP 104719 channel/profile classification difference query from Tom; explained by Isaac
> Tom asked why CP 104719 was brokered for trade `012dr52qh1v` (A_CLIENTS_TOA / CATCHALL Dynamic-Broker) but internalised 12 minutes later for `012dr52qh3k` (A_CLIENTS / CATCHALL Dynamic-Don't B Book). Rory identified different channel classification as the driver. Isaac Dann followed up 2026-05-22: both trades fell under the same profile, but CP 104719's 28-day yield is hovering near the rehab threshold — a single agent cycle (~few-hourly) can flip the classification. Order B landed in a 2.5-hour window where rehab had succeeded, then re-brokered afterwards. Tom confirmed resolved. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1779357670831129)

> [resolved] 2026-05-15 — HRP missing give-up (missing booking config on Toa)
> Tom flagged HRP was missing Mahi's side of a give-up. James investigated — missing `connectivity.booking.bookingSystemRouting` config on Toa side (not sent). Tom asked HRP to book manually; James confirmed fix applied. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1778840217972969)

> [open] 2026-05-04 — XAUUSD TOO_LARGE reject storm on TOA_CHI/A_EXTERNAL_WASH; ZenDesk ticket open, analytics support not yet assigned
> Emergency alert fired ~12:00Z: 98% reject ratio (93/95 orders) from counterparty 90000580 on XAUUSD in TOA_CHI/A_EXTERNAL_WASH — validation error `quantity=TOO_LARGE, maximumShowQuantity=TOO_LARGE`, burst window 11:59:38–12:00:00Z. Justin Young routed to ZenDesk (ticket 22907) and asked who's on analytics support — no reply in thread as of catchup. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777898434100499)

> [resolved] 2026-05-04 — EURUSD mid-formation LP set broadened; arb opportunities eliminated
> Elan approved adding all LPs back into mid formation for NY (now retail-only). Shyam added DB_RCTV_NWPB_1, EDGW_RCTV_NWPB_1, GTSX_RCTV_HRP_2 as supplementary EURUSD mid-formation LPs — backtests confirm significantly reduced spiky pricing and arb opportunities at open and general periods. Adaptive mid logic also added to betaRetailPricer1 for EURUSD as a further experiment. Shyam continuing review of other instruments and overall FI/skew PnL. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777869938380839)

> [resolved] 2026-05-03 — XAUUSD retail NY4→CHI hedging disabled (negative retail spreads in CHI)
> Daria disabled XAUUSD retail hedging via NY4→CHI because retail flow was achieving positive spreads while CHI was delivering negative spreads — the brokering test was working against retail PnL. Closes out the 2026-04-28 CME hedging expansion trial. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777845150173619)

> [resolved] 2026-05-01 — XAUUSD retail losses from sharp/sniping flow; DFSN signal added; signal-follow whitelist cleaned
> Isaac identified XAUUSD retail losses from 2026-04-30 caused by signal-follow clients sniping sharp moves in pricing. Affected counterparties moved back to broker-only classification (signal-follow whitelist cleaned). DFSN signal rule added to the pricing model to widen Mahi out of the way during large moves. Separate from but related to the CME hedging brokering test (2026-04-28 open issue). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1746063187834529)

> [resolved] 2026-05-01 — Wide spread on majors (~15:00 BST); LR kicking in on published rate
> Tom flagged EURUSD at ~20 ticks wide for a couple of hours with no client complaints yet. Will identified LR kicking in on the published rate — removed from published, spread immediately restored. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746107990556329)

> [resolved] 2026-05-01 — JPY crypto LMAX position risk at rollover (non-issue)
> Tom wanted LMAX removed from JPY crypto hedging/STP ahead of anticipated large JPY financing charge at rollover. Amir confirmed with Isaac that JPY crypto pairs are weekend-only for hedging and are not STP'd — no position should build regardless. No config change needed. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1746087135603309)

> [resolved] 2026-04-28 — XAUUSD brokered counterparties expansion to test CME hedging; CHI hedging disabled 2026-05-03
> Daria added counterparty 104881 to be brokered to Toa (working through 104881, 105048, 105153, 105681, 105773) to evaluate whether hedging XAUUSD to CME helps. Result: CHI hedging disabled 2026-05-03 as retail was achieving positive spreads (negative in CHI), meaning the NY4→CHI brokering was not beneficial for retail flow. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1777845150173619)

> [resolved] 2026-04-22 — XAUUSD signal switched synapse → neuron, then back → synapse 2026-05-08
> Shyam moved XAUUSD from synapse to neuron model to reduce spiky pricing; also cited better skew PnL over the last month. https://mahifx.slack.com/archives/C06U76A7ZJR/p1776832052585769. Reverted to synapse 2026-05-08 following skew analysis (see 2026-05-08 entry).

> [resolved] 2026-04-20 — USDCAD ask-price spike, over-weighting HSBC mid; LP set broadened 2026-05-04
> Tom flagged order 012dr52nxnb filled at 1.371 while market was around 1.370; only HSBC was deviating (other mid-formation LPs unavailable). Tom asked Elan re. adding COMZ and other non-skew-protective LPs into mid. Resolved 2026-05-04: Elan approved adding all LPs into mid formation now that NY is retail-only; Shyam added DB_RCTV_NWPB_1, EDGW_RCTV_NWPB_1, GTSX_RCTV_HRP_2 for EURUSD, significantly reducing spiky pricing. Further instruments under review. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1776694811277649)

> [resolved] 2026-04-21 — EURHUF indicative pricing; Commerz added
> Daria flagged EURHUF going indicative on/off (2026-04-17), proposed adding LPs into price formation just for that pair. Tom preferred Jane St + Commerz. Shyam added Commerz on 2026-04-21; backtests showed it stops the indicative pricing. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776394647886729

> [open] 2025-04-15 — DB filtered out for small-ticket FX brokering (NWPB min size)
> Tom queried order 012dr82osqn filling via UBS not DB despite both being highlighted. Isaac explained DB was filtered because client order was 5k vs the 15k min-ticket on Mahi's NWPB FX hedger config. James noted Natwest has min ticket sizes and that work with Reactive on a direct setup will remove the constraint. Tom raised whether a 15k floor is justifiable for small-volume auto-brokered clients. Direct-Reactive setup is the in-flight remediation; as of 2025-07-07 Liam/Isaac are configuring HRP LP mappings for Reactive (HSBC/JPM/UBS/NWM/JLQD/XTXM_RCTV_HRP_1) and test trades are progressing. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776233897732439

> [resolved] 2026-04-13 — Missed give-up to HRP (3 EURUSD trades, one not given up)
> Levi reported HRP saw only 2 of 3 trades give up; HRP manually booked the missing one. Daria pulled the FIX AE messages — all three appear to have been sent from Mahi side. Tom said he'd check with HRP; no further messages, treating as resolved on Mahi side. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776034785118149

> [resolved] 2026-04-13 — First-5min market-open EXPIRED / REJECTSYSTEMERROR RAT bursts
> Levi flagged a quantity of rejected orders at market open. Daria identified cancels/rejects clustered after the first 5min, particularly AUDCAD CAD crosses; brokering rules cancelled them because market data wasn't being received yet (Jane Street AUDCAD MD started at 21:10). RATE_LIMIT_EXCEEDED was hit due to retries — 150 orders/sec/counterparty cap. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776049759858249

> [watching] 2026-04-13 — Wide pricing persisting > 1h after rollover
> Tom raised wide pricing in the post-rollover hour, asking for any improvements. No response captured in the window. https://mahifx.slack.com/archives/C06TW3D8NMV/p1776042834123209

## Notable topics

- Build push to Toa Chicago blocked pending release branch + regression (2026-07-03): David Cooney requested latest build be pushed to Toa Chicago to support Lee's options connectivity work. Lee Butts replied it needs a new release branch cut and regression testing first — not ready to go. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1783049787092519)
- Centroid UAT IP updated to 192.109.23.20 (2026-06-30): Argamon requested the Centroid UAT IP be updated from 185.125.204.156 to 192.109.23.20 for the ongoing incremental MD refresh testing. Addressed to Isaac Dann in mahi-argamon-operations; ✅ actioned (no reply needed). [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1782799990703719)
- PXM_LD4_A monitoring disabled on APN1 (2026-06-29): Maten disabled PD monitoring for PXM_LD4_A distribution connection on Toa Argamon APN1 — had been disconnected since config was added; disabled to reduce PD noise. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1782721198480769)
- Booking rejects PD alert = test trades (2026-06-29): PD incident Q3H4ARZS4AW58Y fired for booking rejects; James confirmed these are test trades. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1782727722330439)
- Centroid UAT incremental MD refresh testing (2026-06-23): Levi requested IP whitelist + FIX credentials for Centroid's incremental snapshot→incremental MD refresh UAT. Isaac issued UAT credentials and Beeks whitelisted 185.125.204.156. Orders session also added; Isaac asked whether orders should land in retail book or unused book — no response yet as of catchup. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1782182611235909)
- CP 90000580 XAUUSD brokering resolved (2026-06-25): After re-internalising on 2026-06-22 (flow going offside in 2 min), Daria reverted all brokered XAUUSD flow back to LPs from NY4 retail environment at Elan's request (02:59 BST). Closes the rehab-loop watch for now. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1782352799253379)
- Twilight XAUUSD TOB spread config tightened (2026-06-21): NY4 retail model was 100oz at 8c during twilight after matching to Toa retail model. After $1.5k loss, Elan approved reducing TOB qty to 25–50oz at 15c and mirroring NYC spread beyond. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1782081899504989)
- Jonah Ink departed Argamon (Aug 2026): Will relayed Isaac's intel — Jonah has left. Escalation contact for rec disputes and P&L attribution now unclear. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1754902798818409)
- Elan considering switching off NY Insti routing around Mahi (2026-08-11): Zendesk 21238. Liam noted this suits Mahi since Toa is the insti vehicle. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1754902798818409)
- 26Degrees recurring brokering issues: stuck orders (2026-08-26, force-cancelled via JMX, Zendesk 21328) and duplicate trade IDs crashing hybridHedger (2026-08-27, ~$6k retail loss). Dynamic-mid startup performance fixed (PRICING_MID reduces restart from ~10 min to ~1 min). 26D switched back GTC→IOC 2026-08-29. Pattern of recurring 26D disruptions. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1756321563066389)
- PB NOP UI work pending (Zendesk 21166, 2026-07-29): Argamon wants HRP and NatWest users to see only their own NOP/kill-switch. Liam flagged significant UI work; Dave/Elan may have a hack (hide NatWest NOP from HRP users). [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1753780318658499)
- FSS cull complete (2026-07-24): 14 markets decommissioned from Argamon (COMMERZ_FSS, JPM, NATWEST_FSS, XTX_2, XTX_STD, DEUTSCHE_FSS, HSBC, JPM_INST, JUMP, UBS, XTX_DARK, XTX, HCTECH, LMAX). RI hedgers not running post-release (expected per Will). Environment significantly cleaned up. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1753334480526809)
- XTX-Algo hedger confirmed live (2026-07-08): All test trades passed. Separately: XTX_ALGO not suitable for brokering (IOC timeout); PRICING_MID style adopted to fix slow dynamic-mid restarts. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751978544253569)
- Contract split confirmed (2026-07-01): Mahi=retail tenant, Toa=B2B/Crypto/RI; connectivity pipeline falls to Toa; insti contract signed to Toa. Resourcing shuffle between teams pending. Retail contract conversion to fixed-fee still pending before Elan's planned spread tightening. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751381584552799)
- Currency position rec is a formal recurring process (resolved 2026-07-02): Argamon submits rec reports; Mahi adjusts Compass positions to match. Root causes include crypto JPY hedging currency exposure and large EURAUD trader P&L included in Compass but not client platform. Will Carter proposed argamon_rec.ipynb in analytics-python-tools. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1751424351939279)
- Reactive Markets production progressing (recurring): NatWest slow consumer isolated (not yet fixed). Beeks escalation required each incident — pattern is: hour on phone with L1, L2 escalation, fixed instantly. HSBC_RCTV_HRP_1 noted as slow consumer. HRP/NatWest streams disconnected after Beeks weekend change (2026-07-07) required switch to OZ takers. GTS Reactive markets added to hybridHedger1 non-LP-reducing rules 2026-07-14. [permalink](https://mahifx.slack.com/archives/C06TW3D8NMV/p1751845142867209)
- CHI signal process NPE root cause: tenant profile rename (2026-06-11): James identified that renaming a tenant profile kills models referencing the old name. Liam confirmed the NPE-safe version exists (used in Distribution) but not deployed everywhere — an open code hygiene issue. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1781179106111309)
- CBOE hedger toggled off after PnL firewall breach (2026-06-11): New CBOE hedger at TOA-ARGAMON tripped during overnight XAU reval event — Lee turned off CBOE and restored CME after determining hedgers were over-trading relative to client volume. Separately established that root cause was Elan's spread config changes, not hedging. CBOE hedger remains off. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1781138596048159)
- referencePriceMarketSelectors tuned for XAU/EUR/GBP (2026-06-10): Shyam updated LP sets for three instruments after lead-lag and TOB analysis. XAU: removed NWM_RCTV_HRP_1 and MAHI_BENCHMARK_LDN, added COMZ_RCTV_NWPB_1. EUR: removed GTSX_RCTV_HRP_2, added COMZ_RCTV_NWPB_1. GBP: added UBS_RCTV_HRP_1. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1781062155159539)
- Build hygiene flag: Maten noted after the 2026-06-07 gateway rollback that toa-argamon should retain more than just the latest build so rollbacks can happen without copying from another env. [permalink](https://mahifx.slack.com/archives/C035H1VNCAD/p1780814743280519)
- Weekly P&L (w/c 2026-05-12): $5.9k retail loss from XAUAUD scalping (CPs 105988 + 105990). Root cause: `arbProtectionParameters` clamping published quote into UBS's wide twilight spread. Fix: removed XAUAUD from arb protection; now uses pure triangulated price. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1778648027949039)
- XAUUSD routing rehab-loop risk (2026-05-25): Routing toxic flow to Toa improves yields → loses toxic classification → gets re-internalised → becomes toxic again. Daria proposed static brokering list for metals or harder rehab barrier; FX/metals tenant profile split planned. [permalink](https://mahifx.slack.com/archives/C06U76A7ZJR/p1779681392035259)
- Reactive direct setup is the strategic remediation for NWPB min-ticket-size filtering. Flagged 2025-04-15; HRP LP mappings configured; production test trades in progress.
- Centroid LDN distribution issues (James Furness dig) — backpressure root-caused via pcap; Centroid migration from OneZero complete. CPU-saturation at high load; LP feed pruning applied.
- XAUUSD sharp-flow / signal-follow risk — whitelist cleaned 2025-05-01; DFSN signal added; monitoring ongoing.
- Insti model: Lucera replacing Centroid path (NatWest drop copy 5-month delay was blocking factor). Conformance complete; NatWest maker session live. Pricing review before full go-live.
- Compass DB access / Pulse — Argamon requested broader DB access for rec. Liam: Pulse contract required. Slow HOUSE1TradePositionHistory queries addressed.
