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
  - {name: "Manglai", role: "GTC — technical contact; owns pricing sign-off and go-live date", confidence: low}
  - {name: "Jack Zheng", role: "GTC — CEO", confidence: low}
last_catchup: null                                         # ISO8601; updated by /catchup
---

## Status

- **Stage:** pre-live, go-live targeted 2026-08-10/11 (Manglai, 2026-07-28; delay reason unstated, he's on holiday until then). Signed 2026-05-14. Listed under "Signed but not yet live" in `../MahiProduct/data/fleet.txt`.
- **Integration:** LDN only (`gtcfx-ln-admin-1.zlt5`), on 3 Beeks hosts repurposed from trademax (freed by the trademax LDN→NYC region swap, 2026-05-04), cluster zlt5 / cage LD5. Planned flow: GTC MT4/5 → GTC OneZero hub → Mahi (A/B book) → GMG (FCA entity) → HRP & LPs for hedge flow. GMG still on PrimeXM, which Mahi wants moved. ~3000 MT groups, so trading-account config uses constant values rather than a maintained list. Pricing reviewed and signed off post-call; `marketDataProxyTx` listen config outstanding as of 2026-08-03.
- **Relationship:** warm and actively managed — David Cooney has the OneZero/Ralich relationship (Ralich cleared Mahi risk-management on joint Mahi/OZ clients, on condition it isn't broadcast); Kate Stagg runs day-to-day; message reinforced to CEO Jack Zheng on the weekly call and well received.

## Recent issues

## Notable topics
