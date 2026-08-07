---
slug: gtcfx
refs:
  vibepulse: null                                          # no ../VibePulse/.claude/clients/gtcfx.yaml yet (pre-live)
  billing: null                                            # not yet in ../MahiProduct/data/billing/clients.json
  hosts: ../MahiProduct/data/client-hosts.json             # entry: gtcfx (s3Slug GTCFX; LDN)
  wiki: null                                               # ../MahiProduct/wiki/clients/gtcfx.md (not yet)
  onboarding: ../MahiProduct/data/onboarding/gtcfx.json    # stage tracker
channels_override: [internal-gtcfx, mahi-gtcfx]            # no VibePulse yaml to resolve from
key_people_overrides:
  - {name: "Manglai", role: "GTC — main day-to-day counterpart; owns pricing sign-off, the OZ fee negotiation, and the go-live date"}
  - {name: "Marios Lysandrou", role: "GTC — supplies group mappings / instrument specs; sets up connections with OneZero"}
  - {name: "Andreas", role: "GTC — joined the Compass/Echo walkthrough", confidence: low}
  - {name: "Jack Zheng", role: "GTC — CEO; Mahi sent a personal message to reinforce the pitch 2026-07-30", confidence: low}
  - {name: "Ralich", role: "OneZero — agreed to waive OZ's per-million fees on GTCFX flow to Mahi; David Cooney's contact", confidence: low}
  - {name: "Lochlan", role: "OneZero — alternative escalation route if the fee negotiation stalls (internal only, not shared with GTC)", confidence: low}
last_catchup: 2026-08-07T07:10:36Z                         # ISO8601; updated by /catchup
---

## Status

- **Stage:** pre-live, go-live targeted 2026-08-10/11 (Manglai, 2026-07-28; delay reason unstated, he's on holiday until then). Signed 2026-05-14. Listed under "Signed but not yet live" in `../MahiProduct/data/fleet.txt`.
- **Integration:** LDN only (`gtcfx-ln-admin-1.zlt5`), on 3 Beeks hosts repurposed from trademax (freed by the trademax LDN→NYC region swap, 2026-05-04), cluster zlt5 / cage LD5. Agreed flow: GTC MT4/5 → GTC OneZero hub → Mahi (A/B book) → GMG (FCA entity) → HRP & LPs for hedge flow. Hedged flow routes to Finalto and Swift, STP'd flow to HRP LPs; HRP stays STP-only at GTC's preference. Spreads benchmarked on FINALTO/SWIFT with `MAHI_BENCHMARK_LDN|FINALTO|HRP_XTX|HRP_MEX|HRP_ARG` mid formation and adaptive mid on signalled markets. A Book exec rules split ABOOK (standard) / ABOOK_TX (toxic); GTC agreed Mahi can risk-manage on classification. ~2,900 MT groups, so per-group trading-account mapping was abandoned in favour of A/B trading accounts with the Compass classifier setting last-look window, LR params and STP pool per counterparty.
- **Risks / open threads:** GMG is still on PrimeXM, which Mahi flags as a system-integrity problem in the agreed path and wants moved. `marketDataProxyTx` won't start without listen config and may be an obsolete HRP_ARG proxy. Counterparty tags still missing on the B Book connections. Design questions unresolved from 2026-07-15: failover, whether HRP can be included in A Book hedging, NOP limits on Finalto/Swift/HRP, and whether LR belongs in the published price (global vs per-channel).
- **Relationship:** warm and actively managed — David Cooney has the OneZero/Ralich relationship (Ralich cleared Mahi risk-management on joint Mahi/OZ clients, on condition it isn't broadcast); Kate Stagg runs day-to-day; message reinforced to CEO Jack Zheng on the weekly call and well received.

## Recent issues

> [open] 2026-08-03 — `marketDataProxyTx` won't start; needs listen config and may be obsolete
> Daria found the process needs a `connectivity.marketData.proxy.listen` config to start up, then noted to Isaac that it looks like it was configured to proxy out HRP_ARG and asked whether the process is still needed at all given how long it's been. Unanswered. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1785713908035349)

> [open] 2026-07-31 — GMG still on PrimeXM — system-integrity concern in the agreed flow path
> David relayed the confirmed path (GTC MT4/5 → GTC OZ hub → Mahi A/B → GMG as FCA entity → HRP & LPs for hedge flow) and flagged that GMG remaining on PrimeXM "introduces some system integrity issues for us", asking for support in moving that business over. No plan yet. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1785484125462009)

> [open] 2026-07-29 — Go-live targeted 10–11 Aug; Manglai declined to start earlier
> Manglai confirmed a 10–11 August target and said he's happy with pricing after the spread changes. Kate asked what's driving the delay and offered to help speed it up, but he's on holiday for a week from Wednesday and wants to go live once he's back — he'd already pushed back on Kate's suggestion of getting the B Book live on 2026-07-28. [go-live-date](https://mahifx.slack.com/archives/C0AKAPLU78W/p1785317790537099) [pushback](https://mahifx.slack.com/archives/C0AKAPLU78W/p1785164995327769)

> [open] 2026-07-28 — CBCX added as a further LP; instrument spec requested before test trades
> GTC sent credentials for one more LP (CBCX) via onetimesecret. Kate confirmed Mahi is connected and receiving market data, and asked for CBCX's instrument spec (minimum and incremental quantities, pricing precision) before test trades can run. [permalink](https://mahifx.slack.com/archives/C0AKRP8C049/p1785225476074889)

> [open] 2026-07-27 — Counterparty tags not arriving on the B Book connections
> Kate flagged that Mahi isn't receiving counterparty tags on the B Book connections and asked GTC to check. Same class of problem as the A Book tags, which were confirmed working 2026-07-24. Still open at window close. [permalink](https://mahifx.slack.com/archives/C0AKRP8C049/p1785153727058559)

> [open] 2026-07-24 — Connection test matrix still incomplete
> As of Kate's status: A-book all 4 sessions logged on (OZ 1/2/3, PXM), B-book only the 3 OZ sessions — B-book PXM not yet brought up on GTC's PrimeXM side. Tested and filling cleanly: A-book OZ 2, B-book OZ 1 and OZ 2. Still to test: A-book OZ 1, OZ 3 and PXM; B-book OZ 3 plus PXM once connected. GTC said 2026-07-27 they'd restart PXM that night and start with one feed. [permalink](https://mahifx.slack.com/archives/C0AKRP8C049/p1784903945431349)

> [open] 2026-07-15 — Design questions still unresolved ahead of go-live
> Isaac's list needing discussion: failover; whether Mahi can hedge with HRP via the hybrid and arb hedgers on the A Book to improve hedging yields (parkable until live, but worth confirming the reason either way); NOP limits on Finalto, Swift and HRP; and whether the A Book price needs to match the B Book price — i.e. whether LR goes in the published price, which changes whether LR is configured globally or per channel (currently published and configured differently per channel). None closed in this window. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1784087993240829)

> [resolved] 2026-07-28 — OneZero waiving its per-million fees on GTCFX flow to Mahi — unblocks the B Book
> David: "OZ are going to waive the fees for GTCFX to send flow to us", per Ralich, and it applies to any joint Mahi/OZ client. Two conditions: don't tell the street, and OZ doesn't want brokers concluding they can plug in any risk-management system ("well if mahi can, why can't i use my dodgy system?"). OZ also wanted a day or two before communicating it to GTC. This resolves the headline commercial blocker from 2026-07-14. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1785244660200009)

> [resolved] 2026-07-28 — ~2,900 MT groups: per-group mapping dropped for classifier-driven A/B treatment
> Kate asked for a group count after receiving the mapping spreadsheet, on the basis that Compass trading accounts want to be a small stable set. Marios came back with ~2,900 groups. Kate's call: define trading accounts as just A Book and B Book and let the Compass classifier set the treatment within each — last-look window, LR parameters, and which STP pool a counterparty routes to — driven by each counterparty's observed behaviour, so new accounts are covered from their first trades with no mapping to maintain either side. Offered direct config or a nominated FIX connection for any counterparties GTC has already identified as toxic. Explicitly not a blocker on the B Book go-live. [decision](https://mahifx.slack.com/archives/C0AKRP8C049/p1785248933790659) [internal-note](https://mahifx.slack.com/archives/C0AKAPLU78W/p1785249094102019)

> [resolved] 2026-07-27 — Spread tweaks after pricing feedback; Manglai satisfied
> Following a call on pricing feedback and rollout plan: reduced EURUSD, USDJPY and GBPUSD top-of-book spreads and altered the benchmark markets. Kate posted the changes for review in the client channel; Manglai confirmed 2026-07-29 he's happy with how pricing looks post-call. He's keen to start with GBPUSD (having earlier favoured EURUSD). [call-notes](https://mahifx.slack.com/archives/C0AKAPLU78W/p1785164995327769) [client-post](https://mahifx.slack.com/archives/C0AKRP8C049/p1785165048362269)

> [resolved] 2026-07-21 — First successful distribution test trades
> XAUUSD fill against counterparty 50005 on DISTRIBUTION_LDN. Remaining distribution connections scheduled for the next day; those needed a bridge restart and resumed 2026-07-23 after Kate chased Manglai in DM. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1784648873374399)

> [resolved] 2026-07-21 — Compass/Echo walkthrough; GTC agreed to classification-based risk management
> Call with Manglai, Andreas and Marios to walk through the Compass and Echo pages. Outcomes: HRP stays as STP markets with Swift/Finalto for hedging rather than being added to hedger execution markets; GTC happy for Mahi to risk-manage on classification, so execution rules move to STP for signal-follow and broker-classified; go-live likely on A Book flow first. Two loose ends — they couldn't load the automation page (possibly a read-only account-type limitation), and the analytics bridge is set up for 2 MT4 + 2 MT5 servers when GTC has several more. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1784642434185129)

> [resolved] 2026-07-15 — LP test trades rejected across Finalto, HRP_ARG and Swift
> Three separate rejects on the first LP test trades: Finalto `58=Invalid account id specified`, GMG_MAHI_HRP_ARG `58=REJECT: symbol not found: instrument=XAUUSD`, Swift `58=Invalid Account`. Root causes were account IDs and stream naming on GTC's side (they'd sent `GMG_MAHI_HRP_NZBank stream` where the account should have been `GMG_MAHI_HRP_NZBank`). HRP orders came good once Mahi set the `.e` suffix on the orders connection. [finalto-reject](https://mahifx.slack.com/archives/C0AKRP8C049/p1784045811733799) [hrp-fixed](https://mahifx.slack.com/archives/C0AKRP8C049/p1784076394388489)

> [resolved] 2026-07-15 — Graphite disk full; process memory raised to the Pepperstone benchmark
> Isaac bumped Graphite from 68 GB to 138 GB after it filled, and raised process memory to match Pepperstone as the benchmark given expected flow. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1784089836383919)

> [resolved] 2026-07-14 — OZ per-million STP fee on B Book flow: A Book first, B Book pending
> Kate's call notes: OneZero charges a per-million fee on A Book flow, and if GTC STP'd their B Book flow to Mahi the monthly cost would be very high. Mahi's suggestion was separate A/B Book connections so OZ can differentiate and cut a deal. Mahi also offered pricing-only for B Book so GTC could still get skew, but Manglai wants execution too. Decision: go live on A Book first while the B Book fee discussion runs. Superseded by the 2026-07-28 fee waiver. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1784026634191269)

> [resolved] 2026-07-14 — HRP whitelisting cleared; HRP streams pricing
> Mahi had been waiting on HRP whitelisting for prime-broker LPs since 2026-07-06 (blocking better reference-mid selection and possible inclusion in hedging); Isaac chased Marios and confirmed HRP streams pricing on 2026-07-14. [awaiting](https://mahifx.slack.com/archives/C0AKAPLU78W/p1783555252360509) [pricing](https://mahifx.slack.com/archives/C0AKAPLU78W/p1784003984500439)

## Notable topics

- 2026-07-27 — Value evidence shared with the client: running flow-predictive skew off the drop copies already set up, Mahi told GTC that in the ~12 hours since market open, had they been executing on Mahi's price, that was **$200k of skew P&L on XAUUSD alone** — and off the PXM drop copy only. Got an :eyes: reaction and no pushback. [permalink](https://mahifx.slack.com/archives/C0AKRP8C049/p1785149280652629)
- 2026-07-14 — Volume shape explains the fee fight: A Book is 8–10 yards/month, B Book around 800 yards/month. The B Book is where essentially all the value sits, which is why the OZ per-million STP fee was the headline blocker rather than a detail. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1784026634191269)
- 2026-07-28 — The OZ fee waiver is precedent-setting and deliberately quiet: it covers any joint Mahi/OZ client, but OZ asked Mahi not to publicise it, specifically to avoid other brokers concluding that any risk-management system can be plugged in. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1785244685921069)
- 2026-07-15 — Lochlan at OneZero is held as an internal escalation backchannel if Manglai's own OZ negotiation stalls — Will's note explicitly says not to tell GTC that route exists. [permalink](https://mahifx.slack.com/archives/C0AKAPLU78W/p1784113367405529)
