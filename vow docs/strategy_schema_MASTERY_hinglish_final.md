# Strategy Schema — Mastery Document (Hinglish)

**Ye kis liye hai:** `strategy_schema_documentation_v3_final.md` 2,500+ lines ka English spec hai. Ye document uska **dimaag** hai — asaan Hinglish me, example ke saath, taaki koi bhi kuch bhi pooche to turant jawab de sako aur baar-baar spec kholna na pade.

**Kaise padhna hai:**

| Agar tumhe | To padho |
|---|---|
| Zero se samajhna hai | Part 1 se shuru karo, sequence me |
| Meeting se pehle revise karna hai | Part 7 (jo galat tha) + Part 15 (rapid fire) |
| Koi ek cheez confirm karni hai | Part 15 me search karo |
| Kal se coding shuru karni hai | Part 16 (nodes) |

**Ek line me pura document:** *Trader baat karke brief deta hai, agent 30+ fields bharta hai, Amazon ki inventory me se deal dhoondta hai, audience suggest karta hai, forecast nikalta hai, aur ek executable Strategy card banata hai — par platform ki API me 11 cheezein hum galat samajhe the aur 2 cheezein abhi blocked hain.*

---
---

# PART 1 — Bilkul zero se: advertising ki bhasha

Ye part sabse zaroori hai. Agar ye clear nahi hua to aage kuch samajh nahi aayega.

## 1.1 Impression, Reach, Frequency — teen alag cheezein

Socho tumhare mohalle me **100 ghar** hain. Tum ek poster leke nikle.

```
Tumne 300 posters chipkaye  →  300 IMPRESSIONS  (kitni baar ad dikha)
Wo 100 gharon ne dekha       →  100 REACH        (kitne LOG ne dekha)
Har ghar ne 3 baar dekha     →  3 FREQUENCY      (ek banda kitni baar dekha)
```

**Formula:** `Impressions = Reach × Frequency`

**Kyun important hai:** Trader kehta hai "mujhe zyada reach chahiye" — matlab **naye log** chahiye. Agar tum sirf impressions badhaate ho to same log baar-baar dekhenge, naye log nahi milenge.

**Real example:**

```
Budget £10,000, CPM £23  →  435,000 impressions

Case A: Frequency 3  →  Reach = 435,000 / 3 = 145,000 log
Case B: Frequency 8  →  Reach =  435,000 / 8 =  54,375 log

Same paisa. Par Case A me 90,000 zyada log ne dekha.
```

Isi liye **frequency cap** hota hai — "ek bande ko hafte me max 3 baar dikhao". Cap lagao to reach badhta hai.

🔴 **Yaad rakho:** VOW me frequency cap **per WEEK** hai, per day ya per campaign nahi.

## 1.2 CPM — sabse important word

**CPM = Cost Per Mille = 1,000 impressions ka daam.** "Mille" Latin me 1,000.

```
CPM £20 ka matlab: 1,000 baar ad dikhane ke £20
Budget £10,000  →  £10,000 / £20 × 1,000 = 500,000 impressions
```

**Ulta formula (ye zyada use hoga):**

```
Impressions = (Budget ÷ CPM) × 1,000
```

**Example:** £10,000 budget, CPM £22.96
`10,000 / 22.96 = 435.5` → `× 1,000` = **435,540 impressions**

🔴 **Warning:** CPM zero ho to divide by zero — crash. Aur VOW me **2 deals ka CPM zero hai** (dono FIFA 2026 ZA). Code me guard chahiye.

## 1.3 Auction — ad kaise bikta hai

Ye samajhna zaroori hai warna deal types samajh nahi aayenge.

**Scene:** Tum Prime Video pe movie dekh rahe ho. Ad break aaya. **Us 1 second me ye hota hai:**

```
1. Prime Video bolta hai: "Ek ad slot khaali hai. Dekhne wala:
   London, 25-34 saal, mobile pe, sports dekh raha hai"

2. Ye message 50 advertisers ko jata hai (milliseconds me)

3. Sab bid lagate hain:
      Nike       £24
      Adidas     £22
      Pepsi      £19
      Local shop  £8

4. Nike jeeta. Nike ka ad chala.

5. Nike ne kitna diya? Do system hote hain:
      First price  → £24 (jo bid kiya wahi)
      Second price → £22.01 (dusre se ek paisa zyada)
```

**Pura process 100 milliseconds me.** Din me arbon baar hota hai. Isi ko **programmatic advertising** kehte hain.

**Do taraf ke players:**

```
DSP  (Demand Side Platform)  =  Advertiser ki taraf — bid lagata hai
                                Amazon DSP, ye hum use karte hain

SSP  (Supply Side Platform)  =  Publisher ki taraf — slot bechta hai
                                Prime Video, Netflix, Channel 4 ki taraf
```

VOW **Amazon DSP ka reseller** hai — matlab VOW ke paas Amazon DSP ka access hai aur wo apne clients ko bechta hai.

## 1.4 Floor rate vs Fixed CPM — ye 92% wala point hai

**Floor rate = minimum daam, final daam nahi.**

Socho tum property bech rahe ho. Do tareeke:

```
FIXED PRICE   "50 lakh. Bas. Isi me milega."
              Tumhe 50 lakh dene padenge. Kam nahi, zyada nahi.

FLOOR PRICE   "Minimum 50 lakh. Isse kam offer mat karo."
              Tum 50 de sakte ho, ya 55, ya 60 — jitna zyada, jeetne ka
              chance zyada. 49 nahi de sakte.
```

**Ad me exactly same:**

```
FIXED_CPM £22    →  £22 hi lagega. Bid ka koi matlab nahi.
FLOOR_RATE £22   →  minimum £22. Tum £25 bid karo to zyada auctions jeeto ge.
```

🔴 **Ye document ka sabse bada correction hai.** Pehle likha tha *"CTV me CPM fixed hote hain, bid ka lever nahi hai"*. **Galat.**

```
369 deals me:
   FLOOR_RATE   341   (92%)   ← bid MATTER karta hai
   FIXED_CPM     28   (8%)    ← bid ka matlab nahi
```

**92% inventory pe bid ek asli lever hai.** Aur ye sabse **kam nuksaan wala** lever hai — audience chhoti nahi karni padti, plan ka shape nahi badalta, sirf daam badhta hai.

## 1.5 Deal kya hai — thok me khareedna

**Deal = advertiser aur publisher ke beech ek pehle se tay kiya hua rasta.**

Analogy: Tum roz sabzi mandi jaate ho aur bhaav-taav karte ho (= open auction). Ya tum sabziwale se **mahine ka contract** kar lo — "roz 5 kilo tamatar, ₹30 kilo, pehle mujhe dena". Wahi deal hai.

**Deal me kya milta hai:**

```
Kaun dikhayega          Prime Video
Kitne ka                £22.96 CPM (floor)
Kis market me           UK
Kitni lambi ad          15s, 20s, 30s
Kis device pe           Connected TV
Kaun sa content         Sports, ya ROS (Run of Service = sab kuch)
```

## 1.6 Teen deal types — hotel ki analogy

Ye David ne bahut pucha tha, isliye achhe se samjho.

Socho ek hotel me 100 kamre hain. Teen tareeke se bikte hain:

### PROGRAMMATIC GUARANTEED (PG)

```
"20 kamre mere naam pakke kar do, 25 tarikh ko. ₹5,000 per kamra.
 Guaranteed. Koi aur nahi le sakta."

Hotel ka wada:    20 kamre PAKKE milenge
Tumhara wada:     ₹1,00,000 dena PADEGA — aao ya na aao
Auction:          NAHI hota. Sab pehle se tay.
Cancel:           NAHI ho sakta
```

**Ad me:** delivery **guaranteed**. Pura budget committed. Pause nahi kar sakte.

🔴 **VOW ki inventory me EK BHI PG deal nahi hai.** Sab 369 deals check kiye. Iska matlab:

> **Koi bhi plan impressions ka WADA nahi kar sakta. Har forecast sirf ANDAAZA hai.**

Ye agent ko bolna padega. Trader ne "435,000 impressions" padha aur usko guarantee samjha — to hum ne dhoka diya.

### PREFERRED DEAL

```
"Mujhe PEHLE poochho. ₹5,000 fix. Mai haan ya na bolunga."

Hotel ka wada:    tumhe PEHLE offer karunga
Tumhara wada:     KUCH NAHI. Mana kar sakte ho.
Auction:          NAHI, par tumhe accept karna hoga
Daam:             FIXED
```

**Ad me:** first look milta hai. Daam fix. Lena zaroori nahi. **VOW me 28 deals (8%)**.

### PRIVATE AUCTION

```
"5 chuni hui companies bid karengi. Minimum ₹4,000. Sabse zyada wala jeetega."

Hotel ka wada:    kuch nahi, bas tum invited ho
Tumhara wada:     kuch nahi
Auction:          HAAN hota hai, par sirf invited log
Daam:             FLOOR (minimum) — upar jaa sakta hai
```

**Ad me:** private club ka auction. **VOW me 341 deals (92%)** — yahi asli inventory hai.

### Ek table me

| | PG | Preferred | Private Auction |
|---|---|---|---|
| Delivery guarantee | ✅ Haan | ❌ Nahi | ❌ Nahi |
| Auction hota hai | ❌ Nahi | ❌ Nahi | ✅ Haan (invited) |
| Daam | Fixed | Fixed | Floor (minimum) |
| Budget commit | ✅ Pura dena padega | ❌ Nahi | ❌ Nahi |
| VOW me kitne | **0** | 28 | **341** |

## 1.7 CTV kya hai

```
CTV      Connected TV — internet wale TV pe ad. Smart TV, Fire Stick, Roku.
         Prime Video, Netflix pe jo ad aata hai.

OLV      Online Video — YouTube type, laptop/mobile pe

Display  Banner ad — image

Linear TV  Purana cable TV — time slot khareedte the, banda nahi
```

**Farak samjho:** Linear TV me tum "raat 9 baje ka slot" khareedte the — pata nahi kaun dekh raha. CTV me tum **banda** khareedte ho — "London ka 25-34 saal ka jo sports dekhta hai".

**Hamara M1 sirf CTV hai.** Display aur OLV baad me.

## 1.8 Endemic vs Non-endemic

```
ENDEMIC       Amazon pe becha jata hai
              → ASIN se track hota hai (Amazon product ID)
              Example: Nike shoes Amazon pe bikte hain

NON-ENDEMIC   Amazon pe nahi bikta
              → apni website pe AD TAG lagana padta hai
              Example: ek university, ek bank, ek insurance company
```

**Schema me:** `product_location` = `ON_AMAZON` ya `NOT_SOLD_ON_AMAZON`

Ye decide karta hai ki tracking ke liye **ASIN** chahiye ya **ad tag**.

---
---

# PART 2 — VOW aur Strategy

## 2.1 VOW kya karta hai

```
Amazon DSP  ←  VOW (reseller)  ←  Advertisers (Nike, university, bank)
```

Amazon DSP directly sabko nahi milta. VOW ke paas access hai, VOW clients ko service deta hai.

## 2.2 Strategy kya hai

**Strategy = ek campaign ka plan.** Amazon DSP me jaake ye **Campaign + Ad Group** ban jata hai.

Ek strategy me kya hota hai:

```
Naam            "Nike UK CTV Awareness Sep 2026"
Kab             1 Sep – 30 Sep 2026
Kahan           UK
Kitna paisa     £10,000
Kya goal        Awareness (log jaane)
Kya naapenge    Reach
Kitni lambi ad  30 second
Kahan dikhega   Prime Video ki inventory (deal ke through)
Kisko dikhega   Sports dekhne wale 25-44 (audience)
```

## 2.3 Manual way vs Agentic way

**Manual (aaj):** trader VOW ke website pe 5-step wizard bharta hai. 30+ fields. Deals ki table me se checkbox lagata hai. 20-30 minute.

**Agentic (hum bana rahe hain):** trader ek line likhta hai —

> *"£10,000 in the UK for September, 30-second creative, Prime Video"*

— aur agent baaki sab khud karta hai, jo nahi pata wo poochta hai, aur ek Strategy card deta hai.

**Ye document us agent ka contract hai.**

---
---

# PART 3 — Char principles (agent ke rules)

Ye char rules pura design chalate hain. Interview me poochein to ye batana.

### 1. Zero Hallucination — apne mann se kuch nahi, AUR sab kuch verify

Ye principle ke **do hisse** hain. Log pehla hissa yaad rakhte hain, dusra bhool jaate hain — aur dusra zyada khatarnak hai.

#### Hissa 1 — Agent khud kuch nahi banayega

**Galat:** *"Prime Video ka CPM around £20 hoga"*
**Sahi:** *"Prime Video UK ROS: £22.96 CPM"* (deal API se aaya)

#### 🔴 Hissa 2 — User ne bol diya, iska matlab wo SAHI hai — aisa NAHI hai

**Ye sabse important baat hai is poore document me.**

User ne kuch bola, to bhi **jaake check karna padega** — registry me, DB me, ya API me. Jab tak match na ho, aage nahi badhna.

**Teen example, teeno me ek hi galti:**

| User bola | Bewakoof agent | Asli me kya hoga |
|---|---|---|
| *"Naam Nike UK Sep 2026 rakh do"* | Naam plan me daal diya | **Us naam se strategy pehle se hai.** Sab kuch tay hone ke baad, last step pe create fail hoga |
| *"Netflix pe chalao"* | `channel = Netflix` | **GB me 30s ka Netflix deal hi nahi hai.** Plan me ek aisi line hai jo khareedi nahi ja sakti — aur pata create time pe chalega |
| *"Tablet ko hata do"* | `device_types` me `TABLET` daal diya | **`TABLET` value API me exist hi nahi karti.** Field chupchap galat hai |

**Teeno case me agent ne kuch INVENT nahi kiya.** Par kuch VERIFY bhi nahi kiya. **Plan utna hi tuta hua hai.**

#### To rule ke TEEN hisse hain, ek nahi

```
1. INVENT MAT KARO        koi value model ke apne guess se na aaye
2. HAMESHA VERIFY KARO    har value — user ki boli hui bhi — plan me
                          ghusne se PEHLE apni authority se check ho
3. CHUPCHAP FIX MAT KARO  jo verify fail kare, wo BATANA hai —
                          chupchap sudharna, hatana ya badalna NAHI
```

#### Teesra hissa sabse zyada bhoola jata hai

Ye char kaam **madadgaar** lagte hain, par teeno galat hain:

```
Naam already hai        →  "-2" laga dena          ❌
TABLET invalid hai      →  chupchap list se hata dena ❌
Postcode 5 match kare   →  pehla utha lena          ❌
Channel parse nahi hua  →  "ROS" ya Prime Video maan lena ❌
```

**Ye char kaam karne se plan BAN JAYEGA aur CHAL JAYEGA.** Isi liye khatarnak hain — koi error nahi aayega, koi investigate nahi karega, aur trader apne hi campaign ke baare me galat baat maan rahega.

> **Verification fail hona ek CONVERSATION hai, cleanup nahi.**

#### Timing ka rule — confirm se PEHLE validate

```
GALAT   extract → trader ko confirm → validate → problem mila
        Trader ne aisi cheez pe haan bol diya jo ban hi nahi sakti.
        Ab agent ko apna hi "samajh gaya" wapas lena padega.

SAHI    extract → validate → trader ko confirm
        Confirmation me sirf wahi jo verify ho chuka hai.
```

**Isi liye validation ek alag step hai**, extraction ke andar nahi. Aur isi liye agent legitimately keh sakta hai *"maine ye samjha"* — kyunki usme sab checked hai.

#### Har field ki authority — poori table

| Field | Kahan check hoga | Kya check | Fail hone pe |
|---|---|---|---|
| **Strategy name** | `check_strategy_name_uniqueness/` | Ye naam pehle se hai? | Clash batao + alternative do. **"-2" apne aap NAHI lagana** — trader ne jaan-boojh ke purane campaign ka naming chuna ho sakta hai |
| **Markets** | market enum (21) **+** `/deals/` | Code valid hai? **Aur us market me deal hai?** | Valid-par-khaali asli case hai — 21 me se 3 market me ek bhi deal nahi. Batao kaunse market me hai |
| **Flight dates** | Business rules | Start future me? End start ke baad? Length limit me? | Exact problem batao, "invalid dates" nahi |
| **Budget** | `/credits/summary/` | Credit balance kaafi hai? | Kitna kam hai, number me batao. **Ye Step 1 pe check ho sakta hai**, Step 12 tak wait nahi |
| **Currency** | currency enum (19) **+** advertiser | Valid code? Advertiser se match? | Mismatch error nahi hai — conversion hai. Rate batao aur bolo hisaab kis currency me kiya |
| **Durations** | duration enum (7) **+** deal `ad_lengths` | Valid? **Aur matched deals support karte hain?** | 45s plan par 45s deal nahi = khareed nahi sakte. Batao inventory kaunsi duration support karti hai |
| **KPI** | kpi enum (16), **ya automated ka 5-value set** | Valid? **Aur jis endpoint pe ja rahe hain wahan allowed?** | `/strategies/` pe valid KPI `/automated-strategies/` reject kar sakta hai. **Jo endpoint use ho raha hai, uske against check karo** |
| **`target_kpi`** | Per-KPI range | Range KPI pe depend karta hai. Frequency 2–5, ROAS decimal | Error message me KPI ka naam bhi ho |
| **Channel** | `/deals/` + naam parsing | Is market + duration me is channel ke deal hain? | **Count batao.** Zero match aam baat hai — plainly bolo, aur jo available hai wo batao |
| **`specific_deal_id`** | `/deals/` | Deal hai? Is market ko serve karta hai? Duration support karta hai? | Haath se deal ID dene wale case me hi purani ID hone ka chance sabse zyada |
| **Product categories** | `/product-categories/` | Category hai? Selectable leaf hai? | 25,973 hain — hamesha search. Non-leaf select nahi ho sakta |
| **ASINs** | `asin-validation/` | Har ASIN hai? Isi advertiser ka hai? | **Per-ASIN batao**, ek saath pass/fail nahi |
| **Locations / postcodes** | `/locations/{market}/?query=` | Har term exactly ek ID pe resolve hua? | Teen tarah: resolved · **ambiguous → POOCHHO** · unresolved → BATAO. Chupchap drop nahi |
| **Custom radius** | `POST /locations/{market}/` | Address resolve hua? Unit km ya miles? | Address na mile to batao, andaaza mat lagao |
| **Audience set** | `/audience-sets/` | Exist karta hai? Is market pe lagta hai? | — |
| **Conversion types** | `/conversions/definitions/` | **Is market ke liye** valid event? | `CHECKOUT` GB-only, `SEARCH` US-only. **Market badla to purani selection dobara invalid ho jaati hai** |
| **Device types** | Device value set | Valid? `streaming_tv` pe `CONNECTED_TV` hai? | `TABLET` exist nahi karta. **Batao — chupchap hatao NAHI.** Trader samajh raha hai tablet exclude ho gaya |
| **Mobile OS** | `IOS` / `ANDROID` | `MOBILE` device me hai tabhi set ho | MOBILE ke bina set karna **validation error** hai, silent no-op nahi |
| **Creative duration** | Plan ki `durations` | File ki length plan se match? | Mismatch = economics badli = **re-approval** |
| **Impression target** | `allocation_mode` | Budget ya impression — **ek hi** authoritative | Dono set aur mode nahi = ambiguous. Poochho kaun chalega |
| **Frequency cap** | Advertiser defaults | Advertiser ne lock kiya? | 🔴 **D47 se blocked** — 403 aata hai, lock detect nahi ho sakta |

#### Do jagah validate KAR HI NAHI SAKTE (aur ye blocker hain)

| Field | Authority | Halat |
|---|---|---|
| Frequency cap, device policy, product categories, selling location | `/admin/advertiser/{id}/` | 🔴 **403** — D47 |
| Channel | Deal pe `channel` field | 🔴 **Exist nahi karta** — naam se parse, `PARSED_GUESS` mark karo. D53 |

**Jahan authority nahi hai, wahan value ko "unverified" mark karna hai — "verified" maan lena nahi.**

Yahan pehla aur chautha principle milte hain: **jo check nahi ho saka, wo pass hone ke barabar nahi hai** — aur plan ko ye farak pata hona chahiye.

### 2. Self-Filling Form — form khud bharta hai

Trader ko 30 fields nahi bharne. Wo baat karta hai, agent slots bharta hai.

```
Trader: "£10,000 UK September Prime Video 30s"

Agent bharta hai:
   markets          = ["GB"]        ← "UK" se
   budget           = "10000.00"    ← "£10,000" se
   flight_dates     = 1-30 Sep 2026 ← "September" se
   durations        = ["30"]        ← "30-second" se
   channel          = "Prime Video" ← seedha
   formats          = streaming_tv  ← CTV hai to hamesha yahi
   goal             = AWARENESS     ← default, par BOLKAR
   currency         = advertiser se
```

### 3. API-Driven — tools se kaam

Agent bolta nahi, **karta** hai. Deal chahiye? API call. Location chahiye? API call.

### 4. Stated Uncertainty — jo pata nahi, wo bolo

Ye chautha principle **naya** hai, aur is verification ke baad add hua.

```
"Prime Video ka reach 145,000"                    ← forecast API se, sach
"Channel 4 ka reach nahi mil sakta, 3P hai"       ← honestly bola
"Ye deal Netflix ka LAGTA hai (naam se guess)"    ← guess, aur bola ki guess hai
```

🔴 **Ye principle isliye zaroori hua** kyunki deal pe `channel` field hi nahi hai — agent ko naam parse karna padta hai. Parse kiya hua channel guess hai, fact nahi. Usko fact ki tarah dikhana jhooth hai.

---
---

# PART 4 — 13 steps ka pura flow

Ye document ka dil hai. Har step: kya hota hai, kya API, example.

## Step 1 — Basics (sabse bada step)

**Yahan 30+ fields bharte hain.** Par trader se sirf 3-4 poochte hain, baaki nikal lete hain.

**Trader ne likha:**
> *"£10,000 in the UK for September, 30-second creative"*

**Agent ne kya bhara:**

| Field | Value | Kahan se aaya |
|---|---|---|
| Strategy name | "UK CTV Awareness Sep 2026" | Agent ne banaya (optional field hai) |
| Flight dates | 2026-09-01 to 2026-09-30 | "September" se |
| Markets | ["GB"] | "UK" se |
| Currency | advertiser se (jaise EUR) | 🔴 **market se NAHI** |
| Durations | ["30"] | "30-second" se |
| Formats | streaming_tv | CTV hai → constant |
| Goal | AWARENESS | **Default, par bolkar** |
| KPI | REACH | Goal se |
| Budget | £10,000 | Seedha |
| Product location | poochna padega | ASIN ya ad tag decide karega |

**Kya nahi pata? Wahi poochho.** Ek baar me ek sawaal, saare nahi.

### Field sources — 5 tarah se value aati hai

| Source | Matlab | Example |
|---|---|---|
| **ASKED** | Trader se poochna padega | Budget |
| **INFERRED** | Brief se nikala | "UK" → GB |
| **DERIVED** | Dusri field se banaya | Goal → KPI |
| **ADVERTISER** | Advertiser ki settings se | Currency, frequency cap |
| **API** | Server se padha | Deal CPM, fee |

🔴 **Ye "Source" column add karna ek bada insight tha.** Pehle sirf "Required / Optional" tha. Par *"required hai"* aur *"poochna padega"* **do alag baatein hain.** Currency required hai — par kabhi poochte nahi.

### Char tarah ki pre-filled values — David ka comment

David ne bola *"goal FIXED nahi hai, defaulted hai"*. Isse ye model nikla:

| Category | Matlab | Agent kya karta hai | Example |
|---|---|---|---|
| **CONSTANT** | Ek hi value hai, sabke liye | Kuch nahi bolta | `formats = streaming_tv` |
| **DEFAULTED** | Pehle se bhara, badal sakte ho | Kuch nahi bolta | Location |
| **DEFAULTED-ADVISED** | Pehle se bhara + agent batata hai | **Bolta hai** | Goal |
| **LOCKED** | Advertiser ne lock kiya, badal NAHI sakte | Batata hai ki locked hai | Device types (maybe) |

**Farak kyun matter karta hai:**

```
CONSTANT ko bolna       →  bakwaas. "Format streaming_tv hai" — obviously.
DEFAULTED-ADVISED       →  "Goal Awareness rakha hai kyunki CTV hai.
                            Chahe to badal do."
LOCKED ko chupana       →  trader change karega, error aayega, bharosa tootega
```

### 🔴 Currency — 9% ka jaal (ye zaroor samjho)

**Pehle likha tha:** currency market se aati hai. GB → GBP.
**Asli baat:** currency **advertiser** se aati hai.

**Saboot:**
```
1. Market select karne se PEHLE hi field me EUR bhara hua tha
2. UK select kiya — phir bhi EUR raha
3. Ek live strategy mili: primary_currency = NOK, market = US
   (market se derive karte to ye kabhi na banta)
```

**Aur do currency ek saath chalti hain:**

```
primary_currency          strategy ki currency, advertiser se     EUR
markets_info[].currency   market ki currency, market se           GBP
```

Platform beech me convert karta hai. Rate dekha: **1 GBP ≈ 1.0909 EUR**

```
Trader ne £10,000 daala   →  DB me EUR 10,909.09 store hua
Trader ne £25 bid daala   →  DB me EUR 27.27 store hua
```

**Ab yahan galti hoti hai:**

```
GALAT:  10,909.09 / 22.96 × 1000 = 475,178 impressions
SAHI:   10,000.00 / 22.96 × 1000 = 435,540 impressions
                                    ─────────
FARAK:                              39,638 impressions  (9% galat!)
```

🔴 **Aur deal ki currency alag ho sakti hai.** 369 deals me **8 currencies**:

```
USD 156 · EUR 95 · GBP 35 · CAD 22 · MXN 19 · BRL 16 · AUD 14 · JPY 12
```

**GBP sirf 35 deals me hai! USD sabse zyada.** Matlab ek GB plan me USD wala deal aa sakta hai.

**Rule:** saara hisaab EK currency me karo, aur bolo ki kaun si.

### 🔴 Enums — sab bahut chhote likhe the

`GET /api/strategies/choices/` se sab padha. Har list badi nikli:

| Field | Likha tha | Asli | Galti kahan se |
|---|---|---|---|
| goal | 3 | **15** | CTV screen pe 3 dikhte the |
| format | 4 | **21** (12 channel hain!) | CTV filter |
| KPI | 6 | **16** (automated me 5) | Andaaza |
| currency | 3 | **19** | Sirf 3 market dekhe the |
| market | 2 | **21** (18 me deals) | Deals list ka GB/US filter |
| conversion | 4 | **6** (market-specific) | Sirf GB screen dekha |
| duration | 4 | **7** | Creative screen |

**Do sabak isse:**

1. **Model me chhoti list = ek DECISION hai, fact nahi.** Agar hum restrict kar rahe hain to likhna padega ki kyun — warna agla banda samjhega ki platform ki limit hai.
2. **Hard-code na karo, `/choices/` se padho.** Server pe config hai, koi badal dega to hamari copy purani ho jayegi.

### 🔴 goal — 15 values

```
AWARENESS · CONVERSION · CONSIDERATION · OTHER · PROSPECTING · REMARKETING ·
RETENTION · UPPER_FUNNEL_PROSPECTING · CONVERSIONS_OFF_AMAZON ·
ENGAGEMENT_WITH_MY_AD · CONSIDERATIONS_ON_AMAZON · PURCHASES_ON_AMAZON ·
MOBILE_APP_INSTALLS · PURCHASES_ON_OFF_AMAZON · MULTI_FUNNEL
```

**15 options hain.** Isliye David ka comment (*"goal defaulted hai, fixed nahi"*) **zyada** important ho gaya, kam nahi.

### 🔴 format — 21 values, aur 12 CHANNEL hain

```
Generic formats:
  standard_display · amazon_mobile_display · aap_mobile_app · video ·
  display · online_video · streaming_tv · other

Channels jo API "format" bolti hai:
  prime_video · netflix · disney · paramount · channel4 · pluto ·
  bskyb · hulu · tubi · roku · vevo · dazn · discovery
```

**Ye sabse ulajh wala point hai.** David ne bola *"Prime Video ek channel hai, format nahi"* — **domain me wo bilkul sahi hai.** Par **API aisa nahi maanti** — API ke `format` enum me hi channel list hai.

**Hamara jawab (dono sach rakhte hain):**

```
Plan model me      →  streaming_tv + channel (Prime Video)   ← imaandaar structure
Forecast request me →  prime_video bhi bhejo                  ← wo API isi field pe
                                                                supply lines rakhti hai
```

### 🔴 target_kpi — string hai, integer nahi

**Pehle likha:** `kpi_target_value: int`, 2 se 5.
**Asli:** field ka naam `target_kpi` hai aur **string** hai.

**String kyun sahi hai** (ye sirf API ki marzi nahi):

```
FREQUENCY               3        integer
RETURN_ON_AD_SPEND      4.5      decimal — int me 4 ban jayega!
VIDEO_COMPLETION_RATE   0.85     rate
REACH                   500000   bada integer
```

Integer field 4.5 ka ROAS target chupchap 4 bana deti. **Range check KPI ke hisab se validation me hona chahiye, type me nahi.**

### 🔴 product_categories — string list, int nahi

`List[int]` likha tha. Asli me **`List[str]`** — values lambi numeric strings hain.

Aur **GB me 25,973 categories hain.** Itni list kabhi dikha nahi sakte — ye hamesha **search** se aayega.

---

## Step 2 — Inventory (deal dhoondhna) — sabse dukhi step

**Purana tareeka:** deals ki table, checkbox lagao.
**Naya tareeka:** trader requirement batata hai, agent deal **dhoondhta** hai.

**Kyun:** "Prime Video ya Netflix" — ye asli decision hai. `EXT7P75718S8MNR` vs `EXT7P75719Q2LKM` — ye plumbing hai, trader ka kaam nahi.

### 🔴 369 deals, 83 nahi

```
Bina filter                                          369
GB + streaming_tv                                     62
GB,ZZ + streaming_tv,prime_video,UNKNOWN              83   ← purana number
GB + saare 14 CTV channel formats                     62   ← channel add karne se kuch nahi badla
```

**Dhyan do teesri aur chauthi line pe:** saare channel formats jodne se **ek bhi deal nahi badha**. Par `UNKNOWN` format aur `ZZ` market jodne se **21 deals aa gaye**.

**Matlab wo padding asli kaam ki hai** — bina padding query me inventory chupchap kam ho jaati hai.

### 🔴 Deal pe channel field HI NAHI HAI

Ye sabse bada blocker hai. Saare 369 deals ke saare fields check kiye:

```
✅ HAI:
   external_deal_id · name · deal_type · deal_price_type ·
   deal_price_amount · deal_price_currency · media_types ·
   devices · environments · locations · genre · ad_lengths

❌ NAHI HAI:
   channel          ← kaun dikhayega, ye pata karne ka koi field nahi
   inventory_tier   ← Amazon ya 3P, koi field nahi
   provider         ← nahi
   publisher        ← nahi
```

**To channel kahan hai? Sirf NAAM me.** Agent ko string parse karni padegi.

**Aur naam ke 8 format hain:**

| Prefix | Kitne | Example |
|---|---|---|
| pipe-form | 148 | `Prime Video \| Preferred Deal \| Video \| UK - 15, 20 – ROS` |
| `3PS` | 129 | `3PS_Freewheel_UK_STV_Paramount_My 5` |
| `VowMade` | 78 | `VowMade_Fifa 2026_ZA_Football_CTV_Amazon DSP_3P_MS_MLMBRID8184` |
| `EB` | 6 | |
| `Tubi` | 4 | |
| `TUBI` | 2 | 🔴 wahi channel, casing alag! |
| `62797` | 1 | |
| `APC` | 1 | |

**Ek parser ye 8 handle nahi kar sakta.** Aur `Tubi` vs `TUBI` batata hai ki data controlled vocabulary se nahi aa raha.

**Isliye:** jo bhi naam se nikala, usko **"derived" mark karna padega** — `channel_confidence: PARSED_CONFIDENT / PARSED_GUESS / UNKNOWN`.

**Ye D53 hai — document ki sabse badi data request:** *"deal object pe ek asli `channel` field de do"*. Ek field poori ek class ki galti mita degi.

### 🔴 genre field hai par null hai

Teen Paramount deals dekhe. Teeno me naam me channel hai, aur `genre: null`:

```
3PS_Freewheel_UK_STV_Paramount_My 5           genre: null
3PS_Freewheel_UK_STV_Paramount_Paramount+     genre: null
3PS_Freewheel_UK_STV_Paramount_PlutoTV        genre: null
```

To "genre upsell" ka jo idea tha (Sports genre £22 me suggest karo ROS £18 ke bajaye) — uske paas **koi structured field nahi hai.**

### Teen inventory tiers

| Tier | Example | Deal milega? | Reach forecast? |
|---|---|---|---|
| **Amazon owned** | Prime Video, Twitch | Haan, abhi | ✅ Milega |
| **3P pre-curated** | Netflix, Hulu | Haan, abhi | ❌ Nahi |
| **3P needs curation** | Disney+ | Nahi — VOW baad me banayega | ❌ Nahi |

🔴 **Ye tier bhi hamara concept hai, API ka nahi.** Naam se channel nikalo, channel se tier — do level ka guess.

### 🔴 Inventory sources — 4 hain, "50+" nahi

`/inventory-sources/` teen params maangta hai (`goal` + `strategy_formats` + `markets`), warna 400.

```
streaming_tv + GB + AWARENESS         →  2
Saare 14 CTV channel formats + GB     →  2   (channel add karne se kuch nahi)
Saare formats (display + OLV bhi)     →  4   ← MAXIMUM
Saare 21 markets                      →  3
```

**Char sources hain, bas:**

```
Amazon Publisher Direct   AMAZON_PUBLISHER_DIRECT   display, online_video
Amazon Streaming TV       AMAZON                    streaming_tv
Third Party Exchange      THIRD_PARTY_EXCHANGE      display, online_video
Twitch                    AMAZON                    display, streaming_tv
```

**CTV ke liye sirf 2:** Amazon Streaming TV aur Twitch. Bas. Ye poora CTV supply surface hai source level pe.

**"50+ inventory" kis cheez ka tha?** Sources ka nahi (4 hain). Sabse likely **369 deals**, ya **21-value format enum**. Ye **D54** hai — Wajahat se confirm karna hai.

---

## Step 3 — Budget Split (optional)

Budget ko inventory ya duration me baant do.

```
Total £10,000
   Prime Video   £6,000  →  CPM £22.96  →  261,000 impressions
   Channel 4     £4,000  →  CPM £18.50  →  216,000 impressions
```

Ya duration ke hisab se: 15s sasta, 30s mehnga.

---

## Step 4 — Audiences (optional!)

**Audience zaroori NAHI hai.** Trader teeno mana kar sakta hai aur bina audience plan chala sakta hai.

**Agent 3 options deta hai:**

```
NARROW     kam log, zyada sahi log
BALANCED   beech ka
WIDE       zyada log, kam precise
```

### 🔴 Teeno ka daam SAME hai — ye bada correction tha

Pehle code likha tha: *"Narrow chhoti hai AUR mehngi hai"*. **Galat.**

**Fee ke teen rule (David ka comment):**

```
1. TRIGGER      1P data use karo to fee lagti hai
2. NO COMPOUND  ek provider se 1 segment lo ya 50 — fee same
3. STACKING     do alag provider (Amazon + Experian) → dono ki fee
```

**Fee data provider pe depend karti hai, profile pe nahi.** Narrow/Balanced/Wide **reach aur precision** me farak hai, **daam** me nahi.

### 🔴 DO alag fee hain — ye document ki galti thi

Pehle likha: audience fee `/contextual-targeting/fees` se aati hai. **Galat.**

| Fee | Kahan hai | GB streaming TV |
|---|---|---|
| **Audience data fee** | **audience set object pe** — `video_fee` | **1.63** GBP |
| **Contextual targeting fee** | `/contextual-targeting/fees` | **0.450** GBP |

**Path hi clue tha:** `contextual-targeting/fees` = **contextual (product category) targeting** ki fee. Audience ki nahi.

**Dono ek plan me lag sakti hain:**

```
1.63 (audience) + 0.450 (contextual) = 2.08 GBP per 1,000 impressions
                                        extra, deal CPM ke UPAR
```

Ye **D49** hai: dono add hoti hain ya nahi? Jab tak jawab na mile, agent sahi effective CPM nahi bol sakta.

### Effective CPM — jo asli number hai

```
Deal CPM              £22.96
+ Audience fee        £ 1.63
─────────────────────────────
Effective CPM         £24.59

Impressions = 10,000 / 24.59 × 1000 = 406,669
(deal CPM se hisab karte to 435,540 — 29,000 zyada dikhata)
```

### 🔴 Amazon audience 3P inventory pe bhi chalti hai

Pehle code me likha tha *"Prime Video portion only"*. **Galat.** Amazon ki audience Netflix/Channel 4 pe bhi lag sakti hai. Deal ki targeting ek **alternative** hai, majboori nahi.

### 🔴 35 audience sets, 15 nahi

15 wala number UI ke pehle page se aaya tha. API me **35** hain.

---

## Step 5 — Targeting (David ke naye comments yahan hain)

### Location — 4 comments ka jawab

**David ke comment:**
1. *"user location search kar sakta hai?"*
2. *"postcode list validate karke IDs nikalne padenge"*
3. *"address + radius se custom location bana sakte hain"*
4. *"include aur exclude ki list hai, ye GB default ko replace karegi"*

**Sab confirm hue. Jawab:**

**(1) Haan, ye SEARCH endpoint hai.** Bina query 400 deta hai: *"Query must be at least 2 characters long"*

```
GET /strategies/locations/GB/?query=SW1

{
  "nextToken": null,
  "geoLocations": [
    {"name": "London, England, UK - SW1Y",
     "id": "XHvCjcKHXsKGemnCjsKQbMKX",
     "category": "POSTAL_CODE"}
  ]
}
```

**Teen cheezein isse pata chali:**
- Location **ID** hai, free text nahi — aur ID **opaque string** hai, number bhi nahi
- Minimum 2 character chahiye
- `category` field hai — `POSTAL_CODE` mila (CITY/REGION bhi hone chahiye)
- `nextToken` aur `geoLocations` — ye **Amazon ki naming** hai, matlab ye Amazon ka passthrough hai

**(2) Postcode resolve karna — teen case handle karne padenge:**

```
Trader ne diya: SW1A, EC2, XYZ99

SW1A  →  ek match      ✅ resolved
EC2   →  paanch match  ⚠️ AMBIGUOUS — poochna padega, pehla nahi utha sakte
XYZ99 →  koi match nahi ❌ UNRESOLVED — batana padega, chupchap drop nahi
```

**(3) Custom radius:** `POST /strategies/locations/{market}/` — address + number + unit (km/miles) → **naya location ID** milta hai.

**Samajhne ki baat:** radius ek alag targeting mode **nahi** hai — wo ID **banane** ka tareeka hai. ID banne ke baad wo normal ID ki tarah `location_include` me jaati hai.

**(4) Include + exclude:**

```
StrategyLocation           include: [StrategyTargetLocation]  exclude: [...]
UpdateStrategyLocation     include: [str]  exclude: [str]     ← POST me sirf IDs
StrategyTargetLocation     amz_id · name · filter_type · market · category
StrategyLocationSummary    market · filter_type · count
```

To pehle jo flat `locations` list thi, wo ab **`location_include` + `location_exclude`** ban gayi.

### Device types — David ka comment

```
CONNECTED_TV   ← streaming_tv ke liye REQUIRED
DESKTOP        ← optional
MOBILE         ← optional
Default        ← ya ALL ya sirf CONNECTED_TV
```

🔴 **`TABLET` value exist NAHI karti.** Document me tablet likha tha — galat.

### Mobile OS — David ka comment

**Pehle likha:** `mobile_environment` = in-app ya mobile_web.
**Asli:** values `IOS` aur `ANDROID` hain.

**Ye do bilkul alag sawaal hain:**
```
environment  →  ad KAHAN dikha (app me ya browser me)
OS           →  KAUN SA operating system
```

Isliye field ka naam **`mobile_operating_systems`** kar diya.

**Aur ek rule:** ye field **sirf tab matter karta hai jab MOBILE device me ho.** MOBILE ke bina ye set karna **validation error** hai, chupchap ignore nahi.

### Content rating, category nahi

API field ka naam `content_rating_exclusions` hai. Document me "content category" likha tha.

```
Content RATING     umar / suitability — 18+, PG
Content CATEGORY   subject — news, sports, gambling
```

**Do alag brand-safety control hain.** Ye **D51** hai.

### 🔴 user_location_signal — naya concept, samajh nahi aaya

Strategy record pe mila: `user_location_signal: "CURRENT"`

Kisi document me nahi hai. **Andaaza:** banda **abhi kahan hai** ya uska **ghar kahan hai** — kis pe target karna. Values pata nahi. **D48** — build mat karo jab tak confirm na ho.

---

## Step 6 — Forecast (Predict Reach)

**Reach curve** — budget badhao to reach kitna badhega.

### Honesty rule — 3P ke liye

```
Amazon inventory  →  reach, frequency, reach curve sab milega
3P inventory      →  sirf CPM aur impressions. Reach NAHI.
                     Agent ko BOLNA padega ki reach available nahi
```

**Kabhi bhi reach number invent nahi karna.**

### 🔴 Repair loop — bid lever wapas aaya

**Pehle likha:** *"CTV CPM fixed hote hain, bid ka lever nahi"*. **92% inventory pe galat.**

**Teen lever, kam se zyada nuksaan ke order me:**

| Order | Lever | Trader kya khota hai |
|---|---|---|
| 1 | **Bid badhao** (floor-rate deals pe) | Kuch nahi — sirf per-impression daam badha |
| 2 | Audience widen karo | Precision |
| 3 | Inventory widen / targeting dheela | Plan ka shape jo usne bola tha |

**Bid sabse kam invasive hai** — aur pehle usko last rakha tha, ulta.

### 🔴 Koi guarantee nahi

**369 deals me EK BHI PG nahi.** PG hi guaranteed delivery deta hai. To:

- Har impression figure **estimate** hai, wada nahi — aur agent ko **inhi shabdon me** bolna hai
- Honesty rule sirf 3P reach ka nahi — **poore plan ke impressions ka** hai
- Trader ne "435,000 impressions" ko milne wala number samjha = hum ne chup rehke dhoka diya

### Zero CPM guard

Do deals ka CPM zero hai (FIFA 2026 ZA). `budget / CPM` = divide by zero. **Explicit guard chahiye, comment nahi.**

---

## Step 7 — Finalise Plan

Pehle "manager approval" tha. **Ab sirf status change hai** — `DRAFT` → `FINALISED`, trader khud karta hai, usi conversation me.

**Isse kya hata:** notification, kisi aur ka intezaar, rejection ka rasta, threshold rule, roles. Aur LangGraph ka `interrupt()` bhi hata.

**Creative approval ka interrupt REHTA hai** — kyunki wahan Amazon/publisher ka wait hai, jo asli me external hai. **Colleague ka wait ≠ platform ka review.** Ye farak yaad rakho.

---

## Step 8 — Asli Strategy banana

### 🔴 D5 answered — teen endpoint, aur pehla galat tha

| Endpoint | Fields | Required | Ye asli me kya hai |
|---|---|---|---|
| `POST /simple-strategies/` | 9 | 4 | **Minimal shell.** `market` aur `format` **singular**. Multi-market nahi ho sakta |
| `POST /automated-strategies/` | 18 | 6 | **Poora planning payload** |
| `POST /strategies/` | — | 6 | Product ka wizard yahi use karta hai |

**Pehle likha tha:** `simple-strategies` = "CTV variant". **Wo naam dekh ke andaaza tha, aur galat tha.**

```
simple-strategies:
  * name · flight_dates · market (SINGULAR) · format (SINGULAR)
    budget · impression_target · id · is_archived · is_readonly

automated-strategies:
  * name · flight_dates · markets_info[] · primary_currency ·
    product_location · formats_and_kpis[]
    goals[] (ARRAY!) · market_deals[] · assets[] · conversion_types[] ·
    asin_numbers · draft_id · pre_approved_creatives · third_party_creatives
```

**Recommendation: `automated-strategies` use karo.** Teen wajah:

1. Sirf yahi poora plan carry kar sakta hai — deals, assets, conversions, per-market budget
2. Iska **KPI set already 5 pe restricted hai** — matlab ye endpoint automated case ke liye **banaya** gaya tha
3. `goals` **array** hai — ek se zyada objective express ho sakta hai

**Aur strategy record khud batata hai kaunse endpoint se bana:**

```
is_simple:    false
is_automated: false     ← test strategy wizard se bani thi
```

To create ke baad agent **confirm** kar sakta hai ki uska route liya gaya.

### 🔴 Automated ka KPI set — 5 values (D12 ka aadha jawab)

```
REACH · FREQUENCY · COST_PER_ACTION ·
RETURN_ON_AD_SPEND · TOTAL_RETURN_ON_AD_SPEND
```

Aur ye goals se map karte hain:
```
REACH, FREQUENCY                              →  Awareness
COST_PER_ACTION, ROAS, TOTAL_ROAS             →  Conversion
```

**Platform ne wo restriction pehle se kar rakhi hai** jo hum poochh rahe the.

---

## Step 9 — Creative upload

CTV me hamesha **video**. Display creative nahi.

**Click-through URL OPTIONAL hai** — TV pe remote se click nahi hota. Par agar device types me MOBILE ya DESKTOP hai, tab click ho sakta hai — to wahan recommend karo, require nahi.

**CTV me call-to-action kaise:** QR code creative me, ya "search for Nike" bolna, ya bas brand recall.

**Duration match check:** plan me 15s tha aur 30s video upload hua → economics badal gayi (CPM alag, impressions alag) → **re-approval chahiye**.

---

## Step 10 — Platform creative approval

Amazon/publisher review karta hai. **Per channel** status:

```
Prime Video  → APPROVED
Channel 4    → PENDING
Netflix      → REJECTED
```

Yahan LangGraph `interrupt()` **sahi** hai — asli external wait hai.

---

## Step 11 — Tracking

```
Amazon pe bechte ho?     →  ASIN chahiye  →  asin-validation API
Apni website pe?         →  AD TAG chahiye →  tag pehle lagana padega
                            (tag lagne ke BAAD ki activity hi track hoti hai)
```

### 🔴 Conversion events — 6 hain aur market ke hisab se alag

| Event | GB | US |
|---|---|---|
| `ADD_TO_SHOPPING_CART` | ✅ | ✅ |
| `APPLICATION` | ✅ | ✅ |
| `CHECKOUT` | ✅ | — |
| `PAGE_VIEW` | ✅ | — |
| `SEARCH` | — | ✅ |
| `OTHER` | — | ✅ |

**Document me 4 likhe the aur universal maane the.** `SEARCH` aur `OTHER` naye hain, aur `CHECKOUT`/`PAGE_VIEW` GB-only nikle.

**Matlab:** market-agnostic list dikhane se aise events offer honge jo us market me hain hi nahi. Aur market badle to selection **dobara check** karni padegi.

**Aur endpoint:** `?selected_advertiser_id=` **required** hai, warna 400.

---

## Step 12 — Credit check

`Balance >= budget`? Nahi to activate nahi.

---

## Step 13 — Activate (ek hi spend action)

**Isse pehle sab kuch free tha.** Ye **join node** hai — creative, tracking, credit teeno kisi bhi order me ho sakte hain, yahan **completeness check** hoti hai.

| Prerequisite | Kab pass |
|---|---|
| Creative uploaded | Plan ki har duration ke liye ek |
| Creative approved | Har matched channel ne APPROVED bola |
| Ad tag | Amazon pe nahi bechte to tag laga ho |
| ASINs | Amazon pe bechte to ASIN validated ho |
| Conversions | Chune ya explicitly skip kiye |
| Credit | Balance >= budget |
| **Spend quantity** | **Budget ho ya impression target — allocation_mode ke hisab se** |

🔴 **`POST /strategies/{id}/activate/` exist nahi karta.** Activation `POST /strategies/{id}/set_status/` se hoti hai.

**Status ke 6 values, 3 confirmed:**
```
1_delivering · 2_out_of_budget · 3_ended · 4_not_running ·
5_ready_to_deliver · 6_inactive
```

**Number sirf sort order ke liye hai, state machine nahi.** `4_not_running` se `1_delivering` ja sakta hai — ye **assumption** hai, confirm nahi.

Activation ke baad VOW ka sync Amazon DSP pe Campaign + Ad Group banata hai.

---
---

# PART 5 — Do blockers (ye sabse zaroori hai yaad rakhna)

## 🔴 D47 — advertiser defaults ka endpoint 403 deta hai

**Paanch admin endpoints trader ke valid session ko mana kar dete hain:**

```
403  GET /api/admin/advertiser/                                    list
403  GET /api/admin/advertiser/{id}/                               ← DEFAULTS
403  GET /api/admin/advertiser/get_channels_choices/               channel list
403  GET /api/admin/advertiser/get_deal_exchange_choices/          exchange list
403  GET /api/admin/advertiser/get_industry_and_sub_industry_choices/
```

**Dusra wala poore "advertiser defaults" concept ka base hai** — frequency cap, device types, product categories, selling location. David ka comment tha ki ye **poochho nahi, padho**. **Agent padh hi nahi sakta.**

**Teesra wala** wo endpoint hai jahan se channel list aani thi hard-code ke bajaye. Wo bhi band hai — to channel deal ke naam se hi nikalna padega, wahi problem.

**Do possibility:**
1. Agent ko **service account** chahiye admin scope ke saath
2. Defaults kisi **non-admin** endpoint pe hain jo hum ne dhoonda nahi

**Ye Wajahat/David se poochna hai. Jab tak jawab na aaye, saare advertiser-default fields implement nahi ho sakte.**

## 🔴 D50 — 15 fields ki poori layer specify nahi hui

Strategy read model me **40 keys** hain. Document me 20 the.

| Field | Value mila | Kya lagta hai |
|---|---|---|
| `is_simple` / `is_automated` | false / false | Kaunse endpoint se bani |
| `impression_target` | null | ✅ Budget ke bajaye impressions pe plan ho sakta hai |
| `allocation_mode` | "BUDGET" | Budget ya impressions |
| `creative_duration_allocation_mode` | "budget" | 🔴 **lowercase!** Upar wala uppercase |
| `creative_durations` | [] | Durations strategy pe store hoti hain |
| `creative_rotation_type` | "RANDOM" | Creative rotation |
| `content_rating_exclusions` | [] | Brand safety — rating |
| `user_location_signal` | "CURRENT" | 🔴 Naya concept |
| `audiences_cpm` | null | Audience fee strategy pe store |
| `planned_cpm` · `cpm_target` · `pacing_ratio` | null | Delivery economics |
| `can_be_extended` | true | Flight extend ho sakti hai |
| `kpis` | — | **Plural** |

**Sawaal:** `pacing_ratio`, `planned_cpm`, `cpm_target`, `allocation_mode`, `creative_rotation_type` — **agent set karega ya platform?**

- Agent karega → plan model me aur conversation me hone chahiye
- Platform karega → schema me read-only hone chahiye

**Abhi dono me nahi hain. To kuch to missing hai, chahe jawab kuch bhi ho.**

---
---

# PART 6 — Calling quirks (implementation me kaam aayenge)

## Required params jo obvious nahi hain

```
/inventory-sources/            goal AND strategy_formats AND markets — teeno
/strategies/locations/{m}/     query, minimum 2 characters
/conversions/definitions/      selected_advertiser_id
```

Teeno bina param **400** dete hain, default nahi.

## Pagination galat scheme pe aati hai

DRF ka `next` link **`http://`** pe aata hai, phir server **301** karke https pe bhejta hai.

**Do nuksaan:** har page pe ek extra redirect, aur **session cookie plaintext hop pe** chali jaati hai.

**Fix:** link follow karne se pehle scheme rewrite karo.

## Advertiser header har call pe chahiye

`Vowmade-Advertiser-Id` — bina iske response **khaali** aata hai, **error nahi**. Ye silent failure hai, sabse khatarnak type.

## UI ke count API ke count nahi hain

**Document ke SAARE count UI ke filtered view se aaye the aur SAARE kam the:**

| Cheez | Likha tha | Asli |
|---|---|---|
| Deals | 83 | **369** |
| Audience sets | 15 | **35** |
| Assets | 4 | **58** |
| Markets with deals | 2 | **18** |
| Product categories | ginа nahi | **25,973** |

**Sabak:** UI pe jo dikhe usko total mat maano. API se ginо.

---
---

# PART 7 — 11 cheezein jo GALAT thi (meeting ke liye ratna)

Ye table hi mastery hai. Koi puche "kya badla" — ye bolna.

| # | Kahan | Document ne bola tha | Asli sach | Kaise pata chala |
|---|---|---|---|---|
| 1 | Step 1 | Currency market se derive hoti hai | **Advertiser** se aati hai | Market chunne se pehle EUR bhara tha; live strategy me NOK + US market |
| 2 | Step 1 | `goal` FIXED hai CTV ke liye | **Defaulted** hai, aur enum me 15 values | David ka comment + `/choices/` |
| 3 | Step 1 | `kpi_target_value`, integer | **`target_kpi`, string** | Spec padha. 4.5 ROAS int me 4 ban jata |
| 4 | Step 1 | `product_categories: List[int]` | `List[str]`, aur GB me 25,973 | API response |
| 5 | Step 1 | 4 format, 6 KPI, 4 duration, 2 market | **21, 16, 7, 21** | `/strategies/choices/` |
| 6 | Step 2 | Deal pe `channel` aur `inventory_tier` hai | **Dono field exist nahi** | 369 deals ke saare fields check kiye |
| 7 | Step 2 | 83 deals, 1 zero-priced | **369 deals, 2** zero-priced | Bina filter query |
| 8 | Step 4 | Audience fee `/contextual-targeting/fees` se | **Do alag fee.** Audience fee audience set pe | Dono endpoint dekhe |
| 9 | Step 6 | CTV CPM fixed, bid lever nahi | **92% floor-rate.** Bid sabse kam invasive repair | 369 deals ka price_type ginа |
| 10 | Step 8 | `simple-strategies` CTV endpoint hai | Minimal shell hai. **`automated-strategies`** sahi hai | Teeno request schema padhe |
| 11 | Step 11 | 4 conversion event, universal | **6 event, market-specific** | Per-market call |

**Ek pattern dekho:** galtiyon me se 5 ka ek hi karan hai — **UI ka filtered view poora set samajh liya**. Ye sabse bada sabak hai.

---
---

# PART 8 — Saare open questions (D47–D54 + purane)

## Do blocker

| # | Sawaal | Kyun block |
|---|---|---|
| **D47** | `/admin/advertiser/{id}/` 403 deta hai — service account chahiye ya koi dusra endpoint hai? | Poora advertiser-defaults concept isi pe khada hai |
| **D50** | `pacing_ratio`, `planned_cpm`, `cpm_target`, `allocation_mode`, `creative_rotation_type` — agent set karega ya platform? | Abhi na plan model me hain na read-only marked |

## Chhe jo schema lock hone se pehle chahiye

| # | Sawaal | Context |
|---|---|---|
| **D48** | `user_location_signal` kya hai, values kya? (`CURRENT` mila) | Kisi document me nahi |
| **D49** | Audience fee + contextual fee **add** hoti hain? | GB stv pe 1.63 + 0.450 = 2.08 GBP |
| **D51** | `content_rating_exclusions` — rating ya category? | Do alag brand-safety control |
| **D52** | `format` enum me channel hain — "Prime Video channel hai" ke saath kaise reconcile? | Domain sahi, API alag |
| **D53** | Deal object pe **controlled `channel` field** mil sakta hai? | 8 naming convention, `Tubi` vs `TUBI` |
| **D54** | "50+ inventory" kis cheez ka count tha? | Sources sirf 4 hain |

## Char data-quality request

1. **Deal pe `channel` field** (D53) — sabse zyada faayda isi se
2. **`genre` populate karo** — field hai, null hai, naam me genre likha hai
3. **Deal naam ki casing fix** — `Tubi` aur `TUBI` ek hi channel
4. **Do zero-priced deals confirm karo** — divide by zero

## Jo BAND ho gaye (ye bhi yaad rakho)

| # | Sawaal | Jawab |
|---|---|---|
| **D5** | Kaunsa create endpoint | `automated-strategies` — 18 fields, KPI 5 pe restricted, `is_automated` flag saboot |
| **D12** | Goal-to-KPI mapping | Aadha — automated ka KPI set 5 values hai |
| **D31** | Currency enum extend karna padega? | Nahi — 19 already hain, NOK sameth |
| **D38** | Impression target support hai? | Haan — `impression_target` field hai |
| **D4** | Deal matching fields | **Blocked confirmed** — channel/tier nahi hain |
| **Comment 31/32/34** | Location search/exclude/radius | Sab confirmed, API support karta hai |

---
---

# PART 9 — Rapid fire (koi kuch bhi pooche)

## Numbers

| Sawaal | Jawab |
|---|---|
| Kitne deals? | **369** (GB + streaming_tv = 62) |
| Kitne audience sets? | **35** |
| Kitne assets? | **58** |
| Kitne product categories? | **25,973** (GB) |
| Kitne market enum me? | **21** (18 me live deals) |
| Kitne inventory sources? | **4** total, CTV ke liye **2** |
| goal enum? | **15** |
| format enum? | **21** (12 channel hain) |
| KPI enum? | **16** (automated me **5**) |
| currency enum? | **19** |
| conversion events? | **6**, market-specific |
| durations? | **7** |
| Deal currencies? | **8** (USD 156 sabse zyada, GBP sirf 35) |
| Floor-rate deals? | **341 = 92%** |
| PG deals? | **ZERO** |
| Zero-priced deals? | **2** (FIFA 2026 ZA) |
| Strategy read model me keys? | **40** |
| Deal naam ke conventions? | **8** |
| Fees markets? | **16** markets × 3 rates |
| GB audience video fee? | **1.63 GBP** |
| GB contextual stv fee? | **0.450 GBP** |
| OpenAPI paths? | **192** paths, **197** definitions |

## Concepts

**Q: Reach aur impressions me farak?**
Reach = kitne LOG. Impressions = kitni BAAR. `Impressions = Reach × Frequency`.

**Q: CPM ka formula?**
`Impressions = (Budget ÷ CPM) × 1000`

**Q: Floor rate aur fixed CPM me farak?**
Floor = minimum, upar ja sakta hai, bid matter karta hai. Fixed = wahi daam. **92% floor hai.**

**Q: Teen deal types?**
PG (guaranteed, budget committed, 0 hain), Preferred (first look, fixed price, 28), Private Auction (invited auction, floor price, 341).

**Q: Auction kya hai?**
Ad slot khaali hone pe milliseconds me 50 advertisers bid lagate hain, sabse zyada wala jeetta hai.

**Q: Effective CPM?**
Deal CPM + audience fee. `22.96 + 1.63 = 24.59`. Ye asli daam hai, deal CPM nahi.

**Q: Endemic vs non-endemic?**
Endemic = Amazon pe bikta, ASIN se track. Non-endemic = apni site, ad tag se track.

**Q: Frequency cap kis period ka?**
**Per WEEK.**

**Q: Teen inventory tier?**
Amazon owned (Prime Video, reach milega), 3P pre-curated (Netflix, reach nahi), 3P needs curation (Disney+, deal baad me banega).

## Design decisions

**Q: Char principles?**
Zero Hallucination, Self-Filling Form, API-Driven, **Stated Uncertainty**.

**Q: Chautha principle kyun add hua?**
Kyunki deal pe channel field nahi hai — naam parse karna padta hai. Parsed value guess hai, aur guess ko fact dikhana jhooth hai.

**Q: Zero Hallucination ke kitne hisse hain?**
**Teen.** (1) Invent mat karo (2) **Hamesha verify karo — user ki boli hui value bhi** (3) Chupchap fix mat karo.

**Q: User ne value bol di, to verify karna zaroori hai?**
**Haan, bilkul.** User ne bola iska matlab wo sahi hai — aisa nahi hai. Naam bola to uniqueness check karo. Netflix bola to deal hai ki nahi dekho. TABLET bola to batao ki wo value exist nahi karti.

**Q: Naam already exist kare to?**
**Batao aur alternative do.** "-2" lagakar aage badhna galat hai — trader ne jaan-boojh ke wo naming chuni ho sakti hai.

**Q: Ambiguous postcode pe kya?**
**Poochho.** `geoLocations[0]` uthana sabse aam galti hai — plan chal jayega, par galat jagah pe.

**Q: Validation kab hoti hai — confirm se pehle ya baad?**
**Pehle.** Warna trader aisi cheez pe haan bol dega jo ban hi nahi sakti, aur agent ko apna "samajh gaya" wapas lena padega.

**Q: Char cheezein jo "chupchap fix" me aati hain?**
Naam pe "-2", TABLET drop, ambiguous ka pehla match, channel parse fail pe ROS maan lena. **Chaaron me plan chal jayega — isi liye khatarnak hain.**

**Q: `UNVERIFIABLE` aur `VALID` me farak?**
Bada farak. Frequency cap check nahi kar sakte (403) aur channel check nahi kar sakte (field nahi) — inko pass mat maano. Plan ko farak pata hona chahiye.

**Q: Char value categories?**
CONSTANT (formats), DEFAULTED (location), DEFAULTED-ADVISED (goal — agent bolta hai), LOCKED (advertiser ne lock kiya).

**Q: "Source" column kyun add hua?**
*"Required hai"* aur *"poochna padega"* do alag baatein hain. Currency required hai, par kabhi poochte nahi.

**Q: Audience ke teen profile me daam ka farak?**
**Koi nahi.** Fee data provider pe depend karti hai, profile pe nahi. Reach aur precision me farak hai.

**Q: Fee ke teen rule?**
Trigger (1P data use ho), No-compound (ek provider se 1 ya 50 segment, fee same), Stacking (do provider = do fee).

**Q: Repair loop ke teen lever, order me?**
1. Bid badhao (kuch nahi khota) 2. Audience widen (precision) 3. Inventory/targeting dheela (plan ka shape).

**Q: Deals matched hain ya selected?**
**Matched.** Trader channel batata hai, agent deal dhoondhta hai. Deal ID trader ka kaam nahi.

**Q: Audience zaroori hai?**
**Nahi.** Trader teeno mana kar sakta hai. Bina audience full inventory pe chalega, koi audience fee nahi.

**Q: Click-through URL required hai?**
CTV pe **nahi** — remote se click nahi hota. MOBILE/DESKTOP ho to recommend karo.

**Q: Approval kaha gaya?**
Plan approval hata — ab sirf `DRAFT → FINALISED` status change, trader khud. **Creative** approval raha, kyunki wahan Amazon ka asli wait hai.

## API

**Q: Create ke liye kaunsa endpoint?**
**`POST /api/automated-strategies/`** — 18 fields, 6 required.

**Q: `simple-strategies` kyun nahi?**
`market` aur `format` **singular** hain. Multi-market/multi-format nahi ho sakta. Wo minimal shell hai.

**Q: Kaunse endpoint exist nahi karte?**
`/rate-cards/match/`, `/advertisers/{id}/defaults/`, `/strategies/{id}/activate/`.

**Q: Activation kaise?**
`POST /api/strategies/{id}/set_status/`

**Q: Enums kahan se?**
`GET /api/strategies/choices/` — document ka sabse kaam ka endpoint.

**Q: Kaun se endpoint required params maangte hain?**
`/inventory-sources/` (goal + formats + markets), `/strategies/locations/{m}/` (query, 2 char), `/conversions/definitions/` (selected_advertiser_id).

**Q: Pagination ka issue?**
`next` link `http://` pe aata hai, 301 hota hai, cookie plaintext hop pe jaati hai. Scheme rewrite karo.

**Q: Kaun se endpoint 403 dete hain?**
Saare 5 `/admin/advertiser/` wale — including advertiser defaults.

## Location

**Q: Location free text hai?**
**Nahi.** Opaque Amazon ID — `XHvCjcKHXsKGemnCjsKQbMKX`. Number bhi nahi.

**Q: Search kaise?**
`GET /strategies/locations/GB/?query=SW1` — minimum 2 character.

**Q: Postcode list ka kya?**
Ek-ek resolve karo. Teen case: resolved, **ambiguous (poochna hai, pehla nahi uthana)**, unresolved (batana hai).

**Q: Custom radius?**
`POST /strategies/locations/{market}/` — address + number + km/miles → naya ID. Radius alag mode nahi, ID banane ka tareeka hai.

**Q: Exclude support hai?**
Haan — `location_include` aur `location_exclude`, dono ID list.

## Devices

**Q: streaming_tv ke liye kaunsa device required?**
**`CONNECTED_TV`.** DESKTOP/MOBILE optional.

**Q: TABLET?**
**Exist nahi karta.**

**Q: `mobile_environment` kya hai?**
Wo naam galat tha. Field `mobile_operating_systems` hai, values `IOS`/`ANDROID`, aur **sirf tab relevant jab MOBILE device me ho**.

---
---
---

# PART 10 — Agentic Way: LangGraph Nodes

*(Ab is document ki sari cheezon se nodes ka design)*

## 10.1 Sochne ka tareeka

Ek node ka **ek kaam** hona chahiye. Agar ek node "extract karta hai AUR poochta hai AUR API call karta hai" — wo teen node hone chahiye. Kyun:

- Test karna asaan
- Fail hone pe pata chalta hai kahan
- LangGraph checkpoint per-node hota hai, to resume clean hota hai

**Aur ek rule:** **node decide nahi karta ki aage kahan jaana hai — gate karta hai.** Node kaam karta hai aur state update karta hai. Routing alag function me.

## 10.2 Saare nodes — 7 phase me

### PHASE A — Samajhna (conversation)

| # | Node | Kaam | Input | Output | Status |
|---|---|---|---|---|---|
| A1 | `classify_intent` | Message ka type — brief / selection / question / greeting / correction / out_of_scope | user message | `intent`, `selection` | ✅ **Ban gaya** |
| A2 | `load_session_context` | Session start pe advertiser defaults + enums + credit padho | advertiser_id | `advertiser_defaults`, `choices`, `credit` | 🔴 **D47 se BLOCKED** |
| A3 | `extract_fields` | Brief se slots bharo | message | 15+ slots | ✅ **Ban gaya** (fix chahiye) |
| A4 | `resolve_dates` | "September" → flight_dates. Past date, weird range handle karo | text | `flight_dates` | ⬜ Banana hai |
| A5 | `resolve_locations` | Postcode/city → Amazon IDs. Ambiguous pe poochho | location text | `location_include/exclude` | ⬜ **Naya — David ke comment se** |
| **A5.5** | **`validate_slots`** | **Har slot apni authority se check karo — user ki boli hui value bhi** | filled slots | `validated_slots`, errors, ambiguous | ⬜ **Naya — Zero Hallucination ka hissa 2. PEHLA banana hai** |
| A6 | `confirm_understanding` | "Maine ye samjha — sahi hai?" | **validated** slots | message | ⚠️ Fix chahiye |
| A7 | `ask_missing` | Ek waqt me EK sawaal | `awaiting` | question | ⬜ Banana hai |
| A8 | `reply_from_registry` | Registry se verbatim phrase | intent | message | ✅ **Ban gaya** |

**A2 ka note (important):** D47 ki wajah se 403 aayega. **Design isko handle karna chahiye** — defaults na mile to agent poochh le, crash na ho. Aur log kare ki defaults nahi mile.

**A5 ka detail** (ye naya hai, David ke comment se):

```
Input: "SW1A, EC2, XYZ99 pe target karo, Manchester ke 10 mile radius me bhi"

1. Text me se location terms nikalo
2. Har term pe:  GET /strategies/locations/GB/?query={term}
3. Result 3 dhero me daalo:
      1 match     →  resolved,   ID le lo
      2+ match    →  ambiguous,  POOCHHO (pehla mat utha lo)
      0 match     →  unresolved, BATAO (chupchap drop mat karo)
4. "10 mile radius" dikhe to:
      POST /strategies/locations/GB/  {address, radius: 10, unit: "miles"}
      →  naya ID
5. Saare ID location_include me
```

### 🔴 A5.5 — `validate_slots` (sabse zaroori naya node)

**Ye node Zero Hallucination ke dusre hisse ka enforcement hai.** Iske bina baaki sab bekaar hai, kyunki galat value poore flow me neeche tak chali jayegi aur create time pe fail hogi.

| Kya | Detail |
|---|---|
| **Kab chalega** | `extract_fields` ke **baad**, `confirm_understanding` se **pehle** |
| **Kaam** | Har bhara hua slot apni authority se check karo |
| **Kyun yahan** | Timing rule — confirm me sirf verified value jaani chahiye |
| **Status** | ⬜ **Naya — aur pehla banana chahiye** |

**Andar kya hota hai:**

```
Har filled slot ke liye:

   1. Authority pata karo    (enum · registry · API · business rule)
   2. Check chalao
   3. Teen me se ek result:

      VALID      →  slot me rehne do, kuch mat bolo
      INVALID    →  validation_errors me daalo + trader ko BATAO
      AMBIGUOUS  →  ambiguous_slots me daalo + POOCHHO

   4. Agar koi INVALID ya AMBIGUOUS hai:
         → confirm_understanding pe NA jao
         → seedha ask_missing pe jao (ye sawaal pehle)
```

**Sirf-enum check (sasta, local, koi API nahi):**
```
formats · goal · currency code · market code · duration ·
device values (TABLET yahan reject hoga) · conversion event ka naam
```

**API check (mehnga — batch karo, parallel karo):**
```
strategy name       →  check_strategy_name_uniqueness/
budget              →  credits/summary/
market me deals     →  deals/?markets=
channel me deals    →  deals/ + naam parse
duration support    →  deals ke ad_lengths
locations           →  locations/{market}/?query=  (har term ek call!)
ASINs               →  asin-validation/
product categories  →  product-categories/
conversion events   →  conversions/definitions/  (market ke saath!)
```

**Cross-field rules (koi API nahi, par sabse zyada bugs yahan):**
```
1. streaming_tv hai   →  CONNECTED_TV zaroori
2. mobile_os set hai  →  MOBILE device me hona chahiye
3. budget + impression_target dono  →  allocation_mode chahiye
4. KPI                →  jis create endpoint pe ja rahe hain, wahan allowed?
5. target_kpi range   →  KPI ke hisab se (frequency 2-5, ROAS decimal)
6. market badla       →  conversion_types DOBARA validate karo
7. deal currency ≠ plan currency  →  flag karo, chupchap convert nahi
```

**Sabse zaroori: kya NAHI karna**

```
❌ Naam clash pe "-2" lagana
❌ TABLET ko chupchap hata dena
❌ Ambiguous postcode ka pehla utha lena
❌ Channel parse fail hone pe ROS ya Prime Video maan lena
❌ Invalid conversion event chupchap drop karna
```

**Ye char kaam karne se plan chal jayega — aur trader ko galat baat pata hogi. Isi liye ye node ka pura point hai.**

**Output state me:**
```
validated_slots        {field: VALID | INVALID | AMBIGUOUS | UNVERIFIABLE}
validation_errors      [{field, submitted, reason, available_options}]
ambiguous_slots        [{field, submitted, candidates}]
unverifiable_slots     [field]   ← D47/D53 wale, authority hi nahi hai
```

🔴 **`UNVERIFIABLE` ek alag result hai, `VALID` nahi.** Frequency cap check nahi kar sakte (403) aur channel check nahi kar sakte (field nahi hai) — inko "pass" mat maano. Plan ko farak pata hona chahiye.

### PHASE B — Inventory

| # | Node | Kaam | Status |
|---|---|---|---|
| B1 | `match_inventory_deals` | Deals dhoondho market + duration + channel se | ⚠️ Rename + fix (`select_inventory` tha) |
| B2 | `derive_channel_tier` | Deal naam parse karke channel + tier + **confidence** | ⬜ **Naya — kyunki field nahi hai** |
| B3 | `normalise_deal_currency` | 8 currency ko ek me lao | ⬜ **Naya — 9% error se bachne ke liye** |
| B4 | `capture_curation` | 3P-needs-curation ke liye requirement record karo | ⬜ Banana hai |

**B1 ka detail:**

```
1. GET /deals/?markets=GB&formats=streaming_tv,prime_video,UNKNOWN&markets=GB,ZZ
      ↑ padding zaroori — bina iske 21 deals kam milte hain
2. ad_lengths filter karo plan ki duration se
3. B2 se channel derive karo
4. Trader ka channel match karo
5. Kuch nahi mila? Widen karo, ya poochho
```

**B2 ka detail — 8 convention:**

```
pipe-form   →  "|" se split, pehla part = channel      → PARSED_CONFIDENT
3PS_        →  "_" se split, aakhri part = channel     → PARSED_CONFIDENT
VowMade_    →  channel dhundhna mushkil                → PARSED_GUESS
EB / Tubi / TUBI / 62797 / APC  →  case-insensitive
                                    known channel list se match → PARSED_GUESS
kuch nahi mila                                          → UNKNOWN

Phir channel → tier:
   Prime Video, Twitch          →  AMAZON_OWNED
   Netflix, Hulu, Paramount...  →  THIRD_PARTY_PRECURATED
   Disney+                      →  THIRD_PARTY_NEEDS_CURATION
   UNKNOWN                      →  tier bhi UNKNOWN, aur BOLNA hai
```

🔴 **`channel_confidence` ko UI tak pahunchana hai.** `PARSED_GUESS` wale deal ko fact ki tarah nahi dikhana.

**B3 ka detail:**

```
Plan currency EUR, deal currency USD
   → Kis rate pe convert? Rate kahan se?  ← ye khud ek open question hai
   → Jab tak clear na ho: BOLO ki currency alag hai, chupchap convert mat karo
```

### PHASE C — Audience

| # | Node | Kaam | Status |
|---|---|---|---|
| C1 | `suggest_audiences` | Teen option — Narrow/Balanced/Wide | ✅ **Ban gaya** (fee bug fix ho gaya) |
| C2 | `apply_audience` | Trader ki choice lagao. Mana kiya to bhi aage badho | ✅ **Ban gaya** |
| C3 | `compute_effective_cpm` | Deal CPM + audience fee + contextual fee | ⬜ **Naya — do fee wali baat se** |

**C3 ka detail:**

```
base            = deal CPM (ek currency me!)          22.96
+ audience fee  = audience set ka video_fee            1.63
+ contextual fee = product-category targeting hai to?  0.450   ← D49, confirm nahi
─────────────────────────────────────────────────────────────
effective CPM

D49 answer na ho, tab tak:
   dono alag dikhao, add karke ek number mat do
   aur bolo ki dono ka interaction confirm nahi hai
```

### PHASE D — Targeting

| # | Node | Kaam | Status |
|---|---|---|---|
| D1 | `apply_targeting_defaults` | Market se location default, CONNECTED_TV set karo | ⬜ Banana hai |
| D2 | `validate_targeting` | Device/mobile-OS rule check | ⬜ **Naya — David ke comment se** |

**D2 ke rules:**

```
1. streaming_tv hai to CONNECTED_TV zaroori     → nahi hai to error
2. mobile_operating_systems set hai par MOBILE nahi  → ERROR (silent ignore NAHI)
3. TABLET aaya                                  → error, ye value nahi hai
4. location_include bhara                       → market default replace ho gaya, batao
5. user_location_signal                          → mat set karo, D48 pending
```

### PHASE E — Forecast + repair

| # | Node | Kaam | Status |
|---|---|---|---|
| E1 | `predict_reach` | Forecast API | ⚠️ Fix chahiye (hardcoded values) |
| E2 | `assess_forecast` | Kaafi hai ya nahi? Kya missing hai? | ⬜ Banana hai |
| E3 | `repair_plan` | Teen lever, **order me** | ⬜ **Naya — bid lever wapas aaya** |
| E4 | `state_uncertainty` | Kya fact, kya estimate, kya guess | ⬜ **Naya — chauthe principle se** |

**E3 ka order (ye bahut important hai):**

```
Lever 1  BID BADHAO
         Sirf FLOOR_RATE deals pe (92% hain)
         Trader kuch nahi khota — bas per-impression daam badha
         Isko PEHLE try karo

Lever 2  AUDIENCE WIDEN
         Precision jaati hai
         Trader ko batao kya kho raha hai

Lever 3  INVENTORY / TARGETING DHEELA
         Plan ka shape badalta hai jo trader ne bola tha
         Ye LAST option, aur poochh kar
```

**E4 ka detail** — har number ke saath uska source:

```
FACT       "Prime Video UK ROS CPM: £22.96"            deal API se
FACT       "Audience fee: £1.63"                        audience set se
ESTIMATE   "~406,000 impressions"                       hisaab, aur KOI PG DEAL NAHI
                                                        → guarantee nahi
ESTIMATE   "Reach ~145,000"                             forecast API, Amazon portion
MISSING    "Channel 4 ka reach nahi mil sakta — 3P"     honest
GUESS      "Ye deal Tubi ka LAGTA hai (naam se)"        PARSED_GUESS
```

### PHASE F — Finalise + create

| # | Node | Kaam | Status |
|---|---|---|---|
| F1 | `render_strategy_card` | Executable Strategy card | ⬜ Banana hai |
| F2 | `finalise_plan` | DRAFT → FINALISED | ⬜ Banana hai |
| F3 | `build_create_payload` | `automated-strategies` ka shape banao | ⬜ **Naya — D5 answered** |
| F4 | `create_strategy` | POST | ⬜ Banana hai |
| F5 | `verify_creation` | `is_automated` check karo | ⬜ **Naya** |

**F3 ka mapping** (plan → payload — shape badalta hai, dhyan se):

```
plan.markets        →  markets_info: [{market, budget, currency, base_bid}]
plan.formats + kpi  →  formats_and_kpis: [{format, kpi, target_kpi}]
plan.goal           →  goals: ["AWARENESS"]        ← ARRAY hai!
plan.selected_deals →  market_deals: [{market, deal_ids}]
plan.creatives      →  assets: [...]
plan.conversions    →  conversion_types: [...]     ← market ke hisab se filtered!
plan.asins          →  asin_numbers: "..."
plan.currency       →  primary_currency            ← advertiser se, market se NAHI
```

**F5 kyun:** `is_automated: true` aana chahiye. `false` aaya to agent ka route nahi liya gaya — bug hai.

### PHASE G — Post-create (M2, baad me)

| # | Node | Status |
|---|---|---|
| G1 | `upload_creative` | ⬜ |
| G2 | `poll_creative_approval` | ⬜ `interrupt()` yahan **sahi** hai |
| G3 | `setup_tracking` | ⬜ Conversion **market-filtered** |
| G4 | `check_credit` | ⬜ |
| G5 | `activation_gate` | ⬜ Join node — 7 prerequisite |
| G6 | `activate` | ⬜ `set_status/` |

## 10.3 Graph ka shape

```
                        START
                          │
                 ┌────────▼────────┐
                 │ classify_intent │
                 └────────┬────────┘
        ┌─────────────────┼─────────────────┬──────────────┐
        │                 │                 │              │
     BRIEF           SELECTION          QUESTION      GREETING/
        │                 │                 │        OUT_OF_SCOPE
        ▼                 ▼                 ▼              ▼
  extract_fields   apply_audience   reply_from_registry ──┘
        │                 │                                │
   ┌────▼────┐            │                              END
   │resolve_ │            │
   │dates    │            │
   └────┬────┘            │
        │                 │
   ┌────▼──────────┐      │
   │resolve_       │      │
   │locations      │      │
   └────┬──────────┘      │
        │                 │
   ┌────▼──────────┐      │
   │validate_slots │      │  ← har value check, user ki boli hui bhi
   └────┬──────────┘      │
        │                 │
   ┌────▼──────────────┐  │
   │ GATE:             │  │
   │ sab bhara AUR     │  │
   │ sab VALID?        │  │
   └──┬─────────┬──────┘  │
   nahi        haan       │
      │         │         │
 ┌────▼────┐    │         │
 │ask_     │    │         │  ← "ye naam already hai" / "GB me Netflix nahi"
 │missing  │    │         │     / "EC2 ke 5 match, kaunsa?"
 └────┬────┘   │         │
     END       │         │
               ▼         │
      ┌─────────────────┐│
      │confirm_         ││  ← isme sirf VERIFIED value
      │understanding    ││
      └────────┬────────┘│
               ▼         │
      ┌─────────────────┐│
      │match_inventory_ ││
      │deals            ││
      └────────┬────────┘│
               ▼         │
      ┌─────────────────┐│
      │derive_channel_  ││
      │tier             ││
      └────────┬────────┘│
               ▼         │
      ┌─────────────────┐│
      │normalise_deal_  ││
      │currency         ││
      └────────┬────────┘│
               ▼         │
      ┌─────────────────┐│
      │suggest_         ││
      │audiences        ││
      └────────┬────────┘│
               │         │
              END ◄──────┘  (trader ka jawab wait)
                         │
               ┌─────────▼──────┐
               │compute_        │
               │effective_cpm   │
               └────────┬───────┘
                        ▼
               ┌────────────────┐
               │apply_targeting_│
               │defaults        │
               └────────┬───────┘
                        ▼
               ┌────────────────┐
               │validate_       │
               │targeting       │
               └────────┬───────┘
                        ▼
               ┌────────────────┐
               │predict_reach   │
               └────────┬───────┘
                        ▼
               ┌────────────────┐
               │assess_forecast │
               └───┬────────┬───┘
                kaafi    kam hai
                   │        │
                   │   ┌────▼──────┐
                   │   │repair_plan│──┐
                   │   └───────────┘  │
                   │        ▲         │
                   │        └─────────┘ (max 3 baar)
                   ▼
          ┌────────────────┐
          │state_          │
          │uncertainty     │
          └────────┬───────┘
                   ▼
          ┌────────────────┐
          │render_strategy_│
          │card            │
          └────────┬───────┘
                  END
```

## 10.4 State me kya add karna hai

Ab tak jo mila, uske hisab se `PlanningAgentState` me ye naye fields chahiye:

```
# Currency ka jaal
primary_currency          advertiser se, market se NAHI
computation_currency      hisaab kis currency me hua — BATANA hai
deal_currencies           deals me kaun kaun si currency mili

# Channel ka guess
channel_confidence        {deal_id: PARSED_CONFIDENT | PARSED_GUESS | UNKNOWN}
unparsed_deal_names       jinka channel nahi nikla — visible rakhna

# Location
location_include          Amazon IDs
location_exclude          Amazon IDs
ambiguous_locations       [{submitted, candidates}]  ← poochna hai
unresolved_locations      [str]                       ← batana hai

# Do fee
audience_fee              audience set se
contextual_fee            /contextual-targeting/fees se
fee_interaction_known     False  ← D49 pending

# Uncertainty (chautha principle)
facts                     kya API se aaya
estimates                 kya calculate hua
guesses                   kya parse hua
unavailable               kya nahi mil saka aur kyun

# Spend
allocation_mode           BUDGET ya IMPRESSIONS
impression_target         budget ka alternative

# Repair
repair_attempts           kitni baar
repair_levers_used        kaun kaun se lever lagaye

# Blocked
advertiser_defaults_available   False jab 403 aaye  ← D47

# Validation (Zero Hallucination hissa 2)
validated_slots        {field: VALID | INVALID | AMBIGUOUS | UNVERIFIABLE}
validation_errors      [{field, submitted, reason, available_options}]
ambiguous_slots        [{field, submitted, candidates}]  ← poochna hai
unverifiable_slots     [field]  ← authority hi nahi (D47, D53)
name_uniqueness_checked  bool   ← naam check hua ya nahi
```

## 10.5 Build order — kis se shuru karo

**Sabse pehle (ye kal shuru kar sakte ho):**

| Order | Node | Kyun pehle |
|---|---|---|
| **1** | **`validate_slots`** | **Zero Hallucination ka hissa 2. Iske bina har doosra node galat data pe kaam karega.** Enum checks se shuru karo (sasta, local), phir API checks add karo |
| 2 | `resolve_locations` | David ka comment hai, API confirmed hai, self-contained hai. `validate_slots` ka hi ek bada hissa |
| 3 | `derive_channel_tier` | Sab kuch iske upar khada hai (matching, tier, forecast) |
| 4 | `validate_targeting` | Chhota, rules clear hain, David ke comment ka seedha jawab |
| 5 | `compute_effective_cpm` | Bina iske forecast galat number dega |
| 6 | `normalise_deal_currency` | 9% error, aur chhupa hua error hai |

**`validate_slots` ko do phase me banao:**

```
Phase 1 (aaj hi ban jayega)   sirf enum + cross-field rules
                              koi API nahi, sab local
                              TABLET, invalid market, mobile-OS-bina-MOBILE
                              — ye sab yahin pakde jayenge

Phase 2 (API wale)            name uniqueness, deals count, locations,
                              ASINs, credit, conversion events
                              — batch karo, parallel chalao
```

**Uske baad:**
7. `state_uncertainty` — chauthe principle ka enforcement
8. `assess_forecast` + `repair_plan` — bid lever ke saath
9. `build_create_payload` — `automated-strategies` ka shape
10. `resolve_dates`, `ask_missing` — conversation polish

**Jab tak jawab na aaye, ye rok do:**
- `load_session_context` → **D47** (403)
- Delivery control fields → **D50**
- `user_location_signal` → **D48**
- Fee stacking ka final number → **D49**

## 10.6 Purane code me jo fix karna hai

| File | Problem | Fix |
|---|---|---|
| `select_inventory.py` | Hardcoded tier labels — `rules.yaml` me bhi hain = **do source of truth** | Registry se padho |
| `predict_reach.py` | `MIN_VIABLE_REACH` hardcoded | Registry se |
| `extract_fields.py` | `_confirmation()` defaults ko "aapne bola" bolke dikhata hai | Defaults alag dikhao — DEFAULTED-ADVISED bolna hai |
| `suggest_audiences.py` | ✅ Fee bug fix ho gaya | — |
| `mock.py` | ✅ "Narrow mehngi hai" hata diya | — |

## 10.7 Tests jo likhne hain

Ye tests hi ye saabit karenge ki hum ne verification se seekha:

```
1. Deal naam ke 8 formats parse hote hain, aur Tubi/TUBI ek hi channel hai
2. Jo naam parse nahi hua uska confidence UNKNOWN hai — aur wo dikhta hai
3. Zero-CPM deal se divide by zero nahi hota
4. USD deal + EUR plan pe currency mismatch flag hota hai
5. Ambiguous postcode pe agent POOCHTA hai, pehla nahi uthata
6. Unresolved postcode chupchap drop nahi hota
7. mobile_operating_systems bina MOBILE = validation error
8. streaming_tv bina CONNECTED_TV = validation error
9. TABLET reject hota hai
10. Conversion event market ke hisab se filter hote hain
11. Repair loop bid PEHLE try karta hai, audience baad me
12. Forecast ke saath "estimate" ka disclaimer aata hai (PG deal nahi hai)
13. Audience fee aur contextual fee ALAG dikhte hain (D49 tak)
14. Advertiser defaults 403 pe agent crash nahi hota, poochta hai
15. Enum values /choices/ se aate hain, hardcoded nahi
```

**Aur `validate_slots` ke apne tests — ye "user ne bola to sahi hai" ki galti pakadte hain:**

```
16. User ne jo naam diya, wo uniqueness API se check hota hai
17. Naam already hai to agent BATATA hai — "-2" lagakar aage NAHI badhta
18. User ne "Netflix" bola par GB me deal nahi → agent batata hai + jo
    available hai wo list karta hai
19. User ne "TABLET" bola → REPORT hota hai, chupchap drop NAHI hota
20. User ne valid market bola par us market me 0 deal → batata hai
21. User ne 45s bola par 45s deal nahi → batata hai kaunsi duration hai
22. User ne CHECKOUT chuna US market pe → invalid, kyunki GB-only hai
23. Market GB se US badla → purani conversion selection DOBARA validate hoti hai
24. User ne budget bola jo credit se zyada hai → Step 1 pe pata chalta hai,
    Step 12 pe nahi
25. Confirmation message me sirf VALIDATED value jaati hai
26. Jo check nahi ho saka wo UNVERIFIABLE hai, VALID nahi
27. User ne specific_deal_id diya jo exist nahi karta → batata hai
28. User ne ROAS target 4.5 diya → string me jaata hai, 4 nahi banta
```

---
---

# Aakhri baat — ek page ka summary

**Kaam kya hai:** Trader ek line likhta hai, agent 30+ fields bharke ek executable Strategy card banata hai.

**Kaise:** 13 step, 4 principle (Zero Hallucination, Self-Filling Form, API-Driven, Stated Uncertainty).

**Sabse important rule:** Zero Hallucination ke **teen** hisse hain — invent mat karo, **hamesha verify karo (user ki boli hui value bhi)**, aur chupchap fix mat karo. Trader ne naam bola to uniqueness check karo. Netflix bola to deal hai ki nahi dekho. TABLET bola to batao ki wo value nahi hai. **Chupchap sudharna sabse bada dhoka hai — kyunki plan chal jayega.**

**Verification se kya mila:** 11 cheezein galat thi. 5 ka ek hi karan — **UI ka filtered view poora set samajh liya.** Saare count kam the, saare enum chhote the.

**Sabse bade 4 corrections:**
1. Currency **advertiser** se, market se nahi — aur 9% arithmetic error ka khatra
2. Deal pe **channel field nahi** — 8 naming convention parse karne padenge
3. **92% floor-rate** — bid ek asli aur sabse safe lever hai
4. `automated-strategies` create endpoint hai, `simple-strategies` nahi

**Do blocker:** D47 (advertiser defaults 403) aur D50 (15 delivery fields specify nahi hue).

**Sabse badi data request:** D53 — deal pe ek asli `channel` field.

**Sabse zaroori honesty:** **Koi PG deal nahi hai — to koi bhi forecast guarantee nahi hai. Sirf estimate.**
