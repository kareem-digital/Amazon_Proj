# Staging API Verification — Findings

**Kab:** 6 August 2026 · `staging.vowmade.dev`
**Kaise:** Full OpenAPI spec (192 paths, 197 definitions) + 60+ authenticated GET requests
**Kyun:** `Strategy_Schema_v4.0_FINAL.md` ke open questions aur counts verify karne ke liye

🔴 **Nateeja: 14 findings mile jo mere document ko badalte hain.** Kuch counts galat the, kai enums bahut bade nikle, aur teen open questions ka jawab mil gaya.

---

## Contents

| § | Kya |
|---|---|
| 1 | 🔴 "50+ inventory" ka jawab |
| 2 | 🔴 Counts — sab galat the |
| 3 | 🔴 Enums — bahut bade nikle |
| 4 | ✅ D5 answered — kaunsa create endpoint |
| 5 | ✅ Location — David ke comments confirmed |
| 6 | 🔴 Do alag fees hain |
| 7 | ✅ D4 confirmed blocked |
| 8 | 🔴 Strategy read model — 15 naye fields |
| 9 | 🔴 403 — ek naya blocker |
| 10 | Kya-kya document me badalna hai |

---
---

# 1. 🔴 "50+ inventory" ka jawab

## Inventory sources — 50+ NAHI hain. Max 4.

`/inventory-sources/` **teen required params** leta hai — `goal`, `strategy_formats`, `markets`. Bina teeno ke 400 deta hai. To "unfiltered count" possible hi nahi hai.

Maine filters widen kar ke test kiya:

| Query | Count |
|---|---|
| `streaming_tv` + GB + AWARENESS | **2** |
| Saare 14 CTV channel formats + GB | **2** ← channels add nahi karte |
| Saare formats (display + OLV bhi) + GB | **4** ← MAX |
| GB + US | 3 |
| Saare 21 markets | 3 |
| `goal=CONVERSION` | 2 |

## Char sources ki poori list

```
Amazon Publisher Direct   type: AMAZON_PUBLISHER_DIRECT   [display, online_video]
Amazon Streaming TV       type: AMAZON                    [streaming_tv]
Third Party Exchange      type: THIRD_PARTY_EXCHANGE      [display, online_video]
Twitch                    type: AMAZON                    [display, streaming_tv]
```

🔴 **Do corrections mere document me:**

1. Maine likha tha *"koi non-AMAZON source kabhi nahi mila"* — **galat.** `THIRD_PARTY_EXCHANGE` aur `AMAZON_PUBLISHER_DIRECT` exist karte hain, bas wo `streaming_tv` serve nahi karte.
2. Maine likha tha Twitch sirf `streaming_tv` hai — **wo `display` bhi serve karta hai.**

**CTV ke liye sirf 2 sources hain. Ye pakka hai.**

## To "50+" kis cheez ka hai?

| Candidate | Count |
|---|---|
| Inventory sources | 4 |
| **Deals** | **369** ← 50+ se bahut zyada |
| `format` enum values | 21 |
| Distinct channels deal names me | ~20 asli (Prime Video, Netflix, Disney, Paramount+, PlutoTV, Tubi, Discovery+, Rakuten TV, My5, Paramount EyeQ...) |
| Product categories | **25,973** |

🔴 **Sabse likely: 369 deals.** Ya `format` enum (21 values, jisme 12 channels hain).

**Wajahat se confirm karna chahiye ki 50+ kis cheez ka number tha.**

---
---

# 2. 🔴 Counts — sab galat the

Mere document ke saare counts **filtered** views se aaye the.

| Kya | Maine likha | **Asli** | Kyun farak |
|---|---|---|---|
| **Deals** | 83 | **369** | Mera 83 `markets=GB,ZZ&formats=streaming_tv,prime_video,UNKNOWN` ke saath tha |
| **Audience sets** | 15 | **35** | UI page 1 dekha tha |
| **Assets** | 4 | **58** | UI filter lagi thi |
| **Strategies** | 361 | 362 | Ek nayi ban gayi |
| **Product categories** | (kabhi nahi ginа) | **25,973** | — |
| **Fees (markets)** | (kabhi nahi ginа) | **16 markets** | — |

## Deals ka breakdown — filters ka asar

```
Unfiltered                                          369
GB + streaming_tv                                    62
GB,ZZ + streaming_tv,prime_video,UNKNOWN             83   ← mera purana number
GB + saare 14 CTV channel formats                    62   ← streaming_tv jitna hi!
```

🔴 **Dilchasp:** saare CTV channel formats jodne se count nahi badha (62 hi raha). Par `UNKNOWN` format aur `ZZ` market jodne se 21 extra deals aa gayi. **To wo padding asal me kaam ki hai** — jaisa maine document me likha tha.

## Deal breakdown — 369 deals

```
MARKETS — 18 distinct (maine 2 likha tha!)
  GB 82 · US 78 · ES 25 · DE 23 · FR 23 · IT 23 · CA 22 · MX 20
  BR 16 · AU 14 · JP 12 · NO 3 · IE 2 · AT 2 · DK 2 · FI 2 · SE 2 · NL 1

DEAL TYPE — sirf 2
  PRIVATE_AUCTION  341  (92%)
  PREFERRED         28  (8%)
  🔴 PROGRAMMATIC_GUARANTEED — EK BHI NAHI

PRICE TYPE
  FLOOR_RATE   341  (92%)
  FIXED_CPM     28  (8%)
  ✅ Mera "lagbhag saari floor-rate" dawa CONFIRMED — asli numbers ke saath

CURRENCY — 8 distinct
  USD 156 · EUR 95 · GBP 35 · CAD 22 · MXN 19 · BRL 16 · AUD 14 · JPY 12
  🔴 GBP sirf 35 me se 369! USD dominate karta hai

ZERO-PRICED DEALS — 2 (maine 1 likha tha)
  VowMade_Fifa 2026_ZA_Football_CTV_Amazon DSP_3P_MS_MLMBRID8184
  VowMade_Fifa 2026_ZA_Football_CTV_Amazon DSP_CT_MS_MLMBRID8184
```

🔴 **Do bade points:**

1. **18 markets me deals hain**, sirf GB/US nahi. Mera *"only GB and US exist"* UI filter se aaya tha — **API me 18 hain.**
2. **92% deals floor-rate hain** — ye D3 (bid lever) ko bahut strong banata hai.

---
---

# 3. 🔴 Enums — bahut bade nikle

Ye sabse bada correction set hai. Har enum mere document se bahut bada hai.

## `goal` — 15 values, 3 nahi

```
AWARENESS · CONVERSION · CONSIDERATION · OTHER · PROSPECTING · REMARKETING ·
RETENTION · UPPER_FUNNEL_PROSPECTING · CONVERSIONS_OFF_AMAZON ·
ENGAGEMENT_WITH_MY_AD · CONSIDERATIONS_ON_AMAZON · PURCHASES_ON_AMAZON ·
MOBILE_APP_INSTALLS · PURCHASES_ON_OFF_AMAZON · MULTI_FUNNEL
```

🔴 Aur ye David ke naye comment (goal = defaulted, not fixed) ko **aur zyada zaroori** banata hai — kyunki 15 options hain, 3 nahi.

## `format` — 21 values, aur usme CHANNELS hain

```
standard_display · amazon_mobile_display · aap_mobile_app · video · display ·
online_video · streaming_tv · prime_video · discovery · paramount · channel4 ·
netflix · disney · pluto · bskyb · hulu · tubi · roku · vevo · dazn · other
```

🔴🔴 **Ye Comment 14 ke nateeje ko badalta hai.**

David ne kaha tha *"Prime Video ek channel hai, format nahi"* — **par API me `netflix`, `disney`, `paramount`, `channel4`, `pluto`, `bskyb`, `hulu`, `tubi`, `roku`, `vevo`, `dazn`, `discovery` — sab FORMAT values hain.**

**API "format vs channel" ka farak nahi karta. API ka `format` enum HI channel list hai.**

Aur ye samjhata hai ki forecast me `prime_video` kyun matter karta hai — kyunki us API me **format hi channel dimension hai**.

## `kpi` — 16 values, 6 nahi

```
REACH · FREQUENCY · COST_PER_VIDEO_COMPLETION · VIDEO_COMPLETION_RATE ·
CLICK_THROUGH_RATE · COST_PER_CLICK · COST_PER_DETAIL_PAGE_VIEW ·
DETAIL_PAGE_VIEW_RATE · RETURN_ON_AD_SPEND · TOTAL_RETURN_ON_AD_SPEND ·
COMBINED_RETURN_ON_AD_SPEND · COST_PER_INSTALL · COST_PER_ACTION ·
COST_PER_FIRST_APP_OPEN · COST_PER_SIGN_UP · OTHER
```

## 🔴 Aur `automated-strategies` me KPI list CHHOTI hai — sirf 5

```
RETURN_ON_AD_SPEND · TOTAL_RETURN_ON_AD_SPEND · COST_PER_ACTION ·
REACH · FREQUENCY
```

🔴 **Ye D12 ka aadha jawab hai.** Agent wale endpoint ka KPI set **already defined hai** — 5 values. Aur wo goals se map karte hain:

```
REACH, FREQUENCY                                    →  Awareness
COST_PER_ACTION                                     →  Conversion
RETURN_ON_AD_SPEND, TOTAL_RETURN_ON_AD_SPEND        →  Conversion
```

## `primary_currency` — 19 values, 3 nahi

```
USD · MXN · CAD · BRL · AED · SAR · GBP · EUR · SEK · TRY · AUD · INR ·
SGD · JPY · NOK · DKK · NZD · CNY · CHF
```

✅ **D31 answered.** `NOK` list me hai — enum extend karne ki zaroorat nahi, wo already hai. Mera *"sirf EUR/GBP/USD"* **galat** tha.

## `market` — 21 values, 2 nahi

```
AU · AT · BE · BR · CA · FR · DE · IN · IT · JP · MX · NL · NZ · SA ·
SG · ES · SE · TR · AE · GB · US
```

🔴 Mera *"only GB and US"* UI filter se tha. **API me 21 markets hain, aur 18 me actual deals hain.**

## `conversion_type` — 6 values, 4 nahi — aur MARKET-SPECIFIC

```
ADD_TO_SHOPPING_CART   [GB, US]
APPLICATION            [GB, US]
CHECKOUT               [GB]        ← sirf GB
OTHER                  [US]        ← sirf US
PAGE_VIEW              [GB]        ← sirf GB
SEARCH                 [US]        ← sirf US
```

🔴 **Do naye events** (`SEARCH`, `OTHER`), aur **market ke hisab se alag hain.** Maine document me 4 likhe the aur market flag ka zikr kiya tha par values nahi.

## `status` — 4th value CONFIRMED

Test strategy ka `status: "4_not_running"`.

✅ **Mera inferred ordering sahi tha:**
```
1_delivering · 2_out_of_budget · 3_ended · 4_not_running ·
5_ready_to_deliver · 6_inactive
```
Ab 3 confirmed hain (`3_ended`, `4_not_running`, `6_inactive`).

---
---

# 4. ✅ D5 answered — kaunsa create endpoint

**Teeno endpoints ke request schemas mil gaye.**

## `POST /simple-strategies/` — 9 fields, 4 required

```
* name              string
* flight_dates      object
* market            string      ← SINGULAR!
* format            string      ← SINGULAR!
  budget            string
  impression_target integer     ← 🔴
  id, is_archived, is_readonly
```

🔴 **Ye CTV variant NAHI hai** — ye ek **minimal single-market, single-format shell** hai. Aur usme `impression_target` hai.

## `POST /automated-strategies/` — 18 fields, 6 required

```
* name                 string
* flight_dates         object
* markets_info         [MarketInfo]
* primary_currency     string
* product_location     string
* formats_and_kpis     [AutomatedStrategyFormatsAndKpis]   ← KPI sirf 5 values
  goals                [string]      ← 🔴 PLURAL, array!
  market_deals         [MarketDeals]
  assets               [VowAssetMarkets]
  conversion_types     [string]
  asin_numbers         string
  draft_id             string        ← 🔴 draft workflow
  pre_approved_creatives, third_party_creatives, rec_creatives
```

## `POST /strategies/` — required: 6, wahi 6

```
name · primary_currency · flight_dates · product_location ·
formats_and_kpis · markets_info
```

## 🔴 Nateeja

| Endpoint | Kis kaam ka |
|---|---|
| `simple-strategies` | Minimal shell — ek market, ek format, budget **ya** impression target |
| `automated-strategies` | **Poora planning payload** — markets_info, formats_and_kpis, deals, assets, conversions, draft_id |
| `strategies` | Product ka wizard yahi use karta hai |

🔴 **`automated-strategies` agent ke liye sabse fit lagta hai** — usme sab kuch hai jo plan me chahiye, aur uska KPI set already 5 par restricted hai.

## Aur confirmation — strategy record batata hai kaunse endpoint se bana

Test strategy me:
```
is_simple:    false
is_automated: false
```

🔴 **To dono flags exist karte hain, aur strategy record karta hai ki wo kis endpoint se bani.** Ye D5 ke liye seedha saboot hai.

---
---

# 5. ✅ Location — David ke comments CONFIRMED

## Comment 32 — include/exclude

**Spec me exactly wahi hai:**

```
StrategyLocation:
  * include : [StrategyTargetLocation]
  * exclude : [StrategyTargetLocation]       ← CONFIRMED

UpdateStrategyLocation:              ← jo POST karte waqt bhejte hain
  * include : [string]               ← sirf IDs
  * exclude : [string]

StrategyTargetLocation:              ← jo GET par milta hai
  * amz_id      string               ← Amazon ka location ID
  * name        string               ← trader ko dikhane wala label
  * filter_type string {INCLUDE, EXCLUDE}
  * market      string {21 markets}
  * category    string

StrategyLocationSummary:
  * market · filter_type · count
```

✅ **David ka comment 32 bilkul sahi hai, aur API already support karta hai.**

## Comment 31 — search

`GET /strategies/locations/GB/` bina query par 400 deta hai:
```
["Query must be at least 2 characters long"]
```

**To ye ek SEARCH endpoint hai.** `?query=SW1` bhejne par:

```json
{
  "nextToken": null,
  "geoLocations": [
    {"name": "London, England, UK - SW1Y", "id": "XHvCjcKHXsKGemnCjsKQbMKX", "category": "POSTAL_CODE"},
    {"name": "London, England, UK - SW1X", "id": "XHvCjcKHXsKGemnCjsKQbMKW", "category": "POSTAL_CODE"},
    ...
  ]
}
```

✅ **Teen cheezein confirm hui:**

1. **Locations IDs hain, free text nahi** — `id` ek opaque string hai (`XHvCjcKHXsKGemnCjsKQbMKX`), numeric bhi nahi
2. **Search chahiye** — minimum 2 characters
3. **`category` field hai** — `POSTAL_CODE` mila; CITY/REGION/COUNTRY bhi hone chahiye

🔴 **Aur ye Amazon ka geo API passthrough hai** — `nextToken` aur `geoLocations` Amazon ki naming hai.

## Comment 34 — radius

Spec me `POST /strategies/locations/{market}/` maujood hai. ✅ David ka jawab confirmed.

---
---

# 6. 🔴 Do alag fees hain — mera document galat tha

Mere `Strategy_Schema_v4.0_FINAL.md` §4.4.5 me likha hai:

> *"Fee rates are read, not specified. GET /api/contextual-targeting/fees returns the rates."*

🔴 **Wo galat hai. Wo endpoint audience fee nahi deta.**

## Fee 1 — Audience data fee (audience set par)

```json
{
  "standard_display_fee": "0.59",
  "video_fee": "1.63",
  "fee_currency": "GBP"
}
```
✅ Mera 1.63 wala number **sahi** tha. Ye **audience set object par** hota hai.

## Fee 2 — Contextual targeting fee (alag endpoint)

`GET /api/contextual-targeting/fees` — **16 markets**, per market teen rates:

```
market   currency   display   online_video   stv
AE       AED        0.825     1.650          1.650
AU       AUD        0.300     0.450          0.450
BR       BRL        0.450     1.275          1.275
CA       CAD        0.300     0.450          0.450
DE       EUR        0.180     0.450          0.450
ES       EUR        0.108     0.450          0.450
FR       EUR        0.147     0.450          0.450
GB       GBP        0.162     0.450          0.450
```

🔴 **Path dekho: `contextual-targeting/fees`.** Ye **contextual (product category) targeting** ki fee hai, **audience targeting** ki nahi.

## Nateeja

```
Audience fee      →  audience set object par (video_fee 1.63 GBP)
Contextual fee    →  /contextual-targeting/fees (GB stv 0.450 GBP)
                     per market, teen format rates
```

**Do bilkul alag fees. Aur dono ek plan me lag sakti hain** — agar audience aur product-category targeting dono use ho.

🔴 **Ye document me correction chahiye.** Aur ek naya sawaal: kya dono fees stack hoti hain?

---
---

# 7. ✅ D4 confirmed blocked

Deal object ke saare fields (369 deals se verify kiya):

```
✅ external_deal_id · name · deal_type · deal_price_type ·
   deal_price_amount · deal_price_currency · media_types ·
   devices · environments · locations · genre · ad_lengths

❌ channel            — NAHI HAI
❌ inventory_tier     — NAHI HAI
❌ provider           — NAHI HAI
❌ publisher          — NAHI HAI
```

✅ **D4 pakka blocked hai.** Channel aur tier deal par **exist nahi karte**. Agent ko naam parse karna padega.

## Aur genre ki halat confirm

Teen Paramount deals dekhi — teeno me `genre: null`, jabki naam me channel likha hai:

```
3PS_Freewheel_UK_STV_Paramount_My 5           genre: null
3PS_Freewheel_UK_STV_Paramount_Paramount+     genre: null
3PS_Freewheel_UK_STV_Paramount_PlutoTV        genre: null
```

## Deal names ke aath prefix — parsing kitni mushkil hai

```
(pipe-form)  148   "Prime Video | Preferred Deal | Video | UK - 15, 20 – ROS"
3PS          129   "3PS_Freewheel_UK_STV_Paramount_My 5"
VowMade       78   "VowMade_Fifa 2026_ZA_Football_CTV_Amazon DSP_3P_MS_MLMBRID8184"
EB             6
Tubi           4
TUBI           2   ← casing bhi inconsistent!
62797          1
APC            1
```

🔴 **Aath alag naming conventions.** Ek parser sabko handle nahi kar sakta. **Ye D4 ko aur strong banata hai.**

---
---

# 8. 🔴 Strategy read model — 15 naye fields

Test strategy `VMA2026368` me **40 keys** hain. Maine document me 20 likhe the.

## Naye fields aur unki values

| Field | Value | Kya lagta hai |
|---|---|---|
| `is_simple` | `false` | 🔴 Kaunse endpoint se bani |
| `is_automated` | `false` | 🔴 Kaunse endpoint se bani |
| `impression_target` | `null` | 🔴 **D38 answered** — budget ke bajaye impressions par plan ho sakta hai |
| `allocation_mode` | `"BUDGET"` | Budget ya impressions par allocate |
| `creative_duration_allocation_mode` | `"budget"` | 🔴 lowercase! Casing inconsistent |
| `creative_durations` | `[]` | Durations strategy par store hoti hain |
| `creative_rotation_type` | `"RANDOM"` | Creative rotation ka control |
| `content_rating_exclusions` | `[]` | 🔴 Brand safety — par "content **rating**", category nahi |
| `user_location_signal` | `"CURRENT"` | 🔴 **Poora naya concept** |
| `audiences_cpm` | `null` | 🔴 Audience fee strategy par store hoti hai |
| `planned_cpm` | `null` | Plan kiya hua CPM |
| `cpm_target` | `null` | CPM ka target |
| `pacing_ratio` | `null` | Delivery pacing |
| `can_be_extended` | `true` | Flight extend ho sakti hai |
| `last_exported` | — | Export tracking |
| `kpis` | — | 🔴 Plural |

## 🔴 Teen bade points

**1. `impression_target` exist karta hai — D38 answered.**

Client ki question list me tha: *"Do you want to plan against a fixed budget or an impression target?"* — **platform ise support karta hai.** `simple-strategies` payload me bhi hai, aur strategy record par bhi.

**2. `user_location_signal: "CURRENT"` — ek naya targeting concept.**

Ye mere kisi bhi document me nahi hai. ⚠️ Andaza: user ki **current** location target karein ya **home** location. Values pata nahi.

**3. Ek poori delivery-control layer maine document nahi ki thi.**

`pacing_ratio`, `planned_cpm`, `cpm_target`, `allocation_mode`, `creative_rotation_type`, `creative_duration_allocation_mode` — ye sab delivery ke controls hain jo mere spec me nahi hain.

---
---

# 9. 🔴 403 — ek naya blocker

Ye endpoints **403 Forbidden** dete hain (session valid hai, par permission nahi):

```
403  GET /admin/advertiser/                                    advertiser list
403  GET /admin/advertiser/{id}/                               🔴 ADVERTISER DEFAULTS
403  GET /admin/advertiser/get_channels_choices/               channel list
403  GET /admin/advertiser/get_deal_exchange_choices/          exchange list
403  GET /admin/advertiser/get_industry_and_sub_industry_choices/
```

## 🔴 Ye Comment 13 ko block karta hai

Comment 13 ka poora concept **advertiser profile defaults** hai — frequency cap, device types, product categories, selling location. Uska endpoint:

```
GET /api/admin/advertiser/{id}/       →  403 Forbidden
```

**Agent ye padh hi nahi sakta.**

🔴 **Ye ek naya blocking question hai.** Do possibilities:

1. Trader account ko `/admin/` access nahi hai — agent ko ek **service account** chahiye
2. Advertiser defaults kisi **doosre** (non-admin) endpoint par hain jo maine nahi dhunda

**Ye Wajahat/David se puchna hai.**

---
---

# 10. Kya-kya document me badalna hai

`Strategy_Schema_v4.0_FINAL.md` me ye corrections chahiye:

## Counts

| § | Kya likha hai | Kya hona chahiye |
|---|---|---|
| 4.2.3 | "83 deals" | **369** deals. GB+streaming_tv par 62 |
| 4.4.1 | "15 audience sets" | **35** |
| 6.12 | "4 assets" | **58** |
| 4.2.3 | "one deal priced at zero" | **do** deals |

## Enums

| § | Kya likha hai | Kya hona chahiye |
|---|---|---|
| 6.2 | markets "GB aur US only" | **21 markets** enum me, **18** me actual deals |
| 4.5 | currency "EUR, GBP, USD" | **19 currencies**. `NOK` already hai — **D31 closed** |
| 4.8 | goal 3 values | **15 values** |
| 4.6 | format 4 values | **21 values**, aur usme 12 channels |
| 4.8 | KPI 6 values | **16** overall, par `automated-strategies` me **5** |
| 6.2 | conversion 4 events | **6 events**, aur market-specific |
| 3.4 | status ordering "Inferred" | `4_not_running` **confirmed** — 3 me se 3 |

## Positions jo badalti hain

| § | Kya |
|---|---|
| **4.4.5** | 🔴 Audience fee `/contextual-targeting/fees` se **nahi** aati. Wo alag fee hai. Audience fee audience set object par hai |
| **4.6.1** | 🔴 API "format vs channel" ka farak **nahi** karta — `format` enum hi channel list hai |
| **4.3** | Inventory source `type` ke **3 values** hain, sirf AMAZON nahi. Aur Twitch `display` bhi serve karta hai |
| **8.6** | Strategy read model me **40 keys**, 20 nahi |

## Open questions jo band ho gaye

| # | Kya tha | Jawab |
|---|---|---|
| **D5** | Kaunsa create endpoint | `automated-strategies` sabse fit — 18 fields, 6 required, KPI set 5 par restricted. Aur `is_simple`/`is_automated` flags saboot hain |
| **D12** | Goal-to-KPI mapping | Aadha mila — `automated-strategies` ka KPI set 5 values par restricted hai |
| **D31** | Currency enum extend karein | Nahi — 19 currencies already hain, `NOK` sameth |
| **D38** | Impression target M1 me | Platform **support karta hai** — `impression_target` field hai |
| **Comment 31/32/34** | Location | Sab confirmed — include/exclude, search, radius |
| **D4** | Deal matching fields | **Blocked confirmed** — channel/tier nahi hain, aur 8 naming conventions hain |

## Naye open questions

| # | Sawaal | Kyun |
|---|---|---|
| **D47** | 🔴 `/admin/advertiser/{id}/` **403** deta hai. Agent advertiser defaults kaise padhega — service account chahiye, ya koi doosra endpoint hai? | Comment 13 ka poora concept isi par khada hai |
| **D48** | `user_location_signal` kya hai? Values kya hain? (`CURRENT` mila) | Ek naya targeting concept, kisi document me nahi |
| **D49** | Audience fee aur contextual fee dono stack hoti hain? | Do alag fees hain |
| **D50** | `pacing_ratio`, `planned_cpm`, `cpm_target`, `allocation_mode`, `creative_rotation_type` — ye agent set karega ya platform? | Ek poori delivery-control layer |
| **D51** | `content_rating_exclusions` — "content rating" hai ya "content category"? | Brand safety ka field, par naam alag hai |
| **D52** | `format` enum me channels hain — to Comment 14 ka "Prime Video is a channel not a format" API ke against kaise reconcile karein? | Model aur API me farak |
| **D53** | Deal names ke **8 naming conventions** hain, aur casing bhi inconsistent (`Tubi` vs `TUBI`). Ek controlled channel field mil sakta hai? | D4 ka aur strong version |
| **D54** | "50+ inventory" kis cheez ka count tha — 369 deals, ya 21 format values? | Inventory sources sirf 4 hain |

---

## Ek line me

> **Mere document ke counts sab filtered views se aaye the aur chhote the. Enums bahut bade nikle — goal 15, format 21, KPI 16, currency 19, market 21. Teen open questions band ho gaye (D5, D31, D38), David ke location comments sab confirmed hue, aur ek naya blocker mila — advertiser defaults ka endpoint 403 deta hai.**

---

**Raw responses:** scratchpad ke `api_responses/`, `api_responses2/`, `api_responses3/` folders me — 60+ JSON files, jisme poore 369 deals aur strategy read model bhi hai.

**Probe scripts:** `api_probe.py`, `api_probe2.py`, `api_probe3.py` — credentials env se padhte hain, file me hardcode nahi hain.
