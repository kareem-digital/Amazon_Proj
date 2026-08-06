# Strategy Creation — Manual Flow vs Agentic Flow

**Ye document kis liye:** VOW platform par trader **manually** kaise strategy banata hai, aur **agent** wahi kaam kaise karega. Data kahan se kahan jaata hai, kaunsi API call hoti hai, kaunsi field required hai, aur poora sequence.

**Source:** `staging.vowmade.dev` par 4 August 2026 ki verification — 9 screens, 17 APIs, test strategy `VMA2026368`. Aur `Strategy_Schema_v4.0_FINAL.md`.

---

## Index

| § | Kya |
|---|---|
| 1 | Do flow, ek nazar me |
| 2 | MANUAL FLOW — jo aaj platform par hai |
| 3 | AGENTIC FLOW — turn by turn |
| 4 | DATA FLOW — data kahan se kahan |
| 5 | POORA SEQUENCE — ek diagram me |
| 6 | Field matrix — required vs optional |
| 7 | Decision points — har branch |
| 8 | Failure paths — kya galat ho sakta hai |
| 9 | Do flows ka aakhri comparison |

---
---

# 1. Do flow, ek nazar me

```
════════════════════════════════════════════════════════════════════════
   MANUAL WAY  (aaj)                    AGENTIC WAY  (banana hai)
════════════════════════════════════════════════════════════════════════

   Trader "New Strategy" dabata hai      Trader ek line likhta hai
            ↓                                      ↓
   ┌──────────────────────┐              "£10,000 in the UK for
   │ Step 1: 12 fields    │               September, 30-second"
   │ bharo                │                        ↓
   └──────────┬───────────┘              ┌─────────────────────────┐
              ↓                          │ Agent 11 fields KHUD    │
   ┌──────────────────────┐              │ nikaal leta hai         │
   │ Step 2: 7 fields     │              └────────┬────────────────┘
   │ bharo                │                       ↓
   └──────────┬───────────┘              ┌─────────────────────────┐
              ↓                          │ Deals KHUD match        │
   ┌──────────────────────┐              │ karta hai               │
   │ Step 3: 83 deals me  │              └────────┬────────────────┘
   │ se tick karo         │                       ↓
   └──────────┬───────────┘              ┌─────────────────────────┐
              ↓                          │ 3 audience options      │
   ┌──────────────────────┐              │ dikha kar RUKTA hai     │
   │ Step 4: 15 sets me   │              └────────┬────────────────┘
   │ se tick karo         │                       ↓
   └──────────┬───────────┘                "balanced"
              ↓                                   ↓
   ┌──────────────────────┐              ┌─────────────────────────┐
   │ Step 5: 4 assets me  │              │ Forecast + Strategy     │
   │ se tick karo         │              │ card taiyaar            │
   └──────────┬───────────┘              └─────────────────────────┘
              ↓
   ┌──────────────────────┐
   │ Step 6: Review       │
   │ → Create Strategy    │
   └──────────────────────┘

   6 screens · ~25 clicks              2 messages
   ~10 minutes                          ~30 seconds
════════════════════════════════════════════════════════════════════════
```

## Sabse bada farak — ek line me

| | Manual | Agentic |
|---|---|---|
| Trader kya karta hai | **Form bharta hai** | **Baat karta hai** |
| Deals | Table me se **chunta hai** | Agent **match karta hai** |
| Kitne inputs | ~25 | **3** (market, budget, dates) |
| Kya sequence hai | Fixed — 6 steps, ek ke baad ek | Adaptive — jo mila nahi wahi puchega |

---
---

# 2. MANUAL FLOW — jo aaj platform par hai

## Poora naksha

```
┌─ SCREEN 0 ── Strategies List ─────────────────────────────────────┐
│                                                                   │
│  361 strategies · 25 columns · 4 filters                          │
│                                                                   │
│  APIs jo load par chalti hain:                                    │
│    ① GET /api/credits/summary/?advertiser={uuid}      56 B        │
│    ② GET /api/reports/user-preferences/               0.3 kB      │
│    ③ GET /api/strategies/?{11 params}                 21 kB 1.4s  │
│                                                                   │
│                    [ + New Strategy ]                             │
└───────────────────────────┬───────────────────────────────────────┘
                            ↓
┌─ STEP 1 ── Strategy Details ──────────────────────────────────────┐
│  URL: /app/strategies/create/dsp?step=0                           │
│                                                                   │
│  Trader BHARTA hai (8 fields):                                    │
│    • Strategy name          text                                  │
│    • Flight dates           date range                            │
│    • Target markets         multi-select   (sirf UK, US)           │
│    • Primary currency       dropdown       (EUR pehle se bhari!)   │
│    • Formats                4 cards                               │
│    • Product categories     2-level tree   (video format par)      │
│    • Where do you sell?     2 cards                               │
│    • Product ASINs          textarea                              │
│                                                                   │
│  🔴 Format chunte hi CHAR pre-flight APIs chalti hain:            │
│    ④ GET /audience-sets/check_market_has_audience_set/?markets=GB │
│         → [{"market":"GB","exists":true}]              31 B 285ms │
│    ⑤ GET /creatives/recs/check_market/?markets=GB                │
│         → [{"market":"GB","exists":true}]              31 B 256ms │
│    ⑥ GET /assets/check_market_has_assets/?markets=GB              │
│         &target_types=DISPLAY,VIDEO,STREAMING_TV,MOBILE           │
│         &dsp_approved=true                            227 B 328ms │
│    ⑦ GET /inventory-sources/?strategy_formats=streaming_tv        │
│         &markets=GB&goal=AWARENESS                    136 B 771ms │
│         → Amazon Streaming TV, Twitch                             │
│                                                                   │
│  Off Amazon chunne par:                                           │
│    ⑧ GET /conversions/definitions/                    0.7 kB      │
│                                                                   │
│  🔴 "Next" par SIRF EK call:                                      │
│    ⑨ GET /strategies/check_strategy_name_uniqueness/?name=...    │
│         → {"is_unique": true}                          18 B 242ms │
│                                                                   │
│  NEXT block hota hai jab: name/dates/markets/format missing ho     │
│                           ya On Amazon par invalid ASIN ho         │
└───────────────────────────┬───────────────────────────────────────┘
                            ↓
┌─ STEP 2 ── Goal, KPI & Bid ───────────────────────────────────────┐
│  🔴 Stepper 5 se 6 ho jaata hai (2 format chune to)               │
│                                                                   │
│  Trader BHARTA hai (7 fields):                                    │
│    • Goal                   3 cards      (Awareness pehle se)      │
│    • KPI — PER FORMAT       2 cards × N  (Reach / Frequency)       │
│    • KPI target value       dropdown     (2,3,4,5 — frequency par) │
│    • Customise inventory    multi-select (pehle se bhari)          │
│    • Ad Tag conversions     4 checkbox   (per market flag)         │
│    • Budget                 decimal      [Primary｜Market] toggle  │
│    • Base bid               decimal      🔴 REQUIRED               │
│                                                                   │
│  Koi API call nahi (name check step 1 ke Next par hui thi)         │
│                                                                   │
│  NEXT block hota hai jab: base bid khaali ho                       │
│     → "All fields should be filled."                              │
│                                                                   │
│  🔴 Currency toggle CONVERT karta hai:                            │
│     Market  → £10,000        Primary → €10,909.09   (1.0909)      │
└───────────────────────────┬───────────────────────────────────────┘
                            ↓
┌─ STEP 3 ── Deals ─────────────────────────────────────────────────┐
│  Trader 83 deals me se TICK karta hai                             │
│                                                                   │
│  Filters: Market ▾  Format ▾  Source ▾  Device ▾  Deal type ▾     │
│                                                                   │
│    ⑩ GET /deals/?markets=GB,ZZ                                    │
│         &formats=streaming_tv,prime_video,UNKNOWN                 │
│         &deal_type=&ad_lengths=&genre=&sources=&devices=          │
│         &publisher=&page_size=25                     17 kB 2.45s  │
│         → count: 83                                               │
│    ⑪ GET /deals/filter-properties/?formats=...        0.8 kB      │
│         → genres, ad_lengths, exchanges, devices                  │
│                                                                   │
│  NEXT DISABLED jab tak ek bhi deal tick na ho                     │
└───────────────────────────┬───────────────────────────────────────┘
                            ↓
┌─ STEP 4 ── Audiences ─────────────────────────────────────────────┐
│  Trader 15 sets me se TICK karta hai                              │
│                                                                   │
│  Filters: Fee ▾ (Free/Has fee)   Goal ▾                           │
│  Toggle:  [ Similar ] [ Exact ]  ← Exact default                  │
│                                                                   │
│    ⑫ GET /audience-sets/?search=&page_size=25        15 kB 1.28s  │
│         → count: 15                                               │
│                                                                   │
│  NEXT DISABLED jab tak ek set tick na ho                          │
└───────────────────────────┬───────────────────────────────────────┘
                            ↓
┌─ STEP 5 ── Creatives ─────────────────────────────────────────────┐
│  Trader 4 assets me se TICK karta hai                             │
│  🔴 Ye UPLOAD screen nahi hai — library se chunna hai              │
│                                                                   │
│    ⑬ GET /assets/?target_types=...&dsp_approved=...  2.6 kB       │
│         → count: 4                                                │
│                                                                   │
│  🔴 Asset tick karne par:                                         │
│    ⑭ GET /creatives/?approval_status=APPROVED&markets=GB          │
│         &asset={uuid}&no_pagination=true             7.2 kB       │
│         → 25 creatives! (ek asset se)                             │
│                                                                   │
│  🔴 0 creatives ke saath bhi aage jaa sakte hain                  │
└───────────────────────────┬───────────────────────────────────────┘
                            ↓
┌─ STEP 6 ── Summary ───────────────────────────────────────────────┐
│  5 review cards, har ek me [Edit]                                 │
│                                                                   │
│  🔴 Screen par aate hi forecast chalta hai:                       │
│    ⑮ POST /strategies/reach-forecast/                531 B        │
│         REQUEST me sirf 4 cheezein:                               │
│           flight_dates · formats · goal · market_budgets          │
│         🔴 KOI deals nahi, KOI audiences nahi, KOI targeting nahi │
│                                                                   │
│         RESPONSE:                                                 │
│           total_reach: 233,803                                    │
│           total_impressions: 860,716                              │
│           supplies: [DSP_STREAMING_TV, DSP_PRIME_VIDEO]           │
│                                                                   │
│              [ Create Strategy ]                                  │
└───────────────────────────┬───────────────────────────────────────┘
                            ↓
                    ⑯ POST /api/strategies/
                       1.0 kB → 201 Created
                       id: VMA2026368
                            ↓
┌─ POST-CREATION ── Strategy Overview ──────────────────────────────┐
│  Status: Paused · Inactive · Syncing ⟳                            │
│                                                                   │
│    ⑰ GET /api/strategies/VMA2026368/                3.5 kB       │
│                                                                   │
│  7 sections:                                                      │
│    Overview · Planner · Campaigns · Creatives ·                    │
│    Audience sets · 🔴 Locations · Strategy history                │
│                                                                   │
│  🔴 TARGETING yahan hai — creation me nahi                        │
│  🔴 BUDGET SPLIT yahan hai — platform ne khud 50/50 kar diya      │
└───────────────────────────────────────────────────────────────────┘
```

## Manual flow ki teen zaroori baatein

**1. Wizard poora client-side hai.** Steps ke beech **kuch save nahi hota**. Sirf ek call jaati hai — name uniqueness check. Poora plan browser me banta hai aur aakhir me **ek POST** se create hota hai.

**2. Forecast me deals/audiences jaate hi nahi.** Trader 83 deals me se chunta hai, 15 audiences me se chunta hai — aur forecast un me se **kuch bhi** use nahi karta. Sirf dates, formats, goal, budget.

**3. Targeting aur budget split creation ke BAAD hote hain.** Wizard me targeting ka step hi nahi hai.

---
---

# 3. AGENTIC FLOW — turn by turn

## Ideal case — do turn me plan

```
╔═══════════════════════════════════════════════════════════════════╗
║  TURN 0 — Session shuru                                           ║
╚═══════════════════════════════════════════════════════════════════╝

  🔴 Brief padhne se PEHLE advertiser settings load hoti hain

     GET /api/admin/advertiser/{id}/

     → frequency_cap        3        is_locked: false
     → device_types         [CTV]    is_locked: TRUE  ← brand policy
     → product_categories   Education
     → selling_location     NOT_SOLD_ON_AMAZON
     → primary_currency     GBP

  🔴 ORDER zaroori hai: pehle defaults, phir brief.
     Ulta karne se defaults brief ko overwrite kar denge.


╔═══════════════════════════════════════════════════════════════════╗
║  TURN 1 — Trader brief deta hai                                   ║
╚═══════════════════════════════════════════════════════════════════╝

  TRADER:  "£10,000 in the UK for September, 30-second creative"

  ┌───────────────────────────────────────────────────────────────┐
  │ 1. CLASSIFY INTENT                                            │
  │    Rules → LLM (closed enum, 8 labels)                        │
  │    → intent = BRIEF                                           │
  │    ✅ Koi API call nahi                                       │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │ 2. EXTRACT FIELDS                                             │
  │    LLM structured output                                      │
  │                                                               │
  │    Brief se mila:        markets     ["GB"]                    │
  │                          budget      10000.00                  │
  │                          currency    GBP    (£ symbol se)      │
  │                          dates       2026-09-01 → 09-30        │
  │                          durations   ["30"]                    │
  │                                                               │
  │    Advertiser se aaya:   frequency_cap · device_types ·        │
  │                          product_categories · selling_location │
  │                                                               │
  │    Khud set hua:         name    "Education_GB_Awareness_Sep2026"│
  │                          goal    AWARENESS  (advised default)   │
  │                          format  ["streaming_tv"]  (constant)   │
  │                          kpi     REACH                         │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │ 3. GATE — basics poore hain?                                  │
  │    market ✅  budget ✅  dates ✅  durations ✅               │
  │    → AAGE BADHO                                               │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │ 4. PRE-FLIGHT + NAME CHECK           4 TOOL CALLS             │
  │                                                               │
  │    GET /audience-sets/check_market_has_audience_set/?markets=GB│
  │    GET /assets/check_market_has_assets/?markets=GB&...         │
  │    GET /inventory-sources/?strategy_formats=streaming_tv&...   │
  │    GET /strategies/check_strategy_name_uniqueness/?name=...    │
  │                                                               │
  │    Naam already hai? → "_v2" laga kar dobara check             │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │ 5. MATCH DEALS                       2 TOOL CALLS             │
  │                                                               │
  │    GET /deals/?markets=GB,ZZ&formats=streaming_tv,prime_video  │
  │    GET /rates/ctv/GB/                                         │
  │                                                               │
  │    Filter: market ✅ · duration 30s ✅ · channel ⚠️ (blocked)  │
  │    → 4 deals match hui                                        │
  │    → tier classify (channel naam se — blocked, D4)             │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │ 6. SUGGEST AUDIENCES                 3 TOOL CALLS             │
  │                                                               │
  │    Agent PROMPT likhta hai:                                   │
  │      "adults interested in online education in the UK"        │
  │                                                               │
  │    POST /audience-sets/suggest/          → {"id": "abc"}       │
  │    GET  /audience-sets/suggest/abc/      → flat list, 40+ seg  │
  │    GET  /contextual-targeting/fees       → rate (1.63)         │
  │                                                               │
  │    Agent 3 groups banata hai:  Narrow / Balanced / Wide        │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │ 7. GATE — choice pending                                      │
  │    awaiting_choice = "audience"                               │
  │    🔴 TURN KHATAM. Default NAHI lena.                          │
  └───────────────────────────────────────────────────────────────┘

  AGENT BOLTA HAI:
    ① "Ye aapne bataya: GB, £10,000, September, 30s
        Ye maine set kiya: GBP (advertiser), Awareness (CTV default)"
    ② "GB me ye inventory hai: Prime Video £18.22 ... "
    ③ "Teen audience options — ya skip kar dein"

  TOTAL: 9 tool calls, 2 LLM calls


╔═══════════════════════════════════════════════════════════════════╗
║  TURN 2 — Trader audience chunta hai                              ║
╚═══════════════════════════════════════════════════════════════════╝

  TRADER:  "balanced"

  ┌───────────────────────────────────────────────────────────────┐
  │ 1. CLASSIFY INTENT                                            │
  │    Rules match! → SELECTION, selection = BALANCED             │
  │    ✅ Koi LLM call nahi (rules ne pakad liya)                 │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │ 2. APPLY AUDIENCE                                             │
  │    chosen_audience = BALANCED                                 │
  │    audience_declined = false                                  │
  │    awaiting_choice = None                                     │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │ 3. FORECAST                          1 TOOL CALL              │
  │                                                               │
  │    POST /strategies/reach-forecast/                           │
  │    🔴 REQUEST me sirf 4 cheezein:                             │
  │       flight_dates · formats · goal · market_budgets          │
  │       (audience yahan JAATI HI NAHI — platform ka design)      │
  │                                                               │
  │    → total_reach 233,803 · impressions 860,716                │
  │    → frequency 3.68  (khud calculate karna hai)               │
  └────────────────────────────┬──────────────────────────────────┘
                               ↓
                    reach theek hai?
                    ┌──────────┴──────────┐
                   HAAN                  NAHI
                    ↓                     ↓
              aage badho          REPAIR LOOP (§7)
```

## Aage ka flow (abhi banana hai)

```
╔═══════════════════════════════════════════════════════════════════╗
║  TURN 3 — Finalise                                                ║
╚═══════════════════════════════════════════════════════════════════╝
  TRADER:  "looks good, create it"
           → plan_status: DRAFT → FINALISED
           ✅ Koi API call nahi (agent-internal)

╔═══════════════════════════════════════════════════════════════════╗
║  TURN 4 — Create                                                  ║
╚═══════════════════════════════════════════════════════════════════╝
  POST /api/strategies/       ← 🔴 kaunsa endpoint? D5 open
  → 201, id: VMA2026368
  → status: Paused · Syncing

╔═══════════════════════════════════════════════════════════════════╗
║  PHASE C — teen branch, PARALLEL                                  ║
╚═══════════════════════════════════════════════════════════════════╝
  ┌── Targeting ──────┐  ┌── Creative ───────┐  ┌── Tracking ──────┐
  │ POST /targeting/  │  │ POST gen_upload   │  │ POST asin-valid  │
  │ POST locations/   │  │ POST register     │  │ GET conversions  │
  │ (postcode/radius) │  │ [WAIT: approval]  │  │ PATCH strategy   │
  └────────┬──────────┘  └────────┬──────────┘  └────────┬─────────┘
           │                      │                      │
  ┌── Budget ─────────┐  ┌── Credit ─────────┐          │
  │ PATCH flight-     │  │ GET credits/      │          │
  │ ranges/budget/    │  │ summary/          │          │
  └────────┬──────────┘  └────────┬──────────┘          │
           └──────────────────────┼──────────────────────┘
                                  ↓
╔═══════════════════════════════════════════════════════════════════╗
║  PHASE D — JOIN NODE                                              ║
╚═══════════════════════════════════════════════════════════════════╝
           8 prerequisites check → sab theek?
                    ┌──────────┴──────────┐
                   HAAN                  NAHI
                    ↓                     ↓
      POST /strategies/{id}/       SAARE missing
      set_status/                  ek saath batao
                    ↓
              monitor sync
              (fail ho sakta hai!)
```

---
---

# 4. DATA FLOW — data kahan se kahan

## Char source, ek plan

```
┌────────────────────────────────────────────────────────────────────┐
│  SOURCE 1 — TRADER KA BRIEF                                        │
│  "£10,000 in the UK for September, 30-second creative"             │
│                                                                    │
│  → markets · budget · currency · dates · durations                 │
│  Source label:  INFERRED                                           │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────┴───────────────────────────────────────┐
│  SOURCE 2 — ADVERTISER PROFILE                                     │
│  GET /api/admin/advertiser/{id}/                                   │
│                                                                    │
│  → primary_currency · frequency_cap · device_types ·               │
│    product_categories · selling_location                           │
│  Source label:  ADVERTISER  (+ is_locked flag)                     │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────┴───────────────────────────────────────┐
│  SOURCE 3 — SPECIFICATION (rules, humne tay kiye)                   │
│                                                                    │
│  → goal = AWARENESS         (advised default)                      │
│  → formats = streaming_tv   (constant)                             │
│  → name convention          (generated)                            │
│  → fee rules, tier rules, validation rules                         │
│  Source label:  CONSTANT / ADVISED / GENERATED                     │
└────────────────────────────┬───────────────────────────────────────┘
                             │
┌────────────────────────────┴───────────────────────────────────────┐
│  SOURCE 4 — VOW APIs (live data)                                   │
│                                                                    │
│  → deals · rate card · audience segments · fee rate ·              │
│    forecast · locations · assets · creatives                       │
│  Source label:  API / MATCHED                                      │
└────────────────────────────┬───────────────────────────────────────┘
                             ↓
        ╔════════════════════════════════════════════╗
        ║          AGENT STATE  (ek plan)            ║
        ║                                            ║
        ║  Har field ke saath uska SOURCE bhi        ║
        ║  record hota hai — taaki baad me           ║
        ║  batа sakein "ye kahan se aaya"            ║
        ╚═══════════════════┬════════════════════════╝
                            ↓
        ╔════════════════════════════════════════════╗
        ║       API PAYLOADS  (jo bheja jaata hai)   ║
        ╚═══════════════════┬════════════════════════╝
                            ↓
        ╔════════════════════════════════════════════╗
        ║   PLATFORM OBJECTS  (jo ban jaata hai)     ║
        ║   Strategy → Campaigns → Ad Groups         ║
        ╚════════════════════════════════════════════╝
```

## 🔴 Zaroori rule — kya kahan se aana chahiye

```
┌──────────────────┬────────────────────────┬──────────────────────┐
│  Kya             │  Kahan se AANA chahiye │  KABHI NAHI          │
├──────────────────┼────────────────────────┼──────────────────────┤
│  Numbers         │  VOW API               │  Spec ya code se     │
│  (CPM, reach,    │                        │  (stale ho jaayega)  │
│   fee rate)      │                        │                      │
├──────────────────┼────────────────────────┼──────────────────────┤
│  Rules           │  Specification         │  API se              │
│  (fee logic,     │  (registry)            │  (wo rules nahi      │
│   tier rules)    │                        │   deta)              │
├──────────────────┼────────────────────────┼──────────────────────┤
│  Shabd           │  Specification         │  LLM se generate     │
│  (agent kya      │  (phrases)             │  (bahak sakta hai)   │
│   bolta hai)     │                        │                      │
├──────────────────┼────────────────────────┼──────────────────────┤
│  Trader ne kya   │  Conversation          │  Assume karna        │
│  kaha            │                        │                      │
└──────────────────┴────────────────────────┴──────────────────────┘
```

## Ek line ka example — teen source ek saath

Agent bolta hai:

```
"Netflix - £31.50 CPM (30s) - third-party, pre-curated (no reach forecast)"
```

| Hissa | Kahan se |
|---|---|
| `Netflix` | ✅ VOW API — deal name |
| `£31.50` | ✅ VOW API — deal_price_amount |
| `30s` | ✅ VOW API — ad_lengths |
| `third-party, pre-curated` | ✅ **Specification** — tier label |
| `no reach forecast` | ✅ **Specification** — tier rule |
| Line ki shape | ✅ **Specification** — template |

**Teen source, ek line. Aur koi hissa agent ne khud nahi banaya.**

---
---

# 5. POORA SEQUENCE — ek diagram me

```
 TRADER              AGENT                          VOW APIs
   │                   │                                │
   │                   │─── GET /admin/advertiser/{id}/─→│  TURN 0
   │                   │←─── defaults + is_locked ───────│
   │                   │                                │
   │── brief ─────────→│                                │  TURN 1
   │                   │ classify (LLM, closed enum)    │
   │                   │ extract (LLM, structured)      │
   │                   │ [GATE: basics poore?]          │
   │                   │                                │
   │                   │─── GET check_market_has_aud ──→│
   │                   │─── GET check_market_has_assets→│
   │                   │─── GET inventory-sources/ ────→│
   │                   │─── GET check_name_uniqueness ─→│
   │                   │←─── pre-flight results ────────│
   │                   │                                │
   │                   │─── GET /deals/ ───────────────→│
   │                   │─── GET /rates/ctv/{market}/ ──→│
   │                   │←─── 83 deals + rate card ──────│
   │                   │ match: market·duration·channel │
   │                   │ classify tier                  │
   │                   │                                │
   │                   │ prompt likho                   │
   │                   │─── POST /audience-sets/suggest→│
   │                   │←─── {"id": "abc"} ─────────────│
   │                   │─── GET .../suggest/abc/ ──────→│
   │                   │←─── flat list, 40+ segments ───│
   │                   │─── GET /contextual-targeting/fees→│
   │                   │←─── rate ──────────────────────│
   │                   │ 3 groups banao                 │
   │                   │ [GATE: choice pending] STOP    │
   │←── 3 messages ────│                                │
   │                   │                                │
   │── "balanced" ────→│                                │  TURN 2
   │                   │ classify (rules only)          │
   │                   │ apply choice                   │
   │                   │─── POST /strategies/reach-forecast→│
   │                   │←─── reach 233,803 ─────────────│
   │                   │ frequency = 860716/233803      │
   │                   │ [reach theek? → repair loop]   │
   │←── forecast ──────│                                │
   │                   │                                │
   │── "create it" ───→│                                │  TURN 3
   │                   │ DRAFT → FINALISED              │
   │                   │─── POST /api/strategies/ ─────→│  TURN 4
   │                   │←─── 201, VMA2026368 ───────────│
   │←── card ──────────│                                │
   │                   │                                │
   │                   │  ┌── PARALLEL ────────────┐    │  PHASE C
   │                   │  │ POST targeting/        │───→│
   │                   │  │ PATCH flight-ranges/   │───→│
   │                   │  │ POST gen_upload_urls/  │───→│
   │                   │  │ POST register/         │───→│
   │                   │  │ [WAIT: approval]       │    │
   │                   │  │ POST asin-validation/  │───→│
   │                   │  │ PATCH /strategies/{id}/│───→│
   │                   │  │ GET credits/summary/   │───→│
   │                   │  └────────────────────────┘    │
   │                   │                                │
   │                   │ [JOIN: 8 prerequisites]        │  PHASE D
   │                   │─── POST .../set_status/ ──────→│
   │                   │ monitor sync (fail ho sakta)   │
   │←── live ──────────│                                │
```

## Tool calls ka hisaab

| Turn | Tool calls | LLM calls |
|---|---|---|
| 0 — session start | 1 | 0 |
| 1 — brief | 8 | 2 (classify + extract) |
| 2 — audience choice | 1 | 0 (rules ne pakda) |
| 3 — finalise | 0 | 1 (classify) |
| 4 — create | 2 | 1 |
| Phase C | 7+ | 0 |
| Phase D | 1 | 0 |
| **Total** | **~20** | **~4** |

**Manual me trader ~25 clicks karta hai. Agentic me ~20 API calls hoti hain, par trader sirf 3 messages likhta hai.**

---
---

# 6. Field matrix — required vs optional (Agentic Way)

## 🟢 Trader se PUCHNA hai — sirf 4

| Field | Kyun | Na de to |
|---|---|---|
| **Market** | Deals, currency, rate card, categories — sab market par | 🔴 Ruko, pucho |
| **Budget** | CPM ke saath milkar impressions banata hai | 🔴 Ruko, pucho |
| **Flight dates** | Forecast ka input | 🔴 Ruko, pucho |
| **Creative durations** | Kaunsi deals, kaunsa CPM | 🟠 Ruko, pucho — **par contested (D13)** |

**Aur wo bhi tab jab brief me na ho.**

## 🟡 CHOICE ke roop me — 2

| Field | Kaise |
|---|---|
| **Audience** | 3 options dikhao — ya decline. **Default NA lo** |
| **KPI target value** | Sirf jab KPI = frequency ho (2–5) |

## 🔴 KABHI NAHI puchna — 11

| Field | Kahan se | Source |
|---|---|---|
| Strategy name | Agent banayega | `GENERATED` |
| Primary currency | Advertiser profile | `ADVERTISER` |
| Goal | Awareness default — **par badal sakte hain** | `ADVISED` |
| Formats | CTV me `streaming_tv` | `CONSTANT` |
| Product categories | Advertiser, ya brief se | `ADVERTISER`/`INFERRED` |
| Frequency cap | Advertiser profile | `ADVERTISER` |
| Selling location | Advertiser profile | `ADVERTISER` |
| Base bid | Deal ke CPM se — **par contested (D3)** | `DERIVED` |
| ASINs | Baad me, tracking step par | `LATER` |
| Deals | Agent **match** karega | `MATCHED` |
| Location / device | Default bhara aayega | `DERIVED`/`ADVERTISER` |

## Manual vs Agentic — inputs ka farak

```
MANUAL                          AGENTIC
────────────────────────       ────────────────────────
Step 1:  8 fields              Brief:  1 message
Step 2:  7 fields                       ↓
Step 3:  deal ticks            Choice:  1 word ("balanced")
Step 4:  audience ticks                 ↓
Step 5:  asset ticks           Confirm: 1 word ("create")
Step 6:  review + click
────────────────────────       ────────────────────────
~25 inputs                     3 inputs
```

---
---

# 7. Decision points — har branch

## Branch 1 — Intent gate (turn ke shuru me)

```
                    message aaya
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     BRIEF          SELECTION      baaki sab
        │                │                │
        ↓                ↓                ↓
   extract_fields   apply_choice      registry se
        │                │             jawab do
        │                │                │
        ↓                ↓                ↓
    plan badla      plan badla      plan CHHUA NAHI
```

## Branch 2 — Basics gate

```
        market · budget · dates · durations
                         │
              ┌──────────┴──────────┐
          sab mile              kuch missing
              ↓                     ↓
        deals match karo    🔴 SAB EK SAATH pucho
                                    ↓
                              TURN KHATAM
```

🔴 **Ek-ek karke na pucho** — char round trip = wahi wizard.

## Branch 3 — Inventory tier fork

```
                   deals mile
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
 AMAZON_OWNED    3P_PRECURATED    3P_NEEDS_CURATION
 (Prime, Twitch)  (Netflix, Hulu)     (Disney+)
      │                 │                 │
      ↓                 ↓                 ↓
 deal ready        deal ready      🔴 DEAL NAHI HAI
 reach forecast    NO forecast     rate card se daam
 milega            milega          curation capture karo
      │                 │                 │
      └─────────────────┼─────────────────┘
                        ↓
              🔴 Agent ko BATANA hai ki
                 kaunse hisse ka reach
                 forecast nahi hoga
```

## Branch 4 — Audience choice

```
              3 options dikhaye
                     │
    ┌────────┬───────┼───────┬──────────┐
    │        │       │       │          │
 narrow  balanced  wide   "none"    "ok" (ambiguous)
    │        │       │       │          │
    └────────┴───────┘       │          ↓
             ↓               ↓     🔴 DOBARA PUCHO
        forecast karo   run of service   default NA LO
                        no data fee           │
                        no widen lever        ↓
                             │           TURN KHATAM
                             ↓
                        forecast karo
```

## Branch 5 — Repair loop

```
              forecast aaya
                     │
        reach target se kam hai?
                     │
         ┌───────────┴───────────┐
        NAHI                    HAAN
         ↓                       ↓
    aage badho        🔴 max_reach check karo
                               │
                    ┌──────────┴──────────┐
              est == max              est < max
                    ↓                     ↓
         "inventory khatam hai"    lever dhundo
          — koi lever kaam                │
            nahi karega          ┌────────┴────────┐
                                 │  audience hai?  │
                                 │  bid lagta hai? │
                                 │  device locked? │
                                 │  geo narrow hai?│
                                 └────────┬────────┘
                                          ↓
                                 lever mila → apply → re-forecast
                                 lever nahi → 🔴 SAAF BOLO
                                              "kya use nahi kar paya"

              🔴 Max 2-3 attempts, phir report karo
```

## Branch 6 — Activation join node

```
        Phase C ke saare branch khatam?
                     │
        8 prerequisites check:
          creatives uploaded (per duration)
          creatives approved (per channel)  ← 🔴 BLOCKED, D10
          targeting written
          budget allocated
          ad tag registered   (off-Amazon ho to)
          ASINs attached      (on-Amazon ho to)
          conversions chosen
          credit sufficient
                     │
         ┌───────────┴───────────┐
     sab theek              kuch missing
         ↓                       ↓
     ACTIVATE          🔴 SAARE missing EK SAATH batao
         ↓                  (ek-ek karke nahi)
   monitor sync
```

---
---

# 8. Failure paths — kya galat ho sakta hai

## Har step par kya fail ho sakta hai

| Kahan | Kya fail hoga | Agent kya kare |
|---|---|---|
| **Turn 0** | Advertiser API fail | 🔴 Ruko — advertiser context ke bina kuch nahi (fail closed) |
| **Extract** | LLM fail | Pattern matching se fallback. Brief refuse **na karo** |
| **Classify** | LLM fail | `BRIEF` maan lo — asli brief refuse karna zyada bura hai |
| **Name check** | Naam already hai | `_v2` laga kar dobara check. **Rukо nahi** |
| **Pre-flight** | Market me audiences nahi | Batao ki forecast limited hoga |
| **Deals** | Ek bhi deal match nahi | Duration widen ya genre drop ka propose karo |
| **Deals** | CPM = 0 (ek deal hai aisi) | 🔴 Division by zero guard — skip karo |
| **Deals** | Currency mismatch (USD deal, GBP plan) | 🔴 Ek currency me convert karo, phir hisaab |
| **Suggest** | Async timeout | Batao ki suggestion aa raha hai, ya baad me |
| **Forecast** | Reach bahut kam | Repair loop — par max 2-3 attempts |
| **Forecast** | 3P inventory hai | 🔴 Reach **invent na karo**. Saaf bolo |
| **Create** | 400 / validation error | Kaunsi field galat thi wo batao |
| **Create** | 201 mila | 🔴 **Ye "live" nahi hai** — Paused hai, sync pending |
| **Sync** | `CAMPAIGN_SYNC_ISSUES` | 🔴 Failure batao. Success **na batao** |
| **Approval** | Creative REJECTED | Reason batao, naya creative maango |
| **Credit** | Balance kam | Top-up ka propose karo |
| **Activate** | Prerequisite missing | **Saare** missing ek saath batao |

## 🔴 Char golden rules failure me

```
1. Advertiser context nahi  →  RUKO. Kabhi default advertiser na lo.
                               Galat tenant ka data dikhna sabse bura hai.

2. LLM fail                 →  DEGRADE karo, refuse na karo.
                               Brief parse karne ki koshish karo.

3. Reach forecast nahi      →  BOLO ki nahi hai. Number invent na karo.
                               "Plausible" jhooth se admitted gap behtar hai.

4. Kuch verify nahi kar     →  BOLO. "Maine kiya par dikha nahi sakta"
   sakte                       se behtar kuch nahi hai.
```

---
---

# 9. Do flows ka aakhri comparison

## Ek table me sab

| | **MANUAL** | **AGENTIC** |
|---|---|---|
| **Entry point** | "New Strategy" button | Ek message |
| **Trader inputs** | ~25 (8+7+ticks+ticks+ticks) | **3** |
| **Screens/turns** | 6 screens | 2–3 turns |
| **Deals** | 83 me se tick | Agent **match** karta hai |
| **Deal ID dikhta hai?** | ✅ Haan, poora naam | ❌ Nahi — sirf channel + CPM |
| **Audiences** | 15 me se tick | 3 options, ya decline |
| **Assets** | 4 me se tick | Filter + suggest |
| **Currency** | Dropdown (EUR pehle se) | Advertiser se, **puchte nahi** |
| **Goal** | 3 cards | Awareness default, **advice ke saath** |
| **Base bid** | Manual, **required** | Deal se derive — **contested** |
| **Forecast** | Step 6 par apne aap | Audience choose hone ke baad |
| **Targeting** | Creation ke **baad** (Locations) | Creation ke **baad** (same) |
| **Budget split** | Platform khud 50/50 | Platform khud — agent explain karta hai |
| **Validation** | Next button block hota hai | Gate + saaf sawaal |
| **Kya galat ho sakta** | Trader galat deal chun le | Agent galat match kare |
| **Time** | ~10 minutes | ~30 seconds |

## Teen cheezein jo agentic way me BEHTAR hain

```
1. TRADER KO KAM SOCHNA PADTA HAI
   83 deals me se chunna ek expert ka kaam hai.
   "Prime Video par chalao" bolna aasan hai.

2. AGENT HONEST HO SAKTA HAI
   Manual me screen sirf number dikhata hai.
   Agent bol sakta hai "ye floor rate hai, actual zyada ho sakta hai"
   ya "is hisse ka reach forecast nahi milega".

3. GALTI PEHLE PAKDI JAATI HAI
   Manual me trader step 5 tak jaake pata karta hai ki
   assets nahi hain. Agent step 1 me pre-flight se pata kar leta hai.
```

## Teen cheezein jo agentic way me MUSHKIL hain

```
1. DEAL MATCHING KA DATA NAHI HAI
   channel aur inventory_tier fields deal par EXIST NAHI karti.
   Agent ko deal ka NAAM parse karna padega — jo
   Zero-Hallucination principle ke khilaf hai.        → D4

2. FORECAST AUDIENCE NAHI LETA
   Platform ka forecast sirf 4 inputs leta hai.
   To "audience widen karke re-forecast" — wo capability
   product me hai hi nahi. Nayi banani padegi.        → D7

3. TARGETING CREATION KE BAAD HOTI HAI
   Trader ko lagta hai wo ek hi baat kar raha hai,
   par API do jagah split karti hai.                  → D1
```

---

## Ek line me poora farak

> **Manual way me trader FORM bharta hai aur khud faisle leta hai.
> Agentic way me trader BAAT karta hai aur agent faisle propose karta hai —
> par har number VOW ke API se aata hai, aur har rule specification se.**

---

**Ye document `staging.vowmade.dev` par 4 August 2026 ki verification se bana hai — 9 screens, 17 APIs, test strategy `VMA2026368`.**

**Poora specification `Strategy_Schema_v4.0_FINAL.md` me hai. Concepts `docs/deals_and_audiences_explained.md` me. Ye document sirf FLOW dikhata hai.**
