---
slug: velocity
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/velocity.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: velocity
  hosts: ../MahiProduct/data/client-hosts.json          # entry: velocity
  wiki: ../MahiProduct/wiki/clients/velocity.md
channels:
  internal-velocity: CPDS0M2KF
  mahi-velocity: C05NB72AGR2
contacts:
  - {name: "Dan Beale", role: "Velocity client ops: feeds, spreads, KAU/crosses, LP hedging, yield profiles; daily counterpart"}
  - {name: "Jackson March", role: "Velocity (Singapore hours): API creds/hedge accounts, whitelists, LP testing"}
  - {name: "Richard Holman", role: "Velocity principal: pricing/hedging policy, commercial terms, prospect flow"}
  - {name: "Russell Hewson", role: "Velocity: sim data requests, Echo login"}
  - {name: "Liv Mottershead", role: "Velocity, joined Richard's team 2026-07", confidence: low}
last_catchup: 2026-10-28T07:19:51Z
status: active
---
## Now
PnL under pressure since late Aug (hedge costs up, Kama/Argamon widened); hedging slowed 2026-10-12 and PnL stabilised, but losses on 10-14 and 10-19 pushed hedging to classification-based rules (no blanket delay); still losing 10-21 on hedge spread. Commercials moving from PnL share to a volume-banded fixed fee, awaiting client CFO sign-off. Interest-only feed is toxic (counterparty 1100) and being priced out; client still wants it. 10-22 Will C is researching a premium big-ticket skew (streaky slicer flow, FM-BIG sim pending). 10-21 1034 tags moved off prem to the wider session and the toxic list is being rejected; premium EXEC channel not yet live. 10-23 Andrew M proposes a depth ladder (tight first clip, charge for size) on gold plus per-session skew. 10-27 Prem twilight widening cut 2x to 1.2x after a client complaint about wide gold.

## Streams

### last-look-slack — Last-look retry and passing client slack back
status: open · since: 2026-10-26 · last: 2026-10-26
State: 10-26 Richard queried a trade rejected then instantly refilled; Denny: the first order was cancelled by last look, the retry was repriced to our TOB and passed. Richard then said Velocity had stopped passing slack (client-side limit) to Mahi because it was not improving them, asked whether that is resolved and whether to resume; Denny will check execution settings and revert.
Next: Mahi (Denny): answer on whether slack can be passed again.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1793032599037739 https://mahifx.slack.com/archives/C05NB72AGR2/p1793033048353429

### gold-depth-ladder — Tight gold TOB, charge for size, per-session skew
status: open · since: 2026-10-23 · last: 2026-10-23
State: Andrew M proposes (internal only) keeping the tight XAUUSD TOB for the first clip and laddering depth so bigger tickets fill wider on VWAP, instead of widening the Prem TOB; Will C's 20 Oct analysis has the 9c Prem channel below hedge cost, with losses in identifiable tags. Jul-Sep half-spread paid: Velocity 20-100oz 35.3 $/M (79% of volume) equals the network median, >100oz 95.7 vs median 56.2; about $330k a quarter per +10 $/M on the 20-100oz band if flow stays. FinPrime prospect figures stay internal; any Velocity-facing version uses network bands only. Second lever is a per-counterparty/FIX-session flow-momentum skew variant being built in the SkewValueAdd sim, with Velocity a live candidate. Figures are Athena-based, not yet Compass-linked.
Next: Mahi: size a depth ladder on Velocity's own flow in sim; score per-session skew once built.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1792771031124009

### premium-skew-lean — Skew on big premium tickets (slicers)
status: open · since: 2026-10-22 · last: 2026-10-26
State: 10-26 Will C registered additional FM signals with a qty threshold for the prem channel and restarted the signal process; signals were only configured for Prem so he bounced again, and Denny bounced starfishFilePersisterExternalMarketData1 to pick up new signals in metadata_signal_xauusd and riskPath for signalprofiles. Will C's evening screenshots read 'not bad' and 'synapse still better', with jumps when the >24oz trigger fires. Earlier: Will C found premium flow comes in streaks: after a $200k+ ticket the same client's next ticket goes the same way 73-83% of the time (2,119 tickets, 8-21 Oct, both weeks, placebo 50%), mostly one client slicing an order; 1034 tags named 'slicers'. LR cannot capture it as 97% of premium orders are limit IoC at our quote with zero slack (fill-time worsening just cancels; 77% re-send after an LR cancel but only 35% fill), and the client base rejects channel LR and a 9c spread. Proposed lean: after a premium fill over $100k, lean 6c for 1-2 min, screened at about $2/M vs about $1.4/M live (recorded-fill screen, not an engine result). Engine tests: IFMS-B swap +$0.7/M vs live with range including zero; FM-BIG (existing FM flow signal, 0.24 qty threshold, 120s, A_CLIENTS_PREMIUM) earned +$8/M on the triggering client's follow-ups (one Asia session, 26 fills, thin); lean came out about 3c, not 6c. Four-arm sim (live / live+FM-BIG / FM-BIG only / no skew) over three Asia sessions due 14:00-14:30 BST 10-22; result not seen. Richard (12:16) said premium should not carry sever tags and they should be switched off.
Next: Will C: score the four-arm run, size test if live+FM-BIG holds, London window before any change-set; live trial needed to see client reaction.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1792656425258739 https://mahifx.slack.com/archives/CPDS0M2KF/p1792671488308169 https://mahifx.slack.com/archives/CPDS0M2KF/p1793022086770639

### tag-exec-routing — Turn off worst 1034 tags, EXEC channel for toxic flow
status: open · since: 2026-10-15 · last: 2026-10-21
State: 10-20 strategy agreed with Richard: turn off the worst tags and route signal-follow (later broker-classified) flow to a prem EXEC pool channel at a worse price. 10-21 Richard asked to set all 1034 tags to reject anything toxic; Denny offered either an execution rule rejecting signal-follow 1034 tags (complaints risk) or moving them to the wider A feed set broker-only. Denny confirmed rejecting Dan's list of 11 tags (11:43 BST) and Dan then moved 1034 off prem onto the wider session; rejecting continues until PnL improves (Dan agreed). Dan is chasing a broker-of-broker chain to remove the sub-tag. Dan asked for a month-on-month Aug/Sep/Oct tag analysis and new-tag lists; Denny delivered volume and 1s/5s/30s yield for all 1,464 1034 counterparties. Shyam added the A_CLIENTS_PREMIUM to A_CLIENTS_PREMIUM_EXEC mapping late 10-21 (list still disabled) and bounced dist, so EXEC on premium is not yet live. Will C TODO: classification-based LR review, classify captive vs non-captive audience.
Next: Mahi: enable the premium EXEC list and verify routing; Client: tag removal up the broker chain, review the tag spreadsheet.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1792407215108419 https://mahifx.slack.com/archives/C05NB72AGR2/p1792578643181169 https://mahifx.slack.com/archives/C05NB72AGR2/p1792583066524929 https://mahifx.slack.com/archives/CPDS0M2KF/p1792620577365139

### hedging-pnl-turnaround — PnL bleed, hedge speed and spreads
status: open · since: 2026-08-24 · last: 2026-10-21
State: Bleed began late Aug (Kama widened, mid-quality problems); ref LPs swapped 08-26 and PnL recovered, then CLIENTS_NET fell through Sep-Oct as hedging took the spread (Kama rule share, 1034 flow). 10-08 Mahi told the client prem-feed economics no longer add up (prem 12.2 pips TOB vs LP 19-22) and asked for ~17 pips average. dynamicOrderSpeedScaling went 1.0 to 0.1 on 10-12 (CHG-2610-T6H5) and PnL stabilised; a $3.5k overnight loss 10-14 (slow hedging, 54% LP fill) led to overnight rules scoped back to speed 1 and OR-IMI-IMS cut to 500ms. 10-15 call: client happy PnL is stabilising, agreed to review counterparty classification and drop toxic tags from prem. 10-15 pm client asked for tag-by-tag controls on a toxic tag (1034Z58AF42E6, small share of its flow seen, 60d aggregate poor): harsher last look per tag is possible; hedging a tag after X seconds is not a function, but the hybrid hedger can react with a delay to the last client tag into the same book (no separate book needed). Will D to try slower rules for it and sim first. 10-19 Will D ran 20s hedge-trigger delay / 60s closure after a $550 drop (472oz sold by four CPs in a minute), Large Position rule trigger lowered to 200oz; the delay on broker-classified tags then cost a further $400 (delays interfered with risk clearing), so it was reverted: sharpest tags register risk immediately but clear slower. Book +$350 after. Classification-based hedging now: Dynamic broker and Dynamic signal rules highest priority, close within 30s at $750 VaR/s reduction (kept slow to avoid paying LP spread); OR-IMI-IMS predicate only up to 100ms, price-dyn-0.7-3000 may return as predicate. 10-20 Will C posting yield-profile checks of the new setup (spread in +12/m, out -20/m, PnL -18/m). 10-20 Denny comparison (30d, XAUUSD internalised, house side): Velocity CLIENTS_LDN has the lowest inception yield of six institutional books ($16.0/M vs $20.5-67.5/M) and falls to -$5.0/M by 1m. 417 new counterparties since 10-12, 77 classed Broker or Signal Follow; Richard asked to switch off losing tags rather than change the model. Tag handling now runs in tag-exec-routing. 10-21 15:10 BST Will C: last 2h hedging spread yield 12/m vs client spread 22/m, still losing; removed the 0.1 dynamic order speed override and 10x-ed the DTA override given the new rule setup.
Next: Mahi: monitor the new classification-based hedging, sim tag-delay setup, NZ watch overnight book, re-read the slowdown after a full week, size a higher-risk backstop (~300oz). Will D: PnL-by-price analysis for the interest feed.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1787575981397189 https://mahifx.slack.com/archives/C05NB72AGR2/p1792072610702039 https://mahifx.slack.com/archives/C05NB72AGR2/p1792421041345839 https://mahifx.slack.com/archives/CPDS0M2KF/p1792591829282439

### interest-feed — Interest-only (risk-reducing) C feed
status: open · since: 2026-08-18 · last: 2026-10-20
State: 10-20 Will C wants to check whether the fills are actually risk-decreasing; Denny posted an analysis artifact. Live 08-18 with riskAdjustedFirmQty. Fill rate climbed from ~15% to ~92% (09-22) after refresh and last-look relaxation, extended to XAG and FX majors. Mahi analysis (09-29): 97.7% of fills reduce risk but are -$30/M at 1m; counterparty 1100 machine-guns 1-10ms bursts and is 99% of added risk; exec rule split, channel LR $100k/s and LR cap 1000 $/M added, still ~12oz/day of risk-increasing fills and the hedger races the feed. Will C wants it off; base spread widened 20 to 30 to quietly cut flow, now no fills. Client wants it kept but priced correctly.
Next: Will D: data-backed PnL effect at different price levels; fix hedger-vs-interest race.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1787071381197089 https://mahifx.slack.com/archives/CPDS0M2KF/p1790693863681659 https://mahifx.slack.com/archives/CPDS0M2KF/p1792060203147839 https://mahifx.slack.com/archives/CPDS0M2KF/p1792480630454159

### prem-a-feed — Prem and A feed spreads, fills, LR
status: open · since: 2026-08-26 · last: 2026-10-27
State: 10-27 evening Richard flagged gold gone very wide (clients complaining) with Prem wider than A; Shyam traced it to the 2x TWILIGHT minimum-width-market widening on Prem (protective, in place since July, Prem ~$1.00-1.50 over the hour either side of NY close) and cut it to 1.2x (Prem expected ~$0.70-1.00), later confirmed to the client as nothing abnormal. A had been tighter than Prem over twilight since 17 Aug because Kama (near-fixed $0.30 twilight quote) joined A's benchmark; Shyam proposes dropping Kama from A's MWMS benchmark over twilight and roll. Internally Will C: Prem can be brought in, client must say what they want, tags can now be turned off on that feed. 10-21 Dan asked how wide the A feed should be in XAUUSD; Will C: starts at 20c with volatility-based widening, currently 22c TOB; Dan says the 1034 client sees 32-35c and will check. 10-20 Will C thinks 9c is very tight for anyone executing and the analysis only needed base 9 to 12; Richard holds to the agreed 9 and says deal flow dries up once wider than 12. 10-16 Richard saw prem 12/14c wide against the agreed 9c base; Will D confirmed 9 is the base and said temporary volatility widening is in place that should not be increased, to be checked. Asia 20c TOB live (Hantec complained 08-26 of 20-35c swings). 09-24 models swapped (CLIENT_PRICE_LDN = prem, B_LDN = A) and client now supplies spread-config CSVs; Compass timezone boundaries shared. A-feed fill rate MTD 57% vs 75% target (12% LiquidityThrottled cancels, refresh raised); 4x SNG LR multiplier cut to 2x with a second tier (09-28); A_CLIENTS_PREMIUM fill price back to passthrough 10-06. Prem price instability and roll widening (10-02) explained as LP-spread protection.
Next: Mahi: decide on dropping Kama from A's twilight/roll MWMS benchmark; client to say how tight Prem should be. Will D: check the temporary volatility widening and bring prem back to 9c. Mahi: confirm 3dp XAUUSD quotes from Kama/Jump/ZZ do not cause 3dp limit rejects (client says 3dp is accepted), then change config.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787744856529959 https://mahifx.slack.com/archives/C05NB72AGR2/p1790247752525379 https://mahifx.slack.com/archives/C05NB72AGR2/p1793134646597689 https://mahifx.slack.com/archives/C05NB72AGR2/p1793143080432879

### db-pro — Deutsche Bank Limit Pro passive hedging via Reactive
status: open · since: 2026-08-18 · last: 2026-10-22
State: 10-22 DB cancels for subceeding minimum notional forced the hedge minimum order up to $100k (Richard: DB Pro minimum is 10oz); the cancels tripped the Reactive switch again and LimitPro not-permissioned rejects returned; Denny re-enabled DB_PRO and awaits Reactive. 10-20 passive hedging retried: first rejects were 'Exceeded maximum price precision' (3dp sent, DB takes 2dp); after Denny changed to 2dp, rejects became 'LimitPro not permissioned for account VELOCITY_ALGO'. Richard says permission was disabled after the dp issues and Reactive are switching it back on; Denny turned DB_PRO off until resolved and sees no passive trades. In/out test trades succeeded 08-24 and 6dp price fixed 08-25; drop copy via Xenfin is live. Session window 17:05 Fri NY queried 09-22 (client says ask Reactive/DB). 10-01 adding DB_PRO as an XAUUSD execution market crashed hybridHedger1; reverted and restarted, setup not finished. Shared Reactive cross-connect in LD4 costs GBP 100/month; on-charge/addendum question went to Nicole 08-18 with no answer seen in channel.
Next: Reactive: re-enable LimitPro permission; Mahi: re-enable DB_PRO and confirm passive trades; Nicole: on-charge/addendum answer.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787049402059669 https://mahifx.slack.com/archives/C05NB72AGR2/p1790081928596799 https://mahifx.slack.com/archives/C05NB72AGR2/p1792494641397569 https://mahifx.slack.com/archives/C05NB72AGR2/p1792668512445189

### cfd-expansion — CFD / index instruments (J40, Z40, new CFD list)
status: open · since: 2026-08-19 · last: 2026-10-21
State: 08-19 IG FIX timeout dropped Velocity's bridge, Mahi held 84 J40 and client had to flatten by voice; policy agreed to confirm positions before re-enabling the hedger. Z40 hedging fixed after a 10-02 NFP loss (more aggressive news rule, fillRatioTracker off, single LP). Client supplied pricing for CNI/DJI/GDI/USO/UKO and a 28-instrument CFD list; yield profiles now generate (10-15) and 21 of 28 instruments have drop copies. riskPathCsv MD throttled (1ms updates) on 10-13 which had distorted CFD yields. Off-market NDMUSD fills explained 10-21 by Richard: both trades were on a different bespoke feed for that client.
Next: drop copies missing for AEXEUR, DJFUSD, DXFEUR, JPUUSD, NDFUSD, S30SGD, SPFUSD.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787147771318879 https://mahifx.slack.com/archives/CPDS0M2KF/p1790947414363299 https://mahifx.slack.com/archives/C05NB72AGR2/p1792067342224599 https://mahifx.slack.com/archives/C05NB72AGR2/p1792574647919929

### hedge-lps — Hedging LP set (Argamon, Virtu, ZZ, Kama, others)
status: open · since: 2026-08-26 · last: 2026-10-15
State: Argamon in hedging from 08-27 (whitelist gap fixed 09-01), ZZ added with tag-1034 blacklist (09-02), SGX/Edgewater added. Argamon fill rate ~15% (off-market, last look, throttle, Lucera drops) so removed 09-18 at client request, restored 09-22. Virtu (bilateral, to replace Kama) still being configured by the client; NWM Morgan Stanley test 09-29 then client asked to hold off. Kama routes to its institutional channel since 10-02 (fills at limit, 5 pip markup 10-07); Argamon and Kama widened to 20-24c TOB 10-06. Ref-mid LP set re-chosen 10-07 by 1s yield and lead-lag. 10-15 client asked to cut the ~16 price layers on hedge LP sessions; Will D agreed to cut to 5.
Next: Mahi: apply 5-layer cut on hedge sessions. Client: Virtu ready-to-test notice; decision on VELBINT099HS (left live). Mahi: move hedge weight off Kama where possible.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787725457576859 https://mahifx.slack.com/archives/C05NB72AGR2/p1789653498837279 https://mahifx.slack.com/archives/C05NB72AGR2/p1792079679596159

### flow-onboarding — Prospect datasets, new tags and tob size requests
status: open · since: 2026-08-21 · last: 2026-10-26
State: 10-26 Richard asked about a TF Global dataset; Will C found it in email (Zendesk 23703) but trade_time came through as minutes and seconds only, so it cannot be marked to market; asked for a raw source export with full UTC timestamps and trade ID. Client runs prospect datasets through MarkToMarket sims (Dan, Russell; latest SB1 data GMT+3 10-15, FX data pending) and moves tags to A/prem feeds (911, 460 to A; 1034 upgrade; new FX cpty 122). Hantec asked for 500oz TOB (09-16): Will C advised stepping it up weekly with a dedicated session; decision not yet communicated. Exinity/VTI C2C (Elysium) contra mapping queried 08-21.
Next: Client: re-send TF Global export with UTC timestamps. Mahi: reply on the 500oz TOB request; run SB1 FX sim.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787309743078989 https://mahifx.slack.com/archives/CPDS0M2KF/p1789548932088989 https://mahifx.slack.com/archives/C05NB72AGR2/p1792062011672689 https://mahifx.slack.com/archives/C05NB72AGR2/p1793021118443629

### client-tooling — Access, reports and self-serve requests
status: open · since: 2026-08-19 · last: 2026-10-15
State: Whitelists (61.13.206.154 done 08-19), Echo logins, yield-profile filters (notional buckets, 1034* wildcard), hedge-party filter and hold-time stats supplied. 10-14 Dan asked for Pulse login and LP average spreads by timezone; Mahi pointed him to the existing Pulse creds on their side or support@ for docs.
Next: Mahi: average LP spreads by timezone for Dan.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787118553763069 https://mahifx.slack.com/archives/C05NB72AGR2/p1792064490877339

### commercial-terms — Move from PnL share to volume-banded fee
status: open · since: 2026-09-09 · last: 2026-10-06
State: INV-1039 ($28.4k, 51 days late) was held over negative-month netting; Will C held to Schedule 1 (monthly, no carry-forward) and it was paid 09-14. 10-01 meeting: agreed to drop PnL share for a volume-banded long-term deal; 10-06 Richard accepted terms: 12-month $15k + $2.00/$1.50/$1.25 per M tiers, $20k minimum (3-month rolling $17.5k + higher tiers). Velocity CEO backs the long-term commitment.
Next: Client CFO (Tim) sign-off, then new 12-month contracts; client wants consultation before Asia widening (SLAs).
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1788953874786009 https://mahifx.slack.com/archives/CPDS0M2KF/p1790847451087629 https://mahifx.slack.com/archives/CPDS0M2KF/p1791298648881549

### hedger-reliability — Hedger switched off or crashing
status: watching · since: 2026-09-04 · last: 2026-10-01
State: 09-04 hybrid hedger left off after KAU testing into NFP (arb flat; gold +$3.2k by luck); Will C: never leave hedgers off into news. Liam/Justin proposed UI safeguards (MahiProduct PR 67 draft). 09-11 hybridHedger1 died repeatedly on unacked orders to Argamon/XTX/Kama; 10-01 crashed after DB_PRO market add.
Next: Mahi: hedger-off reminder safeguards (PR 67); investigate unacked-order crashes.
Refs: https://mahifx.slack.com/archives/CPDS0M2KF/p1788525147002129 https://mahifx.slack.com/archives/CPDS0M2KF/p1790871377514399

### kau-kilo-gold — XAU/Kilogram (KAUUSD) pricing and hedge
status: watching · since: 2026-08-25 · last: 2026-09-30
State: Priced at fixed 32.15 x XAU (rounded from 32.15074656 at client request); 3kg TOB on A feed, depth levels added. Hedge lands 32.14 (covariance vs pricing mismatch, 0.01oz residual below min clip); Mahi changed VaR gate, client accepted small residual. Ops signed off 09-18, client rolled out 09-21. 09-30 Russell asked if hedging as 32 again; thread reply not seen.
Next: Client: spread protections for KAU; Mahi confirm 32.15 hedge behaviour.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1787642723388769 https://mahifx.slack.com/archives/C05NB72AGR2/p1790778810519969

### platform-ops — LD network incident and Compass 26.4 release
status: closed · since: 2026-10-16 · last: 2026-10-17 · closed: 2026-10-19
State: LD networking incident 10-16 (client told to fail over where possible) recovered by 11:47 and declared resolved 12:30 UTC; Richard said the NDM/IG issue was unrelated. Compass 26.4 staged 10-16 and released at weekly reboots, announced complete 10-17.
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1792143214303699 https://mahifx.slack.com/archives/C05NB72AGR2/p1792164118298939

### xau-crosses — XAU/CNH and XAU/SGD crosses
status: closed · since: 2026-09-11 · last: 2026-09-24 · closed: 2026-10-15
State: XAUCNH and XAUSGD tested with USD leg hedges and signed off by Dan 09-24 (CNH flow from 1034 tags).
Refs: https://mahifx.slack.com/archives/C05NB72AGR2/p1789118712696429 https://mahifx.slack.com/archives/C05NB72AGR2/p1790246595306799

## Arc
- 2026-01-06 — Contract signed (re-papered 12 Jan), Compass + Echo pilot, $20k minimum plus 50% PnL share
- 2026-02-26 — Go-live
- 2026-04-29 — Premium channel rolled out for first tags, repeated tuning
- 2026-06-09 — Prem feed fill-rate crisis (45%)
- 2026-06-25 — CFD contract-change intent confirmed
- 2026-08-18 — Interest-only C feed live
- 2026-09-18 — KAUUSD signed off by client ops
- 2026-10-06 — Client accepts volume-banded terms replacing PnL share
