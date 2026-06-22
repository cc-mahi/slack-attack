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
  - {name: "Youssef Bouz", role: "client — CFD internalisation rollout; swap-free account queries; incident compensation messenger", confidence: low}
  - {name: "Layan", role: "client ops — reports Finalto gold fills for Compass adjustment", confidence: low}
  - {name: "Khalil", role: "senior GCC contact above Youssef; driving $70k cash compensation demand post-2026-05-15 XAGUSD incident", confidence: low}
last_catchup: 2026-06-22T07:15:50Z
---

## Recent issues

> [resolved] 2026-06-19 — 3,886oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 3,886oz gold long filled on Finalto at 15:09 BST; Rory acknowledged "Hi Layan, will do" at 15:22 BST; William confirmed "This is done now" at 15:26 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781878191313449)

> [resolved] 2026-06-17 — 4,416oz XAUUSD short filled on Finalto, Compass adjustment done
> Layan reported 4,416oz gold short filled on Finalto at 15:17 BST; William confirmed "this is done" at 15:20 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781705869811169)

> [resolved] 2026-06-16 — 2,336oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 2,336oz gold long filled on Finalto at 15:19 BST; William confirmed "this has been done" at 16:35 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781619554232999)

> [resolved] 2026-06-16 — Finalto defensive feed: 3 hedger order IDs queried; no Mahi action needed
> Nael asked about IDs 62616952, 98582117, 66229658 at 13:42 BST. William identified them as XAUUSD hedger trades sent to Finalto on 2026-06-15 at 12:14:20 UTC. Finalto had emailed GCC to say two new accounts were added to their Defensive Feed, citing those order IDs. Nael confirmed Finalto handles defensive feed filtering internally — no action required on Mahi side. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781613749969279)

> [resolved] 2026-06-15 — 5,212oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 5,212oz gold long filled on Finalto at 15:10 BST; Rory acknowledged at 15:10 BST; Rory confirmed "apologies delay on this one — this has now been actioned" at 09:33 BST on 2026-06-16. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781532606027979)

> [resolved] 2026-06-12 — 6,286oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 6,286oz gold long filled on Finalto at 15:11 BST; Rory acknowledged "Hi Layan, will do" at 15:12 BST; Nathan confirmed "this has been completed" at 00:03 BST on 2026-06-15. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781273515072669)

> [resolved] 2026-06-11 — XPTUSD abnormal spreads; config fix + pricer bounce resolved in ~20 min
> Nael reported XPTUSD spreads "not normal at all" and "very low" at 10:09 BST — LMAX and Finalto minimum spread showing 150+. Cameron Hughes bounced pricers at 10:19 BST to pick up MWMS changes for XPD and XPT, then made a config change to bring TOB ($2) in line with LP spreads (too-frequent widening), then reverted from pool pricing back to model pricing. Nael confirmed "much better now" at 10:27 BST. [client-permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781168985256809) [internal-bounce](https://mahifx.slack.com/archives/C09QS1NUA80/p1781169575044879)

> [resolved] 2026-06-10 — 736oz XAUUSD short filled on Finalto, Compass adjustment done
> Layan reported 736oz gold short filled on Finalto at 15:17 BST; William acknowledged "Hi Layan, adjusting" at 15:18 BST and confirmed "all done" at 15:21 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781101072404299)

> [resolved] 2026-06-09 — 5,342oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 5,342oz gold long filled on Finalto at 15:12 BST; William confirmed "sure" at 15:12 BST and "all done" at 15:14 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1781014342126009)

> [resolved] 2026-06-08 — 4,124oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 4,124oz gold long on Finalto at 15:12 BST; Rory acknowledged "will do" at 15:30 BST; William confirmed "done" at 17:29 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780927951026909)

> [resolved] 2026-06-08 — XAGUSD close-by adjustment: 30k LMAX stalled ~5 min; manual hedger backstop config fixed
> Nael submitted a 176,100oz XAGUSD close-by adjustment at ~09:07 BST; Finalto leg cleared in ~40s; LMAX cleared 146,100oz quickly then stalled on the final 30,000oz from ~08:04:30 to 08:09:55 UTC (completing 08:11:38 UTC). Nael flagged urgently at 09:07 BST; Rory responded and confirmed risk cleared; William explained the delay was due to spread-reducing logic and hedging throttle. Nael asked to disable hedgers while reviewing — William confirmed OK at 09:15 BST. Shyam posted root cause in internal channel at 06:39 BST on 2026-06-09: (1) `VAR-CLEARANCE` idled once ahead of schedule — parked 30k residual until schedule clock caught up ~5 min; (2) `BACKSTOP` spread cap = 2× base_spread(remaining) — at 30k that resolves to 0.032, below LMAX's ~0.039 silver spread, so backstop never fired. Fix deployed: time-laddered backstops added to both manual hedgers — wider spread tolerance the longer risk sits (Finalto: 200%/500% at 30s/60s; LMAX: 300%/800% at 30s/60s of base spread). [client-permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780906021922689) [root-cause](https://mahifx.slack.com/archives/C09QS1NUA80/p1780983580727989)

> [resolved] 2026-06-05 — 992oz XAUUSD + 10,000oz XAGUSD long filled on Finalto, Compass adjustments done
> Layan reported 992oz XAUUSD + 10,000oz XAGUSD filled on Finalto at 15:09 BST; William confirmed "that's done now" at 15:16 BST. Separately, Nael attempted to move 1,500oz XAUUSD from Finalto to LMAX via the CSV adjustment sheet but reported nothing happened. William checked Compass and found the positions were already correctly reflected in the manual adjustment books (+1.5k Finalto, -1.5k LMAX). Confusion about hedger state during adjustments; William held a huddle at 15:34 BST to clarify procedure. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780668561320359) [huddle](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780670075330379)

> [open] 2026-06-05 — XAGFUT/NG1FUT decimal mismatch: Finalto sends 4dp but rejects orders >3dp; workaround deployed
> William reported Finalto rejected a 5k XAG futures hedging order: Finalto sends 4dp market data for XAGFUT and NG1FUT but rejects limit orders with >3dp ("Price tag must not contain more than 3 decimal places"). William added 1-pip maxSlippage to hedger rules as a rounding workaround and cleared the risk; futures hedgers P+W bounced. GCC asked to raise with Finalto with priority to align decimal places across all instruments. Nael confirmed 15:12 BST Silver Futures is 3dp on Finalto UI, Silver Spot is 4dp (mismatch confirmed); Nael confirmed "will check with Finalto immediately". Finalto response not yet seen. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780655431818729) [internal-bounce](https://mahifx.slack.com/archives/C09QS1NUA80/p1780655879654819)

> [resolved] 2026-06-04 — 1599oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 1599oz gold long filled on Finalto at 15:12 BST; William acknowledged "Hi Layan, will do" at 15:12 BST and confirmed "Done" at 15:30 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780582340123069)

> [resolved] 2026-06-03 — 289oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan reported 289oz gold long filled on Finalto at 15:06 BST; William acknowledged "Hi Layan, yes we'll get that adjustment in" at 15:40 BST and confirmed "All done" at 15:42 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780497763685249)

> [open] 2026-06-02 — 1636oz XAUUSD long filled on Finalto, Compass adjustment pending
> Layan requested Compass adjustment for 1636oz gold long filled on Finalto at 15:12 BST; William acknowledged "Hi Layan, sure" at 15:12 BST but no completion confirmation in window. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780409523294259)

> [open] 2026-06-02 — A-book performance poor; root cause identified, no fix deployed
> William flagged at 14:35 BST on 2026-06-02: "A Book performance has been bad today as well, investigating this." Will Carter had also noted at 12:03 BST that volumes were "really struggling". Will Carter requested an update on 2026-06-03 09:22 BST. William responded 2026-06-03 14:57 BST: caused by very sharp flow going offside before 500ms — 3-10s delayed triggers on hedging meant flow went offside before hedging. PnL improved on 2026-06-03 with better flow, but William will "think about how it could be changed in the event of very toxic flow like this coming in". No config change deployed yet. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1780407303939239) [root cause reply](https://mahifx.slack.com/archives/C09QS1NUA80/p1780495057012879) [volumes](https://mahifx.slack.com/archives/C09QS1NUA80/p1780398232116689)

> [resolved] 2026-06-01 — 1331oz XAUUSD long filled on Finalto, Compass adjustment done
> Layan requested Compass adjustment for 1331oz gold long filled on Finalto at 15:51 BST; William confirmed "Hi Layan, sure" at 15:51 and "This is done" at 15:59 BST. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780325460256019)

> [open] 2026-05-27 — GCC demanding $70k cash compensation for 2026-05-15 XAGUSD incident; Mahi holding at 0% share offer
> Khalil (senior GCC contact above Yousef) is driving a $70k cash demand — 1:1 with the headline incident figure. Yousef has been the messenger. Will Carter posted a formal internal handover at 14:33 BST: Mahi's position is zero cash, 0% Mahi share on Skew, PSM and Brokered LR for the rest of the pilot until ~$25–30k of foregone PnL has accrued. Rationale: $70k exceeds total Mahi earnings from the relationship (~$54k across 3.5 months) and sets a cash precedent that would anchor the July renegotiation (target $360–600k/year). Will sent the formal response to Yousef on 2026-05-27 afternoon (full message text in thread), itemising the value-add ledger ($87.5k Skew PnL, $14k hedger savings, $12B internalised flow, Jan 31 cover) and the proportionality framing. Awaiting Yousef response; billing as normal in the meantime (cc: Nicole Vivian). Risks: Khalil escalating to David/Susan; GCC walking (account flagged at-risk in March 2026). Day-to-day coverage handover to Bonnie Cassidy and William Denny. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779888805588859) [response-text](https://mahifx.slack.com/archives/C09QS1NUA80/p1779888839513849)

> [open] 2026-05-26 — Tag 334513 gold futures orders rejected: auto-classified Arbitrageur, Finalto book too thin to broker
> Client (Nael) reported 4 gold futures orders for tag 334513 rejected 2026-05-26. William investigated: tag was auto-classified Arbitrageur due to consistent ~100ms yield drop pattern, so orders were attempted to be brokered; Finalto's order book was thin around the time and couldn't sweep sufficient quantity, so orders were cancelled. William offered to whitelist tag for internalisation but flagged PnL risk. Client asked to keep classification as Arbitrageur for now and will update if that changes. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779786760466559) [resolution](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779791095115839)

> [open] 2026-05-22 — EUR50 0.1-lot rejection recurs for tag 4004261; config fix pending distribution restart
> Nael reported tag 4004261 hitting a minimum-quantity rejection on EUR50 at 0.1 lots — same error as the 2026-05-21 EUR50 fix. William applied a further config change (min and increment set to 0.01 for E50EUR, inline with other indices) but noted it will only take effect after the next distribution restart. Restart not yet confirmed. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779473426190189) [resolution-reply](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779478899495639)

> [resolved] 2026-05-21 — EUR50 and indices quantity definitions corrected; OMXS30 setup deferred to weekend release
> Nael reported EUR50 order of 0.1 lots rejected — EUR50 had no quantity definition so was defaulting to increment=1, min=1. Nathan Burch updated EUR50 to increment=0.01, min=0.01. Nael then shared a full LMAX indices quantity spec table; Nathan audited all indices and updated J225/JPXJPY and AUS200/ASXAUD which had non-matching overrides. OMXS30 was not priced — Nathan added it to the codebase but confirmed it can only go into Compass at the next weekend release. All other indices in the list now match LMAX spec. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779397153018939) [resolution](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779419816310389) [OMXS30 deferred](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779421344026129)

> [open] 2026-05-21 — 4543oz XAUUSD long filled on Finalto, Compass adjustment requested
> Nael reported 4543oz gold long filled on Finalto at 15:20 BST; William acknowledged. Adjustment status not yet confirmed in window. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779373250103729)

> [resolved] 2026-05-20/26 — UKOFUT and USOFUT futures test-traded and hedged; commodities workflow confirmed
> William initiated futures test trades 2026-05-20: tested USOFUT, ran into hedger issue requiring a config change — had client close position, adjusted, re-tested, hedged OK. NG1FUT test trade sent ~17:54 BST; hedged successfully; client closed. UKOFUT/USOFUT were pending a restart to pick up a pricing change. 2026-05-26: William invited Nael to test UKOFUT first, made a config change, trade was placed and hedged, client closed; USOFUT then tested and hedged. William confirmed "the commodities workflow looks good" and stated he will make tweaks then switch to internalise. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779296193084449) [2026-05-26 test](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779791175876139)

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

> [resolved] 2026-05-06 — Fast-hedge for futures requested; all futures now internalising as of 2026-06-02
> Client asked for fast-hedge setup on futures ASAP — specifically tags 4004072 and 4004241 experiencing slippage on gold futures. 2026-05-13: metals + indices futures test-traded and switched to internalise. 2026-05-20: NG1FUT hedged successfully. 2026-05-26: UKOFUT/USOFUT test-traded and hedged. 2026-05-28: hybridHedgerFutsP1/W1 bounced for NG1 pip size change; further NG1FUT review needed. 2026-06-02: William bounced hybridHedgerFutsP1/W1 to add maxSlippage rule (force NG1FUT Finalto price to 3dp to avoid Finalto rejections); Nael (tag 4036) test-traded NG1FUT at ~10:27 BST — hedged successfully; William confirmed "will move that instrument to internalise as well now". Client confirmed "all futures now being internalised" — William confirmed yes. Crypto instruments promised as next step. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1778060389989769) [2026-06-02 NG1 go-live](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780392380808399) [NG1 internalise confirmed](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780392540340019) [all futures confirmed](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780392570055929)

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

- 2026-06-15 — Post-pilot deal framing: Will Carter noted positive PnL start to the week ("no slippage, fair-ish VWAPs for full-amount gold tickets") and outlined post-pilot commercial thinking: lock GCC in for a long-term deal with volume bands to capture growth, noting existing volumes constrain how much more can be charged but the system is now working well in the background. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1781512339189479)
- 2026-06-11 — XAU futures two large VaR spikes ($140k and $230k) then net +$8k; Rory flagged PnL drop alerts from futures-vs-spot reval mismatch: Cameron Hughes confirmed up $8k after two large XAU futures VaR spikes. Rory observed PnL drop alerts caused by futures momentarily being revalled against spot (same pattern as Amana) before correcting to contract price. Rory asked whether `reference.directMidMarkets` could suppress these false alerts — no response yet. [cam-internal](https://mahifx.slack.com/archives/C09QS1NUA80/p1781203245782619) [rory-alert](https://mahifx.slack.com/archives/C09QS1NUA80/p1781203645125219)
- 2026-06-09 — Time-laddered backstop fix deployed to both manual hedgers: Shyam added time-laddered spread tolerance to `VAR-CLEARANCE` and `BACKSTOP` rules (Finalto 200%/500%, LMAX 300%/800% at 30s/60s) after 30k XAGUSD stalled on LMAX for ~5 min during 2026-06-08 close-by. Prevents backstop from being priced out when quantity shrinks and base spread drops. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1780983580727989)
- 2026-06-02 — NG1FUT internalisation complete; crypto test trades promised next: William confirmed all futures now internalising; told Nael "We'll make sure the Crypto instruments are ready to test trade soon". [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780392614316269)
- 2026-06-02 — hybridHedgerFutsP1/W1 bounced for NG1FUT maxSlippage fix: force rounding of Finalto price to 3dp (priceFormatPip) to avoid raw TOB 4dp rejection. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1780391840837769)
- 2026-06-01 — LR on A_CLIENTS channel tuned: William reduced refresh rate from $250k/sec to $50k/sec (then walked back to $100k/sec as less aggressive) to lift LR from ~$1/M. Monitoring underway. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1780329833967329)
- 2026-05-29 — NZ bank holiday 1 June: Sam Hewitt posted standard advisory — Slack less monitored; emergency support via support@mahimarkets.com or London (+44 203 397 1985) / NZ (+64(3) 2880079) phone lines. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1780029481215959)
- 2026-05-28 — FXCubic client-feed throttle review: Youssef asked how many price ticks/sec GCC clients receive via their FXCubic FIX connection. William shared a stats CSV showing ~500/sec from Mahi to GCC, ~100/sec from both LMAX and Finalto. GCC currently throttles outbound to clients at 100ms (10/sec); Youssef asked whether reducing to 50ms or 10ms would improve client experience. William assessed: Finalto interval mean ~20ms / median ~2ms, no current evidence of stale-price rejections or arb — but proposed trial of 50ms then 10ms; client agreed to try next day. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779981594374659)
- 2026-05-27 — XAUUSD continuity pool P&L bump at market open (~22:00 UTC 2026-05-26): Daria flagged $5.5k P&L bump during the XAUUSD market open window. CLIENT_PRICE_INSTI_MAHI was not pricing (CLIENT_PRICE_INSTI_LDN forced indicative for 15 min after open, 30 min on Sunday, and closed for the last hour before weekend); GCC was publishing the continuity pool (Finalto). Finalto gave better fills than the model price — dist filled at published price + LR and P&L came from the difference. Daria also noted XAUUSD skew P&L took a non-real hit over this period. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779837414097499)
- 2026-05-21 — Bank holiday notice (Mon 25 May): Nia posted standard bank holiday advisory — Slack less monitored, emergency support via support@mahimarkets.com or London/NZ phone lines. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1779350401978569)
- 2026-05-19 — Dashboard deploy coordinated for gcc-brokers: Justin Young pushed new columns (LR execution rule breakdown); Leonardo Borsi deployed after Kate/Will cleared config work. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779204790064199)
- 2026-05-18 — UI improvement planned after 2026-05-15 incident: Justin Young picked up Will Carter's request to make process restart prompts more obvious. Post-save modal will trigger when `hedging.*`, `pricing.*`, or `distribution.*` non-dynamic config is edited, listing affected processes with inline restart action. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1779085027341739)
- 2026-05-15 — Liam Cordelle noted Claude Code was not useful for diagnosing the hybridHedger incident: 2+ hours spent by Will, Kate, and Liam trying to coax Claude sessions out of false assumptions; only resolved when Will checked Config Audit directly. [permalink](https://mahifx.slack.com/archives/C09QS1NUA80/p1778855033172619)
- 2026-05-01 — Bank holiday notice (Mon 4 May): Nia posted standard Mahi bank holiday advisory — Slack less monitored, emergency support via support@mahimarkets.com or London/NZ phone lines. [permalink](https://mahifx.slack.com/archives/C09PNC1MFAA/p1777622406041909)
- 2026-04-23 — "Crypto later?" — William agreed to follow-up session with client on crypto setup after CFD list sign-off.
