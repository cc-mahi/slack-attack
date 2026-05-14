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
  - {name: "Pavlos Elpidorou", role: "IC Markets Head of Market Risk"}
  - {name: "Joanna Theophanous", slack_handle: "i.theophanous", role: "IC Markets ops/client-side contact", confidence: low}
  - {name: "Kyriakos", role: "IC Markets — requested toxic execution account list; first name only seen", confidence: low}
last_catchup: 2026-05-14T07:21:58Z
---

## Recent issues

> [open] 2026-05-12 — BTCUSD hedge enqueue failures (no maker quotes, 2026-05-02 trades); awaiting Mahi response
> IC (message to Nathan Burch) shared oneZero hub logs for several BTCUSD trades from 2026-05-02 showing "Problem enqueuing Hedge executions: No quotes currently on book for symbol BTCUSD (from any non-excluded liquidity source)" across 6+ order IDs. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778580830867009) No reply from Nathan or Mahi team in the thread as of the catchup window.

> [watching] 2026-05-12 — signalProcessFI1 memory spike and restart at IC Markets
> Inald Gjoni noted signalProcessFI1 restarted at IC Markets; memory usage started climbing ~15:10 BST 2026-05-12. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1778602202367479) No follow-up in thread; no client-visible impact reported.

> [open] 2026-05-13 — Pavlos Elpidorou (Head of Market Risk) onboarding call to be scheduled
> Kyriakos (IC) introduced Pavlos Elpidorou as new Head of Market Risk and requested a call with Will Carter / David Cooney to brief him and walk through Compass and Echo. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778659347695939) A follow-up message (unattributed in log) offered to schedule a call for the following day; David Cooney confirmed availability Thursday or Friday. Compass/Echo access status per prior entry: acknowledged by Will Carter 2026-05-06 but no on-thread confirmation yet.

> [resolved] 2026-05-08 — IC requested updated toxic execution account list; Cameron Hughes shared ~170-account list in-thread
> Kyriakos (IC side) asked for the latest list of accounts in toxic execution. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778260250029739) Cameron Hughes replied with the full list in-thread (~170 account IDs, including 1000137974); IC acknowledged. No follow-up action outstanding.

> [resolved] 2026-05-06 — BTCUSD/ETHUSD weekend indicative pricing; root cause found and fixed 2026-05-13
> Joanna Theophanous (i.theophanous, IC side) reported high latency on several BTCUSD and ETHUSD trades over the weekend (examples attached as image). [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778085021583819) Nathan Burch found no Mahi-side latency (Compass <100ms, dashboard clean) and awaited IC oneZero logs. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778114040166719) 2026-05-13 resolution: Daria Horton identified root cause as a pricing filter misconfiguration — the model looks up filters via its own market, not the LP market, so the existing filter override wasn't being applied; trigger time was up to 9s behind transaction time during low-activity periods (Athena MD confirmed, both Toa APN1 and IC Markets envs affected). Daria added a local crypto instrument filter override and confirmed correct filter application. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1778636377654129) Client-facing message sent to Joanna: "Toa rate was being filtered out, leading to indicative pricing. Corrected configuration now, confident won't recur this weekend." [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778636027354749)

> [open] 2026-05-06 — New IC team member Pavlos Elpidorou: Compass + Echo access requested, not yet confirmed
> IC asked Mahi to create Compass and Echo accounts for new team member Pavlos Elpidorou (p.elpidorou@icmarketsgroup.com). [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1778055176495339) Will Carter replied "Morning, will do" but no confirmation of completion was posted in the window. Pavlos joined the channel at 18:31 BST same day — access may have been provisioned but not confirmed on-thread.

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

## Notable topics

- 2026-05-11: Crypto full licence contract confirmed signed — 12-month term. Includes weekend support; IC billed for May. XAU pilot expires 29 May — next negotiation target. Weekend coverage plan: interns in Dubai + London to monitor Slack (Cooney's call).
- Compass tag is now a major B-book directional risk concentration at IC (single client running ~$1.1B notional gold, $5M+ peak MtM swings). New LR rule and arb-blacklist in place but worth watching.
- IC interested in passing reference-client-group on FIX so execution rules can route off it — open product/roadmap question, no IC response yet.
- 2026-05-04: Tag 1000137974 (500m gold directional trader) causing burst slippage complaints — no-LR rule lifted 2026-05-05, tag back in custom-1; throttle config under review, slippage rebate summary owed to IC.
- IC provided their current toxic tags list on request (2026-05-04); list includes tag 1000137974 among ~160 entries.
- 2026-05-05: Andrew Morgan ran account-level analysis on tag 1000137974 — balance/deposit figures don't add up ($6.23M cumulative profit, $4.7M net deposit, but only $2.24 account balance); flagged as possible active open positions or unusual account structure; roadmap entry exists to unify Echo counterparty + balance views. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777984229936749)
- 2026-05-05: Justin Young deployed the Compass knowledge base to icmarkets-crypto-ny environment. [permalink](https://mahifx.slack.com/archives/C07UBJNUWG1/p1777969694228499)
- 2026-05-06: BTCUSD/ETHUSD latency complaint from IC — Mahi found nothing on their end; awaiting IC oneZero logs to close.
- 2026-05-06: New IC team member Pavlos Elpidorou onboarded to the Slack channel; Compass + Echo access creation acknowledged by Will Carter but not confirmed complete.
- 2026-05-08: IC (Kyriakos) requested updated toxic execution account list; Cameron Hughes shared ~170 accounts including 1000137974.
- 2026-05-13: Indicative pricing root cause resolved — pricing model filter lookup bug (model uses own market not LP market; Toa rate filtered out during low-activity periods). Daria added local crypto instrument filter override; both Toa APN1 and IC Markets envs affected. Fix confirmed applied.
- 2026-05-13: Pavlos Elpidorou confirmed as Head of Market Risk (was "team member" in prior entry). Call with Will Carter / Cooney to be scheduled for Compass + Echo briefing.
- 2026-05-12: BTCUSD hedge enqueue failures (no maker quotes) reported by IC for 2026-05-02 trades — no Mahi reply yet; Nathan Burch tagged.
- 2026-05-12: signalProcessFI1 memory spike and restart at IC Markets (~15:10 BST) — no client impact reported, no follow-up in thread.
