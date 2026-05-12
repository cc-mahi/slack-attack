---
slug: alphacap-broker
refs:
  vibepulse: ../VibePulse/.claude/clients/alphacap-broker.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: ../MahiProduct/wiki/clients/alpha-capital-group.md
channels_override: null
key_people_overrides:
  - {name: "Gerard McConnell", role: "ACG Markets — sign-off / Prop side ops contact", confidence: low}
last_catchup: 2026-05-12T07:09:56Z
---

## Recent issues

> [open] 2026-04-29 — Argamon symbol coverage gap blocking go-live
> Will Carter framed minimum path to go-live; Andrew confirmed "they need it all" but the go-live spreadsheet's instruments are all available direct from Argamon. Cam working through CFDs/crypto where Argamon proxies LP — externalisation a problem for proxied LP, hence CPL/dist setups instead. Phased asset-class approach agreed (FX + Metals first, CFDs/crypto phase 2/3). [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777462009649679)

> [open] 2026-04-29 — ACG remaining instrument subscriptions pending Argamon enablement
> 22 instruments still missing after Cam bounced fixMarketDataArgamon and fixOrdersArgamon to pick up subscription mappings: 4 FX (GBPPLN, USDCZK, USDHUF, USDPLN), 3 metals (XAGEUR, XPDUSD, XPTUSD), 7 commodities (COFFEE/CORN/COTTON/SOYBEAN/SUGAR/COCOA/WHEATUSD), 8 crypto (ADA/AVAX/BCH/DOG/LINK/SOL/XLC/XRP). Cam reached out to Tom McLean at Argamon — Tom's reply (Apr 30): commodities subscribed our side but not flowing in ACG MD logs (suggests ACG hasn't subscribed); AVAX/DOGE/LINK/SOL crypto only available in NY (not LDN); FX/metals visible on taker feed, ACG end needs to subscribe. Cam telling ACG we want NY crypto despite NY/LN latency. [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777538204659809)
> Progress (May 6): Cameron Hughes bounced pricers twice — first bounce (13:44) added XAUAUD, XAGAUD, AVAXUSD, DOGUSD, LINKUSD, SOLUSD [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1778071485886139); second bounce (14:38) added base spreads and custom instrument lists for COFARA, CORN, COTTON, SOYBEAN, SUGARRAW, USCOCOA, WHEAT [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1778074723331379). Remaining gap: 4 FX (GBPPLN, USDCZK, USDHUF, USDPLN), 3 metals (XAGEUR, XPDUSD, XPTUSD), 2 crypto (ADA/BCH/XLC/XRP — 4 of the 8 original crypto still unresolved). Active work in progress; keeping open.

> [open] 2026-04-29 — Account manager handoff: Maten → Cameron Hughes for setup work
> Andrew (Apr 27) handed Maten back to Cameron Hughes for ongoing setup; Cam owns pricing model config. External: ACG want to match Argamon's symbol naming. Zendesk ticket 22877 carries the fuller brief. Andrew (Apr 30) noted David Rapp got "a bit shirty" last week and needs keeping in the loop alongside Maten Rehimi; ACG are "low maintenance on the prop side" and a "great customer" there, but the broker side is unfunded effort until fees kick in. [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777291816435319)

> [resolved] 2026-04-24 — Spread/comm/markup file V5.4 signed off by Rapp
> Iteration through V5.1 (Apr 22) → V5.4. Rapp: "lets just go with that to get some numbers in MT5 — once we start benchmarking monthly we can widen or tighten and refine and so on." Friction in thread: Rapp had promised George Kohler this would be set up by COB Apr 24 without involving Mahi; Andrew pushed back ("not earning any fees from this", "long tail on dealing with him here, before any fees kick in for us"). [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777047238816599)

> [resolved] 2026-04-17 — MT5 group/symbol setup plan executed end-to-end
> Maten's Mar-31 proposal walked through with Rapp on Apr 14 (4pm BST call); refined plan posted Apr 16 (narrow T4B Group/Symbol filters, import .s symbols into ACGM folder, GOOD-RAW-USD group, Mahi gateway routing rule above T4B). Rapp + Gerard McConnell signed off Apr 16. Maten executed same day; David confirmed business as usual on prop side. Test trades confirmed Apr 17 — successful EURUSD.s 1k BUY/SELL via Compass after a permissions/funds glitch. [permalink](https://mahifx.slack.com/archives/C09F15FRTAB/p1774974109945799)

## Notable topics

- 2026-04-20 — Go-live target early May; T4B replacement project follows launch. Andrew flagged that the high-priority/high-risk milestones (coexistence with T4B, end-to-end trades) are already delivered, and Mahi has backfilled all the REST APIs T4B had. [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1776681404918759)
- 2026-04-29 — Risk-management strategy ownership. Will: "we are the risk management experts" per Rapp; "we're free to run it as we want." Implication: Mahi dictates how risk works once instrument coverage settles. [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777465055105989)
- 2026-04-29 — Externalisation gap for proxied-LP CFDs at Argamon. CFDs at Argamon often have only proxied LP pricing, so Mahi can't externalise the trades. Cam considering CPL pricing setups in Argamon for CFDs where direct LP pricing exists; TOA crypto already available. Open design question. [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777462376226129)
- 2026-05-05 — Swap management: inventory-skewed benchmark swap solution scoped. Andrew (responding to Rapp/Maten Apr-30 call note that ACG want MT swaps to match Argamon's values, with daily updates and 10% markup) flagged need to push MQ swap-management setup into KB and scope the inventory-skewed benchmark swap solution further. Separately, David Cooney relayed that Elan (Argamon) estimates the swaps give an annual return of ~25%, underpinning the commercial case. [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777975121524689) [permalink](https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777991358798539)
