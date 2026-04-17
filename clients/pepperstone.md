---
slug: pepperstone
name: Pepperstone
type: broker
status: live
products: [fx, crypto]
regions: [LDN, NYC]
contract_expires: 2028-07-16
channels:
  internal: internal-pepperstone
  client: [mahi-pepperstone-vnd]
  other: []
key_people: []
athena_dbs: [pepperstone_ldn, pepperstone_nyc, pepperstone_crypto_ldn, pepperstone_crypto_nyc]
aws_profile: 730335273835_MahiAnalytics
last_catchup: null
---

## Summary

Large broker client on fixed-fee commercial terms covering MFXEcho, Compass, Pulse and Crypto. Currently in a 3-year term (signed 2025-07-16 via 3rd Addendum, expires 2028-07-16) at a 10%-discounted $115,088/mo software fee, with hosting pass-throughs (Beeks, WAN, AWS capped at $10k) billed on top. FX and Crypto desks run as separate infra (VibePulse slugs `pepperstone` and `pepperstone-crypto`) but share Slack channels and commercial terms.

## Technical notes

### Shared

- Ring-fenced AWS account `730335273835` — use `aws_profile: 730335273835_MahiAnalytics`.
- Athena: use `primary` workgroup (not analytics). `athena list-databases` returns empty; use `aws glue get-databases` to enumerate.
- Available workgroups: `pepperstone_ldn`, `pepperstone_nyc`, `pepperstone_crypto_ldn`, `pepperstone_crypto_nyc`, `primary`.
- Billing: software fee $115,088/mo, but total invoiced is ~$141–142k once hosting pass-throughs (Beeks $10k flat + GBP WAN 1,085 + Crypto GBP 4,394 + AWS up to $10k) are added. Billing-prep must include hosting in Pepperstone totals (per Nicole, Feb 2026).
- Cannot terminate for convenience during the 3yr term (clause 2.2.2, expires 2028-07-16). Post-expiry the software fee reverts to $127,876/mo.

### FX desk (VibePulse: `pepperstone`)

- Hosts — LDN: `pepperstone-ln-trading-1.gs03.prod.mahimarkets.com`, `pepperstone-ln-admin-1.gs03.prod.mahimarkets.com` (DC LD5). NYC: `pepperstone-ny-trading-1.p7l0.prod.mahimarkets.com`, `pepperstone-ny-admin-1.p7l0.prod.mahimarkets.com` (DC NY4).
- Athena DBs: `pepperstone_ldn`, `pepperstone_nyc`.
- Distribution markets — LDN: `CLIENT_PRICE_LDN`, `CLIENT_PRICE_BETA_LDN`, `DISTRIBUTION_LDN`. NYC: `CLIENT_PRICE_NYC`, `CLIENT_PRICE_BETA_NYC`, `DISTRIBUTION_NYC`.

### Crypto desk (VibePulse: `pepperstone-crypto`)

- Hosts — LDN: `pepperstone-crypto-ln-trading-1.gs03.prod.mahimarkets.com`, `pepperstone-crypto-ln-admin-1.gs03.prod.mahimarkets.com` (DC LD5). NYC: `pepperstone-crypto-ny-trading-1.sd55.prod.mahimarkets.com`, `pepperstone-crypto-ny-admin-1.sd55.prod.mahimarkets.com` (DC NY4).
- Athena DBs: `pepperstone_crypto_ldn`, `pepperstone_crypto_nyc`.
- Distribution markets — LDN: `CLIENT_PRICE_LDN`, `CLIENT_PRICE_BETA_LDN`, `CLIENT_PRICE_SPOT_LDN`, `DISTRIBUTION_LDN`, `HRP_LDN`. NYC: `CLIENT_PRICE_NYC`, `CLIENT_PRICE_BETA_NYC`, `CLIENT_PRICE_SPOT_NYC`, `DISTRIBUTION_NYC`.
- LP FIX connections — LDN: `fixMarketData1/2/3`, `fixMarketDataModulus1`. NYC: `fixMarketData1/2/3`, `fixMarketDataB2C2`, `fixMarketDataModulusUAT1`.
- LP markets: `LMAX_NYC`, `LMAX_DIRECT_LDN`, `B2C2_NYC`, `WINTERMUTE_NYC`, `HRP_LDN`, `HRP_PROXY`, `MODULUS`, `MODULUS_LDN`.
- Order table naming is **inverted**: `houseorder_*` = DISTRIBUTION orders (Mahi→MT5), `externalorder_*` = LP hedging.
- `com.x.validation.AD` = Mahi pre-flight validation.
- Party names: `SPOT_HOUSE` = `SPOT_HEDGING_MODEL_H1_LDN`; `SI` = `SI_HEDGING_MODEL_H1_NYC` / `SI_HEDGING_MODEL_ARB_NYC`; client flow = `SPOT_CLIENTS_NYC` / `SPOT_CLIENTS_LDN`; simulation = `PTR_CLIENTS` / `PTR_CLIENTS_NET` / `PTR_CLIENTS_HEDGING`; `SI_HOUSE` = Crypto SI PnL.

## Recent issues

## Notable topics
