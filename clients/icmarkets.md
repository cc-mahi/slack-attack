---
slug: icmarkets
aliases: [icmarkets-crypto]
refs:
  vibepulse: ../VibePulse/.claude/clients/icmarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: icmarkets-crypto
  hosts: ../MahiProduct/data/client-hosts.json          # entry: icmarkets
  wiki: null                                             # ../MahiProduct/wiki/clients/icmarkets.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Pavlos Elpidorou", role: "IC Markets Head of Market Risk (Compass/Echo user)"}
  - {name: "Joanna Theophanous", slack_handle: "i.theophanous", role: "IC Markets ops/client-side contact", confidence: low}
  - {name: "Kyriakos", role: "IC Markets — requested toxic execution account list; first name only seen", confidence: low}
  - {name: "Dimitrios Lambrou", role: "IC Markets — joined mahi-ic-markets channel 2026-05-18; role unknown", confidence: low}
  - {name: "Karam", role: "IC Markets — queries execution profiles and Echo dashboards; first name only seen", confidence: low}
last_catchup: 2026-05-25T07:20:48Z
---

## Recent issues

> [resolved] 2026-05-22 — Trade rejection/cancellation query from Michalis; logs expired, root cause untraced
> Michalis (IC side) asked why a trade from 2026-05-14 was rejected/cancelled (image shared). [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1779435759721649) Rory King investigated: order was cancelled because time-in-force was sent as GTC. Michalis pushed back — the requested price was available at the time. Rory dug further but could not find the trade in Mahi's system, and logs for May 14 had since expired. Advised IC to report similar occurrences promptly so the workflow can be traced in real time. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1779446588534029) No further follow-up in window.

> [resolved] 2026-05-22 — Tag 7902035 LR resistance: machine-gunning orders to avoid VWAP spread
> Karam (IC side) asked whether Mahi switches accounts automatically between execution profiles, referencing tag 7902035. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1779457354165619) Will Carter explained classification-based liquidity depletion rules; Cameron Hughes confirmed tag 7902035 is not on the classified depletion list but is subject to default LR rules. Tag was machine-gunning orders in milliseconds to avoid paying VWAP spread — system applied LR as protection. Chart of LR relative to trading behaviour shared. IC acknowledged. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1779475924502669)

> [resolved] 2026-05-08 — IC requested updated toxic execution account list; Cameron Hughes shared ~170-account list in-thread
> Kyriakos (IC side) asked for the latest list of accounts in toxic execution. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778260250029739) Cameron Hughes replied with the full list in-thread (~170 account IDs, including 1000137974); IC acknowledged. No follow-up action outstanding.

> [resolved] 2026-05-06 — BTCUSD/ETHUSD weekend latency complaint; root cause found in pricing filter misconfiguration
> Joanna Theophanous (i.theophanous, IC side) reported high latency on several BTCUSD and ETHUSD trades over the weekend (examples attached as image). [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778085021583819) Kate Stagg acknowledged. Nathan Burch investigated overnight (01:34 UTC 2026-05-07): all Compass processing within ~100ms, order handling latency dashboard clean — no Mahi-side latency found; shared the order events trace URL and asked IC for further information or oneZero logs. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778114040166719) 2026-05-13 update: Daria identified the root cause — the pricing filter for IC crypto was looking up filters using its own market rather than the LP market, so the Toa filter override was not being applied, leading to indicative pricing during low-activity periods (Athena MD queries showed trigger time up to 9s behind transaction time). Fixed: added an override for local crypto instruments on icmarkets-crypto-ny; pricer processes now log correct filters. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1778636377654129) Daria notified Joanna in the client channel; IC acknowledged with ✓. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778636027354749)

> [open] 2026-05-06 — New IC team member Pavlos Elpidorou (Head of Market Risk): Compass + Echo access + onboarding call pending
> IC asked Mahi to create Compass and Echo accounts for new team member Pavlos Elpidorou (p.elpidorou@icmarketsgroup.com). [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778055176495339) Will Carter replied "Morning, will do" but no confirmation of completion was posted in the window. Pavlos joined the channel at 18:31 BST same day — access may have been provisioned but not confirmed on-thread. 2026-05-13 update: IC (Kyriakos) confirmed Pavlos's role as Head of Market Risk and requested a call with Will Carter and Cooney to brief him on Compass and Echo; call scheduled for 2026-05-14. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778659347695939) No post-call confirmation in the window.

> [open] 2026-05-04 — Tag 1000137974 slippage complaint: large burst orders consuming order book; LR rule reinstated
> IC flagged $13 slippage on a 10,000oz ($46m) gold buy (tag 1000137974). [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777899133408759) Cameron Hughes found the trade swept 6 price tiers due to 20k oz of pending orders from the same burst arriving in the same ms and consuming the stack before this 10k order settled; VWAP across the burst was ~$4650.57, broadly in line with the quoted price. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777908230843349) IC flagged multiple trades affected, mostly from the same tag. Cameron Hughes placed the tag into a no-LR rule at ~17:45 BST and committed to providing a slippage summary so IC could rebate if needed. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777913117580329) Daria's internal analysis (00:57 UTC) identified the root cause as `liquidityThrottle.sweepQuantityExpiryPeriod` / `pendingLiquidityExpiryPeriod` resetting pending qty between bursts when split orders arrive in different ms — setting both to 0 would disable the throttle (already the config at Pepper). Ideally IC sends the full order not split legs; if throttle is disabled, published liquidity depth will need boosting for 500m+ sizes. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777939076875329) IC side separately instructed Mahi to "deplete this client" (07:54 UTC); Cooney confirmed internally that Angus had specifically asked Mahi to LR the tag hard. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777964054205519) IC management response at 08:12 UTC: "trading positions over 500m, slippage expected and better than they would've gotten in the real world." [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777965157342419) 2026-05-05 update: Cooney requested re-enabling the LR rule at 09:38 BST (tag was sitting close to stop-out with ~$800 at top of book, feared a full fill); Cameron Hughes confirmed at 09:39 BST he had already removed the tag from the no-LR rule earlier that morning, leaving it in custom-1 execution — LR active. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777970283729469) Will Carter and Andrew Morgan subsequently ran yield profile analysis on the tag — noting ~£1M in LR alone and flagging it as a "proper whale". [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777983965093089) Open items: slippage summary/rebate list still owed to IC; throttle config change not yet confirmed applied; liquidity depth for large orders under review.

> [resolved] 2026-05-11 — Crypto full licence contract confirmed signed (12 months); weekend support included; XAU pilot expires 29 May
> Nicola confirmed the 12-month crypto agreement is now signed (11 :tada: reactions). [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1778494046358709) Contract includes weekend support — Cooney's plan: get interns in Dubai and London to monitor Slack rather than pulling in the main team. IC will be billed for May (they had a 1-month extension at pilot rate due to impact of Iran/Dubai). [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1778495367683659) XAU pilot expiry is 29 May — next negotiation target per Nicola.

> [open] 2026-05-01 — IC Markets system upgrade aborted; retry next weekend
> Justin Young started the deploy at 21:59 UTC but pulled it 17 minutes later: "We've identified a last minute issue, we've decided to err on the side of caution and pull the release, we'll try again this time next weekend." [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777670185603189) Internal post-mortem: Justin hadn't accounted for the NYC server reboot falling in the middle of the 45-min window — starting before the reboot risked the deploy being killed; starting after left no buffer to fix issues. Failover config also unclear. Plan: discuss with Liam next week; NYC could be deployed with a `norestart` deploy before the reboot. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777670658111869)

> [resolved] 2026-04-27 — Zendesk #22850: IC backup, START SLAVE + 69GB dump cleanup
> Inald flagged ticket — IC backup running on trading1/trading2 with 69GB dumps eating memory; needed START SLAVE post-backup + dump removal. Daria assigned Sam Hewitt, who picked it up. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777303185515629)

> [resolved] 2026-04-30 — Tag 1000137974 (500m gold) flipped to best-execution mid-flow
> Client traded 500m gold but didn't come through the execution channel; Isaac added tag 1000137974 to custom execution with a longer lookback and switched them. Briefly missing from MT drop-copy view (ICMarketsMT4S10_1000137974 visible but no trades executed by us). Tag added to "bad boys register". Client was up 3m then down 2m on the swing. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777531625614099)

> [resolved] 2026-04-30 — Compass tag: ~$1.1B notional directional trader, LR + arb-blacklist applied
> Cooney analysed the compass tag (just taken over at IC): inception PnL +$2.85M house ($173/M), max short -234,749 oz (~$1.1B notional), max long +55,226 oz. Yield curve positive 0–8m (+1.4 to +2.4 bps) but turns toxic at 60m (-2.98 bps) / 120m (-5.31 bps) — classified as informed/directional rather than latency arb. B Book hit -$8.3M intraday before unwinding. Cameron Hughes created a new crypto-zero LR rule with Angus's requested tags and blacklisted them from Crypto Arbitrgaeur classification to avoid slippage. LR pulled 178k in ~30 mins after rule landed. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777537314872139)

> [open] 2026-04-30 — reference-client-group FIX tag discussion: awaiting IC response
> Side discussion on whether IC's "reference client group" classification could be passed as a FIX tag so Mahi could trigger execution rules off it; Cooney explained current LR triggers off counterparty / group (Mahi-side, e.g. suffix "ALG") / global. IC asked if it's on the roadmap — no response yet. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777542894734739)

> [resolved] 2026-04-30 — best-execution enablement for 5 crypto client IDs
> Angus asked for best-execution enablement on crypto for client IDs 7318652, 7325161, 11560836, 7934653, 7934661 — Cameron Hughes confirmed done. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777542894734739)

> [resolved] 2026-05-12 — BTCUSD enqueue failures on IC crypto hub (no quotes on book); linked to pricing filter fix
> IC contacted Nathan Burch with OZFix enqueue errors for small BTCUSD orders (0.01–0.02 BTC) on 2026-05-02: "Problem enqueuing Hedge executions: No quotes currently on book for symbol BTCUSD from any non-excluded liquidity source." [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778580830867009) Root cause is the same latency filter misconfiguration Daria corrected on 2026-05-13 (see BTCUSD/ETHUSD latency entry above). No separate fix needed; pricing filter correction resolves this class of issue.

> [resolved] 2026-05-14 — OZFIXTakerMahiFX not connected on secondary hub; IC load-balancing to secondary hub
> IC reported OZFIXTakerMahiFX session down on their secondary hub (IP 168.245.178.93, ports 22916/22917). [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778789271070959) Nathan Burch added the secondary IP alongside the existing primary (168.245.178.232) so that the session fails over automatically. IC clarified that as part of a load-balancing exercise the secondary hub is moving to live use (not just failover) — MetaTrader servers migrating EOD 2026-05-16 5pm NYC. Liam Cordelle, Will Carter, and James were tagged. Nathan confirmed the config update; IC acknowledged.

> [resolved] 2026-05-16 — XBTUSD "Failed to find matching volume" warning on IC crypto
> IC (Michalis) reported error: "Failed to find matching volume at liquidity sources for either Hedge execution or warehouse VWAP determination." [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778932720894889) Cooney explained: a monitoring node widens the stack in sympathy with external stacks; when it can't find enough liquidity for the back elements it alerts and pauses publishing affected elements until liquidity recovers. Transient; no action needed. IC reassured.

> [resolved] 2026-05-20 — ORL account 70094243 moved to harsher pool on IC request
> IC (unidentified sender, likely Harry) asked for ORL account 70094243 to be sent to the harsher pool. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1779258843143559) Shyam Hari confirmed done.

## Notable topics

- 2026-05-11: Crypto full licence contract confirmed signed — 12-month term. Includes weekend support; IC billed for May. XAU pilot expires 29 May — next negotiation target. Weekend coverage plan: interns in Dubai + London to monitor Slack (Cooney's call).
- Compass tag is now a major B-book directional risk concentration at IC (single client running ~$1.1B notional gold, $5M+ peak MtM swings). New LR rule and arb-blacklist in place but worth watching.
- IC interested in passing reference-client-group on FIX so execution rules can route off it — open product/roadmap question, no IC response yet.
- 2026-05-04: Tag 1000137974 (500m gold directional trader) causing burst slippage complaints — no-LR rule lifted 2026-05-05, tag back in custom-1; throttle config under review, slippage rebate summary owed to IC.
- IC provided their current toxic tags list on request (2026-05-04); list includes tag 1000137974 among ~160 entries.
- 2026-05-05: Andrew Morgan ran account-level analysis on tag 1000137974 — balance/deposit figures don't add up ($6.23M cumulative profit, $4.7M net deposit, but only $2.24 account balance); flagged as possible active open positions or unusual account structure; roadmap entry exists to unify Echo counterparty + balance views. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777984229936749)
- 2026-05-05: Justin Young deployed the Compass knowledge base to icmarkets-crypto-ny environment. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777969694228499)
- 2026-05-06: BTCUSD/ETHUSD latency complaint from IC — root cause was pricing filter misconfiguration on icmarkets-crypto-ny (Toa latency filter not applied); fixed by Daria 2026-05-13, IC acknowledged.
- 2026-05-06: New IC team member Pavlos Elpidorou (Head of Market Risk) onboarded to the Slack channel; Compass + Echo access acknowledged by Will Carter; Compass/Echo onboarding call with Cooney + Will Carter scheduled for 2026-05-14. No post-call confirmation seen.
- 2026-05-08: IC (Kyriakos) requested updated toxic execution account list; Cameron Hughes shared ~170 accounts including 1000137974.
- 2026-05-14: IC is migrating MetaTrader servers to their secondary hub (live use, not just failover) — OZFIXTakerMahiFX secondary hub connection resolved by Nathan; MT server move completed EOD 2026-05-16 5pm NYC.
- 2026-05-18: Dimitrios Lambrou (role unknown) joined the mahi-ic-markets channel.
- 2026-05-21: Nia Rose posted bank holiday notice for 25 May; reduced Slack monitoring; emergency contact via support@mahimarkets.com or LN +44 203 397 1985 / NZ +64(3) 2880079. XAU pilot expires 29 May — approaching deadline for next negotiation.
