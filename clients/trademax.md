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
  - {name: "Bailey White", role: "TMGM — commercial lead / decision maker on integration path", confidence: low}
  - {name: "Manglai", role: "TMGM — technical contact on pricing review", confidence: low}
last_catchup: null                                         # ISO8601; updated by /catchup
---

## Status

- **Stage:** pre-live, pricing in production trial — listed under "Signed but not yet live" in `../MahiProduct/data/fleet.txt`, but pricing + skew have been running on metals since ~2026-07-24 (gold on the A stream, all metals on the B stream, ~1 pip skew). Not yet switched to Mahi pricing client-side.
- **Integration:** Metals-first pilot (XAU ~80% of scope), Pricing & Skew only, no volume caps. Trade reports arrive via PTR — XAU only, so skew is XAU-only even though pricing is configured for other metals and FX. `TRADEMAX_POOL_1` (top-of-book, XAUUSD only) feeds `CLIENT_PRICE_NYC` down A_CLIENTS; `TRADEMAX_POOL_2` (full depth, all metals) feeds `CLIENT_PRICE_B_NYC` down B_CLIENTS. Deliberate call to source pricing purely off TMGM's own pool feeds — no proxied reference/continuity-pool feed — so an indicative price traces straight back to their feed. FX-Majors subscriptions + pricing set up 2026-07-27 (B stream), skew still to review. Execution is a medium-term ambition, not a go-live gate; drop-copy is the fastest route per Kate Stagg.
- **Relationship:** internal urgency is high (Andrew: "This is an urgent setup request", Bailey pushing back on delays). Nicola runs the commercial cadence; Andrew + Will + Shyam + Isaac on the technical side.

## Recent issues

## Notable topics
