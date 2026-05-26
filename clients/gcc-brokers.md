---
slug: gcc-brokers
refs:
  vibepulse: ../VibePulse/.claude/clients/gcc-brokers.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: gcc-brokers
  hosts: ../MahiProduct/data/client-hosts.json          # entry: gcc-brokers
  wiki: null                                             # ../MahiProduct/wiki/clients/gcc-brokers.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Carl", role: "client ops / LMAX + Finalto mappings", confidence: low}
  - {name: "Nael", role: "client trading ops", confidence: low}
  - {name: "Youssef Bouz", role: "client — CFD internalisation rollout; swap-free account queries", confidence: low}
  - {name: "Layan", role: "client ops — reports Finalto gold fills for Compass adjustment", confidence: low}
last_catchup: 2026-05-26T07:05:02Z
---

## Recent issues

> [open] 2026-05-22 — EUR50 0.1-lot rejection recurs for tag 4004261; config fix pending distribution restart
> Nael reported tag 4004261 hitting a minimum-quantity rejection on EUR50 at 0.1 lots — same error as the 2026-05-21 EUR50 fix. William applied a further config change (min and increment set to 0.01 for E50EUR, inline with other indices) but noted it will only take effect after the next distribution restart. Restart not yet confirmed. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779473426190189) [resolution-reply](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779478899495639)

> [resolved] 2026-05-21 — EUR50 and indices quantity definitions corrected; OMXS30 setup deferred to weekend release
> Nael reported EUR50 order of 0.1 lots rejected — EUR50 had no quantity definition so was defaulting to increment=1, min=1. Nathan Burch updated EUR50 to increment=0.01, min=0.01. Nael then shared a full LMAX indices quantity spec table; Nathan audited all indices and updated J225/JPXJPY and AUS200/ASXAUD which had non-matching overrides. OMXS30 was not priced — Nathan added it to the codebase but confirmed it can only go into Compass at the next weekend release. All other indices in the list now match LMAX spec. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779397153018939) [resolution](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779419816310389) [OMXS30 deferred](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779421344026129)

> [open] 2026-05-21 — 4543oz XAUUSD long filled on Finalto, Compass adjustment requested
> Nael reported 4543oz gold long filled on Finalto at 15:20 BST; William acknowledged. Adjustment status not yet confirmed in window. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779373250103729)

> [open] 2026-05-20 — NG1FUT fast-hedge tested; USOFUT/UKOFUT testing deferred pending restart
> William initiated futures test trades 2026-05-20: tested USOFUT (USOFUT), ran into hedger issue requiring a config change — had client close position, adjusted, re-tested, hedged OK. NG1FUT test trade sent ~17:54 BST; hedged successfully; client closed. UKOFUT/USOFUT still pending a restart to pick up a pricing change — William confirmed "pending USOIL, UKOIL — should be good to test after restart yes?" Client confirmed. Status: NG1 hedged and verified; UKOFUT/USOFUT restart still needed before those can go live. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779296193084449)

> [resolved] 2026-05-19 — LR caps bumped to 250; XAGUSD skew PnL tracking updated
> Will Carter identified classified LR had caps at 0.000001 $/m (described as "Pepperstone-style settings at a broker doing 0.5% of Pepperstone volumes"), bumped all LR caps to 250 ahead of contract renegotiation. XAGUSD skew PnL tracking updated by Kate to reflect actual PnL since internalisation was turned on. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779204726386989) [XAGUSD skew update](https://mahifx.slack.com/archives/C09QS1NUA80/p1779206206868889)

> [open] 2026-05-19 — Mahi to forgo value-add share for pilot duration following 2026-05-15 incident
> Will Carter confirmed Mahi will forgo its share of value-add for the duration of the pilot to make the client whole on the ~$70k loss from the 2026-05-15 XAGUSD hedging incident. Noted value-add figures are "plummeting in May" — Kate Stagg is owning the fix. Client described as "at risk" by Will. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779182527592749)

> [resolved] 2026-05-18 — Post-mortem published; hybridHedger1 max market position config stripped and bumped
> Kate published post-mortem PDF for 2026-05-15 XAGUSD incident. Daria bumped max market position for XAGUSD to 100k (legacy config from Jan emergency hedging; was 7,500 — became binding when XAGUSD switched to internalisation). Will Carter subsequently suggested removing it entirely; confirmed in thread. Kate also stripped the max market position XAU/XAG config and bounced hybridHedger1 on 2026-05-18. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779101281240979) [max pos bump](https://mahifx.slack.com/archives/C09QS1NUA80/p1779051773373389)

> [resolved] 2026-05-18 — 6710oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 6710oz gold long filled on Finalto at 16:26 BST; William confirmed "all done" at 16:32 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779117985727249)

> [resolved] 2026-05-15 — XAGUSD ~45k oz unhedged for ~90 mins; ~$70k client loss; root cause: stale max market position cap
> Nael reported 45,200oz XAGUSD long + 128oz XAUUSD short not hedged ~30 mins at 11:25 BST. Rory and Kate declared high urgency; hedger turned off at 11:45 BST to trade out of positions. Client PnL swung from +$12k to -$60k (later scoped as ~$70k by Will). Root cause (Will Carter, ~14:35 BST): Nathan had raised the XAGUSD FINALTO `maximumMarketPosition` override from 7,500 to 20,000oz on 2026-05-13 ~22:47 UTC, but hybridHedger1 had not been restarted since 2026-05-10 06:33 UTC — the cap is loaded once at startup from an ImmutableTable, so the running hedger was still operating on the old 7,500oz cap. Flow filled the FINALTO bucket; backstop rule was LMAX-only on the offer side; LMAX spreads widened during the 09:50 BST sell-off (XAG $77.4→$76.89 in 30s, 5×5000oz client buys); backstop had nowhere to route and parked ~$45k→$45.7k oz for ~90 mins. Second contributing factor: backstop `Aggressive-XAGUSD` rule had a 2×BaseSpread max-spread constraint — Kate widened to 10× during the incident. XAGUSD PnL reported as turning from +$12k to -$60k. PagerDuty High-VaR alert (17943 VaR, CRITICAL) fired during the incident. Youssef Bouz expressed strong frustration to Will Carter ("80k off our P&L … due to a silly misconfiguration … unacceptable"). Post-incident actions: restart loaded 20k cap; property to be made hot-reload; alert added for cap-value divergence; Justin Young picking up UI change to prompt process restarts after non-dynamic config saves. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778842025992969) [root cause](https://mahifx.slack.com/archives/C09QS1NUA80/p1778851998984029) [Nathan override](https://mahifx.slack.com/archives/C09QS1NUA80/p1778712459189179)

> [resolved] 2026-05-15 — 368oz XAUUSD long filled on LMAX, Compass adjustment done
> Nael reported 368oz gold long filled on LMAX at 19:58 BST; Cameron Hughes actioned. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778871535032839)

> [resolved] 2026-05-15 — Will Carter investigated and resolved issue for Youseff; call made
> Will Carter identified a problem and called Youseff directly at ~14:37 BST to resolve. Issue resolved before call. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778852277364829)

> [resolved] 2026-05-14 — XAGUSD switched to internalisation + fast-hedge; 7149oz gold Compass adjustment done
> William confirmed XAGUSD internalisation go-live after reviewing Echo yield profiles showing past month's flow as suitable. Bounce of futures hedgers at 09:38 BST to pick up oil futures. Daria shared hedger performance stats: XAUUSD ~$13k savings ($71/M), XAGUSD ~$920 ($59/M) since rollover-hedgers were added. Nael reported 7149oz XAUUSD long on Finalto at 15:12 BST; Rory confirmed actioned at 15:24 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778754219771339) [savings](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778731913293849) [Compass adjust](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778767936951789)

> [resolved] 2026-05-13 — Metals + indices futures hedging tested; metals and indices futures switched to internalise
> Extended futures test trading session 2026-05-13 ~17:44–18:56 BST: XAU future, XAG future, DOW future, NDX future, SPX future, DAX future — all tested and hedged. William confirmed "all hedging tested for metals and indices futures; switching flow to internalise on those now". Client asked about USOIL, UKOIL, NGAS commodity futures — William confirmed "hedger setup nearly complete for the commodities, ready to test trade soon". Bounced hedger during session to pick up riskQuantisationOverride for futures indices. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778695014614019)

> [resolved] 2026-05-13 — Compass position divergence on metals; 15k XAUUSD LP limit hit; positions reconciled
> Carl reported stuck volume from close-by process at 21:25 BST. Daria found Compass XAUUSD positions had diverged (15k limit on XAUUSD positions at any one LP — positions diverged since XAGUSD switching to internalisation). Raised LP limit with client permission; position snapshot provided by Carl (XAUUSD: Finalto 65, LMAX 0, Client 65; XAGUSD: Finalto 111049, LMAX 124900, Client 235949). Nathan confirmed positions reconciled by 23:33 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778703945959439) [reconciled](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778711637266609)

> [resolved] 2026-05-07 — CO1USD, CL1USD and CFD Indices switched to live internalisation
> William proposed the go-live switch at 13:37 BST; client confirmed at 14:22 BST; William confirmed "all done" at 14:27 BST. Covers CO1USD, CL1USD, and all previously-tested indices (ASXAUD, G30EUR, F40EUR, JPXJPY, UKXGBP, NDXUSD, DOWUSD, SPXUSD). Pricers bounced at 11:22 BST to pick up XAU signals change ahead of the switch. William noted futures fast-hedge setup is still in progress (separate entry). [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778157450972219) [pricers bounce](https://mahifx.slack.com/archives/C09QS1NUA80/p1778149361517089)

> [resolved] 2026-05-07 — 6718oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 6718oz gold long filled on Finalto at 16:39 BST; William confirmed adjustment done at 16:58 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778168396858199)

> [resolved] 2026-05-06 — 116oz XAUUSD long filled on Finalto, Compass adjustment done
> Client reported 116oz gold long filled on Finalto at 15:05 BST; William confirmed booked at 16:26 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778076310926249)

> [open] 2026-05-06 — Fast-hedge for futures requested; tags 4004072/4004241 slipping on gold futures
> Client asked for fast-hedge setup on futures ASAP — specifically tags 4004072 and 4004241 are experiencing slippage on gold futures. William acknowledged aim to deliver and will keep updated; no timeline given. 2026-05-07: client reiterated "Yes please important for the futures" after go-live of CFD Indices; William confirmed "Futures setup still in progress, will let you know when that's ready to go". 2026-05-12: William confirmed "restructuring existing futures workflow to enable fast hedging — couple more restarts needed". 2026-05-13: metals + indices futures test trades completed; flow switched to internalise (see separate entry). 2026-05-20: USOFUT and UKOFUT tested; NG1 test hedged successfully; UKOFUT/USOFUT pending restart for pricing change. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778060389989769) [2026-05-12 update](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778576488756259) [2026-05-20 test](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779267185575169)

> [resolved] 2026-05-06 — XAGUSD false FI PnL drop on A_CLIENTS (Nathan investigation)
> Nathan flagged a Graphite signal showing a FI PnL drop on XAGUSD for A_CLIENTS on 2026-05-05. Investigated and confirmed false alarm — XAGUSD is not skewed for A_CLIENTS; only XAUUSD is. Nathan noted that only XAUUSD skew on A_CLIENTS should be reported/billed. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1778107331037799)

> [resolved] 2026-05-05 — 1251oz XAUUSD long filled on Finalto, Compass adjustment done
> Nael reported 1251oz gold long filled on Finalto at 15:04 BST; William confirmed adjustment complete at 15:39 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777989872967679)

> [resolved] 2026-05-05 — UKXGBP riskQuantisationOverride fix; hybridHedgerCFD1 bounced
> William identified that small UKXGBP test positions were not fulfilling the `minRisk` quantity needed to activate VaR triggers. Applied a change to `hedging.risk.riskQuantisationOverride` for UKX in Compass config, then bounced `hybridHedgerCFD1` to pick it up. Related to ongoing CFD internalisation testing. [internal-config](https://mahifx.slack.com/archives/C09QS1NUA80/p1777995611679109) [bounce](https://mahifx.slack.com/archives/C09QS1NUA80/p1777995516640649)

> [open] 2026-05-04 — Counterparty 4004089 reclassified to Dynamic Signal Follow after ABook PnL drop
> A-book XAUUSD PnL dropped ~$2,700 at 10:20 UTC as counterparty 4004089 traded ahead of a large price move (internalised; market moved against). After a second similar event, 4004089 was reclassified to Dynamic Signal Follow (now brokered). Counterparty 700154 then placed a similarly-sized internalised XAUUSD trade; market moved in Mahi's favour and ~$2,500 was recovered. Reclassification appears actioned; no follow-up confirmation of stability. [internal](https://mahifx.slack.com/archives/C09QS1NUA80/p1777949002875889)

> [open] 2026-05-04 — Fast-hedge strategy proposed for counterparty 700154; swap-free viability questioned
> Cameron Hughes shared yield profile for counterparty tag 700154 (Echo access issue resolved after permissions fix): stays onside for 16 mins in aggregate, making it suitable for fast-hedge (hold risk up to 5 min, let arb hedger chip away, clear via hybrid). Youssef raised concern that this client's high volume is tied to a swap-free offer, which may erode the edge — estimated XAUUSD spread margin ~$20/M and FX ~$11/M. Daria noted analysis needed on whether positions are held overnight vs closed intraday, plus swap charge quantum, before concluding viability. No resolution yet. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777908996386319) [Daria analysis](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777931713192039)

> [resolved] 2026-05-01 — CFD internalisation live testing: all instruments confirmed and switched live 2026-05-07
> Client confirmed routing split: Futures + Spot Commodities (USOIL/UKOIL/NGAS) → Finalto only; Spot Indices + CFD Crypto → LMAX only (Finalto has no CFD Indices; crypto offer on Finalto deemed poor). Shyam set up MAHI_LP_CFD proxy (VELOCITY_EXINITY + LMAX) for CFD pricing. William bounced hybridHedgerCFD1 to pick up CO1USD and CL1USD additions; initial CL1USD test hedged to LMAX (wrong), fixed mapping, re-tested to Finalto. CO1USD also confirmed Finalto. DOWUSD, NDXUSD, SPXUSD tested to LMAX — all confirmed. JPXJPY, UKXGBP also confirmed during testing session. ASXAUD test position opened and subsequently closed (confirmed "done" by client 2026-05-01 ~17:13 BST). G30EUR and F40EUR deferred to next week — markets closed over bank holiday weekend. NG1USD flagged internally as third Finalto commodity — mapping not yet complete. 2026-05-05: UKXGBP riskQuantisationOverride fix applied (small positions were not satisfying minRisk to activate VaR triggers); hybridHedgerCFD1 bounced again. 2026-05-06: G30EUR and F40EUR test trades completed by client (14:46 BST); F40EUR hedged by William, client closed position; G30EUR position also closed. Pricers and hybridHedgerCFD1 bounced for CFD benchmark normalisation change at 10:54 BST. William stated "ready to go live with the Indices" pending these tests — indices go-live appears imminent. Remaining open: NG1USD Finalto mapping and fast-hedge setup for futures (separate entry). [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777636046504329) [internal](https://mahifx.slack.com/archives/C09QS1NUA80/p1777635124504809) [ASXAUD close](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777653635607519) [G30EUR/F40EUR tests done](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778061056321559)

> [resolved] 2026-04-30 — 7230oz XAUUSD long filled on Finalto, Compass adjustment needed
> Carl reported 7230oz gold long filled on Finalto at 21:56 BST; Shyam adjusted Compass positions to match at 01:13 BST 2026-05-01. Carl confirmed "Perfect thanks". [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777559404368639)

> [resolved] 2026-04-30 — Daria ran manual hedger training call with Carl and Nael
> Daria huddled with Nael/Carl to walk through XAUUSD manual hedging process (hybridHedgerManualFinalto1 + hybridHedgerManualLmax1). Daria confirmed Carl and Nael watched the process, then operated XAGUSD hedger themselves — "should be able to leave it with them from now on". Total XAUUSD spread on the training session was $360 averaging $21/M vs Nathan's estimate of $219/M — saving est. $3.3k vs unhedged. Hedgers left enabled post-session. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777581628461159) [internal](https://mahifx.slack.com/archives/C09QS1NUA80/p1777585361762089)

> [resolved] 2026-04-24 — 1599oz XAUUSD long filled on Finalto, Compass adjustment needed
> Nael reported 1599oz gold long filled on Finalto; William to adjust Compass position. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777020863581119)

> [open] 2026-04-23 — LMAX XAUUSD feed still throttled to ~10/sec after requested 100/sec uplift
> Daria asked for LMAX feed throttle uplift from 10/sec (1 per 100ms) to 100/sec to improve hedging in fast markets. Client applied 100/sec ~04:59 BST, but Mahi still seeing <10/sec as of 11:43 BST — William suspects EOD restart needed on Mahi side; asked Carl to also recheck throttle on LP side. No further mention in window. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776908972956929)

> [resolved] 2026-04-23 — CFD internalisation go-live instrument list proposed
> Will proposed initial indices for CFD hedging go-live: ASXAUD, G30EUR (DE40), STXEUR, F40EUR, JPXJPY, IBXEUR, UKXGBP, NDXUSD, DOWUSD, SPXUSD, E50EUR. Awaiting Youssef confirmation. Now superseded by 2026-05-01 live testing run — routing split confirmed and testing commenced. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776957653145169)

> [resolved] 2026-04-23 — NG futures orders rejected (distribution quantity set to 500)
> Carl's 1k-quantity NG futures orders rejected; Shyam identified the distribution qty was capped at 500 vs Finalto min 10k. Normal-quantity bumped to 10k; distribution gateway restart scheduled for EOD. NGASM6→NGM6 mapping confirmed active. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1776900791650569)

## Notable topics

- 2026-05-21 — Bank holiday notice (Mon 25 May): Nia posted standard bank holiday advisory — Slack less monitored, emergency support via support@mahimarkets.com or London/NZ phone lines. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779350401978569)
- 2026-05-19 — Dashboard deploy coordinated for gcc-brokers: Justin Young pushed new columns (LR execution rule breakdown); Leonardo Borsi deployed after Kate/Will cleared config work. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779204790064199)
- 2026-05-18 — UI improvement planned after 2026-05-15 incident: Justin Young picked up Will Carter's request to make process restart prompts more obvious. Post-save modal will trigger when `hedging.*`, `pricing.*`, or `distribution.*` non-dynamic config is edited, listing affected processes with inline restart action. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779085027341739)
- 2026-05-15 — Liam Cordelle noted Claude Code was not useful for diagnosing the hybridHedger incident: 2+ hours spent by Will, Kate, and Liam trying to coax Claude sessions out of false assumptions; only resolved when Will checked Config Audit directly. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1778855033172619)
- 2026-05-01 — Bank holiday notice (Mon 4 May): Nia posted standard Mahi bank holiday advisory — Slack less monitored, emergency support via support@mahimarkets.com or London/NZ phone lines. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777622406041909)
- 2026-04-23 — "Crypto later?" — William agreed to follow-up session with client on crypto setup after CFD list sign-off.
