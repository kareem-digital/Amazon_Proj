# Deals, Rate Card, AMC aur Audience Profiles — Poora Concept

**Ye document kis liye:** VOW platform par Deals, Rate Card, AMC audiences aur Narrow/Balanced/Wide — ye char cheezein baar-baar aati hain. Yahan har ek ka poora matlab hai, asaan shabdon me, real examples aur asli platform data ke saath.

**Data ka source:** `staging.vowmade.dev` par 4 August 2026 ki verification — 83 deals, 15 audience sets, 17 APIs. Aur Wajahat ke flowcharts.

---

## Index

| § | Kya |
|---|---|
| 1 | Deal kya hai |
| 2 | Deal ke andar kya-kya hota hai — 12 fields |
| 3 | Deal ka naam padhna |
| 4 | 🔴 Kya targeting deal me aati hai |
| 5 | 🔴 Kya audience deal me aati hai |
| 6 | Rate Card kya hota hai |
| 7 | AMC audience kya hai |
| 8 | Narrow / Balanced / Wide kya hain |
| 9 | Sab kaise jodta hai — ek picture |
| 10 | Ek page ka summary |

---
---

# 1. DEAL kya hai

## Ek line me

**Deal = publisher aur khareedar ke beech pehle se tay kiya hua intezaam** — kaunsi inventory, kis daam par, kaun khareed sakta hai.

## Deal ke bina kya hota hai

```
Deal ke BINA  →  Open Auction. Sabke liye khula. Koi rishta nahi.
                 Premium publishers (Prime Video, Netflix) yahan aate hi nahi.

Deal ke SAATH →  Aapko ek DEAL ID milti hai — jaise EXT245WE18EEMKX
                 Wo ID DSP me daalne se wo specific inventory KHUL jaati hai
```

## Analogy — wholesale market ka pass

```
Sabzi mandi me do hisse hote hain:

RETAIL     →  koi bhi jaa sakta hai, daam roz badalta hai
              ye "open auction" hai

WHOLESALE  →  andar jaane ke liye PASS chahiye
              pass wale ko fixed rate milta hai, ya pehle mauka
              ye "deal" hai
```

🔴 **Deal ID wahi pass hai.** Uske bina wo inventory dikhti bhi nahi.

## Premium publishers open auction me kyun nahi aate

```
Ek luxury car brand ka ad chal raha hai
        ↓
Open auction me uske saath ek satta app ka ad bhi chal sakta hai
        ↓
Brand ko nuksan

Isliye Prime Video / Netflix apni inventory KHULI auction me
nahi daalte — sirf deals ke through bechte hain.
```

---
---

# 2. Deal ke ANDAR kya-kya hota hai — 12 fields

Maine staging par 83 deals ka poora payload dekha. Ek asli deal:

```json
{
  "external_deal_id": "VIA-159-00100",
  "name": "3PS_Freewheel_UK_STV_Paramount_My 5",

  "deal_type": "PRIVATE_AUCTION",
  "deal_price_type": "FLOOR_RATE",
  "deal_price_amount": "22.96",
  "deal_price_currency": "GBP",

  "media_types":  [{"media_type": "VIDEO_STV", "bid_request_volume": 22156624,
                    "bid_request_volume_rate": 0.840},
                   {"media_type": "VIDEO_OLV", "bid_request_volume": 4212881,
                    "bid_request_volume_rate": 0.160}],

  "devices":      [{"device_type": "CONNECTED_TV", "device_name": "SMART_TV",
                    "bid_request_volume": 14738262, "bid_request_volume_rate": 0.559},
                   {"device_type": "CONNECTED_TV", "device_name": "FIRE_TV",
                    "bid_request_volume": 5827208,  "bid_request_volume_rate": 0.221},
                   {"device_type": "DESKTOP", "device_name": "WINDOWS_DESKTOP",
                    "bid_request_volume": 1321689,  "bid_request_volume_rate": 0.050}],

  "environments": [{"environment_type": "APP", "bid_request_volume": 24890285,
                    "bid_request_volume_rate": 0.944},
                   {"environment_type": "WEB", "bid_request_volume": 1479220,
                    "bid_request_volume_rate": 0.056}],

  "locations":    [{"country_code": "GB", "bid_request_volume": 16049990,
                    "bid_request_volume_rate": 0.609}],

  "genre": null,
  "ad_lengths": []
}
```

## Char groups me samjho

| Group | Fields | Kya batate hain |
|---|---|---|
| **Pehchaan** | `external_deal_id`, `name` | Kaunsi deal hai |
| **Paisa** | `deal_type`, `deal_price_type`, `deal_price_amount`, `deal_price_currency` | Kitna, aur kaise |
| **Kitni inventory hai** | `media_types`, `devices`, `environments`, `locations` — sab volume ke saath | Kitna maal available hai |
| **Kya chalega** | `genre`, `ad_lengths` | Kis content ke saath, kitne second ka ad |

## `bid_request_volume` — ye kya hai

**Kitni inventory available hai.**

```
"bid_request_volume": 22156624

Matlab: is deal par 2.2 CRORE baar sawaal aaya —
        "koi ad chahiye?"
```

**Bada number = badi supply = aapko slot milne ka zyada chance.**

Aur `bid_request_volume_rate` batata hai **hissa**:

```
SMART_TV   14,738,262   →  55.9%   ← aadhi se zyada inventory smart TV par
FIRE_TV     5,827,208   →  22.1%
DESKTOP     1,321,689   →   5.0%
                            ─────
                            78% Connected TV
```

**Ye planning me kaam ka hai** — agar aapko sirf TV chahiye, to ye deal 78% TV hai, achhi hai.

## `environments` — ek dilchasp number

```
APP  =  94.4%
WEB  =   5.6%
```

🔴 **94% CTV inventory app ke andar hai**, browser me nahi. Isliye app-vs-web par target karne ka koi faayda nahi — 94% to already app hai.

**Yahi wajah ho sakti hai** ki mobile targeting me app-vs-web nahi, balki **IOS/ANDROID** ke options hote hain.

## 🔴 Ek badi problem — 3P deals ka data khaali hota hai

| Field | Prime Video (Amazon) | Netflix (3P) |
|---|---|---|
| `genre` | `"ROS"` | `null` |
| `devices` | 3 entries volumes ke saath | `[]` **khaali** |
| `environments` | APP 100% | `[]` **khaali** |
| `media_types` | VIDEO_STV 100% | `[]` **khaali** |
| `ad_lengths` | `["15","20"]` | `[]` **khaali** |
| `locations` volume | **1,457,882,193** | **1** |

🔴 **Location volume `1` measurement nahi hai — placeholder hai.**

**Iska matlab:** Amazon deals par duration, device aur volume par match kar sakte hain. **3P deals par nahi.** Aur 3P deals hi majority hain.

---
---

# 3. Deal ka NAAM padhna — ye practical skill hai

🔴 **Bahut zaroori jaankari deal ke naam me chhupi hoti hai, field me nahi.**

## Third-party deal

```
3PS_Freewheel_UK_STV_Paramount_My 5
│    │         │  │   │         └── channel — My5 (Paramount ka UK channel)
│    │         │  │   └── publisher group — Paramount
│    │         │  └── Streaming TV
│    │         └── market — UK
│    └── SSP / exchange — Freewheel
└── 3PS = 3rd Party Supply
```

## Amazon deal

```
Prime Video | Preferred Deal | Video | UK - 15, 20 – ROS
│             │                │       │    │        └── genre — Run Of Service
│             │                │       │    └── ad lengths — 15 aur 20 second
│             │                │       └── market
│             │                └── media type
│             └── deal type
└── channel
```

## Deal IDs — saat alag formats

```
VIA-159-00100                            structured, sequential
a0f440c9-0159-40bf-aab5-b1108b10614a     UUID
EXT245WE18EEMKX                          Amazon external deal ID
apsb8dd1c90                              lowercase alphanumeric
2653736                                  plain numeric
PM-RDDS-8837                             prefixed alphanumeric
Disney-FAST-SFV-IOA-AZ-2026              descriptive slug
```

🔴 **Isliye agent kisi deal ID ka FORMAT validate nahi kar sakta** — sirf lookup try kar sakta hai aur bata sakta hai ki mila ya nahi.

---
---

# 4. 🔴 Kya TARGETING deal me aati hai?

**Jawab: ADHI aati hai.** Aur yahi sabse zaroori samajhna hai.

## Jo deal me PEHLE SE BAKED hai

| Targeting | Kahan se |
|---|---|
| Market — "UK" | `locations[]` |
| Device — Smart TV, Fire TV | `devices[]` |
| App ya Web — 94% app | `environments[]` |
| Media type — Streaming TV | `media_types[]` |
| Ad length — 15, 20 second | `ad_lengths[]` |
| Content — Paramount ka My5 | 🔴 **NAAM me** |
| Genre — ROS | `genre` (par bharosemand nahi) |

🔴 **Yaani deal khud ek targeting decision hai.**

`3PS_Freewheel_UK_STV_Paramount_My 5` chunne ka matlab hai *"UK me, TV par, Paramount ke My5 channel par"* — ye aapne **deal chun kar hi** tay kar diya.

## Jo deal me NAHI hai — aap UPAR se lagate ho

```
Audience segments      "healthy food me interested log"
Location narrowing     "sirf SW1, SW3 postcodes"
Instream position      "pre-roll only"
Content exclusions     "violent content ke saath nahi"
Device narrowing       (deal ke andar se, aur kam kar sakte ho)
Mobile OS              IOS ya ANDROID
```

## Analogy — train ticket

```
DEAL = "Rajdhani, Delhi → Mumbai, 3AC"

Deal me BAKED:
   Kaunsi train, kaunsa route, kaunsa class

Aap UPAR se choose karte ho:
   Upper berth ya lower berth

Aap NAHI maang sakte:
   1AC — kyunki us train me 1AC hai hi nahi
   ↑ YE CAPABILITY BOUNDARY hai
```

## 🔴 Deal teen kaam karta hai

```
1. Kuch targeting PEHLE SE TAY kar deta hai      (market, device, content)
2. Kuch aapke liye CHHOD deta hai                (audience, postcode)
3. Aur kuch cheezein NAAMUMKIN kar deta hai      (capability boundary)
```

---
---

# 5. 🔴 Kya AUDIENCE deal me aati hai?

**Jawab: NAHI.** Audience deal ke **upar** lagti hai.

```
Deal        →  "UK me, TV par, Paramount My5 par ad chalao"    £22.96 CPM
                              +
Audience    →  "aur unme se sirf healthy-food waale logon ko"   +£1.63 VCPM
                              =
Effective   →  £24.59 CPM
```

## Audience do jagah se aa sakti hai

| Kahan se | Kya milta hai | Kharcha |
|---|---|---|
| **Amazon DSP** | Amazon ke segments — purchase data, search data, Prime Video viewing | £1.63 VCPM |
| **Inventory source (SSP)** | Netflix/Paramount ke apne segments — unki viewing data | Unki apni fee |

**Ye David ka Comment 1 aur 19 hai.** Pehle document kehta tha *"3P par sirf unki apni targeting"* — wo **galat** tha.

> **Amazon audiences 3P inventory par bhi chal sakti hain.** SSP ki targeting ek **alternative** hai, **only option** nahi.

## 🔴 PAR — deal ek boundary banata hai

Ye maine platform par pakda, aur ye zaroori hai:

```
3PS_Netflix_Always On_Auto Intenders_..._NOT Amazon Audience Enabled_STV_UK
                                          ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                                          NAAM me likha hai!

3PS_Netflix_Always On_Run of Network_Amazon Audience Enabled_STV_UK
                                     ↑ "NOT" nahi hai
```

**Paanch Netflix deals par Amazon audience NAHI lag sakti. Ek par lag sakti hai.**

🔴 **Aur ye deal object me FIELD nahi hai — sirf naam me hai.**

Isliye ye ek **data-quality request** hai client ke liye: *"Amazon Audience Enabled ko ek boolean field banao."*

## Ek line me

> **Audience deal me nahi hoti — par deal tay karta hai ki kaunsi audience LAG SAKTI hai.**

---
---

# 6. RATE CARD kya hota hai

Flowchart me aapne ye dekha:

```
2 - Choose CTV inventory
    GET /deals/,  GET /rates/ctv/:market/     ← ye rate card hai
```

## Deal aur Rate Card me farak

| | **Rate Card** | **Deal** |
|---|---|---|
| Kya hai | **Daam ki list** | **Asli bookable intezaam** |
| ID hoti hai? | ❌ Nahi | ✅ Haan — deal ID |
| Kya batata hai | *"Prime Video 30-second ka £25 hai"* | *"ye specific inventory tumhare liye reserved hai"* |
| Doosre ke bina exist karta hai? | ✅ **Haan** — deal na ho to bhi daam pata hota hai | Rate card ke bina deal ban hi nahi sakta |

## Analogy — shaadi ka banquet hall

```
RATE CARD  =  "500 guests ka hall, ₹5 lakh"          ← published daam
              Aap budget plan kar sakte ho
              Par booking nahi hui

DEAL       =  "12 December ke liye signed contract"   ← asli booking
```

## Rate card ka shape

```json
{
  "channels": [
    {
      "name": "Prime Video",
      "durations": [
        {"duration": "15", "cpm": "18.22"},
        {"duration": "30", "cpm": "25.00"}
      ]
    },
    {"name": "Netflix", "durations": [{"duration": "30", "cpm": "31.50"}]}
  ]
}
```

**Channel → duration → CPM.** Bas.

## 🔴 Rate card sabse zyada zaroori kab hota hai

Flowchart me dekhein:

```
Inventory tier?
        ↓
3P needs curation - Disney+
        ↓
"Rate-card CPM only — deal curated later, after the IO is signed"
```

**Disney+ ki deal ABHI EXIST NAHI KARTI.** Par rate card ka daam **hai**.

To agent kya karta hai:

```
1. Rate card se daam le:              Disney+ 30s = £34.00
2. Impressions calculate kare:        £5,000 ÷ £34 × 1000 = 147,058
3. Trader ko plan dikha de
4. Trader haan bole
5. VOW Disney+ se baat kare, IO sign ho
6. TAB deal bane
```

🔴 **Rate card ke bina Disney+ plan me aa hi nahi sakta.**

## Aur ek kaam — genre upsell

Flowchart me: *"flat rate card, plus optional genre deals at a higher CPM"*

```
Prime Video ROS      £18.22     ← Run Of Service, kahin bhi chalega
Prime Video Action   £22.07     ← sirf Action content ke saath

Farak: £3.85
```

**Agent brief padh kar suggest kar sakta hai:**

> *"Aapke brief me sports/action ki baat hai — £4 zyada me Action genre behtar match dega."*

🔴 **Par ye abhi buildable nahi hai** — kyunki `genre` field polluted hai (usme `"2026"`, `"TEST"`, `"15, 20, 30"` jaisi values hain).

## Ek line me

> **Rate card = daam ki list. Deal = signed booking. Rate card deal ke bina bhi kaam aata hai.**

---
---

# 7. AMC AUDIENCE kya hai

Flowchart me:

```
4 - Add audiences? optional
        ↓
"Retargeting, if prior campaign data"
        ↓
AMC audiences — POST /audiences/amc-audiences/
```

## AMC = Amazon Marketing Cloud

**Ek "clean room" hai** — ek surakshit jagah jahan advertiser apna data Amazon ke data ke saath **mila kar analyse** kar sakta hai, **par kisi ek insaan ki pehchaan nahi dekh sakta.**

## Normal audience vs AMC audience

| | **Normal Amazon audience** | **AMC audience** |
|---|---|---|
| Data kiska | **Amazon ka** | 🔴 **AAPKA khud ka** |
| Kaun use kar sakta hai | Koi bhi advertiser | Sirf aap |
| Example | *"jo healthy food kharidte hain"* | *"jo MERA pichla ad dekhe par kharida nahi"* |
| Chahiye kya | Kuch nahi | 🔴 **Pichla campaign data** |

## Analogy — dukaan ka register

```
NORMAL AUDIENCE:
   Aap ek list kharidte ho — "is ilaake me jo log health-conscious hain"
   Ye list bechne wale ke paas hai, sabko bechta hai

AMC AUDIENCE:
   Aapki DUKAAN ka register —
   "jo log pichle mahine aaye the, dekha, par kharida nahi"

   Ye list SIRF AAPKI hai. Kisi aur ke paas nahi.
```

## Kaam ke examples

| AMC audience | Kis liye |
|---|---|
| "Ad dekha, kharida nahi" | **Retargeting** — dobara dikhao |
| "6 mahine pehle kharida tha, ab nahi" | **Win-back** — wapas laao |
| "Cart me daala, chhod diya" | **Cart abandoners** — sabse zyada convert karte hain |
| "Pichle campaign me ad dekha" | **Frequency control** — inhe bar-bar na dikhao |
| "Product page dekha par cart me nahi daala" | High-intent browsers |

## "Clean room" ka matlab

```
❌ Aap NAHI dekh sakte:  "Rajesh Kumar, rajesh@email.com, ne ad dekha"

✅ Aap dekh sakte ho:    "45,000 logon ne ad dekha par kharida nahi"
                          → un 45,000 ka ek SEGMENT ban jaayega
                          → us segment par ad chalao
```

**Privacy bachi rehti hai, par targeting ho jaati hai.**

## 🔴 Do baatein jo dhyaan me rakhein

**1. Naye advertiser ke liye AMC bekaar hai.**

Pichla data nahi hai to kuch banega hi nahi. Isliye flowchart me likha hai *"if prior campaign data"* — ye **conditional** hai, hamesha available nahi.

**2. Flowchart kehta hai "Amazon inventory only" — par ye contested hai.**

David ke **Comment 19** ne yahi baat Amazon audiences ke liye theek ki thi (*"can use amazon audiences too"* on 3P). **AMC ke liye ye correction lagta hai ya nahi, ye pata nahi.**

🟠 **Ye ek open question hai.**

---
---

# 8. NARROW / BALANCED / WIDE kya hain

**Ye teen "shapes" hain jisme agent audience present karta hai.**

## Analogy — job posting

Ye sabse saaf example hai:

```
NARROW:    "5 saal Python + AWS + Delhi + fintech experience"
           →  20 candidates aayenge
           →  sab EXACTLY fit
           →  par 20 me se koi na mila to? PROBLEM (underdelivery)

BALANCED:  "3+ saal Python"
           →  300 candidates
           →  zyadatar theek hain
           →  usual choice

WIDE:      "koi bhi developer"
           →  5,000 candidates
           →  bahut milenge, par zyadatar fit nahi
```

## Asli numbers (staging se)

| Profile | Segments | Log |
|---|---|---|
| **Narrow** | 6 | ~1,200,000 |
| **Balanced** | 14 | ~4,800,000 |
| **Wide** | 31 | ~15,400,000 |

## 🔴 Teen zaroori corrections

### Correction 1 — Ye API feature NAHI hai (Comment 20)

```
Document soch raha tha:
   API teen ready-made groups deta hai
   { "bundles": { "narrow": [...], "balanced": [...], "broad": [...] } }

ASLIYAT:
   POST /api/audience-sets/suggest/     →  {"id": "abc-123"}    ← async!
   GET  /api/audience-sets/suggest/abc-123/
        →  ek FLAT LIST — 40+ segments, reach aur relevance ke saath

   Teen groups AGENT banata hai
```

**Restaurant analogy:** socha tha ready thali milegi — asal me kaccha saaman milta hai, thali khud banani padti hai.

### Correction 2 — Teeno ka DAAM SAME hai (Comment 2)

```
❌ Pehle document kehta tha:
   Narrow   £3.50 fee    ← mehnga
   Balanced £2.00 fee
   Wide     £0.85 fee    ← sasta

✅ Asliyat (maine verify kiya):
   Narrow   £1.63
   Balanced £1.63        ← BARABAR
   Wide     £0.00        ← free, par is wajah se ki usme
                            sirf Demographic + Device hai
```

**Fee ke teen rules:**

| Rule | Matlab |
|---|---|
| 1. Fee kab lagti hai | Jab **1P data** use ho — Amazon ka ya kisi 3P ka apna |
| 2. Compound nahi hoti | Ek provider se 1 segment lo ya 30 — **ek hi fee** |
| 3. Providers stack hote hain | Amazon + Experian = **dono** ki fee |

**Aur kaunsi category free hai:**

```
🟢 FREE  →  Demographic (age, gender, income) · Device
🔴 PAID  →  In-market · Lifestyle · Interest · Custom-built  →  £1.63
```

🔴 **Fee data se aati hai, breadth se nahi.** Teeno me farak **reach aur precision** ka hai, **paise ka nahi.**

### Correction 3 — Trader teeno DECLINE kar sakta hai (Comment 4)

```
Chautha option:  "koi audience nahi"
                 →  poori inventory par chalega (run of service)
                 →  koi data fee nahi
                 →  SABSE ZYADA impressions
```

| Kya chuna | Impressions | Fee |
|---|---|---|
| Balanced audience | 406,669 | £1.63 |
| **Koi audience nahi** | **435,540** | **£0** |

**Par ek nuksan:** reach kam aaye to agent *"audience widen karun?"* nahi keh sakta — audience hi nahi hai.

## "Widen karna" ka asal matlab kya hai

Audience ek **boolean tree** hoti hai. Maine ek asli set dekha (`Healthy snacks`):

```
AND
├── OR   Presence of children · Presence of Children aged 5-11 · 1 child
└── AND
    ├── OR   Females
    └── AND
        ├── OR   Age 36-40 · Age 36-45 (High Reach)
        └── OR   Healthy Food · Healthy Lifestyle · Health Conscious ·
                 Gluten Free · Diet and Nutrition · +12 more
```

**Padho:** *chhote bachon wale ghar* **AUR** *female* **AUR** *36-45 saal* **AUR** *healthy food interest*

**To "widen" karne ke do bilkul alag tareeke hain:**

```
Tareeka 1:  OR me ek term JODO
            "Healthy Food, Diet, ... + Organic Food"
            →  thoda widen hua

Tareeka 2:  poori AND branch HATAO
            "Age 36-45" wali shart hata do
            →  BAHUT widen hua
```

🔴 **Dono ka reach par bilkul alag asar hai** — aur isliye agent ko **batana** chahiye ki usne kaunsa kiya.

## Do chhoti baatein

**1. `audience_groups` ek JSON STRING hai, object nahi.** Do baar parse karna padta hai.

**2. Ek `prompt` field bhi hai** — natural language me, jaise:

```
"Mums looking for healthier snacks for their kids school lunch boxes"
"find me audiences who are most likely to buy car accessories for luxury cars"
```

🔴 **Yaani suggest feature pehle se use ho raha hai.** Aur agent ka kaam is step par asal me **prompt likhna** hai — segments browse karna nahi.

---
---

# 9. Sab kaise jodta hai — ek picture

```
┌─────────────────────────────────────────────────────────────────┐
│  RATE CARD                                                      │
│  "Prime Video 30s = £25, Netflix 30s = £31.50"                  │
│  Daam ki list. Deal na ho to bhi plan bana sakte ho.            │
│  GET /rates/ctv/{market}/                                       │
└──────────────────────────┬──────────────────────────────────────┘
                           │  isse deal banti hai / match hoti hai
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│  DEAL                                                           │
│  "3PS_Freewheel_UK_STV_Paramount_My 5"   £22.96 FLOOR           │
│  GET /deals/                                                    │
│                                                                 │
│  Isme BAKED:     market · device · app/web · ad lengths ·       │
│                  content (My5) · media type                     │
│  Iski BOUNDARY:  "Amazon audience lag sakti hai ya nahi"        │
└──────────────────────────┬──────────────────────────────────────┘
                           │  iske UPAR lagta hai
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│  AUDIENCE                          +£1.63 VCPM                  │
│                                                                 │
│  Normal:  Amazon ke segments (healthy food, parents)            │
│           POST /audience-sets/suggest/                          │
│           →  Narrow / Balanced / Wide me present hoti hai        │
│                                                                 │
│  AMC:     aapka khud ka data (retargeting)                      │
│           POST /audiences/amc-audiences/                        │
│           →  sirf jab pichla campaign data ho                    │
│                                                                 │
│  Ya:      koi audience nahi  →  run of service, free            │
└──────────────────────────┬──────────────────────────────────────┘
                           │  iske UPAR lagta hai
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│  EXTRA TARGETING                                                │
│  location (postcodes) · instream position · content exclusions   │
│  device narrowing · mobile OS (IOS/ANDROID)                      │
│  🔴 Ye strategy BANNE KE BAAD set hoti hai                      │
│  POST /strategies/{id}/targeting/{market}/locations/            │
└──────────────────────────┬──────────────────────────────────────┘
                           ↓
              EFFECTIVE CPM  =  £22.96 + £1.63  =  £24.59
              IMPRESSIONS    =  budget ÷ 24.59 × 1000
```

---
---

# 10. Ek page ka summary

| Concept | Ek line me |
|---|---|
| **Deal** | Pehle se tay intezaam — kaunsi inventory, kis daam. Ek "pass" jo inventory unlock karta hai |
| **Deal me kya hai** | 12 fields — pehchaan, paisa, kitni inventory (volume), aur kya chalega |
| **Targeting deal me?** | 🔴 **Adhi.** Market/device/content baked hai. Audience/postcode upar se lagta hai |
| **Audience deal me?** | ❌ **Nahi** — par deal tay karta hai ki kaunsi audience **lag sakti hai** |
| **Rate card** | Daam ki list. Deal ke bina bhi kaam aata hai (Disney+ ke liye zaroori) |
| **AMC audience** | Aapka khud ka pichla campaign data. Retargeting. Naye advertiser ke liye bekaar |
| **Narrow/Balanced/Wide** | Ek flat list ko teen breadth par present karna. **Daam same, reach alag** |

## Paanch cheezein jo yaad rakhni hain

```
1. Deal khud ek targeting decision hai — usse market, device aur
   content pehle se tay ho jaate hain

2. Audience deal ke UPAR lagti hai — par deal batata hai ki
   kaunsi audience LAG SAKTI hai (aur wo naam me chhupa hai)

3. Rate card aur Deal do alag cheezein hain — Disney+ ka daam
   pata hai par deal nahi hai

4. AMC = aapka khud ka data. Naya advertiser use nahi kar sakta

5. Narrow/Balanced/Wide me DAAM ka farak nahi hai — sirf
   reach aur precision ka
```

## Char cheezein jo abhi BLOCKED hain

| Kya | Kyun |
|---|---|
| Genre par matching | `genre` field me `"2026"`, `"TEST"`, `"15, 20, 30"` values hain |
| Channel par matching | Deal par `channel` field **exist hi nahi karti** |
| Tier ka fork | Deal par `inventory_tier` field **exist hi nahi karti** |
| Amazon-audience capability | Sirf deal ke **naam** me hai, field nahi |

**Char me se teen ke liye client se data-quality request bhejni hai.**

---

**Ye document `staging.vowmade.dev` par 4 August 2026 ki verification se bana hai — 83 deals, 15 audience sets, 17 APIs. Aur Wajahat ke chaar flowcharts se.**

**Poora specification `Strategy_Schema_v4.0_FINAL.md` me hai. Ye document sirf concepts samajhne ke liye hai.**
