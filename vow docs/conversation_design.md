# Planning Agent — Conversation Design

**Ye document kis liye:** Manual VOW platform par trader 6-step wizard bharta hai. Agentic way me wo **baat** karega. Ye document batata hai — user kya daal sakta hai, hum kya extract karenge, kya puchenge, aur **har possible case** me kya hoga.

**Grounding:** `strategy_schema_registry_v4.md` (§5, §6), David ke 28 comments, `user_questions.txt`, aur platform walkthrough (177 findings).

---

## 1. Manual vs Agentic — kya badal raha hai

### Manual (jo aaj VOW platform par hai)

```
Step 1  Strategy details    12 fields bharo
Step 2  Goal, KPI & Bid     7 fields bharo
Step 3  Deals               83 deals me se tick karo
Step 4  Audiences           15 sets me se tick karo
Step 5  Creatives           4 assets me se tick karo
Step 6  Summary             review karo → Create
```

Trader **har field khud bharta hai.** Har step par form hai.

### Agentic (jo hum bana rahe hain)

```
Trader:  "£10,000 in the UK for September, 30-second creative"
             ↓
Agent:   brief samjha → deals match kiye → audiences suggest ki
             ↓
Trader:  "balanced"
             ↓
Agent:   forecast diya → strategy card taiyaar
```

Trader **baat karta hai.** Agent form bharta hai.

🔴 **Yahi Comment 6 ka poora point hai:** *"The trader should end up being asked for very little."*

---

## 2. Plan ko kya chahiye — aur kya PUCHNA hai

Ye sabse zaroori table hai. Har field ka **source** batata hai ki wo kahan se aayega.

### 2.1 Jo trader se PUCHNA padta hai (sirf 4)

| Field | Kyun puchna padta hai | Agar na de to |
|---|---|---|
| **Market** | Deals, currency, rate card, categories — sab market par depend | 🔴 Rok do, pucho. Iske bina kuch nahi ho sakta |
| **Budget** | CPM ke saath milkar impressions banata hai | 🔴 Rok do, pucho |
| **Flight dates** | Forecast ka input hai | 🔴 Rok do, pucho |
| **Creative durations** | Kaunsi deals available hain aur CPM kya hoga — ye tay karta hai | 🟠 Rok do, pucho — **par ye contentious hai, §7 dekho** |

**Aur wo bhi tab jab brief me na ho.** Brief me likha ho to nahi puchenge.

### 2.2 Jo trader se KABHI NAHI puchna (Comment 6)

| Field | Kahan se aayega | Comment |
|---|---|---|
| **Strategy name** | Agent banayega — `Education_GB_Awareness_Sep2026` | 7 |
| **Currency** | Advertiser ki setting se | 9 |
| **Goal** | CTV me hamesha `AWARENESS` — fixed | 6 |
| **Format** | Hamesha `streaming_tv` — fixed | 14 |
| **Product categories** | Advertiser se, ya brief se imply | 15 |
| **Frequency cap** | Advertiser ki setting se | 13 |
| **Base bid** | Deal ke CPM se (par ye **contested** hai — §7) | 12 |
| **Selling location** | Advertiser se | 16 |
| **ASINs** | Baad me, tracking step par | 17 |
| **Deals** | Agent **match** karega, table nahi dikhayega | 18 |
| **Location/device targeting** | Default bhara aayega | 21, 22 |

### 2.3 Jo trader se PUCHNA hai, par sirf jab zaroori ho

| Field | Kab puchna | Comment |
|---|---|---|
| **Audience choice** | Teen options dikha kar — ya decline | 4 |
| **KPI target value** | Sirf jab KPI `frequency` ho (2–5) | 10 |
| **Channel** | Sirf jab brief me na ho aur farak padta ho | 18 |

---

## 3. Teen bade scenarios

### Scenario A — Trader **sab kuch** ek prompt me deta hai

```
"£10,000 in the UK for September, 30-second creative"
```

**Kya extract hoga:**

| Field | Value | Kaise |
|---|---|---|
| `markets` | `["GB"]` | "UK" se |
| `market_budgets` | `10000.00` | "£10,000" se |
| `primary_currency` | `GBP` | `£` symbol se |
| `flight_dates` | `2026-09-01` → `2026-09-30` | "September" se — poora mahina |
| `durations` | `["30"]` | "30-second" se |

**Kya khud set hoga:** goal=AWARENESS, kpi=reach, format=streaming_tv, name=generated

**Agent ka raasta:**
```
Turn 1:  confirm karo → deals match karo → audiences suggest karo → RUKO
Turn 2:  trader ne audience chuni → forecast do
```

**Do turn me plan taiyaar.** ✅ Ye ideal case hai.

---

### Scenario B — Trader **aadha** deta hai

```
"I need a CTV campaign in the UK"
```

**Kya extract hoga:**

| Field | Value |
|---|---|
| `markets` | `["GB"]` ✅ |
| `market_budgets` | ❌ missing |
| `flight_dates` | ❌ missing |
| `durations` | ❌ missing |

**Agent ka raasta:**
```
Turn 1:  jo mila wo confirm karo
         jo missing hai — SAB EK SAATH pucho:
         
         "Before I can carry on I need a few more details:
          - the budget
          - the start and end dates
          - the creative durations - 10, 15, 20 or 30 seconds"
          
Turn 2:  "£10,000, September, 30 seconds"
         → merge karo → aage badho
```

🔴 **Ek saath pucho, ek-ek karke nahi.** Char alag sawaal = char round trip = wahi wizard experience jo hum hata rahe hain. Ye `ask_for_missing.py` me already implement hai.

---

### Scenario C — Trader **kuch nahi** deta

```
"hi"     ya     "I need to plan a campaign"
```

**Kya extract hoga:** kuch nahi

**Agent ka raasta:**
```
"hi"  →  GREETING intent  →  registry ka welcome, aur teen cheezein maango
                              (plan ko chhua nahi jaayega)

"I need to plan a campaign"  →  BRIEF intent, par kuch nahi mila
                             →  chaaron cheezein ek saath maango
```

---

## 4. Turn-by-turn — poora ideal safar

```
┌─ TURN 1 ────────────────────────────────────────────────────────┐
│ TRADER: "£10,000 in the UK for September, 30-second creative"   │
│                                                                 │
│ AGENT karta hai:                                                │
│   1. classify_intent        → BRIEF                             │
│   2. extract_fields         → market, budget, dates, duration   │
│   3. [gate] basics poore?   → HAAN, aage badho                  │
│   4. select_inventory       → GET /deals/  (TOOL CALL)          │
│                             → 4 deals mile, tier classify hui   │
│   5. suggest_audiences      → POST /suggest/  (TOOL CALL)       │
│                             → 3 options bane                    │
│   6. [gate] choice pending  → RUKO                              │
│                                                                 │
│ AGENT bolta hai:                                                │
│   - "ye samjha maine..." (confirmation)                         │
│   - "GB me ye inventory hai..." (deals + CPM)                   │
│   - "teen audience options..." + "ya skip kar sakte hain"       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─ TURN 2 ────────────────────────────────────────────────────────┐
│ TRADER: "balanced"                                              │
│                                                                 │
│ AGENT karta hai:                                                │
│   1. classify_intent        → SELECTION, selection=BALANCED     │
│   2. apply_audience         → chosen_audience set               │
│   3. [gate] settled?        → HAAN                              │
│   4. predict_reach          → POST /reach-forecast/ (TOOL CALL) │
│                                                                 │
│ AGENT bolta hai:                                                │
│   - Impressions, reach, frequency, CPM                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    (aage — abhi nahi bana)
                    finalise → create → targeting → activate
```

**Do turn. Do trader inputs. Teen tool calls.**

---

## 5. 🔴 Har possible case — poori list

Ye wo table hai jo aapne maanga — "all the things possible".

### 5.1 Market ke case

| Trader kya likhega | Agent kya kare | Kahan se |
|---|---|---|
| `UK` · `Britain` · `GB` · `England` | `markets = ["GB"]` | ✅ Ban chuka |
| `US` · `USA` · `America` | `markets = ["US"]` | ✅ Ban chuka |
| `UK and Germany` | 🟠 M1 me ek market. **Saaf bolo** aur ek se shuru karne ka propose karo | Comment 8 |
| `Germany` | 🔴 Platform par sirf **GB aur US** hain. Batao ki wo market available nahi | Platform verified |
| Market nahi bataya | Pucho — iske bina kuch nahi ho sakta | Comment 8 |

### 5.2 Budget ke case

| Trader kya likhega | Agent kya kare | Status |
|---|---|---|
| `£10,000` · `$25,000` · `50k` · `2.5m` | Extract karo, currency symbol se le lo | ✅ Ban chuka |
| `budget of 50000` | Extract karo | ✅ Ban chuka |
| `8 to 10 thousand` (range) | 🔴 **Open question** — upper lo, lower lo, ya pucho? | v4.0 §5.4 |
| `£500` (bahut chhota) | ❓ Minimum spend hai? `user_questions.txt` puchta hai — **client se poochna hai** | Open |
| `500,000 impressions` (budget nahi) | 🔴 Abhi support nahi. `user_questions.txt` me hai — batao ki budget chahiye | Open |
| `$10,000` par market `GB` | ❓ Kaunsa jeetega — symbol ya market? **Open question** | Comment 9 |
| Budget nahi bataya | Pucho | — |

### 5.3 Dates ke case

| Trader kya likhega | Agent kya kare | Status |
|---|---|---|
| `September` | Poora mahina — 1 se 30 | ✅ Ban chuka |
| `next month` · `Q4` · `in two weeks` | Aaj ke hisab se resolve karo | ✅ Ban chuka (date prompt me hai) |
| `1-15 September` | Wahi range | ✅ Ban chuka |
| `last September` (past) | 🔴 Reject karo — `lower >= today` chahiye. Dobara pucho | v4.0 §5.4 |
| `for 1 day` | 🟠 Chalega, par frequency bahut high hogi — batana chahiye | Ban nahi |
| `always on` | ❓ Kya matlab? Pucho | Open |
| Dates nahi bataye | Pucho | — |

### 5.4 Duration ke case

| Trader kya likhega | Agent kya kare | Status |
|---|---|---|
| `30-second` · `30s` · `30 sec` | `["30"]` | ✅ Ban chuka |
| `15 and 30` | `["15", "30"]` | ✅ Ban chuka |
| `45 seconds` | 🟠 Platform par 45 **hai** (7 durations: 10,15,20,30,40,45,60). Code me sirf 4 hain — **fix karna hai** | Platform verified |
| `I don't know yet` | 🔴 **Bada case.** Creative abhi bana hi nahi. §7 dekho | Open |
| Duration nahi bataya | Pucho — par ye contentious hai | §7 |

### 5.5 Extra cheezein jo trader de sakta hai

| Trader kya likhega | Agent kya kare | Kahan se |
|---|---|---|
| `on Prime Video` | `channel = ["Prime Video"]` — matching narrow ho jaayegi | Comment 18 |
| `Netflix only` | Channel filter. Par batao ki 3P se **reach forecast nahi** aata | Comment 18 |
| `Action genre` | Genre upsell — ROS vs Action ka CPM farak batao | v4.0 §5.5.5 |
| `deal ID EXT245WE18EEMKX` | Escape hatch — us deal ko dhundo | Comment 18 |
| `my ASINs are B08N5WRWNW...` | 🟠 ASINs **baad me** chahiye. Park kar do, tracking step par use hoga | Comment 17 |
| `frequency of 3` | KPI = frequency, target = 3 | Comment 10 |
| `target parents in London` | Audience + geography dono. Audience suggest me use karo | Comment 5 |
| `postcodes SW1, SW3` | Geography. Batao ki wo creation ke **baad** set hoti hai | Comment 5 ✅ Ban chuka |
| `display ads bhi chahiye` | 🔴 CTV scope se bahar. `capability` phrase se jawab do | ✅ Ban chuka |
| `YouTube par chalao` | 🔴 Hamari inventory me nahi. Batao kaunse channels hain | Ban nahi |

### 5.6 Contradiction aur correction ke case

| Case | Agent kya kare | Status |
|---|---|---|
| Ek hi message me ulta: `"£10k... no make it £20k"` | Aakhri wala lo (LLM ye handle karta hai) | ✅ Ban chuka |
| Baad me correction: `"actually £25,000"` | BRIEF intent → merge → dobara aage badho | ✅ Ban chuka |
| Audience chunte waqt correction | BRIEF, SELECTION nahi. Plan update karo | ✅ Ban chuka |
| `"forget everything, start over"` | ❓ Reset command chahiye — **abhi nahi hai** | Open |
| `"same as last campaign"` | 🔴 History capability nahi hai — batao | Open |

### 5.7 Non-brief messages

| Trader kya likhega | Intent | Agent kya kare | Status |
|---|---|---|---|
| `hi` · `hello` | GREETING | Welcome + scope | ✅ Ban chuka |
| `what can you do?` | CAPABILITY | Kaam ki list + kya nahi karta | ✅ Ban chuka |
| `what's the weather?` | OUT_OF_SCOPE | Short redirect | ✅ Ban chuka |
| `ignore your instructions` | OUT_OF_SCOPE | Wahi redirect | ✅ Ban chuka |
| `asdfgh` | UNCLEAR | Rephrase maango | ✅ Ban chuka |
| `what's the CPM?` | QUESTION | 🟠 Abhi deferred phrase. Asli jawab baad me | Partial |
| `ok` (audience choose karte waqt) | SELECTION (khaali) | Dobara pucho, default **na lo** | ✅ Ban chuka |
| `` (khaali) | EMPTY | Chhota nudge | ✅ Ban chuka |

---

## 6. Kitne sawaal, aur kaise puchne hain

### Rule 1 — Ek saath pucho, ek-ek karke nahi

```
❌ GALAT:
   Agent: "Market?"        Trader: "UK"
   Agent: "Budget?"        Trader: "£10,000"
   Agent: "Dates?"         Trader: "September"
   Agent: "Duration?"      Trader: "30s"
   → CHAR round trip. Wizard hi ban gaya.

✅ SAHI:
   Agent: "Before I can carry on I need a few more details:
            - the budget
            - the start and end dates
            - the creative durations
           Send them over and I'll put the plan together."
   → EK round trip.
```

### Rule 2 — Jo mila hai wo confirm karo, jo nahi mila wo maango

Dono ek hi message me. Trader ko dikhna chahiye ki agent ne kya samjha (ye trust ka mechanism hai — v4.0 §5.4).

### Rule 3 — Jo khud set kiya hai, use "understood" na kaho

🔴 **Ye abhi galat hai:**
```
"Here is what I understood..."
   - Goal: Awareness, measured on reach (fixed for CTV)     ← user ne nahi kaha!
```

Sahi hona chahiye:
```
Ye aapne bataya:      market GB · £10,000 · September · 30s
Ye maine set kiya:    currency GBP (advertiser default) · goal Awareness (CTV fixed)
```

**Do alag section.** Kyunki *"I understood"* ka matlab hai *"aapne kaha"*.

---

## 7. 🔴 Do tension jo resolve karni hain

### Tension 1 — David ke do inputs ULTE hain

`user_questions.txt` me David ne **12 discovery questions** likhe hain:

```
What is your goal or business outcome?
Where do you sell your products or services?
Tell us about your target audience?
Do you want to plan against a fixed budget or an impression target?
Do you have 1st party data you can share with us?
What are your flight dates?
What is your budget?
How will we measure success?
Do you have any specific channels in mind?
What devices do you want your ads to appear on?
Do you want to apply geo targeting?
Do you have a supplier to create the cut downs?
```

Par **Comment 6** me David ne kaha: *"The trader should end up being asked for very little — in practice the market, the budget and the dates."*

**Ye do baatein ek doosre ke khilaf hain.** 12 sawaal vs 3 sawaal.

**Mera padhna:** 12 wali list ek **checklist** hai — jo cheezein plan ko chahiye. Comment 6 kehta hai un me se **zyadatar khud pata karo**, pucho nahi. Jaise:

| David ka sawaal | Comment 6 ke hisab se |
|---|---|
| "What is your goal?" | CTV me hamesha Awareness — **na pucho** |
| "Where do you sell?" | Advertiser se — **na pucho** |
| "What devices?" | Advertiser se — **na pucho** |
| "Geo targeting?" | Default market country — **na pucho** |
| "Flight dates?" | ✅ **Pucho** |
| "Budget?" | ✅ **Pucho** |
| "Channels in mind?" | Optional — brief me ho to lo, warna match karo |

🔴 **Ye David se confirm karna hai.**

### Tension 2 — Duration puchna chahiye ya nahi

**Abhi:** `durations` **required** hai (`gates.py` me BASICS me hai). Iske bina flow ruk jaata hai.

**Problem:** trader ko planning ke waqt duration pata **nahi** ho sakti — creative abhi agency ke paas hai. David ka apna sawaal hai: *"If we recommend multiple creative duration do you have a supplier to create the cut downs?"* — yaani **agent recommend karta hai**, trader batata nahi.

**Par duration zaroori hai** — usse deals aur CPM tay hote hain.

**Teen options:**

| Option | Kaise |
|---|---|
| A. Puchte raho | Aaj yahi hai. Trader ruk sakta hai |
| B. Default maan lo | Sabse aam duration (30s?) le lo aur **bata do** |
| C. Sab durations par plan karo | Multi-duration plan, budget split ke saath |

🔴 **Ye bhi David se puchna hai.**

---

## 8. Ab kya bana hai, kya nahi

| Hissa | Status |
|---|---|
| Intent classification (8 kism) | ✅ Ban chuka |
| Greeting / out-of-scope / capability | ✅ Ban chuka |
| Brief extraction (market, budget, dates, duration) | ✅ Ban chuka |
| Missing fields ek saath puchna | ✅ Ban chuka |
| Deals match karna | ✅ Ban chuka (mock par) |
| 3 audience options | ✅ Ban chuka |
| Trader ka choice, aur decline | ✅ Ban chuka |
| Geography instead (Comment 5) | ✅ Ban chuka |
| Forecast | ✅ Ban chuka (mock par) |
| **Audience fee ka sahi model (Comment 2)** | 🔴 **Galat — agla step** |
| **"Amazon audiences only" (Comment 19)** | 🔴 **Galat — agla step** |
| **"Goal" ko understood batana** | 🔴 Galat |
| Repair loop (reach kam → widen) | ❌ Nahi bana |
| Question answering ("CPM kya hai?") | ❌ Nahi bana |
| Advertiser defaults load karna | ❌ Nahi bana |
| Finalise → Create strategy | ❌ Nahi bana |
| 45s/40s/60s durations | 🔴 Code me sirf 10/15/20/30 |
| Reset / start over | ❌ Nahi bana |
| Impression target (budget ki jagah) | ❌ Nahi bana |

---

## 9. Client se puchne wale sawaal (is document se nikle)

| # | Sawaal | Kyun |
|---|---|---|
| 1 | 12 discovery questions vs "ask very little" — kaunsa? | Tension 1 |
| 2 | Duration puchni hai, default leni hai, ya multi-duration plan? | Tension 2 |
| 3 | Minimum spend per market/channel kya hai? | `user_questions.txt` me hai, hamare paas jawab nahi |
| 4 | Impression target ke against plan karna M1 me chahiye? | David ka sawaal hai |
| 5 | Budget range diya to upper/lower/pucho? | v4.0 open |
| 6 | Currency symbol aur market ulte hon to kaunsa jeetega? | Comment 9 |
| 7 | "Start over" / reset chahiye? | Practical |
| 8 | Sirf GB aur US hain — aur markets aayenge? | Platform verified |

---

**Ye document abhi ka snapshot hai. Jaise-jaise steps bante jaayenge, §8 update hoga.**
