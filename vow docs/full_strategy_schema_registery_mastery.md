# VOW Strategy Schema — FULL MASTERY GUIDE
### Ekdum easy words me, A to Z, real examples ke saath

> **Ye file kis liye hai?**
> Tumne (Kareem) Confluence par `Strategy Schema documentation v2.0` share kiya. David Moss (Manager) ne usme **28 comments** kiye.
> Comments ka reply dene se pehle tumhe poore document ki **mastery** chahiye — har section, har field, har technical word.
> Ye file wahi mastery deti hai. Isko padh lene ke baad tum kisi bhi team member ke kisi bhi sawaal ka jawab de sakoge.

---

## 🗂️ Is file me kya hai (Index)

| # | Part | Kya milega |
|---|---|---|
| 0 | **Do Documents ki Kahani** | v1.1.0 vs v2.0, legend, tumhara role |
| 1 | **Vocabulary Bible** | Har technical word — business + tech, ekdum simple |
| 2 | **Document ka Maksad** | SSOT kya hai, revision kyun hui |
| 3 | **Section 1: Core Principles** | 3 principles — what / why / purpose |
| 4 | **Section 2: Business Logic** | Selling location, attribution, **3 inventory tiers**, audiences |
| 5 | **Section 3: 13-Step Agentic Flow** | Har step, har field, real example ke saath |
| 6 | **Section 4: API Catalogue** | Har endpoint plain words me |
| 7 | **Section 5: Pydantic Models** | Har enum, har schema, har field |
| 8 | **Section 6: State Machine** | LangGraph state, 25-line flow, interrupt |
| 9 | **Section 7: Brief Parsing & Edge Cases** | Entity normalisation, failure protocols |
| 10 | **Section 8: Summary of Changes** | Poora change ledger |
| 11 | **⚠ Open Questions + Gaps** | David ke comments ki tayyari |
| 12 | **End-to-End Worked Example** | Ek brief, 13 steps, poora chalta hua |
| 13 | **Glossary A–Z** | Quick lookup table |
| 14 | **Self-Test** | 40 sawaal + jawab |

---

# PART 0 — Do Documents ki Kahani

## 0.1 Do files hain, dono ka farak samajh lo

| | **Document A** | **Document B** |
|---|---|---|
| **File** | `strategy_schema_registry.md` | `VOWAgent-Strategy Schema documentation v2.0.pdf` |
| **Version** | 1.1.0 | 2.0.0 |
| **Likha kisne** | **Tumne (Kareem)** | Revision — client feedback ke baad |
| **Status** | "Approved Technical Architecture" | **"For client verification"** (abhi approve NAHI hua) |
| **Structure** | **6-step UI wizard** ke hisaab se | **13-step agentic flow** ke hisaab se |
| **Scope** | Saare formats (Display, Online Video, Streaming TV, Prime Video) | **Sirf CTV** (Streaming TV + Prime Video) |
| **Pages** | ~630 lines markdown | 30 pages PDF |

**Ye samajhna sabse zaroori hai:** v2.0 tumhare kaam ko **reject** nahi karta. Wo tumhare v1.1.0 ko **base** maanta hai aur uske upar client ke confirmed decisions chipkata hai. Document ki pehli line hi ye kehti hai:

> *"Original version: 1.1.0 by Kareem. This revision: 2.0.0 — reordered, scoped to CTV, and extended with client-confirmed corrections."*

Aur summary page kehta hai: **~15 cheezein UNCHANGED** hain. Yaani tumhara aadha kaam bilkul sahi tha.

## 0.2 Legend — 4 nishaan jo har section par lage hain

v2.0 ka sabse smart design decision ye hai ki **har section par nishaan** laga hai. Isse reviewer (David) ko turant pata chal jaata hai ki kya naya hai aur kya purana.

| Nishaan | Matlab | Plain me |
|---|---|---|
| ✅ **UNCHANGED** | Kareem ne jo likha tha, wahi as-is rakha gaya | "Ye sahi tha, chhua nahi" |
| 🔄 **CHANGED** | Concept tha, par badal diya (purana bhi dikhaya gaya comparison ke liye) | "Ye tha, par ab aise hoga" |
| ➕ **NEW** | v1.1.0 me nahi tha, client feedback se aaya | "Ye bilkul naya hai" |
| ❌ **REMOVED** | v1.1.0 me tha, par CTV scope ke liye hataya (future scope me rakha) | "Delete nahi, sirf abhi nahi" |

**Purpose:** Ye "diff" hai — do versions ka farak. Isse client ek nazar me dekh sakta hai ki uski baat sun li gayi ya nahi. **David ke 28 comments me se kai comments in nishaano par hi honge** — jaise "ye UNCHANGED kyun likha hai jab actually change hua hai?"

## 0.3 Aur ek line jo document ki poori seriousness batati hai

Document ke aakhri page par:

> *"This document is for client verification. Once confirmed, it becomes the shared contract that Wajahat (state + graph), Vishal (registry), and Basil (adaptive canvas) build against."*

**Contract** = wo kaagaz jispar sab log sehmat hain. Ek baar sign, sab isi ke hisaab se banayenge.

To document approve hone ke baad:
- **Wajahat** — LangGraph ka **state + graph** banayega (agent ki yaadash aur raasta)
- **Vishal** — **registry** banayega (schema/field definitions ka central store)
- **Basil** — **adaptive canvas** banayega (chat ke saath badalta UI)
- **Riddhi** — UI (tumhare task slide ke mutabik tum output usko dete ho)
- **Tum (Kareem)** — **Planning Agent ka dimaag** — brief se Strategy Card banane wali conversation

**Isliye ye document approve hona zaroori hai.** 4 logon ka kaam isi par ruka hai. Agar schema me galti reh gayi, 4 log galat cheez bana denge. **David tumhe rok nahi raha — wo contract theek kara raha hai.**

## 0.4 Tumhara exact role (task slide se)

> **"Kareem — Planning Agent (M1). Owns the brain."**
> **"In plain terms: a form that fills itself in as you chat."**

**Tum kya produce karoge:**
1. Conversation + slot-filling (khud bharne wala form)
2. Narrow / Balanced / Wide — teen audience options
3. Forecast + repair loop (bahut chhoti audience ko khud chaudi karna)
4. Executable Strategy Card — approval ke liye ready
5. 50–100 session ka evidence pack

**Input:** Wajahat · Vishal · Apramit · Swagger → **Tum** → **Output:** Riddhi (UI)

**Pehla kaam (START HERE):** *"Design the Strategy schema — jointly with Wajahat & Vishal. M0 is design; M1 is build."*

- **M0** = Milestone 0 = **design phase** ← abhi yahi chal raha hai (ye document)
- **M1** = Milestone 1 = **build phase** = code likhna

**Matlab:** jab tak M0 (ye document) approve nahi hota, M1 (code) shuru nahi ho sakta. Isliye tumhari mastery aur David ke comments ka jawab dono critical hain.

---

# PART 1 — VOCABULARY BIBLE
### Har technical word — start se end tak jo aayega

Ye part sabse important hai. Document ka 90% content **business reality** hai, code nahi. Ye words samajh gaye to document apne aap khul jaayega.

---

## 1.A — Kaun-Kaun Log Hain (Kirdaar)

Poori chain ye hai:

```
ADVERTISER  →  TRADER  →  VOW  →  Amazon DSP  →  PUBLISHER  →  TV screen
  (Nike)      (insaan jo   (tumhara   (kharidne ka   (Prime Video,   (ghar me
              ad chalata   platform)   engine)        Netflix,        dekhne wala)
              hai)                                   Disney+)
```

### **Advertiser**
Jiska product hai. Jiska paisa hai. Example: Nike, Coca-Cola, ya ek chhota "BrightPath Online Courses" jaisa education website.

Document me ye `advertiser_id` field ke roop me aata hai — ek UUID jaise `353eea43-bc42-456f-ba4f-3d3e20ea6bc8`.

### **Trader** (ya Media Buyer / Media Planner)
Wo **insaan** jo asli me campaign set karta hai. Advertiser kehta hai "mujhe UK me awareness chahiye", trader deals chunta hai, budget baantta hai, audience select karta hai.

> **🎯 YE TUMHARA USER HAI.** Document me jahan bhi "trader" likha ho, matlab **wo insaan jo tumhare agent se chat kar raha hai.**

Document me trader ka zikr:
- *"The agent must state which it chose and why, so the trader can adjust"* (Step 3)
- *"Trader picks one of the three"* (Step 4)
- *"shown per option so the trader sees the real cost"* (Step 4)

**Design lesson:** Agent trader ko **replace** nahi kar raha. Agent trader ka **assistant** hai. Faisla trader leta hai. Isliye har jagah agent ko apni assumption **batani** padti hai.

### **DSP — Demand Side Platform**
**Plain:** kharidne walon ka software.

- **Demand side** = jise ad chahiye (Nike) — demand yaani zaroorat
- **Supply side** = jiske paas jagah hai (Netflix) — supply yaani maal

DSP ek dukaan/exchange hai jahan se trader ad slots kharidta hai. Yahan **Amazon DSP** use ho raha hai.

**Real example:** Nike ko Netflix par ad chahiye. Nike Netflix ko phone nahi karti. Nike ka trader Amazon DSP me jaata hai, Netflix ka deal dhoondta hai, kharid leta hai. Amazon DSP beech me sab handle karta hai — bidding, delivery, reporting.

### **Publisher**
Jinke paas dikhane ki jagah hai — Prime Video, Netflix, Disney+, Hulu.

Document me inhe **"provider"** bhi kehte hain (`SelectedDealSchema.provider` field: *"e.g. Prime Video, Netflix, Disney+"*).

### **VOW**
Tumhari company ka platform. Trader aur Amazon DSP ke beech baithta hai.

Trader VOW me kaam karta hai → VOW peeche se Amazon DSP se baat karta hai. Aur **tum** VOW ke andar ek AI agent bana rahe ho.

---

## 1.B — CTV: Document ki Reeh ki Haddi

### **CTV — Connected TV**
**Plain:** wo TV jo **internet se juda** hua hai.

Smart TV, Fire Stick, Roku, Apple TV, ya TV par chal raha Prime Video app.

**Real example:** Tum Prime Video par movie dekh rahe ho. Beech me 30-second ka ad aata hai. **Wo CTV ad hai.** Kisi ne wo slot programmatically kharida hai.

### **Linear TV** (iska ulta)
Purana broadcast TV — channel fix time par program chalata hai. Tum bas dekhte ho, choose nahi karte.

### **Streaming TV vs Prime Video** — document ke do formats
- `prime_video` = Amazon ka apna Prime Video
- `streaming_tv` = baaki streaming inventory (Netflix, Disney+, Hulu waghera Amazon DSP ke through)

### **🔴 v2.0 ka SABSE BADA decision: scope sirf CTV**

| v1.1.0 me formats | v2.0 me formats |
|---|---|
| `display` ✅ | `display` ❌ **future scope** |
| `online_video` ✅ | `online_video` ❌ **future scope** |
| `streaming_tv` ✅ | `streaming_tv` ✅ **IN SCOPE** |
| `prime_video` ✅ | `prime_video` ✅ **IN SCOPE** |

**Scope** = "abhi hum ye banayenge, baaki baad me."
**Future scope** = "delete nahi kiya, sirf abhi nahi banayenge."

**Why (kyun)?** Kyunki CTV ke rules Display se **bilkul alag** hain:
- CTV me click nahi hota → click-based KPI bekaar
- CTV video-only hai → image creatives bekaar
- CTV me deals pehle se curated hote hain → open auction browsing bekaar

Ek hi document me dono ghusane se **contradiction** aata. Isliye alag kar diya.

**Purpose:** Team ko clarity mile ki M1 me exactly kya banana hai. Scope creep (kaam ka phailna) rukta hai.

---

## 1.C — PAISA: 6 Words Jo Har Page Par Aayenge

Ye 6 samajh liye to document ka aadha hissa khul gaya.

### 1. **Impression**
Ad ka **ek baar dikhna**.

**Real example:** Rahul ne Prime Video par Nike ka ad dekha. = 1 impression.
Rahul ne wahi ad 3 baar dekha (3 din, 3 episodes) = **3 impressions**, par **1 person**.

### 2. **CPM — Cost Per Mille**
"Mille" Latin me hazaar. Matlab **1,000 impressions ka daam**.

**Formula (document page 13 se, literally):**
```
Impressions = budget ÷ CPM × 1,000
```

**Real example — poora ganit:**
```
Budget         = £10,000
CPM            = £30
Impressions    = 10,000 ÷ 30 × 1,000 = 333,333 impressions
```

Ye number document ke API example me literally hai: `"estimated_impressions": 333333`

**Ek aur example (chhota budget):**
```
Budget = £5,000, CPM = £25
Impressions = 5,000 ÷ 25 × 1,000 = 200,000 impressions
```

### 3. **Reach**
**Kitne alag-alag (unique) log** ne dekha.

333,333 impressions ka matlab 333,333 log **nahi**. Kuch logon ne kai baar dekha.

Document ke example me: `"estimated_unique_reach": 210000`

### 4. **Frequency**
Ek banda **average kitni baar** dekha.

```
Frequency = Impressions ÷ Reach
          = 333,333 ÷ 210,000
          = 1.58
```

Document me literally: `"average_frequency": 1.58`

**Matlab:** average banda ye ad **1.58 baar** dekha.

### 🔴 **Reach vs Frequency — Document ka Chhupa Hua Theme**

Same paise me tum **dono** nahi paa sakte:

| Tum chahte ho | Kya hoga |
|---|---|
| **Zyada log** (high reach) | Har banda **kam baar** dekhega |
| **Baar-baar dikhana** (high frequency) | **Kam log** dekhenge |

**Real example — £10,000, 333,333 impressions:**
- Option A: 300,000 logon ko 1.1 baar → bahut log, par yaad nahi rahega
- Option B: 50,000 logon ko 6.6 baar → kam log, par pakka yaad rahega

**Kaun sahi hai?** Ye brand ke maksad par depend karta hai. **Isliye Step 1 me trader se puchte hain: "KPI kya hai — reach ya frequency?"**

### 5. **KPI — Key Performance Indicator**
**Plain:** "success kis number se naapoge?"

Agar KPI = `reach` → agent zyada log dhoondega
Agar KPI = `frequency` → agent kam logon ko baar-baar dikhayega

### 6. **VCPM aur Effective CPM**

- **Deal CPM** = inventory (slot) ka daam
- **VCPM** = audience data use karne ki **extra fee**
- **Effective CPM** = **asli total daam**

**➕ v2.0 ka NEW insight (page 3), literally:**
> *"the audience fee (VCPM) stacks on top of the deal CPM. A narrow audience is both smaller and more expensive per impression. The agent should surface the effective CPM (deal + audience fee), not just the deal price."*

**"Stacks on top"** = upar se jud jaata hai.

**Real example:**
```
Prime Video Preferred Deal CPM  = £28.88
"Healthy Snacks" audience VCPM  = £ 1.63
--------------------------------------
EFFECTIVE CPM                   = £30.51   ← trader ye dega
```

Trader ko sirf £28.88 dikhana **misleading** hai. Aur uska asar:
```
£28.88 CPM par → 10,000 ÷ 28.88 × 1000 = 346,260 impressions
£30.51 CPM par → 10,000 ÷ 30.51 × 1000 = 327,761 impressions
                                          ↑ 18,499 impressions kam!
```

**Aur ek zaroori baat:** Narrow audience **do tarah se buri** hai — chhoti bhi hai **aur** mehngi bhi (VCPM zyada). Isliye Narrow ka double nuksaan.

**Purpose:** Trader ko sach dikhana. Ye document ke **Zero-Hallucination** principle ka hi extension hai.

---

## 1.D — GOAL: Marketing Funnel

Ad ka maksad kya hai?

```
        ╔═══════════════════════════════════════╗
        ║  AWARENESS — "log jaan jaayein"       ║  ← upar, chaudi, bahut log
        ╚═══════════════════════════════════════╝
             ╔═════════════════════════════╗
             ║  CONSIDERATION — "sochein"  ║      ← beech
             ╚═════════════════════════════╝
                  ╔═══════════════════╗
                  ║ CONVERSION —      ║             ← neeche, patli, kam log
                  ║ "kharid lein"     ║
                  ╚═══════════════════╝
```

**Funnel** = chhanni/kip. Upar 1,00,000 log aate hain, neeche 1,000 kharidte hain.

### 🔴 v2.0 ka bada change: CTV ka goal HAMESHA Awareness

Client ne literally kaha (document page 6):
> *"CTV is typically used as an Awareness goal as it's hard to track anything further down the funnel"*

**Plain me:** TV par ad dekh kar koi turant remote se checkout nahi karta. To "kharidne" ko naapna CTV me mushkil hai.

**Iska seedha asar:**

| Field | v1.1.0 | v2.0 |
|---|---|---|
| **Goal** | 3 choices (Awareness/Consideration/Conversion) | **Fixed = `AWARENESS`** |
| **KPI** | 6 choices | **Sirf `reach` ya `frequency`** |

### Wo 4 KPI jo hataye gaye — inka matlab (jaan lo, poochha jaayega)

| KPI | Full form | Matlab |
|---|---|---|
| **CTR** | Click Through Rate | Kitne % logon ne click kiya |
| **CPC** | Cost Per Click | Ek click ka daam |
| **CPA** | Cost Per Acquisition | Ek customer banane ka daam |
| **CPDPV** | Cost Per Detail Page View | Ek banda Amazon product page tak pahuncha, uska daam |

**Ye chaaron CLICKS ya PURCHASE naapte hain. CTV me click nahi hota. Isliye ❌ hataye gaye.**

> 💡 **Ye tumhara ready-made jawab hai** agar koi puche "CTR kyun nahi hai?" — *"Kyunki CTV me remote se click nahi hota. Click-based metric wahan bekaar hai."*

---

## 1.E — DEAL & INVENTORY

### **Inventory**
**Plain:** bechne ke liye available **ad slots**. Dukaan ka "stock" jaisa.

Netflix ke paas roz karodon impressions ki jagah hai — wo unka inventory hai.

### **Deal**
Publisher ke saath ek **pehle se tay hua sauda**: "itne daam par, is tarah ki jagah, mujhe milegi."

**Real example (document se):** `Prime Video | Preferred Deal | UK - 30 | £28.88`
Padho: Prime Video ka Preferred Deal, UK market, 30-second ads, £28.88 CPM.

Deal ID example: `EXT7P75718S8MNR`

### 3 Deal Types (v1.1.0 aur v2.0 dono me ✅ SAME)

| Deal Type | Daam | Commitment | Pause? |
|---|---|---|---|
| **Programmatic Guaranteed (PG)** | Fixed CPM, **guaranteed volume** | **Poora budget owed** | ❌ **Nahi** |
| **Preferred Deal** | Fixed CPM | Koi nahi | ✅ Haan |
| **Private Auction** | Floor CPM, competitive | Koi nahi | ✅ Haan |

**Plain analogy:**
- **PG** = Hotel ka **non-refundable** booking. Kamra pakka, paisa pakka jaayega. Cancel kiya = paisa gaya.
- **Preferred Deal** = Daam tay hai par lena zaroori nahi. Aaram se pause.
- **Private Auction** = Boli lagti hai, par **floor** (minimum) tay hai. "Private" = sirf invited buyers bid kar sakte hain.

**Floor CPM** = neeche ki limit, isse kam pe bech nahi sakte.
**Guaranteed volume** = "itne impressions milenge, guarantee."

### ⚠ PG ka Khatra — Agent Design ke liye Zaroori

> Agar agent galti se PG deal chun le aur trader baad me campaign band kare → **poora paisa gaya**, kuch bacha nahi.

**Isliye** document me "Can pause?" column hai. Agent ko ye pata hona chahiye. **Ye ek gap hai** — document me kahin nahi likha ki agent PG choose karte waqt trader ko warn karega. **David ne yahan comment kiya ho sakta hai.**

---

## 1.F — AUDIENCE

### **Audience Set / Segment**
Logon ka ek **group** jinhe target karna hai.

**Real examples (document se):**
- `Healthy snacks` — VCPM £1.63
- `Higher Education Seekers` — VCPM £1.85, estimated reach 450,000
- `E-Learning & Tech Enthusiasts` — VCPM £1.63, reach 1,200,000
- `General Career Advancement` — VCPM £1.20, reach 3,500,000

**Dhyan do pattern:** Jaise-jaise audience badi hoti hai, **VCPM sasti** hoti jaati hai (£1.85 → £1.63 → £1.20) aur **reach badhti** jaati hai (450K → 1.2M → 3.5M). Ye bilkul logical hai — specific data mehnga, general data sasta.

### 🔴 ~3,400 Segments — aur uska natija

**➕ v2.0 NEW (page 3), literally:**
> *"audiences are mandatory and suggestion-driven. The agent always suggests three options using VOW's existing pgvector + OpenAI feature (POST /audience-sets/suggest/). **Nobody browses the ~3,400 segments manually.**"*

**Do bade badlav isme chhupe hain:**

1. **Mandatory** (pehle optional thi) — audience choose kiye bina aage nahi
2. **Suggestion-driven** — koi insaan 3,400 me se haath se nahi dhoondega. **Agent suggest karega.**

**Why?** 3,400 options ka dropdown **insaan ke liye bekaar** hai. Wo 20 dekhega, thak jaayega, galat chun lega. Machine 3,400 me se sahi 5-10 nikal sakti hai.

### 3 Audience Profiles

| Profile | Kya hai | Trade-off |
|---|---|---|
| **Narrow** (High Precision) | Bilkul sahi log, kam log, **elevated intent** | Mehngi VCPM + **underdelivery ka risk** |
| **Balanced** (Recommended) | Beech ka raasta, best blend | **Default suggestion** |
| **Wide** (Maximum Scale) | Bahut log, mota demographic target | Sasti VCPM, **kam precision** |

**Intent** = kharidne ki niyat. "High intent" = ye banda kharidne ke bahut kareeb hai.
**Precision** = nishaana kitna sahi.
**Scale** = kitne bade paimane par.

### **Underdelivery** — Narrow ka Asli Khatra
**Plain:** plan kiya tha 2,00,000 log, mile sirf 20,000.

**Kyun?** Audience itni chhoti thi ki budget kharch hi nahi ho paya. Slots hi nahi mile.

**Real example:**
```
Audience: "UK me Rolex pehnne wale, 45-50 saal, Manchester me rehne wale,
           jo golf khelte hain aur electric car chalate hain"
→ Total log: 800
→ Budget: £10,000
→ Nateeja: £400 kharch hua, £9,600 wapas. Campaign fail.
```

**Yahi wajah hai ki "Repair Loop" banaya gaya** (Part 5, Step 6 me detail me).

### 🔄 v2.0 me "Broad" → "Wide"
Client ki vocabulary ke hisaab se naam badla.

> **⚠ GAP:** Code enum me `WIDE = "WIDE"` hai (page 22), **par** document ke API example me abhi bhi `bundles.broad` likha hai (v1.1.0 se copy hua). **Ye inconsistency hai. David ne yahan comment kiya ho sakta hai.**

### ❌ Product Audiences — hataye gaye
**Product audience** = "jinhone is ASIN ko dekha/kharida, unhe dikhao."
CTV ke liye applicable nahi (client ne kaha) → removed.

### **AMC — Amazon Marketing Cloud** (conditional)
Amazon ka **data room** jahan advertiser ka **purana campaign data** hota hai.

Document kehta hai AMC audiences **conditional** hain — *"available only when the advertiser has prior campaign data (retargeting tactic)."*

**Why?** AMC purane data se audience banata hai. **Naya advertiser** — data hi nahi hoga. To ye feature uske liye khaali rahega.

**Retargeting** = jo log pehle aaye the, unhe dobara dikhana.

---

## 1.G — CREATIVE

### **Creative**
**Asli ad** jo screen par dikhta hai. CTV me = **video file**.

### **Asset**
System me register hua media file (video/image).

**Real example (document se):** `SC_WGY_30s_HEART_Online_16x9`
Padho: SC=Snack Co, WGY=campaign code, **30s=30 second**, HEART=creative theme, 16x9=aspect ratio.

### **Duration** — 10, 15, 20, 30 seconds
Video ki lambai.

### 🔴 Duration itni important kyun hai? (3 wajah)

**1. Duration decide karta hai kaunse DEALS available hain**
Document page 5, literally: *"Determines which deals are available and what CPM applies"*
Kuch deals sirf 15s ke liye hain, kuch sirf 30s.

**2. Har duration ka ALAG CPM**
30s mehnga (zyada screen time), 15s sasta.

**3. Isliye same budget me alag impressions:**
```
Budget £10,000
15s ad @ CPM £20  →  10,000 ÷ 20 × 1000 = 500,000 impressions
30s ad @ CPM £30  →  10,000 ÷ 30 × 1000 = 333,333 impressions
                                           ↑ 167,000 kam!
```

**Isliye ➕ v2.0 me "Creative Durations" Step 1 me hi Required field ban gaya** — kyunki iske bina deals hi filter nahi ho sakte.

**Aur isliye ➕ Step 9 me "Duration Match Check" aaya:**
> Plan me 15s tha, trader ne 30s video upload kar diya → **impressions 500K se 333K ho gaye** → poora plan ka ganit badal gaya → **dobara approval chahiye.**

### **Click-Through URL**
Ad par click karne se kahan jaayega. Example: `https://example.com/landing`

> **⚠ GAP:** CTV me remote se click nahi hota, phir bhi ye field **Required** hai (v1.1.0 se ✅ UNCHANGED). Document ne isko justify nahi kiya. **David ne yahan comment kiya ho sakta hai.** Possible reasons: Amazon DSP ka field mandatory hai, ya interactive/QR CTV formats ke liye.

### **Approval Status** — creative ka
Har platform apna review karta hai: `PENDING` → `APPROVED` ya `REJECTED`.

---

## 1.H — TRACKING: ASIN, Ad Tag, aur Attribution

Ad chal gaya. Ab pata kaise chalega kaam hua?

### Do Case — Selling Location

#### **Case A: `ON_AMAZON`** (Endemic)
Advertiser Amazon par bechta hai.

**ASIN — Amazon Standard Identification Number**
Amazon par har product ka **unique code**. Example: `B08N5WRWNW`

ASIN dene se Amazon khud bata deta hai:

| Metric | Full form | Matlab |
|---|---|---|
| **DPV** | Detail Page View | Product page kitni baar khula |
| **ATC** | Add To Cart | Cart me kitni baar dala |
| **Purchase** | — | Kitne bike |
| **ROAS** | Return On Ad Spend | £1 ad me lagaya, kitna sale aaya |

**ROAS example:** £10,000 ad kharch, £40,000 sale → **ROAS = 4x**

**➜ ASIN yahan REQUIRED hai.**

#### **Case B: `NOT_SOLD_ON_AMAZON`** (Non-Endemic)
Advertiser apni website par bechta hai.

**Ad Tag** = ek **chhota code** jo advertiser apni website par lagata hai. Ye Amazon ko batata hai "koi aaya, kisi ne cart me daala, kisi ne kharida."

**➜ ASIN yahan OPTIONAL hai.** Par kyun rakha? **Halo sales** ke liye.

### **Halo Sales** — bahut interesting concept
**Plain:** Netflix par ad dekha, phir seedha **Amazon** par jaake wahi cheez kharidi — bina click kiye.

Ad ka "halo" (aura/prabhav) effect. ASIN de do to Amazon ye bhi bata dega.

**Real example:**
```
BrightPath ka ad Prime Video par chala.
Rahul ne dekha. Rahul ne BrightPath ki website par nahi gaya.
Rahul ne Amazon par "online course" search kiya aur BrightPath ka book kharid liya.
→ Ye HALO SALE hai. ASIN diya tha, to ye track ho gaya.
```

### **Ad Tag Conversions** — kaunse events track karne hain
`Page view` · `Add to shopping cart` · `Checkout` · `Application`

**Conversion** = koi kaam ho jaana jo tum chahte the.
**Application** = form submit karna (jaise loan/course ke liye apply).

### ⚠⚠ Ad Tag ki SABSE ZAROORI Warning

Document page 17, literally:
> *"the tag must be installed before the campaign runs (**tracking only records activity after it goes live**)"*

**Plain me:** ad tag **pehle** lagana padega. Baad me lagaya to jo pehle hua wo **hamesha ke liye gaya** — peeche ka data recover nahi hota.

**Isliye Step 11 me agent check karta hai:** "tag laga hai ya nahi? Nahi laga to yahan setup instructions hain."

### **Attribution** aur **Attribution Window**

**Attribution** = credit dena. "Ye sale ad ki wajah se hui."

Document: **14-day post-view aur post-click** (✅ UNCHANGED)

**Plain:** ad dekhne ke **14 din ke andar** koi kharide → ad ko credit. 15ve din → credit nahi.

| Term | Matlab |
|---|---|
| **post-view** | Ad **dekha** (click nahi kiya) → 14 din ka window |
| **post-click** | Ad par **click** kiya → 14 din ka window |
| **Window** | Time ki khidki |
| **Lookback** | Peeche dekhna — "sale hui, peeche 14 din me koi ad tha?" |

**CTV ke liye `post-view` hi kaam ka hai** kyunki click nahi hota.

### **Endemic / Non-Endemic**
Bas fancy words:
- **Endemic** = Amazon par bechta hai (`ON_AMAZON`)
- **Non-Endemic** = Amazon par nahi bechta (`NOT_SOLD_ON_AMAZON`)

---

## 1.I — Aur 5 Business Words

| Word | Full form | Matlab | Document me kahan |
|---|---|---|---|
| **IO** | Insertion Order | Advertiser aur publisher ke beech ka **signed contract** | *"VOW curates the deal after the IO is signed"* (Disney+ tier) |
| **ROS** | Run Of Schedule | "Koi khaas genre nahi, jahan slot mile chala do" — **sasta** | *"Prime Video ROS at $18.22"* |
| **Genre** | — | Content ki kism: Action, Comedy, Sports, Drama | Genre upsell logic |
| **Rate Card** | — | **Daam ki list** — "Netflix 30s = $X" | `GET /api/rates/ctv/{market}/` |
| **Curation** | — | Deal ko **haath se banana** (automatic nahi) | 3P-needs-curation tier |

**ROS vs Genre — real example (document se):**
```
Prime Video ROS    = $18.22 CPM   ← jahan slot mile
Prime Video Action = $22.07 CPM   ← sirf Action content me
                     ↑ $3.85 mehnga, kyunki specific hai
```

---

## 1.J — TECH WORDS (Code ki taraf)

Ab technical words. Har ek ka **plain matlab + document me kahan aata hai.**

### **Schema**
**Plain:** ek **form ka blueprint** — kaunse khaane hain, har khaane me kya daal sakte ho, kaunsa khaana zaroori hai.

**Real example:** Bank ka form. "Naam = text, zaroori. Umar = number, zaroori. Middle name = text, optional." **Yahi schema hai.**

**Purpose:** Sab log ek hi shape ki data bhejein. Frontend, backend, agent — sab same samjhein.

**Isliye is document ka naam "Strategy Schema" hai** — ye Strategy ka blueprint hai.

### **Slot**
**Plain:** form ka **ek khaana** jise bharna hai.

Example: `strategy_name` ek slot hai. `flight_dates` ek slot hai.

### **Slot Filling**
**Plain:** baat karte-karte khaane bharte jaana.

**Real example:**
```
Trader: "UK me August me £10,000 ka Prime Video campaign"
Agent (peeche se):
  markets        = ["GB"]        ✅ bhar gaya
  flight_dates   = Aug 2026      ✅ bhar gaya
  market_budgets = £10,000       ✅ bhar gaya
  formats        = prime_video    ✅ bhar gaya
  strategy_name  = ???           ❌ khaali
  durations      = ???           ❌ khaali

Agent: "Samajh gaya. Do cheezein batao — strategy ka naam kya rakhun,
        aur video kitne second ka hai?"
```

**Yahi tumhare task slide ka "a form that fills itself in as you chat" hai.**

### **Stateful**
**Plain:** **yaad rakhne wala.**

**Stateless** = har baar bhool jaana (jaise Google search — pichhla search yaad nahi).
**Stateful** = pichhli baat yaad rehna.

**Real example:**
```
Trader: "UK me campaign chahiye"
Agent: "Budget?"
Trader: "£10,000"
Agent: "Theek hai, UK me £10,000."   ← UK YAAD RAHA. Ye stateful hai.
```

### **State**
**Plain:** agent ki **yaadash ka dabba** — ab tak jo pata chala, sab isme hai.

Document me `PlanningAgentState` — ek bada dictionary jisme 40+ fields hain.

### **LangGraph**
**Plain:** ek library jo AI agent ko **step-by-step raasta** banane deti hai, aur beech me **state yaad** rakhti hai.

Socho ek **flowchart** jo asli me chalta hai. Har dabba ek kaam karta hai, teer (arrow) batate hain aage kahan jaana hai.

**Why LangGraph?** Kyunki:
1. **Loops** chahiye (audience chhoti → widen → phir forecast → phir check)
2. **Branches** chahiye (Amazon inventory → forecast karo; Netflix → mat karo)
3. **Rukna** chahiye (approval ka wait — `interrupt()`)
4. **State** yaad rehna chahiye

Simple LLM call se ye nahi hota.

### **Node**
**Plain:** flowchart ka **ek dabba** = ek kaam.

Document ke nodes: `extract_fields`, `select_inventory`, `propose_budget_split`, `suggest_audiences`, `predict_reach`, `create_strategy`, `activate` waghera.

### **Edge**
**Plain:** dabbon ke beech ka **teer** — "iske baad ye."

### **interrupt()**
**Plain:** graph ko **beech me rok dena** aur insaan ka intezaar karna.

Document page 14, literally:
> *"Implementation: LangGraph `interrupt()`. The graph physically stops and persists state. It cannot proceed until a human sends approve or reject."*

**Persists** = save kar deta hai (disk par), taaki server band ho jaaye to bhi data na jaaye.

**Real example:**
```
Agent: plan taiyar → Strategy Card dikhaya → ⏸ RUK GAYA
(3 ghante beet gaye, server restart ho gaya)
Manager: "Approve"
Agent: wahin se aage chala — kuch bhoola nahi
```

### **Checkpointer**
State ko save/load karne wala hissa. (Tumhare repo me `app/agent/checkpointer.py` hai.)

### **Pydantic**
**Plain:** Python ki ek library jo **data ki jaanch (validation)** karti hai.

**Real example:**
```python
class Person(BaseModel):
    name: str          # text hona chahiye
    age: int           # number hona chahiye

Person(name="Rahul", age=25)      # ✅ theek
Person(name="Rahul", age="paach") # ❌ ERROR — age number nahi hai
```

**Why?** Agar galat data andar aa gaya, wo Amazon DSP tak pahunch jaayega aur wahan fail hoga — tab debug karna mushkil. Pydantic **darwaze par hi** rok deta hai.

**Purpose:** Zero-Hallucination principle ko technically enforce karna.

### **BaseModel**
Pydantic ka base class. `class X(BaseModel)` likhne se X ek validated schema ban jaata hai.

### **Field(...)**
Pydantic me field define karna. Teen roop:
```python
name: str = Field(...)                    # ... matlab REQUIRED
currency: str = Field("GBP")              # default value GBP
notes: Optional[str] = Field(None)        # OPTIONAL, default khaali
```

**`...` (three dots / Ellipsis) = "ye field ZAROORI hai."** Ye Python ka special value hai.

### **Optional[X]**
"Ye X ho sakta hai, ya khaali (None) ho sakta hai."

### **default_factory=list**
"Default me khaali list rakho." (`[]`)

### **Enum**
**Plain:** **fix choices ki list.** Isse bahar kuch nahi.

**Real example:**
```python
class CurrencyEnum(str, Enum):
    EUR = "EUR"
    GBP = "GBP"
    USD = "USD"
```
Matlab currency sirf ye 3 ho sakti hai. `"INR"` daalo → error.

**Why?** Typo rokta hai. Koi `"gbp"` ya `"Pound"` na likh de.

**`str, Enum` kyun?** Taaki value string ki tarah bhi kaam kare (JSON me bhejne ke liye).

### **TypedDict**
**Plain:** ek **dictionary jiske keys aur unke types pehle se tay hain.**

Pydantic se farak: TypedDict **validate nahi karta**, sirf editor ko batata hai. Halka hai. Isliye LangGraph state ke liye use hota hai (state bahut baar update hota hai, har baar validation slow hoga).

### **Annotated[list, add_messages]**
LangGraph ka special pattern.

**Plain:** "ye list hai, aur jab naya message aaye to **purane ko replace na karo, peeche jod do**."

Bina iske: naya message aaya → poori list overwrite → **puri chat bhool gayi**.
Iske saath: naya message **append** hota hai → chat bachi rehti hai.

### **REST API**
**Plain:** do software ke beech baat karne ka tarika. Ek **puchhta** hai, doosra **jawab** deta hai.

- **Endpoint** = ek pata (URL). Example: `/api/deals/`
- **GET** = "mujhe data do" (padhna)
- **POST** = "ye data lo / ye banao" (likhna)
- **Payload / Request body** = jo data tum bhejte ho
- **Response** = jo data wapas aata hai

### **HTTP Status Codes**
| Code | Matlab |
|---|---|
| **200 OK** | Sab theek, ye lo data |
| **201 Created** | Nayi cheez **ban gayi** |
| 400 | Tumhara request galat tha |
| 404 | Cheez mili nahi |
| 500 | Server me gadbad |

**200 vs 201 ka farak:** 200 = "data mil gaya". 201 = "**nayi cheez ban gayi**". Isliye `POST /api/strategies/` → **201 Created** (nayi strategy bani).

### **JSON**
Data likhne ka format. `{ "key": "value" }`

### **UUID**
Universally Unique Identifier — ek lamba unique code jo duniya me kisi aur ka nahi hoga.
Example: `353eea43-bc42-456f-ba4f-3d3e20ea6bc8`

### **Path Parameter — `{market}`**
URL me `{...}` ka matlab "yahan asli value daalo."
```
Template: /api/contextual-targeting/{market}/asin-validation/
Asli call: /api/contextual-targeting/GB/asin-validation/
```

### **Query Parameter — `?name=...`**
URL ke `?` ke baad ka hissa.
```
/api/strategies/check_strategy_name_uniqueness/?name=Summer_Brand_2026
                                                 ↑ query parameter
```

### **pgvector + Embedding + Vector Similarity Search**
Document kehta hai audience suggestion **"VOW's existing pgvector + OpenAI feature"** se hoti hai.

**Plain me kaise kaam karta hai:**

1. **Embedding** = kisi text ko **numbers ki lambi list** me badalna, taaki uska **matlab** numbers me aa jaaye.
   ```
   "online learning platform" → [0.23, -0.81, 0.44, ... ] (1500 numbers)
   "Higher Education Seekers" → [0.25, -0.79, 0.41, ... ] (1500 numbers)
                                  ↑ bahut kareeb! Matlab milta hai.
   ```

2. **pgvector** = PostgreSQL database ka ek **extension** jo in numbers ko store karta hai aur "kaun kiske kareeb hai" dhoondh sakta hai.

3. **Vector similarity search** = "is brief ke matlab ke sabse kareeb kaunse audience segments hain?"

**Real example:**
```
Brief: "Driving high awareness for online learning platforms in UK"
        ↓ embedding
3,400 audience segments me se sabse kareeb 10 nikle:
  1. Higher Education Seekers        (94% match)
  2. E-Learning & Tech Enthusiasts   (91% match)
  3. General Career Advancement      (78% match)
  ...
```

**Why?** Keyword search se ye nahi hota. "online learning" keyword `Higher Education Seekers` me nahi hai — par **matlab** wahi hai. Embedding matlab pakadta hai, keyword nahi.

**Purpose:** 3,400 segments me se automatic sahi wale nikalna, bina insaan ke browse kiye.

### **ISO Code**
International standard ke codes.
- **ISO country code (2-letter):** `GB` (UK), `US`, `DE` (Germany), `FR` (France)
- **ISO currency code:** `GBP`, `USD`, `EUR`
- **ISO date:** `YYYY-MM-DD` → `2026-08-01`

**Why?** Har jagah ek hi format. `"UK"`, `"United Kingdom"`, `"Britain"` — teeno ek cheez, par computer confuse hoga. Isliye sirf `GB`.

> **⚠ Chhota interesting point:** UK ka ISO code `GB` hai, `UK` nahi. Isliye document me har jagah `markets: ["GB"]` hai.

### **`bounds: "[)"`** — Interval Notation
Ye ganit ka notation hai. Document me `flight_dates` me aata hai.

```
[  =  ye din SHAMIL hai (inclusive)
)  =  ye din SHAMIL NAHI hai (exclusive)

"[)"  matlab: lower din shamil, upper din shamil nahi
```

**Real example:**
```
lower = "2026-08-01", upper = "2026-08-31", bounds = "[)"
→ Campaign 1 August se 30 August tak chalega
→ 31 August SHAMIL NAHI hai
```

**Why zaroori?** Ek din ka farak = ek din ka budget. Trader sochta hai 31 din, actually 30 din. **Ye ek confusion ka point hai — David ne yahan comment kiya ho sakta hai.**

### **Hallucination**
**Plain:** AI ka **jhooth bolna / cheezein bana dena** jo asal me nahi hain.

**Real example:**
```
Trader: "Netflix par mera reach kitna hoga?"
❌ Hallucinating agent: "Approximately 180,000 people."   ← ye number BANA LIYA
✅ Honest agent: "Netflix ke liye reach data available nahi hai.
                  Main CPM aur impressions bata sakta hun: 333,333 impressions."
```

**Ye document ka #1 principle hai.** Detail Part 3 me.

### **SSOT — Single Source of Truth**
**Plain:** **ek hi jagah** jahan sach likha hai.

v1.1.0 kehta hai: *"This document serves as the Single Source of Truth (SSOT) for the Strategy Module."*

**Why?** Agar 3 jagah likha hai aur teeno alag hain, to koi nahi jaanta sach kya hai. Ek jagah rakho, sab wahi dekhein.

### **Config-driven vs Hard-coded**
Document page 12, client ka critical note:
> *"This targeting list frequently changes so it should be easy to add new targeting types."* — the implementation must be **config-driven, not hard-coded**.

| | Matlab | Naya add karne me |
|---|---|---|
| **Hard-coded** | Code me seedha likha hua | Code badlo → test karo → deploy karo (**din lagenge**) |
| **Config-driven** | Ek config file/DB table me likha hua | Ek line add karo (**minute lagega**) |

**Real example:**
```python
# ❌ HARD-CODED
class Targeting(BaseModel):
    locations: list[str]
    device_types: list[str]
    # "language" add karna hai? → code badlo, deploy karo

# ✅ CONFIG-DRIVEN
TARGETING_TYPES = load_from_config()   # config file/DB se aaya
# "language" add karna hai? → config me ek line
```

**Purpose:** Client ne saaf kaha targeting list **badalti rehti hai**. Har baar deploy karna bewakoofi hai.

---

# PART 2 — Document ka Maksad (What / Why / Purpose)

## 2.1 WHAT — Ye document kya hai?

Ek **contract** hai. Teen cheezein ek jagah:

1. **Business rules** — CTV ad kharidne ke asli niyam (paisa, deals, tracking)
2. **Data shape** — kaunse fields hain, kaunse required, kaunse optional
3. **Flow** — kaam kis kram me hoga, kahan rukna hai, kahan loop hai

## 2.2 WHY — Ye document kyun banaya?

**Kyunki 5 log ek hi cheez bana rahe hain aur unhe ek hi samajh chahiye.**

Socho ye document na ho:
```
Kareem sochta hai:   audience Step 4 par aayegi
Wajahat sochta hai:  audience Step 2 par aayegi
Basil banata hai:    audience ka UI Step 6 par
Riddhi banati hai:   audience optional hai
Vishal registry me:  audience mandatory hai

→ Teen hafte ka kaam, sab bekaar. Sab ne apna-apna soch liya.
```

**Isliye SSOT.** Ek jagah likho, sab wahi padhein.

## 2.3 PURPOSE — Ye document kya haasil karta hai?

| Purpose | Kaise |
|---|---|
| **Client verification** | Client dekh kar bole "haan, humne yahi kaha tha" |
| **Diff dikhana** | ✅🔄➕❌ se saaf pata chale kya badla |
| **Ambiguity nikalna** | ⚠ Open Questions se pata chale kahan clarity nahi hai |
| **Build ka base** | Approve hone ke baad code isi se likha jaayega |
| **Scope lock karna** | Kya IN hai, kya OUT — clearly likha |

## 2.4 Revision kyun hui? (v1.1.0 → v2.0)

v1.1.0 me kuch bhi **galat** nahi tha. Par 3 baatein hui:

**1. Client ne CTV-first decide kiya**
v1.1.0 saare formats cover karta tha. Client ne kaha "pehle CTV karo." → Scope chhota karna pada.

**2. Client ne bahut naye requirements diye**
Inventory tiers, budget split, plan approval, credit check, activation — ye v1.1.0 me **the hi nahi**, kyunki client ne tab bataye nahi the.

**3. v1.1.0 UI wizard ke hisaab se tha, agent ke hisaab se nahi**
Ye sabse gehri baat hai. Detail Part 5 me — par short me:

```
UI Wizard ki soch:  "6 page hain, ek-ek bharo"       (screen ka kram)
Agent ki soch:      "pehle ye jaanna zaroori hai,
                     phir ye, kyunki isse ye nikalta hai"  (logic ka kram)
```

Ye do kram **alag** hain. Aur agent banane ke liye **logic ka kram** chahiye.

---

# PART 3 — SECTION 1: Core Principles
### ✅ Teeno UNCHANGED — Kareem ne jo likha, wahi

Document Section 1 kehta hai: *"✅ UNCHANGED — all three kept exactly as written."*

Ye tumhari jeet hai. Teen principles jo tumne v1.1.0 me likhe, wo v2.0 me **bilkul jaise the waise** rakhe gaye. Kyunki wo sahi the.

---

## Principle 1: Zero-Hallucination Policy

**Document literally:**
> *"The agent NEVER invents strategy parameters, metrics, targeting criteria, or deal IDs. It only populates values verified against the VOW database and REST APIs."*

### WHAT — kya kehta hai?
Agent kuch **bana nahi sakta**. Har value **VOW ke database ya API se verified** honi chahiye.

### WHY — kyun zaroori hai?
Kyunki **yahan asli paisa lagta hai.**

**Real example — agar ye principle na ho:**
```
Trader: "Netflix par UK me deal chahiye"
❌ Hallucinating agent: "Mil gaya — Deal ID EXT9K21847PQ, CPM £24.50"
                         ↑ Ye deal EXIST HI NAHI KARTI. LLM ne bana di.

Nateeja: Strategy create hui → Amazon DSP par bheji → FAIL
         Ya worse: galat deal par £10,000 chala gaya
```

**Aur ek example — metrics:**
```
Trader: "Netflix par reach kitna?"
❌ Hallucinating: "About 180,000 unique viewers"
                   ↑ Netflix reach data DETA HI NAHI. Ye number jhooth hai.

Trader ne is number par plan banaya → client ko promise kiya → deliver nahi hua
→ Trust khatam.
```

### PURPOSE — kya haasil hota hai?
**Trust.** Aur ye trust hi product hai.

Aur v2.0 ne is principle ka ek **sabse zabardast extension** kiya — **Honesty Rule** (Step 6):

> ➕ *"For Netflix/Disney, the agent shows: rate-card CPM and derived impressions (budget ÷ CPM × 1,000). It explicitly states that reach is unavailable and why. **Never invent a reach number.**"*

**Ye Zero-Hallucination ka hi CTV version hai.** "Nahi pata" kehna galat number dene se **behtar** hai.

### 💡 Isse kaise implement karte ho?
1. Har value ke liye pehle API call karo, phir slot bharo
2. Kabhi LLM se ID/number generate na karao
3. Jo data nahi hai, uske liye field me `None` rakho aur user ko batao

---

## Principle 2: Self-Filling Form Paradigm

**Document literally:**
> *"The agent operates as a stateful slot-filling engine backed by LangGraph. Inputs via chat or uploaded briefs are parsed into registered Pydantic slot schemas."*

**Paradigm** = soch ka tarika / model.

### Line ko tod kar samjho

| Hissa | Matlab |
|---|---|
| **stateful** | Yaad rakhne wala — pichhli baat bhoolta nahi |
| **slot-filling** | Form ke khaane bharne wala |
| **engine** | Chalta hua system |
| **backed by LangGraph** | LangGraph library se bana hua |
| **Inputs via chat or uploaded briefs** | Do raaste: chat, ya document upload |
| **parsed into** | Todkar nikala jaata hai |
| **registered Pydantic slot schemas** | Pehle se define kiye hue validated khaano me |

**Registered** = pehle se system me daale hue (Vishal ka "registry" kaam yahi hai).

### WHAT — poori line ka matlab?
Ek aisa system jo **baat karte-karte form bharta hai, yaad rakhta hai, aur har value jaanchta hai.**

### WHY?
Purana tarika: trader 6 page ka form bharta tha. Har page par 8 field, dropdown me 3,400 options. **20-30 minute.**

Naya tarika: trader ek paragraph likhta hai. **2 minute.**

### PURPOSE — Real example, poora:

```
─────────────────────────────────────────────────────────────
Trader: "I want a Prime Video awareness campaign in the UK
         for £10,000 running in August for my education
         website. 30 second creative."
─────────────────────────────────────────────────────────────

Agent peeche se (parsing):
  "Prime Video"        → formats = ["prime_video"]
  "awareness"          → goal = "AWARENESS"
  "UK"                 → markets = ["GB"], primary_currency = "GBP"
  "£10,000"            → market_budgets = [{market:"GB", budget:"10000.00"}]
  "August"             → flight_dates = {lower:"2026-08-01", upper:"2026-08-31"}
  "education website"  → product_location = "NOT_SOLD_ON_AMAZON"
                       → product_categories = [1]  (Education)
  "30 second"          → durations = ["30"]

Khaali khaane:
  strategy_name = ???
  kpi           = ???
  base_bid      = ???

─────────────────────────────────────────────────────────────
Agent: "Samajh gaya — UK me August 2026, £10,000, Prime Video,
        30-second, Awareness goal, education website (Amazon
        par nahi bechte).

        Do cheezein confirm karo:
        1. Strategy ka naam?
        2. KPI — reach ya frequency?"
─────────────────────────────────────────────────────────────
```

**Dhyan do:** Ek paragraph se **8 fields bhar gaye**. Aur agent ne jo samjha wo **dikhaya** — taaki trader galti pakad sake. (Ye v2.0 ka ➕ NEW *"Did I understand correctly?"* mechanism hai — Part 9 me.)

---

## Principle 3: API-Driven Tool Execution

**Document literally:**
> *"Every step maps to official VOW API endpoints."*

### WHAT?
Agent khud kuch nahi karta. Har kaam ke liye **VOW ka API call** karta hai.

**Tool** = agent ke haath me diya gaya ek kaam karne ka zariya (yahan = API call).

### WHY?
**Do wajah:**

**1. Zero-Hallucination ko technically enforce karna.**
Agar agent sirf API se values le sakta hai, to wo **bana hi nahi sakta**. Principle 1 automatically lagu ho jaata hai.

**2. Business logic ek jagah rahe.**
Agar agent apna ganit karega aur VOW backend apna, dono alag ho jaayenge. Ek jagah rakho — VOW ke API me.

### PURPOSE — Real example:

```
❌ WRONG (agent apna kaam kar raha):
Agent: "Strategy name 'Summer_2026' unique hai" (LLM ne guess kiya)
→ Actually pehle se exist karti thi → create fail

✅ RIGHT (API-driven):
Agent → GET /api/strategies/check_strategy_name_uniqueness/?name=Summer_2026
     ← {"is_unique": false, "name": "Summer_2026"}
Agent: "Ye naam pehle se hai. 'Summer_2026_v2' rakh dun?"
```

### 💡 Ek exception jo document me hai
**Step 3 (Budget Split)** — document kehta hai *"No API call — this is agent-side logic."*

Yaani budget split ka ganit **agent khud** karta hai. Ye Principle 3 ka apwaad (exception) hai.

**Kyun theek hai?** Kyunki budget split koi **fact** nahi hai jo verify karna ho — wo ek **proposal** hai. Aur agent apna proposal saaf-saaf batata hai (*"I've split evenly by impressions, which weights spend toward the 30s"*), to hallucination ka khatra nahi.

> **⚠ Par David ne yahan comment kiya ho sakta hai:** "Agent-side logic Principle 3 ke khilaaf hai — isko API me kyun nahi rakha?" Ye ek valid question hai. Tumhara jawab: *"budget split ek recommendation hai, verified fact nahi. Aur agent apni method saaf batata hai. Par agar consistency chahiye to isko VOW API me move kar sakte hain."*

---

## 3.4 v1.1.0 ka Architecture Diagram — samjho

Tumhare v1.1.0 me ye diagram tha. v2.0 me diagram nahi hai, par soch wahi hai:

```
  +-----------------------------------------------------+
  |         USER INTERFACE / BRIEF INPUT                |   ← trader chat karta hai
  +-----------------------------------------------------+   ya brief upload karta hai
                        |
                        v
  +-----------------------------------------------------+
  |   LANGGRAPH PLANNING AGENT (STATE ENGINE)           |   ← TUMHARA KAAM
  |   - Stateful Slot Filling & Verification            |
  |   - Schema Validation via Pydantic                  |
  |   - Automated Natural Language Brief Extractor      |
  +-----------------------------------------------------+
                        |
                        v
  +-----------------------------------------------------+
  |         VOW REST API ENGINE / TOOLS                 |   ← APIs jo verify karte hain
  |   - Uniqueness & ASIN Validation                    |
  |   - Audience Vector Search & Suggestion             |
  |   - Reach & Frequency Forecasting                   |
  |   - Amazon DSP Campaign Entity Creation             |
  +-----------------------------------------------------+
                        |
                        v
  +-----------------------------------------------------+
  |      DATABASE & AMAZON DSP SYNC ENGINE              |   ← asli DSP par jaata hai
  +-----------------------------------------------------+
```

**4 layers, upar se neeche:**
1. **UI layer** — trader se input
2. **Agent layer** — tumhara dimaag (LangGraph)
3. **API layer** — verification aur execution
4. **Sync layer** — Amazon DSP par bhejna

**"Sync Engine"** = wo background process jo VOW ka data Amazon DSP par bhejta hai. Document page 19 kehta hai:
> *"After activation, VOW's outbound sync creates the Campaigns and Ad Groups on Amazon DSP."*

**Campaign / Ad Group** = Amazon DSP ke apne structure. VOW ki "Strategy" → Amazon par "Campaigns + Ad Groups" ban jaati hai.
**Outbound sync** = bahar bhejne wali process (VOW → Amazon).
**`is_syncing: true`** = "abhi bheja ja raha hai, ruko."

---

# PART 4 — SECTION 2: Business Logic

Ye section document ka **niyam-kaanoon** hai. Char sub-sections.

---

## 4.1 — Product Attribution & Selling Locations
### ✅ UNCHANGED

**Document literally:**
> *"On Amazon (ON_AMAZON) [Endemic]: ASINs required. Enables DPV, ATC, Purchase, ROAS tracking."*
> *"Off Amazon (NOT_SOLD_ON_AMAZON) [Non-Endemic]: ASINs optional (monitors halo sales). Ad tag conversions required for site event tracking."*

### Poora comparison table

| | **ON_AMAZON** (Endemic) | **NOT_SOLD_ON_AMAZON** (Non-Endemic) |
|---|---|---|
| **Kaun** | Amazon par bechta hai | Apni website/app par bechta hai |
| **ASIN** | ✅ **REQUIRED** | ⚪ **OPTIONAL** |
| **ASIN se kya milta hai** | DPV, ATC, Purchase, ROAS | **Halo sales** (Amazon par organic sale) |
| **Ad Tag** | Zaroori nahi | ✅ **REQUIRED** |
| **Tracking kaise** | Amazon ka apna data | Website par laga tag |

### WHY — ye fork kyun hai?

Kyunki **tracking ka raasta bilkul alag** hai.

**Case A — Nike (Amazon par bechta hai):**
```
Nike ka shoe Amazon par hai, ASIN = B08N5WRWNW
Ad chala → Rahul ne dekha → Rahul ne Amazon par shoe kharida
→ Amazon KHUD jaanta hai. ASIN se match kar leta hai.
→ ROAS, DPV, ATC — sab automatic.
```

**Case B — BrightPath (apni website par bechta hai):**
```
BrightPath ka course brightpath.co.uk par hai
Ad chala → Rahul ne dekha → Rahul brightpath.co.uk par gaya → enroll kiya
→ Amazon ko KUCH NAHI PATA. Wo BrightPath ki website nahi dekh sakta.
→ Isliye AD TAG chahiye — jo BrightPath ki website se Amazon ko batayega.
```

**Aur Case B me ASIN kyun optional rakha?**
```
Ho sakta hai BrightPath Amazon par bhi ek book bechta ho.
Ad Netflix par chala → Rahul ne dekha → Rahul Amazon gaya → book kharidi
→ Ye HALO SALE hai. ASIN diya to ye bhi track ho jaayega.
→ Isliye optional — "de do to bonus insight milega."
```

### PURPOSE
Trader ko sahi tracking mile, aur agent sahi sawaal poochhe. Agar agent `ON_AMAZON` case me ASIN na maange, poora ROAS reporting fail ho jaayega.

---

## 4.2 — Attribution Window
### ✅ UNCHANGED — 14-day post-view aur post-click

Pehle Part 1.H me detail me samjhaya. Short recap:

```
Din 0:  Rahul ne Prime Video par BrightPath ka ad dekha
Din 5:  Rahul ne BrightPath ki website par enroll kiya
        → ✅ Ad ko CREDIT milega (14 din ke andar hai)

Din 0:  Rahul ne ad dekha
Din 20: Rahul ne enroll kiya
        → ❌ Ad ko credit NAHI (14 din nikal gaye)
```

**WHY 14 din?** Ye Amazon DSP ka default hai. Bahut chhota window (1 din) = asli asar miss karoge. Bahut bada (90 din) = jo ad se nahi hua, uska bhi credit le loge.

> **⚠ Ek gap:** Document kehta hai "Default Window: 14-day" — par kya trader **badal** sakta hai? Document me kahin field nahi hai. `attribution_window` naam ka koi field schema me **nahi hai**. **David ne yahan comment kiya ho sakta hai.**

---

## 4.3 — Deal Types & 🔴 THE THREE INVENTORY TIERS
### 🔄 CHANGED — deal types same, par inventory tiers ➕ NEW

> **⚡ Ye document ka SABSE IMPORTANT hissa hai.**
> Document khud kehta hai: *"the primary fork in the CTV flow"* aur *"This classification drives most of the downstream branching."*
>
> **Fork** = raasta do/teen taraf batna. **Downstream branching** = aage ke saare faisle isse tay hote hain.

### Pehle: 3 Deal Types (✅ UNCHANGED — Part 1.E me detail me)

| Type | Price | Commitment | Can pause? |
|---|---|---|---|
| Programmatic Guaranteed (PG) | Fixed CPM, guaranteed volume | Full budget owed | ❌ No |
| Preferred Deals | Fixed CPM | None | ✅ Yes |
| Private Auctions | Floor CPM, competitive | None | ✅ Yes |

### Ab: ➕ 3 INVENTORY TIERS (bilkul naya)

Document literally:
> *"Every deal now carries an inventory tier. This classification drives most of the downstream branching — whether reach can be forecast, whether Amazon audiences apply, and whether the deal is selectable now."*

| Tier | Examples | Deals | Reach Forecast | Audiences |
|---|---|---|---|---|
| **1. AMAZON_OWNED** | Prime Video | Pre-curated, **selectable now** | ✅ **Available** | **Amazon audiences** |
| **2. THIRD_PARTY_PRECURATED** | Netflix, Hulu, others | Pre-curated, **selectable now** | ❌ **Not available** | **Their own targeting (adds CPM)** |
| **3. THIRD_PARTY_NEEDS_CURATION** | Disney+, others | **Rate-card CPM only; VOW curates the deal after the IO is signed** | ❌ **Not available** | Their own targeting (adds CPM) |

### Ek-ek tier ko kholo

#### **Tier 1: AMAZON_OWNED** — Prime Video

**Kya hai:** Amazon ka apna inventory.

**Kyun special:** Amazon ke paas apna data hai — kaun kya dekhta hai, kaun kya kharidta hai. Isliye:
- ✅ **Reach forecast** de sakta hai (Amazon ko pata hai kitne unique log hain)
- ✅ **Amazon audiences** lag sakti hain (3,400 segments)
- ✅ Deal **abhi select** kar sakte ho

**Real example:**
```
Deal: Prime Video | Preferred Deal | UK - 30 | £28.88 CPM
Audience: Higher Education Seekers (VCPM £1.85)
Budget: £6,000

Agent bata sakta hai:
  Effective CPM   = £28.88 + £1.85 = £30.73
  Impressions     = 6,000 ÷ 30.73 × 1000 = 195,249
  Unique reach    = 128,000        ← ✅ ASLI FORECAST
  Frequency       = 1.53           ← ✅ ASLI
  Reach curve     = ✅ chart bhi de sakta hai
```

#### **Tier 2: THIRD_PARTY_PRECURATED** — Netflix, Hulu

**Kya hai:** Doosri company ka inventory, par deal **pehle se ban chuki** hai (Amazon DSP me available hai).

**"Pre-curated"** = pehle se taiyar. Koi kaagaz sign nahi karna, abhi utha lo.

**Kya nahi mil sakta:**
- ❌ **Reach forecast** — Netflix apna viewer data Amazon ko **nahi deta**. Netflix ko pata hai uske kitne log hain, par wo batata nahi.
- ❌ **Amazon audiences** — Netflix apni targeting deta hai, jiska **extra CPM** lagta hai

**Real example:**
```
Deal: Netflix | Preferred | UK - 30 | £32.00 CPM
Budget: £3,000

Agent kya bata sakta hai:
  CPM          = £32.00           ← ✅ pata hai
  Impressions  = 3,000 ÷ 32 × 1000 = 93,750    ← ✅ ganit se nikala
  Unique reach = ❌ "AVAILABLE NAHI HAI"
  Frequency    = ❌ "AVAILABLE NAHI HAI"

Agent bolega: "Netflix ke liye main 93,750 impressions estimate kar
               sakta hun, par unique reach data Netflix share nahi
               karta. Isliye main reach number nahi de sakta."
```

**Yahi HONESTY RULE hai.**

#### **Tier 3: THIRD_PARTY_NEEDS_CURATION** — Disney+

**Kya hai:** Deal **exist hi nahi karti** abhi. Sirf rate card (daam ki list) hai.

Document literally: *"Rate-card CPM only; VOW curates the deal after the IO is signed"*

**Plain me:**
```
Trader: "Disney+ par ad chahiye"
Agent:  "Disney+ ke liye abhi deal ready nahi hai. Main tumse
         requirements le leta hun, VOW team IO sign hone ke baad
         deal banayegi.

         Batao:
         - Kaunse genres? (Required)
         - Kaunse durations? (Required)
         - Targeting preference? (Optional)
         - Kitna budget? (Required)
         - Flight dates? (Required)"
```

**"Curation"** = deal ko **haath se banana**.
**"IO signed"** = kaagaz sign hona.

**Purpose:** Deal ready na hone par bhi trader ka kaam ruke nahi. Agent requirements **capture** kar leta hai, taaki VOW team baad me deal bana sake. Ise document **"Curation Capture"** kehta hai.

### 🔴 WHY — Ye teen tiers itne important kyun?

Document ka jawab (page 3):
> *"a plan spanning Prime + Netflix + Disney has **three portions, each with different capabilities**. The agent must handle them differently — and be honest about what it can and cannot forecast."*

**Real example — ek plan, teen portions:**

```
╔═══════════════════════════════════════════════════════════════════╗
║  BrightPath Campaign — £10,000 total                              ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  PORTION 1: Prime Video (£6,000)         [AMAZON_OWNED]           ║
║  ✅ Deal select ho gayi                                            ║
║  ✅ Amazon audience laga di (Higher Education Seekers)             ║
║  ✅ Reach forecast: 128,000 unique log, frequency 1.53             ║
║  ✅ Reach curve chart bhi hai                                      ║
║  ✅ Audience chhoti nikli to REPAIR LOOP chal sakta hai            ║
║                                                                   ║
║  PORTION 2: Netflix (£3,000)             [3P_PRECURATED]          ║
║  ✅ Deal select ho gayi                                            ║
║  ❌ Amazon audience NAHI lag sakti — Netflix ki targeting (+CPM)   ║
║  ❌ Reach forecast NAHI — sirf 93,750 impressions bata sakte hain  ║
║  ❌ Repair loop NAHI chal sakta (kya repair karein? data nahi)     ║
║                                                                   ║
║  PORTION 3: Disney+ (£1,000)             [3P_NEEDS_CURATION]      ║
║  ❌ Deal EXIST NAHI KARTI — sirf rate card                         ║
║  ❌ Reach forecast NAHI                                            ║
║  📝 Requirements capture kiye: genres, durations, budget, dates   ║
║  ⏳ VOW team IO sign hone ke baad deal banayegi                     ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

⚠ AUR SABSE ZAROORI: Total reach ADD NAHI KAR SAKTE!
```

### ⚠ "Total reach cannot be summed" — ye kyun?

Document literally: *"Total reach cannot be summed across providers (no cross-platform deduplication)"*

**Deduplication (dedup)** = **duplicate hatana**.

**Plain example:**
```
Prime Video reach  = 128,000 log
Netflix reach      =  90,000 log (agar mil bhi jaata)
─────────────────────────────────
Total?  128,000 + 90,000 = 218,000?

❌ NAHI! Kyunki:
Rahul Prime Video BHI dekhta hai AUR Netflix BHI dekhta hai.
Wo dono me GINA jaayega = 2 baar.

Asli unique log ho sakte hain 180,000 — kyunki 38,000 log dono me hain.

Par ye kaise pata chalega? Iske liye Prime aur Netflix ko apna
viewer data compare karna padega — "kaun dono me hai?"
Wo NAHI karte. Isliye DEDUPLICATION possible nahi.
→ Isliye total reach nahi bata sakte.
```

**Cross-platform deduplication** = alag-alag platforms par same insaan ko ek hi baar ginna. Ye advertising industry ka ek **asli, unsolved problem** hai.

### PURPOSE — is tier system ka
1. **Honesty** — agent jhooth nahi bolta
2. **Correct branching** — kaunsa API call karna hai, kaunsa nahi
3. **Correct expectations** — trader ko pehle hi pata chal jaata hai kya milega
4. **Ek plan, teen behaviour** — same campaign ke teen hisson ko alag-alag handle karna

---

## 4.4 — Audience Set Profiles
### 🔄 CHANGED — "Broad" → "Wide", + fee consequence, + mandatory

### Naam ka change

| Profile | Was (v1.1.0) | Now (v2.0) |
|---|---|---|
| 1 | Narrow (High Precision) | **Narrow** — highly targeted, elevated intent, **higher audience fee, risk of underdelivery** |
| 2 | Balanced (Recommended) | **Balanced** — optimal blend, the usual recommendation |
| 3 | **Broad** (Maximum Scale) | **Wide** — broad demographic/interest reach, **lower fee**, less precision |

**Dhyan do — v2.0 ne sirf naam nahi badla, "consequence" (natija) bhi joda:**
- Narrow → **higher fee + underdelivery risk**
- Wide → **lower fee**

**WHY?** Kyunki v1.1.0 me sirf likha tha "Narrow = high precision" — jo sunne me **accha** lagta hai. Par asal me Narrow **do tarah se bura** hai (chhoti + mehngi). v2.0 ne ye trade-off saaf likha.

### ➕ NEW: VCPM stacking (Part 1.C me detail me)

```
Deal CPM £28.88 + Audience VCPM £1.63 = Effective CPM £30.51
```

### ➕ NEW: Mandatory + Suggestion-driven

| | v1.1.0 | v2.0 |
|---|---|---|
| Audience | **Optional** | ✅ **MANDATORY** |
| Kaise chuni jaati | Browse/search karke | **Agent suggest karta hai** (pgvector) |

### ❌ REMOVED: Product audiences
CTV ke liye applicable nahi.

### ⚪ CONDITIONAL: AMC audiences
Sirf jab advertiser ka **purana campaign data** ho (retargeting).

---

# PART 5 — SECTION 3: THE 13-STEP AGENTIC FLOW
### 🔄 CHANGED — entirely reordered

> **Ye document ka DIL hai.** Poora document isi flow ke hisaab se likha gaya hai.

---

## 5.0 — Pehle: Kram kyun badla? (Sabse gehri baat)

Document literally:
> *"🔄 CHANGED — entirely reordered. The original followed the 6-step UI wizard. This follows the client-confirmed CTV-first agentic flow (v5)."*

### Do tarah ki soch

```
╔════════════════════════════════╦════════════════════════════════════╗
║   UI WIZARD KI SOCH            ║   AGENT KI SOCH                    ║
╠════════════════════════════════╬════════════════════════════════════╣
║ "6 screen hain, ek-ek bharo"   ║ "Pehle ye jaanna ZAROORI hai,     ║
║                                ║  kyunki isse ye NIKALTA hai"       ║
║                                ║                                    ║
║ Kram = SCREEN ka kram          ║ Kram = DEPENDENCY ka kram          ║
║ (jo dikhne me accha lage)      ║ (jo logically zaroori ho)          ║
╚════════════════════════════════╩════════════════════════════════════╝
```

**Real example — kram kyun matter karta hai:**

```
❌ v1.1.0 ka kram: Audiences (Step 4) ... Deals (Step 3)
   Ruko — deals PEHLE the, audiences BAAD me. Theek hai.
   Par v1.1.0 me Deals ke andar "inventory tier" ka concept HI NAHI THA.

✅ v2.0 ka kram: Inventory tier PEHLE (Step 2), phir audiences (Step 4)

KYUN? Kyunki:
  Agar inventory = Prime Video (AMAZON_OWNED)
     → Amazon audiences suggest karo (3,400 segments)
  Agar inventory = Netflix (3P)
     → Amazon audiences BEKAAR hain! Netflix apni targeting deta hai
     → Alag sawaal poochhne padenge

To audience suggest karne SE PEHLE inventory pata hona ZAROORI hai.
Warna agent galat cheez suggest karega.
```

**Yahi "dependency" hai.** A ke bina B nahi ho sakta → A pehle.

### Poora Old vs New Comparison (document se, literally)

| **Old (v1.1.0 wizard)** | **New (v2.0 agentic, confirmed)** |
|---|---|
| 1. Strategy details | **1. Basics (+ durations)** |
| 2. Goal, KPI & bid | *(goal/KPI/bid folded into Basics)* |
| 3. Deals | **2. CTV inventory (three-tier fork)** |
| — | **3. Budget split** ➕ NEW |
| 4. Audiences | **4. Audiences (mandatory, suggestion-driven)** |
| — | **5. Targeting** ➕ NEW |
| *(forecast was a sub-step)* | **6. Predict reach (Amazon only; repair loop)** |
| — | **7. Plan approval** ➕ NEW |
| *(create was at the end)* | **8. Create the real strategy** |
| 5. Creatives | **9. Upload video creative (+ duration check)** |
| — | **10. Platform creative approval** ➕ NEW |
| *(ASINs were in step 1)* | **11. Tracking setup (ASINs + ad tag)** 🔄 MOVED |
| — | **12. Credit check** ➕ NEW |
| 6. Summary → create | **13. Activate** ➕ NEW |

### 🔴 3 Bade Structural Changes (ye yaad rakhna)

**1. 6 steps → 13 steps**
Kyunki UI wizard ke ek page me kai kaam chhupe hue the. Agent ke liye unhe alag karna pada.

**2. "Create" beech me aa gaya (Step 8), aakhir me nahi**
v1.1.0 me: sab bharo → create → khatam
v2.0 me: plan banao → **APPROVE karao** → create → creative upload → creative approve → tracking → credit → **activate**

**WHY?** Kyunki "create" aur "activate" **do alag cheezein** hain. Create = database me record banana (free). Activate = **paisa kharch shuru** karna.

**3. Approval gates aa gaye (Step 7 aur Step 10)**
Do jagah insaan ka **approval** chahiye. Pehle koi approval nahi tha.

### 💡 Sabse zaroori concept: "Costless plan" vs "Spend action"

Document page 18-19, literally:
> *"Credit is checked only at activation, not during planning. **Everything before this point is a costless plan.**"*
> *"Step 13: Activate — **The single spend action in the entire flow. Everything before this was free.**"*

```
╔══════════════════════════════════════════════════════════════════╗
║  STEPS 1 – 12:  FREE. Kuch paisa nahi lagta.                    ║
║                 Sirf plan ban raha hai. Jitni baar chaho         ║
║                 badlo, cancel karo — kuch nahi hoga.             ║
╠══════════════════════════════════════════════════════════════════╣
║  STEP 13:       💰 PAISA. Yahi ek jagah kharch shuru hota hai.  ║
╚══════════════════════════════════════════════════════════════════╝
```

**WHY ye design brilliant hai:**
- Trader bina dar ke experiment kar sakta hai
- Manager ko approve karne ka mauka **paisa lagne se pehle** milta hai
- Galti pakadne ke 12 mauke hain

---

## 🟦 STEP 1: BASICS
### 🔄 CHANGED — v1.1.0 ke Step 1 + Step 2 ko **merge** kiya, durations joda, CTV me scope kiya

### WHAT — is step me kya hota hai?
Trader se **buniyadi jaankari** lena — naam, tareekh, market, currency, duration, goal, KPI, budget, bid.

### WHY — do steps ko merge kyun kiya?
Kyunki chat me ye **ek hi saans me** aa jaata hai:

```
Trader: "UK me August me £10,000 ka Prime Video awareness campaign,
         30-second, reach KPI"
         ↑        ↑         ↑        ↑                    ↑        ↑
       market   dates    budget   format+goal        duration   KPI

v1.1.0 me ye 2 screens the. Chat me ye 1 sentence hai.
→ Isliye merge kar diya.
```

### 📋 POORA FIELD MATRIX — har field ka matlab

#### 1. **Strategy name**
| | |
|---|---|
| **Type** | String (text) |
| **Requirement** | **Required** |
| **Change** | ✅ Unchanged |
| **Validation** | `GET /api/strategies/check_strategy_name_uniqueness/` |

**Kya define karti hai:** Is campaign ka **naam** — jisse trader baad me dhoondhega.

**WHY unique hona zaroori?** Agar 2 strategies ka same naam ho, reporting me confusion. "Summer_2026 ka performance kya hai?" — kaunsa Summer_2026?

**Real example:**
```
Trader: "naam Summer_Brand_Awareness_2026 rakho"
Agent → GET /api/strategies/check_strategy_name_uniqueness/?name=Summer_Brand_Awareness_2026
     ← {"is_unique": true, "name": "Summer_Brand_Awareness_2026"}
Agent: ✅ theek hai

--- ya agar duplicate ho ---
     ← {"is_unique": false}
Agent: "Ye naam pehle se hai. 'Summer_Brand_Awareness_2026_v2' rakh dun?"
```

**Naming convention (best practice):** `Season_Objective_Year` → `Summer_Brand_Awareness_2026`. Isse dhoondhna aasan.

---

#### 2. **Flight dates**
| | |
|---|---|
| **Type** | Date range |
| **Requirement** | **Required** |
| **Change** | ✅ Unchanged |
| **Validation** | `lower ≥ today`, `upper > lower` |

**"Flight"** = advertising ki bhasha me **campaign ka chalne ka time**. (Hawai jahaz se koi lena-dena nahi — "ad ki udaan".)

**Kya define karti hai:** Campaign **kab se kab tak** chalega.

**Do rules:**
- `lower ≥ today` — **shuru aaj ya aage** ho. Peeche nahi (guzri tareekh me ad nahi chala sakte)
- `upper > lower` — **khatam shuru ke baad** ho

**Real example:**
```json
{
  "lower": "2026-08-01",
  "upper": "2026-08-31",
  "bounds": "[)"
}
```

**`bounds: "[)"` ka matlab (Part 1.J me detail me):**
```
[ = lower SHAMIL hai      → 1 August shamil
) = upper SHAMIL NAHI hai → 31 August SHAMIL NAHI
→ Campaign 1 Aug se 30 Aug = 30 din
```

**WHY zaroori:** 30 vs 31 din = ek din ka budget ka farak. Aur agar trader sochta hai 31 din, wo galat calculate karega.

**Aur ek WHY:** flight dates se **daily budget** nikalta hai:
```
£10,000 ÷ 30 din = £333/din
```

---

#### 3. **Target markets**
| | |
|---|---|
| **Type** | Multi-select |
| **Requirement** | **Required** |
| **Change** | ✅ Unchanged |
| **Format** | ISO 2-letter country codes: `GB`, `US`, `DE` |

**Kya define karti hai:** **Kis desh** me ad chalega.

**Multi-select** = ek se zyada chun sakte ho.

**WHY ISO code?** Part 1.J me — ek hi format sab jagah. `"UK"`, `"United Kingdom"`, `"Britain"` — teeno ek cheez, par computer confuse hoga.

**⚠ UK ka code `GB` hai, `UK` nahi.**

**WHY market itna important?** Kyunki market se **bahut kuch depend** karta hai:
```
market = GB  →  deals GB ke  →  audiences GB ki  →  currency GBP
              →  product categories GB ki  →  rate card GB ka
              →  creatives GB me approved hone chahiye
```

Document v1.1.0 me literally: *"Triggers asset, audience, and creative pre-checks."*

**Real example — multi-market:**
```
markets = ["GB", "FR"]
→ Ab budget DONO market me baantna padega
→ market_budgets = [
     {market: "GB", budget: "6000.00", base_bid: "30.00"},
     {market: "FR", budget: "4000.00", base_bid: "28.00"}
   ]
→ Deals dono market ke liye alag
→ Creatives dono language me chahiye ho sakte hain
```

---

#### 4. **Primary currency**
| | |
|---|---|
| **Type** | Dropdown |
| **Requirement** | **Required** |
| **Change** | ✅ Unchanged |
| **Choices** | `EUR`, `GBP`, `USD` |

**Kya define karti hai:** **Reporting** kis currency me dikhegi.

**"Primary"** kyun? Kyunki multi-market campaign me kai currency ho sakti hain (GB = GBP, FR = EUR). "Primary" = **main reporting currency** jisme sab jodkar dikhaya jaayega.

**Real example:**
```
markets = ["GB", "FR"]
GB me kharch: £6,000
FR me kharch: €4,700
primary_currency = "GBP"
→ Report me: Total £10,000 (€4,700 ko GBP me convert kiya)
```

**WHY sirf 3 currency?** Kyunki abhi VOW in 3 markets me kaam karta hai. Aur zaroorat pade to enum me add ho jaayega.

---

#### 5. **➕ Creative durations** — NEW FIELD
| | |
|---|---|
| **Type** | Multi-select |
| **Requirement** | **Required** |
| **Change** | ➕ **NEW** |
| **Values** | `10`, `15`, `20`, `30` (seconds) |

**Document literally:** *"Determines which deals are available and what CPM applies"*

**Kya define karti hai:** Video **kitne second** ka hoga.

### 🔴 WHY ye field Step 1 me hai (bahut important)

Kyunki duration ke **bina deals filter hi nahi ho sakte.**

```
Duration pata nahi
   ↓
Kaunse deals available hain? PATA NAHI
   ↓
CPM kya hai? PATA NAHI
   ↓
Impressions kitne? PATA NAHI
   ↓
Poora plan ATKA HUA
```

**Real example — duration ka asar:**
```
Budget £10,000

Duration 15s → available deals: Prime 15s @ £20, Netflix 15s @ £24
             → Prime chuna: 10,000 ÷ 20 × 1000 = 500,000 impressions

Duration 30s → available deals: Prime 30s @ £28.88, Netflix 30s @ £32
             → Prime chuna: 10,000 ÷ 28.88 × 1000 = 346,260 impressions

FARAK: 153,740 impressions! Sirf duration badalne se.
```

**PURPOSE:** Duration pehle poochho, warna baad me poora plan dobara banana padega. (Aur exactly yahi Step 9 ka "duration match check" rokta hai.)

**Multi-select kyun?** Kyunki trader do duration chala sakta hai — 15s aur 30s dono. Phir budget dono me baantna padega (**Step 3 = Budget Split**).

---

#### 6. **Goal**
| | |
|---|---|
| **Type** | **Fixed** (pehle "Card Select" tha) |
| **Requirement** | **Required** |
| **Change** | 🔄 **CHANGED** |
| **Value** | CTV ke liye **hamesha `AWARENESS`** |

**Client ka quote (document me literally):**
> *"CTV is typically used as an Awareness goal as it's hard to track anything further down the funnel"*

**Kya define karti hai:** Campaign ka **maksad** kya hai.

**WHY fixed?** Part 1.D me detail me. Short: TV se click/purchase track karna mushkil hai.

**Real example:**
```
❌ Trader: "Mujhe CTV se conversions chahiye"
   Agent: "CTV pe conversion track karna reliable nahi hai —
           TV se click nahi hota. CTV Awareness ke liye best hai.
           Agar conversions chahiye to Display/Search behtar hai,
           par wo abhi is module ke scope me nahi hai."
```

**⚠ "Fixed" ka type kya hai?** Document ne `Type = Fixed` likha hai. Par Pydantic model me `goal: GoalEnum = Field(GoalEnum.AWARENESS)` hai — yaani **default** AWARENESS hai, par **enum me teeno values maujood** hain.

> **Ye ek design question hai:** "Fixed" ka matlab kya — trader badal sakta hai ya nahi? Enum me CONSIDERATION aur CONVERSION abhi bhi hain (comment `# future scope` ke saath). **David ne yahan comment kiya ho sakta hai.**

---

#### 7. **KPI**
| | |
|---|---|
| **Type** | Select |
| **Requirement** | **Required** |
| **Change** | 🔄 **CHANGED** — 6 choices se 2 |
| **Choices** | CTV ke liye sirf `reach` ya `frequency` |

**Kya define karti hai:** Success **kis number se naapa** jaayega — aur isse agent ka behaviour badal jaata hai.

**Real example — KPI se agent ka faisla badalta hai:**
```
KPI = reach
→ Agent WIDE audience suggest karega (zyada log)
→ Agent frequency cap lagane ki salah dega (taaki ek banda
   baar-baar na dekhe aur budget zyada logon me faile)

KPI = frequency
→ Agent NARROW/BALANCED audience suggest karega (kam log, baar-baar)
→ Frequency cap ki zaroorat nahi
```

**Hataye gaye 4 KPI:** `ctr`, `cpc`, `cpa`, `cpdpv` — sab click/purchase naapte hain, CTV me kaam ke nahi (Part 1.D me detail me).

---

#### 8. **Formats**
| | |
|---|---|
| **Type** | **Fixed** |
| **Requirement** | **Required** |
| **Change** | 🔄 **CHANGED** |
| **Values (M1)** | Sirf `streaming_tv` aur `prime_video` |

**Kya define karti hai:** Ad **kis tarah** ka hoga / kahan chalega.

**Removed:** `display`, `online_video` — **future scope**.

**WHY?** Part 1.B me. Short: CTV ke rules Display se bilkul alag hain.

---

#### 9. **Product categories**
| | |
|---|---|
| **Type** | Multi-select |
| **Requirement** | **Required for video** |
| **Change** | ✅ Unchanged |
| **API** | `GET /api/contextual-targeting/{market}/product-categories/` |

**Kya define karti hai:** Advertiser ka product **kis category** ka hai. Example: `Education (1)`, `Electronics`, `Food & Beverage`.

**Dhyan do:** ID **number** hai, naam nahi → `product_categories: [1]` (`list[int]`)

**WHY "required for video"?**
Do wajah:
1. **Contextual targeting** — ad ko **matching content** ke saath dikhana. Education ka ad documentary ke saath, na ki horror movie ke saath.
2. **Brand safety** — video me content ke saath ad dikhta hai. Galat content ke saath brand ki izzat kharab ho sakti hai.

**Contextual targeting** = content ke hisaab se ad dikhana (banda kaun hai, uske hisaab se nahi).

**Real example:**
```
Advertiser: BrightPath (online courses)
product_categories = [1]  (Education)

→ Ad educational/documentary content ke saath dikhega
→ Aur audience suggestion me bhi ye input jaata hai:
   POST /api/audience-sets/suggest/ me "product_categories": ["Education"]
```

**WHY market-specific API?** Kyunki har desh me categories alag ho sakti hain. UK me "Further Education" hai, US me "Community College".

---

#### 10. **Selling location**
| | |
|---|---|
| **Type** | Radio (ek hi chun sakte ho) |
| **Requirement** | **Required** |
| **Change** | ✅ Unchanged |
| **Values** | `ON_AMAZON` ya `NOT_SOLD_ON_AMAZON` |

**Kya define karti hai:** Advertiser **kahan bechta** hai — aur isse **tracking ka poora raasta** tay hota hai (Part 4.1 me detail me).

**Real example:**
```
BrightPath = education website, Amazon par nahi bechta
→ product_location = "NOT_SOLD_ON_AMAZON"
→ Isliye Step 11 me AD TAG check hoga
→ ASIN optional rahegi
```

---

#### 11. **Product ASINs**
| | |
|---|---|
| **Type** | Textarea |
| **Requirement** | **Conditional** |
| **Change** | 🔄 **MOVED** |
| **Rule** | `ON_AMAZON` → Required; `NOT_SOLD_ON_AMAZON` → Optional |
| **Validation** | `POST /api/contextual-targeting/{market}/asin-validation/` |

**Document literally:** *"Still required if ON_AMAZON, but the validation and collection now happens at Step 11 (tracking setup)."*

**Textarea** = bada text box (kai ASINs comma se alag karke daal sakte ho).

**Real example:**
```
Input: B08N5WRWNW, B09B3H5F2C
→ POST /api/contextual-targeting/GB/asin-validation/
   {"asins": ["B08N5WRWNW", "B09B3H5F2C"]}
← {
    "valid_asins": [{
      "asin": "B08N5WRWNW",
      "title": "Wireless Noise Cancelling Headphones",
      "brand": "AudioBrand",
      "image_url": "https://...",
      "product_category": "Electronics"
    }],
    "invalid_asins": ["B09B3H5F2C"]
  }
Agent: "B08N5WRWNW ✅ mil gaya — Wireless Noise Cancelling Headphones.
        B09B3H5F2C ❌ nahi mila. Check karke dobara bhejo?"
```

**WHY validation zaroori?** Kyunki galat ASIN ka matlab **tracking fail**. Aur trader ko tab pata chalega jab campaign khatam ho jaayega — bahut late.

### ⚠⚠ YAHAN DOCUMENT KA SABSE BADA OPEN QUESTION HAI

**Document literally (page 8):**
> *"⚠ Open question: `product_location` and `asin_numbers` are fields in the `POST /strategies/` payload called at Step 8. If ASINs are collected at Step 11 (after Step 8), they'd need to be patched onto the strategy afterwards. Alternatively, the ASIN question stays early (it's a plan field) and only the ad-tag check moves late. Confirm with client."*

**Plain me problem:**

```
Step 8:  POST /api/strategies/  ← ye call ASIN maangta hai
Step 11: ASIN collect karte hain ← par ye Step 8 KE BAAD hai!

→ TIMING CONFLICT. Jo cheez Step 8 me chahiye, wo Step 11 me mil rahi hai.
```

**Do possible solutions (document ne dono likhe):**

| Option | Kaise | Nuksaan |
|---|---|---|
| **A: Patch baad me** | Step 8 me strategy bina ASIN banao, Step 11 me `PATCH` karke ASIN chipkao | Ek extra API call. Aur beech me strategy **adhoori** rehti hai |
| **B: ASIN wapas Step 1 me** | ASIN Step 1 me hi poochho (kyunki wo "plan field" hai), sirf **ad-tag check** Step 11 me rakho | Trader se ASIN pehle poochhna padega (chat me thoda awkward) |

**PATCH** = HTTP method jo **mojood cheez ka ek hissa** update karta hai.

**Mera vichaar:** **Option B behtar hai.** Kyunki:
1. `product_location` ek **plan-level decision** hai (Amazon par bechta hai ya nahi) — ye planning ka hissa hai, tracking ka nahi
2. ASIN se **product category** bhi nikalti hai (validation response me `product_category` aata hai!) — jo Step 1 me chahiye
3. Ek call se kaam ho jaayega, patch ki zaroorat nahi

**Aur Step 11 me sirf ye rahe:** ad tag registered hai ya nahi + conversions choose karna. Wo genuinely "tracking setup" hai.

> 🎯 **Ye ⚠ document me DO BAAR aaya hai** (page 8 aur page 18). **David ne is par pakka comment kiya hoga.** Ye tumhara sabse tayyar jawab hona chahiye.

---

#### 12. **➕ Frequency cap** — NEW
| | |
|---|---|
| **Type** | Number |
| **Requirement** | **Optional** |
| **Change** | ➕ **NEW** — client confirmed optional |

**Kya define karti hai:** Ek banda **maximum kitni baar** ad dekhega.

**Real example:**
```
frequency_cap = 3 (per week)
→ Rahul ko hafte me maximum 3 baar ad dikhega
→ Chautha impression Rahul ko NAHI jaayega, kisi naye bande ko jaayega
```

**WHY zaroori?**
1. **Ad fatigue** — same ad 15 baar dekh kar banda **chidh** jaata hai. Brand ko **nuksaan** hota hai.
2. **Budget efficiency** — kam logon par paisa barbaad nahi hota, zyada logon tak pahunchta hai

**Reach KPI ke saath frequency cap best combo hai:**
```
KPI = reach + frequency_cap = 3
→ "Zyada se zyada log, par koi 3 baar se zyada na dekhe"
→ Budget faila, wastage rukа
```

**⚠ Note:** Pydantic model me comment hai `"Optional weekly cap"` — yaani **weekly**. Par document ke field table me sirf "Number" likha hai, unit nahi. **Ye ambiguity hai — daily ya weekly ya lifetime? David ne comment kiya ho sakta hai.**

---

#### 13. **➕ Budget cap** — NEW
| | |
|---|---|
| **Type** | Number |
| **Requirement** | **Optional** |
| **Change** | ➕ **NEW** — client confirmed optional |

**Kya define karti hai:** Kharch ki **upar ki limit**.

**⚠ Confusing point:** `market_budgets` me pehle se budget hai. To `budget_cap` alag kyun?

**Possible matlab:**
```
market_budgets = £10,000 (poore month ka)
budget_cap     = £500 (daily cap?)
→ "Poore month £10,000, par ek din me £500 se zyada mat kharch karo"
→ Isse "pacing" control hota hai
```

**Pacing** = kharch ka rate — paisa dheere-dheere kharch ho ya jaldi.

**WHY zaroori?** Bina cap ke poora budget pehle 3 din me kharch ho sakta hai (agar inventory sasti mil gayi) — phir baaki 27 din ad nahi chalega.

> **⚠ Document ne ye clear nahi kiya ki `budget_cap` daily hai ya lifetime, aur `market_budgets` se kaise alag hai. David ne yahan comment kiya ho sakta hai.**

---

#### 14. **Market budgets** aur **Base bids**
| Field | Type | Req | Change |
|---|---|---|---|
| **Market budgets** | Table | Required | ✅ Unchanged — per-market budget, **must be > 0** |
| **Base bids** | Table | Required | ✅ Unchanged — per-market base CPM bid |

**Table kyun?** Kyunki **har market ka apna** budget aur bid hota hai.

**Real example:**
```json
"market_budgets": [
  {"market": "GB", "budget": "10000.00", "base_bid": "30.00"}
]

--- multi-market ---
"market_budgets": [
  {"market": "GB", "budget": "6000.00", "base_bid": "30.00"},
  {"market": "FR", "budget": "4000.00", "base_bid": "26.00"}
]
```

### **Base bid** — ye kya hai? (Confusion point)

**Base bid** = **maximum CPM jo tum dene ko taiyar ho.**

```
base_bid = £30
→ "Main ek impression ke liye maximum £0.03 (£30/1000) dunga"
→ Auction me isse zyada bid nahi lagegi
```

**Budget vs Base bid ka farak:**

| | Budget | Base Bid |
|---|---|---|
| **Kya hai** | Total kitna paisa | Per-1000-impression max daam |
| **Example** | £10,000 | £30 |
| **Analogy** | "Mere paas £10,000 hai" | "Main ek kg tamatar £30 se zyada nahi dunga" |

**Kyun dono chahiye?**
```
Sirf budget: £10,000 — par agent £100 CPM par bhi kharid dega
             → sirf 100,000 impressions milenge (bahut mehnga)

Budget + Base bid: £10,000, max £30 CPM
             → agent £30 se upar nahi jaayega
             → kam se kam 333,333 impressions guarantee
```

**Aur Step 6 ke repair loop me base bid **badhaya** jaata hai:**
> *"Adjust base CPM bid up to market recommended floor (e.g. increase from £15 to £30 for Prime Video)"*

**Kyun?** Kyunki agar base bid bahut kam hai (£15), aur Prime Video ka floor £28 hai, to **koi impression hi nahi milega** — auction har baar haar jaayega. Isliye bid badhana padta hai.

**"must be > 0"** — zero budget/bid ka matlab campaign chalega hi nahi.

---

### 🔧 Step 1 ke API calls
```
GET /api/strategies/check_strategy_name_uniqueness/
GET /api/contextual-targeting/{market}/product-categories/
```

### ❌ Step 1 se REMOVED
| Kya hataya | Kahan gaya | Kyun |
|---|---|---|
| **Ad tag conversions** | 🔄 Step 11 | Wo tracking ka kaam hai, planning ka nahi |
| **Display, Online Video formats** | ❌ Future scope | CTV scope |
| **4 non-awareness KPIs** (CTR, CPC, CPA, CPDPV) | ❌ Future scope | CTV me click nahi hota |

---

## 🟦 STEP 2: CTV INVENTORY — The Tier Fork
### 🔄 CHANGED — v1.1.0 ka Step 3 "Deals" tha. Ab audiences se **pehle** aata hai, aur 3-tier fork laata hai.

### WHAT?
Trader se poochhna: **kaunse platform par ad chalana hai** — aur unhe **tier** ke hisaab se baantna.

### 🔴 WHY audiences se pehle?

```
Pehle inventory pata karo
   ↓
Tier pata chalta hai
   ↓
Tier se pata chalta hai:
   • Amazon audiences lag sakti hain ya nahi?
   • Reach forecast possible hai ya nahi?
   • Deal abhi select ho sakti hai ya nahi?
   ↓
TAB audience suggest karo (sahi tarah se)
```

Agar audience pehle suggest kar di, aur baad me pata chala ki inventory Netflix hai (jahan Amazon audiences lagti hi nahi) → **poora kaam bekaar.**

### 📋 FIELD MATRIX

#### 1. **Selected deals**
| | |
|---|---|
| **Type** | Checkbox table |
| **Requirement** | **Required** |
| **Change** | ✅ Core concept unchanged |
| **API** | `GET /api/deals/?markets={market}&formats=streaming_tv` |

**Kya define karti hai:** Kaunse deals chuni gayi.

**Real example (document se):**
```
Available deals (GB, 30s):
┌──────────────────────────────────────────┬───────────┬────────┬─────┐
│ Deal Name                                │ Deal Type │ CPM    │ [x] │
├──────────────────────────────────────────┼───────────┼────────┼─────┤
│ Prime Video | Preferred Deal | UK - 30   │ Preferred │ £28.88 │ [x] │
│ Prime Video | Action | UK - 30           │ Preferred │ £22.07 │ [ ] │
│ Netflix | Preferred | UK - 30            │ Preferred │ £32.00 │ [x] │
└──────────────────────────────────────────┴───────────┴────────┴─────┘
```

---

#### 2. **➕ Inventory tier (per deal)** — NEW
| | |
|---|---|
| **Type** | Enum |
| **Requirement** | **Derived** |
| **Change** | ➕ **NEW** |
| **Values** | `AMAZON_OWNED`, `THIRD_PARTY_PRECURATED`, `THIRD_PARTY_NEEDS_CURATION` |

**"Derived"** = trader **nahi bharta**, system **khud nikalta** hai.

**Kya define karti hai:** Har deal kis tier ki hai — aur isse aage ka poora behaviour tay hota hai (Part 4.3 me detail me).

**Real example:**
```
Deal "Prime Video | Preferred | UK - 30"
→ provider = "Prime Video"
→ inventory_tier = AMAZON_OWNED  ← system ne derive kiya
→ Isliye: reach forecast ✅, Amazon audiences ✅

Deal "Netflix | Preferred | UK - 30"
→ provider = "Netflix"
→ inventory_tier = THIRD_PARTY_PRECURATED  ← derive kiya
→ Isliye: reach forecast ❌, Netflix ki targeting (+CPM)
```

> **⚠ Ek gap:** Document ne likha "Derived" — par **kaise** derive hota hai, ye nahi bataya. Provider name se? Ek mapping table se? API response me aata hai? **David ne yahan comment kiya ho sakta hai.**
>
> Sambhavit jawab: `GET /api/inventory-sources/` (jo ➕ NEW endpoint hai) is mapping ko deta hoga. Par document ne connect nahi kiya.

---

#### 3. **➕ CTV rate card** — NEW
| | |
|---|---|
| **Type** | Reference |
| **Requirement** | **Read** (sirf padhna) |
| **API** | `GET /api/rates/ctv/{market}/` |
| **Deta hai** | channels, durations, CPMs |

**Kya define karti hai:** **Daam ki list** — kis channel par, kis duration ka, kitna CPM.

**Real example (rate card):**
```
GB Rate Card:
┌──────────────┬──────────┬─────────┐
│ Channel      │ Duration │ CPM     │
├──────────────┼──────────┼─────────┤
│ Prime Video  │ 15s      │ £20.00  │
│ Prime Video  │ 30s      │ £28.88  │
│ Netflix      │ 15s      │ £24.00  │
│ Netflix      │ 30s      │ £32.00  │
│ Disney+      │ 15s      │ £26.00  │
│ Disney+      │ 30s      │ £34.00  │
└──────────────┴──────────┴─────────┘
```

### 🔴 WHY rate card critically important hai

**Do wajah:**

**1. Tier 3 (Disney+) ke liye ye HI EK data source hai.**
Deal exist nahi karti. Rate card se hi daam pata chalta hai. Aur rate card se impressions derive hote hain.

**2. Q&A side path ke liye.**
Document page 27, literally:
> *"Q&A side path: at any point, the trader can ask a pricing/availability question ('what's the CPM for Netflix 30s?'). **The agent answers from the rate card** and resumes."*

**Real example:**
```
Trader (beech me): "Netflix 30s ka CPM kya hai?"
Agent → rate card se → "£32.00"
Agent: "Netflix 30s ka CPM £32 hai. Ab hum audience par the — aage chalein?"
       ↑ jawab de kar WAHIN SE aage chala. Flow toota nahi.
```

**"Side path"** = main raaste se hatkar ek chhota raasta, phir wapas main raaste par.

---

#### 4-8. **➕ Curation Fields** — NEW (Tier 3 ke liye)

| Field | Type | Requirement |
|---|---|---|
| **Curation: genres** | Multi-select | **Required for curation tier** |
| **Curation: durations** | Multi-select | **Required for curation tier** |
| **Curation: targeting prefs** | Text | Optional |
| **Curation: budget** | Number | **Required for curation tier** |
| **Curation: flight dates** | Date range | **Required for curation tier** |

**Document literally:**
> *"➕ NEW — Curation capture (for 3P-needs-curation tier): When deals can't be selected yet (Disney+ etc.), the agent captures what VOW needs to curate later: genres, durations, targeting preferences, budget, flight dates."*

**Kya define karte hain:** Wo saari jaankari jo **VOW team ko baad me deal banane ke liye chahiye.**

**Real example — poora dialogue:**
```
Trader: "Prime, Netflix aur Disney+ teeno par chalao"

Agent: "Prime Video aur Netflix ki deals ready hain — main select
        kar leta hun.

        Disney+ ke liye deal abhi ready nahi hai. VOW team IO
        sign hone ke baad banayegi. Main tumse details le leta
        hun taaki wo turant kaam shuru kar sakein:

        1. Kaunse genres? (Required)
        2. Kaunse durations? (Required)
        3. Koi targeting preference? (Optional)
        4. Disney+ ke liye kitna budget? (Required)
        5. Flight dates — same rakhein ya alag? (Required)"

Trader: "Family aur Kids genre, 30s, budget £1,000, dates same"

Agent (state me save):
  curation_requirements = [{
    provider: "Disney+",
    genres: ["Family", "Kids"],
    durations: ["30"],
    targeting_preferences: null,
    budget: "1000.00",
    flight_dates: {lower: "2026-08-01", upper: "2026-08-31"}
  }]

Agent: "Note kar liya. Disney+ ka hissa 'pending curation' rahega —
        VOW team isko manually banayegi. Prime aur Netflix ka plan
        main aage badha raha hun."
```

### PURPOSE
Trader ka kaam **ruke nahi**. Deal ready na hone par bhi agent aage badh sakta hai. **Ye "graceful degradation" hai** — jo nahi ho sakta, uske liye best alternative do.

---

#### **➕ Genre Upsell Logic** — NEW

**Client ka quote (document me literally):**
> *"based on the brief we can suggest whether a specific available genre would be a better match at a slightly higher CPM"*

**Example (document se):** *"Prime Video ROS at $18.22 vs Action at $22.07"*

**Upsell** = "thoda mehnga wala lo, behtar hai" — bech kar aur bechna.

### WHAT?
Agent brief padh kar samajhta hai ki **genre-specific deal** behtar match hoga, aur suggest karta hai — **thoda zyada CPM par**.

### WHY?
Kyunki ROS (Run Of Schedule) sasta hai par **random content** ke saath ad chalega. Genre-specific mehnga hai par **relevant content** ke saath.

**Real example — sports drink:**
```
Brief: "Energy drink for gym-goers, UK, August, £8,000"

Agent sochta hai:
  ROS deal      = $18.22 CPM  →  8,000 ÷ 18.22 × 1000 = 439,078 impressions
  Sports genre  = $22.07 CPM  →  8,000 ÷ 22.07 × 1000 = 362,483 impressions

Agent: "Do options hain:

        A) Prime Video ROS @ $18.22 → 439,000 impressions
           Ad kisi bhi content ke saath chalega

        B) Prime Video Sports @ $22.07 → 362,000 impressions
           Ad SIRF Sports content ke saath chalega

        Tumhara product gym-goers ke liye hai. Sports content
        dekhne wale log tumhare target audience se bahut milte
        hain. 77,000 impressions kam milenge, par har impression
        zyada relevant hoga.

        Main option B recommend karta hun. Tum kya kehte ho?"
```

**Dhyan do — agent ne:**
1. Dono options **numbers ke saath** dikhaye
2. **Trade-off saaf** bataya (77,000 kam impressions)
3. **Reason** diya (gym-goers ↔ Sports content)
4. **Faisla trader par** chhoda

**Ye document ke "agent is an assistant, not a replacement" philosophy ka perfect example hai.**

**Document ki entity normalisation table me bhi ye hai:**
> `sports drink` → *"Consider genre-specific deals (Sports)"* ➕ NEW

---

### 🔧 Step 2 ke API calls
```
GET /api/deals/
GET /api/deals/filter-properties/     ← Ad length, Genre, Deal type ke filter options
GET /api/rates/ctv/{market}/          ← ➕ NEW
```

---

## 🟦 STEP 3: BUDGET SPLIT
### ➕ **ENTIRELY NEW** — v1.1.0 me tha hi nahi

**Client ka quote:**
> *"We will need to support the suggested budget split across inventories or creative durations."*

### WHAT?
Agent **propose** karta hai ki total budget kaise baante — **inventories** me (Prime/Netflix/Disney) aur **durations** me (15s/30s).

### WHY ye step chahiye?

**Document khud maanta hai ye mushkil hai:**
> *"This is genuinely hard — different durations have different CPMs, and there's no reach data for Netflix/Disney to optimise against."*

**Do problem:**

**Problem 1 — Alag CPM:**
```
15s @ £20 CPM  aur  30s @ £30 CPM
£5,000 dono me →  15s: 250,000 impressions
                  30s: 166,667 impressions
→ Same paisa, ALAG impressions. To "even" split ka matlab kya?
```

**Problem 2 — Netflix/Disney ka reach data nahi:**
```
Normally budget wahan lagate ho jahan best reach mile.
Par Netflix ka reach data nahi hai!
→ To kaise decide karo Netflix me £3,000 ya £4,000 daalna hai?
→ Koi objective jawab nahi hai.
```

### 📋 FIELD MATRIX

| Field | Type | Requirement |
|---|---|---|
| **Split by inventory** | Allocation (%) | **Required when multiple inventories selected** |
| **Split by duration** | Allocation (%) | **Required when multiple durations selected** |
| **Split method** | Enum | **Agent states its assumption** |

**"Allocation"** = baantna / hissa dena.
**"Agent states its assumption"** = agent apni **maan-liye-gaye baat** batata hai.

### 🔴 Do Split Methods — Poora Ganit

**Document literally:**
> *"EVEN_BY_BUDGET — same £ per inventory/duration; uneven impressions (higher CPM = fewer impressions)"*
> *"EVEN_BY_IMPRESSIONS — same impression count; uneven £ (higher CPM = more spend)"*

#### Method 1: **EVEN_BY_BUDGET** — barabar paisa

```
Total: £10,000
Durations: 15s (£20 CPM) aur 30s (£30 CPM)

Baraabar PAISA baanto:
┌──────┬─────────┬─────────┬──────────────────────────────┐
│      │ Budget  │ CPM     │ Impressions                  │
├──────┼─────────┼─────────┼──────────────────────────────┤
│ 15s  │ £5,000  │ £20     │ 5,000 ÷ 20 × 1000 = 250,000  │
│ 30s  │ £5,000  │ £30     │ 5,000 ÷ 30 × 1000 = 166,667  │
├──────┼─────────┼─────────┼──────────────────────────────┤
│TOTAL │ £10,000 │         │ 416,667                      │
└──────┴─────────┴─────────┴──────────────────────────────┘

✅ Paisa BARAABAR (£5,000 each)
❌ Impressions ALAG (250K vs 167K) — 15s ko 83K zyada mile
```

#### Method 2: **EVEN_BY_IMPRESSIONS** — barabar impressions

```
Total: £10,000
Baraabar IMPRESSIONS chahiye. Kitne? Ye nikalna padega:

Agar X impressions dono ko dene hain:
  15s ka kharch = X ÷ 1000 × 20 = 0.020X
  30s ka kharch = X ÷ 1000 × 30 = 0.030X
  Total         = 0.050X = £10,000
  → X = 200,000 impressions each

┌──────┬─────────────┬─────────┬──────────────────────────┐
│      │ Impressions │ CPM     │ Budget                   │
├──────┼─────────────┼─────────┼──────────────────────────┤
│ 15s  │ 200,000     │ £20     │ 200 × 20 = £4,000        │
│ 30s  │ 200,000     │ £30     │ 200 × 30 = £6,000        │
├──────┼─────────────┼─────────┼──────────────────────────┤
│TOTAL │ 400,000     │         │ £10,000                  │
└──────┴─────────────┴─────────┴──────────────────────────┘

✅ Impressions BARAABAR (200K each)
❌ Paisa ALAG (£4,000 vs £6,000) — 30s ne £2,000 zyada khaya
```

#### Method 3: **CUSTOM**
Trader khud batata hai: "Prime 70%, Netflix 30%."

### 🔴 SABSE ZAROORI RULE — Agent apni assumption batata hai

**Document literally:**
> *"The agent must state which it chose and why, so the trader can adjust. Example: **'I've split evenly by impressions, which weights spend toward the 30s at its higher CPM.'**"*

**"weights spend toward"** = kharch ko us taraf jhukata hai.

**Real example — agent ka poora message:**
```
Agent: "Budget split propose kar raha hun. Tumne 15s aur 30s
        dono chune hain, aur teen inventories.

        Main ne EVEN_BY_IMPRESSIONS chuna hai — matlab dono
        durations ko baraabar impressions milenge:

        ┌─────────────┬──────────┬─────────┬─────────────┐
        │ Inventory   │ Duration │ Budget  │ Impressions │
        ├─────────────┼──────────┼─────────┼─────────────┤
        │ Prime Video │ 15s      │ £2,400  │ 120,000     │
        │ Prime Video │ 30s      │ £3,600  │ 120,000     │
        │ Netflix     │ 15s      │ £1,440  │  60,000     │
        │ Netflix     │ 30s      │ £1,560  │  52,000     │
        │ Disney+     │ 30s      │ £1,000  │  29,412     │
        ├─────────────┼──────────┼─────────┼─────────────┤
        │ TOTAL       │          │ £10,000 │ 381,412     │
        └─────────────┴──────────┴─────────┴─────────────┘

        ⚠ Dhyan do: is method me kharch 30s ki taraf jhuka hai,
        kyunki 30s ka CPM zyada hai. Agar tum baraabar PAISA
        chahte ho (EVEN_BY_BUDGET), to 15s ko zyada impressions
        milenge par 30s ko kam.

        Kaunsa chahiye? Ya custom % batao."
```

**Dhyan do — agent ne:**
1. Apni **choice batayi** (EVEN_BY_IMPRESSIONS)
2. **Poora table** dikhaya
3. **Consequence bataya** ("kharch 30s ki taraf jhuka hai")
4. **Alternative bataya** (EVEN_BY_BUDGET)
5. **Trader ko control diya**

### ⚠ IMPORTANT: Koi API call nahi

**Document literally:** *"No API call — this is agent-side logic. The resulting budgets feed into the `market_budgets` field at strategy creation."*

**Matlab:**
- Ye ganit **agent khud** karta hai
- Nateeja `market_budgets` me jaata hai (jo Step 8 ke `POST /api/strategies/` me bheja jaata hai)

> **⚠ Principle 3 ke saath tension:** "API-Driven Tool Execution" kehta hai har step API se mapped ho. Ye step nahi hai. **David ne yahan comment kiya ho sakta hai.** (Jawab Part 3 me diya hai.)

### PURPOSE
1. Trader ka **manual ganit bacha**
2. Agent ki **soch transparent** rahi
3. Trader ko **adjust karne ka mauka** mila
4. Multi-inventory / multi-duration campaign **possible** hua

---

## 🟦 STEP 4: AUDIENCES
### 🔄 CHANGED — pehle optional thi, ab **mandatory + suggestion-driven**, aur budget split ke **baad**

### WHAT?
Agent **teen audience options** banata hai (Narrow / Balanced / Wide), trader **ek chunta** hai.

### WHY budget split ke baad?
Kyunki audience ki **VCPM fee** budget par asar daalti hai. Pehle budget baanto, phir dekho ki us budget me kaunsi audience afford kar sakte ho.

### 📋 FIELD MATRIX

#### 1. **Audience options**
| | |
|---|---|
| **Type** | 3 profiles |
| **Requirement** | **Required** |
| **Change** | 🔄 **CHANGED** — optional se **mandatory** |
| **Behaviour** | *"Agent always generates narrow / balanced / wide"* |

**Kya define karti hai:** Teen taiyar options jo agent ne banaye.

**Real example — API se aaya response:**
```json
{
  "bundles": {
    "narrow": [
      {"id": "aud_101", "name": "Higher Education Seekers",
       "vcpm": "1.85", "estimated_reach": 450000}
    ],
    "balanced": [
      {"id": "aud_101", "name": "Higher Education Seekers",
       "vcpm": "1.85", "estimated_reach": 450000},
      {"id": "aud_102", "name": "E-Learning & Tech Enthusiasts",
       "vcpm": "1.63", "estimated_reach": 1200000}
    ],
    "broad": [
      {"id": "aud_101", "name": "Higher Education Seekers", ...},
      {"id": "aud_102", "name": "E-Learning & Tech Enthusiasts", ...},
      {"id": "aud_103", "name": "General Career Advancement",
       "vcpm": "1.20", "estimated_reach": 3500000}
    ]
  }
}
```

**Dhyan do pattern — bundles nested hain:**
```
narrow   = 1 segment              (sabse chhota, sabse mehnga: £1.85)
balanced = narrow + 1 more        (2 segments)
broad    = balanced + 1 more      (3 segments, sabse bada, sasta: £1.20)
```

**Bundle** = groups ka group. Ek "bundle" me kai audience segments hote hain.

---

#### 2. **➕ Chosen option** — NEW
| | |
|---|---|
| **Type** | Select one |
| **Requirement** | **Required** |
| **Change** | ➕ **NEW** — *"Trader picks one of the three"* |

**Kya define karti hai:** Trader ne kaunsa profile chuna.

**WHY ye field NEW hai?** Kyunki v1.1.0 me trader **khud browse** karke segments chunta tha. Ab agent 3 options deta hai aur trader **ek chunta** hai. Ye ek naya interaction pattern hai — isliye naya field.

---

#### 3. **Matching mode**
| | |
|---|---|
| **Type** | Toggle |
| **Requirement** | **Required** |
| **Change** | ✅ Unchanged |
| **Values** | `Similar` vs `Exact` |

**Kya define karti hai:** Audience match **kitna sakht** hoga.

- **Exact** = bilkul wahi log jo segment me hain
- **Similar** = wo log **+ unke jaise** log (lookalike)

**Real example:**
```
Segment: "Higher Education Seekers" — 450,000 log

Exact mode   → 450,000 log target honge
Similar mode → 450,000 + unke jaise (lookalike) log
             → ho sakta hai 900,000 log
             → zyada reach, par thodi kam precision
```

**Lookalike** = "isse milte-julte log."

**WHY?** Agar audience chhoti hai aur reach nahi mil raha, `Similar` on karke reach badha sakte ho — **repair loop ka ek tool.**

---

#### 4. **➕ Effective CPM (per option)** — NEW
| | |
|---|---|
| **Type** | Display |
| **Requirement** | **Read-only** |
| **Change** | ➕ **NEW** |
| **Formula** | Deal CPM + audience VCPM fee |
| **Kyun** | *"shown per option so the trader sees the real cost"* |

**Real example — teen options ke saath effective CPM:**
```
Deal: Prime Video Preferred @ £28.88 CPM
Budget: £10,000

┌───────────┬────────┬───────────────┬─────────────┬────────────┐
│ Option    │ VCPM   │ Effective CPM │ Impressions │ Reach est. │
├───────────┼────────┼───────────────┼─────────────┼────────────┤
│ NARROW    │ £1.85  │ £30.73        │ 325,415     │ 450,000    │
│ BALANCED  │ £1.74* │ £30.62        │ 326,584     │ 1,650,000  │
│ WIDE      │ £1.56* │ £30.44        │ 328,515     │ 5,150,000  │
└───────────┴────────┴───────────────┴─────────────┴────────────┘
                                     (* average VCPM of bundle)

Agent: "Teen options hain. Dhyan do — Narrow sabse mehnga hai
        (£30.73 effective CPM) AUR sabse chhota (450K available
        log). Balanced main recommend karta hun."
```

**WHY ye field itna important hai?** Kyunki bina iske trader sochega ki audience **free** hai. Wo £28.88 dekh kar plan banayega, aur £30.73 dega. Part 1.C me poora ganit hai.

---

### 🔴 4 Constraints for CTV (Document literally)

> *"Amazon audiences only apply to Amazon-owned inventory. For Netflix/Disney, their own targeting applies"*
> *"❌ Product audiences not applicable to CTV (removed)"*
> *"AMC audiences are conditional — only when the advertiser has prior campaign data"*
> *"Nobody browses — the agent uses POST /api/audience-sets/suggest/ exclusively"*
> *"The audience set does not need to be created before forecasting — it's created later at strategy creation via a simplified CTV endpoint"*

**Constraint 1: Amazon audiences sirf Amazon inventory par**

**Real example — mixed plan me kya hota hai:**
```
Plan: Prime Video £6,000 + Netflix £3,000 + Disney+ £1,000

Prime Video portion:
  ✅ Amazon audience "Higher Education Seekers" lag gayi
  ✅ VCPM £1.85

Netflix portion:
  ❌ Amazon audience NAHI lag sakti
  → Netflix ki apni targeting use karni padegi
  → Uska ALAG extra CPM lagega
  → Agent: "Netflix ke liye Amazon audiences apply nahi hoti.
            Netflix apni targeting deta hai jiska alag CPM lagta hai.
            Kya main Netflix ke liye general demographic targeting rakhun?"

Disney+ portion:
  ❌ Same — Disney ki apni targeting
  → Aur wo curation requirements me capture ho gaya
```

**Constraint 4 (sabse zaroori — timing):** *"The audience set does not need to be created before forecasting — it's created later at strategy creation via a simplified CTV endpoint"*

**Plain me:**
```
❌ Purana tarika hota:
   1. Audience set database me BANAO
   2. Uska ID lo
   3. Us ID se forecast karo
   → Agar forecast bura nikla, ek bekaar audience set database me pada reh gaya

✅ Naya tarika:
   1. Audience suggest karo (sirf memory me, banao nahi)
   2. Directly forecast karo
   3. Plan approve hone ke BAAD (Step 8 me) audience set banao
   → Database saaf rehta hai, koi kachra nahi
```

**WHY?** Kyunki repair loop me agent **kai baar** audience badalta hai. Har baar database me create karta to 10 bekaar audience sets ban jaate.

---

### 🔧 Step 4 ke API calls
```
POST /api/audience-sets/suggest/  →  GET /api/audience-sets/suggest/{id}/
```

**Dhyan do — do calls hain, POST phir GET.** Ye **async pattern** hai:
```
POST /api/audience-sets/suggest/     → "kaam shuru karo"
     ← {"id": "sug_789", "status": "processing"}

(vector search chal raha hai... 3,400 segments par...)

GET /api/audience-sets/suggest/sug_789/  → "kaam ho gaya?"
     ← {"status": "complete", "bundles": {...}}
```

**Async** = kaam turant nahi hota, thoda time lagta hai. Isliye "shuru karo" aur "ho gaya?" do alag calls.

**WHY async?** Kyunki 3,400 segments par vector similarity search me time lagta hai. Ek hi call me karte to request **timeout** ho jaati.

---

### ⚠⚠ OPEN QUESTION #2 — Suggest endpoint ka response shape

**Document literally:**
> *"⚠ Open question: the suggest endpoint's response shape. v1.1.0 assumed it returns `bundles.narrow/balanced/broad`. **The real endpoint may return a flat list that we group ourselves.** Confirm against the real API."*

**Plain me:**

```
v1.1.0 ne MAAN LIYA tha ki API aisa deta hai:
{
  "bundles": {
    "narrow":   [...],
    "balanced": [...],
    "broad":    [...]
  }
}
   ↑ API ne PEHLE SE grouping kar di

Par asli API ho sakta hai aisa de:
{
  "suggestions": [
    {"id": "aud_101", "name": "...", "vcpm": "1.85", "score": 0.94},
    {"id": "aud_102", "name": "...", "vcpm": "1.63", "score": 0.91},
    {"id": "aud_103", "name": "...", "vcpm": "1.20", "score": 0.78},
    ... 10 aur ...
  ]
}
   ↑ FLAT list. Grouping HUM karenge.
```

**Kyun ye matter karta hai?**

| Agar API grouping deta hai | Agar flat list deta hai |
|---|---|
| Agent bas display karta hai | **Agent ko grouping logic likhna padega** |
| Kaam kam | Naya sawaal: "Narrow me kitne segments? 1? 2?" |
| | Naya sawaal: "Kis basis par group karein — score? reach? VCPM?" |
| | **Ye ek poora naya feature hai** |

**Agar flat list hai to grouping logic kuch aisa hoga:**
```python
# Ek possible approach (document me NAHI hai — ye mera suggestion hai)
sorted_by_reach = sorted(suggestions, key=lambda s: s["estimated_reach"])
narrow   = sorted_by_reach[:1]     # sabse chhota 1
balanced = sorted_by_reach[:2]     # sabse chhote 2
wide     = sorted_by_reach[:3]     # sabse chhote 3
# ya cumulative reach target ke hisaab se
```

> 🎯 **David ne is par pakka comment kiya hoga.** Ye ek **real risk** hai — agar API ka shape alag nikla, to schema aur code dono badalna padega.
>
> **Tumhara jawab hona chahiye:** *"Ye ek genuine unknown hai. Isliye maine ise ⚠ Open Question mark kiya, assume karke aage nahi badha. Agar VOW backend team se abhi confirm ho jaaye to main schema final kar dunga. Aur agar flat list hai, to main ForecastResultSchema jaisa ek grouping layer add karunga jo Balanced ko default recommend kare."*

---

## 🟦 STEP 5: TARGETING
### ➕ **ENTIRELY NEW** — v1.1.0 me tha hi nahi

### WHAT?
Audience ke **upar** extra filters — kahan, kis position par, kis device par ad dikhe.

### Audience vs Targeting me farak? (Confusion clear karo)

```
AUDIENCE  = "KAUN dekhega?"      → "Higher Education Seekers"
TARGETING = "KAHAN/KAISE dikhega?" → "London me, mid-roll position par,
                                      Smart TV par, horror content ke
                                      alawa"
```

Audience **logon** ke baare me hai. Targeting **context** ke baare me hai.

### 📋 FIELD MATRIX — saare Optional

| Field | Type | Requirement | Kya define karti hai |
|---|---|---|---|
| **Location** | Multi-select | Optional | Desh ke **andar** ki jagah — city, region, postcode |
| **Instream position** | Select | Optional | Ad video me **kahan** aayega — pre/mid/post-roll |
| **Content-category exclusions** | Multi-select | Optional | **Kis tarah ke content ke saath NAHI** dikhana |
| **Device type** | Multi-select | Optional | Smart TV, mobile, tablet, desktop |
| **Mobile environment** | Select | Optional | App ke andar ya browser me |

### Ek-ek field ko real example ke saath samjho

#### **Location**
```
markets = ["GB"]           ← Step 1: desh
location = ["London", "Manchester"]  ← Step 5: desh ke ANDAR

→ Ad sirf London aur Manchester me dikhega, poore UK me nahi
```

**API:** `GET /api/strategies/locations/{market}/`

**WHY?** Local business. "BrightPath ka campus London me hai" → sirf London me ad chalao, Scotland me paisa barbaad na karo.

#### **Instream position**
```
Pre-roll  = video SHURU hone se pehle    → sabse zyada dekha jaata hai
Mid-roll  = video ke BEECH me            → best attention (banda invested hai)
Post-roll = video KHATAM hone ke baad    → sabse kam dekha jaata hai
```

**"Instream"** = video stream ke **andar** ka ad (banner nahi, video ad).

**WHY?** Mid-roll me banda pehle se video dekh raha hai — attention zyada. Par CTV me mostly mid-roll hota hai anyway.

#### **Content-category exclusions**
```
exclusions = ["News", "Horror", "True Crime"]
→ Ad in genres ke saath NAHI dikhega
```

**WHY? — Brand safety ka real example:**
```
BrightPath (education) ka ad chal raha hai.
Agar wo ek True Crime documentary ke beech me aaye jahan
crime ki baat ho rahi hai — brand ko nuksaan.

Ya: airline ka ad ek plane crash news ke saath aa jaaye. Disaster.

→ Isliye exclusions.
```

**"Exclusion"** = nikalna / mana karna.

#### **Device type**
```
device_types = ["Connected TV", "Mobile"]
→ Ad sirf in devices par dikhega
```

**WHY?** CTV campaign me mostly "Connected TV" chahiye. Par kuch advertiser mobile bhi chahte hain.

#### **Mobile environment**
```
"in-app"     = mobile APP ke andar (Prime Video app)
"mobile web" = mobile BROWSER me
```

**WHY?** In-app me tracking behtar hai, aur user experience alag hai.

---

### 🔴 CRITICAL DESIGN NOTE — Config-driven

**Client ka quote (document me literally):**
> *"This targeting list frequently changes so it should be easy to add new targeting types."*
> — *the implementation must be **config-driven, not hard-coded**. Adding a new targeting type should be a **configuration change, not a code change**.*

**Ye Part 1.J me detail me samjhaya hai. Yahan Step 5 ke context me:**

```
❌ HARD-CODED (galat approach):
class TargetingSchema(BaseModel):
    locations: list[str]
    instream_positions: list[str]
    content_category_exclusions: list[str]
    device_types: list[str]
    mobile_environments: list[str]

→ Client kal kahega "language targeting add karo"
→ Code badlo → PR → review → test → deploy → 3 din

✅ CONFIG-DRIVEN (sahi approach):
targeting_types.yaml:
  - key: locations
    type: multi_select
    api: /api/strategies/locations/{market}/
  - key: device_types
    type: multi_select
    options: [Connected TV, Mobile, Tablet, Desktop]
  - key: language              ← ek line add ki
    type: multi_select
    options: [English, French, German]

→ Client kal kahega "language add karo"
→ Config me 4 line → 10 minute
```

> **⚠ IMPORTANT GAP:** Document ne client ka ye critical requirement **likha** hai, par **Pydantic model me follow NAHI kiya.** `TargetingSchema` me 5 hard-coded fields hain! Ye **contradiction** hai.
>
> ```python
> class TargetingSchema(BaseModel):
>     """➕ NEW — CTV targeting options (config-driven, extensible)"""
>     locations: list[str] = Field(default_factory=list)
>     instream_positions: list[str] = Field(default_factory=list)
>     content_category_exclusions: list[str] = Field(default_factory=list)
>     device_types: list[str] = Field(default_factory=list)
>     mobile_environments: list[str] = Field(default_factory=list)
> ```
> Docstring kehta hai "config-driven, extensible" — par code **hard-coded** hai!
>
> 🎯 **David ne is par pakka comment kiya hoga.** Ye ek asli technical inconsistency hai.
>
> **Possible fix (tumhara jawab):**
> ```python
> class TargetingSchema(BaseModel):
>     """Config-driven targeting. Keys validated against
>        the targeting-type registry at runtime, not compile time."""
>     selections: dict[str, list[str]] = Field(default_factory=dict)
>     # {"locations": ["London"], "device_types": ["Connected TV"]}
> ```
> Isse naya targeting type add karne ke liye **code badalna nahi padega** —
> sirf registry/config me entry.

---

### ❌ Not supported by VOW today (future scope)
Document literally: *"genre exclusions, day-parting, language."*

| Feature | Matlab |
|---|---|
| **Genre exclusions** | "Horror ke saath mat dikhao" — content-category exclusions se alag |
| **Day-parting** | Din ke **time** ke hisaab se — "sirf shaam 6-11 baje" |
| **Language** | Content ki bhasha ke hisaab se |

**WHY ye note zaroori?** Taaki trader **maange na** ya agent **promise na kare**. Ye Zero-Hallucination ka hi extension hai — jo nahi hai, uske baare me saaf batao.

### 🔧 Step 5 ke API calls
```
POST /api/contextual-targeting/{market}/products/
GET  /api/strategies/locations/{market}/
```

---

## 🟦 STEP 6: PREDICT REACH
### 🔄 CHANGED — pehle ek sub-step tha, ab **first-class step** with **tier-based honesty rule**

**"First-class step"** = poora apna step, kisi ke andar chhupa hua nahi.

### WHAT?
Forecast nikalna — kitne impressions, kitna reach, kitni frequency milegi. **Aur jahan data nahi hai, wahan saaf mana karna.**

### 📋 FIELD MATRIX

| Field | Type | Requirement | Change |
|---|---|---|---|
| **Reach curve** | Chart | Read-only **(Amazon only)** | 🔄 CHANGED — *"Only available for Amazon-owned inventory. For 3P, state honestly that reach is unavailable"* |
| **Estimated impressions** | Number | Read-only | ✅ Unchanged |
| **Estimated unique reach** | Number | Read-only **(Amazon only)** | 🔄 CHANGED — *"Not available for Netflix/Disney"* |
| **Average frequency** | Number | Read-only **(Amazon only)** | 🔄 CHANGED — *"Not available for Netflix/Disney"* |
| **Indicative CPM** | Number | Read-only | ✅ Unchanged |

### Ek-ek field

#### **Estimated impressions** — ✅ SABHI tiers ke liye available
```
Formula: budget ÷ CPM × 1,000
→ Ye pure GANIT hai. Koi data nahi chahiye.
→ Isliye Netflix/Disney ke liye BHI mil jaata hai.
```

#### **Estimated unique reach** — ❌ Sirf Amazon
```
Kitne ALAG-ALAG log dekhenge.
→ Iske liye VIEWER DATA chahiye ("kaun kya dekhta hai")
→ Amazon ke paas hai. Netflix nahi deta.
→ Isliye Netflix/Disney ke liye NAHI mil sakta.
```

#### **Average frequency** — ❌ Sirf Amazon
```
Formula: impressions ÷ reach
→ Reach ke BINA frequency nahi nikal sakti!
→ Netflix ka reach nahi hai → frequency bhi nahi
```

#### **Indicative CPM** — ✅ Sabhi tiers
```
"Indicative" = anumaanit / ishara karne wala
→ Actual CPM auction me thoda badal sakta hai (Private Auction me)
→ Isliye "indicative" — pakka nahi, ishara
→ Rate card se pata chal jaata hai → sabhi tiers ke liye available
```

#### **Reach curve** — ❌ Sirf Amazon

**Reach curve** = ek **chart** jo dikhata hai "kitna paisa lagane par kitna reach milega."

**Real example (document se, literally):**
```json
"reach_curve": [
  {"budget": 2500,  "reach": 65000},
  {"budget": 5000,  "reach": 120000},
  {"budget": 7500,  "reach": 170000},
  {"budget": 10000, "reach": 210000}
]
```

**Chart me:**
```
Reach
210K │                                    ●
     │                          ●
170K │                ●
120K │      ●
 65K │  ●
     └────┬──────┬──────┬──────┬─────→ Budget
        £2.5K  £5K   £7.5K  £10K
```

### 🔴 Reach Curve se ek ZAROORI insight — Diminishing Returns

Numbers dekho:
```
£2,500  → 65,000  reach     (pehla £2,500 → +65,000)
£5,000  → 120,000 reach     (doosra £2,500 → +55,000)  ← kam!
£7,500  → 170,000 reach     (teesra £2,500 → +50,000)  ← aur kam!
£10,000 → 210,000 reach     (chautha £2,500 → +40,000) ← aur kam!
```

**Diminishing returns** = jitna aage badho, utna **kam faayda** milta hai.

**WHY aisa hota hai?** Kyunki shuru me naye log milte hain. Baad me **wahi log dobara** milte hain (frequency badhti hai, reach nahi).

**Ye trader ke liye SONA hai:**
```
Agent: "Reach curve dekho — £7,500 se £10,000 tak jaane par
        sirf 40,000 naye log milenge. Pehle £2,500 me 65,000
        mile the.

        Agar tumhara goal max reach hai, to £7,500 par ruk kar
        £2,500 doosre market ya doosre inventory me lagana zyada
        efficient ho sakta hai. Kya main FR market ka option
        dikhaun?"
```

**Yahi tumhare task slide ka "forecast-backed Strategy card" hai** — ek card jiske peeche asli numbers hain.

---

### 🔴🔴 THE HONESTY RULE — ➕ NEW (Document ka best feature)

**Document literally:**
> *"➕ NEW — the honesty rule for 3P inventory: For Netflix/Disney, the agent shows: rate-card CPM and derived impressions (budget ÷ CPM × 1,000). **It explicitly states that reach is unavailable and why. Never invent a reach number.**"*

### Real example — poora agent message, teen portions ke saath:

```
╔══════════════════════════════════════════════════════════════════╗
║  FORECAST — BrightPath Campaign                                  ║
║  Total budget £10,000 · 1–30 Aug 2026 · GB                       ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ✅ PRIME VIDEO (£6,000)                  [AMAZON_OWNED]         ║
║     Deal CPM         £28.88                                      ║
║     Audience VCPM    £ 1.85  (Higher Education Seekers)          ║
║     Effective CPM    £30.73                                      ║
║     Impressions      195,249                                     ║
║     Unique reach     128,400          ← ASLI FORECAST            ║
║     Frequency        1.52             ← ASLI FORECAST            ║
║     Reach curve      ✅ available (chart neeche)                  ║
║                                                                  ║
║  ⚠️  NETFLIX (£3,000)             [THIRD_PARTY_PRECURATED]       ║
║     Rate-card CPM    £32.00                                      ║
║     Impressions      93,750           ← ganit se (3000÷32×1000)  ║
║     Unique reach     ❌ NOT AVAILABLE                             ║
║     Frequency        ❌ NOT AVAILABLE                             ║
║                                                                  ║
║     KYUN: Netflix apna viewer-level data Amazon DSP ke saath      ║
║     share nahi karta. Isliye main sirf impressions bata sakta     ║
║     hun. Reach ka number main GUESS NAHI karunga.                 ║
║                                                                  ║
║  📝 DISNEY+ (£1,000)          [THIRD_PARTY_NEEDS_CURATION]       ║
║     Rate-card CPM    £34.00                                      ║
║     Impressions      29,412           ← ganit se                 ║
║     Unique reach     ❌ NOT AVAILABLE                             ║
║     Deal status      ⏳ PENDING CURATION                          ║
║                                                                  ║
║     KYUN: Disney+ ki deal abhi exist nahi karti. VOW team IO      ║
║     sign hone ke baad banayegi. Requirements capture ho gayi.     ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  TOTAL IMPRESSIONS: 318,411                                      ║
║                                                                  ║
║  ⚠️  TOTAL UNIQUE REACH: ADD NAHI KAR SAKTE                       ║
║     Prime ka reach 128,400 hai. Netflix/Disney ka data nahi.      ║
║     Aur agar hota bhi, to jodna GALAT hota — kyunki wahi          ║
║     insaan Prime aur Netflix dono dekh sakta hai (double          ║
║     counting). Cross-platform deduplication possible nahi hai.    ║
╚══════════════════════════════════════════════════════════════════╝
```

### WHY ye rule product ka **sabse bada asset** hai?

**Socho ek competitor ka product:**
```
Competitor agent: "Total reach: 285,000 unique viewers"
                   ↑ Prime 128K + Netflix (guess 95K) + Disney (guess 62K)
                     = SAB JHOOTH

Trader ne client ko promise kiya: "285,000 log dekhenge"
Campaign khatam → asli report: 145,000
Client: "Tum ne 285K bola tha!"
→ Trust khatam. Product uninstall.
```

**Tumhara agent:**
```
"Prime par 128,400 confirmed. Netflix/Disney ka reach data
 available nahi — main guess nahi karunga."

Trader ne client ko yahi bola. Client ne accept kiya.
Campaign khatam → report matched.
→ TRUST BANA.
```

> 💡 **"Nahi pata" kehna, galat number dene se HAZAAR guna behtar hai.**
> Ye document ka sabse mature design decision hai — aur ye tumhare v1.1.0 ke Zero-Hallucination principle ka seedha natija hai. **Ye tumhari jeet hai.**

---

### ➕ NEW — Do Consequences (Document literally)

> *"The repair loop (too narrow → widen → re-forecast) applies **only to the Amazon portion**"*
> *"Total reach cannot be summed across providers (no cross-platform deduplication)"*

**Consequence 1 — Repair loop sirf Amazon par:**
```
Prime Video portion: reach 0 nikla?
→ ✅ Repair kar sakte ho: audience widen karo → dobara forecast → check karo

Netflix portion: reach 0 nikla?
→ ❌ Repair NAHI kar sakte. Kyunki reach ka data hi nahi hai!
→ Kya widen karein? Kaise pata chalega ki behtar hua?
→ Netflix ke liye "repair" ka concept exist nahi karta
```

**Consequence 2 — Total reach add nahi (Part 4.3 me poora explanation)**

---

### 🔄 REPAIR LOOP — Concept ✅ correct, Mechanism 🔄 updated

**Document ka comparison table (literally):**

| **Was (v1.1.0)** | **Now (v2.0)** |
|---|---|
| If `estimated_unique_reach == 0`, switch from Narrow to Balanced/Broad | If reach is insufficient, **extend the audience** (not necessarily switch profiles — could **add segments within the chosen profile**) |
| Also adjust base CPM bid upward | ✅ Still valid as Action 2 |
| Re-run forecast | ✅ Unchanged |

### 🔴 Mechanism kaise badla — ye samajhna zaroori hai

```
❌ v1.1.0 ka tarika (JUMP):
   Narrow reach 0 → seedha BALANCED par jump karo
                  → seedha BROAD par jump karo

   Problem: Ye bahut BADA jump hai!
   Narrow  = 450,000 log
   Balanced = 1,650,000 log
   → 4x jump! Trader ne Narrow chuna tha (precision ke liye),
     aur agent ne usko 4x chaudi kar di.
   → Trader ka intent (precision) mar gaya

✅ v2.0 ka tarika (EXTEND):
   Narrow reach kam → Narrow ke ANDAR ek segment ADD karo
                    → dobara forecast
                    → phir bhi kam? Ek aur segment add karo
                    → zaroorat pade to TAB Balanced par jao

   Faayda: Chhote-chhote kadam. Trader ka intent (precision) bacha.
```

**"Extend the audience"** = audience **badhana** (segments jodna), **badalna** nahi.

### Real example — poora repair loop chalta hua:

```
════════════════════════════════════════════════════════════════
ROUND 1
Trader ne NARROW chuna: ["Higher Education Seekers"]  (450,000)
Budget: £6,000 (Prime portion)
Effective CPM: £30.73

→ POST /api/audience-sets/reach-forecast/
← {
    "is_available": true,
    "estimated_impressions": 195249,
    "estimated_unique_reach": 22000,     ← BAHUT KAM!
    "average_frequency": 8.87            ← BAHUT ZYADA!
  }

Agent sochta hai:
  Frequency 8.87? Yaani ek banda 9 baar dekhega. Ye AD FATIGUE hai.
  Reach sirf 22,000 — £6,000 me itne kam log?
  → REPAIR chahiye

════════════════════════════════════════════════════════════════
ROUND 2 — Action 1: Audience EXTEND karo (profile badla NAHI)
Agent: Narrow ke andar ek similar segment add karta hai
  audience = ["Higher Education Seekers",
              "Postgraduate Course Researchers"]   ← ADDED
  Combined reach available: ~780,000

→ POST /api/audience-sets/reach-forecast/
← {
    "estimated_unique_reach": 68000,     ← behtar!
    "average_frequency": 2.87            ← behtar!
  }

Agent sochta hai: Frequency 2.87 theek hai. Reach 68,000 acceptable.
                  → Ho gaya. LOOP KHATAM.

════════════════════════════════════════════════════════════════
Agar phir bhi kam hota:
ROUND 3 — Action 2: Base bid badhao
  base_bid £15 → £30  (Prime Video ka recommended floor)

  KYUN? Agar bid market floor se kam hai, auction har baar HAAR
  jaayega → impression hi nahi milega → reach 0.

  Document literally: "increase from £15 to £30 for Prime Video"

ROUND 4 — Action 3: Matching mode Exact → Similar
  → Lookalike log bhi shamil ho jaayenge → reach badhega

ROUND 5 — Last resort: Balanced profile par jao
  → Par pehle trader ko BATAO ki uska Narrow intent badal raha hai
════════════════════════════════════════════════════════════════
```

**Aur repair ke baad agent trader ko batata hai:**
```
Agent: "Tumhara Narrow audience (Higher Education Seekers) bahut
        chhoti nikli — £6,000 me sirf 22,000 log milte, aur har
        banda 9 baar ad dekhta (ad fatigue).

        Maine Narrow profile ke ANDAR ek similar segment joda:
        'Postgraduate Course Researchers'. Ab:
          Reach: 68,000 (pehle 22,000)
          Frequency: 2.87 (pehle 8.87)

        Tumhara precision intent maine bachaya — profile Balanced
        nahi kiya, sirf ek relevant segment joda.

        Theek hai? Ya main Balanced par jaun?"
```

**Yahi tumhare task slide ka "Forecast + the repair loop (auto-widen too-narrow audiences)" hai.**

### 🔧 Step 6 ke API calls
```
POST /api/audience-sets/reach-forecast/   (ya simplified CTV endpoint, naam TBC)
```

**TBC** = To Be Confirmed = "abhi tay nahi hua."

> **⚠ Ye ek chhota open question hai** — endpoint ka naam pata nahi. Aur document me `POST /api/strategies/reach-forecast/` bhi hai (v1.1.0 se). **Do endpoints kyun? Kaunsa use karein?** David ne comment kiya ho sakta hai.

---

## 🟦 STEP 7: PLAN APPROVAL
### ➕ **ENTIRELY NEW** — v1.1.0 me tha hi nahi

**Client ka confirmation (document literally):**
> *"The client confirmed: approval gates the plan, **before it is finalised. Not before launch.** Optionally routes to a manager."*

### WHAT?
Plan taiyar hone ke baad, **insaan** ko dikhana aur uska **approval** lena. Approval na mile to aage nahi badhna.

**"Gates"** = darwaza band karna. "Approval gates the plan" = **approval ke bina plan aage nahi jaayega.**

### 🔴 WHY — "before it is finalised, NOT before launch" ka kya matlab?

Ye bahut subtle par important distinction hai:

```
❌ Option A: "Approval before LAUNCH"
   Plan banao → strategy create karo → creative upload karo
   → tracking setup karo → SAB TAIYAR → phir approval maango

   Problem: Agar manager ne yahan REJECT kar diya, to
            8 steps ka kaam BEKAAR gaya!

✅ Option B (jo chuna gaya): "Approval before FINALISED"
   Plan banao → APPROVAL LO → phir strategy create karo
   → creative upload → tracking → activate

   Faayda: Reject hone par sirf plan wapas jaata hai (Step 4).
           Aage ka kaam shuru hi nahi hua tha.
```

**Matlab:** approval **jaldi** lena hai, **late** nahi. Kyunki jaldi reject sasta hai, late reject mehnga.

### 📋 FIELD MATRIX

| Field | Type | Requirement | Kya define karti hai |
|---|---|---|---|
| **Approval status** | Enum | **Required** | `PENDING` → `APPROVED` ya `REJECTED` |
| **Approved by** | String (user) | Set on approval | **Kisne** approve kiya |
| **Approved at** | Timestamp | Set on approval | **Kab** approve kiya |
| **Manager required** | Boolean | **Configurable** (possibly budget-threshold-based) | Manager ka approval chahiye ya nahi |
| **Rejection reason** | Text | **Required on reject** | **Kyun** reject kiya |

### Ek-ek field

#### **Approval status** — `PENDING` → `APPROVED` / `REJECTED`
Shuru me `PENDING` (intezaar me). Phir ek do me se.

#### **Approved by** aur **Approved at** — Audit Trail
**Audit trail** = **kaam ka record** — kisne kya kiya, kab kiya.

**WHY zaroori?**
```
6 mahine baad: "£50,000 ka ye campaign kisne approve kiya tha?"
→ approved_by = "david.moss@company.com"
→ approved_at = "2026-07-29T14:22:00Z"
→ Jawab mil gaya.
```

**Timestamp** = exact time. ISO format: `2026-07-29T14:22:00Z` (Z = UTC timezone).

Document literally: *"The approval is logged in the audit trail."*

**Compliance ke liye zaroori hai.** Paisa involve hai — record hona chahiye.

#### **Manager required** — Configurable, budget-threshold-based
Document literally: *"Configurable (possibly budget-threshold-based)"*

**Threshold** = seema / limit.

**Plain matlab:**
```
Agar budget < £5,000  → trader khud approve kar sakta hai
Agar budget ≥ £5,000  → MANAGER ka approval chahiye
```

**WHY?** Chhote campaigns ke liye manager ko rokna bekaar hai (bottleneck). Bade paise ke liye manager zaroori hai.

**"Possibly"** ka matlab — document ne isko **pakka nahi** kiya. Ye bhi ek chhota open question hai.

> **⚠ David ne yahan comment kiya ho sakta hai:** "Threshold kya hai? Kaun set karta hai? Per-advertiser ya global?"

#### **Rejection reason** — Required on reject
Reject karne par **wajah likhna zaroori** hai.

**WHY?** Kyunki reject hone par flow Step 4 par wapas jaata hai. Agar wajah na ho, to trader ko **pata hi nahi** chalega kya theek karna hai.

**Real example:**
```
❌ Reject bina reason: "Rejected"
   Trader: "Ab main kya karun??"

✅ Reject with reason: "Netflix ka £3,000 hissa hatao — hamare paas
                        Netflix ka annual commitment pehle se pura ho
                        gaya hai. Wo budget Prime Video me daalo."
   Trader: "Samajh gaya" → Step 4 par jaake theek karta hai
```

---

### 🔴 IMPLEMENTATION: LangGraph `interrupt()`

**Document literally:**
> *"Implementation: LangGraph `interrupt()`. **The graph physically stops and persists state.** It cannot proceed until a human sends approve or reject. **The budget is locked at this moment — nothing launches that a person hasn't approved.**"*

### Line ko tod kar samjho

| Hissa | Matlab |
|---|---|
| **physically stops** | Sach me ruk jaata hai — koi background me nahi chalta |
| **persists state** | Poori state **save** kar deta hai (database/disk par) |
| **cannot proceed until** | Insaan ke jawab **ke bina** aage nahi badh sakta |
| **budget is locked** | Us waqt ka budget **fix** ho jaata hai |

### WHY `interrupt()` zaroori hai — normal code se kyun nahi?

```
❌ Normal approach (galat):
   while approval_status != "APPROVED":
       sleep(60)          ← 60 second wait
       check_approval()

   Problems:
   1. Server ka process 3 GHANTE zinda rehna padega (manager lunch par hai)
   2. Server restart hua → SAB KHATAM. Poora plan gaya.
   3. 100 approvals pending? 100 process zinda? Server crash.
   4. Paisa (compute) barbaad

✅ interrupt() approach (sahi):
   1. State DATABASE me save
   2. Process BAND ho gaya (0 resource use)
   3. Manager 3 ghante baad "approve" bhejta hai
   4. State database se LOAD hui
   5. Graph WAHIN SE aage chala — kuch bhoola nahi
   6. Server 10 baar restart ho, koi farak nahi
```

**Real example — poora timeline:**
```
Mon 14:00 — Agent ne plan banaya, Strategy Card dikhaya
Mon 14:00 — interrupt() → state save → process khatam
            (state me: sab 40 fields, chat history, forecast, sab)
Mon 14:01 — Server par 0 load. Kuch nahi chal raha.
Mon 18:00 — Server maintenance ke liye restart hua
Tue 09:30 — David Moss ne dashboard par plan dekha
Tue 09:35 — David: "Approve" click kiya
Tue 09:35 — State database se load hui
Tue 09:35 — Graph Step 8 par chala: POST /api/strategies/
            → 19 ghante ka gap, phir bhi kuch nahi bhoola
```

### **"Budget is locked at this moment"** — kya matlab?

```
Mon 14:00 — Plan approve hone ke liye bheja. Budget: £10,000
Mon 15:00 — Trader ne socha "£12,000 kar dun"
            → NAHI KAR SAKTA. Plan locked hai.
Tue 09:35 — David ne £10,000 wale plan ko approve kiya

→ David ne EXACTLY jo dekha, wahi approve hua.
→ Agar budget badalna hai, plan wapas Step 4 par jaake naya
  approval chahiye.
```

**WHY?** Warna ye ho sakta:
```
Trader plan bhejta hai £5,000 ka (chhota, easily approve ho jaayega)
Manager approve karta hai
Trader budget £50,000 kar deta hai
→ £50,000 kharch ho gaya jo kisi ne approve nahi kiya!
→ FRAUD ka raasta
```

**Isliye lock.** Document ki line: *"nothing launches that a person hasn't approved."*

### **On rejection** — Step 4 par wapas
Document literally: *"On rejection: the flow returns to Step 4 (audiences) so the trader can adjust the plan."*

**WHY Step 4 (audiences), Step 1 nahi?**

```
Sochо: kya reject hone par sab kuch dobara poochhna chahiye?
  Naam? Nahi — wo theek tha
  Dates? Nahi — wo theek tha
  Market? Nahi — wo theek tha
  Deals? Shayad — par mostly theek

  AUDIENCE? ✅ HAAN — yahi mostly problem hoti hai
             (bahut chhoti, bahut badi, bahut mehngi)

→ Isliye Step 4. Wahan se audience badlo → targeting →
  forecast → dobara approval
```

**Smart design:** Reject ka cost **kam** rakha. Sirf 4 steps dobara, 7 nahi.

### 🔧 Step 7 ke API calls
**Koi nahi.** Document literally: *"No API call — this is agent-internal."*

> **⚠ Par audit trail kahan store hoga?** Agar API call nahi hai, to `approved_by`, `approved_at` kahan save honge? LangGraph checkpointer me? Ya VOW database me?
>
> Document ne clear nahi kiya. **David ne yahan comment kiya ho sakta hai.**
>
> Tumhara jawab: *"State checkpointer me save hoti hai, jo LangGraph ka persistence layer hai. Par compliance ke liye VOW database me bhi ek audit record banana behtar hoga — main iske liye ek endpoint suggest karta hun."*

---

## 🟦 STEP 8: CREATE THE REAL STRATEGY
### 🔄 CHANGED — v1.1.0 me "Summary & Create" (Step 6) tha. **Key change: real strategy, not a draft**

### WHAT?
Steps 1–7 ka sab data ikattha karke `POST /api/strategies/` par bhejna — **asli** strategy banane ke liye.

### 📋 CHANGE TABLE (Document literally)

| Field | Change |
|---|---|
| **Endpoint** | 🔄 `POST /api/strategies/` — **not** `/strategies/draft/`. Client: *"don't need to create draft strategy; draft is just for the wizard creation"* |
| **Audience set** | ➕ Created at this step via the **simplified CTV endpoint** (not before forecasting) |
| **All slots** | All filled slots from Steps 1–7 are assembled into the creation payload |

### 🔴 Change 1: Draft endpoint ❌ REMOVED — WHY?

**Client ka quote:** *"don't need to create draft strategy; draft is just for the wizard creation"*

**Plain me samjho:**

```
UI WIZARD me draft kyun chahiye tha?
  Trader Step 3 par tha, achanak meeting aa gayi
  → "Save as draft" click kiya
  → Kal wapas aaya, Step 3 se continue kiya
  → Isliye draft chahiye tha: ADHOORA KAAM BACHANE KE LIYE

AGENT me draft kyun NAHI chahiye?
  Agent ki state LANGGRAPH CHECKPOINTER me pehle se save hai!
  → Trader ne chat chhodi? State save hai.
  → Kal wapas aaya? Wahin se continue.
  → Draft ki ZAROORAT HI NAHI. Duplicate mechanism hai.
```

```
╔═════════════════════════════════════════════════════════════╗
║  UI WIZARD:  adhoora kaam → DRAFT strategy (database me)    ║
║  AGENT:      adhoora kaam → CHECKPOINTED STATE (LangGraph)  ║
║                                                             ║
║  → Dono ek hi kaam karte hain. Do rakhne ka faayda nahi.    ║
╚═════════════════════════════════════════════════════════════╝
```

**Aur ek gehri wajah:** Draft strategies **database me kachra** banati hain.
```
Trader ne 10 baar plan try kiya → 10 draft strategies database me
→ Kaunsi asli hai? Kaunsi kachra?
→ Reporting me confusion, cleanup ka kaam
```

**Agent me:** koi kachra nahi. Sirf **approve hua plan** database me jaata hai.

### 🔴 Change 2: Audience set YAHAN banti hai

Document: *"Created at this step via the simplified CTV endpoint (not before forecasting)"*

**Timeline dekho:**
```
Step 4: Audience SUGGEST hui (sirf memory me, database me nahi)
Step 6: Forecast hui (suggested audience ke saath, memory se)
        + Repair loop chala (audience 3 baar badli)
Step 7: Approval mili
Step 8: ✅ AB audience set DATABASE me BANTI hai
        (sirf FINAL, approved wali)
```

**WHY?** Part 5 Step 4 me detail me. Short: repair loop me audience kai baar badalti hai. Har baar create karte to 10 bekaar audience sets ban jaate.

**"Simplified CTV endpoint"** = ek chhota/aasan endpoint jo sirf CTV ke liye hai. (Poora audience-set creation endpoint bahut fields maangta hoga; CTV ke liye kam chahiye.)

> **⚠ Endpoint ka naam document me NAHI hai.** Sirf "simplified CTV endpoint" likha hai. **David ne comment kiya ho sakta hai.**

### 🔴 Change 3: All slots assemble hote hain

**Real example — poora payload (v1.1.0 se + v2.0 ke naye fields):**
```json
POST /api/strategies/
{
  "name": "Summer_Brand_Awareness_2026",
  "advertiser_id": "353eea43-bc42-456f-ba4f-3d3e20ea6bc8",
  "channel_type": "dsp",
  "goal": "AWARENESS",
  "kpi_target_type": "reach",
  "primary_currency": "GBP",
  "flight_dates": {
    "lower": "2026-08-01",
    "upper": "2026-08-31",
    "bounds": "[)"
  },
  "durations": ["30"],                        ← ➕ v2.0 NEW
  "product_location": "NOT_SOLD_ON_AMAZON",
  "product_asins": [],
  "formats": ["prime_video", "streaming_tv"],
  "product_categories": [1],
  "market_budgets": [
    {"market": "GB", "budget": "10000.00", "base_bid": "30.00"}
  ],
  "frequency_cap": 3,                         ← ➕ v2.0 NEW
  "ad_tag_conversions": ["Page view", "Checkout"],
  "selected_deals": ["EXT7P75718S8MNR"],
  "selected_audience_sets": ["aud_101", "aud_102"],
  "selected_creatives": [
    {
      "asset_id": "asset_99812",
      "click_through_url": "https://example.com/landing"
    }
  ]
}
```

**Response (v1.1.0 se):**
```json
201 Created
{
  "id": "VMA2026365",
  "name": "Summer_Brand_Awareness_2026",
  "status": "draft",              ← ⚠⚠ YAHAN DEKHO!
  "is_syncing": true,
  "created_at": "2026-07-27T17:55:00Z"
}
```

**`VMA2026365`** — VOW ka strategy ID format. Padho: VMA (prefix) + 2026 (saal) + 365 (sequence number).

**`201 Created`** = nayi cheez ban gayi (200 se alag — 200 sirf "data mil gaya").

---

### ⚠⚠ OPEN QUESTION #3 — Created strategy ka status kya hoga?

**Document literally (page 15):**
> *"⚠ Open question: what status does the created strategy land in? If it's still `"draft"` by default, activation via `set_status` remains a separate step. Confirm with client."*

**Ye ek ASLI contradiction hai. Dekho:**

```
Client ne kaha (Step 8):  "draft strategy ki zaroorat NAHI hai —
                           draft sirf wizard ke liye hai"
   ↓
To draft endpoint ❌ REMOVED kar diya
   ↓
Par API ka response deta hai:  "status": "draft"
                                          ↑ AB BHI DRAFT!
```

**Confusion samjho:**
- **"Draft endpoint"** = `POST /api/strategies/draft/` — ek **alag endpoint** jo adhoora data leta tha
- **"Draft status"** = `status: "draft"` — ek **field ki value** jo batati hai strategy abhi active nahi hai

**Ye do alag cheezein hain!** Client ne pehli hataane ko kaha, doosri ke baare me kuch nahi bola.

**To Step 8 ke baad status kya hoga?** Teen possibilities:

| Possibility | Matlab | Natija |
|---|---|---|
| **A: `"draft"`** | Purana behaviour hi rahega | Step 13 me `set_status` se `active` karna padega ✅ Ye theek hai |
| **B: `"created"`** | Naya status | Pydantic model me yahi hai! `status: str = Field("created")` |
| **C: `"paused"`** | Ban gayi par ruki hui | Bhi possible |

**Aur dekho — Pydantic model me contradiction hai:**
```python
# FullStrategySchema me:
status: str = Field("created", description="Strategy status")  # 🔄 CHANGED from "draft"
                    ↑ document ne "created" likha

# Par API response example me:
"status": "draft"
           ↑ v1.1.0 se copy hua, update nahi kiya
```

> 🎯 **David ne is par pakka comment kiya hoga.** Document apne aap se contradict kar raha hai.
>
> **Tumhara jawab:** *"Ye ek genuine ambiguity hai jo maine flag kiya. Do cheezein confuse ho rahi hain — 'draft endpoint' (hataya gaya) aur 'draft status' (ab bhi ho sakta hai). Mera recommendation: status `created` rakhein, aur Step 13 me `set_status` se `active` karein. Isse 'created but not spending' aur 'active and spending' ka farak saaf rahega. Par ye VOW backend team se confirm karna padega."*

### 🔧 Step 8 ke API calls
```
POST /api/strategies/
+ audience-set creation via simplified CTV endpoint (naam TBC)
```

---

## 🟦 STEP 9: UPLOAD VIDEO CREATIVE
### 🔄 CHANGED — v1.1.0 ka Step 5 "Creatives" tha. **Video only, approval ke baad, + duration check**

### WHAT?
Asli video file upload karna, aur check karna ki uski duration **approved plan se match** karti hai.

### WHY approval ke baad?

```
❌ Approval SE PEHLE creative:
   Trader video banata hai (agency ko £5,000 deta hai) →
   plan approve nahi hua → video BEKAAR

✅ Approval KE BAAD creative:
   Plan approve hua → ab confidence hai ki campaign chalega →
   TAB video banao/upload karo
```

**Purpose:** Trader ka paisa aur waqt bachana.

### 📋 FIELD MATRIX

| Field | Type | Requirement | Change |
|---|---|---|---|
| **Video file** | Upload (direct or URL) | **Required** | 🔄 CHANGED — *"For CTV, always video. No display creatives, no pre-approved selection, no responsive e-commerce"* |
| **Click-through URL** | URL | **Required** | ✅ Unchanged |
| **Duration** | **Derived from file** | **Checked** | ➕ NEW — *"Must match one of the durations in the approved plan"* |

### Ek-ek field

#### **Video file** — Upload (direct or URL)
```
"direct" = file computer se upload karo
"url"    = ek link do jahan se file download ho jaaye
```

**Pydantic me:** `upload_method: str = Field("direct", description="direct or url")`

#### **Click-through URL** — Required
Part 1.G me discuss kiya — CTV me click nahi hota, par field Required hai. **⚠ Ye ek gap hai.**

#### **Duration** — **Derived** from file
**"Derived"** = file se **khud nikala** jaata hai (trader nahi likhta).

```
Video file upload hui → system uski length padhta hai → 30 seconds
→ duration_seconds = 30
```

---

### 🔴 ➕ NEW: DURATION MATCH CHECK (Ye brilliant hai)

**Document literally:**
> *"➕ NEW — Duration match check: If the uploaded video is 30s but the approved plan specified 15s deals, **the economics change** (different CPM → different impressions for the same budget). This triggers **re-approval** (return to Step 7 with the amended plan)."*

**"Economics change"** = paise ka ganit badal jaata hai.
**"Amended plan"** = sudhara hua plan.

### Real example — poora scenario:

```
════════════════════════════════════════════════════════════════
APPROVED PLAN (Step 7 me David ne approve kiya):
  durations       = ["15"]
  Deal            = Prime Video 15s @ £20 CPM
  Budget          = £10,000
  Impressions     = 10,000 ÷ 20 × 1000 = 500,000
  Estimated reach = 310,000
  → David ne 500,000 impressions aur 310,000 reach APPROVE kiya

════════════════════════════════════════════════════════════════
STEP 9 — Trader video upload karta hai:
  File: BrightPath_Brand_30s.mp4
  System derives: duration_seconds = 30      ← 30, NOT 15!

════════════════════════════════════════════════════════════════
DURATION MATCH CHECK:
  approved durations = ["15"]
  uploaded duration  = 30
  → ❌ MISMATCH!

Agent recalculates:
  30s deal ka CPM = £28.88 (15s ka £20 tha)
  Impressions     = 10,000 ÷ 28.88 × 1000 = 346,260
  Reach           = ~215,000 (estimate)

════════════════════════════════════════════════════════════════
Agent ka message:
"⚠ Duration mismatch pakda.

 Approved plan me 15-second ka video tha. Tumne 30-second
 upload kiya. Isse plan ka ganit badal gaya:

 ┌────────────────┬──────────────┬──────────────┬──────────┐
 │                │ APPROVED     │ AB (30s)     │ FARAK    │
 ├────────────────┼──────────────┼──────────────┼──────────┤
 │ Duration       │ 15s          │ 30s          │          │
 │ CPM            │ £20.00       │ £28.88       │ +£8.88   │
 │ Impressions    │ 500,000      │ 346,260      │ -153,740 │
 │ Est. reach     │ 310,000      │ ~215,000     │ -95,000  │
 │ Budget         │ £10,000      │ £10,000      │ same     │
 └────────────────┴──────────────┴──────────────┴──────────┘

 Tumhe 153,740 KAM impressions milenge — same paise me.

 David ne 15-second wala plan approve kiya tha. Ye badla hua
 plan main automatically aage nahi badha sakta.

 Do options:
   A) 15-second ka video upload karo (approved plan ke hisaab se)
   B) Main badla hua plan David ko dobara approval ke liye bhejun

 Kya karna hai?"

════════════════════════════════════════════════════════════════
Trader: "B — dobara bhej do"
→ Flow Step 7 par WAPAS jaata hai (amended plan ke saath)
→ David ko naya plan dikhta hai, purane ke comparison ke saath
→ David approve kare to Step 8-9 phir se
```

### 🔴 WHY ye check itna important hai?

**Kyunki bina iske ye ho sakta:**
```
David: "£10,000 me 500,000 impressions? Approve!"
Trader: 30s video upload
Campaign chala → asli result: 346,000 impressions
David: "Tumne 500,000 bola tha!"
Trader: "Video 30s tha..."
David: "Mujhe kisne bataya?!"
→ Trust khatam. Aur ye kisi ki galti nahi thi — system ne
  batana chahiye tha.
```

**Ye check ek "silent failure" ko "loud failure" me badal deta hai.**
- **Silent failure** = galti hui, kisi ko pata nahi chala, baad me nateeja bura
- **Loud failure** = galti hui, turant pata chal gaya, theek kar liya

**Software design me loud failure hazaar guna behtar hai.**

### 🔧 Upload path (Document literally)
```
POST /api/assets/amz_assets/gen_upload_urls/   ← upload URLs lo
POST /api/assets/amz_assets/register/           ← asset Amazon par register karo
```

**Do calls kyun? — Ye ek standard pattern hai (pre-signed URL upload):**

```
1. POST /gen_upload_urls/
   → Server kehta hai: "Ye lo ek special URL. Isme seedha file daal do."
   ← {"upload_url": "https://s3.amazonaws.com/...?signature=xyz&expires=..."}

2. Tum file SEEDHA us URL par bhejte ho
   → File S3/storage me chali gayi. VOW ke server se guzri BHI NAHI.

3. POST /register/
   → "File upload ho gayi, ab isko Amazon par asset register kar do"
   ← {"asset_id": "asset_99812"}
```

**WHY ye pattern?**
```
❌ Seedha VOW server par upload:
   500 MB video → VOW server par → VOW server se S3 par
   → VOW server ka bandwidth barbaad
   → 500 MB memory me load
   → 10 log ek saath upload karein? Server crash

✅ Pre-signed URL:
   500 MB video → SEEDHA S3 par
   → VOW server ne sirf ek URL diya (2 KB ka response)
   → 1000 log upload karein? Koi farak nahi
```

**Pre-signed URL** = ek temporary URL jisme permission built-in hai. Thodi der baad expire ho jaata hai.

### ❌ REMOVED for CTV (Document literally)

| Kya hataya | Endpoint | Kyun |
|---|---|---|
| **Browse existing assets** | `GET /api/assets/` | CTV me naya video upload hota hai, purana browse nahi |
| **Pre-approved creatives** | `GET /api/creatives/` | CTV me har video ka **fresh platform approval** chahiye |
| **Responsive e-commerce** | `POST /api/creatives/recs/` | Ye **Display** ka format hai (product images auto-generate) |
| **Third-party tags** | `POST /api/creatives/third-party/` | Display ka format |

**"Responsive e-commerce creative"** = ek aisa Display ad jo **khud** product ki image, price, rating uthake banata hai. CTV video me ye possible nahi.

**"Third-party tag"** = doosri company ka ad code. Display me common, CTV me nahi.

**Document literally:** *"These are valid for Display but not for CTV scope."*

---

## 🟦 STEP 10: PLATFORM CREATIVE APPROVAL
### ➕ **ENTIRELY NEW** — v1.1.0 me tha hi nahi

### WHAT?
Har platform (Amazon, Netflix, Disney) **apna** review karta hai — video content aur technical quality check karta hai.

### 📋 FIELD MATRIX

| Field | Type | Requirement |
|---|---|---|
| **Amazon approval status** | Enum | Read-only |
| **Netflix approval status** | Enum | Read-only **(if Netflix inventory)** |
| **Disney approval status** | Enum | Read-only **(if Disney inventory)** |

**Values:** `PENDING` → `APPROVED` ya `REJECTED`

**"Read-only"** = agent/trader ise **set nahi** kar sakte, sirf **padh** sakte hain. Platform hi decide karta hai.

**"if Netflix inventory"** = ye field sirf **tab** dikhega jab plan me Netflix ho. Conditional field.

### 🔴 WHY teen alag statuses?

**Document literally:**
> *"Every video must pass the platform's content and technical review before it can run. **Each platform reviews its own inventory independently.** A plan can be **fully approved and funded and still not launch** until the creative clears."*

**"Independently"** = ek doosre se alag, apna faisla.

**Real example — mixed results:**
```
Same video, teen platforms par bheja:

Amazon:   ✅ APPROVED  (2 ghante me)
Netflix:  ⏳ PENDING   (48 ghante lagte hain)
Disney:   ❌ REJECTED  — "Audio levels exceed our -24 LKFS spec"

Nateeja: Amazon ka hissa (£6,000) chal sakta hai
         Netflix ka hissa (£3,000) intezaar me
         Disney ka hissa (£1,000) BLOCKED — naya video chahiye
```

**Ye ek complex reality hai jo v1.1.0 me miss ho gayi thi.**

### 🔴 "Fully approved and funded and still not launch" — samjho

```
Step 7:  Plan APPROVED ✅ (David ne kiya)
Step 12: Credit sufficient ✅ (paisa hai)
Step 10: Creative REJECTED ❌ (Disney ne mana kiya)

→ Sab kuch taiyar hai, par ad CHAL NAHI SAKTA.
```

**WHY?** Kyunki do **alag-alag** approval hain:
```
Plan approval    (Step 7)  = "Kya ye SPEND karna theek hai?"     → INTERNAL (David)
Creative approval (Step 10) = "Kya ye VIDEO hamare platform par
                               chal sakta hai?"                   → EXTERNAL (Netflix)
```

**Do alag log, do alag sawaal, do alag gates.**

### Content vs Technical review — kya check hota hai?

| Review type | Kya dekhte hain | Reject ke examples |
|---|---|---|
| **Content review** | Ad me kya dikh raha hai | Alcohol/tobacco, competitor ka naam, misleading claim, adult content, political content |
| **Technical review** | File ki quality | Resolution kam, audio level galat, file format wrong, duration mismatch, bitrate kam |

**Real reject reasons:**
```
Amazon:  "Creative contains a competitor brand logo at 0:18"
Netflix: "Video resolution 1280x720 below our 1920x1080 minimum"
Disney:  "Audio levels exceed -24 LKFS specification"
```

### **On rejection** — Step 9 par wapas
Document literally: *"On rejection: the agent reports the reason and asks for a replacement (return to Step 9)."*

**Real example:**
```
Agent: "❌ Disney+ ne creative reject kar diya.

        Wajah: 'Audio levels exceed our -24 LKFS specification'

        Matlab: tumhare video ka audio Disney ke standard se
        zyada tez hai. Isko -24 LKFS par normalize karna padega.

        Status:
          Amazon  ✅ APPROVED — £6,000 ka hissa chal sakta hai
          Netflix ⏳ PENDING  — 48 ghante lagenge
          Disney  ❌ REJECTED — naya file chahiye

        Kya karna hai?
          A) Audio theek karke naya file upload karo (Step 9)
          B) Disney+ ka hissa (£1,000) hata do, baaki chalao"
```

### ⚠⚠ OPEN QUESTION #4 — 3P approval status kahan se aayega?

**Document literally:**
> *"⚠ Open question: do Netflix/Disney review statuses surface inside VOW's API, or is that tracked externally? Confirm with client."*

**"Surface inside VOW's API"** = VOW ke API me dikhega ya nahi.

**Ye problem samjho:**

```
Agar VOW ke API me AATA hai:
  ✅ Agent poll kar sakta hai: GET /api/creatives/{id}/approval-status/
  ✅ Agent automatically pata kar lega jab approve ho
  ✅ Trader ko notify kar sakta hai
  ✅ Flow automatically aage badh sakta hai

Agar VOW ke API me NAHI aata (externally tracked):
  ❌ Agent ko PATA HI NAHI chalega
  ❌ Koi insaan Netflix ke dashboard par jaake dekhega
  ❌ Phir manually VOW me daalega
  ❌ Flow ATAK jaayega — agent intezaar me baitha rahega
  → Ye ek POORA naya manual workflow hai!
```

**Ye ek bada operational question hai.** Iska jawab poore Step 10 ka design badal deta hai.

> 🎯 **David ne is par comment kiya ho sakta hai.**
>
> **Tumhara jawab:** *"Maine ye flag kiya kyunki iska jawab Step 10 ka design decide karta hai. Agar VOW API me nahi aata, to humein ek manual-entry interface ya webhook chahiye hoga, aur agent ko 'waiting for external confirmation' state me rakhna padega. Ye M1 ke scope ko badha sakta hai — isliye ye pehle confirm karna zaroori hai."*

---

## 🟦 STEP 11: TRACKING SETUP
### 🔄 **MOVED** — ASIN validation Step 1 me tha, ad-tag conversions Step 2 me the. **Dono ab yahan.**

### WHAT?
Tracking ka intezaam — ASIN validate karna, ad tag check karna, conversion events chunna.

### WHY yahan move kiya?

**Sochne ka tarika:**
```
Step 1  = "PLAN kya hai?"          (naam, budget, dates, market)
Step 11 = "MEASUREMENT kaise hoga?" (ASIN, ad tag, conversions)

→ Ye do ALAG kaam hain. Alag steps me hone chahiye.
→ Aur trader ko planning ke waqt tracking ke sawaal se
  disturb nahi karna chahiye.
```

**Aur ek wajah:** Ad tag setup me **advertiser ke developer** ka kaam hai (website par code lagana). Wo planning ke waqt available nahi hoga. Isliye late me.

### 📋 FIELD MATRIX

| Field | Type | Requirement | Change |
|---|---|---|---|
| **Sells on Amazon?** | Question | Asked here | 🔄 **MOVED** from Step 1 |
| **Product ASINs** | Textarea | **Required if endemic** | ✅ Validation unchanged: `POST /api/contextual-targeting/{market}/asin-validation/` |
| **Sells on own website?** | Question | Asked here | ➕ **NEW explicit question** |
| **Ad tag registered?** | Check | **Required if yes** | ➕ **NEW** |
| **Ad tag conversions** | Multi-select | **Required if ad tag exists** | 🔄 **MOVED** from Step 2 |

### Ek-ek field

#### **Sells on Amazon?** — 🔄 MOVED from Step 1
Ye `product_location` ka sawaal hai. Jawab: `ON_AMAZON` ya `NOT_SOLD_ON_AMAZON`.

#### **Product ASINs** — Required if endemic
Part 5 Step 1 me detail me. Validation same.

#### **➕ Sells on own website?** — NEW EXPLICIT question

**"Explicit"** = saaf-saaf poochha gaya.

**WHY ye naya sawaal chahiye?** Kyunki `product_location` **do cheezein confuse** karta hai:

```
product_location = "NOT_SOLD_ON_AMAZON"
→ Matlab: Amazon par NAHI bechta
→ Par ye NAHI batata ki wo KAHAN bechta hai!

Possible cases:
  A) Apni website par bechta hai      → AD TAG chahiye
  B) Physical store me bechta hai      → ad tag possible NAHI
  C) Phone par order leta hai          → ad tag possible NAHI
  D) Sirf brand awareness chahta hai   → koi tracking nahi
     (koi product nahi bechta — jaise ek charity ya government ad)
```

**Isliye alag sawaal:** "Kya tum apni website par bechte ho?"
- **Haan** → ad tag ka raasta
- **Nahi** → tracking ka koi raasta nahi, aur ye theek hai

**Real example:**
```
Advertiser: UK Government road safety campaign
product_location = "NOT_SOLD_ON_AMAZON"  (kuch bechte hi nahi)
sells_on_own_site = false                 (website hai par bechte nahi)
→ Koi ad tag nahi, koi ASIN nahi
→ Sirf reach/frequency naapenge

Agar ye sawaal na hota, agent zabardasti ad tag maangta —
jo ismein possible hi nahi hai.
```

**Purpose:** Agent galat sawaal na poochhe.

#### **➕ Ad tag registered?** — NEW CHECK

**Document literally:**
> *"➕ NEW. Check whether an ad tag is already registered. If not, show setup instructions — **the tag must be installed before the campaign runs (tracking only records activity after it goes live)**."*

### 🔴 Ye document ki SABSE ZAROORI operational warning hai

```
╔════════════════════════════════════════════════════════════════╗
║  AD TAG PEHLE LAGANA PADEGA.                                   ║
║  Baad me lagaya → jo pehle hua wo HAMESHA KE LIYE GAYA.        ║
║  Peeche ka data recover NAHI hota.                             ║
╚════════════════════════════════════════════════════════════════╝
```

**Real example — disaster scenario:**
```
1 Aug   — Campaign activate hua, ad chalne laga
1-14 Aug — 200,000 impressions gaye. 800 log website par aaye.
           40 logon ne enroll kiya.
           ❌ AD TAG NAHI LAGA THA → KUCH RECORD NAHI HUA

15 Aug  — Advertiser: "Report do"
          Trader: "Conversions: 0"
          Advertiser: "0?! Kuch nahi hua?"
          Trader: "Nahi... tag hi nahi laga tha..."

16 Aug  — Tag laga diya
16-31 Aug — 45 conversions record hue

Final report: 45 conversions (asal me ~85 the)
→ Aadha data HAMESHA KE LIYE GAYA. ROAS galat. Optimisation galat.
→ Aur ye batana hi mushkil hai ki kitna miss hua.
```

**Isliye agent CHECK karta hai:**
```
Agent: "Tumne bataya ki brightpath.co.uk par bechte ho.
        Main check kar raha hun ki ad tag registered hai...

        ❌ Koi ad tag nahi mila.

        ⚠ ZAROORI: Ad tag campaign shuru hone SE PEHLE lagana
        padega. Tracking sirf tag lagne ke BAAD ka data record
        karti hai — peeche ka data recover nahi hota.

        Setup instructions:
        1. Ye code apni website ke <head> me daalo:
           <script src="https://s.amazon-adsystem.com/..."></script>
        2. Checkout page par ye event fire karo:
           amzn('trackEvent', 'Checkout')
        3. Ho jaane par mujhe batao, main verify kar dunga.

        Ya: tum bina conversion tracking ke bhi chala sakte ho —
        par phir sirf reach/frequency naap paoge, ROI nahi."
```

**Purpose:** Ek irreversible (jise wapas nahi kar sakte) galti rokna.

#### **Ad tag conversions** — 🔄 MOVED from Step 2

**Events (Document literally):** `Page view`, `Add to cart`, `Checkout`, `Application`
**API:** `GET /api/conversions/definitions/`

**Kya define karti hai:** Website par **kaunse kaam** track karne hain.

**Real example — funnel banake:**
```
BrightPath ke liye:
  ✅ Page view  → "kitne log course page par aaye?"      → 800
  ✅ Application → "kitne logon ne apply form bhara?"     → 120
  ✅ Checkout   → "kitne logon ne payment kiya?"          → 45
  ⬜ Add to cart → (BrightPath me cart nahi hai)

→ Funnel: 800 aaye → 120 ne apply kiya → 45 ne pay kiya
→ Conversion rate: 45/800 = 5.6%
```

**WHY multiple events?** Kyunki poora funnel dikhta hai. Agar 800 aaye par sirf 5 ne apply kiya, to problem **website par** hai, ad par nahi. Ye insight sirf multi-event tracking se milti hai.

### 🔧 Step 11 ke API calls
```
POST /api/contextual-targeting/{market}/asin-validation/
GET  /api/conversions/definitions/
```

### ⚠⚠ OPEN QUESTION #1 (REPEATED) — ASIN ka timing conflict

**Document literally (page 18):**
> *"⚠ Open question (repeated from Step 1): since `product_location` and `asin_numbers` are fields in `POST /strategies/` (called at Step 8), they may need to be collected before Step 8 and only the ad-tag check moves here. Confirm with client."*

**Ye wahi question hai jo Step 1 me tha.** Poora analysis Part 5 Step 1 me diya hai (field #11).

**Short recap:**
```
Step 8  me POST /strategies/ chahiye:  product_location + product_asins
Step 11 me ye collect ho rahe hain     ← Step 8 KE BAAD!
→ TIMING CONFLICT
```

**Recommended fix:** ASIN aur `product_location` **Step 1 me hi rakho** (wo plan fields hain). Sirf **ad-tag check aur conversions** Step 11 me rakho (wo genuinely tracking hai).

> 🎯 **Ye document me DO BAAR flag hua hai. David ne pakka comment kiya hoga.** Ye tumhara sabse taiyar jawab hona chahiye.

---

## 🟦 STEP 12: CREDIT CHECK
### ➕ **ENTIRELY NEW** — v1.1.0 me tha hi nahi

**Document literally:**
> *"Credit is checked only at activation, not during planning. **Everything before this point is a costless plan.**"*

### WHAT?
Check karna ki account me **paisa hai ya nahi** — campaign chalane se pehle.

### 📋 FIELD MATRIX

| Field | Type | Requirement | Kya define karti hai |
|---|---|---|---|
| **Account balance** | Number | Read-only | Account me kitna paisa hai |
| **Strategy budget** | Number | Read-only | Campaign ko kitna chahiye |
| **Sufficient** | Boolean | **Derived** (balance ≥ budget) | Paisa kaafi hai ya nahi |

**"Derived"** = system khud calculate karta hai: `sufficient = (balance >= budget)`

### 🔴 WHY credit check yahan (Step 12), pehle nahi?

**Document ki line samjho:** *"Everything before this point is a costless plan."*

```
❌ Agar credit check Step 1 me hota:
   Trader: "Main ek plan banake dekhna chahta hun ki £50,000 me
            kya milega"
   Agent: "Tumhare account me £5,000 hai. Aage nahi badh sakte."
   Trader: "Arre main SIRF DEKHNA chahta tha! Kharch nahi kar raha!"
   → BEKAAR block. Trader ko plan banane se roka.

✅ Credit check Step 12 me:
   Trader poora plan banata hai, forecast dekhta hai, approval
   leta hai, creative upload karta hai — SAB FREE
   → Ab activate karne se pehle: "paisa hai?"
   → Nahi hai? "Top-up karo" → phir activate
```

**Purpose:** Planning **free** rakhna. Trader jitne plan chahe banaye, compare kare, seekhe.

### 🔴 Aur ek gehri wajah — Budget planning ke waqt pata nahi hota

```
Step 1: Trader ne £10,000 bola
Step 3: Budget split hua
Step 6: Forecast aaya — "£7,500 me hi 90% reach mil raha hai"
Step 7: Trader ne budget £7,500 kar diya, David ne approve kiya

→ AGAR credit check Step 1 me hota, £10,000 par check hota
→ Par asli zaroorat £7,500 nikli
→ To Step 1 ka check GALAT number par hota tha!

✅ Step 12 me check → FINAL, approved budget par check
```

### **If insufficient** — top-up

**Document literally:** *"If insufficient: prompt a top-up via `POST /api/credits/` or `POST /api/credits/stripe/`."*

**"Top-up"** = paisa daalna / recharge karna.
**Stripe** = ek payment gateway (card se paisa lene wali service).

**Do endpoints kyun?**
```
POST /api/credits/         → general credit add (bank transfer, invoice, manual)
POST /api/credits/stripe/   → card se turant payment
```

**Real example:**
```
Agent → GET /api/credits/summary/
     ← {"balance": "7500.00", "currency": "GBP"}

Strategy budget: £10,000
Balance: £7,500
Sufficient: FALSE

Agent: "⚠ Activate karne se pehle ek cheez.

        Account balance:  £ 7,500
        Strategy budget:  £10,000
        Kami:             £ 2,500

        Do options:
        A) £2,500 (ya zyada) top-up karo — main payment link
           bhej deta hun
        B) Budget £7,500 kar do — par dhyan do, isse forecast
           badlega (reach ~210,000 se ~168,000 ho jaayega) aur
           plan dobara approve karana padega

        Kya karna hai?"
```

**Dhyan do — agent ne option B ka consequence bhi bataya** (dobara approval chahiye). Ye consistent honesty hai.

### 🔧 Step 12 ka API call
```
GET /api/credits/summary/
```

---

## 🟦 STEP 13: ACTIVATE
### ➕ **ENTIRELY NEW** — v1.1.0 me implicit tha ("create strategy" me chhupa hua)

**Document literally:**
> *"**The single spend action in the entire flow. Everything before this was free.**"*

### WHAT?
Campaign ko **chalu** karna. Yahi wo ek jagah hai jahan **paisa kharch shuru** hota hai.

### 🔧 API call
```
POST /api/strategies/{id}/set_status/
```

**`set_status`** = status badalna. Yahan: `created`/`draft` → `active`

### 🔴 WHY ye ek alag step hai? Create se alag kyun?

**Ye document ka ek sabse important architectural insight hai:**

```
╔═══════════════════════════════════════════════════════════════╗
║  CREATE (Step 8)                                              ║
║  = Database me record banana                                  ║
║  = "Ye plan exist karta hai"                                  ║
║  = 💚 FREE. Kuch kharch nahi.                                 ║
║  = Delete kar sakte ho, badal sakte ho                        ║
╠═══════════════════════════════════════════════════════════════╣
║  ACTIVATE (Step 13)                                           ║
║  = Amazon DSP ko batana "chalu karo"                          ║
║  = "Ye plan CHAL raha hai"                                    ║
║  = 💰 PAISA. Kharch shuru.                                    ║
║  = Ab impressions khareede ja rahe hain                       ║
╚═══════════════════════════════════════════════════════════════╝
```

**Analogy — hotel booking:**
```
CREATE   = Booking form bhar diya, kamra select kiya (paisa nahi diya)
ACTIVATE = Card swipe kar diya (💰 paisa gaya)
```

**Aur analogy — flight:**
```
CREATE   = Seat select ki, passenger details bhare
ACTIVATE = "Pay Now" click kiya
```

### Real example — activate ka moment:
```
Agent: "Sab taiyar hai. Final confirmation:

        ┌───────────────────────────────────────────────────┐
        │ Strategy:     Summer_Brand_Awareness_2026          │
        │ ID:           VMA2026365                          │
        │ Budget:       £10,000                             │
        │ Flight:       1–30 Aug 2026                       │
        │ Market:       GB                                  │
        │ Plan approval:    ✅ David Moss, 29 Jul 09:35     │
        │ Creative approval: ✅ Amazon, ✅ Netflix           │
        │ Credit:           ✅ £12,000 available            │
        └───────────────────────────────────────────────────┘

        ⚠ ACTIVATE karne par KHARCH SHURU ho jaayega.
        Ye is poore flow ka pehla aur ek hi spend action hai.

        Confirm karun?"

Trader: "Haan"

Agent → POST /api/strategies/VMA2026365/set_status/
        {"status": "active"}
     ← 200 OK {"id": "VMA2026365", "status": "active", "is_syncing": true}

Agent: "✅ Campaign ACTIVE hai.

        VOW ka sync engine ab Amazon DSP par Campaigns aur Ad
        Groups bana raha hai (is_syncing: true). 10-15 minute
        lagenge. Uske baad delivery shuru hogi.

        Main tumhe notify karunga jab pehle impressions aayenge."
```

### 🔴 Activation ke baad kya hota hai?

**Document literally (page 19):**
> *"After activation, VOW's outbound sync creates the Campaigns and Ad Groups on Amazon DSP."*

**Poora picture:**
```
VOW me:                    Amazon DSP par:
─────────────              ─────────────────
Strategy VMA2026365   →    Campaign "Summer_Brand_Awareness_2026"
                            ├── Ad Group: Prime Video 30s
                            │     ├── Deal: EXT7P75718S8MNR
                            │     ├── Audience: aud_101, aud_102
                            │     └── Creative: asset_99812
                            └── Ad Group: Netflix 30s
                                  ├── Deal: EXT8K93021MNPQ
                                  └── Creative: asset_99812
```

**Terms:**
- **Outbound sync** = bahar bhejne wali process (VOW → Amazon)
- **Campaign** = Amazon DSP ka top-level container
- **Ad Group** = Campaign ke andar ek group (ek deal + ek audience + ek creative ka combo)
- **`is_syncing: true`** = "abhi bheja ja raha hai, ruko"

**WHY ek Strategy → kai Ad Groups?**
```
Kyunki har deal+audience+creative ka combo ALAG Ad Group hota hai.
Isse Amazon DSP me har combo ka ALAG performance dikhta hai.
→ "Prime 30s ne 200K impressions diye, Netflix 30s ne 90K"
```

---

## 🎯 5.14 — Poore Flow ka Ek Nazar me Naksha

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                        13-STEP CTV AGENTIC FLOW                                ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  💚 FREE ZONE — Steps 1–12                                                    ║
║  ─────────────────────────────────────────────────────────────────────────    ║
║                                                                                ║
║  1. BASICS               naam, dates, market, currency, DURATIONS,            ║
║                          goal(fixed AWARENESS), KPI, formats,                 ║
║                          categories, selling loc, budget, bid,                ║
║                          freq cap, budget cap                                 ║
║      │                   🔧 name-uniqueness, product-categories               ║
║      ▼                                                                        ║
║  2. CTV INVENTORY        deals + 🔴 TIER FORK + rate card                     ║
║      │                   ├─ AMAZON_OWNED (Prime) ────── forecast ✅            ║
║      │                   ├─ 3P_PRECURATED (Netflix) ─── forecast ❌           ║
║      │                   └─ 3P_NEEDS_CURATION (Disney) ─ capture reqs 📝      ║
║      │                   + genre upsell logic                                 ║
║      │                   🔧 deals, filter-properties, rates/ctv               ║
║      ▼                                                                        ║
║  3. BUDGET SPLIT ➕      inventories + durations me baanto                     ║
║      │                   EVEN_BY_BUDGET / EVEN_BY_IMPRESSIONS / CUSTOM        ║
║      │                   ⚠ agent apni assumption BATATA hai                   ║
║      │                   🔧 koi API nahi — agent-side logic                    ║
║      ▼                                                                        ║
║  4. AUDIENCES            🔴 MANDATORY + suggestion-driven (pgvector)          ║
║      │                   3 options: NARROW / BALANCED / WIDE                  ║
║      │                   + effective CPM (deal + VCPM) ➕                      ║
║      │                   + matching mode (Similar/Exact)                      ║
║      │                   🔧 POST suggest/ → GET suggest/{id}/                  ║
║      ▼                                                                        ║
║  5. TARGETING ➕         location, instream position, content exclusions,      ║
║      │                   device type, mobile env — SAB OPTIONAL               ║
║      │                   ⚠ config-driven hona chahiye (hard-coded nahi)        ║
║      │                   🔧 contextual-targeting/products, locations           ║
║      ▼                                                                        ║
║  6. PREDICT REACH        🔴 HONESTY RULE                                       ║
║      │                   Amazon  → reach ✅ frequency ✅ curve ✅               ║
║      │                   3P      → CPM + impressions ONLY                     ║
║      │                   ⚠ total reach ADD NAHI kar sakte                      ║
║      │  ┌──────────────  🔁 REPAIR LOOP (sirf Amazon portion)                  ║
║      │  │                1. audience EXTEND karo (profile switch nahi)         ║
║      │  │                2. base bid badhao (£15→£30)                         ║
║      │  └───────────────►3. dobara forecast                                    ║
║      │                   🔧 audience-sets/reach-forecast/                      ║
║      ▼                                                                        ║
║  7. ⏸️  PLAN APPROVAL ➕  LangGraph interrupt() — GRAPH RUK JAATA HAI          ║
║      │                   state persist hoti hai · budget LOCK hota hai        ║
║      │                   PENDING → APPROVED / REJECTED                        ║
║      │                   approved_by, approved_at (audit trail)               ║
║      │                   optionally manager (budget threshold?)               ║
║      │  ◄─── REJECT ───► wapas Step 4 (audiences)                             ║
║      │                   🔧 koi API nahi — agent-internal                      ║
║      ▼                                                                        ║
║  8. CREATE STRATEGY      🔄 POST /api/strategies/ — REAL, not draft            ║
║      │                   ❌ /strategies/draft/ REMOVED                         ║
║      │                   + audience set YAHAN banti hai (simplified CTV)      ║
║      │                   ⚠ status kya hoga? OPEN QUESTION                      ║
║      ▼                                                                        ║
║  9. UPLOAD CREATIVE      video only (direct ya URL) + click-through URL       ║
║      │                   ➕ DURATION MATCH CHECK                               ║
║      │  ◄─ MISMATCH ───► wapas Step 7 (re-approval, amended plan)             ║
║      │                   🔧 gen_upload_urls/ → register/                       ║
║      ▼                                                                        ║
║ 10. PLATFORM APPROVAL ➕ Amazon / Netflix / Disney — SAB ALAG review           ║
║      │                   content + technical                                  ║
║      │  ◄─ REJECT ────► wapas Step 9 (naya video)                             ║
║      │                   ⚠ 3P status VOW API me aata hai? OPEN QUESTION        ║
║      ▼                                                                        ║
║ 11. TRACKING SETUP 🔄    sells on Amazon? → ASIN (required if endemic)        ║
║      │                   sells on own site? ➕ → ad tag registered? ➕         ║
║      │                   → ad tag conversions 🔄 (from Step 2)                ║
║      │                   ⚠⚠ TIMING CONFLICT with Step 8 — OPEN QUESTION        ║
║      │                   🔧 asin-validation/, conversions/definitions/         ║
║      ▼                                                                        ║
║ 12. CREDIT CHECK ➕      balance vs budget → sufficient?                       ║
║      │                   insufficient → top-up (credits/ ya credits/stripe/)  ║
║      │                   🔧 GET /api/credits/summary/                          ║
║      ▼                                                                        ║
║  ══════════════════════════════════════════════════════════════════════       ║
║  💰 SPEND ZONE — Step 13                                                      ║
║  ══════════════════════════════════════════════════════════════════════       ║
║                                                                                ║
║ 13. ACTIVATE ➕          🔴 THE SINGLE SPEND ACTION                            ║
║                          🔧 POST /api/strategies/{id}/set_status/              ║
║                          → outbound sync → Amazon DSP Campaigns + Ad Groups   ║
║                                                                                ║
║  ═══════════════════════════ DONE ════════════════════════════════════        ║
║                                                                                ║
║  📞 Q&A SIDE PATH (kabhi bhi, kisi bhi step par):                              ║
║     Trader: "Netflix 30s ka CPM kya hai?"                                     ║
║     Agent → rate card se jawab → wahin se aage chala                          ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
```

### 3 Loops + 1 Interrupt — yaad rakho

| # | Loop | Kahan se kahan | Trigger |
|---|---|---|---|
| 1 | **Repair loop** | Step 6 → Step 6 (apne andar) | Reach 0 ya insufficient |
| 2 | **Plan rejection** | Step 7 → **Step 4** | Manager ne reject kiya |
| 3 | **Duration mismatch** | Step 9 → **Step 7** | Video duration ≠ approved duration |
| 4 | **Creative rejection** | Step 10 → **Step 9** | Platform ne video reject kiya |
| 5 | **Credit insufficient** | Step 12 → Step 12 (top-up ke baad) | Balance < budget |
| ⏸️ | **Interrupt** | Step 7 (aur Step 10?) | Human ka intezaar |

---

# PART 6 — SECTION 4: API CATALOGUE
### 🔄 CHANGED — original catalogue kept, with additions and removals marked

## 6.1 — Poora Endpoint Table (24 endpoints)

### ✅ UNCHANGED (14 endpoints — Kareem ke original)

| # | Operation | Method | Endpoint | Kya karta hai | Kis step me |
|---|---|---|---|---|---|
| 1 | Check name uniqueness | `GET` | `/api/strategies/check_strategy_name_uniqueness/` | Naam pehle se hai ya nahi | **1** |
| 2 | ASIN validation | `POST` | `/api/contextual-targeting/{market}/asin-validation/` | ASIN sahi hai ya nahi | **11** |
| 3 | Product categories | `GET` | `/api/contextual-targeting/{market}/product-categories/` | Category ki list | **1** |
| 4 | Conversion definitions | `GET` | `/api/conversions/definitions/` | Ad tag events ki list | **11** |
| 5 | List deals | `GET` | `/api/deals/` | Available deals | **2** |
| 6 | Deal filter properties | `GET` | `/api/deals/filter-properties/` | Filter options (ad length, genre, deal type) | **2** |
| 7 | List audience sets | `GET` | `/api/audience-sets/` | Audience sets ki list | *(ab use nahi — suggest hi use hota hai)* |
| 8 | Suggest audiences | `POST` | `/api/audience-sets/suggest/` | 🔴 pgvector se audience suggest | **4** |
| 9 | Audience reach forecast | `POST` | `/api/audience-sets/reach-forecast/` | Audience ka reach forecast | **6** |
| 10 | Strategy reach forecast | `POST` | `/api/strategies/reach-forecast/` | Poori strategy ka forecast | **6** |
| 11 | List assets | `GET` | `/api/assets/` | Registered assets | ❌ *CTV me removed* |
| 12 | List creatives | `GET` | `/api/creatives/` | Approved creatives | ❌ *CTV me removed* |
| 13 | Create strategy | `POST` | `/api/strategies/` | 🔴 Strategy banana | **8** |
| 14 | Read strategy | `GET` | `/api/strategies/{id}/` | Strategy padhna | *(reporting)* |

### ➕ NEW (9 endpoints — v2.0 me joda gaya)

| # | Operation | Method | Endpoint | Kya karta hai | Kis step me |
|---|---|---|---|---|---|
| 15 | **CTV rate card** | `GET` | `/api/rates/ctv/{market}/` | Channels, durations, CPMs ki list | **2** + Q&A |
| 16 | **Inventory sources** | `GET` | `/api/inventory-sources/` | Inventory providers (tier mapping?) | **2** |
| 17 | **Activate strategy** | `POST` | `/api/strategies/{id}/set_status/` | 🔴 Campaign chalu karna | **13** |
| 18 | **Credit summary** | `GET` | `/api/credits/summary/` | Balance check | **12** |
| 19 | **Upload URLs** | `POST` | `/api/assets/amz_assets/gen_upload_urls/` | Upload ke liye pre-signed URL | **9** |
| 20 | **Register asset** | `POST` | `/api/assets/amz_assets/register/` | Asset Amazon par register | **9** |
| 21 | **Locations** | `GET` | `/api/strategies/locations/{market}/` | Desh ke andar ki locations | **5** |
| 22 | **Products (targeting)** | `POST` | `/api/contextual-targeting/{market}/products/` | Contextual product targeting | **5** |
| 23 | **Credits top-up** | `POST` | `/api/credits/` , `/api/credits/stripe/` | Paisa daalna | **12** |

### ❌ REMOVED (1 endpoint)

| Operation | Method | Endpoint | Kyun hataya |
|---|---|---|---|
| **Draft create** | `POST` | `/api/strategies/draft/` | Client: *"draft is just for the wizard"* |

---

## 6.2 — Zaroori Endpoints ka Poora Detail (Payload + Response)

### 🔹 1. Check Strategy Name Uniqueness

**Kaam:** Naam pehle se exist karta hai ya nahi.

```http
GET /api/strategies/check_strategy_name_uniqueness/?name=Summer_Brand_Awareness_2026
```
```json
200 OK
{
  "is_unique": true,
  "name": "Summer_Brand_Awareness_2026"
}
```

**Agent ka use:**
```
is_unique: true  → aage badho
is_unique: false → "Ye naam pehle se hai. 'Summer_Brand_Awareness_2026_v2' rakh dun?"
```

**Document ka protocol (Section 7.2, ✅ UNCHANGED):**
> *"Duplicate Name: If `check_strategy_name_uniqueness` returns `false`, append timestamp or suffix e.g. `Name_v2` and prompt user."*

**Dhyan do:** "**and prompt user**" — agent khud se naam nahi badalta, **poochhta** hai. Kyunki naam trader ki pehchaan hai — silently badalna bura hai.

---

### 🔹 2. ASIN Validation

**Kaam:** ASIN Amazon catalogue me exist karta hai ya nahi.

```http
POST /api/contextual-targeting/GB/asin-validation/
```
```json
{
  "asins": ["B08N5WRWNW", "B09B3H5F2C"]
}
```
```json
200 OK
{
  "valid_asins": [
    {
      "asin": "B08N5WRWNW",
      "title": "Wireless Noise Cancelling Headphones",
      "brand": "AudioBrand",
      "image_url": "https://m.media-amazon.com/images/I/sample.jpg",
      "product_category": "Electronics"
    }
  ],
  "invalid_asins": []
}
```

**🔴 Dhyan do — response me `product_category` bhi aata hai!**

**Ye ek zabardast insight hai:**
```
ASIN validate kiya → product_category MUFT me mil gayi
→ Step 1 ka "product_categories" field AUTO-FILL ho sakta hai!
→ Trader se poochhne ki zaroorat nahi

Ye ek AUR wajah hai ASIN ko Step 1 me rakhne ki
(Open Question #1 ka jawab!)
```

**Document ka protocol:**
> *"Invalid ASIN: If `asin-validation` flags an invalid ASIN, highlight the exact ASIN to the user and request correction."*

**"Highlight the exact ASIN"** = saaf batao **kaunsa** galat hai, sirf "error" nahi.

```
❌ Bura: "Kuch ASINs invalid hain"
✅ Accha: "B09B3H5F2C nahi mila. B08N5WRWNW theek hai (Wireless
          Noise Cancelling Headphones, AudioBrand). Galat wale ko
          check karke dobara bhejo?"
```

---

### 🔹 3. Audience Suggestion Engine (🔴 Sabse important)

**Kaam:** Brief se pgvector search karke 3 bundles banana.

```http
POST /api/audience-sets/suggest/
```
```json
{
  "market": "GB",
  "goal": "AWARENESS",
  "product_categories": ["Education"],
  "brief_text": "Driving high awareness for online learning platforms in UK"
}
```
```json
200 OK
{
  "bundles": {
    "narrow": [
      {"id": "aud_101", "name": "Higher Education Seekers",
       "vcpm": "1.85", "estimated_reach": 450000}
    ],
    "balanced": [
      {"id": "aud_101", "name": "Higher Education Seekers",
       "vcpm": "1.85", "estimated_reach": 450000},
      {"id": "aud_102", "name": "E-Learning & Tech Enthusiasts",
       "vcpm": "1.63", "estimated_reach": 1200000}
    ],
    "broad": [
      {"id": "aud_101", ...},
      {"id": "aud_102", ...},
      {"id": "aud_103", "name": "General Career Advancement",
       "vcpm": "1.20", "estimated_reach": 3500000}
    ]
  }
}
```

### 🔴 Payload ke 4 fields — har ek ka role

| Field | Kya karta hai | Kyun chahiye |
|---|---|---|
| `market` | Desh filter | GB ki audiences chahiye, US ki nahi |
| `goal` | Goal filter | AWARENESS ke liye broad segments, CONVERSION ke liye high-intent |
| `product_categories` | Category hint | Education → education-related segments |
| **`brief_text`** | 🔴 **Vector search ka input** | Yahi wo text hai jo embedding banta hai |

**`brief_text` sabse important hai.** Yahi pgvector ka asli input hai.

**Real example — brief_text ka asar:**
```
brief_text: "Driving high awareness for online learning platforms in UK"
→ Embedding bana → 3,400 segments se compare
→ Top matches:
   "Higher Education Seekers"      (semantic match: education + seeking)
   "E-Learning & Tech Enthusiasts" (semantic match: online learning)
   "General Career Advancement"    (semantic match: skill development)

Dhyan do: "online learning" ye keyword kisi bhi segment ke NAAM me nahi hai!
Par MATLAB match kar gaya. Yahi vector search ki taqat hai.
```

**Aur ye bhi dekho — VCPM aur reach ka pattern:**
```
Higher Education Seekers      VCPM £1.85   reach   450,000  ← specific, mehnga
E-Learning & Tech Enthusiasts VCPM £1.63   reach 1,200,000  ← medium
General Career Advancement    VCPM £1.20   reach 3,500,000  ← general, sasta

→ Jitna specific, utna mehnga aur chhota
→ Jitna general, utna sasta aur bada
```

### ⚠ Ye response shape ek OPEN QUESTION hai
Part 5 Step 4 me poora detail. Short: asli API flat list de sakta hai, grouping hum karenge.

---

### 🔹 4. Strategy Reach & Frequency Forecast

**Kaam:** Poori strategy ka forecast + reach curve.

```http
POST /api/strategies/reach-forecast/
```
```json
{
  "markets": ["GB"],
  "budget": "10000.00",
  "base_bid": "30.00",
  "formats": ["prime_video"],
  "audience_set_ids": ["aud_101", "aud_102"],
  "flight_dates": {
    "lower": "2026-08-01",
    "upper": "2026-08-31"
  }
}
```
```json
200 OK
{
  "estimated_impressions": 333333,
  "estimated_unique_reach": 210000,
  "average_frequency": 1.58,
  "indicative_cpm": "30.00",
  "reach_curve": [
    {"budget": 2500,  "reach": 65000},
    {"budget": 5000,  "reach": 120000},
    {"budget": 7500,  "reach": 170000},
    {"budget": 10000, "reach": 210000}
  ]
}
```

**Poora ganit verify karo:**
```
budget ÷ CPM × 1000 = 10,000 ÷ 30 × 1000 = 333,333 ✅ matches
impressions ÷ reach = 333,333 ÷ 210,000  = 1.587    ✅ matches 1.58
```

### 🔴 v2.0 ka change — `is_available` flag

v2.0 ne is response me ek naya field joda (Pydantic model me):
```python
class ForecastResultSchema(BaseModel):
    is_available: bool           # ➕ NEW — False for Netflix/Disney
    estimated_impressions: Optional[int] = None
    estimated_unique_reach: Optional[int] = None    # Only for Amazon
    average_frequency: Optional[float] = None       # Only for Amazon
    indicative_cpm: Optional[str] = None
    reach_curve: Optional[list[dict]] = None        # Amazon only
```

**Dhyan do — sab `Optional` ban gaye!** Kyunki 3P inventory me ye fields **khaali** rahenge.

**Netflix ke liye response aisa hoga:**
```json
{
  "is_available": false,          ← 🔴 KEY FLAG
  "estimated_impressions": 93750,  ← ganit se, ye mil gaya
  "estimated_unique_reach": null,  ← ❌ nahi hai
  "average_frequency": null,       ← ❌ nahi hai
  "indicative_cpm": "32.00",       ← rate card se
  "reach_curve": null              ← ❌ nahi hai
}
```

**`is_available: false` dekhkar agent samajh jaata hai** ki honesty rule lagana hai.

---

### 🔹 5. Full Strategy Creation

Poora payload aur response Part 5 Step 8 me diya hai.

**Ek baat dohrao — `channel_type`:**
```python
class ChannelTypeEnum(str, Enum):
    DSP = "dsp"
    SPONSORED = "sponsored"
```

**"Sponsored"** = Amazon Sponsored Products/Brands (search ads, Amazon ke andar). DSP se bilkul alag product.

**CTV ke liye hamesha `dsp`.** `sponsored` future ke liye hai.

---

### 🔹 6. Activate Strategy (➕ NEW)

```http
POST /api/strategies/VMA2026365/set_status/
```
```json
{"status": "active"}
```
```json
200 OK
{
  "id": "VMA2026365",
  "status": "active",
  "is_syncing": true
}
```

**Status ki possible values (Pydantic se):** `draft | active | paused`
**Par v2.0 me:** `created` bhi ho sakta hai (⚠ Open Question #3)

---

### 🔹 7. Credit Summary (➕ NEW)

```http
GET /api/credits/summary/
```
```json
200 OK
{
  "balance": "12500.00",
  "currency": "GBP",
  "pending_charges": "0.00"
}
```
*(Response shape document me nahi hai — ye mera anumaan hai. ⚠ Document ne isko specify nahi kiya.)*

---

### 🔹 8. Asset Upload (➕ NEW, 2 calls)

```http
POST /api/assets/amz_assets/gen_upload_urls/
```
```json
{"filename": "BrightPath_Brand_30s.mp4", "content_type": "video/mp4"}
```
```json
{"upload_url": "https://s3.../?X-Amz-Signature=...", "expires_in": 3600}
```

Phir file **seedha** us URL par PUT karo, phir:

```http
POST /api/assets/amz_assets/register/
```
```json
{"upload_key": "uploads/abc123.mp4", "name": "BrightPath_Brand_30s"}
```
```json
{"asset_id": "asset_99812", "duration_seconds": 30}
```

**Dhyan do — `duration_seconds` register response me aata hai.** Yahi se duration match check hota hai!

*(Ye payloads document me nahi hain — sirf endpoint names hain. ⚠ David ne comment kiya ho sakta hai: "in endpoints ka contract kahan hai?")*

---

## 6.3 — ⚠ API Catalogue ke Gaps (David ke comments ki tayyari)

| # | Gap | Detail |
|---|---|---|
| 1 | **9 naye endpoints, koi payload/response spec nahi** | v1.1.0 ne 5 endpoints ke poore examples diye the. v2.0 ke 9 naye endpoints me sirf **naam** hai. Contract adhoora hai. |
| 2 | **Simplified CTV audience-set endpoint ka naam nahi** | Step 8 me use hota hai, par catalogue me hai hi nahi! |
| 3 | **Do reach-forecast endpoints** | `/api/audience-sets/reach-forecast/` aur `/api/strategies/reach-forecast/` — kaunsa kab? Document ne "or the simplified CTV endpoint, name TBC" bhi likha — teesra option! |
| 4 | **`GET /api/inventory-sources/` ka use kahin nahi likha** | Endpoint list me ➕ NEW hai, par kisi step me mention nahi. Tier derivation ke liye hai? |
| 5 | **`GET /api/audience-sets/` ab bekaar hai** | ✅ Unchanged mark hai, par Step 4 kehta hai "Nobody browses". To ye endpoint kyun list me hai? |
| 6 | **`GET /api/assets/` aur `GET /api/creatives/`** | Catalogue me ✅ Unchanged, par Step 9 me ❌ REMOVED. **Direct contradiction!** |
| 7 | **Approval ke liye koi endpoint nahi** | Step 7 kehta hai "No API call". To audit trail kahan store hoga? |
| 8 | **Credit top-up ke do endpoints, farak nahi bataya** | `/api/credits/` vs `/api/credits/stripe/` |

> 🎯 **Gap #6 sabse strong comment-worthy hai** — catalogue aur step section **ek doosre se contradict** kar rahe hain. Ye ek asli editorial galti hai.

---

# PART 7 — SECTION 5: PYDANTIC DATA MODELS
### 🔄 CHANGED — original models kept where valid, extended and restructured

## 7.1 — Pehle: Pydantic ka Recap

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(...)                    # REQUIRED (... = zaroori)
    age: int = Field(...)                     # REQUIRED
    city: str = Field("London")               # default "London"
    notes: Optional[str] = Field(None)        # OPTIONAL

Person(name="Rahul", age=25)
# → name="Rahul", age=25, city="London", notes=None ✅

Person(name="Rahul", age="paach")
# → ❌ ValidationError: age must be an integer
```

**3 patterns yaad rakho:**
| Pattern | Matlab |
|---|---|
| `Field(...)` | **REQUIRED** — dena hi padega |
| `Field("GBP")` | Default value hai |
| `Optional[X] = Field(None)` | **OPTIONAL** — khaali reh sakta hai |
| `Field(default_factory=list)` | Default khaali list `[]` |

**`description=`** = documentation. Code chalane par asar nahi, par API docs me dikhta hai.

---

## 7.2 — ENUMS (Fix choices ki lists)

### ✅ UNCHANGED Enums (3)

```python
class ChannelTypeEnum(str, Enum):
    """✅ UNCHANGED"""
    DSP = "dsp"
    SPONSORED = "sponsored"
```
**Matlab:** DSP (programmatic display/video) ya Sponsored (Amazon search ads). CTV = `dsp`.

```python
class ProductLocationEnum(str, Enum):
    """✅ UNCHANGED"""
    ON_AMAZON = "ON_AMAZON"
    NOT_SOLD_ON_AMAZON = "NOT_SOLD_ON_AMAZON"
```
**Matlab:** Endemic ya Non-endemic. Poora explanation Part 4.1 me.

```python
class CurrencyEnum(str, Enum):
    """✅ UNCHANGED"""
    EUR = "EUR"
    GBP = "GBP"
    USD = "USD"
```

---

### 🔄 CHANGED Enums (3) — values same, par scope chhota

```python
class GoalEnum(str, Enum):
    """🔄 CHANGED — kept all values, but for CTV M1 only AWARENESS is used"""
    AWARENESS = "AWARENESS"
    CONSIDERATION = "CONSIDERATION"   # future scope
    CONVERSION = "CONVERSION"         # future scope
```

```python
class KPIEnum(str, Enum):
    """🔄 CHANGED — kept all values, but for CTV M1 only reach and frequency"""
    REACH = "reach"
    FREQUENCY = "frequency"
    CTR = "ctr"        # future scope
    CPC = "cpc"        # future scope
    CPA = "cpa"        # future scope
    CPDPV = "cpdpv"    # future scope
```

```python
class FormatEnum(str, Enum):
    """🔄 CHANGED — kept all values, but for CTV M1 only streaming_tv and prime_video"""
    DISPLAY = "display"              # future scope
    ONLINE_VIDEO = "online_video"    # future scope
    STREAMING_TV = "streaming_tv"
    PRIME_VIDEO = "prime_video"
```

### 🔴 Ye "keep but comment" approach — accha ya bura?

**✅ Faayde:**
1. Future me kuch delete nahi karna padega, sirf comment hatana hai
2. Purana data (agar exist karta hai) break nahi hoga
3. Intent saaf hai — "ye future me aayega"

**❌ Nuksaan (⚠ David ne comment kiya ho sakta hai):**
1. **Comment code enforce nahi karta!** `goal="CONVERSION"` **validate ho jaayega** — kyunki enum me hai
2. Naya developer confuse hoga: "CONVERSION available hai? Use kar lun?"
3. Ek bug ka raasta khula hai

**Mera suggestion (tumhara jawab):**
```python
# Option A: Runtime validator lagao
from pydantic import field_validator

CTV_ALLOWED_GOALS = {GoalEnum.AWARENESS}

class Basics(BaseModel):
    goal: GoalEnum = GoalEnum.AWARENESS

    @field_validator("goal")
    @classmethod
    def ctv_goal_must_be_awareness(cls, v):
        if v not in CTV_ALLOWED_GOALS:
            raise ValueError(f"CTV M1 supports only AWARENESS, got {v}")
        return v

# Option B: Do enums — CTVGoalEnum (sirf AWARENESS) aur GoalEnum (sab)
```

**Isse comment ek asli rule ban jaata hai.**

---

### ➕ NEW Enums (5) — v2.0 ke naye concepts

```python
class DurationEnum(str, Enum):
    """➕ NEW — creative durations for CTV"""
    TEN = "10"
    FIFTEEN = "15"
    TWENTY = "20"
    THIRTY = "30"
```
**Kyun string, number nahi?** Kyunki API me string bheji jaati hai aur JSON me consistency rehti hai. (Aur `"10"` se sort karna aasan nahi hai — par yahan zaroorat nahi.)

```python
class InventoryTierEnum(str, Enum):
    """➕ NEW — the three inventory tiers driving the flow's primary fork"""
    AMAZON_OWNED = "AMAZON_OWNED"
    THIRD_PARTY_PRECURATED = "THIRD_PARTY_PRECURATED"
    THIRD_PARTY_NEEDS_CURATION = "THIRD_PARTY_NEEDS_CURATION"
```
**🔴 Ye document ka sabse important enum hai.** Poora explanation Part 4.3 me.

```python
class ApprovalStatusEnum(str, Enum):
    """➕ NEW — for plan approval and creative approval"""
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
```
**Dono jagah use hota hai** — plan approval (Step 7) aur creative approval (Step 10). Reuse accha hai.

```python
class BudgetSplitMethodEnum(str, Enum):
    """➕ NEW — how the budget is divided"""
    EVEN_BY_BUDGET = "EVEN_BY_BUDGET"
    EVEN_BY_IMPRESSIONS = "EVEN_BY_IMPRESSIONS"
    CUSTOM = "CUSTOM"
```
**Poora ganit Part 5 Step 3 me.**

```python
class AudienceProfileEnum(str, Enum):
    """➕ NEW — the three audience options"""
    NARROW = "NARROW"
    BALANCED = "BALANCED"
    WIDE = "WIDE"
```
> **⚠ Yahan `WIDE` hai — par API response example me `bundles.broad` hai. INCONSISTENCY.**
> Ye ek asli mismatch hai jo code me bug banega.

---

## 7.3 — COMPONENT SCHEMAS (chhote building blocks)

### **DateRangeSchema** — ✅ UNCHANGED
```python
class DateRangeSchema(BaseModel):
    """✅ UNCHANGED"""
    lower: str = Field(..., description="ISO date YYYY-MM-DD")
    upper: str = Field(..., description="ISO date YYYY-MM-DD")
    bounds: str = Field("[)", description="Interval boundary notation")
```

**Har field:**
- `lower` — shuru ki tareekh, **REQUIRED**
- `upper` — khatam ki tareekh, **REQUIRED**
- `bounds` — default `"[)"` (Part 1.J me poora explanation)

> **⚠ Design question:** `lower`/`upper` **string** hain, `date` nahi. Kyun?
> Kyunki JSON me date string hoti hai, aur Postgres ka range type isi format me leta hai.
> **Par nuksaan:** Pydantic date validate nahi karega! `lower="hello"` pass ho jaayega.
> **David ne yahan comment kiya ho sakta hai.** Fix: `lower: datetime.date`

---

### **MarketBudgetBidSchema** — ✅ UNCHANGED
```python
class MarketBudgetBidSchema(BaseModel):
    """✅ UNCHANGED"""
    market: str = Field(..., description="ISO country code")
    budget: str = Field(..., description="Total budget decimal string")
    base_bid: str = Field(..., description="Base CPM bid decimal string")
```

### 🔴 WHY budget "decimal string" hai, float nahi?

**Ye ek bahut important engineering decision hai:**

```python
# ❌ Float ka problem:
>>> 0.1 + 0.2
0.30000000000000004        ← paisa me ye DISASTER hai!

>>> 10000.00 * 3
30000.000000000004

# Paisa ke saath float NEVER use karo.

# ✅ String/Decimal safe hai:
budget = "10000.00"
Decimal(budget) * 3 = Decimal("30000.00")   ← exact
```

**Real disaster example:**
```
1 million impressions ka calculation float me:
Expected: £30,000.00
Actual:   £29,999.99999999997
→ Reporting me mismatch, reconciliation fail, audit issue
```

**Isliye document ne `budget: str` rakha** — aur ye **sahi decision** hai. ✅ Tumhari jeet.

---

### **SelectedDealSchema** — 🔄 CHANGED (5 naye fields)
```python
class SelectedDealSchema(BaseModel):
    """🔄 CHANGED — added inventory_tier, genre, ad_lengths, provider"""
    deal_id: str = Field(..., description="External deal ID e.g. EXT7P75718S8MNR")
    name: str = Field(..., description="Deal name")
    cpm: str = Field(..., description="Fixed or floor CPM price")
    inventory_tier: InventoryTierEnum = Field(...)     # ➕ NEW
    provider: str = Field(...)                          # ➕ NEW  "Prime Video, Netflix, Disney+"
    genre: Optional[str] = Field(None)                  # ➕ NEW  "Genre if genre-specific deal"
    ad_lengths: list[str] = Field(default_factory=list) # ➕ NEW  "Supported durations"
    deal_type: str = Field(...)                         # ➕ NEW  "PG, Preferred, or Private Auction"
```

**Har naye field ka WHY:**

| Field | Kyun joda | Kis feature ke liye |
|---|---|---|
| `inventory_tier` | Tier fork ka core | Honesty rule, audience applicability, repair loop |
| `provider` | Kaunsa platform | Budget split (per-inventory), creative approval (per-platform) |
| `genre` | Genre-specific deal | **Genre upsell logic** |
| `ad_lengths` | Deal kaunsi durations support karta hai | **Duration match check** |
| `deal_type` | PG / Preferred / Private | ⚠ PG ka pause warning |

**Real example — poora deal object:**
```python
SelectedDealSchema(
    deal_id="EXT7P75718S8MNR",
    name="Prime Video | Preferred Deal | UK - 30 - ROS",
    cpm="28.88",
    inventory_tier=InventoryTierEnum.AMAZON_OWNED,   # → forecast ✅
    provider="Prime Video",                           # → budget split key
    genre=None,                                       # ROS = no genre
    ad_lengths=["30"],                                # → duration check
    deal_type="Preferred"                             # → pause allowed ✅
)
```

> **⚠ Note:** `deal_type` **string** hai, enum nahi! `inventory_tier` enum hai par `deal_type` nahi.
> **Inconsistent.** `DealTypeEnum` hona chahiye tha (PG/PREFERRED/PRIVATE_AUCTION).
> **David ne yahan comment kiya ho sakta hai.**

---

### **SelectedAudienceSetSchema** — 🔄 CHANGED (3 naye fields)
```python
class SelectedAudienceSetSchema(BaseModel):
    """🔄 CHANGED — added profile and effective_cpm"""
    audience_set_id: str = Field(..., description="Audience set UUID")
    name: str = Field(..., description="Audience set name")
    vcpm_fee: str = Field(..., description="VCPM fee decimal")
    profile: AudienceProfileEnum = Field(...)           # ➕ NEW
    effective_cpm: Optional[str] = Field(None)          # ➕ NEW  "Deal CPM + audience VCPM"
    estimated_reach: Optional[int] = Field(None)        # ➕ NEW  "If Amazon inventory"
```

**`estimated_reach` Optional kyun?** Kyunki `"If Amazon inventory"` — Netflix/Disney ke liye `None`. **Honesty rule schema me baithi hui hai.** ✅ Ye accha design hai.

**`effective_cpm` Optional kyun?** Kyunki ye **derived** hai — deal CPM chahiye jo audience ke waqt pata na ho.

---

### **SelectedCreativeSchema** — 🔄 CHANGED (2 naye fields)
```python
class SelectedCreativeSchema(BaseModel):
    """🔄 CHANGED — added duration_seconds for the match check"""
    asset_id: str = Field(..., description="Registered asset ID")
    click_through_url: HttpUrl = Field(..., description="Landing page URL")
    duration_seconds: int = Field(...)          # ➕ NEW  "Video length in seconds"
    upload_method: str = Field("direct")        # ➕ NEW  "direct or url"
```

**`HttpUrl`** — Pydantic ka special type. Ye **URL validate** karta hai:
```python
click_through_url = "https://example.com/landing"  ✅
click_through_url = "not-a-url"                     ❌ ValidationError
click_through_url = "example.com"                   ❌ scheme missing
```

**Ye accha hai** — galat URL ad me jaane se pehle pakda jaata hai.

**`duration_seconds: int`** — ye **duration match check** ka core hai:
```python
if creative.duration_seconds not in [int(d) for d in strategy.durations]:
    trigger_reapproval()
```

> **⚠ Note:** `durations` me `DurationEnum` (string `"30"`) hai, par `duration_seconds` **int** (30) hai.
> **Type mismatch!** Comparison ke liye convert karna padega. Ye ek chhota design smell hai.
> **David ne comment kiya ho sakta hai.**

---

## 7.4 — ➕ NEW SCHEMAS (4)

### **BudgetSplitSchema** — ➕ NEW
```python
class BudgetSplitSchema(BaseModel):
    """➕ NEW — how budget is divided across inventories and durations"""
    method: BudgetSplitMethodEnum = Field(...)
    by_inventory: list[dict] = Field(..., description="[{provider, budget, impressions_estimate}]")
    by_duration: list[dict] = Field(..., description="[{duration, budget, cpm, impressions_estimate}]")
```

**Real example:**
```python
BudgetSplitSchema(
    method=BudgetSplitMethodEnum.EVEN_BY_IMPRESSIONS,
    by_inventory=[
        {"provider": "Prime Video", "budget": "6000.00", "impressions_estimate": 240000},
        {"provider": "Netflix",     "budget": "3000.00", "impressions_estimate": 112000},
        {"provider": "Disney+",     "budget": "1000.00", "impressions_estimate": 29412}
    ],
    by_duration=[
        {"duration": "15", "budget": "4000.00", "cpm": "20.00", "impressions_estimate": 200000},
        {"duration": "30", "budget": "6000.00", "cpm": "30.00", "impressions_estimate": 200000}
    ]
)
```

> **⚠ BADA GAP:** `list[dict]` **untyped** hai! `dict` me kuch bhi daal sakte ho — Pydantic check nahi karega.
>
> ```python
> by_inventory=[{"totally": "wrong", "keys": 123}]   # ✅ PASS ho jaayega!
> ```
>
> **Ye Pydantic ka poora maksad hi tod deta hai.** Fix:
> ```python
> class InventorySplitItem(BaseModel):
>     provider: str
>     budget: str
>     impressions_estimate: int
>
> class DurationSplitItem(BaseModel):
>     duration: DurationEnum
>     budget: str
>     cpm: str
>     impressions_estimate: int
>
> class BudgetSplitSchema(BaseModel):
>     method: BudgetSplitMethodEnum
>     by_inventory: list[InventorySplitItem]     # ← typed!
>     by_duration: list[DurationSplitItem]       # ← typed!
> ```
>
> 🎯 **David ne is par pakka comment kiya hoga.** Ye document me **kai jagah** hai (`reach_curve: list[dict]`, `validated_asins: list[dict]`). Ek pattern-level problem hai.

---

### **CurationRequirementsSchema** — ➕ NEW
```python
class CurationRequirementsSchema(BaseModel):
    """➕ NEW — captured for 3P-needs-curation inventory (e.g. Disney+)"""
    provider: str = Field(..., description="e.g. Disney+")
    genres: list[str] = Field(default_factory=list)
    durations: list[str] = Field(default_factory=list)
    targeting_preferences: Optional[str] = None
    budget: str = Field(..., description="Allocated budget for this provider")
    flight_dates: DateRangeSchema = Field(...)
```

**Real example (Part 5 Step 2 se):**
```python
CurationRequirementsSchema(
    provider="Disney+",
    genres=["Family", "Kids"],
    durations=["30"],
    targeting_preferences=None,
    budget="1000.00",
    flight_dates=DateRangeSchema(lower="2026-08-01", upper="2026-08-31")
)
```

> **⚠ Inconsistency:** Field table (page 9) me `genres` aur `durations` **"Required for curation tier"** hain.
> Par schema me `default_factory=list` = **optional**!
>
> **Table aur code contradict kar rahe hain.** Fix: `genres: list[str] = Field(..., min_length=1)`
>
> **David ne yahan comment kiya ho sakta hai.**

---

### **TargetingSchema** — ➕ NEW
```python
class TargetingSchema(BaseModel):
    """➕ NEW — CTV targeting options (config-driven, extensible)"""
    locations: list[str] = Field(default_factory=list)
    instream_positions: list[str] = Field(default_factory=list)
    content_category_exclusions: list[str] = Field(default_factory=list)
    device_types: list[str] = Field(default_factory=list)
    mobile_environments: list[str] = Field(default_factory=list)
```

> **⚠⚠ SABSE BADI CONTRADICTION IS DOCUMENT ME:**
>
> Docstring kehta hai **"config-driven, extensible"** — par code me **5 hard-coded fields** hain!
>
> Client ka requirement tha: *"This targeting list frequently changes so it should be easy to add new targeting types... must be config-driven, not hard-coded."*
>
> Ye schema us requirement ko **poora nahi karta.**
>
> **Poora fix Part 5 Step 5 me diya hai.**
>
> 🎯 **David ne is par pakka comment kiya hoga. Ye tumhara sabse taiyar jawab hona chahiye.**

---

### **ForecastResultSchema** — 🔄 CHANGED
```python
class ForecastResultSchema(BaseModel):
    """🔄 CHANGED — added availability flag for the honesty rule"""
    is_available: bool = Field(..., description="False for Netflix/Disney — no reach data")  # ➕ NEW
    estimated_impressions: Optional[int] = None
    estimated_unique_reach: Optional[int] = Field(None, description="Only for Amazon inventory")
    average_frequency: Optional[float] = Field(None, description="Only for Amazon inventory")
    indicative_cpm: Optional[str] = None
    reach_curve: Optional[list[dict]] = Field(None, description="[{budget, reach}] — Amazon only")
```

**🔴 `is_available` — ye ek chhota field hai par bahut bada concept hai.**

**Ye honesty rule ko SCHEMA LEVEL par enforce karta hai:**
```python
if not forecast.is_available:
    # Agent JAANTA hai ki reach nahi mil sakta
    # Isliye guess karne ka mauka hi nahi
    show_impressions_only_with_explanation()
else:
    show_full_forecast_with_reach_curve()
```

**Aur sab fields `Optional` hain** — kyunki 3P me khaali rahenge. **Schema hi bata deta hai ki khaali ho sakta hai.**

✅ **Ye v2.0 ka best schema change hai.** Ye ek business rule ko type system me convert karta hai.

> **⚠ Chhota gap:** `is_available: false` hai par **kyun** — ye field me nahi hai.
> `unavailable_reason: Optional[str]` hona chahiye tha, taaki UI wahi message dikha sake.

---

### **TrackingSetupSchema** — ➕ NEW
```python
class TrackingSetupSchema(BaseModel):
    """➕ NEW — tracking prerequisites collected at Step 11"""
    sells_on_amazon: bool = Field(...)
    validated_asins: list[dict] = Field(default_factory=list, description="[{asin, title, brand}]")
    sells_on_own_site: bool = Field(...)
    ad_tag_registered: Optional[bool] = None
    ad_tag_conversions: list[str] = Field(default_factory=list)
```

**"Prerequisites"** = pehle se zaroori cheezein.

**`ad_tag_registered: Optional[bool]`** — teen states:
```
None  = "abhi check nahi kiya"
True  = "tag laga hua hai"
False = "tag nahi laga — setup instructions dikhao"
```

**Ye 3-state design accha hai** — `None` aur `False` me farak matter karta hai.

> **⚠ `validated_asins: list[dict]` — phir untyped dict.** Wahi problem.

---

## 7.5 — 🔴 FullStrategySchema (Master Schema)
### 🔄 CHANGED — restructured from wizard steps to **semantic grouping**

**"Semantic grouping"** = **matlab** ke hisaab se group karna (screen ke hisaab se nahi).

### Restructure kyun? — Ye ek gehri baat hai

```python
# ❌ v1.1.0 (wizard-based grouping):
class FullStrategySchema(BaseModel):
    details: Step1DetailsSlotSchema         ← "Step 1"?
    goal_kpi_bid: Step2GoalKPIBidSlotSchema  ← "Step 2"?
    deals: Step3DealsSlotSchema              ← "Step 3"?
    audiences: Step4AudienceSlotSchema
    creatives: Step5CreativeSlotSchema

# ✅ v2.0 (flat + semantic comments):
class FullStrategySchema(BaseModel):
    # --- Identity ---
    # --- Basics (Step 1) ---
    # --- Inventory (Step 2) ---
    # --- Budget Split (Step 3) ---
    ...
```

### 🔴 WHY ye change zaroori tha?

**Document ki apni line (PlanningAgentState me):**
> *"Named semantically, not by wizard step — **the state describes the plan, not the UI that collected it.**"*

**Ye ek bahut mature software design principle hai. Samjho:**

```
Problem: Agar field ka naam "step1_details" hai, aur kal UI badal
         gaya (Step 1 ab Step 3 ban gaya), to?

         → Field ka naam GALAT ho jaayega
         → Ya poora database migration karna padega
         → Ya naam galat rehne dena padega (confusing)

Solution: Field ka naam us cheez ke MATLAB par rakho, UI par nahi.

         "step1_details"      ❌ UI se bandha hua
         "strategy_name"      ✅ matlab se bandha hua

         UI 10 baar badle, "strategy_name" wahi rahega.
```

**Ye "separation of concerns" hai** — data ka structure UI ke structure se **alag** hona chahiye.

✅ **Ye v2.0 ka ek excellent change hai. Aur ye ek asli technical improvement hai jo David ko pasand aayega.**

### Poora Schema — semantic groups ke saath

```python
class FullStrategySchema(BaseModel):
    """🔄 CHANGED — restructured from wizard steps to semantic grouping"""

    # ═══ IDENTITY ═══
    id: Optional[str] = Field(None, description="System-assigned strategy ID")
    advertiser_id: str = Field(..., description="Parent advertiser UUID")
    channel_type: ChannelTypeEnum = ChannelTypeEnum.DSP

    # ═══ BASICS (Step 1) ═══
    name: str = Field(..., description="Unique strategy name")
    flight_dates: DateRangeSchema = Field(...)
    markets: list[str] = Field(..., description="ISO country codes")
    primary_currency: CurrencyEnum = Field(CurrencyEnum.GBP)
    durations: list[DurationEnum] = Field(...)                      # ➕ NEW
    formats: list[FormatEnum] = Field(...)
    goal: GoalEnum = Field(GoalEnum.AWARENESS)                      # 🔄 CHANGED default
    kpi_target_type: KPIEnum = Field(...)
    product_categories: list[int] = Field(default_factory=list)
    product_location: ProductLocationEnum = Field(...)
    market_budgets: list[MarketBudgetBidSchema] = Field(...)
    frequency_cap: Optional[int] = Field(None)                      # ➕ NEW
    budget_cap: Optional[str] = Field(None)                         # ➕ NEW

    # ═══ INVENTORY (Step 2) ═══
    selected_deals: list[SelectedDealSchema] = Field(...)           # 🔄 enriched
    curation_requirements: list[CurationRequirementsSchema] = Field(default_factory=list)  # ➕ NEW

    # ═══ BUDGET SPLIT (Step 3) ═══
    budget_split: Optional[BudgetSplitSchema] = None                # ➕ NEW

    # ═══ AUDIENCES (Step 4) ═══
    audience_options: list[SelectedAudienceSetSchema] = Field(default_factory=list)  # 🔄 all three
    chosen_audience_profile: Optional[AudienceProfileEnum] = None   # ➕ NEW
    matching_mode: str = Field("Exact")                             # ✅ UNCHANGED

    # ═══ TARGETING (Step 5) ═══
    targeting: Optional[TargetingSchema] = None                     # ➕ NEW

    # ═══ FORECAST (Step 6) ═══
    forecast: Optional[ForecastResultSchema] = None                 # 🔄 enriched

    # ═══ APPROVAL (Step 7) ═══
    approval_status: Optional[ApprovalStatusEnum] = None            # ➕ NEW
    approved_by: Optional[str] = None                               # ➕ NEW
    approved_at: Optional[str] = None                               # ➕ NEW

    # ═══ CREATIVE (Step 9) ═══
    selected_creatives: list[SelectedCreativeSchema] = Field(default_factory=list)  # 🔄 enriched
    creative_duration_match: Optional[bool] = None                  # ➕ NEW
    creative_approval_status: Optional[ApprovalStatusEnum] = None   # ➕ NEW

    # ═══ TRACKING (Step 11) ═══
    tracking: Optional[TrackingSetupSchema] = None                  # ➕ NEW
    product_asins: list[str] = Field(default_factory=list)          # 🔄 MOVED from Step 1

    # ═══ ACTIVATION (Steps 12-13) ═══
    credit_sufficient: Optional[bool] = None                        # ➕ NEW
    status: str = Field("created", description="Strategy status")    # 🔄 CHANGED from "draft"
    is_syncing: bool = Field(False)
```

### 🔴 4 Zaroori Observations

**1. `audience_options` me TEENO options hain**
```python
audience_options: list[SelectedAudienceSetSchema]  # 🔄 CHANGED — now carries all three
chosen_audience_profile: Optional[AudienceProfileEnum]  # ➕ konsa chuna
```

**WHY teeno save karte hain?** Kyunki:
1. **Audit** — "kya options the?" ka record
2. **Re-approval** — reject hone par baaki do options dikha sakte ho
3. **Learning** — kaunsa profile log zyada chunte hain, ye data mil jaata hai

✅ Accha design.

**2. `creative_approval_status` — SIRF EK field**
```python
creative_approval_status: Optional[ApprovalStatusEnum] = None
```

> **⚠⚠ CONTRADICTION!** Step 10 ka field table kehta hai **TEEN** alag statuses:
> - Amazon approval status
> - Netflix approval status
> - Disney approval status
>
> Par schema me **ek hi** field hai!
>
> ```python
> # Kaise handle karoge?
> Amazon: APPROVED, Netflix: PENDING, Disney: REJECTED
> → creative_approval_status = ???
> ```
>
> **Fix chahiye:**
> ```python
> creative_approval_statuses: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
> # {"Amazon": "APPROVED", "Netflix": "PENDING", "Disney+": "REJECTED"}
> ```
>
> 🎯 **David ne is par pakka comment kiya hoga.** Ye ek asli schema bug hai jo implementation me atkega.

**3. `status: Field("created")` vs API response `"draft"`**
> **⚠ Open Question #3** — Part 5 Step 8 me poora detail.

**4. `matching_mode: str = Field("Exact")` — enum kyun nahi?**
> **⚠** `Similar` / `Exact` do fix values hain. String rakhne se typo ka khatra:
> ```python
> matching_mode = "exact"   # lowercase — accept ho jaayega, par galat!
> matching_mode = "Similiar" # typo — accept ho jaayega!
> ```
> `MatchingModeEnum` hona chahiye tha. **Ye inconsistent hai** — document ne 5 naye enum banaye par ye nahi.

---

# PART 8 — SECTION 6: STATE MACHINE
### 🔄 CHANGED — needs complete rebuild

**Document literally:**
> *"🔄 CHANGED — needs complete rebuild. The original was a **linear pipe**. The confirmed flow has **branches, loops, and interrupts**."*

## 8.1 — "Linear pipe" se "branches, loops, interrupts" — matlab kya?

### v1.1.0 ka state machine — LINEAR PIPE
```
START → ParseUserPrompt → ValidateSlotSchema → InvokeTool
      → ForecastRepairLoop → PresentCard → ExecuteCreate → END

Ek seedhi line. Ek raasta. Ek direction.
(Sirf ek chhota loop tha — ForecastRepairLoop ke andar)
```

**"Pipe"** = paani ka pipe — ek taraf se ghusa, doosri taraf se nikla. Beech me koi mod nahi.

### v2.0 ka state machine — BRANCHES + LOOPS + INTERRUPTS
```
START → ... → BRANCH (tier ke hisaab se 3 raaste)
            → LOOP (repair)
            → ⏸ INTERRUPT (approval — ruk jaata hai)
            → LOOP (duration mismatch → re-approve)
            → LOOP (creative reject → re-upload)
            → LOOP (credit insufficient → top-up)
            → END
```

**WHY badalna pada?** Kyunki asli business flow **linear nahi hai**:
```
Branch:    "Amazon inventory hai? To forecast karo. Netflix? To mat karo."
Loop:      "Reach kam hai? Audience widen karo, phir se forecast karo."
Interrupt: "Manager ka jawab aane tak RUKO."
```

Ye teeno **ek seedhi line me possible nahi** hain.

---

## 8.2 — Confirmed State Machine (v5) — Poora 25-line flow

Document ne literally ye diya hai:

```
1  START
2   → extract_fields (slot-filling from brief)
3   → select_inventory (CTV, three-tier fork)
4      → [if 3P needs curation] capture_curation_requirements
5   → propose_budget_split (across inventories + durations)
6   → suggest_audiences (3 options via pgvector; mandatory)
7   → apply_targeting (optional, configurable)
8   → predict_reach
9      → [if Amazon] real forecast + reach curve
10     → [if 3P] CPM + derived impressions only (honest)
11     → [if too narrow] REPAIR: extend audience → re-predict (loop)
12  → present_plan (on the strategy card)
13  → ⏸ PLAN APPROVAL (interrupt — optionally a manager)
14     → [if rejected] return to suggest_audiences
15  → create_strategy (POST /strategies/ — the real one, not draft)
16  → upload_creative (video, gen_upload_urls + register)
17     → [if duration mismatch] amend plan → RE-APPROVE (loop back)
18  → platform_creative_approval (Amazon / Netflix / Disney review)
19     → [if rejected] return to upload_creative
20  → tracking_setup (ASINs + ad tag check)
21  → credit_check (GET /credits/summary/)
22     → [if insufficient] prompt top-up (loop)
23  → activate (POST /strategies/{id}/set_status/ — the single spend action)
24  → DONE
```

### Line-by-line samjho

| Line | Node | Kya karta hai | Type |
|---|---|---|---|
| 2 | `extract_fields` | Brief se slots bharna | Node |
| 3 | `select_inventory` | Deals chunna + tier derive karna | Node |
| 4 | `capture_curation_requirements` | Disney+ ke liye reqs lena | **Conditional node** |
| 5 | `propose_budget_split` | Budget baantna | Node |
| 6 | `suggest_audiences` | 3 options banana (pgvector) | Node |
| 7 | `apply_targeting` | Optional filters lagana | Node |
| 8 | `predict_reach` | Forecast | Node |
| 9-10 | *(branch)* | Amazon vs 3P — alag behaviour | **Conditional edge** |
| 11 | *(loop)* | Repair: extend → re-predict | **Loop** |
| 12 | `present_plan` | Strategy Card dikhana | Node |
| 13 | ⏸ | **INTERRUPT** — insaan ka intezaar | **Interrupt** |
| 14 | *(loop back)* | Reject → line 6 par wapas | **Loop** |
| 15 | `create_strategy` | POST /strategies/ | Node |
| 16 | `upload_creative` | Video upload | Node |
| 17 | *(loop back)* | Duration mismatch → line 13 par wapas | **Loop** |
| 18 | `platform_creative_approval` | Platform review | Node |
| 19 | *(loop back)* | Reject → line 16 par wapas | **Loop** |
| 20 | `tracking_setup` | ASIN + ad tag | Node |
| 21 | `credit_check` | Balance check | Node |
| 22 | *(loop)* | Insufficient → top-up | **Loop** |
| 23 | `activate` | 💰 SPEND | Node |

### 🔴 Node naming pattern — dhyan do

Sab node names **verb_noun** pattern me hain:
```
extract_fields
select_inventory
propose_budget_split
suggest_audiences
apply_targeting
predict_reach
present_plan
create_strategy
upload_creative
tracking_setup      ← ⚠ ye pattern se hatka hai! "setup_tracking" hona chahiye
credit_check        ← ⚠ ye bhi! "check_credit" hona chahiye
activate
```

**⚠ Do node names inconsistent hain.** Chhoti baat hai, par ek "contract document" me consistency matter karti hai. **David ne comment kiya ho sakta hai.**

---

## 8.3 — ➕ Q&A Side Path (Bahut important feature)

**Document literally:**
> *"Q&A side path: at any point, the trader can ask a pricing/availability question ('what's the CPM for Netflix 30s?'). The agent answers from the rate card and resumes."*

### WHAT?
Trader **kabhi bhi**, **kisi bhi step par** ek sawaal poochh sakta hai. Agent jawab deta hai aur **wahin se aage** chalta hai.

### WHY ye zaroori hai?

```
❌ Bina Q&A side path:
Agent: "Audience chuno — Narrow, Balanced, ya Wide?"
Trader: "Ruko, pehle batao Netflix 30s ka CPM kya hai?"
Agent: "Kripya Narrow, Balanced, ya Wide chunein."
Trader: "Arre main sawaal poochh raha hun!"
Agent: "Invalid input. Kripya ek option chunein."
→ 😡 Trader frustrate ho gaya. Ye ek DUMB FORM hai, agent nahi.

✅ Q&A side path ke saath:
Agent: "Audience chuno — Narrow, Balanced, ya Wide?"
Trader: "Ruko, Netflix 30s ka CPM kya hai?"
Agent: "Netflix 30s GB me £32.00 CPM hai (rate card se). Prime
        Video 30s £28.88 hai — thoda sasta.
        Ab audience par wapas — Narrow, Balanced, ya Wide?"
Trader: "Balanced"
→ 😊 Ye ek ASLI conversation hai.
```

### 🔴 Technical challenge — ye implement karna mushkil hai

```
Problem: LangGraph me flow linear-ish hota hai. Agar trader
         beech me kuch aur poochhta hai, to graph confuse ho
         jaayega.

Solution: Ek "router" node chahiye jo har message par decide kare:
          "Ye jawab hai (aage badho) ya sawaal hai (jawab do,
           wahin raho)?"
```

**Design pattern:**
```
Har user message par:
  ↓
[classify_intent node]
  ├─ intent = "answer"    → aage badho (next step)
  ├─ intent = "question"  → answer_from_rate_card → WAHIN RAHO
  ├─ intent = "correction" → previous slot update karo → WAHIN RAHO
  └─ intent = "restart"   → poochho "sach me shuru se?"
```

> **⚠ Document ne ye feature likha hai par implementation ka koi detail nahi diya.**
> Sirf ek line hai. **David ne comment kiya ho sakta hai:** "Ye kaise implement hoga? Kaunsa node? Kaunsi state field?"
>
> **Tumhara jawab:** *"Ye ek intent-router node se hoga — main isko state machine me explicit karunga. State me `current_stage` field pehle se hai jo resume point track karti hai, to Q&A ke baad wahin lautna possible hai."*

---

## 8.4 — 🔴 PlanningAgentState — Poora State Object

### 🔄 CHANGED — restructured from wizard-step-based to semantic field names

### Pehle: v1.1.0 ka state (document ne comparison diya)
```python
# WAS (v1.1.0):
class PlanningAgentState(TypedDict):
    messages: List[Dict[str, Any]]
    advertiser_id: str
    current_step: int  # 0 to 5
    strategy_id: Optional[str]
    step1_details: Optional[Dict[str, Any]]      ← ⚠ "step1"
    step2_goal_kpi_bid: Optional[Dict[str, Any]]  ← ⚠ "step2"
    step3_deals: Optional[Dict[str, Any]]         ← ⚠ "step3"
    step4_audiences: Optional[Dict[str, Any]]     ← ⚠ "step4"
    step5_creatives: Optional[Dict[str, Any]]     ← ⚠ "step5"
    forecast_results: Optional[Dict[str, Any]]
    validation_errors: List[str]
    is_complete: bool
```

**3 problems the:**
1. **`step1_`, `step2_`... naam UI se bandhe** hue the
2. **`current_step: int` (0-5)** — 13 steps me ye kaam nahi karega
3. **Sab `Dict[str, Any]`** — koi type safety nahi

### Ab: v2.0 ka state

```python
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class PlanningAgentState(TypedDict):
    """State carried through the LangGraph planning flow.

    Named semantically, not by wizard step — the state describes
    the plan, not the UI that collected it.
    """
    # ═══ CONVERSATION ═══
    messages: Annotated[list, add_messages]

    # ═══ SESSION CONTEXT ═══
    advertiser_id: str
    session_id: str
    current_stage: str                    # ➕ NEW — for the adaptive canvas
    current_artifact_id: Optional[str]    # ➕ NEW — for the adaptive canvas

    # ═══ BASICS ═══
    strategy_name: Optional[str]
    flight_dates: Optional[dict]
    markets: list[str]
    durations: list[str]                  # ➕ NEW
    primary_currency: str
    goal: str                             # fixed: AWARENESS for CTV
    kpi: str                              # reach or frequency
    market_budgets: list[dict]
    product_location: Optional[str]
    frequency_cap: Optional[int]          # ➕ NEW
    budget_cap: Optional[str]             # ➕ NEW

    # ═══ INVENTORY ═══
    inventory_tier: Optional[str]         # ➕ NEW — which tier fork we're on
    selected_deals: list[dict]
    curation_requirements: list[dict]     # ➕ NEW

    # ═══ BUDGET SPLIT ═══
    budget_split: Optional[dict]          # ➕ NEW

    # ═══ AUDIENCES ═══
    audience_options: list[dict]          # the three profiles
    chosen_audience: Optional[dict]       # which one the trader picked

    # ═══ TARGETING ═══
    targeting: Optional[dict]             # ➕ NEW

    # ═══ FORECAST ═══
    forecast: Optional[dict]              # reach/impressions/CPM (with availability flag)

    # ═══ APPROVAL ═══
    approval_status: Optional[str]        # ➕ NEW — PENDING/APPROVED/REJECTED
    approved_by: Optional[str]            # ➕ NEW
    approved_at: Optional[str]            # ➕ NEW

    # ═══ CREATIVE ═══
    creative_id: Optional[str]
    creative_duration_match: Optional[bool]      # ➕ NEW
    creative_approval_status: Optional[str]      # ➕ NEW

    # ═══ TRACKING ═══
    tracking_setup: Optional[dict]        # ➕ NEW
    product_asins: list[str]              # 🔄 MOVED

    # ═══ ACTIVATION ═══
    credit_sufficient: Optional[bool]     # ➕ NEW
    strategy_id: Optional[str]
    strategy_status: Optional[str]

    # ═══ ERRORS ═══
    validation_errors: list[str]
```

### 🔴 4 Zaroori Changes

#### **1. `messages: Annotated[list, add_messages]`**

**Ye v1.1.0 ke `List[Dict[str, Any]]` se bahut behtar hai.**

```python
# ❌ v1.1.0: messages: List[Dict[str, Any]]
#    LangGraph me jab node state return karta hai, wo REPLACE karta hai
#    → naya message aaya → poori list overwrite → PURI CHAT GAYI!

# ✅ v2.0: messages: Annotated[list, add_messages]
#    add_messages ek "reducer" hai — ye batata hai "APPEND karo, replace nahi"
#    → naya message aaya → list ke PEECHE jud gaya → chat bachi
```

**"Reducer"** = ek function jo batata hai "purani value aur nayi value ko **kaise jodna** hai."

**Real example:**
```python
# State me: messages = [msg1, msg2]
# Node return karta hai: {"messages": [msg3]}

# Bina add_messages:
#   → messages = [msg3]              ❌ msg1, msg2 GAYE!

# add_messages ke saath:
#   → messages = [msg1, msg2, msg3]  ✅ sab bache
```

✅ **Ye ek critical bug fix hai.** v1.1.0 me ye bug tha (chhupa hua).

#### **2. `current_step: int` → `current_stage: str`**

```python
# ❌ v1.1.0: current_step: int  # 0 to 5
#    Problem: ab 13 steps hain! 0-12? Par steps ke andar sub-states bhi hain
#             (repair loop, approval waiting) — number se express nahi hote

# ✅ v2.0: current_stage: str
#    "basics", "inventory", "budget_split", "audiences", "targeting",
#    "forecast", "awaiting_approval", "creating", "creative_upload",
#    "awaiting_creative_approval", "tracking", "credit_check", "activating"
```

**WHY string behtar hai?**
1. **Padhne me saaf** — logs me `"awaiting_approval"` vs `"7"`
2. **Sub-states possible** — `"forecast_repairing"` ek alag stage ho sakti hai
3. **Steps reorder karne par naam nahi badalta**

> **⚠ Par ek gap:** `current_stage` ki **allowed values document me nahi hain!**
> `str` hai, enum nahi. Koi bhi string daal sakte ho.
> **David ne comment kiya ho sakta hai:** "Stage values kya hain? Enum kahan hai?"

#### **3. ➕ `session_id`, `current_artifact_id` — Adaptive Canvas ke liye**

```python
session_id: str
current_stage: str                    # ➕ NEW — for the adaptive canvas
current_artifact_id: Optional[str]    # ➕ NEW — for the adaptive canvas
```

**"Adaptive canvas"** = **Basil ka kaam.** Ek UI jo chat ke saath **badalta** hai.

**Kaise kaam karta hai:**
```
Agent stage "audiences" par hai
   ↓ current_stage = "audiences"
   ↓ current_artifact_id = "art_audience_options_v1"
   ↓
UI (adaptive canvas) ye dekhta hai aur AUDIENCE COMPARISON CARD dikhata hai
   (teen options ka table, effective CPM ke saath)

Agent stage "forecast" par gaya
   ↓ current_stage = "forecast"
   ↓ current_artifact_id = "art_forecast_v1"
   ↓
UI ne khud badal kar REACH CURVE CHART dikha diya
```

**"Artifact"** = ek visual cheez jo UI dikhata hai (card, chart, table).

**WHY?** Kyunki poori planning chat me nahi ho sakti. Reach curve chart chahiye. Audience comparison table chahiye. Ye fields UI ko batate hain **kya dikhana hai**.

**Ye Basil ka contract hai — is document se wo ye do fields lega.**

> **⚠ Par document ne ye explain nahi kiya ki artifact kaise banta hai, kahan store hota hai, ya kya shapes possible hain.** Sirf do fields hain. **David ne comment kiya ho sakta hai.**

#### **4. Sab `dict` hain — Pydantic schemas nahi**

```python
flight_dates: Optional[dict]           # DateRangeSchema kyun nahi?
market_budgets: list[dict]             # list[MarketBudgetBidSchema] kyun nahi?
selected_deals: list[dict]             # list[SelectedDealSchema] kyun nahi?
budget_split: Optional[dict]           # BudgetSplitSchema kyun nahi?
targeting: Optional[dict]              # TargetingSchema kyun nahi?
forecast: Optional[dict]               # ForecastResultSchema kyun nahi?
```

**Document ne Section 5 me 12 zabardast Pydantic schemas banaye — par state me sab `dict` hai!**

**WHY aisa kiya?** Do possible wajah:
1. **LangGraph TypedDict maangta hai** — Pydantic model state me thoda mushkil hota hai
2. **Performance** — state har node par serialize/deserialize hoti hai, Pydantic validation slow hoga

**Par nuksaan:**
```python
state["market_budgets"] = [{"totally": "wrong"}]   # ✅ PASS! Koi error nahi
state["forecast"] = "hello"                         # ✅ PASS! dict nahi hai par...
```

> 🎯 **David ne is par comment kiya ho sakta hai.** Ye ek asli design tension hai.
>
> **Tumhara jawab (best practice):**
> *"State me `dict` rakhna LangGraph ka standard pattern hai — performance ke liye. Par validation kho jaati hai. Mera plan: **boundary par validate karo** — jab node state se data padhta hai, use Pydantic model me convert karo, kaam karo, phir `.model_dump()` karke wapas dict me daalo. Isse dono faayde milte hain:*
>
> ```python
> def predict_reach(state: PlanningAgentState) -> dict:
>     # Boundary par PARSE karo
>     deals = [SelectedDealSchema(**d) for d in state["selected_deals"]]
>     #        ↑ galat data yahan pakda jaayega
>
>     result = call_forecast_api(deals)
>     forecast = ForecastResultSchema(**result)   # response validate
>
>     # Boundary par DUMP karo
>     return {"forecast": forecast.model_dump()}
> ```
> *Ise 'parse, don't validate' pattern kehte hain."*

---

# PART 9 — SECTION 7: BRIEF PARSING & EDGE CASES

## 9.1 — Entity Normalisation
### ✅ UNCHANGED — original examples are correct. Additions ➕

**"Entity"** = ek cheez jo text me pehchani ja sakti hai (tareekh, jagah, paisa, product).
**"Normalisation"** = usko **ek standard shape** me badalna.

### WHY zaroori hai?

```
Insaan likhta hai:              Computer chahta hai:
"August"                    →   {"lower": "2026-08-01", "upper": "2026-08-31"}
"UK"                        →   ["GB"]
"£10,000"                   →   "10000.00"
"next month"                →   ??? (aaj ke hisaab se calculate karo)
"ten thousand pounds"       →   "10000.00"
"Aug-Sept"                  →   2 mahine ka range

→ Insaan ki bhasha DHEELI hai. Computer ko PAKKI shape chahiye.
→ Normalisation ye gap bharta hai.
```

### 📋 Poora Normalisation Table (Document se, literally)

| Input | Extraction | Status |
|---|---|---|
| `August 2026` | `flight_dates: {lower: "2026-08-01", upper: "2026-08-31"}` | ✅ Original |
| `UK` | `markets: ["GB"]`, `primary_currency: "GBP"` | ✅ Original |
| `£10,000` | `market_budgets: [{market: "GB", budget: "10000.00"}]` | ✅ Original |
| `education website` | `product_location: "NOT_SOLD_ON_AMAZON"` | ✅ Original |
| **`30 seconds`** | `durations: ["30"]` | ➕ **NEW** |
| **`UK and France`** | `markets: ["GB", "FR"]` | ➕ **NEW** |
| **`sports drink`** | Consider genre-specific deals (Sports) | ➕ **NEW** |
| **`Prime and Netflix`** | Multiple inventory tiers | ➕ **NEW** |

### Ek-ek rule ka WHY + real example

#### **`August 2026` → flight_dates**
```
Input:  "August"
Logic:  1. Mahina pehchano → August
        2. Saal? Nahi diya → next occurring August → 2026
        3. Pehla din → 2026-08-01
        4. Aakhri din → 2026-08-31 (August me 31 din hote hain)
Output: {lower: "2026-08-01", upper: "2026-08-31", bounds: "[)"}
```

**⚠ Edge case:** Agar aaj 15 August 2026 hai aur trader "August" bolta hai?
- Wo **is** August ka baaki hissa chahta hai? (16-31 Aug)
- Ya **next** August? (Aug 2027)

Document ne ye case nahi cover kiya. **Ambiguity.** Agent ko **poochhna** chahiye.

#### **`UK` → markets + currency (DO cheezein!)**
```
Input:  "UK"
Output: markets: ["GB"]              ← ISO code
        primary_currency: "GBP"      ← ⚠ CURRENCY BHI!
```

**🔴 Ye ek smart inference hai.** Agent ne UK se **currency bhi** guess kar li.

**Par ⚠ khatra hai:**
```
Ek US company UK me campaign chala rahi hai, par reporting USD me
chahti hai (kyunki unka accounting USD me hai).

Agent ne GBP maan liya → GALAT.

→ Isliye agent ko CONFIRM karna chahiye:
  "UK campaign — main GBP me reporting maan raha hun. Theek hai?"
```

**Yahi wajah hai ki "Did I understand correctly?" mechanism zaroori hai** (9.4 me).

#### **`£10,000` → budget**
```
Input:  "£10,000"
Logic:  1. Symbol se currency confirm → £ = GBP
        2. Comma hatao → 10000
        3. Decimal add karo → "10000.00"
        4. String rakho (float NAHI — Part 7.3 me kyun)
Output: market_budgets: [{market: "GB", budget: "10000.00"}]
```

**⚠ Multi-market edge case:**
```
"UK and France me £10,000"
→ £10,000 KUL hai ya PER MARKET?

Agent ko POOCHHNA chahiye:
"£10,000 total hai (dono market milakar) ya har market me £10,000?"

→ Document ne ye edge case cover nahi kiya. ⚠ GAP.
```

#### **`education website` → do inferences**
```
Input:  "education website"
Output: product_location: "NOT_SOLD_ON_AMAZON"   ← "website" se
        product_categories: [1]                  ← "education" se
```

**Do alag words se do alag fields! Ye zabardast parsing hai.**
- **"website"** → apni site par bechta hai → Amazon par nahi
- **"education"** → category = Education (ID 1)

#### **➕ `30 seconds` → durations** (NEW)
```
Input:  "30 second creative" / "30s ad" / "half-minute spot"
Output: durations: ["30"]
```

**WHY ye ➕ NEW hai?** Kyunki `durations` field hi v2.0 me naya hai!

#### **➕ `UK and France` → multi-market** (NEW)
```
Input:  "UK and France"
Output: markets: ["GB", "FR"]
```

**Iske consequences (document ne nahi likhe, par yaad rakho):**
```
markets = ["GB", "FR"]
→ market_budgets me DO entries chahiye
→ Budget split karna padega (kitna GB me, kitna FR me?)
→ base_bid dono market ke liye alag ho sakta hai
→ Deals dono market ke liye alag
→ primary_currency? GB=GBP, FR=EUR — kaunsa "primary"?
→ Creatives dono language me chahiye?
```

**⚠ Multi-market ka poora treatment document me nahi hai.** Sirf normalisation rule hai. **David ne comment kiya ho sakta hai.**

#### **➕ `sports drink` → genre hint** (NEW)
```
Input:  "sports drink"
Output: Consider genre-specific deals (Sports)
```

**Dhyan do — ye ek FIELD nahi hai, ek HINT hai.** Ye kisi slot me nahi jaata; ye agent ke **behaviour** ko badalta hai (Step 2 me genre upsell suggest karega).

**Real example (Part 5 Step 2 se):**
```
Brief: "Energy drink for gym-goers"
→ Agent Step 2 me: "Prime Video Sports genre @ $22.07 recommend
   karta hun (ROS $18.22 ke muqable) kyunki tumhara product
   sports audience se match karta hai."
```

#### **➕ `Prime and Netflix` → multiple tiers** (NEW)
```
Input:  "Prime and Netflix"
Output: Multiple inventory tiers
        → Prime Video   = AMAZON_OWNED
        → Netflix       = THIRD_PARTY_PRECURATED
```

**Ye trigger karta hai:**
1. Budget split (Step 3) — do inventories me baantna
2. Honesty rule (Step 6) — Netflix ka reach nahi milega
3. Do creative approvals (Step 10) — Amazon aur Netflix alag

**Ek chhoti si phrase se poora flow badal jaata hai.**

---

## 9.2 — Validation Failure Protocols
### ✅ UNCHANGED — teeno protocols correct

**"Protocol"** = tay kiya hua tarika — "aisa hone par aisa karo."

### **Protocol 1: Duplicate Name**
> *"If `check_strategy_name_uniqueness` returns `false`, append timestamp or suffix e.g. `Name_v2` **and prompt user**."*

```
Trader: "naam Summer_2026 rakho"
Agent → check → {"is_unique": false}

Agent: "'Summer_2026' pehle se exist karta hai.
        Main 'Summer_2026_v2' suggest karta hun. Theek hai,
        ya doosra naam chahiye?"
```

**🔴 "and prompt user" — sabse important hissa.**
```
❌ Agent khud naam badal deta:
   Agent: "Ho gaya! Strategy 'Summer_2026_v2' ban gayi"
   Trader (2 hafte baad): "Summer_2026 kahan hai? Mujhe nahi mil raha!"
   → Trader ne wo naam expect kiya jo usne diya tha

✅ Agent poochhta hai:
   Trader ko PATA hai ki naam badla — kyunki usne haan boli
```

**Design principle:** **Trader ki di hui values silently na badlo.** Suggest karo, confirm karo.

### **Protocol 2: Invalid ASIN**
> *"If `asin-validation` flags an invalid ASIN, **highlight the exact ASIN** to the user and request correction."*

```
Agent: "Do ASINs check kiye:
        ✅ B08N5WRWNW — Wireless Noise Cancelling Headphones (AudioBrand)
        ❌ B09B3H5F2C — Amazon catalogue me nahi mila

        B09B3H5F2C check karke dobara bhejo? Ya sirf pehle wale
        ke saath aage badhun?"
```

**Aur ek option bhi diya** — "sirf pehle wale ke saath aage badhun?" Ye accha UX hai.

### **Protocol 3: Past Dates**
> *"If `flight_dates.lower < today`, **auto-adjust to tomorrow's date and inform user**."*

```
Aaj: 29 July 2026
Trader: "1 July se chalao"
→ 1 July guzar chuka hai!

Agent: "1 July guzar chuka hai (aaj 29 July hai). Main start
        date 30 July (kal) kar raha hun. End date 31 August
        wahi rahegi. Theek hai?"
```

**🔴 Dhyan do — ye protocol Protocol 1 se ALAG hai:**

| | Duplicate name | Past date |
|---|---|---|
| Action | **Suggest** karo, poochho | **Auto-adjust** karo, **batao** |
| Kyun | Naam trader ki pehchaan hai | Past date **impossible** hai — koi choice nahi |

**Ye consistent hai:**
- Jahan **choice** hai → poochho
- Jahan **koi choice nahi** hai (impossible value) → theek karo aur batao

✅ **Ye teeno protocols v1.1.0 se aaye hain aur ✅ UNCHANGED hain. Tumhari jeet.**

> **⚠ Gap:** Sirf 3 protocols hain. Aur kai failure cases hain jo cover nahi:
> - Budget zero ya negative?
> - `upper < lower` (end date shuru se pehle)?
> - Market invalid (`"XX"`)?
> - Koi deal available nahi us market/duration me?
> - Suggest API ne koi audience nahi di?
> - API timeout ho gaya?
> - `POST /strategies/` ne 400 diya?
>
> **David ne yahan comment kiya ho sakta hai:** "error handling incomplete hai."

---

## 9.3 — Repair Loop
### 🔄 CHANGED — concept correct, mechanism updated

**Poora detail Part 5 Step 6 me hai.** Yahan short recap:

```
❌ v1.1.0: reach == 0 → Narrow se seedha Balanced/Broad par JUMP
✅ v2.0:   reach kam  → audience EXTEND karo (segments add karo)
                        → base bid badhao
                        → dobara forecast

+ ➕ Aur: repair loop SIRF Amazon portion par lagta hai
          (3P ke liye reach data hi nahi, to repair ka matlab nahi)
```

---

## 9.4 — ➕ NEW: "Did I Understand Correctly?" Confirmation

**Document literally:**
> *"➕ NEW — 'Did I understand correctly?' confirmation. After extracting fields from a brief, the agent immediately shows what it understood so the trader can correct before proceeding. **This is the single most important trust mechanism in the product.**"*

### 🔴 "The single most important trust mechanism in the product"

Ye document ka **sabse strong statement** hai. Kisi bhi feature ke baare me itni badi baat nahi kahi gayi.

### WHY?

```
Problem: Agent ne brief padha. Ab wo 8 fields bhar chuka hai —
         PAR TRADER KO PATA NAHI ki agent ne kya samjha!

Agar agent ne "UK" ko "Ukraine" samajh liya?
Agar "August" ko "Augustus" campaign name samajh liya?
Agar "£10,000" ko "$10,000" samajh liya?

→ Trader ko 5 STEP BAAD pata chalega, jab forecast galat aayega
→ Ya usse bhi bura: campaign chal jaayega galat market me
```

### Real example — bina confirmation:
```
Trader: "UK me August me £10k ka Prime Video campaign"

Agent (chup-chaap):
  markets = ["UA"]           ← ❌ Ukraine samajh liya!
  currency = "USD"           ← ❌ galat
  budget = "10000.00"

Agent: "Theek hai! Ab audience suggest kar raha hun..."

(5 steps baad)
Agent: "Forecast: Ukraine me 45,000 reach"
Trader: "UKRAINE?! Maine UK bola tha!"
→ 5 steps ka kaam BEKAAR. Aur trust khatam.
```

### Real example — WITH confirmation:
```
Trader: "UK me August me £10k ka Prime Video campaign,
         education website, 30 second"

Agent: "Samajh gaya. Confirm karo main sahi samjha:

        ┌────────────────────┬──────────────────────────────┐
        │ Market             │ United Kingdom (GB)          │
        │ Currency           │ GBP (£)                      │
        │ Flight dates       │ 1 Aug – 30 Aug 2026          │
        │ Budget             │ £10,000                      │
        │ Format             │ Prime Video                  │
        │ Creative duration  │ 30 seconds                   │
        │ Goal               │ Awareness (CTV default)      │
        │ Selling location   │ Off Amazon (own website)     │
        │ Product category   │ Education                    │
        └────────────────────┴──────────────────────────────┘

        Ye cheezein maine ASSUME ki hain — batao agar galat hain:
        • Currency GBP (kyunki UK) — agar USD reporting chahiye to batao
        • Flight 1–30 Aug (poora August) — ya specific dates?
        • Goal Awareness — CTV ke liye ye fixed hai

        Aur ye 2 cheezein main nahi jaan paya:
        • Strategy ka naam?
        • KPI — reach ya frequency?"
```

### 🔴 Dhyan do — is message me 4 layers hain:

| Layer | Kya karta hai | Kyun |
|---|---|---|
| **1. Jo samjha** | Table me sab dikhaya | Trader ek nazar me verify kare |
| **2. Jo ASSUME kiya** | Alag se highlight kiya | Assumptions sabse khatarnaak hote hain |
| **3. Jo pata nahi** | Saaf poochha | Trader ko pata rahe kya chahiye |
| **4. Kyun assume kiya** | "kyunki UK" | Trader agent ki soch samajh sake |

### 🔴 WHY ye "single most important trust mechanism" hai?

**Kyunki AI ka sabse bada dar ye hai:**
> *"Mujhe pata nahi ye kya kar raha hai."*

Ye mechanism us dar ko **khatam** karta hai:
```
Trader dekh sakta hai EXACTLY kya agent ne samjha
   ↓
Galti turant pakad sakta hai
   ↓
Trader ko CONTROL feel hota hai
   ↓
Trader agent par bharosa karta hai
   ↓
Trader agent USE karta hai
```

**Iske bina:** agent ek **black box** hai. Trader use nahi karega.

**Aur ye Zero-Hallucination ka natural partner hai:**
```
Zero-Hallucination      = "main jhooth nahi bolunga"
Did-I-Understand        = "main jo samjha wo dikha dunga"
Honesty Rule            = "jo nahi pata, saaf bataunga"

→ Teeno milkar TRUST banate hain. Yahi product hai.
```

> 💡 **Implementation tip:** Ye ek **node** hona chahiye — `confirm_extraction` — `extract_fields` ke turant baad. Aur ideally ek chhota `interrupt()` bhi, taaki trader ka jawab aane tak aage na badhe.
>
> **⚠ Document ne isko state machine me nahi dikhaya!** Line 2 me `extract_fields` hai, par confirmation node nahi hai. **David ne comment kiya ho sakta hai.**

---

# PART 10 — SECTION 8: SUMMARY OF ALL CHANGES

## 10.1 — Document ka apna summary table

| Category | Count | Items |
|---|---|---|
| ✅ **Unchanged** | ~15 | Core principles, product attribution, deal types, date validation, name uniqueness, currency, most API endpoints, brief parsing examples |
| 🔄 **Changed** | ~12 | Step order, goal scoped to Awareness, KPI scoped to reach/frequency, deals enriched with tier, audiences mandatory + renamed Wide, forecast with availability flag, state restructured, creative simplified to video |
| ➕ **New** | ~15 | Durations, inventory tiers, budget split, targeting, plan approval, creative duration check, platform creative approval, tracking setup (moved), credit check, activation, curation capture, effective CPM, adaptive-canvas fields |
| ❌ **Removed** | ~5 | Draft endpoint, product audiences, non-CTV formats (scoped out), non-awareness KPIs (scoped out), canary-check |

**Total: ~47 changes tracked.**

### ⚠ "canary-check" — ye kya hai?

Summary me `❌ Removed` me **"canary-check"** likha hai — **par ye poore document me kahin aur mention nahi hai!**

**Canary check** kya hota hai (general software term):
> Coal mine me pehle canary (chidiya) bhejte the — agar chidiya mar gayi to gas hai, mat jao.
> Software me: chhote hisse par pehle test karo, theek chala to poora chalao.

**Advertising me iska matlab hota:** campaign ko pehle chhote budget par chalao (jaise £500), dekho theek chal raha hai, phir poora £10,000 chalu karo.

> 🎯 **Ye ek ORPHAN ITEM hai** — summary me hai par kahin explain nahi kiya. Na v1.1.0 me hai (main check kar chuka hun — `strategy_schema_registry.md` me "canary" shabd nahi hai), na v2.0 ke kisi step me.
>
> **David ne is par pakka comment kiya hoga:** "Canary-check kya hai? Ye kahan tha jo remove kiya?"
>
> **Tumhara jawab:** *"Ye summary me galti se aa gaya — ye v1.1.0 me nahi tha. Main isko summary se hata dunga. Ya agar client ne discussion me mention kiya tha, to ise proper section me explain karunga."*

---

## 10.2 — Mera detailed Change Ledger (document se zyada precise)

### ✅ UNCHANGED — Jo Kareem ne sahi likha (16 items)

| # | Item | Kahan |
|---|---|---|
| 1 | Zero-Hallucination Policy | §1 |
| 2 | Self-Filling Form Paradigm | §1 |
| 3 | API-Driven Tool Execution | §1 |
| 4 | ON_AMAZON / NOT_SOLD_ON_AMAZON logic | §2.1 |
| 5 | DPV, ATC, Purchase, ROAS tracking | §2.1 |
| 6 | Halo sales concept | §2.1 |
| 7 | 14-day attribution window | §2.2 |
| 8 | 3 deal types (PG, Preferred, Private Auction) | §2.3 |
| 9 | Strategy name uniqueness validation | Step 1 |
| 10 | Flight date rules (`lower ≥ today`, `upper > lower`) | Step 1 |
| 11 | ISO country/currency codes | Step 1 |
| 12 | Product categories (required for video) | Step 1 |
| 13 | Market budgets + base bids (> 0) | Step 1 |
| 14 | Matching mode (Similar/Exact) | Step 4 |
| 15 | 14 of 24 API endpoints | §4 |
| 16 | Entity normalisation examples (4) + validation protocols (3) | §7 |

### 🔄 CHANGED — 13 items

| # | Item | Was | Now |
|---|---|---|---|
| 1 | **Step order** | 6-step UI wizard | 13-step agentic flow |
| 2 | **Goal** | 3 choices | Fixed AWARENESS |
| 3 | **KPI** | 6 choices | reach / frequency only |
| 4 | **Formats** | 4 formats | streaming_tv + prime_video |
| 5 | **Deal types** | Just types | + 3 inventory tiers |
| 6 | **Audience** | Optional, browse | **Mandatory**, suggestion-driven |
| 7 | **"Broad"** | Broad | **Wide** |
| 8 | **ASIN location** | Step 1 | Step 11 (⚠ conflict) |
| 9 | **Ad tag conversions** | Step 2 | Step 11 |
| 10 | **Creative** | Browse assets + pre-approved | Video upload only |
| 11 | **Create endpoint** | `/strategies/` or `/strategies/draft/` | `/strategies/` only |
| 12 | **Forecast schema** | Always available | + `is_available` flag |
| 13 | **State naming** | `step1_`, `step2_`... | Semantic (`strategy_name`, etc.) |
| 14 | **`messages` type** | `List[Dict]` | `Annotated[list, add_messages]` |
| 15 | **`current_step: int`** | 0–5 | `current_stage: str` |
| 16 | **Repair mechanism** | Profile switch | Audience extend |
| 17 | **Status default** | `"draft"` | `"created"` (⚠ conflict) |

### ➕ NEW — 20 items

| # | Item | Kahan |
|---|---|---|
| 1 | **3 inventory tiers** | §2.3 — sabse bada |
| 2 | Creative durations field | Step 1 |
| 3 | Frequency cap | Step 1 |
| 4 | Budget cap | Step 1 |
| 5 | CTV rate card | Step 2 |
| 6 | Genre upsell logic | Step 2 |
| 7 | Curation capture (5 fields) | Step 2 |
| 8 | **Budget Split step** | Step 3 |
| 9 | Effective CPM display | Step 4 |
| 10 | VCPM stacking insight | §2.4 |
| 11 | Chosen audience option field | Step 4 |
| 12 | **Targeting step** (5 fields) | Step 5 |
| 13 | **Honesty rule** | Step 6 |
| 14 | `is_available` flag | Step 6 |
| 15 | "Cannot sum reach" rule | Step 6 |
| 16 | **Plan Approval step** + interrupt() | Step 7 |
| 17 | **Duration match check** | Step 9 |
| 18 | **Platform creative approval** (3 statuses) | Step 10 |
| 19 | Ad tag registered check | Step 11 |
| 20 | "Sells on own website?" question | Step 11 |
| 21 | **Credit check step** | Step 12 |
| 22 | **Activate step** | Step 13 |
| 23 | Q&A side path | §6 |
| 24 | **"Did I understand correctly?"** | §7.3 |
| 25 | `session_id`, `current_stage`, `current_artifact_id` (adaptive canvas) | State |
| 26 | 9 new API endpoints | §4 |
| 27 | 5 new enums | §5 |
| 28 | 4 new schemas | §5 |

### ❌ REMOVED — 8 items

| # | Item | Kyun |
|---|---|---|
| 1 | `POST /api/strategies/draft/` | Client: draft is just for wizard |
| 2 | Product audiences | Not applicable to CTV |
| 3 | `display` format | Future scope |
| 4 | `online_video` format | Future scope |
| 5 | CTR, CPC, CPA, CPDPV KPIs | CTV has no clicks |
| 6 | Browse existing assets (`GET /api/assets/`) | CTV uploads fresh |
| 7 | Pre-approved creatives (`GET /api/creatives/`) | CTV needs fresh approval |
| 8 | Responsive e-commerce + 3P tags | Display-only formats |
| 9 | "canary-check" | ⚠ **Ye kya hai?** Kahin explain nahi |

---

# PART 11 — ⚠ OPEN QUESTIONS + GAPS
### David ke 28 comments ki tayyari

## 11.1 — Document ke apne 5 ⚠ Open Questions

Ye **document ne khud** flag kiye hain. Ye tumhari **taqat** hain — tumne assume karke aage nahi badha, saaf bataya ki clarity chahiye.

---

### ⚠ **OQ-1: ASIN Timing Conflict** (page 8 + page 18 — DO BAAR)

**Document:**
> *"`product_location` and `asin_numbers` are fields in the `POST /strategies/` payload called at Step 8. If ASINs are collected at Step 11 (after Step 8), they'd need to be patched onto the strategy afterwards. Alternatively, the ASIN question stays early (it's a plan field) and only the ad-tag check moves late."*

**Problem:**
```
Step 8:  POST /strategies/ → chahiye product_location + product_asins
Step 11: ASIN collect ho rahi hai  ← Step 8 KE BAAD!
```

**Tumhara ready jawab:**
> *"Ye maine deliberately flag kiya, assume karke aage nahi badha. Do options hain:*
> *(A) Step 8 me bina ASIN create karo, Step 11 me PATCH karo — par isse strategy beech me adhoori rehti hai aur ek extra call lagta hai.*
> *(B) `product_location` aur `product_asins` Step 1 me hi rakho (wo plan fields hain), sirf ad-tag check aur conversions Step 11 me.*
>
> *Main **Option B** recommend karta hun, teen wajah se:*
> *1. `product_location` ek planning decision hai (Amazon par bechta hai ya nahi) — tracking setup nahi*
> *2. ASIN validation response me `product_category` bhi aata hai — jo Step 1 ka field hai! To ASIN pehle lene se ek aur field auto-fill ho jaata hai*
> *3. Ek call bachta hai, aur strategy pehli baar me poori banti hai*
>
> *Step 11 me phir sirf wo cheezein rahengi jo genuinely tracking hain: ad tag registered hai ya nahi, aur kaunse conversion events track karne hain."*

---

### ⚠ **OQ-2: Suggest Endpoint Response Shape** (page 11)

**Document:**
> *"the suggest endpoint's response shape. v1.1.0 assumed it returns `bundles.narrow/balanced/broad`. The real endpoint may return a flat list that we group ourselves."*

**Tumhara ready jawab:**
> *"v1.1.0 me maine `bundles` structure assume kiya tha, par wo verify nahi hua tha. Agar asli API flat list deta hai, to grouping logic humein likhna padega — aur uske kai design sawaal hain: Narrow me kitne segments? Grouping ka basis kya — similarity score, estimated reach, ya VCPM?*
>
> *Ye ek genuine unknown hai, isliye maine assume nahi kiya. VOW backend team se ek confirmed response sample chahiye. Agar flat list hai, to main ek grouping layer add karunga jo cumulative reach ke hisaab se 3 bundles banaye, aur Balanced ko default recommend kare."*

---

### ⚠ **OQ-3: Created Strategy ka Status** (page 15)

**Document:**
> *"what status does the created strategy land in? If it's still `"draft"` by default, activation via `set_status` remains a separate step."*

**Aur document apne aap se contradict karta hai:**
```
Pydantic model:  status: str = Field("created")   # 🔄 CHANGED from "draft"
API response:    "status": "draft"                 ← purana example
```

**Tumhara ready jawab:**
> *"Yahan do cheezein confuse ho rahi hain, aur maine isliye flag kiya:*
> *1. **Draft endpoint** (`POST /strategies/draft/`) — client ne isko hataane ko kaha ✅*
> *2. **Draft status** (`status: "draft"`) — ye ek field ki value hai, iske baare me client ne kuch nahi kaha*
>
> *Mera recommendation: Step 8 ke baad status `created` ho, aur Step 13 (`set_status`) me `active` bane. Isse teen states saaf rehti hain:*
> *• `created` = plan database me hai, kharch nahi ho raha*
> *• `active` = chal raha hai, kharch ho raha hai*
> *• `paused` = ruka hua*
>
> *Aur main API response example ko update kar dunga — abhi wo v1.1.0 se copy hua hai aur `draft` dikhata hai. Wo galti hai."*

---

### ⚠ **OQ-4: 3P Creative Approval Status kahan se?** (page 16)

**Document:**
> *"do Netflix/Disney review statuses surface inside VOW's API, or is that tracked externally?"*

**Tumhara ready jawab:**
> *"Iska jawab poore Step 10 ka design decide karta hai:*
>
> *Agar VOW API me aata hai: agent poll karke automatically pata kar lega, trader ko notify karega, flow aage badhega. Simple.*
>
> *Agar externally tracked hai: humein manual-entry interface ya webhook chahiye hoga. Agent ko 'awaiting external confirmation' state me rakhna padega, aur koi insaan Netflix ke dashboard se status laakar VOW me daalega. **Ye M1 ke scope ko badha deta hai** — ek poora naya workflow.*
>
> *Isliye ye pehle confirm karna zaroori hai — ye estimate ko affect karta hai."*

---

### ⚠ **OQ-5: Simplified CTV Forecast Endpoint ka naam** (page 13)

**Document:** *"POST /api/audience-sets/reach-forecast/ (or the simplified CTV endpoint, name TBC)"*

**Aur ek related problem:** Document me **do** forecast endpoints hain:
- `POST /api/audience-sets/reach-forecast/`
- `POST /api/strategies/reach-forecast/`

**Tumhara ready jawab:**
> *"Do endpoints hain aur ek teesra 'simplified CTV endpoint' bhi mention hua hai jiska naam pata nahi. Mujhe VOW backend team se ye clarify karna hai:*
> *• `audience-sets/reach-forecast/` — sirf audience ka reach?*
> *• `strategies/reach-forecast/` — poori strategy ka (deals + audience + budget)?*
> *• CTV ke liye ek naya simplified endpoint hai?*
>
> *Mera anumaan: `strategies/reach-forecast/` poora forecast deta hai (reach curve ke saath) aur wahi use karna chahiye. Par confirm karna zaroori hai."*

---

## 11.2 — 🔴 Gaps jo maine dhoondhe (document ne flag nahi kiye)

Ye **document ne khud nahi bataye** — ye asli inconsistencies hain. David ke comments inme se kai par honge. **In par tumhara jawab tayyar hona chahiye.**

---

### 🔴 **GAP-1: TargetingSchema — "config-driven" kehta hai, hard-coded hai**

```python
class TargetingSchema(BaseModel):
    """➕ NEW — CTV targeting options (config-driven, extensible)"""  ← kehta hai
    locations: list[str] = ...              ← par hard-coded
    instream_positions: list[str] = ...
    content_category_exclusions: list[str] = ...
    device_types: list[str] = ...
    mobile_environments: list[str] = ...
```

**Client ka requirement:** *"must be config-driven, not hard-coded. Adding a new targeting type should be a configuration change, not a code change."*

**Ye schema us requirement ko poora NAHI karta.**

**Tumhara jawab:**
> *"Ye sahi catch hai. Docstring intent bata raha hai par code use enforce nahi karta. Fix:*
> ```python
> class TargetingSchema(BaseModel):
>     """Config-driven targeting. Keys validated against the
>        targeting-type registry at runtime, not compile time."""
>     selections: dict[str, list[str]] = Field(default_factory=dict)
>     # {"locations": ["London"], "device_types": ["Connected TV"]}
> ```
> *Aur ek `targeting_types.yaml` config file jo Vishal ke registry ka hissa banegi. Naya targeting type add karne ke liye sirf config me entry — koi code change nahi, koi deploy nahi."*

**Severity: HIGH** — ye client ke explicit requirement ka violation hai.

---

### 🔴 **GAP-2: `creative_approval_status` — 1 field, par 3 platforms**

```python
# Step 10 field table:
Amazon approval status   Enum   Read-only
Netflix approval status  Enum   Read-only (if Netflix inventory)
Disney approval status   Enum   Read-only (if Disney inventory)
                                 ↑ TEEN alag statuses

# Par schema me:
creative_approval_status: Optional[ApprovalStatusEnum] = None
                          ↑ EK hi field!
```

**Kaise handle karoge:** Amazon=APPROVED, Netflix=PENDING, Disney=REJECTED?

**Tumhara jawab:**
> *"Ye ek asli schema bug hai. Step 10 ka business rule teen independent statuses maangta hai, par schema ek hi rakhta hai. Fix:*
> ```python
> creative_approval_statuses: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
> # {"Amazon": "APPROVED", "Netflix": "PENDING", "Disney+": "REJECTED"}
>
> # Aur ek derived helper:
> @property
> def all_creatives_approved(self) -> bool:
>     return all(s == ApprovalStatusEnum.APPROVED
>                for s in self.creative_approval_statuses.values())
> ```
> *Isse partial approval bhi handle ho jaayega — Amazon ka hissa chal sakta hai jab Netflix pending hai."*

**Severity: HIGH** — implementation me pakka atkega.

---

### 🔴 **GAP-3: `Broad` vs `Wide` — naam badla par API example nahi**

```python
class AudienceProfileEnum(str, Enum):
    WIDE = "WIDE"        ← enum me WIDE
```
```json
"bundles": {
  "narrow": [...],
  "balanced": [...],
  "broad": [...]         ← API example me BROAD
}
```

**Tumhara jawab:**
> *"Naam change v2.0 me hua par API example v1.1.0 se copy hua aur update nahi hua. Ye ek asli mismatch hai jo code me bug banega. Do sawaal:*
> *1. Kya asli API `broad` key deta hai? Agar haan, to schema me mapping chahiye: `{"broad": WIDE}`*
> *2. Ya API bhi update hoga `wide` par?*
>
> *Jab tak confirm nahi hota, main enum me `WIDE` rakhta hun (client vocabulary) aur API boundary par mapping layer add karta hun."*

**Severity: MEDIUM** — chhota par pakka bug banega.

---

### 🔴 **GAP-4: `list[dict]` — untyped, Pydantic ka maksad khatam**

**Ye 4 jagah hai:**
```python
by_inventory: list[dict]        # BudgetSplitSchema
by_duration: list[dict]         # BudgetSplitSchema
reach_curve: Optional[list[dict]]  # ForecastResultSchema
validated_asins: list[dict]     # TrackingSetupSchema
```

**Aur state me poora dict hai** (Part 8.4 me).

**Tumhara jawab:**
> *"Ye ek pattern-level problem hai. `list[dict]` me Pydantic kuch validate nahi karta — galat keys bhi pass ho jaayenge. Fix: nested models banao (main Part 7.4 me sample dikha chuka hun).*
>
> *State ke liye alag baat hai — wahan `dict` LangGraph ka standard hai (performance ke liye). Par main **boundary par parse** karunga: node state se padhega → Pydantic model me convert → kaam → `.model_dump()` → wapas dict. Isse validation milegi bina LangGraph pattern todne ke."*

**Severity: MEDIUM** — silent bugs ka raasta.

---

### 🔴 **GAP-5: API Catalogue vs Steps — Direct Contradiction**

| Endpoint | Catalogue (§4) | Step section |
|---|---|---|
| `GET /api/assets/` | ✅ **Unchanged** | ❌ **REMOVED for CTV** (Step 9) |
| `GET /api/creatives/` | ✅ **Unchanged** | ❌ **REMOVED for CTV** (Step 9) |
| `GET /api/audience-sets/` | ✅ **Unchanged** | *"Nobody browses"* (Step 4) |

**Tumhara jawab:**
> *"Ye ek editorial galti hai — main catalogue update karna bhool gaya. Fix: `GET /api/assets/`, `GET /api/creatives/`, aur `GET /api/audience-sets/` ko catalogue me bhi ❌ REMOVED (CTV scope) mark karunga, ek note ke saath ki ye Display ke liye valid hain."*

**Severity: LOW** (editorial) **par credibility ke liye HIGH** — contradiction document ki reliability par sawaal uthata hai.

---

### 🔴 **GAP-6: "canary-check" — orphan item**

Summary me `❌ Removed` me hai, **par poore document me kahin nahi. Na v1.1.0 me hai.**

**Tumhara jawab:**
> *"Ye galti se summary me aa gaya — v1.1.0 me canary-check nahi tha (maine verify kiya). Main isko summary se hata dunga. Agar client ne discussion me ye mention kiya tha (chhote budget se test karna, phir scale up), to main isko ek proper 'future scope' section me explain karunga — kyunki ye actually ek useful feature hai."*

**Severity: LOW** par confusing.

---

### 🔴 **GAP-7: 9 naye endpoints, koi payload/response spec nahi**

v1.1.0 ne 5 endpoints ke poore request/response examples diye the. v2.0 ke 9 naye endpoints me **sirf naam** hai.

**Tumhara jawab:**
> *"Sahi hai. v1.1.0 me maine 5 endpoints ke poore contracts diye the, aur naye endpoints me nahi. Wajah: ye VOW ke existing endpoints hain jinke actual shapes mujhe confirm nahi hue. Main backend team se sample request/response lekar section 4.2 me add kar dunga — kyunki ye document ek contract hai, aur adhoora contract kaam nahi karta."*

**Severity: MEDIUM** — Wajahat/Vishal ko implement karne me atkega.

---

### 🔴 **GAP-8: `attribution_window` ka koi field nahi**

Document kehta hai "Default Window: 14-day" — par kya trader badal sakta hai? Schema me **koi field nahi**.

**Tumhara jawab:** *"Agar ye configurable hai to `attribution_window_days: int = 14` field chahiye. Agar fixed hai to document me saaf likhna chahiye 'not configurable in M1'. Main confirm karke likhta hun."*

---

### 🔴 **GAP-9: `budget_cap` vs `market_budgets` — farak clear nahi**

`market_budgets` me pehle se budget hai. `budget_cap` alag kyun? Daily hai? Lifetime? Per market?

**Tumhara jawab:** *"Ye ambiguous hai. Mera anumaan: `budget_cap` daily pacing cap hai. Par main confirm karke `budget_cap_daily` ya `daily_budget_cap` naam de dunga taaki confusion na ho. Aur `frequency_cap` me bhi unit clear karunga — Pydantic comment 'weekly' kehta hai par field table me nahi likha."*

---

### 🔴 **GAP-10: Step 1 ka `Type = "Fixed"` — kya matlab?**

`Goal` aur `Formats` ka type "Fixed" likha hai. Par enum me sab values maujood hain (comment ke saath). **Comment enforce nahi karta.**

**Tumhara jawab:** *"'Fixed' ka matlab hona chahiye ki M1 me trader badal nahi sakta. Par enum me CONSIDERATION/CONVERSION abhi bhi valid values hain — validate ho jaayenge. Main ek runtime validator add karunga (Part 7.2 me sample) taaki comment ek asli rule ban jaaye."*

---

### 🔴 **GAP-11: Error handling incomplete**

Sirf 3 validation protocols hain. Ye cases cover nahi:
- Budget zero/negative
- `upper < lower`
- Invalid market code
- Koi deal available nahi
- Suggest API ne khaali result diya
- API timeout / 500
- `POST /strategies/` ne 400 diya
- Multi-market me budget total ya per-market?

**Tumhara jawab:** *"Sahi hai — 3 protocols kaafi nahi. Main ek poora 'Failure Protocol' section add karunga jisme har failure case aur agent ka behaviour ho. Ye Wajahat ke graph design ke liye zaroori hai — usko pata hona chahiye kaunse edges error par jaate hain."*

---

### 🔴 **GAP-12: PG deal ka pause warning kahin nahi**

Document `deal_type` table me "Can pause? ❌ No" aur "Full budget owed" likhta hai — **par agent ke behaviour me ye kahin use nahi hota.**

**Tumhara jawab:** *"Ye ek missing safety rail hai. Agar agent PG deal chunta hai, use trader ko warn karna chahiye: 'Ye Programmatic Guaranteed deal hai — poora £X budget commit ho jaayega aur pause nahi kar sakte.' Main isko Step 2 ke behaviour me add karunga."*

**Severity: HIGH** — ye asli paisa ka risk hai.

---

### 🔴 **GAP-13: Click-through URL — CTV me kyun Required?**

CTV me remote se click nahi hota. Field ✅ UNCHANGED aur Required hai. Justification document me nahi.

**Tumhara jawab:** *"Ye v1.1.0 se aaya hai jahan Display bhi scope me tha. CTV ke liye main check karunga ki Amazon DSP isko mandatory maangta hai ya nahi. Agar mandatory hai to document me note add karunga ('Amazon DSP requires it even for CTV'). Agar nahi, to CTV ke liye Optional kar dunga."*

---

### 🔴 **GAP-14: "Did I understand correctly?" state machine me nahi hai**

Document isko *"the single most important trust mechanism"* kehta hai — par 25-line state machine me **koi confirmation node nahi hai.**

**Tumhara jawab:** *"Sahi catch. Main state machine me `confirm_extraction` node add karunga, `extract_fields` ke turant baad, ek chhote interrupt ke saath. Agar ye product ka sabse important trust mechanism hai, to ise state machine me first-class hona chahiye."*

**Severity: MEDIUM** — document apne hi statement ko follow nahi karta.

---

### 🔴 **GAP-15: `inventory_tier` "Derived" — par kaise?**

Field table kehta hai "Derived" par derivation logic kahin nahi. `GET /api/inventory-sources/` se? Provider name se? Mapping table se?

**Tumhara jawab:** *"Mera anumaan: `GET /api/inventory-sources/` (jo ➕ NEW endpoint hai) provider→tier mapping deta hai. Par document ne ye connect nahi kiya. Main clarify karke likhunga: 'Tier is resolved from GET /api/inventory-sources/, keyed on the deal's provider.' Ye Wajahat ke liye zaroori hai."*

---

### 🔴 **GAP-16: `state` me `dict`, `matching_mode` string, node naming inconsistent**

Chhote consistency issues:
- `matching_mode: str` — enum hona chahiye
- `deal_type: str` — enum hona chahiye
- `current_stage: str` — enum/Literal hona chahiye
- Node names: `tracking_setup` aur `credit_check` pattern se hatke hain (`setup_tracking`, `check_credit` hona chahiye)
- `durations: list[DurationEnum]` (string `"30"`) vs `duration_seconds: int` (30) — type mismatch

**Tumhara jawab:** *"Ye sab consistency fixes hain, main ek pass me theek kar dunga. Ek contract document me consistency matter karti hai — kyunki 4 log isse code likhenge."*

---

## 11.3 — 🎯 David ke Comments ka Framework

Jab tum David ke 28 comments dekhoge, wo mostly in 6 buckets me girenge:

| Bucket | Kya hoga | Tumhara approach |
|---|---|---|
| **1. Open Questions** (5) | "Ye clarify karo" | ✅ Tumne khud flag kiya — **taqat hai**. Recommendation ke saath jawab do |
| **2. Real inconsistencies** (GAP 1-5, 15) | "Ye contradiction hai" | ✅ Maan lo, fix suggest karo. **Argue mat karo** |
| **3. Missing detail** (GAP 7, 11) | "Iska contract kahan hai?" | ✅ "Add kar dunga" — commit do |
| **4. Business rule questions** | "Kya PG deal me warning hai?" | ✅ Business logic samjha kar jawab do (GAP-12) |
| **5. Scope questions** | "Ye M1 me hai ya M2?" | ✅ Scope table se jawab do |
| **6. Editorial/wording** | "Ye line confusing hai" | ✅ Turant fix kar do, discussion na karo |

### 🎯 Reply karte waqt 5 rules

1. **Pehle maano, phir samjhao.** *"Sahi catch"* → phir fix. Defensive na bano.
2. **Har jawab me ek recommendation do.** Sirf "confirm karna padega" na bolo — apni raay do.
3. **Jo tumne khud flag kiya, uska credit lo.** *"Maine isko deliberately ⚠ mark kiya kyunki assume karna risky tha"* — ye maturity dikhata hai.
4. **Business reason do, sirf technical nahi.** *"Ye field Optional hai kyunki Netflix reach data nahi deta"* > *"Ye Optional hai."*
5. **Jo galat hai, turant maan lo.** Contradictions defend karne se document ki credibility jaati hai, tumhari nahi.

---

# PART 12 — END-TO-END WORKED EXAMPLE
### Ek brief, 13 steps, poora chalta hua

Ye poora document ek example me. Isko padh lo to sab jud jaayega.

---

## Setup

**Advertiser:** BrightPath Online Courses
**Business:** UK me online professional courses bechta hai, apni website `brightpath.co.uk` par
**Amazon par:** ek study-guide book bechta hai (ASIN `B08N5WRWNW`)
**Trader:** Sarah (media buyer)
**Manager:** David Moss (approval authority)

---

## 💬 Turn 1 — Brief

```
Sarah: "BrightPath ke liye ek CTV campaign chahiye. UK me August me
        £10,000. Prime Video aur Netflix dono. 15 aur 30 second ke
        ads hain. Education website hai. Max reach chahiye."
```

### 🔧 STEP 1 — extract_fields
```
Agent parse karta hai:
  "UK"                → markets = ["GB"], primary_currency = "GBP"
  "August"            → flight_dates = {lower:"2026-08-01", upper:"2026-08-31", bounds:"[)"}
  "£10,000"           → market_budgets = [{market:"GB", budget:"10000.00", base_bid:???}]
  "Prime Video"       → formats includes "prime_video"
  "Netflix"           → formats includes "streaming_tv"
  "15 aur 30 second"  → durations = ["15", "30"]
  "Education website" → product_location = "NOT_SOLD_ON_AMAZON"
                      → product_categories = [1]
  "Max reach"         → kpi = "reach"
  CTV default         → goal = "AWARENESS"

Khaali: strategy_name, base_bid

🔧 GET /api/contextual-targeting/GB/product-categories/
   ← Education = ID 1 ✅ confirmed
```

### 💬 Turn 2 — "Did I understand correctly?" (➕ NEW)
```
Agent: "Samajh gaya. Confirm karo:

┌───────────────────┬──────────────────────────────────────┐
│ Market            │ United Kingdom (GB)                  │
│ Currency          │ GBP (£)                              │
│ Flight            │ 1 Aug – 30 Aug 2026 (30 din)         │
│ Budget            │ £10,000                              │
│ Formats           │ Prime Video + Streaming TV (Netflix) │
│ Durations         │ 15s aur 30s                          │
│ Goal              │ Awareness (CTV ke liye fixed)        │
│ KPI               │ Reach                                │
│ Selling location  │ Off Amazon (own website)             │
│ Product category  │ Education                            │
└───────────────────┴──────────────────────────────────────┘

Maine ye ASSUME kiya:
 • Currency GBP (kyunki UK) — agar USD reporting chahiye to batao
 • 1–30 Aug (poora August) — ya specific dates chahiye?
 • Goal Awareness — CTV ke liye ye fixed hai (client-confirmed:
   'CTV se funnel me neeche kuch track karna mushkil hai')

Do cheezein chahiye:
 1. Strategy ka naam?
 2. Base bid (max CPM)? Prime Video ke liye typical £28-32 hota hai."

Sarah: "Naam BrightPath_Autumn_Awareness_2026. Base bid £32."
```

### 🔧 Name uniqueness check
```
🔧 GET /api/strategies/check_strategy_name_uniqueness/?name=BrightPath_Autumn_Awareness_2026
   ← {"is_unique": true} ✅

State update:
  strategy_name = "BrightPath_Autumn_Awareness_2026"
  market_budgets = [{market:"GB", budget:"10000.00", base_bid:"32.00"}]
  current_stage = "inventory"
```

---

## 🔧 STEP 2 — select_inventory (Tier Fork)

```
🔧 GET /api/deals/?markets=GB&formats=streaming_tv,prime_video
🔧 GET /api/rates/ctv/GB/

Available deals:
┌────────────────────────────────────┬───────────┬────────┬──────────┬───────────────────────┐
│ Deal                               │ Type      │ CPM    │ Lengths  │ Tier (derived)        │
├────────────────────────────────────┼───────────┼────────┼──────────┼───────────────────────┤
│ Prime Video | Preferred | UK - 15  │ Preferred │ £20.00 │ 15       │ AMAZON_OWNED          │
│ Prime Video | Preferred | UK - 30  │ Preferred │ £28.88 │ 30       │ AMAZON_OWNED          │
│ Prime Video | Education | UK - 30  │ Preferred │ £31.50 │ 30       │ AMAZON_OWNED          │
│ Netflix | Preferred | UK - 15      │ Preferred │ £24.00 │ 15       │ THIRD_PARTY_PRECURATED│
│ Netflix | Preferred | UK - 30      │ Preferred │ £32.00 │ 30       │ THIRD_PARTY_PRECURATED│
└────────────────────────────────────┴───────────┴────────┴──────────┴───────────────────────┘
```

### 💬 Turn 3 — Genre upsell (➕ NEW)
```
Agent: "Deals mil gaye. Ek suggestion hai:

Prime Video par ek EDUCATION genre deal available hai @ £31.50 CPM
(ROS £28.88 ke muqable — £2.62 mehnga).

Tumhara product education courses hai. Education content dekhne wale
log tumhare target audience se bahut match karte hain.

  ROS 30s       @ £28.88 → £6,000 me 207,756 impressions
  Education 30s @ £31.50 → £6,000 me 190,476 impressions
                            ↑ 17,280 impressions kam, par har
                              impression zyada relevant

⚠ Aur ek baat: dono deals PREFERRED hain — matlab tum inhe kabhi
   bhi pause kar sakte ho, koi budget commitment nahi. (Agar PG
   deal hoti, poora budget commit ho jaata aur pause nahi kar sakte.)

Kya karun — ROS ya Education genre?"

Sarah: "Education genre lo. Aur Netflix bhi rakho."
```

### State update
```
selected_deals = [
  {deal_id:"EXT7P...", name:"Prime Video | Education | UK - 30",
   cpm:"31.50", inventory_tier:"AMAZON_OWNED", provider:"Prime Video",
   genre:"Education", ad_lengths:["30"], deal_type:"Preferred"},

  {deal_id:"EXT9K...", name:"Prime Video | Preferred | UK - 15",
   cpm:"20.00", inventory_tier:"AMAZON_OWNED", provider:"Prime Video",
   genre:null, ad_lengths:["15"], deal_type:"Preferred"},

  {deal_id:"EXT4M...", name:"Netflix | Preferred | UK - 30",
   cpm:"32.00", inventory_tier:"THIRD_PARTY_PRECURATED", provider:"Netflix",
   genre:null, ad_lengths:["30"], deal_type:"Preferred"},

  {deal_id:"EXT2N...", name:"Netflix | Preferred | UK - 15",
   cpm:"24.00", inventory_tier:"THIRD_PARTY_PRECURATED", provider:"Netflix",
   genre:null, ad_lengths:["15"], deal_type:"Preferred"}
]
inventory_tier = "MIXED"   ← Amazon + 3P dono
current_stage = "budget_split"

⚠ Disney+ nahi chuna → curation_requirements khaali rahega
```

---

## 🔧 STEP 3 — propose_budget_split (➕ NEW)

```
Agent-side ganit (koi API nahi):

Do inventories (Prime, Netflix) × Do durations (15s, 30s) = 4 combinations

CPMs:
  Prime 15s   £20.00
  Prime 30s   £31.50 (Education genre)
  Netflix 15s £24.00
  Netflix 30s £32.00

Agent chunta hai: EVEN_BY_IMPRESSIONS
Kyun? Kyunki KPI = reach hai → baraabar impressions se reach
      zyada evenly faila
```

### 💬 Turn 4 — Budget split proposal
```
Agent: "Budget split propose kar raha hun.

Maine EVEN_BY_IMPRESSIONS chuna — har combination ko lagbhag
baraabar impressions:

┌─────────────┬──────┬─────────┬────────┬─────────────┐
│ Inventory   │ Dur  │ Budget  │ CPM    │ Impressions │
├─────────────┼──────┼─────────┼────────┼─────────────┤
│ Prime Video │ 15s  │ £1,900  │ £20.00 │  95,000     │
│ Prime Video │ 30s  │ £2,993  │ £31.50 │  95,000     │
│ Netflix     │ 15s  │ £2,280  │ £24.00 │  95,000     │
│ Netflix     │ 30s  │ £2,827  │ £32.00 │  88,344     │
├─────────────┼──────┼─────────┼────────┼─────────────┤
│ TOTAL       │      │ £10,000 │        │ 373,344     │
└─────────────┴──────┴─────────┴────────┴─────────────┘

Per inventory:
  Prime Video: £4,893 (49%)
  Netflix:     £5,107 (51%)

⚠ Dhyan do: is method me kharch 30s ki taraf jhuka hai (kyunki
   30s ka CPM zyada hai). Agar tum baraabar PAISA chahte ho
   (EVEN_BY_BUDGET), to 15s ko zyada impressions milenge:

   EVEN_BY_BUDGET me: £2,500 each →
     Prime 15s  125,000 imp
     Prime 30s   79,365 imp
     Netflix 15s 104,167 imp
     Netflix 30s  78,125 imp
     Total: 386,657 (13,313 zyada!)

Kaunsa chahiye? Ya custom % batao."

Sarah: "EVEN_BY_IMPRESSIONS theek hai. Par Prime me thoda zyada
        daalo — 60/40 Prime/Netflix."
```

### 💬 Agent adjust karta hai
```
Agent: "Theek hai, CUSTOM split:

┌─────────────┬──────┬─────────┬────────┬─────────────┐
│ Inventory   │ Dur  │ Budget  │ CPM    │ Impressions │
├─────────────┼──────┼─────────┼────────┼─────────────┤
│ Prime Video │ 15s  │ £2,340  │ £20.00 │ 117,000     │
│ Prime Video │ 30s  │ £3,660  │ £31.50 │ 116,190     │
│ Netflix     │ 15s  │ £1,800  │ £24.00 │  75,000     │
│ Netflix     │ 30s  │ £2,200  │ £32.00 │  68,750     │
├─────────────┼──────┼─────────┼────────┼─────────────┤
│ TOTAL       │      │ £10,000 │        │ 376,940     │
└─────────────┴──────┴─────────┴────────┴─────────────┘

Prime £6,000 (60%) · Netflix £4,000 (40%) ✅"
```

---

## 🔧 STEP 4 — suggest_audiences (Mandatory)

```
🔧 POST /api/audience-sets/suggest/
{
  "market": "GB",
  "goal": "AWARENESS",
  "product_categories": ["Education"],
  "brief_text": "Online professional courses for UK adults,
                 maximum awareness reach"
}
   ← {"id": "sug_5521", "status": "processing"}

🔧 GET /api/audience-sets/suggest/sug_5521/
   ← {"status":"complete", "bundles": {...}}
```

### 💬 Turn 5 — Teen options + Effective CPM (➕ NEW)
```
Agent: "3,400 segments me se vector search karke 3 options banaye.
        (Koi manual browsing nahi — pgvector + OpenAI se semantic match.)

┌──────────┬─────────────────────────────┬───────┬───────────┬──────────┐
│ Option   │ Segments                    │ VCPM  │ Available │ Eff. CPM │
│          │                             │ (avg) │ reach     │ (Prime30)│
├──────────┼─────────────────────────────┼───────┼───────────┼──────────┤
│ NARROW   │ Higher Education Seekers    │ £1.85 │   450,000 │ £33.35   │
├──────────┼─────────────────────────────┼───────┼───────────┼──────────┤
│ BALANCED │ + E-Learning & Tech         │ £1.74 │ 1,650,000 │ £33.24   │
│ ⭐ REC   │   Enthusiasts               │       │           │          │
├──────────┼─────────────────────────────┼───────┼───────────┼──────────┤
│ WIDE     │ + General Career            │ £1.56 │ 5,150,000 │ £33.06   │
│          │   Advancement               │       │           │          │
└──────────┴─────────────────────────────┴───────┴───────────┴──────────┘

⚠ Dhyan do — 'Effective CPM' me maine audience fee (VCPM) deal CPM
   ke UPAR jodi hai. Ye asli daam hai jo tum doge:
     Prime 30s deal £31.50 + Narrow VCPM £1.85 = £33.35

   Narrow DO tarah se mehnga hai: kam log AUR zyada fee.

Tumhara KPI reach hai. Isliye main BALANCED recommend karta hun —
1.65M available reach, aur VCPM Narrow se sasti.

⚠ Ek baat: ye audiences SIRF Prime Video par lagengi (£6,000 hissa).
   Netflix par Amazon audiences apply nahi hoti — Netflix apni
   targeting deta hai jiska alag CPM lagta hai.

Kaunsa chunoge? Aur matching mode — Similar ya Exact?"

Sarah: "Balanced. Similar mode."
```

### State update
```
audience_options = [teeno bundles, sab save]
chosen_audience = {profile: "BALANCED", ids: ["aud_101","aud_102"], vcpm_fee: "1.74"}
matching_mode = "Similar"
current_stage = "targeting"
```

---

## 🔧 STEP 5 — apply_targeting (➕ NEW, Optional)

```
🔧 GET /api/strategies/locations/GB/
🔧 POST /api/contextual-targeting/GB/products/
```

### 💬 Turn 6
```
Agent: "Optional targeting filters — chaaho to skip kar do:

 1. Location    — poore UK me ya specific cities?
 2. Device      — Connected TV only, ya mobile/tablet bhi?
 3. Content exclusions — kis tarah ke content ke saath NAHI dikhana?
 4. Instream position — pre/mid/post-roll?
 5. Mobile environment — in-app ya mobile web?

⚠ Note: Genre exclusions, day-parting aur language targeting VOW
   me abhi support nahi hain (future scope)."

Sarah: "Connected TV only. Aur News aur True Crime content exclude
        kar do — brand safety."

Agent: "Set:
  device_types = ['Connected TV']
  content_category_exclusions = ['News', 'True Crime']
  Baaki khaali (poora UK, sab positions)"
```

---

## 🔧 STEP 6 — predict_reach (🔴 HONESTY RULE)

```
🔧 POST /api/audience-sets/reach-forecast/  (Prime portion ke liye)
{
  "markets": ["GB"],
  "budget": "6000.00",
  "base_bid": "32.00",
  "audience_set_ids": ["aud_101", "aud_102"],
  "flight_dates": {"lower":"2026-08-01", "upper":"2026-08-31"}
}
   ← {
       "is_available": true,
       "estimated_impressions": 180505,
       "estimated_unique_reach": 118000,
       "average_frequency": 1.53,
       "indicative_cpm": "33.24",
       "reach_curve": [
         {"budget":1500, "reach":38000},
         {"budget":3000, "reach":70000},
         {"budget":4500, "reach":97000},
         {"budget":6000, "reach":118000}
       ]
     }

Netflix portion: is_available = FALSE
→ Sirf ganit: £4,000 ÷ avg CPM £27.50 × 1000 = 145,455 impressions
```

### 💬 Turn 7 — Forecast with Honesty Rule
```
Agent: "Forecast taiyar. Do hisso me — kyunki dono ki capabilities
        alag hain:

╔══════════════════════════════════════════════════════════════════╗
║ ✅ PRIME VIDEO (£6,000)                    [AMAZON_OWNED]        ║
║    Effective CPM      £33.24  (deal £31.50 + VCPM £1.74)         ║
║    Impressions        180,505                                    ║
║    Unique reach       118,000        ← ASLI FORECAST             ║
║    Avg frequency      1.53           ← ASLI FORECAST             ║
║    Reach curve        ✅ available                                ║
║                                                                  ║
║    📊 Reach curve:                                                ║
║       £1,500 →  38,000                                           ║
║       £3,000 →  70,000  (+32,000)                                ║
║       £4,500 →  97,000  (+27,000)                                ║
║       £6,000 → 118,000  (+21,000)                                ║
║       ↑ Diminishing returns — pehla £1,500 sabse efficient tha    ║
║                                                                  ║
║ ⚠️  NETFLIX (£4,000)                 [THIRD_PARTY_PRECURATED]    ║
║    Rate-card CPM      £24.00 (15s) / £32.00 (30s)                ║
║    Impressions        143,750        ← ganit se derive kiya      ║
║    Unique reach       ❌ NOT AVAILABLE                            ║
║    Avg frequency      ❌ NOT AVAILABLE                            ║
║                                                                  ║
║    KYUN: Netflix apna viewer-level data Amazon DSP ke saath      ║
║    share nahi karta. Main tumhe reach ka number DE SAKTA HUN     ║
║    par wo GUESS hoga — aur main guess nahi karunga.              ║
╠══════════════════════════════════════════════════════════════════╣
║ TOTAL IMPRESSIONS: 324,255                                       ║
║                                                                  ║
║ ⚠️  TOTAL UNIQUE REACH: ADD NAHI KAR SAKTE                        ║
║    Prime ka 118,000 confirmed hai. Netflix ka data nahi.         ║
║    Aur hota bhi, to jodna GALAT hota — wahi insaan Prime aur     ║
║    Netflix dono dekh sakta hai (double counting). Cross-platform ║
║    deduplication industry me solved problem nahi hai.            ║
╚══════════════════════════════════════════════════════════════════╝

Frequency 1.53 tumhare reach KPI ke liye accha hai — audience
sahi size ki hai, koi repair ki zaroorat nahi.

⚠ Ek suggestion (reach curve se): £4,500 se £6,000 tak jaane par
sirf 21,000 naye log milte hain. Agar tum £1,500 Netflix se Prime
me shift karo, ya doosre market me daalo, to zyada efficient ho
sakta hai. Chahoge to main option dikhaun?"

Sarah: "Nahi, aise theek hai. Approval ke liye bhej do."
```

**⚠ Dhyan do:** repair loop **chala hi nahi**, kyunki forecast healthy tha. Loop sirf zaroorat par chalta hai.

---

## ⏸️ STEP 7 — PLAN APPROVAL (➕ NEW, interrupt)

```
Agent: "Plan David Moss ko approval ke liye bhej diya.

⏸️ Main yahan RUK gaya hun. Budget £10,000 LOCK ho gaya hai —
   David ne exactly ye plan dekha hai, aur ab isko badla nahi
   ja sakta jab tak approval na aaye.

   Agar kuch badalna hai, plan reject karwana padega aur audience
   step se dobara shuru karna padega."

⏸️ interrupt() → STATE PERSIST → PROCESS BAND

──────────────── 19 ghante baad ────────────────
(Server 2 baar restart hua. Kuch bhi nahi bhoola.)

David dashboard par plan dekhta hai:
  Strategy: BrightPath_Autumn_Awareness_2026
  Budget: £10,000
  Prime £6,000 → 118,000 reach (confirmed)
  Netflix £4,000 → 143,750 impressions (reach unavailable)
  Total impressions: 324,255

David: ✅ APPROVE

state:
  approval_status = "APPROVED"
  approved_by = "david.moss@calyxio.ai"
  approved_at = "2026-07-30T09:35:00Z"

→ STATE LOAD → GRAPH RESUMES from Step 8
```

---

## 🔧 STEP 8 — create_strategy

```
🔧 POST /api/strategies/
{
  "name": "BrightPath_Autumn_Awareness_2026",
  "advertiser_id": "353eea43-bc42-456f-ba4f-3d3e20ea6bc8",
  "channel_type": "dsp",
  "goal": "AWARENESS",
  "kpi_target_type": "reach",
  "primary_currency": "GBP",
  "flight_dates": {"lower":"2026-08-01","upper":"2026-08-31","bounds":"[)"},
  "durations": ["15","30"],
  "formats": ["prime_video","streaming_tv"],
  "product_categories": [1],
  "product_location": "NOT_SOLD_ON_AMAZON",
  "market_budgets": [{"market":"GB","budget":"10000.00","base_bid":"32.00"}],
  "selected_deals": ["EXT7P...","EXT9K...","EXT4M...","EXT2N..."],
  "selected_audience_sets": ["aud_101","aud_102"],
  ...
}
   ← 201 Created
     {"id":"VMA2026412", "status":"created", "is_syncing":false}

🔧 + audience set creation via simplified CTV endpoint
   ← {"audience_set_id": "as_88213"}

Agent: "✅ Strategy VMA2026412 ban gayi. Ab creative chahiye."
```

**⚠ Note:** Yahan `status: "created"` aaya (Open Question #3 ka jawab pending — `"draft"` bhi aa sakta tha).

---

## 🔧 STEP 9 — upload_creative + 🔴 DURATION CHECK

```
Sarah: BrightPath_Brand_30s.mp4 upload karti hai

🔧 POST /api/assets/amz_assets/gen_upload_urls/
   ← {"upload_url": "https://s3...", "expires_in": 3600}
   → file SEEDHA S3 par gayi (VOW server se guzri nahi)

🔧 POST /api/assets/amz_assets/register/
   ← {"asset_id":"asset_44521", "duration_seconds": 30}

DURATION MATCH CHECK:
  approved durations = ["15", "30"]
  uploaded duration  = 30
  → ✅ MATCH! (30 approved list me hai)
```

### 💬 Turn 8
```
Agent: "✅ 30-second video register ho gaya (asset_44521).
        Duration approved plan se match karta hai (15s aur 30s
        dono approved the).

        ⚠ Par plan me 15s ka bhi budget tha — £4,140. Uske liye
        bhi ek 15-second video chahiye. Upload karogi?

        Click-through URL bhi chahiye har creative ke liye."

Sarah: "15s wala kal upload karungi. URL: https://brightpath.co.uk/courses"
```

### ⚠ Yahan ek gap dikha (real implementation issue)
```
Agent: "Theek hai. Par ek baat — 15s creative ke bina wo £4,140
        ka hissa deliver nahi hoga.

        Do options:
        A) Kal 15s upload karo, tab tak strategy created rahegi
           (activate nahi karenge)
        B) 15s ka budget 30s me shift kar dun — par isse plan
           badlega aur dobara approval chahiye"

Sarah: "Option A. Kal upload karungi."
```

**💡 Ye scenario document me cover NAHI hai** — "multiple durations, partial creative upload" ka handling. **Ye ek gap hai jo main note kar raha hun.**

---

## 🔧 STEP 10 — platform_creative_approval (➕ NEW)

```
30s video dono platforms ko bheja gaya.

──── 4 ghante baad ────

Amazon:  ✅ APPROVED
Netflix: ⏳ PENDING (48h SLA)

Agent: "Creative approval status:
          Amazon  ✅ APPROVED
          Netflix ⏳ PENDING (48 ghante ka SLA)

        Netflix ka hissa uske approve hone tak deliver nahi hoga.
        Amazon ka hissa taiyar hai.

        ⚠ Note: Netflix ka approval status VOW API se aa raha hai
        ya externally track hota hai — ye abhi document me open
        question hai."

──── 40 ghante baad ────
Netflix: ✅ APPROVED

Agent: "✅ Netflix ne bhi approve kar diya. Dono platforms clear."
```

---

## 🔧 STEP 11 — tracking_setup

### 💬 Turn 9
```
Agent: "Ab tracking setup. Teen sawaal:

1. Amazon par bechte ho? (Tumne pehle bataya tha 'education
   website' — to main NAHI maan raha hun, par confirm karo)

2. Apni website par bechte ho?

3. Ad tag registered hai?"

Sarah: "Amazon par ek study guide book bechte hain — ASIN B08N5WRWNW.
        Aur haan, apni website par courses bechte hain."
```

### 🔧 ASIN validation
```
🔧 POST /api/contextual-targeting/GB/asin-validation/
{"asins": ["B08N5WRWNW"]}
   ← {
       "valid_asins": [{
         "asin": "B08N5WRWNW",
         "title": "BrightPath Professional Skills Study Guide",
         "brand": "BrightPath",
         "product_category": "Books"
       }],
       "invalid_asins": []
     }
```

### 🔧 Ad tag check
```
Agent (checks): ❌ Koi ad tag registered nahi mila
```

### 💬 Turn 10 — ⚠ Ad tag warning
```
Agent: "✅ ASIN B08N5WRWNW valid hai:
        'BrightPath Professional Skills Study Guide' (Books)

        Note: tum Off-Amazon ho (courses apni website par bechte
        ho), to ASIN optional hai. Par isse main HALO SALES track
        kar sakta hun — matlab jo log ad dekh kar Amazon par ye
        book kharidein, wo bhi report me aayenge. Accha bonus hai.

        ⚠⚠ ZAROORI: Ad tag registered NAHI hai.

        Ad tag ke bina main brightpath.co.uk par ye track nahi
        kar paunga:
          • Course page views
          • Application form submissions
          • Checkout / enrollment

        Aur ye BAHUT important hai: tracking sirf tag lagne ke
        BAAD ka data record karti hai. Agar campaign 1 August
        se chal gaya aur tag 10 August ko laga, to 1-10 August
        ka data HAMESHA KE LIYE GAYA. Peeche ka data recover
        nahi hota.

        Setup:
        1. Ye code brightpath.co.uk ke <head> me daalo:
           <script src="https://s.amazon-adsystem.com/..."></script>
        2. Course page par: amzn('trackEvent','PageView')
        3. Application form par: amzn('trackEvent','Application')
        4. Enrollment par: amzn('trackEvent','Checkout')

        Ho jaaye to batao, main verify kar dunga.

        Ya: bina conversion tracking chala sakte ho — par phir
        sirf reach/frequency naapoge, ROI nahi."

Sarah: "Dev team se karwati hun. Aaj sham tak ho jaayega."

──── 3 ghante baad ────
Sarah: "Tag laga diya"

Agent (verify): ✅ Ad tag registered

🔧 GET /api/conversions/definitions/
   ← ["Page view", "Add to shopping cart", "Checkout", "Application"]

Agent: "✅ Ad tag verify ho gaya. Kaunse events track karne hain?"

Sarah: "Page view, Application, Checkout"

state:
  tracking_setup = {
    sells_on_amazon: true,
    validated_asins: [{asin:"B08N5WRWNW", title:"...", brand:"BrightPath"}],
    sells_on_own_site: true,
    ad_tag_registered: true,
    ad_tag_conversions: ["Page view","Application","Checkout"]
  }
```

**⚠ Note:** Yahan OQ-1 ka problem asli me dikha — `product_location` aur ASIN Step 8 ke `POST /strategies/` me chahiye the, par yahan (Step 11) me mile. To ab **PATCH** karna padega:
```
🔧 PATCH /api/strategies/VMA2026412/
{"product_asins": ["B08N5WRWNW"], "ad_tag_conversions": [...]}
```
**Ye extra call OQ-1 ka seedha nateeja hai.** Agar ASIN Step 1 me hota, ye call nahi lagta.

---

## 🔧 STEP 12 — credit_check (➕ NEW)

```
🔧 GET /api/credits/summary/
   ← {"balance": "7500.00", "currency": "GBP"}

Strategy budget: £10,000
Balance:         £ 7,500
Sufficient:      FALSE ❌
```

### 💬 Turn 11
```
Agent: "⚠ Activate karne se pehle ek cheez:

        Account balance:  £ 7,500
        Strategy budget:  £10,000
        Kami:             £ 2,500

        Do options:

        A) £2,500 (ya zyada) top-up karo
           Main Stripe payment link bhej deta hun

        B) Budget £7,500 kar do
           ⚠ Par isse plan badlega:
             • Prime reach 118,000 → ~97,000 (reach curve se)
             • Total impressions 324,255 → ~243,000
             • Aur David ko DOBARA approve karna padega
               (kyunki usne £10,000 wala plan approve kiya tha)

        Kya karna hai?"

Sarah: "Top-up karti hun"

🔧 POST /api/credits/stripe/
   → payment link → Sarah ne £3,000 daal diye

🔧 GET /api/credits/summary/
   ← {"balance": "10500.00"}

Sufficient: TRUE ✅
state: credit_sufficient = true
```

---

## 💰 STEP 13 — activate (THE SINGLE SPEND ACTION)

### 💬 Turn 12 — Final confirmation
```
Agent: "Sab taiyar hai. Final check:

╔═══════════════════════════════════════════════════════════════╗
║ Strategy         BrightPath_Autumn_Awareness_2026             ║
║ ID               VMA2026412                                   ║
║ Budget           £10,000                                      ║
║ Flight           1–30 Aug 2026 (30 din)                       ║
║ Market           United Kingdom (GB)                          ║
║ Formats          Prime Video + Netflix                        ║
║ Durations        30s ✅ uploaded  ·  15s ⚠ pending            ║
║                                                               ║
║ ✅ Plan approval        David Moss · 30 Jul 09:35 UTC         ║
║ ✅ Creative approval    Amazon ✅  ·  Netflix ✅               ║
║ ✅ Tracking             ASIN ✅ · Ad tag ✅ · 3 events         ║
║ ✅ Credit               £10,500 available                     ║
╚═══════════════════════════════════════════════════════════════╝

⚠ ACTIVATE karne par KHARCH SHURU ho jaayega. Ye is poore flow
  ka pehla aur ek hi spend action hai — Steps 1 se 12 tak
  sab free tha.

⚠ Aur ek baat: 15-second creative abhi pending hai. Us hisse ka
  £4,140 budget tab tak deliver nahi hoga jab tak 15s video
  upload aur approve nahi hota.

Confirm karun?"

Sarah: "Haan, activate kar do"
```

### 🔧 Activation
```
🔧 POST /api/strategies/VMA2026412/set_status/
{"status": "active"}
   ← 200 OK {"id":"VMA2026412", "status":"active", "is_syncing":true}

Agent: "✅ CAMPAIGN ACTIVE HAI.

        VOW ka outbound sync engine ab Amazon DSP par Campaigns
        aur Ad Groups bana raha hai:

        Campaign: BrightPath_Autumn_Awareness_2026
        ├── Ad Group: Prime Video Education 30s
        │     ├── Deal: EXT7P... (£31.50 CPM)
        │     ├── Audience: as_88213 (Balanced, Similar mode)
        │     └── Creative: asset_44521 (30s)
        └── Ad Group: Netflix 30s
              ├── Deal: EXT4M... (£32.00 CPM)
              └── Creative: asset_44521 (30s)

        Sync me 10-15 minute lagenge. Delivery 1 August se shuru
        hogi.

        ⏳ Pending: 15-second creative (£4,140 ka hissa)

        Main notify karunga jab pehle impressions aayenge."
```

---

## 📊 Poora Flow ka Summary — Kya hua

| Step | Kya hua | API calls | Loops |
|---|---|---|---|
| 1 | Basics + "did I understand?" | 2 | — |
| 2 | Deals + tier fork + genre upsell | 2 | — |
| 3 | Budget split (agent-side) | 0 | Sarah ne adjust kiya |
| 4 | 3 audience options + effective CPM | 2 | — |
| 5 | Targeting (device + exclusions) | 2 | — |
| 6 | Forecast + **honesty rule** | 1 | Repair chala nahi (healthy) |
| 7 | ⏸️ **Plan approval** (19h wait) | 0 | — |
| 8 | Create real strategy | 2 | — |
| 9 | Creative upload + duration check | 2 | ✅ match |
| 10 | Platform approval (44h) | ? | — |
| 11 | Tracking (ASIN + ad tag) | 2 + **1 PATCH** | Ad tag setup wait |
| 12 | Credit check | 2 | Top-up loop |
| 13 | 💰 **Activate** | 1 | — |

**Total: ~21 API calls, 12 conversation turns, 3 waits (19h + 44h + 3h)**

### Is example se seekhne wali 8 baatein

1. **Honesty rule asli me kaisa dikhta hai** — Prime ka reach mila, Netflix ka nahi, aur agent ne saaf bataya
2. **Effective CPM** trader ko asli daam dikhata hai (£33.35, na ki £31.50)
3. **Genre upsell** ne trader ko ek behtar option diya, numbers ke saath
4. **Budget split** me agent ne apni assumption batayi, trader ne adjust kiya
5. **interrupt()** ne 19 ghante ka gap handle kiya, server restart ke baad bhi
6. **Ad tag warning** ne ek irreversible galti roki
7. **Credit check** last me hua, isliye planning free rahi
8. **⚠ OQ-1 ka asar** asli me dikha — ek extra `PATCH` call lagana pada

---

# PART 13 — GLOSSARY A–Z (Quick Lookup)

| Term | Full form | Matlab (ekdum simple) |
|---|---|---|
| **Ad Group** | — | Amazon DSP me campaign ke andar ek group (deal + audience + creative ka combo) |
| **Ad Tag** | — | Website par lagne wala chhota code jo Amazon ko batata hai "kisi ne kya kiya" |
| **Adaptive Canvas** | — | Chat ke saath badalta UI (Basil ka kaam) |
| **AMC** | Amazon Marketing Cloud | Amazon ka data room — advertiser ka purana campaign data |
| **Annotated[list, add_messages]** | — | LangGraph pattern: "message replace na karo, peeche jodo" |
| **Artifact** | — | UI par dikhne wali visual cheez (card, chart, table) |
| **ASIN** | Amazon Standard Identification Number | Amazon par product ka unique code (`B08N5WRWNW`) |
| **Async** | Asynchronous | Kaam turant nahi hota — "shuru karo" aur "ho gaya?" do calls |
| **ATC** | Add To Cart | Cart me daalna |
| **Attribution** | — | Credit dena: "ye sale ad ki wajah se hui" |
| **Attribution Window** | — | Kitne din tak ad ko credit milega (yahan 14 din) |
| **Audience Set** | — | Logon ka group jinhe target karna hai |
| **Audit Trail** | — | Kaam ka record — kisne kya kiya, kab kiya |
| **Base Bid** | — | Max CPM jo tum dene ko taiyar ho |
| **BaseModel** | — | Pydantic ka base class |
| **bounds "[)"** | — | `[` = ye din shamil, `)` = ye din shamil nahi |
| **Brand Safety** | — | Brand ki izzat bachana — galat content ke saath ad na dikhe |
| **Brief** | — | Trader ka likha hua campaign requirement |
| **Budget Cap** | — | Kharch ki upar ki limit (⚠ daily ya lifetime? unclear) |
| **Bundle** | — | Audience segments ka group |
| **Campaign** | — | Amazon DSP ka top-level container |
| **Canary check** | — | Chhote budget par pehle test karo, phir scale up (⚠ orphan item) |
| **Checkpointer** | — | LangGraph ka state save/load karne wala hissa |
| **Config-driven** | — | Config file me likha (code me nahi) — badalna aasan |
| **Connected TV (CTV)** | — | Internet se juda TV |
| **Contextual Targeting** | — | Content ke hisaab se ad dikhana (banda kaun hai, uske hisaab se nahi) |
| **Conversion** | — | Koi kaam ho jaana jo tum chahte the |
| **CPA** | Cost Per Acquisition | Ek customer banane ka daam |
| **CPC** | Cost Per Click | Ek click ka daam |
| **CPDPV** | Cost Per Detail Page View | Ek product page view ka daam |
| **CPM** | Cost Per Mille | 1,000 impressions ka daam |
| **CTR** | Click Through Rate | Kitne % ne click kiya |
| **Curation** | — | Deal ko haath se banana (automatic nahi) |
| **Deal** | — | Publisher ke saath pehle se tay hua sauda |
| **Deduplication (dedup)** | — | Duplicate hatana — same insaan ko ek hi baar ginna |
| **Derived** | — | System khud nikalta hai (trader nahi bharta) |
| **Diminishing Returns** | — | Jitna aage badho, utna kam faayda |
| **DPV** | Detail Page View | Product page kitni baar khula |
| **DSP** | Demand Side Platform | Kharidne walon ka software |
| **Effective CPM** | — | Deal CPM + audience VCPM = asli daam |
| **Embedding** | — | Text ko numbers ki list me badalna (matlab ke saath) |
| **Endemic** | — | Amazon par bechta hai (`ON_AMAZON`) |
| **Endpoint** | — | API ka pata (URL) |
| **Enum** | Enumeration | Fix choices ki list |
| **Exclusion** | — | Nikalna / mana karna |
| **Field(...)** | — | Pydantic: `...` matlab REQUIRED |
| **First-class step** | — | Poora apna step, kisi ke andar chhupa nahi |
| **Flight Dates** | — | Campaign kab se kab tak chalega |
| **Floor CPM** | — | Neeche ki limit — isse kam pe bech nahi sakte |
| **Fork** | — | Raasta do/teen taraf batna |
| **Frequency** | — | Ek banda average kitni baar dekha (impressions ÷ reach) |
| **Frequency Cap** | — | Ek banda max kitni baar dekhega |
| **Funnel** | — | Chhanni — upar bahut log, neeche kam |
| **Future Scope** | — | Delete nahi kiya, sirf abhi nahi banayenge |
| **Genre** | — | Content ki kism (Action, Comedy, Sports) |
| **GET** | — | "Mujhe data do" (padhna) |
| **Halo Sales** | — | Ad dekha, phir Amazon par kharida — bina click kiye |
| **Hallucination** | — | AI ka jhooth bolna / cheezein bana dena |
| **Hard-coded** | — | Code me seedha likha — badalne ke liye deploy chahiye |
| **HttpUrl** | — | Pydantic type jo URL validate karta hai |
| **Impression** | — | Ad ka ek baar dikhna |
| **Indicative CPM** | — | Anumaanit CPM (pakka nahi) |
| **In-app** | — | Mobile app ke andar |
| **Instream** | — | Video stream ke andar ka ad |
| **Intent** | — | Kharidne ki niyat |
| **interrupt()** | — | LangGraph: graph rok kar insaan ka intezaar |
| **Inventory** | — | Bechne ke liye available ad slots |
| **Inventory Tier** | — | Deal ki kism: Amazon-owned / 3P-precurated / 3P-needs-curation |
| **IO** | Insertion Order | Advertiser aur publisher ke beech signed contract |
| **ISO Code** | — | International standard code (`GB`, `GBP`, `2026-08-01`) |
| **JSON** | — | Data likhne ka format `{"key": "value"}` |
| **KPI** | Key Performance Indicator | "Success kis number se naapoge?" |
| **LangGraph** | — | Library jo AI agent ko step-by-step raasta + state deti hai |
| **Linear TV** | — | Purana broadcast TV |
| **Linear Pipe** | — | Ek seedhi line, koi mod nahi |
| **Lookalike** | — | "Isse milte-julte log" |
| **Lookback** | — | Peeche dekhna — "sale hui, peeche kitne din me ad tha?" |
| **M0 / M1** | Milestone 0 / 1 | M0 = design (ye document), M1 = build (code) |
| **Matching Mode** | — | Similar (lookalike bhi) vs Exact (bilkul wahi) |
| **Mid-roll** | — | Video ke beech me ad |
| **Node** | — | Flowchart ka ek dabba = ek kaam |
| **Non-Endemic** | — | Amazon par nahi bechta (`NOT_SOLD_ON_AMAZON`) |
| **Normalisation** | — | Dheeli bhasha ko pakki shape me badalna |
| **Optional[X]** | — | X ho sakta hai, ya khaali (None) |
| **Outbound Sync** | — | Bahar bhejne wali process (VOW → Amazon) |
| **Pacing** | — | Kharch ka rate — dheere ya jaldi |
| **Paradigm** | — | Soch ka tarika / model |
| **PATCH** | — | HTTP method jo mojood cheez ka ek hissa update karta hai |
| **Path Parameter** | — | URL me `{market}` jaisa placeholder |
| **Persists** | — | Save kar deta hai (disk/DB par) |
| **PG** | Programmatic Guaranteed | Fixed CPM, guaranteed volume, **poora budget owed, pause nahi** |
| **pgvector** | — | PostgreSQL extension jo embeddings store aur search karta hai |
| **POST** | — | "Ye data lo / ye banao" (likhna) |
| **Post-click** | — | Ad par click kiya |
| **Post-view** | — | Ad dekha (click nahi kiya) |
| **Pre-curated** | — | Pehle se taiyar |
| **Pre-roll** | — | Video shuru hone se pehle ad |
| **Pre-signed URL** | — | Temporary URL jisme permission built-in hai |
| **Precision** | — | Nishaana kitna sahi |
| **Prerequisites** | — | Pehle se zaroori cheezein |
| **Private Auction** | — | Floor CPM par invited buyers ki boli |
| **Product Audience** | — | "Jinhone ye ASIN dekha/kharida" (❌ CTV me nahi) |
| **Provider** | — | Platform ka naam (Prime Video, Netflix, Disney+) |
| **Pydantic** | — | Python library jo data validate karti hai |
| **Q&A Side Path** | — | Beech me sawaal poochh kar wahin se aage chalna |
| **Rate Card** | — | Daam ki list |
| **Reach** | — | Kitne alag-alag (unique) log ne dekha |
| **Reach Curve** | — | Chart: kitna paisa → kitna reach |
| **Read-only** | — | Sirf padh sakte ho, set nahi |
| **Reducer** | — | Function jo batata hai purani + nayi value kaise jodni hai |
| **Registered** | — | Pehle se system me daala hua |
| **REST API** | — | Do software ke beech baat karne ka tarika |
| **Retargeting** | — | Jo pehle aaye the, unhe dobara dikhana |
| **ROAS** | Return On Ad Spend | £1 ad me lagaya, kitna sale aaya |
| **ROS** | Run Of Schedule | "Koi khaas genre nahi, jahan slot mile" — sasta |
| **Scale** | — | Kitne bade paimane par |
| **Schema** | — | Form ka blueprint |
| **Scope** | — | "Abhi hum ye banayenge, baaki baad me" |
| **Segment** | — | Ek audience group |
| **Semantic Grouping** | — | Matlab ke hisaab se group karna (UI ke hisaab se nahi) |
| **Slot** | — | Form ka ek khaana |
| **Slot Filling** | — | Baat karte-karte khaane bharna |
| **SSOT** | Single Source of Truth | Ek hi jagah jahan sach likha hai |
| **State** | — | Agent ki yaadash ka dabba |
| **Stateful** | — | Yaad rakhne wala |
| **Stateless** | — | Har baar bhool jaane wala |
| **Streaming TV** | — | Streaming inventory (Netflix, Disney, Hulu) |
| **TBC** | To Be Confirmed | Abhi tay nahi hua |
| **Threshold** | — | Seema / limit |
| **Timestamp** | — | Exact time (`2026-07-30T09:35:00Z`) |
| **Tool** | — | Agent ke haath me diya kaam karne ka zariya (yahan = API call) |
| **Trader** | — | 🎯 Wo insaan jo agent se chat karta hai — **tumhara user** |
| **TypedDict** | — | Dictionary jiske keys aur types tay hain (validate nahi karta) |
| **Underdelivery** | — | Plan 200,000 tha, mile 20,000 |
| **Upsell** | — | "Thoda mehnga wala lo, behtar hai" |
| **UUID** | — | Duniya me unique lamba code |
| **VCPM** | — | Audience data use karne ki fee (per 1000) |
| **Wide** | — | Broad ka naya naam (Maximum Scale audience profile) |
| **Zero-Hallucination** | — | Agent kuch banata nahi — sab API se verified |
| **201 Created** | — | Nayi cheez ban gayi |
| **200 OK** | — | Sab theek, data mil gaya |

---

# PART 14 — SELF-TEST (40 Sawaal + Jawab)

Jawab dekhne se pehle khud sochо. Atak gaye? Us Part par wapas jao.

## Foundation (1–10)

**1. DSP ka full form aur "demand side" ka matlab?**
> Demand Side Platform. Demand side = jise ad chahiye (advertiser). Supply side = jiske paas jagah hai (Netflix). DSP kharidne walon ka software hai.

**2. £20,000 budget, CPM £25 → kitne impressions?**
> 20,000 ÷ 25 × 1,000 = **800,000 impressions**

**3. 800,000 impressions, 500,000 reach → frequency?**
> 800,000 ÷ 500,000 = **1.6**

**4. CTV ka goal hamesha Awareness kyun?**
> Client: *"CTV is typically used as an Awareness goal as it's hard to track anything further down the funnel."* TV se click/purchase track karna reliable nahi.

**5. CTR, CPC, CPA, CPDPV kyun hataye?**
> Sab clicks/purchase naapte hain. CTV me remote se click nahi hota.

**6. PG deal ka sabse bada khatra?**
> **Poora budget owed** aur **pause nahi kar sakte**. Cancel kiya = paisa gaya.

**7. Effective CPM kya hai aur kyun dikhana zaroori?**
> Deal CPM + audience VCPM. Bina iske trader sochega audience free hai. £28.88 dekhega, £30.51 dega.

**8. Narrow audience "do tarah se buri" kyun hai?**
> Chhoti bhi hai (underdelivery risk) **aur** mehngi bhi (zyada VCPM).

**9. Halo sales kya hai?**
> Netflix par ad dekha, phir seedha Amazon par kharida — bina click. ASIN dene se track ho jaata hai.

**10. Ad tag pehle lagana kyun zaroori?**
> *"Tracking only records activity after it goes live."* Baad me lagaya to pehle ka data **hamesha ke liye gaya** — recover nahi hota.

## Inventory Tiers (11–17)

**11. Teen inventory tiers naam se batao.**
> `AMAZON_OWNED` (Prime Video), `THIRD_PARTY_PRECURATED` (Netflix, Hulu), `THIRD_PARTY_NEEDS_CURATION` (Disney+)

**12. Netflix ka reach forecast kyun nahi milta?**
> Netflix apna viewer-level data Amazon DSP ke saath share nahi karta.

**13. Disney+ ka deal kyun exist nahi karta?**
> *"Rate-card CPM only; VOW curates the deal after the IO is signed."* Kaagaz sign hone tak deal banti hi nahi.

**14. Total reach add kyun nahi kar sakte?**
> **Cross-platform deduplication** possible nahi. Wahi insaan Prime aur Netflix dono dekh sakta hai — double counting hogi. Prime aur Netflix apna data compare nahi karte.

**15. Netflix ke liye kya bata sakte hain?**
> Rate-card CPM aur derived impressions (`budget ÷ CPM × 1000`). Reach aur frequency **nahi**.

**16. Repair loop sirf Amazon portion par kyun?**
> Kyunki repair ke liye reach data chahiye — "widen karne se behtar hua?" ye janne ke liye. Netflix ka reach data hi nahi hai.

**17. Curation capture me kya-kya lete hain?**
> Genres, durations, targeting preferences (optional), budget, flight dates.

## 13-Step Flow (18–30)

**18. Kram kyun badla (6 → 13 steps)?**
> v1.1.0 UI wizard ke **screen kram** par tha. v2.0 **dependency kram** par hai — "pehle ye jaanna zaroori hai kyunki isse ye nikalta hai."

**19. Inventory audiences se pehle kyun?**
> Kyunki tier se pata chalta hai Amazon audiences apply hongi ya nahi. Netflix par Amazon audiences bekaar hain.

**20. "Everything before Step 13 is free" — kyun important?**
> Trader bina dar ke experiment kar sakta hai. Manager ko approve karne ka mauka **paisa lagne se pehle** milta hai. Galti pakadne ke 12 mauke.

**21. Durations Step 1 me kyun Required hai?**
> *"Determines which deals are available and what CPM applies."* Duration ke bina deals filter hi nahi ho sakte.

**22. EVEN_BY_BUDGET vs EVEN_BY_IMPRESSIONS?**
> BY_BUDGET = baraabar £, alag impressions. BY_IMPRESSIONS = baraabar impressions, alag £ (mehnga CPM = zyada spend).

**23. Budget split me agent kya "state" karta hai aur kyun?**
> Apni **assumption** — kaunsa method chuna aur kyun. *"so the trader can adjust."* Transparency.

**24. Approval "before finalised, not before launch" — kyun?**
> Jaldi reject **sasta** hai. Late reject me 8 steps ka kaam bekaar jaata.

**25. `interrupt()` kya karta hai aur normal wait se kyun behtar?**
> Graph **physically rukta** hai, state **persist** hoti hai, process **band** ho jaata hai. Server restart ho, 19 ghante beet jaayein — kuch nahi bhoolta. Normal wait me process zinda rehna padega aur restart par sab khatam.

**26. "Budget is locked" — kyun zaroori?**
> Warna trader chhota plan approve karwa ke budget badha sakta hai. *"Nothing launches that a person hasn't approved."*

**27. Reject par Step 4 par wapas kyun, Step 1 nahi?**
> Kyunki problem mostly **audience** me hoti hai. Naam/dates/market theek hote hain. Reject ka cost kam rakha.

**28. Draft endpoint kyun hataya?**
> Client: *"draft is just for the wizard creation."* Agent ki state LangGraph checkpointer me pehle se save hai — draft duplicate mechanism hai. Aur draft database me kachra banati hai.

**29. Duration match check kya karta hai?**
> Upload hui video ki duration approved plan se compare karta hai. Mismatch → economics badal gayi → **Step 7 par wapas (re-approval)**.

**30. Creative approval ke 3 statuses kyun?**
> *"Each platform reviews its own inventory independently."* Amazon approve, Netflix pending, Disney reject — ek saath ho sakta hai.

## Schema & Code (31–36)

**31. Budget "decimal string" kyun, float nahi?**
> Float me `0.1 + 0.2 = 0.30000000000000004`. Paisa me ye disaster hai. String/Decimal exact rehta hai.

**32. `Annotated[list, add_messages]` kya karta hai?**
> Reducer — batata hai "message **append** karo, replace nahi." Iske bina naya message aane par **poori chat overwrite** ho jaati.

**33. `current_step: int` se `current_stage: str` kyun?**
> 13 steps + sub-states (repair loop, awaiting approval) number se express nahi hote. String padhne me saaf, aur steps reorder karne par naam nahi badalta.

**34. `is_available` flag kya karta hai?**
> Honesty rule ko **schema level** par enforce karta hai. `false` = Netflix/Disney, reach data nahi. Agent guess kar hi nahi sakta.

**35. State me `dict` hai par Pydantic schemas bhi hain — kaise reconcile karoge?**
> **Boundary par parse karo:** node state se padhega → Pydantic model me convert (validate) → kaam → `.model_dump()` → wapas dict. "Parse, don't validate" pattern.

**36. "Semantic grouping" ka matlab aur kyun better?**
> Field ka naam **matlab** par rakho, UI par nahi. `strategy_name` ✅ vs `step1_details` ❌. Document: *"the state describes the plan, not the UI that collected it."* UI 10 baar badle, naam wahi rahega.

## Open Questions & Gaps (37–40)

**37. ASIN timing conflict kya hai aur tumhara fix?**
> Step 8 ka `POST /strategies/` `product_location` + `product_asins` maangta hai, par ye Step 11 me collect hote hain — **Step 8 ke baad**. Fix: ASIN aur product_location **Step 1 me rakho** (plan fields hain), sirf ad-tag check Step 11 me. Bonus: ASIN validation response me `product_category` bhi aata hai jo Step 1 ka field hai.

**38. TargetingSchema me kya contradiction hai?**
> Docstring kehta hai "config-driven, extensible", par code me **5 hard-coded fields** hain. Client ka explicit requirement violate ho raha hai. Fix: `selections: dict[str, list[str]]` + config registry.

**39. `creative_approval_status` me kya problem hai?**
> Step 10 **teen** statuses maangta hai (Amazon/Netflix/Disney), schema me **ek** field hai. Fix: `dict[str, ApprovalStatusEnum]`.

**40. "Did I understand correctly?" kyun sabse important trust mechanism hai?**
> AI ka sabse bada dar: *"mujhe pata nahi ye kya kar raha hai."* Ye mechanism trader ko **exactly dikhata hai** ki agent ne kya samjha — galti turant pakdi jaati hai, trader ko control feel hota hai. Iske bina agent ek **black box** hai aur trader use nahi karega.
>
> ⚠ Par document ne isko state machine me **add nahi kiya** — ye ek gap hai.

---

# 🎯 FINAL: David ke Comments se Pehle Ye 6 Baatein Yaad Rakho

### 1. Tumhara kaam mostly SAHI tha
**~15 items ✅ UNCHANGED** hain. Teeno core principles bilkul jaise the waise rakhe gaye. Ye tumhari jeet hai.

### 2. Jo badla, wo tumhari galti nahi thi
Client ne **naye requirements** diye jo tumhe pehle bataye nahi gaye the — inventory tiers, budget split, approval gates, credit check. Aur CTV-first scope ka faisla baad me hua.

### 3. Tumne 5 ⚠ Open Questions khud flag kiye
Ye **maturity** hai. Assume karke aage badhna aasan hota — tumne rok kar clarity maangi. Ye tumhari **taqat** hai, kamzori nahi.

### 4. Jo asli inconsistencies hain, wo turant maan lo
TargetingSchema, creative_approval_status, Broad/Wide, API catalogue contradiction, canary-check. Argue mat karo — fix suggest karo.

### 5. Har jawab me ek RECOMMENDATION do
Sirf *"confirm karna padega"* na bolo. Bolo: *"Main Option B recommend karta hun, kyunki [3 reasons]. Confirm ho jaaye to schema final kar dunga."*

### 6. Ye document ek CONTRACT hai
4 log isse code likhenge — Wajahat (state + graph), Vishal (registry), Basil (adaptive canvas), Riddhi (UI). Isliye consistency aur completeness matter karti hai. David ye ensure kara raha hai — **tumhare khilaaf nahi hai.**

---

> **Ab David ke 28 comments bhejo.** Main har comment ko is document ke exact section se jodkar samjhaunga — kya keh raha hai, kyun keh raha hai, aur tum kya jawab do.







