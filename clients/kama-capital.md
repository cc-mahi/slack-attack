---
slug: kama-capital
aliases: []
refs:
  vibepulse: null   # no ../VibePulse/.claude/clients/kama-capital.yaml yet
  billing: ../MahiProduct/data/billing/clients.json     # entry: kama-capital
  hosts: ../MahiProduct/data/client-hosts.json          # entry: kama-capital
  wiki: ../MahiProduct/wiki/clients/kama-capital.md
channels:
  internal-kama: C0B6FMU96G2
  mahi-kama-capital: C0B7T6S6D0C
  mahi-kama-config-updates: C0C1L6G37HN
contacts:
  - {name: "Mohamad (Moe) Ibrahim", role: "COO, decision-maker; sets execution rules and LP choices"}
  - {name: "Ali Chayto", role: "dealing; day-to-day on routing, LPs, test trades"}
  - {name: "Jad Hayek", role: "ops / access, whitelisting, Compass users"}
  - {name: "Mahmoud Kleit", role: "built Kama's swap sync tool; on holiday as of 2026-10-09", confidence: low}
  - {name: "Sammy (xrigroup)", role: "third-party consultant helping Kama on SI and tags; pushes SI", confidence: low}
last_catchup: 2026-10-15T12:57:40Z
status: active
---

## Now
Live Compass-managed A Book on XAUUSD (plus HFT and Kama Securities flow) with most connectors routed since 2026-09-29; Kama keeps tuning execution style and the LP pool. Kate Stagg is the day-to-day owner; Moe Ibrahim drives changes on the client side. Pilot term status is unresolved: Bonnie says it lapsed 33 days ago, Will says the post-pilot terms were already recorded ready to send.

## Streams

### lp-pool-expansion — LP pool and hedging markets, KL/KS connectors
status: open · since: 2026-09-21 · last: 2026-10-15
State: Pool started as Scope only. Moe asked 2026-10-01 for Scope, MAS, Edgewater, MatchPrime-FXedge and Arts with NOP limits. FXEdge and Arts went in after test trades (5-6 Oct), then Arts was pulled for latency (6 Oct). MatchPrime was restricted to gold on 7 Oct and restored on all symbols the same day after they fixed swap rates. On 14-15 Oct Star and Velocity were added and Ali sent a clean-up list, ending with Moe's final list: LIQUIDITY_POOL_HFT_LDN = Edgewater_2_KS, MAS_Toxic_KS, Scope_Toxic_KL; LIQUIDITY_POOL_LDN = Edgewater_2_KS, Scope_KL, MAS_KS, FX_EDGE_KL. Kate suggested spreading load across LLC (KL) and Securities (KS) connectors rather than all on KL. Pool changes need EOD restarts; hedger changes can be bounced intraday.
Next: Kate to make the 15 Oct pool changes and remove listed LPs ahead of weekend restarts; Ali to flag when Star and Velocity are ready for test trades before they join the pool.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1789990153651149 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1792062491797469

### si-and-risk-golive — Risk-management go-live and SI
status: open · since: 2026-09-15 · last: 2026-10-15
State: Risk go-live began 2026-09-14 but the first A Book client switched off after a position-rec scare and an SOR restart that tripped PXM's firewall; flow came back 17-23 Sep. Kate pushed Kama to run the Compass book for a few weeks before SI, and ran SI sims on Moe's tag cohort (results weak; Sammy argued SI may not suit Kama). Mahi view (Andrew, Will): flow with Kama in aggregation (e.g. Star, tag 42060) is not SI material. On the 8 Oct call Kama wanted SI soon and supplied a list of tags; Kate is running sims on those tags and the full portfolio and will review with them. Kama also wants to add 26degrees and ISAM and asked for anonymised reject-rate data from other clients.
Next: Kate to finish the SI sims and walk Kama through them; decide what reject-rate data (if any) to share.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789482321712589 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792064464469069

### xau-execution-style — Broker vs Broker First, HFT book and markup
status: open · since: 2026-09-21 · last: 2026-10-15
State: A 21 Sep cancel burst came from FOK/IOC MinQty handling (fixed with reference.marketSupport.FOK) and led to Kama moving all A_CLIENTS to Broker First (29 Sep). HFT flow got its own book and hedgers (30 Sep) with internalisation on the toxic HFT pool; $20/M markup on HFT and $10/M on A Book internalised flow was agreed on the 1 Oct call and set up via MultiChannelConfig on 2 Oct (a type=list vs ArrayList misconfig caused stuck orders that day). Single-IOC vs sweep/boost on the PXM connectors was debated 30 Sep. On 15 Oct Kama asked for Broker (not Broker First) over high-impact news and said they are happy to switch manually; Moe set twilight and roll flow to Broker. Kate flagged that execution rules cannot be day-specific.
Next: Mahi to confirm whether news criteria can be added to execution rules and whether '*' as counterparty tag matches everything.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790009143944299 https://mahifx.slack.com/archives/C0B6FMU96G2/p1792064464469069

### xauusd-skew-signals — B Book XAUUSD skew tuning
status: open · since: 2026-10-08 · last: 2026-10-14
State: B Book XAUUSD skew was about -$0.35/M for 1-8 Oct because FI optimisation parties included CLIENTS_LDN (INSTI-priced, never skewed). Kate switched the skew signal to IFM, then limited optimisation parties to B_CLIENTS_LDN (8 Oct). Skew since was +$1.61/M over 9, 12 and 13 Oct (+$528 on $329M; early). On 14 Oct she moved the signal from IFM to flow-price-thresh (57.7% volume correct, $675 potential vs IFM 51.0%, $424).
Next: Kate to keep reviewing; a before/after backtest was planned.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791471223806789 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791965822602239

### weekend-risk-carry — Friday close hedging did not clear risk
status: open · since: 2026-10-12 · last: 2026-10-12
State: Compass book carried risk over the 9-10 Oct weekend (about $23k PnL bump on open). Cause: a Broker First trade was topped up just before close and Friday_Close tried to clear it but got no LP fill. Friday_Close had only 4 fills since 14 Sep (all XAUUSD, 9 Oct) and Metals.WEEKDAY-CLOSE none; the weekly hybrid-diagnostic missed dormant rules. Kama prefer Broker First to avoid cancels and client rebate claims.
Next: Shyam's PR (MahiProduct #126) adding dormant-rule and weekend-carry checks awaits Will's approval; Kate to find a way to avoid carry without day-specific execution rules.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791798684555499

### pilot-commercials — Pilot expiry and post-pilot terms
status: open · since: 2026-09-10 · last: 2026-10-12
State: Per the wiki the 3-month pilot clock started 2026-08-05 and the post-pilot terms were recorded ready to send on 2026-09-10. On 12 Oct Bonnie (from Nic's handover doc) said the pilot is 33 days expired and asked Will whether she should raise it; Will replied "same story" with a link to the 10 Sep note and "month left on the pilot", which is ambiguous. No evidence in Slack that terms were sent to Kama.
Next: Will/Bonnie to confirm whether the post-pilot terms have gone to Kama and what the current billing basis is.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1789029069493129 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791824519808849

### fx-hedge-swaps — Hedging crosses in drivers vs swap cost
status: open · since: 2026-10-09 · last: 2026-10-09
State: Moe says Kama loses on swaps because Compass hedges crosses in the drivers (EURJPY example) and wants hedging in the same currency as the client trade. Kate pushed back (drivers avoid the cross spread; only a loss if risk is held several nights). Peer data: Kama's FX major and JPY swap points are about half the network median, while gold swap is second widest. Moe agreed to inventory-skewed swaps; Mahmoud (swap sync tool) is on holiday and will do it on return.
Next: Kate to raise swap skewing with Moe; follow up when Mahmoud is back.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791544461594299

### lp-timeouts-pxm-unsub — LP latency and timeouts triggering PXM unsubscribes
status: open · since: 2026-09-15 · last: 2026-10-09
State: Recurring pattern: an order sitting unanswered trips PXM's firewall timeout and PXM unsubscribes XAUUSD on Kama's price sessions with no automatic resubscribe (15 Sep SOR restart; 2 Oct misconfigured MCC restart). Latency incidents: Arts slow fills (6 Oct, removed), MAS holding IOCs about 360ms against the 300ms latency guard (5 Oct), and a MAS order unanswered about 2 minutes that crashed the hedger (9 Oct, MAS then disabled by PXM; Moe taking it to MAS). Kama asked whether orders can be resent after timeout; Liam notes a hard timeout creates risk if the guess is wrong. Threads not expanded in this window.
Next: Kama to confirm PXM auto-resubscribe behaviour and chase MAS; Mahi to decide on hardTimeoutLength/resend handling.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791257314493849 https://mahifx.slack.com/archives/C0B7T6S6D0C/p1791566302175459

### beeks-multicast — Beeks multicast/IGMP issue and false PnL alerts
status: open · since: 2026-09-28 · last: 2026-09-28
State: Outdated reference mid prices caused false PnL-drop pager alerts on Kama; tied to a Beeks multicast issue (Zendesk 23343, Beeks NOCINT-839427). Beeks reported enabling IGMP snooping mitigated storm control and is still investigating blackholing on an LD5 distribution switch; Inald sent a chaser asking for an ETA (thread ran to 7 Oct, only the parent permalink is cited).
Next: Inald/Liam to chase Beeks for a fix ETA.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1790597791892939

### xpd-pricing — XPDUSD price jumps between LP levels
status: watching · since: 2026-10-09 · last: 2026-10-09
State: XPDUSD published mid jumped between two LP price levels 10-40bp apart (worst 8 Oct). Kate changed reference.referencePriceMarketSelectors so XPD prices off SCOPE_KL only, applied at weekend restarts. No PnL impact so far (140 XPD fills, about $28M since 8 Sep).
Next: Check XPD price variation after the weekend restart.
Refs: https://mahifx.slack.com/archives/C0B6FMU96G2/p1791557308635619

### settldate-tag64 — Bad SettlDate (tag 64) from LPs
status: watching · since: 2026-10-02 · last: 2026-10-06
State: FXEdge sent a timestamp instead of a yyyyMMdd SettlDate, so Compass rejected fills (2 Oct); Moe approved ignoring settlDate on fixOrders1 (5 Oct). PXM started sending a full timestamp in tag 64 to analyticsFixServerPXM1 on 6 Oct, breaking every fill on that feed; ignoreSettlDate switch-on proposed to the team.
Next: Confirm ignoreSettlDate is on for the PXM analytics feed; Kama to check with PXM.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790929869661149 https://mahifx.slack.com/archives/C0B6FMU96G2/p1791286163263139

### kama-securities-oz — Kama Securities entity and OZ hub connections
status: watching · since: 2026-09-23 · last: 2026-10-02
State: Kama Securities MT5 A and B clients were routed to Compass on 23 Sep (Cameron Hughes saw no rejects). On 2 Oct infra added clientDistributionGatewayOZ3 and InstOZ4 for 10 extra distribution connections for Kama's OZ hub, copying the PXM setup. 5 Oct: Arun saw the OZ FIX sessions unconnected and asked which are expected.
Next: Confirm the OZ sessions are expected to be disconnected until Kama routes to them.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790147027559829 https://mahifx.slack.com/archives/C0B6FMU96G2/p1790923697099829

### limit-order-deviation — Limit order deviation (tag 10001)
status: watching · since: 2026-09-25 · last: 2026-09-28
State: Kama pass limit-order deviation in tag 10001, which is not in Mahi's FIX spec; Mahi expects it baked into price (tag 44). Kama also reported high limit-order rejects from Scope when sending with deviation (25 Sep). Reason for the tag still unknown.
Next: Kate to learn why Kama send tag 10001.
Refs: https://mahifx.slack.com/archives/C0B7T6S6D0C/p1790332508870719 https://mahifx.slack.com/archives/C0B6FMU96G2/p1790598299904109

## Arc
- 2026-06-02 — Deal accepted; pilot agreement signed 2026-06-08
- 2026-08-05 — B Book flow live on Compass (pricing and execution)
- 2026-09-14 — Risk-management go-live (A Book), interrupted and restored 17-23 Sep
- 2026-09-23 — Kama Securities MT5 A/B flow routed to Compass
- 2026-09-29 — Almost all Kama connectors routed to Compass; HFT clients added; VaR raised to 2,000
