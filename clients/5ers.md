---
slug: 5ers
refs:
  vibepulse: ../VibePulse/.claude/clients/5ers.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: 5ers
  hosts: ../MahiProduct/data/client-hosts.json          # entry: 5ers
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Yaniv", role: "client stakeholder — weekend/failover escalations", confidence: low}
  - {name: "Yaron", role: "client stakeholder — feed reliability + spread escalations", confidence: low}
  - {name: "Andreas", role: "client trading ops — YourBourse gateway, spread/order-book settings", confidence: low}
last_catchup: 2026-05-06T07:09:45Z
---

## Recent issues

> [resolved] 2026-05-04 — XPDUSD/XPTUSD not received on YourBourse connection
> Client (Andreas) reported missing prices for XPTUSD and XPDUSD. Isaac diagnosed that the YourBourse connection had not subscribed to those symbols (CTrader/MT5 connections were publishing fine). Andreas confirmed working after clarifying symbol names. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777882979456319)

> [open] 2026-05-05 — XAGEUR MT5 price anomaly — bridge/MT5 transformation suspected
> Client reported XAGEUR chart showing prices ~$6 for most of 2026-05-05 (UTC+3 timezone). Kate checked FIX outgoing logs: Mahi gateway sent 2,344 XAGEUR quotes in the 10:43–10:47 UTC window, all in the $62.77–$62.94 range — no sub-$10 quote ever sent. Kate concluded something between Mahi's gateway and the MT5 server is transforming the price; client directed to check with their bridge. No client confirmation yet. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777987226123949) [kate-conclusion](https://mahifx.slack.com/archives/C07AQJS4E80/p1777994795210969)

> [resolved] 2026-05-05 — TP order not closed — Mid Distance Check cancel / bridge retry gap
> Constantinos raised that trade 546882908 (GBPUSD, acc 26287564) reached TP at 16:10 local time but closed 3.5h later. Kate traced: close order arrived at Mahi 13:10:01 UTC, immediately cancelled by Mid Distance Check (limit 1.35669, mid settled at 1.356675 — wrong side of threshold). Mahi returned a cancel immediately; next order from bridge didn't arrive until 16:56:53 UTC. The 3.5h gap is bridge/MT5 retry behaviour, not Mahi holding the order. Constantinos satisfied. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777980684272069)

> [open] 2026-05-04 — 4dp decimal place config for crypto/index symbols — MT5 vs cTrader discrepancy
> Cameron Hughes put in config for 4dp on a set of symbols (NGCUSD, DOGUSD, XRPUSD, HSI, etc.) per Andreas's instrument list; Daria applied the change in time for EOD restarts 2026-05-04 ~22:00. 2026-05-05 07:41: client reported the issue persists on MT5 only — cTrader prices correctly. Daria tagged but no reply yet as of run time. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777889065439829) [morning-reply](https://mahifx.slack.com/archives/C07AQJS4E80/p1777963272059319)

> [resolved] 2026-05-04 — CUCUSD spread inconsistency — dual LP base conflict
> Client (Andreas) flagged CUCUSD spreads looked wrong with screenshots. Cameron Hughes identified two LPs in the price formation had different bases; switched CUCUSD to B2BROKER only. Client confirmed better shortly after. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777896061408079)

> [open] 2026-05-04 — USDCNH pricing request — feed confirmed, instrument being set up
> Client (Linos) requested USDCNH. Nathan confirmed B2BROKER feed not yet subscribed; asked client to confirm availability. 2026-05-05: Linos confirmed B2BROKER offers the pair. 2026-05-06 01:05: Nathan confirmed instrument will be live today, asked for target spread. Client replied 60pts. Awaiting EOD restart / go-live confirmation. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777897598263539) [feed-confirmed](https://mahifx.slack.com/archives/C07AQJS4E80/p1777979008359279) [nathan-progress](https://mahifx.slack.com/archives/C07AQJS4E80/p1778025953511199)

> [resolved] 2026-04-26 — Recurring weekend disconnections — B2Broker session break / CLIENT_PRICE_LDN going indicative
> Internal (Kate, 04-28): only crypto LP is B2Broker; their session break Saturday morning stopped pricing → drop-out 5ers saw. B2Broker confirmed they can't customise session times. 2026-04-30: Kate deployed crypto feed enrichment — additional market data sourced to supplement B2BROKER, XBTEUR base spreads tightened. 2026-05-01: Kate confirmed to client that additional crypto feeds are normalised into price formation alongside B2Broker; feeds remained stable through the Saturday B2Broker downtime window. CFD side: same pattern applied, additional CFD feeds layered in. **2026-05-02 recurrence:** Yaniv reported crypto trading down on both MT5 and cTrader from ~08:00 UTC. Justin found `CLIENT_PRICE_LDN` was 98–100% indicative during 08:00–10:00 UTC; LMAX also unavailable in that window; B2Broker sessions also down. Yaniv disabled real-account routing on MT5 to restore MT5 crypto. **2026-05-04 RCA (Daria):** enriched feed changes were picked up by pricer1 last week but pricer2 — the one publishing to distribution channels — was never restarted and ran the old config. When B2Broker went down, pricer2 went indicative while pricer1 priced fine (confirming the enrichment itself works). Both pricers now fully patched; fix will cover B2Broker downtime this coming weekend. Full details in Zendesk #22903. [yaron-escalation](https://mahifx.slack.com/archives/C07AQJS4E80/p1777196856253159) [internal-rca](https://mahifx.slack.com/archives/C079M09MGGP/p1777394276388709) [feed-fix-update](https://mahifx.slack.com/archives/C07AQJS4E80/p1777572138698369) [resolved-update-05-01](https://mahifx.slack.com/archives/C07AQJS4E80/p1777652354910519) [05-02-client-report](https://mahifx.slack.com/archives/C07AQJS4E80/p1777713097183339) [05-02-justin-analysis](https://mahifx.slack.com/archives/C079M09MGGP/p1777731760352189) [05-04-rca-internal](https://mahifx.slack.com/archives/C079M09MGGP/p1777851392339829) [05-04-rca-client](https://mahifx.slack.com/archives/C07AQJS4E80/p1777853771186479)

> [resolved] 2026-04-26 — liquidityPool* down on 5ersCryptoCFDs — failed over 5ers→B2BROKER reference
> Sam Hewitt: liquidityPoolMDAggregator1/2 + liquidityPoolSOR1 down; swapped 5ers→B2BROKER in `5ersCryptoCFDs.reference.referencePriceMarketSelectors` to recover. Same root cause as the weekend disconnect (B2Broker session break). 2026-04-30: crypto feed enrichment deployed. 2026-05-01: CFD enrichment also deployed — additional CFD feeds layered in alongside B2Broker; both crypto and CFD sides now multi-source. [permalink](https://mahifx.slack.com/archives/C079M09MGGP/p1777235724205449) [resolved-update](https://mahifx.slack.com/archives/C07AQJS4E80/p1777652354910519)

> [resolved] 2026-04-27 — Spreads "fixed" on assets switched yourbourse→Mahi
> Andreas accepted Kate's proposal to bring base spreads down so dynamic widening drives the price; applied across all symbols 04-27 14:39 BST. Andreas asked 04-28 whether it also applied to FX + XAUUSD — no reply yet, but change was applied across the board. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777278243169839)

> [open] 2026-04-23 — Weekend failover dropouts — trade-flow anomaly via YourBourse gateway
> Kate raised that recent weekend restart windows show 0–1 trades vs expected higher volume during failover; heartbeats on the `5ers.COrders`↔`MahiFXMT5Bridge` FIX session look fine, so order connection is up but flow isn't routing. Nothing changed Mahi-side — Kate suspects a change to gateway routing rules on 5ers/YourBourse side and asked them to check before next scheduled weekend restart. Linked to earlier Yaniv call (2026-04-21): config issue this weekend prevented dist process from coming back up; change being put in to prevent recurrence. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1776934039029069)

> [resolved] 2026-04-29 — Pending-order rejections via bridge: "liquidity violation"
> Constantinos flagged high pending-order rejections, some duplicated. Kate explained: triggered by Mid Distance Check (price crossed minimum-distance-from-mid by end of last-look window), passed to bridge as `liquidity violation`; designed to stop off-market fills. <1% rate today; yields where present weren't profitable, so rejections look justified. Duplicates are bridge resubmits hitting the same threshold. Constantinos satisfied. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777447120492979)

> [watching] 2026-04-23 — Test trades on XAGUSD / JPN225 / XTIUSD via YourBourse gateway
> Andreas sending test trades through yourbourse→Mahi; Shyam + Isaac monitoring. Isaac's 04-24 update: trades flowing as expected; some cancels from off-market/last-look breaching limit orders but nothing unexpected. 04-28: client switched XAUUSD flow to YB+Mahi too. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1776981907673599)

## Notable topics

- 2026-04-28 — Yaniv weekly call recap: T4B→YB demo flow migration complete; FX order-book tier change applied (100k/200k/300k/500k…, was 100k/400k/500k…); Yaniv keen on further education for Yaron given he's been trialling YB's order book on demo; client now using Claude to surface toxic counterparties from MT trade logs. [permalink](https://mahifx.slack.com/archives/C079M09MGGP/p1777391713854269)
- 2026-04-30 — Constantinos requested USDSGD pricing — not previously in environment; Kate confirmed will set up. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777554437360859)
- 2026-05-05 — Yaniv weekly call (Kate): weekend outage reassured — next Saturday normalisation expected to work. Yaniv noted their $26/M yield figure (up from $18/M) — Kate queried whether this is pure slippage or blended with spread PnL; Yaniv to revert. Kate deployed CUSTOM2 custom execution rule + tighter LR profile post-call; client to upload JSON counterparty lists daily. [permalink](https://mahifx.slack.com/archives/C079M09MGGP/p1777991485939459) [client-setup-message](https://mahifx.slack.com/archives/C07AQJS4E80/p1777999802010939)
- 2026-05-05 — Server memory pressure flagged (Arun): 8.7GB swap, 2.2GB free RAM post-weekend restarts; pricer latency alerts active. Likely caused by proxied markets added for crypto enrichment. Kate expects to retire one dist process shortly to recover headroom; Arun confirmed that will help. [permalink](https://mahifx.slack.com/archives/C079M09MGGP/p1777997669364999)
- 2026-05-05 — CUCUSD alternating ~3800-point price swings reported by client for period before 2026-05-04 12:16 UTC; Mahi investigated but found no issue on their side — client directed to investigate further. [permalink](https://mahifx.slack.com/archives/C07AQJS4E80/p1777977791029089)
