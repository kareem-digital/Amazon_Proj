# VOW Platform — Strategy Module ki Poori Mastery

**Ye document kya hai:** VOW Platform ke Strategy Module ka A-to-Z. Har screen, har field, har API, har payload, har response — jo maine `staging.vowmade.dev` par ek poori strategy banate hue observe kiya.

**Kis liye:** Planning Agent ka main module yahi hai. Implementation se pehle poora module clear hona chahiye, aur team me koi bhi kuch bhi poochhe to turant jawab de sakein.

**Observed on:** `staging.vowmade.dev` · 4 August 2026
**Test strategy banayi:** `CTV Test GB Sep2026 KA` → `VMA2026368`

---

## Kaise padhein

| Marker | Matlab |
|---|---|
| ✅ VERIFIED | Maine khud API me dekha — payload ya response me confirm hai |
| 🔍 OBSERVED | Screen par dekha, par API me confirm nahi kiya |
| ⚠️ INFERRED | Andaaza, saboot ke saath — par pakka nahi |
| ❓ UNKNOWN | Pata nahi, poochhna hai |

Jahan bhi maine kuch maana hai, wahan marker lagaya hai. **Bina marker wali baat = verified.**

---

# HISSA 1 — Strategy Module kya hai

## 1.1 Ek line me

**Strategy = ek advertising campaign ka poora plan.** Kis market me, kitne paise me, kaunsi inventory par, kis audience ko, kaunsa video dikhana hai — sab ek Strategy object me.

## 1.2 Purpose — ye module kis samasya ko hal karta hai

VOW ek **DSP reseller** hai. Amazon DSP par ad chalane ke liye advertiser ko chahiye:

```
1. Kaunse market me chalana hai
2. Kitna budget
3. Kaunsi inventory (Prime Video? Netflix? Twitch?)
4. Kis audience ko
5. Kaunsa video creative
6. Kya measure karna hai
```

Strategy Module **ye saara plan ikattha karta hai**, phir usse **Amazon DSP par publish** kar deta hai. Amazon par wo Campaigns aur Ad Groups ban jaate hain.

**To Strategy Module ka kaam:** trader ka iraada → ek structured plan → Amazon DSP par live campaign.

## 1.3 Module kahan hai

```
Sidebar → Strategy icon (doosra item)
URL: staging.vowmade.dev/app/strategies?aid={advertiser_uuid}
```

Poora module **ek advertiser ke andar** kaam karta hai. `aid` (advertiser UUID) sab kuch scope karta hai. Cross-advertiser kuch nahi hai.

## 1.4 Data hierarchy — ye samajhna sabse zaroori hai

```
Advertiser                    UUID — 353eea43-bc42-456f-ba4f-3d3e20ea6bc8
│                             "Vow Made" — header dropdown se chunte hain
│
└── Strategy                  ID — VMA2026368  (VMA + saal + sequence)
    │                         Ye Strategy Module ka main object hai
    │
    ├── Flight Ranges[]       ✅ Ek strategy me KAI flight ranges ho sakti hain
    │   └── Market            └── Format → budget
    │                         September me chalao, phir November me alag budget se
    │
    ├── markets_info[]        Per market: bid · budget · currency · audiences
    ├── market_deals[]        Per market: deals[]
    ├── assets[]              Campaign-level (per market nahi)
    ├── Locations             Targeting — creation ke BAAD set hoti hai
    │
    └── Campaigns[]           Amazon par sync hone ke baad bante hain
        └── Ad Groups[]       Amazon DSP ki apni hierarchy
```

🔴 **Do cheezein yaad rakho:**
1. **Market** poore payload ka organising unit hai — budget, bid, currency, audiences, deals sab per-market hain
2. **Flight ranges ek list hain**, ek value nahi

---

# HISSA 2 — Vocabulary (har technical shabd ka matlab)

Ye sab shabd is module me aate hain. Ek baar samajh lo, poora document aasan ho jaayega.

## 2.1 Platform ke shabd

| Shabd | Matlab |
|---|---|
| **Strategy** | Poora campaign plan. Is module ka main object. ID = `VMA2026368` |
| **Campaign** | Strategy ke andar — Amazon DSP par sync hone ke baad banta hai |
| **Ad Group** | Campaign ke andar — Amazon DSP ki sabse chhoti unit |
| **Flight Range** | Ek date range jisme campaign chalega. Ek strategy me kai ho sakti hain |
| **Advertiser** | Jiska ad hai. Poora module iske andar scoped hai |
| **DSP** | *Demand Side Platform* — jahan se ad khareedte hain (Amazon DSP) |
| **SSP / Exchange** | *Supply Side Platform* — jahan se inventory aati hai (Freewheel, Pubmatic, Magnite) |
| **Inventory** | Ad dikhane ki jagah — Prime Video ke slots, Netflix ke slots |
| **Inventory Source** | Inventory ka bada source — `Amazon Streaming TV`, `Twitch` |
| **Deal** | Ek specific inventory ka sauda, apne CPM ke saath |
| **Asset** | Video **file** — `/api/assets/` |
| **Creative** | Asset + click-through URL + market, Amazon par register hua — `/api/creatives/` |
| **Audience Set** | Segments ka ek bundle, boolean logic ke saath |
| **Audience / Segment** | Ek single targeting group — "Females", "Healthy Food" |

## 2.2 Paise ke shabd

| Shabd | Matlab | Formula |
|---|---|---|
| **CPM** | *Cost Per Mille* — 1,000 impressions ka daam | — |
| **eCPM** | *Effective CPM* — jo actually kharch hua | `spend ÷ impressions × 1000` |
| **VCPM** | *Viewable CPM* — audience data ki fee | — |
| **FIXED_CPM** | Daam pakka hai. Bid ka koi kaam nahi | — |
| **FLOOR_RATE** | Minimum daam. Uske **upar bid** karna padta hai, compete karna padta hai | — |
| **Base bid** | Aap kitna bid karenge — sirf FLOOR_RATE deals par matter karta hai | — |
| **Budget at risk** | ❓ Column exist karta hai, matlab confirm nahi. Shayad commit hua par deliver nahi hoga |

## 2.3 Deal types

| Type | Price | Bid ka kaam? | Kahan mila |
|---|---|---|---|
| `PREFERRED` | `FIXED_CPM` | ❌ Nahi | Prime Video deals |
| `PRIVATE_AUCTION` | `FLOOR_RATE` | ✅ **Haan** | Netflix, Freewheel, sab 3P — **aur Prime Video ke bhi kuch** |
| `PROGRAMMATIC_GUARANTEED` | ❓ | ❓ | Filter me option hai, par **koi deal nahi mili** |

🔴 **Zaroori:** 83 deals me se **lagbhag sab `PRIVATE_AUCTION` + `FLOOR_RATE`** hain. Isliye **base bid required hai.**

## 2.4 Performance metrics (list screen par 25 columns hain)

| Shabd | Poora naam | Matlab |
|---|---|---|
| **Impressions** | — | Ad kitni baar dikha |
| **Reach** | — | Kitne **unique log** ne dekha |
| **Frequency** | — | Ek banda hafte me kitni baar dekhta hai (**per week** — screen par likha hai) |
| **CTR** | Click-through rate | `clicks ÷ impressions` |
| **VCR** | Video completion rate | Video poora dekha gaya ⚠️ staging me 128% aa raha hai — galat hai |
| **VR** | View rate / viewability | Ad screen par asal me dikha |
| **DPVR** | Detail page view rate | Kitne log Amazon product page tak gaye |
| **CPA** | Cost per acquisition | `spend ÷ conversions` |
| **ROAS** | Return on ad spend | `revenue ÷ spend`. 2.58 = ₹1 par ₹2.58 wapas |
| **ACOS** | Advertising cost of sale | ROAS ka ulta |
| **c_roas** | Click-attributed ROAS | Sirf click se aayi sales |
| **t_roas** | Total ROAS | Sab milakar |
| **ecpc** | Effective cost per click | — |
| **cpvc** | Cost per video completion | — |
| **cpdpv** | Cost per detail page view | — |
| **bid_request_volume** | — | Kitni inventory **available** hai — supply ka size |

## 2.5 Amazon-specific

| Shabd | Matlab |
|---|---|
| **ASIN** | Amazon Standard Identification Number — product ka ID |
| **On Amazon / SOLD_ON_AMAZON** | Advertiser Amazon par bechta hai → ASIN se track hoga (endemic) |
| **Off Amazon / NOT_SOLD_ON_AMAZON** | Apni website par bechta hai → **Ad Tag** se track hoga (non-endemic) |
| **Ad Tag** | Website par lagne wala tracking code |
| **Halo sales** | Off-Amazon advertiser ki Amazon par indirect sales |
| **amz_id** | Amazon ka apna ID — creatives aur audiences par hota hai, VOW ke `id` se alag |
| **dsp_approved** | Asset Amazon DSP se approve ho chuka hai — bina iske use nahi ho sakta |

---

# HISSA 3 — Flow ka poora naksha

## 3.1 Manual flow — 6 steps + list + post-creation

```
┌─ SCREEN 1 ─────────────────────────────────────────────────┐
│  Strategies list                                           │
│  361 strategies · 25 columns · 4 filters                   │
│  [ New Strategy ] button                                   │
└────────────────────────┬───────────────────────────────────┘
                         ↓
┌─ WIZARD — 6 steps, sab CLIENT-SIDE (kuch save nahi hota) ──┐
│                                                            │
│  STEP 1  Strategy details                                  │
│          name · dates · markets · currency · formats        │
│          · product categories · On/Off Amazon · ASINs      │
│          → 4 PRE-FLIGHT CHECKS chalti hain                 │
│                                                            │
│  STEP 2  Goal, KPI & Bid                                   │
│          goal · KPI (PER FORMAT!) · KPI target value        │
│          · inventory sources · conversions · budget · bid   │
│          → name uniqueness check                            │
│                                                            │
│  STEP 3  Deals                                             │
│          83 deals me se checkbox tick karo                  │
│                                                            │
│  STEP 4  Audiences                                         │
│          15 audience sets me se tick karo                   │
│                                                            │
│  STEP 5  Creatives                                         │
│          4 assets me se tick karo                           │
│          → asset tick karne par uske creatives fetch hote   │
│                                                            │
│  STEP 6  Summary                                           │
│          sab review · REACH FORECAST chalta hai             │
│          [ Create Strategy ]                                │
└────────────────────────┬───────────────────────────────────┘
                         ↓
              POST /api/strategies/  →  201  →  VMA2026368
                         ↓
┌─ POST-CREATION — Strategy overview page ───────────────────┐
│  Status: Paused · Inactive · Syncing ⟳                      │
│                                                            │
│  Overview  ·  Planner  ·  Campaigns  ·  Creatives          │
│  Audience sets  ·  Locations  ·  Strategy history          │
│                                                            │
│  🔴 TARGETING (Locations) YAHAN HAI — creation me nahi      │
│  🔴 BUDGET SPLIT (Planner) YAHAN HAI — creation me nahi     │
└────────────────────────────────────────────────────────────┘
```

## 3.2 🔴 Teen cheezein jo flow ke baare me zaroori hain

**1. Wizard poora client-side hai.** Steps ke beech **kuch save nahi hota**. Sirf ek call jaati hai — name uniqueness check. Poora plan browser me banta hai aur **aakhir me ek POST** se create hota hai.

**2. Wizard ki lambai dynamic hai.** Step 1 par stepper `1-2-3-4-5` dikhta hai. Do formats chunne par `1-2-3-4-5-6` ho jaata hai. **Format jodne se step badh jaata hai.**

**3. Targeting creation ke baad hi ho sakti hai.** Saare targeting endpoints `/api/strategies/{id}/targeting/…` hain — **strategy ID chahiye**. Isliye:

```
❌ Ye order buildable NAHI hai:
   plan → targeting → forecast → create

✅ Ye order buildable hai:
   plan → forecast → create → phir targeting, locations, budget split
```

---

# HISSA 4 — Screen 1: Strategies List

## 4.1 URL aur scope

```
staging.vowmade.dev/app/strategies
    ?aid=353eea43-bc42-456f-ba4f-3d3e20ea6bc8
    &dateRange=lifetime
    &includeArchived=false
    &page=1&pageSize=20&ordering=name
```

Screen ka poora state URL me hai — linkable aur bookmarkable.

## 4.2 Do kaam ek saath

Ye screen **do cheezein** karti hai, aur dono aapas me kheenchti hain:
1. **Register** — strategy dhoondho, status dekho, kholo
2. **Performance report** — 25 columns, zyadatar delivery aur sales metrics

25 me se sirf ~10 columns plan describe karte hain, baaki **outcomes** hain.

Aur yahi **campaign banane ka entry point** hai — `New Strategy` button.

## 4.3 Header controls

| Control | Kaam |
|---|---|
| **Lifetime** (date range) | `metrics_date_range` set karta hai — metrics kis window ke hain. Kaunsi strategies dikhengi ye **nahi** badalta |
| **Vow Made** (advertiser) | `aid` set karta hai. Poora page iske andar |
| **Credit available €999,889.82** | Account balance. Yahi figure activation ke credit check me use hota hai |
| **Display** | Column chooser — kaunse 25 columns dikhane hain |
| **New Strategy** | Wizard shuru |

## 4.4 Filters — poori lists

**Market** — checkboxes, multi-select
```
☐ 🇬🇧 United Kingdom
☐ 🇺🇸 United States
```
🔴 **Sirf do markets hain.** Aur kuch nahi.

**Status** — checkboxes, **aath values**
```
☐ Delivering          ☐ Ready to deliver
☐ Out of budget       ☐ Inactive
☐ Ended               ☐ Archived
☐ Not running         ☐ Draft
```

API me values numbered hain: `"3_ended"`, `"6_inactive"` ✅ dekha hai.
⚠️ INFERRED ordering (filter list ke order se):
```
1_delivering · 2_out_of_budget · 3_ended · 4_not_running · 5_ready_to_deliver · 6_inactive
```
Sirf 3 aur 6 ki exact strings confirm hain.

🔴 **`Archived` aur `Draft` status nahi hain** — wo alag booleans hain (`is_archived`, `is_draft`). Draft rows ka `status: "6_inactive"` hai. To **sirf status padhne wala draft ko inactive samjhega.**

**Format** — checkboxes, **chhah values**
```
☐ Display          ☐ Prime Video
☐ Online Video     ☐ Netflix
☐ Streaming TV     ☐ Disney+
```
🔴 Par **creation me sirf chaar** hain — Netflix aur Disney+ create karte waqt chun nahi sakte.

**Location** — radio, **single-select**
```
◯ On Amazon
◯ Off Amazon
```
🔴 Ye asal me `product_location` hai. **Filter me naam "Location", column me naam "Channels", API me `product_location`** — teen naam.

## 4.5 25 columns

**Plan attributes (8)**

| Column | Matlab |
|---|---|
| **Strategy** | Naam + code `VMA2025107`. Ye code hi `id` hai ✅ |
| **Status** | `3_ended`, `6_inactive` |
| **Goal** | Awareness / Consideration / Conversion |
| **Flight dates** | Start – end |
| **Budget** | Plan kiya hua kharch. Drafts me `null` ✅ |
| **Markets** | Country flags — kai ho sakte hain |
| **Formats** | `Display +3` — kai formats |
| **Channels** | On Amazon / Off Amazon → asal me `product_location` |

**Delivery metrics (7)**
`Spend` · `Budget at risk` · `Impressions` · `eCPM` · `CTR` · `VCR` · `VR`

**Sales metrics (10) — teen family me**

| Family | Columns | Kya naapta hai |
|---|---|---|
| **Off-Amazon** | CPA, Product Sales, Purchases, ROAS | Advertiser ki **apni site** par, ad tag se |
| **On-Amazon** | Product Sales, Purchases, ROAS | **Amazon** par, ASIN se |
| **Total** | Total ROAS, Total Sales | Dono ka jod |

## 4.6 Row indicators

| Indicator | Matlab |
|---|---|
| 🟠 Orange ⓘ | Sync fail — `failure_reason: "CAMPAIGN_SYNC_ISSUES"` ✅ |
| ⟳ Spinner | `is_syncing: true` ✅ |

## 4.7 API 1 — Credit balance

```
GET /api/credits/summary/?advertiser=353eea43-bc42-456f-ba4f-3d3e20ea6bc8
200 OK · Content-Length 56
Allow: GET, HEAD, OPTIONS
```
Query: `advertiser` = advertiser UUID.
Response: header ka "Credit available €999,889.82" bharta hai.

## 4.8 API 2 — User preferences

```
GET /api/reports/user-preferences/
200 OK · 0.3 kB
```
Kaunse columns dikhane hain, page size — user ki saved settings.

## 4.9 API 3 — Strategy list (main call)

```
GET /api/strategies/
    ?metrics_date_range=&markets=&formats=&product_locations=&goal=&search=
    &page=1&page_size=20&ordering=name&include_archived=false&currency_type=primary

200 OK · Content-Length 21654 · 1.36 s
Allow: GET, POST, HEAD, OPTIONS
Vary: Accept, Cookie, origin
```

**Gyarah query parameters**

| Parameter | Kaam |
|---|---|
| `metrics_date_range` | Metrics ka window. Khaali = lifetime |
| `markets` | Market filter |
| `formats` | Format filter |
| `product_locations` | 🔴 UI me "Channels"/"Location" filter |
| `goal` | Goal filter — **screen par exposed nahi hai** par API accept karta hai |
| `search` | Search box |
| `page` · `page_size` | Pagination |
| `ordering` | Sort — `name` |
| `include_archived` | Archived toggle |
| `currency_type` | `primary` — paise kis currency me dikhane hain |

🔴 **`advertiser` parameter NAHI hai** (credits call me tha). `Vary: Cookie` batata hai ki advertiser **session me** hai. Browser URL ka `aid` sirf front-end state hai.

**Response — DRF pagination**

```json
{
  "count": 361,
  "next": "http://staging.vowmade.dev/api/strategies/?…&page=2&page_size=20…",
  "previous": null,
  "results": [ … 20 strategy objects … ]
}
```

**Ek strategy object — 20 fields**

```json
{
  "id": "VMA2025107",
  "name": "0098y7yiujhhiu7tyu",
  "channel_type": "dsp",
  "goal": "AWARENESS",
  "budget_at_risk": "0.00",
  "primary_currency": "EUR",
  "flight_dates": { "lower": "2025-02-28", "upper": "2025-02-28", "timezone": "UTC" },
  "product_location": "NOT_SOLD_ON_AMAZON",
  "delivery_activation_status": "INACTIVE",
  "formats": ["display", "online_video", "streaming_tv"],
  "markets": ["US"],
  "metrics": { … 29 fields … },
  "status": "3_ended",
  "budget": "3.64",
  "is_draft": false,
  "is_syncing": true,
  "failure_reason": "CAMPAIGN_SYNC_ISSUES",
  "is_archived": false,
  "is_readonly": true,
  "is_automated": false
}
```

**Paanch boolean flags:** `is_draft` · `is_syncing` · `is_archived` · `is_readonly` · `is_automated`
**Do status fields:** `status` (lifecycle) aur `delivery_activation_status` (deliver ho raha hai ya nahi)

**`metrics` object — 29 fields**

| Group | Fields |
|---|---|
| Counts | `impressions`, `click_throughs`, `viewable_impressions`, `purchases` |
| Rates | `vr`, `ctr`, `vcr`, `dpvr`, `acos`, `off_amazon_cvr` |
| Returns | `roas`, `c_roas`, `t_roas`, `off_amazon_roas` |
| Money | `sales`, `total_cost`, `total_sales`, `product_sales`, `off_amazon_product_sales` |
| Unit costs | `ecpm`, `ecpc`, `cpvc`, `cpdpv`, `off_amazon_cpa`, `off_amazon_purchases_cpa` |
| Off-Amazon counts | `off_amazon_purchases`, `off_amazon_conversions` |
| Context | `display_currency` |

🔴 **Sab paise aur rates STRING hain**, number nahi — `"3.64"`, `"0.00000"`. Rates 5 decimal places ke saath.

## 4.10 Is screen ke zaroori findings

| # | Baat |
|---|---|
| 1 | `id` **hi** `VMA2025107` hai — koi alag UUID nahi ✅ |
| 2 | `is_automated` field **pehle se hai** — shayad agent ka marker |
| 3 | `is_readonly` — ended strategies `true`, drafts `false`. **Mutability strategy ki STATE par depend karti hai, field par nahi** |
| 4 | `primary_currency` me **`NOK`** bhi mila, jabki market `US` tha. To **currency market se derive nahi hoti** |
| 5 | Multi-format aur multi-market **normal** hain — `["prime_video","online_video","streaming_tv","display"]`, `["US","GB"]` |
| 6 | `GET /api/strategies/` sirf list nahi — **metrics bhi jod kar deta hai** (21 kB, 1.36 s) |

---

# HISSA 5 — Step 1: Strategy Details

## 5.1 URL

```
staging.vowmade.dev/app/strategies/create/dsp
    ?aid={advertiser}&dateRange=lifetime&step=0
```

🔴 **`/create/dsp`** — channel type **URL path me** hai, form field nahi. To DSP aur Sponsored **alag flows** hain. `channel_type: "dsp"` isi se set hota hai.

🔴 Header ka **advertiser dropdown DISABLE ho jaata hai.** Creation shuru hone par advertiser lock.

## 5.2 Fields — poori table

| # | Field | Control | Required? | Default | Purpose |
|---|---|---|---|---|---|
| 1 | **Strategy name** | Text | ✅ Required | khaali | Baad me strategy dhoondhne ke liye. Uniqueness check hota hai |
| 2 | **Flight dates** | Date range | ✅ Required | khaali | Campaign kab chalega |
| 3 | **Target markets** | Multi-select | ✅ Required ("at least one") | khaali | Kaunse desh ka inventory kharidna hai |
| 4 | **Primary currency** | Dropdown | ❌ Optional | 🔴 **`€ - EUR` pehle se** | Strategy ki apni currency |
| 5 | **Formats** | 4 cards | ✅ Required | koi nahi | Kaunsi kism ki ad |
| 6 | **Product categories** | Hierarchical multi-select | 🔍 Video formats ke saath dikhta hai | khaali | **TARGETING input** — kis tak ad pahunchega |
| 7 | **Where do you sell?** | 2 cards | ✅ Required | koi nahi | On/Off Amazon → measurement kaise hoga |
| 8 | **Product ASINs** | Textarea + Add | On Amazon: ✅ · Off Amazon: ❌ | khaali | Amazon par conversion tracking |

## 5.3 🔴 Currency default — bahut zaroori baat

`Primary currency` **`€ - EUR` pehle se bhari hui aati hai — market chunne se PEHLE.**

Aur `United Kingdom` chunne ke baad bhi **EUR hi rehti hai.**

🔴 **Yaani currency market se derive NAHI hoti.** Wo kahin aur se default aati hai (⚠️ INFERRED: advertiser record se), aur trader badal sakta hai.

Ye us `NOK` wali strategy ko explain karta hai — US market, Norwegian krone.

## 5.4 Format ke 4 cards — platform ke apne shabd

| Card | Platform ka description |
|---|---|
| **Display** | "Designed to showcase your brand, products or services with compelling imagery." |
| **Online Video** | "Online videos ads that appear on online video inventory across desktop, mobile & tablet." |
| **Streaming TV** | "Non-skippable video ads that appear in-stream (before, during, or after) streaming content like TV shows and movies." |
| **Prime Video** | 🔴 "**Deals inventory** exclusively advertising alongside Prime video content." *(logo ke saath)* |

🔴 **Dhyaan do:** teen cards **ad ki kism** batate hain. Chautha **inventory** batata hai. Platform khud use *"deals inventory"* kehta hai.

To **model me teen formats aur ek inventory selection hai** — bas UI ne chaaron ko "formats" heading ke neeche rakh diya hai.

## 5.5 Product categories — hierarchy

Video format chunne par ye field aati hai:

```
Product categories for Online video and/or Streaming TV and/or Prime Video deals
```

Label teen **video** formats ka naam leta hai, Display ka nahi.

**Helper text:** *"Select the product categories that are most relevant to the product your are promoting - VOW will use this to improve strategy **targetting**."*

🔴 **Categories TARGETING input hain**, reporting label nahi.

**Do-level hierarchy:**
```
Automotive              ← parent, sirf expand hota hai, CHUN NAHI SAKTE
Beauty & Fashion
Business
Consumer Electronics
Dating
Education        ←──────┐
Entertainment           │
Family                  │
Finance, Commercial     │
Finance, Personal       │
… (aur bhi)             │
                        │
Education expand karo:  ↓
    ☐ Language Education
    ☐ General                              ← catch-all
    ☐ Schools, College & Universities
    ☐ Schools, K-12
    ☐ Schools, Online Learning
    ☐ Test Preparation
    ☐ Training & Certification
    ☐ Vocational Training & Trade Schools
    ☐ Grants, Scholarships & Financial Aid
```

🔴 **Parent chun nahi sakte** — sirf leaf (subcategory) chun sakte ho, aur multi-select hai.

Chunne ke baad chip banta hai: `× Education (2)`

Payload me values: `["304861615492321169", "345704700972773738"]` — **long numeric strings**, Amazon IDs.

## 5.6 On/Off Amazon aur ASINs

**Helper text:** *"Select where the customers that engage with your ad are **directed to**."*

Ye sawaal ke apne shabdon se behtar definition hai — ye poochh raha hai ki **ad log kahan bhejta hai**.

Card chunne par ASIN field aati hai (**dono cases me**):

```
Type or paste product ASINs ⓘ                    (0 added)
┌──────────────────────────────────────────────┐
│ Type or paste ASINs separated by comma.      │
└──────────────────────────────────────────────┘
                                        [ Add ]
```

| Choice | ASIN field | Aage badh sakte ho? |
|---|---|---|
| **On Amazon** | ✅ Required | ❌ Invalid ASIN `Next` rok deta hai |
| **Off Amazon** | Dikhta hai, par optional | ✅ Zero ASINs se bhi chalega |

🔴 **Ye halo-sales logic hai** — jo advertiser Amazon par nahi bechta, wo bhi ASINs jod kar indirect sales dekh sakta hai.

**Validation batch me hoti hai** — comma-separated paste karo, `Add` dabao, tab validate hota hai.

## 5.7 Validation — client-side

`Next` khaali form par dabane par:
```
Strategy name:    "This field is required."
Flight dates:     "This field is required."
Target markets:   "You must select at least one market."
Format cards:     laal border
Primary currency: koi error nahi (default hai)
```

🔴 **Koi API call nahi jaati** — validation poori client-side hai.

## 5.8 API 4–7 — CHAR PRE-FLIGHT CHECKS

🔴 Format chunte hi **char calls** chalti hain. Ye **feasibility checks** hain — *"is market me kaam karne layak kuch hai ya nahi?"*

### Check 1 — Audience sets hain?

```
GET /api/audience-sets/check_market_has_audience_set/?markets=GB
200 OK · Content-Length 31 · 285 ms

→ [{"market":"GB","exists":true}]
```

**Array hai** — `?markets=GB,US` bhejo to do entries aayengi. Multi-market ke liye **ek hi call**.
Sirf yes/no batata hai. Kitne hain ye nahi.

### Check 2 — Creative recs hain?

```
GET /api/creatives/recs/check_market/?markets=GB
200 OK · Content-Length 31 · 256 ms

→ [{"market":"GB","exists":true}]
```
Bilkul wahi shape. ("Recs" = responsive e-commerce creative — CTV ke liye relevant nahi)

### Check 3 — Assets hain?

```
GET /api/assets/check_market_has_assets/
    ?markets=GB
    &target_types=DISPLAY,VIDEO,STREAMING_TV,MOBILE
    &dsp_approved=true

200 OK · Content-Length 227 · 328 ms

→ [
    {"market":"GB","creative_type":"DISPLAY","exists":true},
    {"market":"GB","creative_type":"VIDEO","exists":true},
    {"market":"GB","creative_type":"STREAMING_TV","exists":true},
    {"market":"GB","creative_type":"MOBILE","exists":true}
  ]
```

🔴 Do naye concepts:
- **`target_types`** = `DISPLAY, VIDEO, STREAMING_TV, MOBILE` — ye **formats se ALAG** taxonomy hai. Asset ki shape batati hai
- **`dsp_approved=true`** — asset ka hona kaafi nahi, **DSP se approved** hona chahiye

⚠️ Note: sirf Streaming TV chuna tha, par query **chaaron** target types poochhti hai. Front-end blanket sawaal poochhta hai.

### Check 4 — Inventory sources kaunse hain?

```
GET /api/inventory-sources/
    ?strategy_formats=streaming_tv
    &markets=GB
    &goal=AWARENESS

200 OK · Content-Length 136 · 771 ms

→ [
    { "name": "Amazon Streaming TV", "type": "AMAZON", "formats": ["streaming_tv"] },
    { "name": "Twitch",              "type": "AMAZON", "formats": ["streaming_tv"] }
  ]
```

🔴 **Teen baatein:**

1. **`goal=AWARENESS` query me hai** — par trader ne goal **abhi chuna hi nahi** (wo step 2 hai)! Front-end default bhej raha hai. **Inventory availability goal par depend karti hai.**

2. **`Twitch`!** Amazon Twitch ka maalik hai. To Amazon-owned inventory me **sirf Prime Video nahi — Twitch bhi** hai. Aur Twitch bilkul alag audience hai (live streaming, younger, gaming).

3. **`type: "AMAZON"`** — ye inventory tier hai. ⚠️ **Koi non-AMAZON source kabhi nahi mila** — GB streaming TV awareness plan me sirf Amazon sources aate hain.

### 🔬 Ek test jo maine kiya

Prime Video ko **doosra format** bhi chun kar ye call dobara dekhi:

```
Result: BILKUL WAHI — do entries, aur dono ke formats me sirf ["streaming_tv"]
```

To **inventory-source level par `prime_video` format bhejne se kuch nahi milta.**

⚠️ **PAR** — forecast par matter karta hai (Hissa 10 dekho). Ye do alag sawaal hain.

## 5.9 API 8 — Conversions (Off Amazon chunne par)

```
GET /api/conversions/definitions/?selected_a…
200 OK · 0.7 kB · 237 ms   (×2 — duplicate request)
```

🔴 **Off Amazon** chunte hi ye call jaati hai. Data step 2 par use hota hai.

---

# HISSA 6 — Step 2: Goal, KPI & Bid

## 6.1 Stepper badal jaata hai

```
Step 1 par:  ①—②—③—④—⑤          paanch steps
Step 2 par:  ✓—②—③—④—⑤—⑥        CHHAH steps
```

🔴 **Do formats chunne se ek step badh gaya.** Wizard ki lambai dynamic hai.

Footer button: **`Next: Deals`**

## 6.2 Fields

| # | Field | Control | Required? | Default | Purpose |
|---|---|---|---|---|---|
| 1 | **Goal** | 3 cards | ✅ Required | 🔴 **Awareness pehle se** | Campaign ka maksad. **Inventory aur audiences dono isse filter hoti hain** |
| 2 | **KPI** — *per format* | 2 cards × per format | ✅ Required | koi nahi | Kya optimise karna hai |
| 3 | **KPI target value** | Dropdown | Conditional — sirf Frequency ke saath | khaali | Kitni frequency chahiye |
| 4 | **Customise default inventory** | Multi-select | ❌ Optional | 🔴 **Pre-flight se pehle se bhari** | Kaunse inventory sources |
| 5 | **Conversions via Ad Tag** | Multi-select | 🔍 shayad optional | khaali | Kya track karna hai |
| 6 | **Budget** | Decimal per market | ✅ Required | khaali | Kitna kharch |
| 7 | **Base bid** | Decimal per market | ✅ **Required** | khaali | Floor deals par bid |

## 6.3 Goal — teen cards

| Card | Platform ka description |
|---|---|
| **Awareness** *(pre-selected)* | "This goal helps you to expose connect your brand or product to more potential customers." |
| Consideration | "This goal helps you to drive potential and engaged customers to your store, website, and Amazon product pages." |
| Conversion | "This goal helps you to drive purchases on and off Amazon, leads, app installs, and other customer conversions." |

**Helper:** *"VOW will monitor all campaigns with similar goals and use our learning to suggest targeting parameters for future campaigns."*

🔴 **Goal sirf plan ka attribute nahi — training data bhi hai.**

Aur **Awareness pre-selected hai** — jo step 1 ki inventory call me `goal=AWARENESS` bheje jaane se match karta hai.

## 6.4 🔴 KPI — PER FORMAT hai!

```
KPI for streaming TV format
    [ Reach ]  [ Frequency ]

KPI for Prime Video deals format
    [ Reach ]  [ Frequency ]
```

**Do alag blocks!** Ek strategy me Streaming TV reach par optimise ho sakti hai aur Prime Video frequency par.

| Option | Platform ka description |
|---|---|
| **Reach** | "The number of unique users exposed from campaign start." |
| **Frequency** | "The number of times an ad is shown to one user **per week**." |

🔴 **"per week"** — frequency ka window **hafta** hai. To target 3 = **hafte me 3 baar**, poore flight me nahi.

## 6.5 KPI target value — Frequency chunne par aata hai

```
KPI target value for Prime Video deals format
┌──────────────────────────────────────┐
│                                    ▾ │
└──────────────────────────────────────┘
    2
    3
    4
    5
```

🔴 **Range 2–5 hai, 1–5 nahi.** `1` offer hi nahi hota — kyunki frequency 1 ka matlab har banda ek hi baar dekhega, jo frequency target hi nahi hai.

Label bhi **per format** hai: *"…for Prime Video deals format"*

**Helper:** *"Select the **primary** KPI you would like to use to measure the success of the strategy - you will also have access to all other metrics available from Amazon in the reporting section of VOW."*

🔴 **"Primary"** — KPI sirf headline metric hai. Reach chunne ka matlab nahi ki frequency data nahi milega. **Sab reporting me rehta hai.**

## 6.6 Customise default inventory

```
Customise default inventory
┌──────────────────────────────────────┐
│ Choose from the list               ▾ │
└──────────────────────────────────────┘
  × Amazon Streaming TV     × Twitch
```

🔴 **Pre-flight call se aaye dono sources PEHLE SE SELECTED hain**, removable chips ki tarah.

Label hi hai *"Customise **default** inventory"* — **platform bharta hai, trader badalta hai.**

## 6.7 Conversions to track via Ad Tag

```
☐ Select all
☐ Add to shopping cart    🇬🇧
☐ Application             🇬🇧
☐ Checkout                🇬🇧
☐ Page view               🇬🇧
```

**Char events**, aur **har ek par market flag** — conversions **per market** hain.

Payload me values: `["PAGE_VIEW", "CHECKOUT"]` ✅

## 6.8 🔴 Budget & Bid — currency toggle

```
Budget & Bid            [ Primary ] [ Market ]

| Market            | Budget     | Base bid   |
| 🇬🇧 United Kingdom | £10,000    | 25         |
```

**Toggle sirf layout nahi badalta — CURRENCY badalta hai aur value CONVERT karta hai:**

```
Market toggle   →  £10,000
Primary toggle  →  €10,909.09
```

🔴 **Rate ~1.0909 GBP→EUR.** Do currencies dono asli hain aur dono payload me jaati hain:
```json
"primary_currency": "EUR",                        ← strategy ki
"markets_info": [{ "currency": "GBP", … }]        ← market ki
```

## 6.9 🔴 Base bid REQUIRED hai — CTV me bhi

Base bid khaali chhod kar `Next` dabaya:
```
| 🇬🇧 United Kingdom | £10000 | Type value |
  All fields should be filled.               ← error, row laal
```

Strategy me **sirf Streaming TV + Prime Video** hain — pure CTV plan. **Platform bina bid ke aage nahi jaane deta.**

🔴 **Wajah step 3 par milti hai:** lagbhag saari deals `PRIVATE_AUCTION` + `FLOOR_RATE` hain. Floor deal par **bid karna padta hai**.

## 6.10 API 9 — Name uniqueness

`Next` dabane par **sirf ek** call:

```
GET /api/strategies/check_strategy_name_uniqueness/?name=CTV+Test+GB+Sep2026+KA
200 OK · Content-Length 18 · 242 ms

→ {"is_unique":true}
```

🔴 **Koi POST nahi. Koi strategy nahi bani. Koi draft nahi.** Wizard poora browser me hai.

Aur naam **type karte waqt check nahi hota** — `Next` par hota hai.

## 6.11 Save as draft

Step 1 par **greyed out** tha. Step 2 par **enabled** ho jaata hai.

To draft **jaan-boojh kar** banate hain, apne aap nahi banta. Aur drafts me `budget: null` hota hai — kyunki budget yahi step par poochha jaata hai.

⚠️ INFERRED: draft = kam `current_step` wali strategy (payload me `current_step: 5` hai).

---

# HISSA 7 — Step 3: Deals

## 7.1 Screen

```
Deals                                            [ Save as draft ] [ Discard ]
✓—✓—③—④—⑤—⑥

[9 channel logos]

Market ▾  Format ▾  Source ▾  Device ▾  Deal type ▾  🔍

| Name                              | Deal type       | CPM    | CPM type | ☐ |
| 3PS_Freewheel_UK_STV_Param…       | Private Auction | £22.96 | Floor    | ☐ |
|   VIA-159-00100                   |                 |        |          |   |
| 3PS_Netflix_Always On_Auto Int…   | Private Auction | £38.12 | Floor    | ☐ |
| Prime Video | Preferred Deal | …   | Preferred Deal  | £15.26 | Fixed    | ☐ |

                                    Selected Deals
                                    🇬🇧 United Kingdom
                                    No deals selected

[ Back ]                            [ Next: Audiences ]  ← DISABLED
```

**Helper text (poora, kyunki ye channels ka naam leta hai):**

> *"Browse through all available Deals tied to your Advertiser, these include curated deals from **Amazon Prime Video, Disney+, Multilocal, Discovery+, Paramount+, Hulu, Netflix, Pubmatic, Passion+**, enabling access to more valuable inventory across multiple channels."*

🔴 **NAU channels.** Aur ye ek jaise nahi hain:
```
Streaming services:  Prime Video, Netflix, Disney+, Hulu, Paramount+, Discovery+, Passion+
Supply platforms:    Pubmatic, Multilocal   (aur data me Freewheel, Magnite bhi)
```

Trader ko *"ye deal Netflix par hai"* kehna kaam ka hai. *"Ye deal Freewheel par hai"* **pipe ka naam** hai, content ka nahi.

## 7.2 Filters — poori lists

**Source** — radio, **single-select**, aath exchanges
```
◯ DRAX Web Video                ← Disney ka exchange
◯ Freewheel Video               ← Comcast
◯ Pubmatic Web Video
◯ Netflix Web Video
◯ Magnite Streaming Web Video
◯ Prime Video ads
◯ Microsoft Monetize
◯ Amazon Publisher Direct
```
🔴 **"Source" = exchange / SSP** jahan se deal aati hai.

**Device** — checkboxes
```
☐ Connected TV   ☐ Desktop   ☐ Mobile   ☐ Unknown
```

**Deal type** — checkboxes, teeno
```
☐ Preferred Deal   ☐ Private Auction   ☐ Programmatic Guaranteed
```

## 7.3 API 10 — Deals list

```
GET /api/deals/
    ?search=&page_size=25&ordering=&page=1
    &markets=GB,ZZ
    &formats=streaming_tv,prime_video,UNKNOWN
    &deal_type=&ad_lengths=&genre=&sources=&devices=&publisher=

200 OK · Content-Length 17294 · 2.45 s
count: 83
```

🔴 **Query me catch-all values padded hain:**
```
markets = GB,ZZ                                  ← ZZ = unknown market
formats = streaming_tv,prime_video,UNKNOWN       ← UNKNOWN = missing format
```
Ye un deals ko include karte hain jinka metadata missing hai. **Agent ko bhi copy karna chahiye** — warna incomplete metadata wali deals chhoot jaayengi.

**Gyarah filter parameters:** `deal_type`, `ad_lengths`, `genre`, `sources`, `devices`, `publisher` — ye matching engine ki vocabulary hai.

## 7.4 Ek deal object — poora

```json
{
  "external_deal_id": "VIA-159-00100",
  "name": "3PS_Freewheel_UK_STV_Paramount_My 5",
  "deal_price_type": "FLOOR_RATE",
  "deal_price_amount": "22.96",
  "deal_price_currency": "GBP",
  "deal_type": "PRIVATE_AUCTION",
  "media_types": [
    { "media_type": "VIDEO_STV", "bid_request_volume": 22156624.0, "bid_request_volume_rate": 0.840 },
    { "media_type": "VIDEO_OLV", "bid_request_volume": 4212881.0,  "bid_request_volume_rate": 0.160 }
  ],
  "devices": [
    { "device_type": "CONNECTED_TV", "device_name": "SMART_TV",        "bid_request_volume": 14738262.0, "bid_request_volume_rate": 0.559 },
    { "device_type": "CONNECTED_TV", "device_name": "FIRE_TV",         "bid_request_volume": 5827208.0,  "bid_request_volume_rate": 0.221 },
    { "device_type": "DESKTOP",      "device_name": "WINDOWS_DESKTOP", "bid_request_volume": 1321689.0,  "bid_request_volume_rate": 0.050 }
  ],
  "environments": [
    { "environment_type": "APP", "bid_request_volume": 24890285.0, "bid_request_volume_rate": 0.944 },
    { "environment_type": "WEB", "bid_request_volume": 1479220.0,  "bid_request_volume_rate": 0.056 }
  ],
  "locations": [
    { "country_code": "GB", "bid_request_volume": 16049990.0, "bid_request_volume_rate": 0.609 }
  ],
  "genre": null,
  "ad_lengths": []
}
```

**Bara fields.** Char volume arrays (`media_types`, `devices`, `environments`, `locations`) — sab me `bid_request_volume` aur `bid_request_volume_rate`.

## 7.5 🔴 `genre` — structured hai par BHAROSEMAND NAHI

`GET /api/deals/filter-properties/` se poori list mili:

```json
"genres": ["15, 20, 30", "2026", "2027", "Action", "Comedy", "Drama",
           "RON", "ROS", "Suspense", "TEST", "Top Trending", "Winter Holiday"]
```

| Value | Asal me kya hai |
|---|---|
| `Action`, `Comedy`, `Drama`, `Suspense` | ✅ asli genres |
| `Top Trending`, `Winter Holiday` | content categories — chalega |
| `RON`, `ROS` | placement types (run of network / run of service), genre nahi |
| `2026`, `2027` | 🔴 **saal** |
| `TEST` | 🔴 test label |
| `15, 20, 30` | 🔴 **ad lengths ki list, genre ke roop me** |

Aur Netflix deals me genre **naam ke andar** hai par field `null` hai:
```
3PS_Netflix_Always On_Primetime Entertainment_…    genre: null
3PS_Netflix_Always On_Sports & Action_…            genre: null
```

⚠️ **Lagta hai `genre` deal ke naam ka AAKHRI TOKEN le leta hai.** Jahan naam genre par khatam ho — sahi. Jahan saal par — galat. Jahan genre beech me ho — khaali.

🔴 **Nateeja: genre par matching build nahi ho sakti.** Ye **data-quality issue** hai, design sawaal nahi.

## 7.6 🔴 "Amazon Audience Enabled" deal ke NAAM me hai

```
3PS_Netflix_Always On_Auto Intenders_Interest Based_NOT Amazon Audience Enabled_STV_UK_…
3PS_Netflix_Always On_Family_Interest Based_NOT Amazon Audience Enabled_STV_UK_…
3PS_Netflix_Always On_Primetime_Interest Based_NOT Amazon Audience Enabled_STV_UK_…
3PS_Netflix_Always On_Sports & Action_Interest Based_NOT Amazon Audience Enabled_STV_UK_…
3PS_Netflix_Always On_Travel_Interest Based_NOT Amazon Audience Enabled_STV_UK_…

3PS_Netflix_Always On_Run of Network_Amazon Audience Enabled_STV_UK_…
                                     ↑ "NOT" nahi hai
```

**Paanch deals `NOT Amazon Audience Enabled`. Ek `Amazon Audience Enabled`.**

Aur deal object me **koi audience-capability field nahi hai.**

🔴 **Yaani ye jaanna ki Netflix deal par Amazon audience laga sakte ho ya nahi — sirf deal ka NAAM padh kar pata chalega.** Koi structured field nahi.

## 7.7 🔴 Metadata quality deals ke beech bahut alag hai

| | Prime Video Preferred | Netflix Private Auction |
|---|---|---|
| `genre` | `"ROS"` | `null` |
| `devices` | 3 entries volumes ke saath | `[]` |
| `environments` | `APP` 100% | `[]` |
| `media_types` | `VIDEO_STV` 100% | `[]` |
| `locations` volume | **1,457,882,193** | **1** |

🔴 **Amazon deal poori tarah described hai. Third-party deal lagbhag khaali.** Location volume `1` measurement nahi, placeholder hai.

**Iska matlab:**

| Kya karna tha | Amazon deals | Third-party deals |
|---|---|---|
| Genre par match | ✅ | ❌ null |
| Device par match | ✅ | ❌ khaali |
| Volume se deliverability check | ✅ 1.46 billion | ❌ volume 1 |
| Mobile share batana | ✅ 18% | ❌ pata nahi |

## 7.8 `filter-properties` — poora response

```
GET /api/deals/filter-properties/?formats=streaming_tv,prime_video,…
200 OK · 0.8 kB
```

```json
{
  "genres": ["15, 20, 30", "2026", "2027", "Action", "Comedy", "Drama",
             "RON", "ROS", "Suspense", "TEST", "Top Trending", "Winter Holiday"],
  "ad_lengths": ["10","10","15","20","30","15","15","20","15","20","30","20","30","40","45","60"],
  "exchanges": ["DRAX Web Video", "Freewheel Video", "Pubmatic Web Video",
                "Netflix Web Video", "Magnite Streaming Web Video", "Prime Video ads",
                "Microsoft Monetize", "Amazon Publisher Direct"],
  "devices": ["MOBILE", "UNKNOWN", "CONNECTED_TV", "DESKTOP"]
}
```

🔴 **`ad_lengths` me duplicates hain** (16 entries, 7 distinct) — endpoint `DISTINCT` nahi lagata.

🔴 **Saat durations hain:** `10, 15, 20, 30, 40, 45, 60`

## 7.9 Deal names — kaise padhein

```
3PS_Freewheel_UK_STV_Paramount_My 5
│    │         │  │   │         └── channel — My5
│    │         │  │   └── publisher group — Paramount
│    │         │  └── Streaming TV
│    │         └── market
│    └── SSP / exchange
└── 3rd Party Supply

Prime Video | Preferred Deal | Video | UK - 15, 20 – ROS
│             │                │       │    │        └── genre — Run Of Service
│             │                │       │    └── ad lengths
│             │                │       └── market
│             │                └── media type
│             └── deal type
└── channel
```

## 7.10 Deal IDs — saat formats

```
VIA-159-00100                            structured, sequential
a0f440c9-0159-40bf-aab5-b1108b10614a     UUID
EXT245WE18EEMKX                          Amazon external deal ID
apsb8dd1c90                              lowercase alphanumeric
2653736                                  plain numeric
PM-RDDS-8837                             prefixed alphanumeric
Disney-FAST-SFV-IOA-AZ-2026              descriptive slug
```

🔴 Agent `specific_deal_id` **validate nahi kar sakta** — sirf lookup try kar sakta hai.

## 7.11 Kuch aur zaroori baatein

| # | Baat |
|---|---|
| 1 | 🔴 **Ek deal `$0.00` par hai** (`VowMade_Fifa 2026_ZA`) → `budget ÷ CPM` **division by zero!** |
| 2 | 🔴 **Mixed currency aam hai** — UK deals USD me (`$1.64`, `$56.13`) |
| 3 | 🔴 `ZA` (South Africa) deals list me hain, jabki market filter me sirf UK/US. **Agent ko `locations[].country_code` se khud filter karna padega** |
| 4 | Prime Video me **Preferred (Fixed) aur Private Auction (Floor) dono** hain. Sabse sasta floor £14.66, sabse sasta fixed £15.26 |
| 5 | Rakuten TV deal sirf **17% GB** hai (baaki ES, IT). Total volume dekhne se deal zyada capable lagta hai |
| 6 | Deals **required** hain — `Next` disabled rehta hai |

---

# HISSA 8 — Step 4: Audiences

## 8.1 Screen

```
Audiences
✓—✓—✓—④—⑤—⑥

Audience sets (all markets)

Fee ▾   Goal ▾   🔍 Search audience sets

| Name                | VCPM  | Market | Goal      | ☐ | ⓘ |
| Healthy snacks      | £1.63 | 🇬🇧     | Awareness | ☐ |   |
| MH Demo 13th Feb    | £1.63 | 🇬🇧     | Awareness | ☐ |   |
| David demo          | £0.00 | 🇬🇧     | Awareness | ☐ |   |
| Impact+ Audience_UK | £1.63 | 🇬🇧     | Awareness | ☐ |   |
| … (15 total)        |       |        |           |   |   |

                      Selected audiences    [ Similar ] [ Exact ]
                      🇬🇧 Audiences (United Kingdom)
                      No audiences selected

[ Back ]              [ Next: Creatives ]  ← DISABLED
```

**Filters:**
```
Fee   — radio, single-select:  ◯ Free    ◯ Has fee
Goal  — checkboxes:            ☐ Awareness  ☐ Conversion  ☐ Consideration
```

## 8.2 🔴 VCPM flat £1.63 hai

**Har audience set ka VCPM ek jaisa hai — £1.63.** Ek £0.00 hai.

To fee:
- Audience se audience **nahi badalti**
- Kitni chuni ispar **nahi badalti**
- Ek **flat rate** hai

**Aur `Fee` filter bhi binary hai** (`Free` / `Has fee`) — range nahi. **Platform khud fee ko present/absent maanta hai.**

## 8.3 API 11 — Audience sets

```
GET /api/audience-sets/?search=&page_size=25&orderi…
200 OK · 15.4 kB · 1.28 s
count: 15
```

🔴 **15 audience sets hain**, 3,400 nahi. Wo 3,400 individual **segments** hain jo sets ke andar hote hain.

## 8.4 Ek audience set — poora

```json
{
  "id": "11e4ee53-3e35-4eb8-818d-04e19474c2c9",
  "name": "Healthy snacks",
  "goal": "AWARENESS",
  "market": "GB",
  "prompt": "Mums looking for healthier snacks for their kids school lunch boxes",
  "audience_groups": "{\"groups\": [ … nested JSON as a STRING … ]}",
  "audience_count": 23,
  "strategy_count": 2,
  "standard_display_fee": "0.59",
  "video_fee": "1.63",
  "fee_currency": "GBP",
  "is_archived": false
}
```

## 8.5 🔴 `prompt` — natural language, aur suggest feature pehle se hai

```json
"prompt": "Mums looking for healthier snacks for their kids school lunch boxes"
"prompt": "find me audiences who are most likely to buy car accessories for luxury cars"
```

Ye **natural-language prompts** hain jinse audience set generate hui.

🔴 **Teen matlab:**
1. **Agent ka kaam is step par PROMPT LIKHNA hai** — segments browse karna nahi, boolean groups banana nahi
2. **Purane prompts training material hain** — kaise likhna chahiye ye batate hain
3. **Prompts reusable hain** — match karta ho to naya banane ki zaroorat nahi

⚠️ `prompt` zyadatar sets par `null` ya `""` hai — sirf tab bharta hai jab set suggest flow se bani ho.

## 8.6 🔴 `audience_groups` — boolean tree, JSON STRING me

Do baatein:
1. **String hai, object nahi** — JSON escape ho kar string field me hai. **Do baar parse karna padega**
2. **Nested boolean tree hai** — `groups` ke andar `audiences` ya aur `groups`, har ek me `operator` (`AND`/`OR`)

`Healthy snacks` ka structure — char level deep:

```
AND
├── OR   Presence of children · Presence of Children aged 5-11 · 1 child
└── AND
    ├── OR   Females
    └── AND
        ├── OR   Age 36-40 · Age 36-45 (High Reach)
        └── OR   Healthy Food · Healthy Lifestyle · Health Conscious ·
                 Gluten Free · Diet and Nutrition · Biscuits Snacks · … (17 total)
```

**Padho:** *chhote bachon wale ghar* **AUR** *female* **AUR** *36–45 saal* **AUR** *healthy food me interest*.

🔴 **Repair loop me "widen" karne ka matlab:** ya `OR` me term jodna, ya `AND` branch hatana — **dono ka reach par bilkul alag asar** hota hai.

## 8.7 🔴 Chhah audience categories

| Category | Examples |
|---|---|
| `Demographic` | Presence of children, Females, Age 36-40, Affluence: High, Income £100k+, Property value |
| `In-market` | Healthy Food, Car Accessories, Biscuits Snacks and Crisps, Diet and Nutrition |
| `Lifestyle` | Healthy Lifestyle, Health Conscious, Lexus Owners, Audi Owners, Back to School Lookalikes |
| `Interest` | Gluten Free grocery Shoppers |
| `Custom-built` | `12qwesed200Purchases`, `Dan test 28.0130Search` — advertiser ke apne retargeting segments |
| `Device` | Airtel, Alexa, Amazon |

Har audience me: `amz_id`, `name`, `category`

## 8.8 🔴🔴 Fee ka poora rule — CATEGORY par depend karta hai

**Do fees hain, ek nahi:**
```json
"standard_display_fee": "0.59",     ← Display ke liye
"video_fee": "1.63",                ← Video ke liye
"fee_currency": "GBP"
```

**Aur kaunsi audience free hai — category se pata chalta hai:**

| Set | Andar kya hai | `video_fee` |
|---|---|---|
| `David demo` | sirf Demographic | **0.00** |
| `TestOverlapping` | sirf Demographic | **0.00** |
| `uk ok` | sirf Device | **0.00** |
| `Healthy snacks` | Demographic + In-market + Lifestyle + Interest | 1.63 |
| `Impact+ Audience_UK` | Demographic + Lifestyle + In-market + Custom-built | 1.63 |
| `cfgvh bn` | sirf Custom-built | 1.63 |

```
🟢 FREE  →  Demographic · Device
🔴 PAID  →  In-market · Lifestyle · Interest · Custom-built    →  £1.63 video
```

**Yaani:** age, gender, income, affluence, household, device targeting **muft**. Behavioural aur interest data **£1.63**.

⚠️ Do sets pattern todte hain (`90990ioj` — 0 audiences par £1.63; `as` — 0 audiences par £0.00). ⚠️ Lagta hai data error hai.

## 8.9 Fee compound nahi hoti

```
Impact+ Audience_UK    audience_count: 32    video_fee: 1.63
cfgvh bn               audience_count:  1    video_fee: 1.63
```

**32 segments aur 1 segment, dono £1.63.**

## 8.10 Kuch aur baatein

| # | Baat |
|---|---|
| 1 | `strategy_count` — sets **bahut reuse** hote hain. `TestOverlapping` **56 strategies** me hai! |
| 2 | 🔴 `standard_display_fee: ""` — **khaali string**, null nahi. Parse fail hoga |
| 3 | 🔴 List **goal se filter nahi hoti** — `CONVERSION` wala set bhi aa gaya jabki strategy Awareness hai |
| 4 | 🔴 `market` **ek value** hai, list nahi. **Audiences markets ke across share NAHI hoti** |
| 5 | `Similar` / `Exact` toggle — `Exact` default. Payload me `audience_targeting_match_type: "EXACT"` |
| 6 | **Narnow/Balanced/Wide kahin nahi hai** — koi grouping, koi teen profiles nahi |
| 7 | ⚠️ Staging me naam junk hain (`cfgvh bn`, `xswsedf`) — un se kuch infer na karein |

---

# HISSA 9 — Step 5: Creatives

## 9.1 Screen

```
Creatives
✓—✓—✓—✓—⑤—⑥

Language ▾   🔍 Search

| Name                              | Language | Markets | ☐ |
| SC_WGY_30s_HEART_Online_16x…      | English  | 🇬🇧      | ☐ |
|   Video, Streaming TV             |          |         |   |
| VOWtestVid1                       | English  | 🇬🇧      | ☐ |
| VOWtestVid1                       | English  | 🇬🇧      | ☐ |
| creative_sample                   | English  | 🇬🇧 🇺🇸   | ☐ |

                      Selected creatives
                      🇬🇧 Creatives (United Kingdom)
                      No creatives selected

[ Back ]              [ Next: Summary ]  ← DISABLED
```

🔴 **Ye UPLOAD screen NAHI hai.** Ye ek **library se chunne** wali screen hai. Koi file input nahi hai.

To **strategy banana aur creative upload karna do alag kaam hain.**

## 9.2 API 12 — Assets

```
GET /api/assets/?search=&page_size=25&languages=&target_typ…rove…
200 OK · 2.6 kB · 437 ms
count: 4
```
⚠️ Truncated parameters lagta hai `target_types=…&dsp_approved=true` — wahi filter jo step 1 ki pre-flight check me tha.

## 9.3 Ek asset — poora

```json
{
  "id": "28a0d426-1163-43f9-b4ad-8449bea9e89b",
  "name": "SC_WGY_30s_HEART_Online_16x9_v02",
  "extension": "mp4",
  "target_types": ["VIDEO", "STREAMING_TV"],
  "asset_type": "VIDEO",
  "content_type": "video/mp4",
  "width": 1920,
  "height": 1080,
  "file_size": 133901873,
  "duration": "30.00",
  "language": "English",
  "markets": ["GB"],
  "metrics": {
    "impressions": 0, "click_throughs": 0, "ctr": "0.00000",
    "total_cost": "0.00", "ecpm": "0.00", "display_currency": "USD"
  },
  "status": "ACTIVE",
  "url": "https://m.media-amazon.com/images/S/al-eu-726f4d26-7fdb/bd609a43-….mp4",
  "is_archived": false
}
```

🔴 **`duration` structured field hai** — `"30.00"`, `"20.00"`, `"10.00"`. Derive karne ki zaroorat nahi.

To **duration-match check muft hai:**
```
deal.ad_lengths   ["15","20"]     ← Prime Video Preferred deal
asset.duration    30, 20, 20, 10

→ sirf do 20-second assets us deal se match karte hain
```

🔴 **Assets me `metrics` bhi hain** — `VOWtestVid1` ka ctr 57.8%, ecpm $25.51. To agent keh sakta hai *"ye creative pehle chal chuki hai"*.

🔴 `markets` assets par **list** hai (`["GB","US"]`) — audience sets ke ulta. To **creatives campaign-level, audiences per-market**.

⚠️ Wahi video **do baar** hai (4K aur 1080p) — same naam, same url, alag `id`. Agent ko group karna padega.

## 9.4 🔴🔴 API 13 — Asset chunne par CREATIVES fetch hote hain

```
GET /api/creatives/
    ?approval_status=APPROVED
    &markets=GB
    &asset=d246bc9a-3bfc-4696-928a-eebfc5cc5aef
    &no_pagination=true

200 OK · Content-Length 7242
→ 25 entries (bare array, koi pagination wrapper nahi)
```

🔴 **`no_pagination=true`** — poora set ek hi call me. Chhote collections ke liye kaam ka.

## 9.5 🔴🔴 ASSET vs CREATIVE — ye samajhna zaroori hai

| | **Asset** `/api/assets/` | **Creative** `/api/creatives/` |
|---|---|---|
| Kya hai | video **file** | file jo Amazon par **register** hui, ek market ke liye, click-through URL ke saath |
| Identity | `id` | `id` **aur** `amz_id` |
| Rakhta hai | dimensions, duration, file size, url, language, markets, past metrics | `type`, `market`, `approval_status`, `click_through_url` |
| Approval | `dsp_approved` filter se | apna `approval_status` field |

**Ek asset → 25 creatives!** Sab `APPROVED`, sab `market: GB`, sirf `type` aur `click_through_url` me farak.

```json
{ "id": "8376ae1f-…", "amz_id": "578666890488795805", "name": "VOWtestVid1",
  "type": "Streaming TV Video", "market": "GB",
  "approval_status": "APPROVED", "click_through_url": null }
```

## 9.6 🔴 Creative ka `type` — do values

```
"Video"  ·  "Streaming TV Video"
```

Wahi asset dono types me register ho sakta hai. **CTV plan ko `Streaming TV Video` chahiye.**

**Agent ka deterministic filter:**
```
type = "Streaming TV Video"  ·  market match  ·  approval_status = APPROVED
```
25 me se ~ek tihai bachte hain.

## 9.7 🟢 Click-through URL `null` ho sakta hai, aur approved bhi

```json
{ "type": "Streaming TV Video", "approval_status": "APPROVED", "click_through_url": null }
{ "type": "Streaming TV Video", "approval_status": "APPROVED", "click_through_url": null }
```

🔴 **Streaming TV creative bina click-through URL ke APPROVED ho sakta hai.**

Wajah: **TV remote se click nahi hota.** CTV me call-to-action QR code, "search for X", ya brand recall hota hai.

⚠️ Staging me URLs polluted hain — testers ne address bar ka URL paste kar diya hai:
```
https://staging.vowmade.dev/app/strategies/create/dsp?aid=…&step=1&…
https://bbd-vow-3349-supergrid-metrics.vowmade.dev/app/…
```
Field kisi bhi URL ko accept karta hai — validate nahi karta.

## 9.8 🔴 `approval_status` per MARKET hai, per channel nahi

```json
{ "market": "GB", "approval_status": "APPROVED" }
```

Creative object me **channel ka koi dimension hi nahi hai.** Granularity **creative × market** hai.

❓ To per-channel approval kahan hai? Ya exist hi nahi karta, ya kahin aur hai.

---

# HISSA 10 — Step 6: Summary + Reach Forecast

## 10.1 Screen

Paanch review cards, har ek me `Edit` link:

**Strategy details**
```
Strategy name        CTV Test GB Sep2026 KA
Flight dates         09/01/2026 - 09/30/2026
Target markets       🇬🇧 United Kingdom
Format               Streaming TV, Prime Video
Product categories   Video → Education (2)
Primary currency     € - EUR
Product sold         Off Amazon
Product ASINs        0 added
```

**Goal, KPI & Bid**
```
Strategy goal              Awareness
Inventory sources          Amazon Streaming TV, Twitch
Deal ID                    Prime Video | Preferred Deal | Video | UK-15, 20–ROS
                           3PS_Netflix_Always On_Run of Network_Amazon Audie…
Streaming TV format KPI    Reach
Conversions to track       Page view (1) · Checkout (1)
Budget & Bid               🇬🇧 UK — Budget: £10,000.00 · Bid: £25.00
```

**Deals**
```
🇬🇧 United Kingdom     CPM
                       £24.79        15, 20 | ROS
                       £34.80        10, 15, 20, 30 | N/A     ← genre null → "N/A"
```

**Audience sets** — `Impact+ Audience_UK`, `David demo` *(2 audience sets)*

**Creatives** — *(0 creatives)* 🔴 asset tick kiya tha par **creative nahi chuna**

🔴 **`Create Strategy` button ENABLED hai 0 creatives ke saath** — to creative strategy banane ke liye zaroori nahi.

## 10.2 🔴🔴 API 14 — Reach Forecast

```
POST /api/strategies/reach-forecast/
200 OK · Content-Length 531
Allow: POST, OPTIONS
```

### Request — sirf CHAR inputs

```json
{
  "flight_dates": { "lower": "2026-09-01", "upper": "2026-09-30" },
  "formats": ["streaming_tv", "prime_video"],
  "goal": "AWARENESS",
  "market_budgets": [
    { "market": "GB", "budget": 10000, "base_bid": "25", "currency": "GBP", … }
  ]
}
```

🔴🔴 **Deals nahi. Audiences nahi. Targeting nahi.**

### Response

```json
{
  "total_reach": 233803,
  "total_impressions": 860716,
  "market_reach": [
    {
      "market": "GB",
      "reach": 233803,
      "budget": "10000.00",
      "currency": "GBP",
      "impressions": 860716,
      "supplies": [
        {
          "supply": "DSP_STREAMING_TV",
          "est_spend": 4931.712321976001,
          "est_reach": 132713,
          "max_reach": 285186,
          "est_impressions": 647856,
          "max_impressions": 6759074,
          "avg_cpm": "7.60",
          "max_cpm": "14.98"
        },
        {
          "supply": "DSP_PRIME_VIDEO",
          "est_spend": 5068.2876889,
          "est_reach": 71120,
          "max_reach": 950000,
          "est_impressions": 212860,
          "max_impressions": 52757286,
          "avg_cpm": "23.98",
          "max_cpm": "23.98"
        }
      ]
    }
  ]
}
```

## 10.3 🔴 Forecast ki paanch zaroori baatein

**1. `supplies` FORMAT se keyed hai**
```
DSP_STREAMING_TV   ← formats: ["streaming_tv", …]
DSP_PRIME_VIDEO    ← formats: […, "prime_video"]
```

🔴 **Yahan `prime_video` MATTER karta hai!** Sirf `streaming_tv` bhejte to ye supply line **aati hi nahi** — 71,120 reach aur 212,860 impressions **chale jaate**.

Poora picture:

| Endpoint | `prime_video` matter karta hai? |
|---|---|
| `/inventory-sources/` | ❌ Nahi — wahi do Amazon sources |
| `/deals/` | filter me jaata hai, asar untested |
| `/reach-forecast/` | ✅ **HAAN** — alag supply line |

**2. Budget khud split hota hai**
```
DSP_STREAMING_TV    est_spend  4,931.71
DSP_PRIME_VIDEO     est_spend  5,068.29
                               10,000.00
```
49/51 — even nahi, **optimisation** hai.

**3. `est_` aur `max_` — deliverability ceiling built-in**
```
                estimated        maximum available
reach            132,713          285,186
impressions      647,856        6,759,074
cpm                £7.60           £14.98
```

🔴 **`max_reach` hi repair loop ko chahiye.** Reach kam ho to asli sawaal *"audience widen karun?"* nahi — *"zyada reach available hai?"* hai. Agar `est_reach = max_reach` ho, to kuch kaam nahi karega.

**4. Forecast ke CPM DEAL ke CPM nahi hain**
```
Deals chuni:       £24.79 · £34.80
Forecast avg_cpm:  £7.60  · £23.98
```

Ganit andar se consistent hai:
```
4,931.71 ÷ 7.60 × 1000 = 648,909 ≈ 647,856 ✓
5,068.29 ÷ 23.98 × 1000 = 211,355 ≈ 212,860 ✓
```

🔴 **Teen alag CPM concepts hain:** rate-card CPM, deal price (fixed/floor), supply average CPM.

**5. Impressions jodti hain, reach nahi**
```
impressions  647,856 + 212,860 = 860,716  =  total ✓
reach        132,713 +  71,120 = 203,833  ≠  total 233,803  (29,970 zyada)
```

🔴 **Reach kabhi derive na karein** — `total_reach` jo API deta hai wahi report karein.

**Frequency return nahi hoti** — derive karni padegi:
```
860,716 ÷ 233,803 = 3.68 average frequency
```

## 10.4 🔴 Wizard me TARGETING step nahi hai

Chhah steps, aur **koi targeting nahi**. Na location, na device type, na content exclusions.

**Wajah:** saare targeting endpoints strategy ke andar nested hain —
```
GET/POST /api/strategies/{id}/targeting/
POST     /api/strategies/{id}/targeting/auto-rec/
GET/POST /api/strategies/{id}/targeting/{market}/locations/
GET/POST /api/strategies/{id}/targeting/{market}/product-categories/
GET/POST /api/strategies/{id}/targeting/{market}/products/
```

**Har ek ko strategy ID chahiye. To targeting creation ke BAAD hi ho sakti hai.**

---

# HISSA 11 — Creation

## 11.1 🔴 API 15 — POST /api/strategies/

```
POST /api/strategies/       201 Created · 1.0 kB · 2.93 s
```

🔴 **`/api/strategies/`, `simple-strategies` NAHI.**

⚠️ `simple-strategies` aur `automated-strategies` dono exist karte hain par yahan use nahi hote.

## 11.2 Poora payload — CONTRACT

```json
{
  "name": "CTV Test GB Sep2026 KA",
  "flight_dates": { "lower": "2026-09-01", "upper": "2026-09-30" },
  "goal": "AWARENESS",
  "primary_currency": "EUR",
  "product_location": "NOT_SOLD_ON_AMAZON",
  "current_step": 5,

  "formats_and_kpis": [
    { "format": "streaming_tv", "kpi": "REACH" },
    { "format": "prime_video",  "kpi": "FREQUENCY", … }
  ],

  "markets_info": [
    {
      "market": "GB",
      "base_supply_bid": "25",
      "budget": 10000,
      "currency": "GBP",
      "audience_targeting": [
        { "audience_set_id": "26f2cbb3-d815-4148-b935-1407a91b60c4", "audience_type": "AUDIENCE_SET" },
        { "audience_set_id": "a6daf3a8-7b95-4170-bd05-eb0f0edc018c", "audience_type": "AUDIENCE_SET" }
      ]
    }
  ],

  "market_deals": [
    {
      "market": "GB",
      "deals": [ { …POORA deal object… }, { …POORA deal object… } ]
    }
  ],

  "selected_inventory_sources": [
    { "name": "Amazon Streaming TV", "type": "AMAZON" },
    { "name": "Twitch", "type": "AMAZON" }
  ],

  "video_product_categories": ["304861615492321169", "345704700972773738"],
  "product_categories": [],
  "audience_targeting_match_type": "EXACT",
  "conversion_types": ["PAGE_VIEW", "CHECKOUT"],

  "assets": [ { "id": "d246bc9a-…", "name": "VOWtestVid1", … } ],
  "pre_approved_creatives": [],
  "rec_creatives": [],
  "third_party_creatives": []
}
```

## 11.3 Response — 201

```json
{
  "id": "VMA2026368",
  "name": "CTV Test GB Sep2026 KA",
  "goal": "AWARENESS",
  "primary_currency": "EUR",
  "flight_dates": { "lower": "2026-09-01", "upper": "2026-09-30", "timezone": "UTC" },
  "product_categories": [],
  "video_product_categories": ["304861615492321169", "345704700972773738"],
  "enable_fraud_invalid_traffic_targeting": false,
  "enable_brand_safety_targeting": false,
  "audience_targeting_match_type": "EXACT",
  "conversion_types": ["PAGE_VIEW", "CHECKOUT"],
  "selected_inventory_sources": [
    { "name": "Amazon Streaming TV", "type": "AMAZON" },
    { "name": "Twitch", "type": "AMAZON" }
  ],
  "is_archived": false,
  "is_readonly": false
}
```

🔴 Response **subset** hai — `markets_info`, `market_deals`, `assets`, `formats_and_kpis` **wapas nahi aate**.

🔴 **Do fields jo request me nahi the par response me hain:**
```json
"enable_fraud_invalid_traffic_targeting": false,
"enable_brand_safety_targeting": false
```
**Brand safety ek boolean hai, aur DEFAULT OFF hai.** Wizard me kahin dikhta hi nahi — to trader ko pata bhi nahi chalta.

## 11.4 🔴 Contract ke bare me zaroori baatein

**1. Market poore payload ka organising unit hai**
```
markets_info[]     market · base_supply_bid · budget · currency · audience_targeting[]
market_deals[]     market · deals[]
```

Per market: **budget, bid, currency, audiences, deals.** Baaki sab campaign-level.

**2. POORA deal object wapas jaata hai** — deal ID nahi, poora record. To agent deals list phenk nahi sakta.

**3. `formats_and_kpis`** — KPI aur target value **per format**, ek list of pairs.

**4. Bid ka naam do endpoints par ALAG hai:**
```
POST /strategies/reach-forecast/    "base_bid": "25"
POST /strategies/                   "base_supply_bid": "25"
```

**5. `current_step: 5`** — wizard ki position payload me hai. ⚠️ Drafts isse chalte hain.

**6. Do category fields:** `product_categories` (display) aur `video_product_categories` (video). Values **long numeric strings** hain.

**7. Char creative arrays:** `assets` (bhara), `pre_approved_creatives`, `rec_creatives`, `third_party_creatives` (khaali) — **teeno khaali bhejne padte hain**.

## 11.5 Creation ke baad kya hota hai

**Modal:**
> **Your strategy has been created!**
> VOW will publish and synchronise your strategy with Amazon in the background.
> You can track the performance of your strategy and all campaigns in the strategy overview page and in reporting.

**Strategy overview page:**
```
CTV Test GB Se…              [ Paused ▾ ]  Syncing ⟳    [ Display ] [ Strategy settings ]
ID: VMA2026368
Inactive
```

🔴 **Created strategy `Paused` / `Inactive` me land karti hai, aur background me sync hoti hai.**

**API 16–17 — creation ke baad:**
```
GET /api/strategies/VMA2026368/?metrics_date_range=&include_archived=true&…   200 · 3.5 kB
GET /api/reports/performance-metrics/?strategy_id=VMA2026368&…                200 · 1.1 kB
```

🔴 **Creation ka matlab Amazon par exist karna NAHI hai.** Sync alag async job hai, aur **fail ho sakta hai** — list me kai strategies par `CAMPAIGN_SYNC_ISSUES` hai.

---

# HISSA 12 — Post-Creation: Strategy Overview

## 12.1 Sidebar — saat sections

```
Overview           basic info + events + performance
Planner            🔴 budget aur bid ka editor
Campaigns          Amazon par sync hone ke baad
Creatives          creative manage karo
Audience sets      audiences manage karo
Locations          🔴 TARGETING YAHAN HAI
Strategy history   changes ka log
```

## 12.2 Overview fields

```
Flight date:     Not started
Markets:         🇬🇧
Goal:            Awareness
Strategy type:   DSP           ← 🔴 API ise channel_type kehta hai
Channel type:    Off Amazon    ← 🔴 API ise product_location kehta hai
```

🔴🔴 **UI ke labels API se ULTE hain.**

## 12.3 🔴 Planner — budget aur bid editor

```
Strategy planner                   [ Duplicate strategy ]  [ Add flight dates ]

Status ▾                                Currency: [ Primary ] [ Market ]

🇬🇧 United Kingdom
                     Market          Streaming TV     Prime Video
Bid                                  ✏ €27.27         ✏ €27.27

Flight dates         Market          Streaming TV     Prime Video
09/01/2026-09/30/2026  Budget  ✏ €10,909.09   ✏ €5,454.55      ✏ €5,454.55
[ Scheduled ]                                                              ⌄
```

**Char zaroori baatein:**

**1. Ye FORECAST nahi hai** — koi reach, impressions, CPM nahi. Bas editable budgets aur bids.

**2. 🔴 Budget PER FORMAT split hota hai, exact 50/50**
```
Market total    €10,909.09
Streaming TV     €5,454.55
Prime Video      €5,454.55
```

**3. 🔴 Forecast ka `est_spend` ≠ stored allocation**
```
Forecast est_spend      4,931.71  /  5,068.29    (49/51 — prediction)
Planner allocation      5,454.55  /  5,454.55    (50/50 — actual cap)
```
**Do alag cheezein hain.**

**4. 🔴🔴 Kai flight ranges ho sakti hain**

Flight dates ek **row** hai status badge ke saath, aur **`Add flight dates`** button hai.

API confirm karta hai:
```
GET/POST  /api/strategies/{id}/flight-ranges/
PUT/PATCH /api/strategies/{id}/flight-ranges/{id}/
PUT/PATCH /api/strategies/{id}/flight-ranges/budget/{id}/
DELETE    /api/strategies/{id}/flight-ranges/{id}/
```

**Poori granularity — CHAR levels:**
```
strategy → flight range → market → format → budget
```

**5. Bid bhi per format stored hota hai** — ek bid bheja (`base_supply_bid: "25"` GBP), do bane (€27.27 × 2), alag-alag editable.

**6. `Duplicate strategy`** — `POST /api/strategies/duplicate/`. Isse `9989809i8(1)`, `(2)` naam aate hain.

## 12.4 🔴 Audience-aware forecast kahin call HI nahi hota

Ye endpoints exist karte hain:
```
POST /api/audience-sets/reach-forecast/
POST /api/strategies/{id}/audiences/reach-forecast/
POST /api/contextual-targeting/{market}/products/reach-forecasting/
```

**Par manual flow me koi bhi unhe call nahi karta.** Product jo ek forecast chalata hai wo Summary par hai, jo audiences aur targeting **nahi** leta.

---

# HISSA 13 — Poora API Reference (17 APIs)

| # | Endpoint | Method | Kab | Size |
|---|---|---|---|---|
| 1 | `/api/credits/summary/?advertiser={uuid}` | GET | List load | 56 B |
| 2 | `/api/reports/user-preferences/` | GET | List load | 0.3 kB |
| 3 | `/api/strategies/?{11 params}` | GET | List load | 21 kB |
| 4 | `/api/audience-sets/check_market_has_audience_set/?markets=GB` | GET | Step 1, format chunne par | 31 B |
| 5 | `/api/creatives/recs/check_market/?markets=GB` | GET | Step 1 | 31 B |
| 6 | `/api/assets/check_market_has_assets/?markets=GB&target_types=…&dsp_approved=true` | GET | Step 1 | 227 B |
| 7 | `/api/inventory-sources/?strategy_formats=…&markets=GB&goal=AWARENESS` | GET | Step 1 | 136 B |
| 8 | `/api/conversions/definitions/?selected_a…` | GET | Step 1, Off Amazon | 0.7 kB |
| 9 | `/api/strategies/check_strategy_name_uniqueness/?name=…` | GET | Step 1 → 2 | 18 B |
| 10 | `/api/deals/?{11 params}` | GET | Step 3 | 17 kB |
| 11 | `/api/deals/filter-properties/?formats=…` | GET | Step 3 | 0.8 kB |
| 12 | `/api/audience-sets/?search=&page_size=25` | GET | Step 4 | 15 kB |
| 13 | `/api/assets/?search=&page_size=25&target_types=…` | GET | Step 5 | 2.6 kB |
| 14 | `/api/creatives/?approval_status=APPROVED&markets=GB&asset={id}&no_pagination=true` | GET | Step 5, asset tick par | 7.2 kB |
| 15 | `/api/strategies/reach-forecast/` | **POST** | Step 6 arrival | 531 B |
| 16 | `/api/strategies/` | **POST** | Create Strategy | 1.0 kB → 201 |
| 17 | `/api/strategies/{VMA_id}/` | GET | Creation ke baad | 3.5 kB |

**Common headers:** `Server: gunicorn` · `Vary: Accept, Cookie, origin` · session cookie auth

---

# HISSA 14 — Paanch Overlapping Taxonomies

🔴 Ek hi broad idea ke liye **paanch alag taxonomies** hain. Ye confusion ka sabse bada source hai.

| # | Taxonomy | Values | Kahan |
|---|---|---|---|
| 1 | `formats` | `display`, `online_video`, `streaming_tv`, `prime_video` (+ `netflix`, `disney+` sirf filter me) | strategy, deals query |
| 2 | `target_types` / `creative_type` | `DISPLAY`, `VIDEO`, `STREAMING_TV`, `MOBILE` | assets |
| 3 | `media_types` | `VIDEO_STV`, `VIDEO_OLV` | deals |
| 4 | Creative `type` | `Video`, `Streaming TV Video` | creatives |
| 5 | `supply` | `DSP_STREAMING_TV`, `DSP_PRIME_VIDEO` | forecast |

Aur **"channel" shabd ke chhah matlab:**

| Term | Kahan | Values |
|---|---|---|
| UI **"Channel type"** | strategy overview | On Amazon / Off Amazon |
| UI **"Channels"** column | strategy list | On Amazon / Off Amazon |
| UI **"Location"** filter | strategy list | On Amazon / Off Amazon |
| API `product_location` | strategy record | `SOLD_ON_AMAZON` / `NOT_SOLD_ON_AMAZON` |
| API `channel_type` | strategy record | `dsp` / `sponsored` |
| UI **"Strategy type"** | overview | DSP |

🔴 **UI jise "Channel type" kehta hai, wo API ka `product_location` hai. API ka `channel_type` UI me "Strategy type" hai.**

---

# HISSA 15 — Currency Model

🔴 Ek plan me **char currency contexts** ho sakte hain:

```
1. primary_currency          EUR    ← strategy ki apni (advertiser se)
2. markets_info[].currency   GBP    ← market ki local
3. deal_price_currency       GBP aur USD  ← per deal!
4. metrics display_currency  USD    ← asset ke past metrics
```

**Conversion asli hai:**
```
£10,000 → €10,909.09       (rate ~1.0909)
£25     → €27.27           (wahi rate)
```

🔴 **Impressions ka ganit:**
```
impressions = budget ÷ effective CPM × 1000
```
Agar budget ek currency me aur CPM doosri me, to ye **galat** hai — is rate par ~9% ka farak.

**Poora hisaab EK currency me karna padega, aur batana padega kaunsi.**

Aur ek deal **$0.00** par hai → **division by zero ka guard chahiye.**

---

# HISSA 16 — Data Quality Issues (implementation se pehle jaan lo)

| # | Issue | Asar |
|---|---|---|
| 1 | 🔴 `genre` polluted hai — `"2026"`, `"TEST"`, `"15, 20, 30"` genre ban gaye hain, aur Netflix genres `null` hain | **Genre par matching build nahi ho sakti** |
| 2 | 🔴 "Amazon Audience Enabled" sirf deal ke **naam** me hai, koi field nahi | `targeting_source` reliably set nahi ho sakta |
| 3 | 🔴 Deal par `inventory_tier` field **hai hi nahi** | Teen-tier fork ka koi data source nahi |
| 4 | 🔴 Deal par `channel` field **hai hi nahi** | Prime Video/Netflix sirf `name` me |
| 5 | 🔴 Third-party deals ka metadata **khaali** hai — devices, environments, media_types `[]`, location volume `1` | 3P par matching aur volume check possible nahi |
| 6 | 🔴 Ek deal `$0.00` par | Division by zero |
| 7 | 🔴 UK deals **USD** me | Currency normalisation zaroori |
| 8 | 🔴 `standard_display_fee: ""` — khaali string | Parse fail |
| 9 | ⚠️ `ad_lengths` filter me **duplicates** | DISTINCT khud lagana padega |
| 10 | ⚠️ `VCR 128.45%` — completion rate 100% se zyada | Metrics recompute na karein |
| 11 | ⚠️ Reach jodne par total se **kam** aata hai (203,833 vs 233,803) | Reach kabhi derive na karein |
| 12 | ⚠️ Audience names staging me junk (`cfgvh bn`, `xswsedf`) | Relevance test meaningless |
| 13 | ⚠️ Click-through URLs me app URLs paste hain | Field validate nahi karta |
| 14 | ⚠️ Wahi asset do baar (4K + 1080p, same url) | Group karna padega |
| 15 | ⚠️ Deal IDs ke **saat formats** | Validate nahi kar sakte |
| 16 | ⚠️ `ZA` deals GB list me aa jaati hain | `locations[].country_code` se khud filter karo |

---

# HISSA 17 — Cheat Sheet (ek page)

## Flow
```
List → New Strategy → 6 steps (sab client-side) → POST /strategies/ → Paused/Syncing
                                                                    → Planner, Locations
```

## 6 Steps
```
1  Strategy details   name·dates·markets·currency·formats·categories·On/Off Amazon·ASINs
2  Goal KPI Bid       goal·KPI per format·target value·inventory·conversions·budget·bid
3  Deals              83 me se tick
4  Audiences          15 me se tick
5  Creatives          4 assets me se tick → phir creative chuno
6  Summary            review · forecast · create
```

## Required fields
```
Step 1:  name · flight dates · markets · formats · On/Off Amazon
         + ASINs (sirf On Amazon)
Step 2:  goal · KPI (per format) · budget · BASE BID
Step 3:  at least ek deal
Step 4:  at least ek audience (🔍 button disabled tha)
Step 5:  ❌ NAHI — 0 creatives par bhi create ho jaata hai
```

## Numbers
```
361  strategies (ek advertiser ke)
 83  deals
 15  audience sets
  4  assets
 25  creatives (ek asset ke!)
  2  markets (UK, US)
  8  status values
  6  format values (creation me 4)
  8  exchanges
  7  ad lengths (10,15,20,30,40,45,60)
  6  audience categories
  4  device types
```

## Key formulas
```
impressions   = budget ÷ effective CPM × 1000
frequency     = impressions ÷ reach            (per week!)
eCPM          = spend ÷ impressions × 1000
ROAS          = revenue ÷ spend
KPI target    = 2 se 5 (1 nahi!)
```

## Sabse zaroori 10 baatein
```
1.  Wizard poora client-side — beech me kuch save nahi hota
2.  Targeting creation ke BAAD hoti hai (Locations section)
3.  Budget split creation ke BAAD hoti hai (Planner) — auto 50/50 per format
4.  KPI PER FORMAT hai, per strategy nahi
5.  Base bid REQUIRED hai — kyunki deals FLOOR_RATE hain
6.  Currency market se derive NAHI hoti — advertiser se default aati hai
7.  Asset ≠ Creative — do alag objects
8.  Forecast me deals/audiences/targeting NAHI jaate
9.  prime_video format forecast me MATTER karta hai (inventory-sources me nahi)
10. Creation ≠ Amazon par exist karna — sync alag async job hai
```

---

# HISSA 18 — Jo abhi pata nahi (poochhna hai)

| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | Deal ka `inventory_tier` kaise tay hota hai? | Teen-tier fork ka data source nahi |
| 2 | `genre` field theek ho sakta hai? | Genre par matching ke liye |
| 3 | "Amazon Audience Enabled" ko boolean field bana sakte hain? | `targeting_source` ke liye |
| 4 | Agent ke liye kaunsa create endpoint — `strategies`, `simple-strategies`, ya `automated-strategies`? | `is_automated` teesre par ishaara karta hai |
| 5 | Audience-aware forecast kabhi use hota hai? | Repair loop ka aadhaar |
| 6 | `total_reach` kaise calculate hota hai? | Sum se zyada aata hai |
| 7 | Kaunsa CPM actual delivery govern karta hai — deal price ya supply average? | Trader ko ek dikhta hai, doosra kharidta hai |
| 8 | Multiple flight ranges M1 me chahiye? | Platform support karta hai |
| 9 | `enable_brand_safety_targeting` default ON hona chahiye? | Abhi OFF hai, trader ko pata nahi |
| 10 | Per-channel creative approval kahan hai? | Abhi per **market** hai |
| 11 | Third-party deals ka metadata kyun khaali hai? | Data gap ya upstream nahi hai? |
| 12 | Amazon sync fail hua ya nahi — kaise check karein? | Webhook hai ya poll karna padega? |
| 13 | Currency normalise kis par karein? | Ek plan me GBP + USD deals |
| 14 | `audience_type` ki aur kaunsi values hain? | `AUDIENCE_SET` ke alawa |
| 15 | Kya `no_pagination=true` deals par bhi chalta hai? | 83 deals ek call me |

---

**Ye document `staging.vowmade.dev` par 4 August 2026 ko ek poori strategy banate hue observe kiya gaya. Test strategy: `CTV Test GB Sep2026 KA` → `VMA2026368`.**

**Jahan bhi ✅ VERIFIED hai, wo API payload ya response me confirm hai. ⚠️ INFERRED wali baatein andaaza hain, saboot ke saath par pakka nahi.**
