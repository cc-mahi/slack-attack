---
slug: icmarkets
aliases: [icmarkets-crypto]
refs:
  vibepulse: ../VibePulse/.claude/clients/icmarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: icmarkets-crypto
  hosts: ../MahiProduct/data/client-hosts.json          # entry: icmarkets
  wiki: null                                             # ../MahiProduct/wiki/clients/icmarkets.md (not yet)
channels_override: null
key_people_overrides: []
last_catchup: 2026-05-03T07:06:49Z
---

## Recent issues

> [resolved] 2026-05-01 — Crypto full licence contract signed (12 months)
> Nicola Perikhanyan announced contract agreed and ready for signature; 7 :tada: reactions. [permalink](https://mahifx.slack.com/archives/C07TZ00FK1Q/p1777626006675209)

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

- 2026-05-01: Crypto full licence contract agreed and ready for signature — 12-month term.
- Compass tag is now a major B-book directional risk concentration at IC (single client running ~$1.1B notional gold, $5M+ peak MtM swings). New LR rule and arb-blacklist in place but worth watching.
- IC interested in passing reference-client-group on FIX so execution rules can route off it — open product/roadmap question, no IC response yet.
