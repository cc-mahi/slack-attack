---
slug: trademax
aliases: [tmgm]                                            # MahiProduct onboarding tracker uses `tmgm`; infra/hosts use `trademax`
refs:
  vibepulse: null                                          # no ../VibePulse/.claude/clients/trademax.yaml yet (pre-live)
  billing: null                                            # not yet in ../MahiProduct/data/billing/clients.json
  hosts: ../MahiProduct/data/client-hosts.json             # entry: trademax (s3Slug TRADEMAX; LDN + NYC)
  wiki: null                                               # ../MahiProduct/wiki/clients/trademax.md (not yet)
  onboarding: ../MahiProduct/data/onboarding/tmgm.json     # stage tracker (slug `tmgm`)
channels_override: [internal-tmgm, mahi-tmgm]              # no VibePulse yaml to resolve from
key_people_overrides:
  - {name: "Bailey White", role: "TMGM — owns the integration decision; paused the project 2026-07-10 and set the XAU-only starting scope"}
  - {name: "Nik Teh", role: "TMGM — hub/FIX side; made the drop-copy Tag1 account-identifier change"}
  - {name: "Rainer", role: "TMGM — queried why account identifiers were needed on drop-copy", confidence: low}
last_catchup: 2026-08-04T07:08:17Z                         # ISO8601; updated by /catchup
---

## Status

- **Stage:** pre-live, pricing in production trial, recovering from a client-side pause. Bailey White paused the project 2026-07-10 over RMF/MT5 integration concerns and platform-stability priorities; Andrew's "PTR is good enough, don't let perfect block useful" push reopened it, and it came back 2026-07-23 as an urgent setup request. Pricing + skew have run on metals since 2026-07-24 (gold on the A stream, all metals on the B stream, ~1 pip skew). Client has **not** yet switched to Mahi pricing — that's the live open question.
- **Integration:** Metals-first pilot (XAU ~80% of scope), Pricing & Skew only, no volume caps. Trade reports arrive via PTR — XAU only, so skew is XAU-only even though pricing is configured for other metals and FX. `TRADEMAX_POOL_1` (top-of-book, XAUUSD only) feeds `CLIENT_PRICE_NYC` down A_CLIENTS; `TRADEMAX_POOL_2` (full depth, all metals) feeds `CLIENT_PRICE_B_NYC` down B_CLIENTS. Deliberate call to source pricing purely off TMGM's own pool feeds — no proxied reference/continuity-pool feed — so an indicative price traces straight back to their feed. FX-Majors subscriptions + pricing set up 2026-07-27 (B stream), skew still to review. Execution is a medium-term ambition, not a go-live gate; drop-copy is the fastest route per Kate Stagg.
- **Relationship:** internal urgency is high (Andrew: "This is an urgent setup request", Bailey pushing back on delays). Nicola runs the commercial cadence; Andrew + Will + Shyam + Isaac on the technical side.

## Recent issues

> [open] 2026-08-04 — XAU judged ready to go live pending Zendesk sanity checks; question now is who pushes it forward
> Follow-on from the 2026-07-28 open question ("when would they switch to our pricing for XAU?"). Shyam's update: XAU is ready for go-live pending some non-critical system sanity checks tracked in [Zendesk #23273](https://mahifx.zendesk.com/agent/tickets/23273), and skewing looks profitable under the new measurement system. He flagged the ball is in Mahi's court and asked whether LDN or NZ should be pushing it forward. Will Carter confirmed ("yes, think so") and said the data looks good enough to go share the potential with Bailey. Still no committed switch date. [xau-ready](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1785808720153749) [will-confirms](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1785823818044729)
>
> Original 2026-07-28 context: Shyam asked in the client channel whether TMGM could start sending trade reports for the other metals and FX (pricing is configured, but skew needs the flow to verify against). Bailey: "we wanted to start just with XAUUSD for now. It's the majority of flow anyway." So XAU-only is a client choice, not a gap. [client-ask](https://mahifx.slack.com/archives/C03AP4AVCCR/p1785203695028909) [internal-question](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1785210700737189)

> [open] 2026-07-27 — FX majors pricing set up on B stream; skew review outstanding, maxAgeOfTradeMs may need raising
> Shyam completed FX-Majors subscriptions + pricing, all on the B stream, with skew still to review. Separately flagged raising `analytics.maxAgeOfTradeMs` from 30s because of the latency being seen on the PTR feed. Arun infra-deployed and started `fiReportingProcess1` the same day. Neither item closed in this window. [fx-setup](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1785128295723979) [todo-list](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1784869049607509)

> [resolved] 2026-07-24 — Per-account counterparty IDs added to the PTR drop-copy (Tag1)
> Shyam flagged that PTR trade capture reports carried only a generic platform identifier, no per-account/counterparty ID. Rainer (TMGM) asked why it was needed; Shyam explained it sharpens signal quality and lets skew be tuned more granularly, but isn't critical. TMGM made the change internally, effective after the weekend hub restart; Nik Teh asked for confirmation and Shyam confirmed 2026-07-26 that account identifiers are visible on Tag1. CPs now get automated classifications off the back of it. [request](https://mahifx.slack.com/archives/C03AP4AVCCR/p1784861692782589) [confirmed](https://mahifx.slack.com/archives/C03AP4AVCCR/p1785101039073179)

> [open] 2026-07-24 — Pricing sourced purely off TMGM's own pool feeds — deliberate, but a single point of failure
> Shyam's call: no extra reference-market or continuity-pool feed proxied in, so if Mahi's price goes indicative it traces straight back to TMGM's feed — judged preferable early on to a price that jumps around or drifts off their mids basis, revisitable once proven. Will Carter flagged the flip side the day before: a single source of failure in the reference markets that should be supplemented with something network-based. Not yet reconciled. [rationale](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1784869049607509) [risk-flag](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1784801305949339)

> [resolved] 2026-07-23 — Project un-paused as an urgent setup request; metals pricing + skew live within a day
> Andrew: "This is an urgent setup request" / "Need to get PTR stood back up asap here. Servers currently not available." Noted Bailey was blaming Mahi a little for delays — despite the delays coming from Mahi pursuing the better long-term solution — and wanted to know the value-add of a delayed PTR skew. Scope set as gold #1, FX secondary. Will Carter got metals base spreads in and calibrated against the relative pool; Isaac confirmed setup essentially complete 2026-07-24; Daria checked whether the original 1-cent skew was still the plan (it landed at ~1 pip). [urgent-request](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1784794556225699) [setup-complete](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1784860298128599)

> [resolved] 2026-07-10 — Bailey paused the project over RMF/MT5 integration concerns; reopened 2026-07-23
> Bailey's message (relayed by Nicola): integrating the RMF feed needs dev work both sides; RMF is performant enough for MT4-originating trades but not MT5, whose order-finalization process gives mean latencies >500ms. Turning finalization off isn't an option because TMGM's internal data pipelines need finalized order IDs, and each hub supports only one RMF — so either they break their pipelines or OZ changes the finalization logic (OZ willing, but slow). Combined with an in-flight redundancy project, they weren't willing to add a point of failure in the execution path: "platform stability is much more important than pricing logic... I think we need to hit pause on the project at this stage." Andrew replied in the client channel that Mahi can skew without seeing the flow at all and PTR would pay for itself several times over. Bailey stayed "inclined to pause" on 2026-07-14; the 2026-07-23 restart superseded it. [pause](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1783669977028689) [andrew-reply](https://mahifx.slack.com/archives/C03AP4AVCCR/p1783677581133339)

> [resolved] 2026-07-07 — Blocked on TMGM creds for integration setup and testing
> Liam had been waiting on credentials since the prior Tuesday with two follow-ups and no reply. Overtaken by the 2026-07-10 pause and then by the PTR restart. [blocked](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1783430135583379)

## Notable topics

- 2026-07-24 — A_CLIENTS / B_CLIENTS here split *which price Mahi returns*, not booking — a non-obvious deviation from the usual meaning. `TRADEMAX_POOL_1` is a small top-of-book stream (100/200/300) feeding `CLIENT_PRICE_NYC` with VWAP tiers 100/300/600, streamed down A_CLIENTS, XAUUSD only. `TRADEMAX_POOL_2` is full depth and the only price for XAGUSD/XCUUSD/XPTUSD/XPDUSD as well as XAUUSD, benchmarking `CLIENT_PRICE_B_NYC` down B_CLIENTS. Isaac noted Mahi offered to form the top-of-book stream itself and was turned down at the time. [permalink](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1784860298128599)
- 2026-07-23 — Commercial bar for this pilot: gold is #1 and FX secondary; what has to be demonstrated is zero operational risk plus skew PnL that stacks up. Andrew was dusting off a prototype graph-re-indexing skew-PnL build to get prod-ready numbers. [permalink](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1784795100232579)
- 2026-07-14 — Engagement with Bailey is slow and scheduling-bound (holiday, Singapore trip, "pretty busy"), and Andrew's read is that he "loves making decisions without the full set of information" — hence the push to get him on a call with the full picture before he settles on pausing. [permalink](https://mahifx.slack.com/archives/C03AP1L0Z7B/p1784015500397489)
