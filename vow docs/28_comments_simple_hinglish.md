# David ke 28 Comments — Simple Explanation

**Ye document kya hai:** Confluence par `Strategy Schema documentation v2.0` par David ne 28 comments kiye. Har comment ka matlab, simple words me, real example ke saath.

**Kaise padhein:** Har comment ka format ek jaisa hai —
```
David kya keh rahe hain   →  numbered points me
Example                    →  table ya code block me
Iska matlab                →  ek line ka takeaway
```

---

## Index

| # | Comment | Ek line me |
|---|---|---|
| 1 | "Their own targeting (adds CPM)" | 3P par targeting Amazon **ya** SSP se — choice hai |
| 2 | "added fee consequence" | Fee data se aati hai, profile se nahi |
| 3 | "Budget split NEW" | Split optional hai |
| 4 | "mandatory" | Audiences optional hain |
| 5 | "Targeting NEW" | Audience targeting ka hissa hai; targeting bhari hui aati hai |
| 6 | Do field lists | CTV ke liye kaato, baaki khud pata karo |
| 7 | "Required" (name) | Naam khud bana lo |
| 8 | "Multi-select" (markets) | Multi-market support hai? Dobara puchna padega? |
| 9 | "Required" (currency) | Currency market se aa jaati hai |
| 10 | "KPI" | Frequency ke saath number bhi chahiye |
| 11 | "Table" | Table data type nahi hai |
| 12 | "Required" (base bids) | CTV me bid apply nahi hota |
| 13 | "Optional" (frequency cap) | Advertiser par default hota hai |
| 14 | "Required" (formats) | Format hamesha streaming_tv |
| 15 | "Required for video" | Category advertiser se ya brief se |
| 16 | "Required" (selling location) | Isko hata do |
| 17 | "Conditional" (ASINs) | Baad me aate hain |
| 18 | "Checkbox table" | Deals match karo, table na dikhao |
| 19 | "Netflix/Disney" | Amazon audiences 3P par bhi chalti hain |
| 20 | "bundles.narrow/balanced/broad" | Ye support nahi hai |
| 21 | "Optional" (location) | Market ke country se default |
| 22 | "Optional" (device type) | Kuch advertisers sirf CTV chahte hain |
| 23 | "Plan Approval" | Bas status change, manager approval nahi |
| 24 | "api/strategies" | Endpoint galat hai |
| 25 | "Required" (click URL) | Streaming TV me optional |
| 26 | Teen approval rows | Per channel ek status, hardcode na karo |
| 27 | "Tracking Setup" | Koi order zaroori nahi |
| 28 | "Confirm with client" | Creation ke baad update ho sakta hai |

---
---

# Comment 1 — "Their own targeting (adds CPM)"

**David do baatein keh rahe hain:**

**1. "Only" galat likha hai.**

Document keh raha tha ki Netflix/Disney par **sirf unki apni** targeting chal sakti hai. Aisa nahi hai — **Amazon ki targeting bhi** 3P inventory par lag sakti hai.

**2. Ye choice deal ke hisab se hoti hai, tier ke hisab se nahi.**

Kaunsi targeting milegi ye pehle se pata nahi chalta. Deal match hone ke **baad** pata chalta hai.

---

### Example

Netflix par ad chalana hai. Targeting do dukaan se mil sakti hai:

| Raasta | Kya milta hai | CPM |
|---|---|---|
| **Amazon DSP se** | Amazon ke segments (healthy food, parents, income) | £22.96 + £1.63 = **£24.59** |
| **Netflix se** | Netflix ke apne segments (jo documentaries dekhte hain) | £22.96 + Netflix ki fee = **£26 approx** |

**Note:** Amazon ka option 3P par **limited** ho sakta hai — kuch cases me sirf device targeting milti hai, poori audience targeting nahi.

### Iska matlab

Tier se sirf do cheezein tay hoti hain — **reach forecast milta hai ya nahi**, aur **deal exist karti hai ya nahi**. Targeting ek alag baat hai.

Aur agent planning me targeting ka **wada nahi** kar sakta, kyunki wo deal match hone ke baad hi pata chalta hai.

---

# Comment 2 — "added fee consequence"

**David teen rules de rahe hain:**

**1. Fee kab lagti hai** — jab 1P data use karo. Amazon ka data 1P hai. Experian jaisi company ka Lifestyle data bhi unka 1P hai.

**2. Fee compound nahi hoti** — ek provider se 1 segment lo ya 30, **ek hi fee**.

**3. Providers stack hote hain** — do alag companies ka data use kiya to **dono** ki fee.

---

### Example

£10,000 budget, Netflix deal £22.96 CPM:

| Kya chuna | Effective CPM | Impressions | Fee |
|---|---|---|---|
| Koi audience nahi | £22.96 | 435,540 | £0 |
| Amazon se **5** segments | £24.59 | 406,669 | £1.63 |
| Amazon se **30** segments | £24.59 | 406,669 | £1.63 |
| Amazon **20** + Experian **5** | £26.59 | 376,081 | £3.63 |

**Note:** Row 2 aur 3 dekho — 6 guna zyada segments, par **daam wahi**. Aur row 4 me sirf 5 segment extra, par **naya provider** aane se £2 badh gaya.

Aur maine verify kiya — **kuch audiences free hain:**
```
FREE  →  Demographic (age, gender, income) · Device
PAID  →  In-market · Lifestyle · Interest · Custom-built  →  £1.63
```

### Iska matlab

Narrow / Balanced / Wide me **daam ka farak nahi** hai — sirf reach aur precision ka farak hai.

Agent ko track karna hai ki **kaunse provider** use ho rahe hain, **kitne segments** nahi.

---

# Comment 3 — "Budget split ➕ NEW"

**David do baatein keh rahe hain:**

**1. Split optional hai**, required nahi.

**2. Iska apna step nahi hona chahiye** — Step 2 (Inventory) ke andar substep ho, aur tab dikhe jab ek se zyada deal match ho. Ek deal me split karne ke liye kuch nahi hai.

---

### Example

£10,000, do inventory match hui. Split karo ya na karo?

**Jab CPM paas-paas ho:**

| | Prime £24 | Netflix £22 | Total |
|---|---|---|---|
| Split ke saath | 208,333 | 227,273 | **435,606** |
| Split ke bina (£23 blended) | — | — | **434,783** |

Farak sirf 823 impressions. **Koi baat nahi.**

**Jab CPM me bada farak ho:**

| | Prime £40 | Netflix £15 | Total |
|---|---|---|---|
| Split ke saath | 125,000 | 333,333 | **458,333** |
| Split ke bina (£27.50 blended) | — | — | **363,636** |

Farak 94,697 impressions — **26%!**

**Note:** Isliye split "preferred" hai. Bina split, agent ko blended estimate dena padta hai — aur wo **bolna** padega ki ye approximate hai.

### Iska matlab

Agent khud ek split **propose karega**. Trader accept, adjust ya skip kar sakta hai.

**Aur ek baat maine platform par pakdi** — platform **khud** 50/50 split kar deta hai creation ke baad, aur wo editable hai. To agent ka kaam bas explain karna reh jaata hai.

---

# Comment 4 — "mandatory"

**David ek baat keh rahe hain:**

**Audiences optional hain.** v1.1.0 me optional thi. v2.0 ne galti se mandatory kar diya — wo revert karo.

Trader teeno options **decline** kar sakta hai aur bina audience ke chala sakta hai.

---

### Example

| Kya chuna | Impressions | Data fee |
|---|---|---|
| Balanced audience | 406,669 | £1.63 |
| **Koi audience nahi** | **435,540** | **£0** |

**Note:** Bina audience ke **zyada** impressions milte hain aur fee bhi nahi lagti. Isko "run of service" kehte hain — poori inventory par chalega, koi filter nahi.

To ye **sasta option** hai, kharaab option nahi.

### Iska matlab

Broad awareness ke liye bina audience ke chalana bilkul valid hai.

**Par ek nuksan hai:** jab reach kam aaye, agent "audience widen karun?" nahi keh sakta — audience hi nahi hai. Us case me agent ko **saaf bolna** chahiye ki uske paas ye option nahi hai.

---

# Comment 5 — "Targeting ➕ NEW"

**David teen baatein keh rahe hain:**

**1. Audience alag step nahi hai — targeting ka hissa hai.**

Location, device, audience — teeno ek hi kaam karte hain: **kisko ad dikhana hai** ye tay karna. To Step 4 (Audiences) aur Step 5 (Targeting) ek hi step hone chahiye, do nahi.

**2. Targeting khaali form nahi hogi — bhari hui aayegi.**

Jaise Uber kholte hain to pickup already aapki location par set hota hai. Waise hi trader ko dikhega:
```
Location:  United Kingdom        (market se aaya)
Device:    Connected TV          (advertiser ki setting se aaya)
```
Trader bas confirm kare ya badle.

**3. Uske baad teen raaste hain — koi bhi EK kaafi hai:**
- audience segments jod do
- ya geography narrow kar do
- ya jaisa hai waisa accept kar lo

---

### Example

BrightPath ko **education me interested parents** chahiye. Do tareeke:

| Tareeka | Kaise | Kharcha |
|---|---|---|
| **Audience se** | "Presence of children + Education interest" | £1.63 data fee |
| **Postcode se** | "SW1, SW3, SW7" — achhe school waale areas | **£0 — free** |

**Note:** Dono ne ek hi kaam kiya — sahi logon tak pahunchna. Kyunki achhe school district me rehne wale log aksar education me interested parents hote hain. Par geography **muft** hai.

### Iska matlab

Audience **zaroori nahi** hai. Trader sirf postcodes se bhi kaam chala sakta hai — aur sasta padega.

Isliye David ne likha *"the user wants to use only postcodes **instead of** audiences"* — geography audience ki **jagah** le sakti hai.

---

# Comment 6 — Step 1 ki poori field list

**Ye 28 me se sabse bada comment hai.** David do instructions de rahe hain:

**1. Jo CTV me kaam nahi karta, kaat do.**

Multi-format choice, click-based KPIs (CTR, CPC, CPA), per-market base bid — ye sab isliye the ki original flow Display aur normal video bhi cover karta tha. CTV me in me **decide karne ke liye kuch nahi** hai.

**2. Baaki sab khud pata karo, trader se na pucho.**

Trader se practically sirf **teen cheezein** puchni chahiye — market, budget, dates. Aur wo bhi brief me likhi ho to nahi.

---

### Example

**Purana tareeka — 11 sawaal:**
```
"Strategy ka naam?"   "Kaunsa market?"   "Currency?"   "Format?"
"Goal?"   "KPI?"   "Product category?"   "Budget?"
"Base bid?"   "Frequency cap?"   "Dates?"
```
Trader sochta hai: *"isse to mai khud form bhar leta."*

**Naya tareeka — 1 sawaal:**

Trader: *"BrightPath ke liye UK me £10,000 ka CTV campaign, September"*

| Field | Kahan se aaya |
|---|---|
| Naam | Agent ne banaya — `Education_GB_Awareness_Sep2026` |
| Market, Budget, Dates | Brief me the |
| Currency, Format, Goal | Automatic |
| Category, Frequency cap | Advertiser ki settings se |
| Base bid | Deal ke CPM se |

Agent: *"Ek sawaal — creative kitne second ka hoga, 15 ya 30?"*

**Note:** 11 me se 10 khud pata kar liya.

### Iska matlab

Ye ek soch ka badlaav hai: **ye form nahi hai, ye baat-cheet hai.**

Isliye maine table me ek naya **Source column** add kiya — kyunki "Required" padh kar log samajh rahe the "trader se puchna padega". Ye do alag baatein hain:
```
Requirement  =  plan ko value chahiye?
Source       =  wo value KAHAN SE aayegi?
```

---

# Comment 7 — "Required" (Strategy name)

**David ek baat keh rahe hain:**

**Naam auto-generated hona chahiye.** Ye sawaal puchne ki zaroorat nahi.

---

### Example

Brief: *"BrightPath education courses ke liye UK me £10,000 ka CTV awareness campaign, September 2026"*

Agent naam banata hai:

| Hissa | Kahan se |
|---|---|
| `Education` | Advertiser ki setting |
| `GB` | Brief |
| `Awareness` | CTV me fixed |
| `Sep2026` | Flight dates |

→ **`Education_GB_Awareness_Sep2026`**

Naam already exist karta hai? → `_v2` laga kar dobara check → chal gaya.

**Note:** Trader se ek bhi sawaal nahi. Aur usko naam pasand nahi to rename kar sakta hai.

### Iska matlab

Naam ek **label** hai, **faisla** nahi. Isse plan me kuch nahi badalta — na budget, na inventory, na reach. Sirf baad me dhundhne ke liye hai.

To requirement `Optional` ho gaya aur source `GENERATED` — do alag baatein. Plan me naam hoga hi, par trader se **maanga nahi** jaayega.

---

# Comment 8 — "Multi-select" (Target markets)

**David do sawaal puch rahe hain:**

**1.** Multi-market support hai?

**2.** Agar hai, to har market ke liye choices **dobara** puchni padengi?

---

### Example — kya per market badalta hai, kya ek baar

| Per market alag | Ek baar hi |
|---|---|
| Budget | Flight dates |
| Currency | Goal aur KPI |
| Matched deals aur CPM | Creative durations |
| Available locations | Audience choice |
| Available product categories | Creatives aur approval |
| Reach forecast | Tracking, credit check |

**Note:** Do cheezein miss ho jaati hain — **locations** aur **product categories** dono endpoints **market ke hisab se** alag list dete hain. Chahe trader ka iraada same ho.

### Reach add ho sakti hai?

| Kya | Add ho sakti hai? | Kyun |
|---|---|---|
| UK reach + Germany reach | ✅ Haan | UK ka banda Germany me nahi dekhega |
| Prime reach + Netflix reach (same market) | ❌ **Nahi** | Wahi banda dono par dekh sakta hai |

Maine verify kiya: API ka `total_reach` **233,803** aaya, par sum **203,833** tha. To API ka number zyada hai.

### Iska matlab

**M1 me ek market per strategy** — par field ko **list hi rakhna** hai, taaki baad me multi-market add karna rebuild na bane.

Brief me kai markets hain? Agent **saaf bolega** aur ek se shuru karne ka proposal dega — chupke se ek uthaa nahi lega.

---

# Comment 9 — "Required" (Primary currency)

**David ek baat keh rahe hain:**

**Currency market se aa jaati hai** — puchne ki zaroorat nahi. `GB → GBP`, `US → USD`, `DE/FR → EUR`.

---

### Example

```
Trader ne UK chuna
   → currency GBP ho jaani chahiye
   → dropdown ki zaroorat nahi
```

**Note — par platform par ulta hai.** Maine verify kiya:

| Kya kiya | Kya hua |
|---|---|
| Page khola | Currency already **EUR** bhari hui thi (market chunne se pehle!) |
| `United Kingdom` chuna | Currency **EUR hi rahi** |
| Purani strategies dekhi | Ek strategy `NOK` currency me, market `US` |

To currency **market se nahi, advertiser ki setting se** aati hai.

### Iska matlab

David ka point **behaviour ke liye sahi** hai — trader se puchna nahi chahiye.

Par **mechanism alag** hai — source `ADVERTISER` hai, `DERIVED` nahi. Maine ye document me correct kar diya hai.

Aur ek zaroori baat: platform **do currency** rakhta hai aur convert karta hai —
```
Market view:   £10,000
Primary view:  €10,909.09      (rate 1.0909)
```
Dono asli hain aur dono payload me jaati hain.

---

# Comment 10 — "KPI"

**David ek baat keh rahe hain:**

**KPI ke saath ek target value bhi chahiye** — range 1 se 5.

---

### Kya problem thi

```
Document me:  KPI = "Frequency"
Par:          KITNI frequency? Wo number kahan store hoga?

"Mujhe frequency chahiye"     → iska koi matlab nahi
"Mujhe frequency 3 chahiye"   → ab matlab hai
```

### Example — ye number forecast BADAL deta hai

Impressions budget aur CPM se **pehle se fix** hain. To frequency target set karna asal me **reach target** set karna hai:

```
£10,000 ÷ £33.33 CPM × 1000  =  300,000 impressions   (fix hai)
```

| Target frequency | Kitne log chahiye |
|---|---|
| 2 | 150,000 |
| **3** | **100,000** |
| 5 | 60,000 |

**Ab repair loop:**
```
Target 3 tha  →  100,000 log chahiye
Forecast aaya →  reach 60,000, frequency 5

Diagnosis: audience BAHUT tight hai. Wahi 300,000 impressions
           kam logon par gir rahi hain — har banda 5 baar dekhega.
Fix:       audience widen karo → frequency 3 par aayegi
```

**Note:** Target ke **bina** agent ke paas compare karne ke liye kuch nahi hai. Forecast "frequency 5" aaya — accha hai ya bura? Pata nahi.

### Iska matlab

Ye sirf label nahi, ek **constraint** hai.

**Do chhoti corrections maine ki:**
1. Range **2–5** hai, 1–5 nahi. Platform 2, 3, 4, 5 deta hai. Aur 1 hatana sahi hai — frequency 1 ka matlab target ka **na hona** hai.
2. Ye **per format** hota hai. Ek strategy me Streaming TV ka reach target aur Prime Video ka frequency target dono ho sakte hain.

---

# Comment 11 — "Table" (Market budgets)

**David ek sawaal puch rahe hain:**

Ek market hai to **ek budget** hai. To "Table" kyun likha hai?

---

### Kya problem hai

Type column me **UI widget** likha hua tha, **data type** nahi.

| Field | Purana (galat) | Naya (sahi) |
|---|---|---|
| Market budgets | `Table` | `Decimal, one per market` |
| Base bids | `Table` | `Decimal, one per market` |
| Target markets | `Multi-select` | `List of str` |
| Product ASINs | `Textarea` | `List of str` |
| Selected deals | `Checkbox table` | `List of deal objects` |

**Note:** Ye ek row ki galti nahi thi — **poore column** me widgets the.

### Iska matlab

Type batata hai field me **kya hai**. Wo screen par kaise dikhega — wo interface ka kaam hai.

Aur ye agent ke liye **matter karta hai** — agent widget nahi dekhta, wo data structure dekhta hai.

Schema neeche wahi hai (`list[MarketBudgetBidSchema]`), sirf documentation theek hui.

---

# Comment 12 — "Required" (Base bids)

**David ek baat keh rahe hain:**

**CTV me base bid apply nahi hota.** Daam deal ka CPM hai, to trader ke set karne ke liye koi bid nahi hai.

---

### Kya sahi hai

| Deal type | Price | Bid ka kaam? |
|---|---|---|
| Preferred Deal | `FIXED_CPM` £15.26 | ❌ Nahi — daam pakka hai |
| Programmatic Guaranteed | `FIXED_CPM` | ❌ Nahi — auction hi nahi hota |

**In dono ke liye David 100% sahi hain.**

### Note — par ek problem hai

| Deal type | Price | Bid ka kaam? |
|---|---|---|
| **Private Auction** | **`FLOOR_RATE`** £22.96 | ✅ **HAAN** |

**Floor ka matlab minimum hai — usse UPAR bid karna padta hai, aur compete karna padta hai.**

Aur maine platform par verify kiya:

| Kya dekha | Nateeja |
|---|---|
| 83 deals me se lagbhag **saari** `PRIVATE_AUCTION` + `FLOOR_RATE` | Netflix ki saari, Freewheel ki saari |
| Pure CTV plan me base bid khaali chhoda | `Next` **block** ho gaya — *"All fields should be filled"* |

### Iska matlab

**Repair loop ka ek lever chala jaata hai** — aur wo field se zyada zaroori hai:

```
Purane levers:  audience widen  +  bid raise
Iske baad:      audience widen  (bid gaya)
```

**Par agar deals floor-rate hain to bid lever MAUJOOD hai** — aur wo reach kam hone par sabse seedha fix hai (bid badhao → zyada auctions jeeto → zyada impressions).

Maine ye document me **open question** ki tarah rakha hai, disagreement ki tarah nahi.

---

# Comment 13 — "Optional" (Frequency cap)

**David ek line likhi:** *"we have a default per advertiser"*

**Par ye 28 me se sabse gehra comment hai** — kyunki ye ek naya concept introduce karta hai jo document me **tha hi nahi**.

---

### Naya concept

**Kuch settings advertiser ki hoti hain, campaign ki nahi.** Wo brief se brief nahi badalti — to har baar puchna waste hai.

Frequency cap pehla hai, par akela nahi. Baad ke comments me pata chala:

| Setting | Kaunse comment se |
|---|---|
| Frequency cap | Comment 13 |
| Product categories | Comment 15 |
| Selling location | Comment 16 |
| Device type | Comment 22 |

**Yaani ye ek pattern hai, ek exception nahi.**

### Example — kab load hoti hain

```
Session shuru
   ↓
GET /api/admin/advertiser/brightpath/     ← settings load
   ↓
Brief parse karo                           ← brief OVERRIDE karta hai
```

**Note:** Order zaroori hai. Pehle defaults, phir brief. Ulta karne se defaults brief ko overwrite kar denge.

### Aur ek cheez — LOCKED settings

Comment 22 me pata chala ki kuch advertisers **sirf Connected TV** chahte hain. Wo **default nahi, RULE** lagta hai.

| | Default | Locked policy |
|---|---|---|
| Trader badal sakta hai? | ✅ Haan | ❌ Nahi |
| Repair loop relax kar sakta hai? | ✅ Haan | ❌ **Nahi** |

Isliye maine ek flag add kiya:
```python
class AdvertiserSetting:
    value: Any
    is_locked: bool = False      # brand policy — override nahi ho sakti
    reason: Optional[str]        # locked hone par trader ko dikhega
```

### Iska matlab

**Bina `is_locked` ke agent starting point aur rule me farak nahi kar sakta** — aur wo aisi cheez relax karne ki offer kar dega jise chhune ki ijazat nahi hai.

```
❌ Bina flag:  "Mobile add kar deta hoon, reach badh jaayegi!"
               → brand policy toot gayi
               
✅ Flag ke saath: "Device widen nahi kar sakta — advertiser ki brand
                   policy hai. Audience widen karta hoon."
```

---

# Comment 14 — "Required" (Formats)

**David ek line likhi:** *"is always streaming_tv"*

**Do baatein hain:**

**1. Ek hi value hai to choice dikhana bekaar hai.** Field ek constant ban jaati hai.

**2. `prime_video` FORMAT nahi hai — CHANNEL hai.**

---

### Example — cold drink se samjho

```
Category (format)  =  Cold drink
Brand (channel)    =  Coca-Cola, Pepsi, Sprite

Coca-Cola ek CATEGORY nahi hai. Wo cold drink ke ANDAR ek brand hai.
```

Waise hi:

| | Kya hai | Values |
|---|---|---|
| **Format** | Inventory ki kism | `streaming_tv` |
| **Channel** | Kaun ad dikha raha hai | Prime Video, Netflix, Disney+ |

**Note:** Document **khud apne aap ko contradict** kar raha tha. Step 2 me `SelectedDealSchema.provider` ka description hi tha *"e.g. Prime Video, Netflix, Disney+"* — to Prime Video **ek step baad sahi jagah** capture ho raha tha. Step 1 galti carry kar raha tha.

### Note — par ek exception maine pakdi

Forecast API me `prime_video` **matter karta hai:**

| Kya bheja | Kya mila |
|---|---|
| `["streaming_tv", "prime_video"]` | **Do** supply lines — 132,713 + 71,120 reach |
| `["streaming_tv"]` | Sirf **ek** line — 71,120 reach **kho gaya** |

### Iska matlab

**Model me** David sahi hain — Prime Video channel hai.

**Par forecast payload me** dono bhejne padte hain, warna 71,120 reach aur 212,860 impressions chali jaati hain. Ye API ka design issue hai, model ka nahi.

---

# Comment 15 — "Required for video" (Product categories)

**David ek line likhi:** *"we have a default on the advertiser, or maybe could imply from the brief"*

**Do baatein:**

**1. Category advertiser par set hoti hai** — ya brief se imply ho jaati hai.

**2. "for video" qualifier bekaar hai** — CTV **hamesha** video hai, to condition hamesha true hai.

---

### Example — doctor ke clinic se samjho

```
Ek dentist ka clinic hai.
Kya aap har appointment par puchenge "aap kaunse doctor ho?"

Nahi. Wo clinic ki PROPERTY hai, appointment ka faisla nahi.
```

Waise hi **BrightPath har brief par education advertiser hai.**

### Resolution order

| Priority | Kahan se |
|---|---|
| 1 | Advertiser ki setting |
| 2 | Brief se imply — *"an education website"* itna kaafi hai |

**Note — ek teesra source hai par bahut late aata hai.** ASIN validation product category wapas deta hai, par ASINs tracking step par collect hote hain — is step ke bahut baad.

Par **cross-check ke liye kaam ka hai:**
```
Advertiser setting:  Education
ASIN validation:     Consumer Electronics
→ Agent: "Ek mismatch hai, confirm kar lein?"
```

### Iska matlab

Category puchni nahi hai. Aur ek **open question** hai jo maine raise kiya:

**Advertiser par jo hai wo product category hai ya INDUSTRY?** Ye do bilkul alag taxonomies hain, do alag endpoints. Agar advertiser industry rakhta hai to **mapping banani padegi** — jo abhi kahin nahi hai.

---

# Comment 16 — "Required" (Selling location)

**David ek line likhi:** *"can leave out"*

**Ek baat keh rahe hain:** Is field ko Step 1 se **nikaal do**.

---

### Kya problem thi

**Ye sawaal DO jagah pucha ja raha tha:**

```
Step 1:   "Amazon par bechte hain?"      ← pucha
Step 11:  "Amazon par bechte hain?"      ← DOBARA pucha!
```

### Example

| | Purana | Naya |
|---|---|---|
| Session shuru | — | Advertiser se load ho gaya |
| Step 1 | Pucha | **Nahi pucha** |
| Step 8 (create) | Value kahan se? Confusion | Advertiser setting se bhar diya |
| Step 11 | Dobara pucha | Confirm kiya, ASINs decide kiye |

**Note:** Ye field **plan kaise banega** wo tay nahi karti — **conversions kaise measure honge** wo tay karti hai. To ye **tracking step** ke saath jaati hai, jahan ASIN aur ad-tag ke sawaal already baithe hain.

### Iska matlab

Field delete nahi hui — sahi jagah chali gayi.

**Aur ye chupke se ek bada open question aadha solve kar deta hai.** Document me do baar flag tha ki `product_location` create payload me **required** hai par Step 11 me collect ho raha hai — uske **baad**.

Agar value **advertiser se** aati hai (jo session ke shuru me load hoti hai), to agent ke paas wo **already hai** jab wo strategy create karta hai. Kuch patch karne ki zaroorat nahi.

---

# Comment 17 — "Conditional" (Product ASINs)

**David ek line likhi:** *"comes later"*

**Ek baat:** ASINs baad me aate hain.

---

### Example — ghar ke registration se samjho

```
Ghar ka registration pehle hota hai.
Furniture baad me aata hai.

Aap registration ke liye furniture ka wait nahi karte.
```

Waise hi:

```
Step 8 — Create:
   POST /api/strategies/
   { "product_asins": [],  ... }     ← KHAALI
   → 201, id: VMA2026368

Step 11 — Tracking:
   Trader ASINs deta hai
   → validate karo
   → PATCH /api/strategies/VMA2026368/
     { "product_asins": ["B08N5WRWNW"] }
   → attach ho gaya
```

**Note:** Maine platform par test kiya —

| Kya chuna | ASIN required? |
|---|---|
| **On Amazon** | ✅ Haan — invalid ASIN `Next` block kar deta hai |
| **Off Amazon** | ❌ Nahi — zero ASINs se bhi chalta hai |

Off Amazon par ASIN field kyun dikhti hai? **Halo sales** ke liye — jo advertiser Amazon par nahi bechta wo bhi apni category ke ASINs jod kar indirect Amazon sales dekh sakta hai.

### Iska matlab

Ye comment wo **confirm** karta hai jo v2.0 ne already kaha tha. Correction chhoti thi: agar baad me aate hain, to **Step 1 me listed nahi hone chahiye**. Row hata di.

Aur Comment 16 ke saath milkar ye **poora timing question band** kar deta hai jo document me do baar aaya tha.

---

# Comment 18 — "Checkbox table" (Selected deals)

**Ye Comment 6 ke baad sabse bada structural comment hai.**

David ka poora comment:

> *"In majority of cases we want to pick the deals based on the requirements of the brief which we can do if we know the market, duration and channel... They may provide a deal id if they have 1 in mind but we want to remove the technical need to select deals from a table. We don't surface the underlying deal choices to the user - only the CPM"*

**Teen baatein:**

**1. Deals MATCH karo, table na dikhao.** Trader requirements batayega, agent deals dhundhega.

**2. Match karne ke inputs:** market, duration, channel. Optional: ROS/genre aur targeting.

**3. Trader ko sirf CPM dikhao** — deal ID ya naam nahi.

---

### Example — Ola se samjho

```
Ola book karte waqt aap driver nahi chunte.
Aap bas bolte ho "Airport jaana hai" — Ola driver match kar deta hai.

Driver ka naam ek IMPLEMENTATION DETAIL hai.
```

Waise hi:

| Kya faisla hai | Kya plumbing hai |
|---|---|
| Prime Video vs Netflix | `EXT7P75718S8MNR` vs `EXT7P75719Q2LKM` |

**Purana tareeka:**
```
Agent: "Ye 83 deals hain, tick karo:
        ☐ 3PS_Freewheel_UK_STV_Paramount_My 5 — £22.96 Floor
        ☐ 3PS_Netflix_Always On_Auto Intenders_NOT Amazon Audience... — £38.12
        ... 81 more"
Trader: "...mujhe kya pata kaunsa lena hai?"
```

**Naya tareeka:**
```
Trader: "Prime Video par chalao, 30-second creative"
Agent:  "Prime Video par £24.79 effective CPM mil raha hai.
         £10,000 par ~403,000 impressions.
         Ye preferred deal hai — daam pakka, pause kar sakte hain.
         Aage badhun?"
```

### Note — do cheezein PHIR BHI batani padengi

Deal chhupana theek hai, par ye do nahi:

| Kya | Kyun |
|---|---|
| **Tier capability** | 3P deals se reach forecast **nahi** aata. Sirf CPM dikhaya to trader ko pata hi nahi chalega ki plan ke ek hisse ka reach missing hai |
| **Commercial commitment** | PG deal **poora budget owe** karti hai aur **pause nahi** ho sakti. Agent ko bolna padega: *"ye guaranteed deal hai, poora £6,000 committed hoga"* |

### Note — aur ek problem: ye abhi buildable NAHI hai

Maine deal ka poora payload dekha:

| Matching input | Available? |
|---|---|
| Market | ✅ Haan |
| Duration | ⚠️ Amazon deals me haan, 3P me khaali |
| **Channel** | ❌ **Field exist nahi karti** — sirf `name` ke andar |
| **Inventory tier** | ❌ **Field exist nahi karti** |
| **Genre** | ❌ Field hai par usme `"2026"`, `"TEST"`, `"15, 20, 30"` values hain |

### Iska matlab

Design bilkul sahi hai. **Par abhi data hi nahi hai.**

Agent ko deal ke **naam** parse karna padega ye decide karne ke liye ki kya khareedna hai — jo hamare Zero-Hallucination principle ke **khilaf** hai.

To ye **client se data-quality request** ban jaati hai.

---

# Comment 19 — "Netflix/Disney"

**David ek line likhi:** *"can use amazon audiences too"*

**Ek baat:** "Only" galat tha. Amazon audiences 3P inventory par bhi chalti hain.

---

### Note — ye Comment 1 wali BAAT HI hai

| Comment | Kahan | Kya galat tha |
|---|---|---|
| 1 | §2.3 ki tier table | "Their own targeting" |
| **19** | Step 4 ki constraints list | "only" |

**Ek hi galti DO jagah likhi hui thi.** David ne dono pakdi.

### Example — cost ka ganit badal jaata hai

Plan: £10,000 — Prime Video £5,000, Netflix £5,000

| Situation | Prime | Netflix | Total impressions |
|---|---|---|---|
| Koi audience data nahi | 208,333 | 217,770 | **426,103** |
| **Amazon data POORE plan par** | 195,084 | 203,335 | **398,419** |
| Amazon sirf Amazon par, Netflix apni | 195,084 | 192,604 | **387,688** |

**Note:** Purana document **sirf situation 1 aur 3** dikha sakta tha. Situation 2 uske liye exist hi nahi karta tha.

### Iska matlab

Purani soch thi ki Amazon ki fee **sirf Amazon inventory** par lagegi. Ab pata chala ki **3P par bhi** lagegi — to us hisse ka CPM bhi badhega.

Trader **teen** situations compare kar raha hai, do nahi.

**Aur agent 3P par result verify nahi kar sakta** — un tiers se reach forecast nahi aata. To wo audience widen kar sakta hai par **dikha nahi sakta** ki kaam kiya. Usko ye **bolna** chahiye.

---

# Comment 20 — "bundles.narrow/balanced/broad"

**David ek line likhi:** *"not currently supported"*

**Ek baat:** Aisa koi object nahi hai. Endpoint teen ready-made groups nahi deta.

---

### Example — thali se samjho

```
Document samajh raha tha:  "Restaurant se READY-MADE THALI aayegi —
                            teen size me, small/medium/large"

Asliyat:                    "Restaurant KACCHA SAAMAN deta hai.
                            Thali khud banani padegi."
```

**Document kya maan raha tha:**
```json
{ "bundles": {
    "narrow":   {"segments": [...], "reach": 45000},
    "balanced": {"segments": [...], "reach": 120000},
    "broad":    {"segments": [...], "reach": 280000} }}
```

**Asliyat:**
```json
POST /api/audience-sets/suggest/     → {"id": "abc-123"}      ← async!
GET  /api/audience-sets/suggest/abc-123/
→ [ {"name": "Healthy Food", "reach": 45000, "relevance": 0.92},
    {"name": "Health Conscious", "reach": 38000, "relevance": 0.88},
    ... 40 more, FLAT LIST ]
```

### Note — aur ek nayi cheez maine pakdi

Audience sets me ek **`prompt` field** hai, aur wo natural language se bhari hui hai:

```
"Mums looking for healthier snacks for their kids school lunch boxes"
"find me audiences who are most likely to buy car accessories for luxury cars"
```

**Yaani suggest feature PEHLE SE use ho raha hai.**

### Iska matlab

**Teen baatein:**

**1.** Grouping ka logic **humein** likhna padega — API nahi deta.

**2.** Aur ye badal deta hai ki teen profiles **kya hain.** Comment 2 (fee provider se) aur Comment 4 (profile optional) ke saath dekho — Narrow/Balanced/Wide **teen price points wala API feature nahi hain.** Wo **ek hi flat list ko teen breadth par present karne ka tareeka** hain.

**3.** Aur agent ka kaam is step par asal me **prompt likhna** hai — segments browse karna nahi.

**Isliye maine ek sawaal banaya:** kya suggest endpoint ka ek **real response sample** mil sakta hai? Grouping rule, fee handling aur poora schema usi par depend karte hain.

---

# Comment 21 — "Optional" (Location)

**David ek line likhi:** *"defaults to market country"*

**Ek baat:** Field khaali shuru nahi hoti — market ka country pehle se bhara hota hai.

---

### Example — Swiggy se samjho

```
Swiggy kholte hain → delivery address ALREADY bhara hua hota hai
Aap chahein to badal sakte ho. Par bharna nahi padta.
```

### `markets` aur `location` DO alag fields hain

Dono aksar `GB` kehte hain, isliye duplication lagte hain. Par:

| | Kya sawaal ka jawab | Kya tay karta hai |
|---|---|---|
| `markets` | Kis market me **khareed** rahe hain? | Kaunsi deals, kaunsa rate card, currency, category list |
| `location` | Ad kahan **dikhna** chahiye? | Geographic delivery |

Same shuru hote hain, **narrow karne par diverge** ho jaate hain:

| Trader ne kaha | markets | location |
|---|---|---|
| Shuru me | `["GB"]` | `["GB"]` |
| "London me chalao" | `["GB"]` | `["London"]` |
| "SW1, SW3, SW7" | `["GB"]` | `["SW1","SW3","SW7"]` |

### Note — narrow karne se reach GHATTI hai

| Location | Addressable audience |
|---|---|
| Poora GB | 280,000 |
| London | 45,000 (84% kam) |
| 3 postcodes | 3,200 (99% kam) |

Agent ko **bolna** chahiye:
> *"Postcodes tak narrow karne se audience 280,000 se 3,200 par aa gayi. £10,000 par frequency bahut high ho jaayegi — har banda 100+ baar dekhega."*

### Iska matlab

"Optional" ka matlab badal jaata hai:
```
Purana matlab:  "khaali reh sakta hai"
Naya matlab:    "aapko CHHUNE ki zaroorat nahi — bhara hua hai"
```

---

# Comment 22 — "Optional" (Device type)

**David ek line likhi:** *"Some advertisers only want CTV only - set at advertiser level"*

**Do baatein — aur doosri bahut gehri hai:**

**1.** Device type advertiser par set hota hai, puchna nahi.

**2.** **Document do cheezein mila raha tha** — content type aur device type.

---

### Example — Netflix se samjho

```
Aap Netflix TV par dekhte ho      → content: streaming video
Aap Netflix phone par dekhte ho   → content: streaming video

CONTENT WAHI HAI. Sirf SCREEN alag hai.
```

Isliye do alag fields chahiye:

| Field | Kya hai | Kahan se |
|---|---|---|
| `formats = ["streaming_tv"]` | Content ki kism | CTV ke liye constant |
| `device_types = ["Connected TV"]` | Screen | Advertiser ki setting |

**🔴 `streaming_tv` ka matlab TV screen NAHI hai.** Matlab hai "streaming content" — wo phone par bhi ho sakta hai.

**Note:** Document **khud iska saboot** deta hai. Isi table me `Mobile environment` field hai (in-app vs mobile web). **Agar delivery sirf TV par hoti to wo field ka koi matlab hi nahi hota.**

### Note — CTV-only ka do nuksan

| Asar | Kyun |
|---|---|
| Inventory **ghatti** hai | Streaming ka bada hissa mobile par hota hai |
| CPM **badhta** hai | CTV inventory mobile se mehngi hai |

To same budget me **kam impressions**. Aur trader ne ye choose nahi kiya — advertiser ki setting se aaya.

### Iska matlab

**"Only want CTV only" ek RULE lagta hai, default nahi.**

Aur repair loop device targeting relax karta hai jab reach kam aaye. Agar advertiser ne rule out kar diya hai to **wo lever available nahi hai.**

```
❌ Bina is_locked:  "Mobile add kar deta hoon!" → brand policy toot gayi

✅ is_locked ke saath: "Device widen nahi kar sakta — advertiser ki
                        brand policy hai (TV screens only).
                        Audience widen karta hoon."
```

**Yahi wajah hai ki maine Comment 13 me `is_locked` flag add kiya.**

---

# Comment 23 — "Plan Approval"

**David ne likha:** *"we simplified this so it's just a status changed to finalise the plan - no manager approval required for now"*

**Ek baat:** Approval simplify ho gaya. Bas ek status change hai. Manager approval abhi nahi.

---

### Example — leave application se samjho

```
❌ Purana:  Leave application → manager ko notification → wo 3 ghante
            baad dekhe → reject kare → aap dobara bhejo

✅ Naya:    Aap khud mark kar do: "Plan finalise"
```

**Purana:**
```
Trader: "approve karo"
Agent:  [interrupt()] → manager ko notification
        → GRAPH RUK GAYA
        → 3 ghante baad manager reject karta hai
        → graph Step 4 par wapas
```

**Naya:**
```
Trader: "plan theek hai"
Agent:  plan_status: DRAFT → FINALISED
        "Plan finalise ho gaya. Ab strategy create karta hoon."
```

### Note — jo hataya wo ek field se BAHUT bada hai

| Kya hataya |
|---|
| Manager ko notification |
| Unknown time ka wait |
| Rejection route |
| Threshold rule (kab approval chahiye) |
| Roles (kaun approve kar sakta hai) |
| Ek LangGraph `interrupt()` |

### Note — par ek interrupt RAHA

| Step | Interrupt? | Kyun |
|---|---|---|
| Plan approval | ❌ Hataya | Wahan **colleague** ka wait tha |
| Creative approval | ✅ **Raha** | Wahan **Amazon** ka wait hai — genuinely external |

**Farak yaad rakho:** platform jo review karta hai uske liye rukna, aur colleague ke liye rukna — ek jaisi cheez nahi hai.

### Iska matlab

Comment me likha tha *"for now"* — to maine do cheezein **extensible** rakhi:

1. `PlanStatusEnum` **alag enum** banaya (`ApprovalStatusEnum` reuse nahi kiya). Plan aur creative ke lifecycle alag hain. Baad me `PENDING_APPROVAL` add karna additive rahega.
2. Fields rename kiye — `plan_status`, `finalised_by`, `finalised_at`.

**Aur approval wapas aaya to manager gate ke roop me nahi aayega** — advertiser-level rule ke roop me: *"£10,000 se upar mera sign-off chahiye."*

---

# Comment 24 — "api/strategies"

**David ne likha:** *"probably more likely simple-strategies endpoint"*

**Ek baat:** Ye endpoint galat lagta hai.

---

### Example — galat address ka courier

```
Courier galat address par bhej diya. Ek packet ka nuksan?

Nahi — pata chala ki POORI address book purani thi.
```

**Maine sochi:** agar ek endpoint galat hai to baaki kitne galat hain? To **poori list** staging Swagger ke against padhi.

### Kya mila

| Document me maana | Asliyat |
|---|---|
| `POST /api/strategies/` creation ke liye | `POST /api/simple-strategies/` bhi hai |
| Koi update endpoint nahi | `PATCH /api/strategies/{id}/` **hai** |
| `POST /api/rate-cards/match/` | 🔴 **EXIST NAHI KARTA** |
| `/api/advertisers/{id}/defaults/` | 🔴 **EXIST NAHI KARTA** |
| Postcode support unknown | `POST /api/strategies/postcode-validation/{market}/` **hai** |
| Fee values unknown | `GET /api/contextual-targeting/fees` **hai** |

**Total 14 corrections.**

### Note — teen candidates hain

Aur maine platform par dekha ki manual wizard **`POST /api/strategies/`** use karta hai, `simple-strategies` **nahi**:

| Endpoint | Status |
|---|---|
| `POST /api/strategies/` | ✅ Product yahi use karta hai |
| `POST /api/simple-strategies/` | Exists, **POST only** — koi read/update nahi |
| `POST /api/automated-strategies/` | Exists — naam agent ke liye sabse fit lagta hai |

### Iska matlab

Ek endpoint ka jawab mil gaya, par **naya sawaal khada ho gaya** — agent ke liye kaunsa?

Aur `is_automated` field strategies par **pehle se hai** — jo teesre endpoint par ishaara karta hai.

Ye maine open question ki tarah rakha hai, kyunki poora create payload isi par depend karta hai.

---

# Comment 25 — "Required" (Click-through URL)

**David ne likha:** *"optional for streaming tv"*

**Ek baat:** Streaming TV me ye required nahi hona chahiye.

---

### Example

```
TV remote se ad par click kar sakte ho?

Nahi.

To landing page URL maangna trader ko ek aisi field par ROK dega
jiska television par koi kaam hi nahi hai.
```

**Maine platform par verify kiya:**
```json
{ "type": "Streaming TV Video", "approval_status": "APPROVED",
  "click_through_url": null }
```

**Streaming TV creative bina URL ke APPROVED ho sakta hai.**

### CTV par call-to-action kaise hota hai

| Tareeka | Kaise |
|---|---|
| QR code | Creative me QR dikhao, phone se scan karo |
| Search prompt | *"search for BrightPath"* |
| Brand recall | Bas naam yaad reh jaaye |

**Aur measurement click par depend nahi karta** — wo ASINs ya ad tag se aata hai.

### Note — ek refinement maine add ki

Device types advertiser se aate hain, aur unme **mobile ya desktop bhi ho sakta hai** — aur un screens par ad **click HO SAKTA hai**.

| Device types | URL |
|---|---|
| Sirf Connected TV | Zaroorat nahi |
| CTV + Mobile | **Recommended** — warna mobile ka click-through waste |

### Iska matlab

Field optional hui, par **URL diya jaaye to validate hoga**.

Aur maine wajah document me **likh di** — taaki koi baad me ise wapas required na kar de.

---

# Comment 26 — Teen approval rows

**David ne likha:** *"It's just a single status for each channel not necessary netflix or disney - could be paramount or channel 4"*

**Ek baat:** Per channel ek status. Aur publisher ke naam hardcode na karo.

---

### Example — Excel se samjho

```
❌ Galat tareeka:
   Har naye employee ke liye ek NAYA COLUMN banao
   → 100 employee = 100 column
   
✅ Sahi tareeka:
   Ek column "Employee name", ek "Status"
   → naya employee = nayi ROW
```

**Purana (hardcoded):**
```python
class CreativeApproval:
    prime_video: ApprovalStatusEnum
    netflix:     ApprovalStatusEnum
    disney:      ApprovalStatusEnum
```

Paramount+ add karna:

| Step | Kaam |
|---|---|
| 1 | Schema me field add karo |
| 2 | Database migration likho |
| 3 | Backend update karo |
| 4 | Frontend update karo |
| 5 | Tests update karo |
| 6 | Release ship karo |

**Ek naam add karne ke liye poora release!**

**Naya (dictionary):**
```python
creative_approval_statuses: dict[str, ApprovalStatusEnum]
```
```json
UK plan:  {"Prime Video": "APPROVED", "Channel 4": "PENDING", "ITVX": "PENDING"}
US plan:  {"Prime Video": "APPROVED", "Hulu": "PENDING", "Peacock": "REJECTED"}
```
→ **Code me kuch nahi badla.** Paramount+ add karna = naya key. Zero code change.

### Note — "Channel 4" ka example jaan-boojh kar hai

Channel 4 ek **British** broadcaster hai. Ye dikhata hai ki list sirf changeable nahi, **market-specific** bhi hai:

| Market | Channels |
|---|---|
| UK | ITVX, Channel 4 |
| US | Hulu, Peacock |

**Hardcode karna ek market se aage scale hi nahi karega.**

### Note — par VALUES enum hi rahenge

```
KEYS   = data     (channel names — badalte hain)
VALUES = enum     (PENDING / APPROVED / REJECTED — fixed hain)
```

Sab kuch dynamic karna **type safety** kho dega, jo yahan matter karti hai.

### Iska matlab

Document me **ye rule EK section pehle already tha** — targeting step me likha hai ki *"targeting list frequently changes so it should be easy to add new targeting types"*. Channels wahi kism ki list hain. Rule likha tha, apply nahi kiya.

**Aur ek problem maine pakdi:** creative object me **channel ka dimension hi nahi hai** — granularity creative × **market** hai. To ye dictionary abhi populate nahi ho sakti.

---

# Comment 27 — "Tracking Setup"

**David ne likha:** *"could be done before creatives if they are no available yet - no order necessary"*

**Ek baat:** Tracking creative se pehle bhi ho sakti hai. Koi order zaroori nahi.

**Ye chhoti allowance lagti hai — par NAHI hai.**

---

### Example — ghar ke renovation se samjho

```
Ghar renovate karna hai — plumber, electrician, painter chahiye.

❌ Order force karo:
   Plumber pehle → wo 3 din late aaya → electrician bekar baitha
   → painter bekar baitha → 3 din waste

✅ Parallel:
   Teeno ko bulao, jo aaye wo kaam kare
   → Par AAKHIR ME ek FINAL INSPECTION chahiye
   → warna adhoora ghar handover ho jaayega
```

**Purana (forced order):**
```
Step 8:  strategy created ✅
Step 9:  creative upload — 🔴 agency ne bheja nahi. RUK GAYE.
Step 10: (block)
Step 11: (block)  ← jabki ad tag AAJ ho sakta tha
Step 12: (block)  ← jabki credit AAJ check ho sakta tha
```

**Naya (parallel):**
```
Step 8: created ✅
        ├─→ Creatives    🔴 agency ka wait (3 din)
        ├─→ Tracking     ✅ AAJ HO GAYA
        └─→ Credit       ✅ AAJ HO GAYA
        
Day 3:  creative aaya → Step 13 JOIN NODE → sab check → ACTIVATE
```
**3 din bache.**

### Note — ye kaam kaise aata hai, uska match karta hai

| Kaam | Kaun karta hai | Kitna time |
|---|---|---|
| Creatives | Agency | Aksar late |
| Ad tag | Advertiser ke developers | Din lag sakte hain |
| Credit | Finance | Alag process |

**Koi doosre par depend nahi karta.** Order force karne ka matlab ek late item sab kuch block kar deta hai.

### Note — order hatane se ek GATE zaroori ho jaata hai

Pehle **order hi guarantee** tha ki sab complete hai. Ab explicit checklist chahiye:

| Prerequisite | Kab theek |
|---|---|
| Creatives uploaded | Plan ki har duration ke liye ek |
| Creatives approved | Har channel ne APPROVED diya |
| Targeting written | Baseline lagi ya trader ne refine kiya |
| Budget allocated | Per format, accept ya edit hua |
| Ad tag registered | Off-Amazon hai aur tag laga hai |
| ASINs attached | On-Amazon hai aur validate hue |
| Conversions chosen | Chune ya jaan-boojh kar skip kiye |
| Credit sufficient | Balance ≥ budget |

### Iska matlab

Chaar sequential steps **teen parallel branches + ek join node** ban gaye.

**Aur document ne ye already imply kiya tha bina kahe** — creative approval step me likha hai *"a plan can be fully approved and funded and still not launch until the creative clears."* Wo prose me likha hua launch gate hai. Ab wo ek checklist hai.

---

# Comment 28 — "Confirm with client"

**David ne likha:** *"no they can be updated on the strategy after creation"*

**Ek baat:** Strategy creation ke baad update ho sakti hai. To ASINs ki timing koi problem nahi hai.

---

### Example — form submit se samjho

```
Document soch raha tha:
   "Form submit ho gaya = sab lock. Ab kuch nahi badal sakta.
    Isliye ASINs pehle bharne padenge."

Asliyat:
   "Submit ke baad bhi EDIT kar sakte ho."
   → to ASINs baad me bhar do
```

```
Create:  POST /api/strategies/
         { "product_asins": [], ... }
         → 201, VMA2026368

Baad me: PATCH /api/strategies/VMA2026368/
         { "product_asins": ["B08N5WRWNW"] }
         → attach ho gaya
```

### Note — ye Comment 27 ko KAAM karne deta hai

| Comment | Kya hai |
|---|---|
| 27 | **Behaviour** — koi order zaroori nahi |
| 28 | **Mechanism** — creation ke baad update ho sakta hai |

Creative, tracking aur credit branches se order hatana **sirf tab** sense banata hai jab wo branches **already exist karti hui strategy me wapas likh sakein**.

**Do comments ek hi change ke do side hain.**

### Note — par kuch fields par GUARDRAIL chahiye

Jawab measurement fields ke baare me tha. Isko "kuch bhi badal sakta hai" **nahi** padhna chahiye:

| Safe hai | Guardrail chahiye | Kyun |
|---|---|---|
| `product_asins` | `market_budgets` | PG deal already poora budget owe karti hai |
| `product_location` | `market_deals` | Deal book ho chuki hai |
| Ad tag, conversions | `flight_dates` | Booking se bandhi hui |
| Creatives | `markets` | Poora plan invalid ho jaayega |
| Targeting, frequency cap | | |

**Example ka khatra:**
```
Strategy me PG deal hai — £10,000 pe 500,000 impressions committed.
Koi budget PATCH karke £5,000 kar deta hai.

→ Deal phir bhi £10,000 owe karti hai
→ Plan kehta hai £5,000, commitment kehta hai £10,000
→ Ye disagreement kabhi resolve nahi hoga
```

### Iska matlab

Document creation ko **point of no return** maan raha tha — wo galat tha.

Par "updatable" ka matlab "sab kuch" nahi hai. Kuch fields me **paise** hain, aur unpar guardrail chahiye.

---
---

# Poora Summary — ek page

## 28 comments, ek line me har ek

```
 1  3P targeting Amazon YA SSP se — per deal choice
 2  Fee data provider se, profile se nahi. Compound nahi hoti
 3  Budget split optional
 4  Audiences optional — decline karna valid hai, aur sasta
 5  Audience targeting ka hissa. Targeting bhari hui aati hai
 6  CTV ke liye kaato, baaki khud pata karo — trader se sirf 3 sawaal
 7  Naam generate karo
 8  M1 me ek market. Reach markets ke across add hoti hai, providers ke across nahi
 9  Currency puchni nahi (par platform par advertiser se aati hai)
10  Frequency KPI ke saath target value 2-5. Ye forecast badal deta hai
11  "Table" widget hai, data type nahi
12  CTV me bid nahi (par floor deals me hai — aur wahi majority hai)
13  ADVERTISER-LEVEL SETTINGS — naya concept. is_locked chahiye
14  Format hamesha streaming_tv. Prime Video channel hai
15  Category advertiser se ya brief se
16  Selling location Step 1 se hatao
17  ASINs baad me — empty create, phir PATCH
18  Deals match karo. Par tier capability aur PG commitment BOLNA hai
19  Amazon audiences 3P par bhi chalti hain
20  bundles exist nahi karta. Flat list milti hai, grouping hamari
21  Location market ke country se default. markets != location
22  Device advertiser ki setting. streaming_tv ka matlab TV screen NAHI
23  Approval = status change. Manager gaya, interrupt gaya
24  simple-strategies. Aur 14 endpoint corrections
25  Click URL optional — TV par click nahi hota
26  Per channel ek status. Keys data, values enum
27  Koi order nahi — 3 parallel branches + join node
28  Creation ke baad update ho sakta hai. Par budget/deals par guardrail
```

## 6 bade themes — 28 comments inhi ke around hain

| Theme | Kaunse comments |
|---|---|
| **Form nahi, baat-cheet hai** — trader se kam pucho | 6, 7, 9, 13, 14, 15, 16, 17, 18, 21, 22 |
| **Requirement aur Source alag hain** | 6, 7, 9, 21 |
| **Advertiser-level settings** (naya concept) | 13, 15, 16, 22 |
| **Ek galti kabhi akeli nahi hoti** | 1 & 19, 16 & 17 & 28, 24 |
| **Faisle se zyada uska ASAR matter karta hai** | 4, 12, 22, 27 |
| **Agent ko saaf bolna chahiye jab wo verify na kar sake** | 3, 4, 8, 12, 18, 19, 21 |

## Kitna kaam nikla

| | |
|---|---|
| Comments | 28 |
| Question band hue | 4 |
| Naye question raise kiye | 22 blocks |
| Endpoint corrections | 14 |
| Endpoints jo exist hi nahi karte | 2 |
| Naye schema fields/models | 5 |
| Platform par verify kiye conflicts | 12 |

---

**Ye document `strategy_schema_documentation_v3.md` ke review notes se bana hai, aur platform par 4 August 2026 ki verification se cross-check kiya gaya hai.**
