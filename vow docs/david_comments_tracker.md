# David Moss — Review Comments Tracker
### `Strategy Schema documentation v2.0` · Confluence · 28 comments

> **Confluence page:** `vowmade.atlassian.net/wiki/spaces/VOWAgent/pages/589824005/Strategy+Schema+documentation+v2.0`
> **Reviewer:** David Moss (Manager)
> **Author:** Kareem
> **Total comments:** 28
>
> ## Kaam ka tarika
> 1. **Pehle sab 28 comments samajhna** — koi reply nahi, sirf deep understanding
> 2. Har comment ka: kya kaha · kya matlab · kya requirement · kahan fix chahiye
> 3. **Sab samajh lene ke baad** — document me notes daalna + replies post karna
>
> ## Companion file
> `full_strategy_schema_registery_mastery.md` — poore document ki mastery guide. Jab kisi comment me koi concept samajh na aaye, wahan se refer karo.

---

# 📊 STATUS BOARD

| # | Location (section) | Ek line me | Severity | Understood | Note drafted | Replied |
|---|---|---|---|---|---|---|
| **1** | §2.3 Tier table → 3P pre-curated → Audiences | 3P targeting ek option nahi, **choice** hai — aur wo **deal se bandhi** hai | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **2** | §2.4 Audience Set Profiles → "added fee consequence" | Fee **profile par nahi, data source par** depend karti hai. Compound nahi hoti | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **3** | §3 Comparison table → "Budget split ➕ NEW" | Budget split **Optional** hai, Required nahi — par accurate CPM ke liye preferred | 🟡 MED | ✅ | ✅ draft | ⬜ |
| **4** | §3 Comparison table → "mandatory" (Audiences) | Audiences **Optional** hai — "optional again". Suggestion ✅, majboori ❌ | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **5** | §3 Comparison table → "Targeting ➕ NEW" | Audiences **targeting ka hissa** hai. **Default lagao, phir refine** — khaali form nahi | 🔴🔴 V.HIGH | ✅ | ✅ draft | ⬜ |
| **6** | Step 1 → v1.1.0 field list (poori) | Kai fields **non-CTV** hain. Simplify karo aur **jawab khud nikalo** ("imply answers") | 🔴🔴 V.HIGH | ✅ | ✅ draft | ⬜ |
| **7** | Step 1 → Strategy name → "Required" | Naam **brief se auto-generate** ho sakta hai | 🟡 MED | ✅ | ✅ draft | ⬜ |
| **8** | Step 1 → Target markets → "Multi-select" | **Multi-market support karenge?** Flow par kya asar — sab dobara? *(SAWAAL, correction nahi)* | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **9** | Step 1 → Primary currency → "Required" | Single market me **market ki currency use karo** — poochho mat | 🟡 MED | ✅ | ✅ draft | ⬜ |
| **10** | Step 1 → KPI (field) | 🔴 **MISSING FIELD** — frequency ke liye target value (1–5) chahiye | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **11** | Step 1 → Market budgets → "Table" | Single market me ek number · **Type column 4 kaam kar raha hai** | 🟡 MED | ✅ | ✅ draft | ⬜ |
| **12** | Step 1 → Base bids → "Required" | CTV me base bid **bekaar** (CPM deal me fixed) → 🔴 **repair loop ka lever toot gaya** | 🔴🔴 V.HIGH | ✅ | ✅ draft | ⬜ |
| **13** | Step 1 → Frequency cap → "Optional" | **Advertiser-level default** hota hai → 🔴 poora missing concept | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **14** | Step 1 → Formats → "Required" | **Hamesha `streaming_tv`** · Prime Video ek **provider** hai, format nahi | 🟡 MED | ✅ | ✅ draft | ⬜ |
| **15** | Step 1 → Product categories → "Required for video" | **Advertiser default** ya brief se imply → advertiser defaults ka **2nd confirmation** | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **16** | Step 1 → Selling location → "Required" | **"Can leave out"** — Step 1 se hatao | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **17** | Step 1 → Product ASINs → "Conditional" | **"Comes later"** → #16 ke saath **Open Question #1 SOLVE** ✅ | 🟡 MED | ✅ | ✅ draft | ⬜ |
| **18** | Step 2 → Selected deals → "Checkbox table" | 🔴🔴 **Deals table HATAO** — agent brief se match karega · trader ko sirf **CPM** dikhega | 🔴🔴 V.HIGH | ✅ | ✅ draft | ⬜ |
| **19** | Step 4 constraints → "Netflix/Disney" | **Amazon audiences 3P par BHI lagti hain** — "only apply to" galat hai · ⚠ mera Note 1 ka explanation over-claimed tha | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **20** | Step 4 ⚠ Open question → `bundles.narrow/balanced/broad` | ✅ **OQ-2 RESOLVED** — bundles shape API me **nahi hai** · 3 profiles **agent-side construct** ban gaye | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **21** | Step 5 Targeting → Location → "Optional" | **Market country par default** hoti hai — khaali nahi rehti | 🟡 MED | ✅ | ✅ draft | ⬜ |
| **22** | Step 5 Targeting → Device type → "Optional" | **Advertiser level par set** hota hai · 🔴 "CTV format ≠ CTV device" · ⚠ mera Note 21 galat tha | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **23** | Step 7 → "Plan Approval" (step ka naam) | 🔄 **SIMPLIFIED** — sirf status change · manager approval hataya · 🔴 `interrupt()` ki zaroorat khatam · **pehla scope-reduction comment** | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **24** | Step 8 → API calls → `api/strategies` | ⚠ Shayad **`simple-strategies`** endpoint hai → 🔴 **poora CTV endpoint family** ka ishara · Note 17 ka evidence kamzor | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **25** | Step 9 → Click-through URL → "Required" | **Optional for streaming TV** — ✅ mera flagged gap band ho gaya | 🟡 MED | ✅ | ✅ draft | ⬜ |
| **26** | Step 10 → poora approval status table | Per-channel ek status ✅ (mera fix confirm) · par **channel list KHULI hai** (Paramount, Channel 4) · ✅ naming resolve: "channel" | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **27** | Step 11 → "Tracking Setup" (step ka naam) | **"No order necessary"** — 🔴🔴 flow **linear chain se PARALLEL BRANCHES** ban jaata hai · document ne **sabse lamba kaam aakhir me** rakha tha | 🔴 HIGH | ✅ | ✅ draft | ⬜ |
| **28** | Step 11 → ⚠ Open question → "Confirm with client" | 🎉 **"No — they can be updated after creation"** · document ka **sabse dohraya gaya OQ SOLVE** · aur ye **#27 ka mechanism** hai | 🟡 MED *(par load-bearing)* | ✅ | ✅ draft | ⬜ |
| 19 | | | | ⬜ | ⬜ | ⬜ |
| 20 | | | | ⬜ | ⬜ | ⬜ |
| 21 | | | | ⬜ | ⬜ | ⬜ |
| 22 | | | | ⬜ | ⬜ | ⬜ |
| 23 | | | | ⬜ | ⬜ | ⬜ |
| 24 | | | | ⬜ | ⬜ | ⬜ |
| 25 | | | | ⬜ | ⬜ | ⬜ |
| 26 | | | | ⬜ | ⬜ | ⬜ |
| 27 | | | | ⬜ | ⬜ | ⬜ |
| 28 | | | | ⬜ | ⬜ | ⬜ |

**Progress: 28 / 28 — 🎉 REVIEW COMPLETE**

> Sab 28 comments samjhe ja chuke hain. Har ek ka **document note** aur **reply** draft ho gaya hai.
> Ab teen kaam bache hain — neeche **"AB KYA KARNA HAI"** section me.

> ## 🎉 MILESTONE — DO Open Questions RESOLVED
>
> **OQ-1 (ASIN timing) — via #16 + #17.** Document ka sabse bada ⚠ (do baar likha gaya tha).
> **Answer: Option A** — selling location aur ASIN dono Step 1 se hatao, Step 11 me collect karo, `PATCH` se attach karo.
> *(Note: is tracker me pehle Option B recommend kiya gaya tha — David ne ulta answer diya. Detail #17 me.)*
>
> **OQ-2 (suggest endpoint shape) — via #20.**
> **Answer: `bundles.narrow/balanced/broad` support NAHI hai.** 3 profiles ab ek **agent-side construct** hain.
> *(Par ek naya BLOCKING sawaal khula: to API asal me kya deta hai? Detail #20 me.)*

> ## ⚠ SELF-CORRECTION LOG
> Jahan is tracker ka pichhla analysis galat nikla — saaf record:
>
> | Kahan | Kya galat tha | Kisne theek kiya |
> |---|---|---|
> | **Note 1** — 3P targeting ka explanation | Maine likha tha *"3P publishers viewer identity nahi dete, isliye Amazon audience targeting IMPOSSIBLE hai"* — ye **over-claim** tha. Amazon audiences 3P par kaam karti hain | **#19** |
> | **Note 1** — OQ-1 ka recommendation | Maine **Option B** (ASIN Step 1 me rakho) recommend kiya tha | **#16 + #17** (David ne Option A chuna) |
> | **Note 21** — Targeting default table | Device type ko **🔒 FIXED** mark kiya tha (socha CTV module = Connected TV). Wo **🏢 ADVERTISER** hai — advertiser ke hisaab se badalta hai | **#22** |
> | **Note 17** — OQ-1 ka **evidence** | `product_asins: []` wale example ko saboot bataya tha — par wo `POST /api/strategies/` ka example tha. Agar `simple-strategies` use karna hai to wo applicable nahi. ⚠ **Conclusion sahi hai, justification galat endpoint ka tha** | **#24** |
>
> 💡 Reply me ye saaf maanna hai — apni galat wajah defend nahi karni.
>
> ⚠ **Aur ek farak dhyan me rakho:** Note 17 wala case "conclusion galat" nahi hai — "evidence kamzor" hai. Reply me ye distinction saaf karni chahiye, warna lagega ki poora resolution galat tha.

> ## ✅ RESOLVED — naming question (via #26)
> `"channel"` vs `"channels"` vs `provider` — teen naam, ek cheez. **Jawab: "channel".**
> David ne teen baar "channel" use kiya (#18, #26, aur rate card me "channels"). `provider` sirf **hamare** schema me hai.
> → `SelectedDealSchema.provider` → **`channel`** rename karo · aur `ChannelTypeEnum` (jo `dsp`/`sponsored` ke liye hai) ko rename karo taaki collision na ho.

> **📌 Note on numbering:** Ek screenshot me kai comments hote hain. Unhe alag-alag number diya gaya hai, kyunki total 28 hain.
> · `3 comemnt.png` → **#3, #4, #5** (Budget split · mandatory · Targeting) — sab §3 comparison table par
> · `comment next.png` → **#6, #7, #8, #9** (v1.1.0 field list · Strategy name · Target markets · Primary currency) — sab Step 1 par
> · `next comm.png` → **#10, #11, #12, #13** (KPI · Market budgets · Base bids · Frequency cap) — sab Step 1 field matrix par
> · `next comm.png` (2nd batch) → **#14, #15, #16, #17** (Formats · Product categories · Selling location · Product ASINs) — sab Step 1 field matrix par
> · `next comm.png` (3rd batch) → **#18** (Selected deals) — **Step 2** par · 🔴 pehla comment jo Step 1 se bahar hai (§2/§3 ke baad)
> · `next comm.png` (4th batch) → **#19, #20, #21** (Netflix/Disney constraint · bundles shape · Location) — **Step 4 aur Step 5** par
> · `next comm.png` (5th batch) → **#22** (Device type) — **Step 5** par
> · `next comm.png` (6th batch) → **#23** (Plan Approval step title) — **Step 7** par · 🔴 pehla **scope-reduction** comment
> · `next comm.png` (7th batch) → **#24, #25, #26** (api/strategies · Click-through URL · Step 10 approval table) — **Step 8, 9, 10** par
> · `next comm.png` (8th batch) → **#27** (Tracking Setup step title) — **Step 11** par · 🔴🔴 flow ka **structure** badalta hai
> · `next comm.png` (9th batch) → **#28** ("Confirm with client" on the ⚠ open question) — **Step 11** par · 🎉 **AAKHRI comment**

### Severity ka matlab
| | |
|---|---|
| 🔴 **HIGH** | Missing feature, missing schema field, ya flow badalta hai — code likhne se pehle theek hona zaroori |
| 🟡 **MEDIUM** | Inconsistency ya adhoori baat — theek karna chahiye par flow nahi badalta |
| 🟢 **LOW** | Wording / editorial — jaldi fix ho jaayega |

---
---

# 🗨️ COMMENT #1

## 📍 Location

| | |
|---|---|
| **Section** | `2.3 Deal Types` → `➕ NEW — Three inventory tiers` |
| **Element** | Tier comparison table |
| **Row** | `3P pre-curated` (Netflix, Hulu, others) |
| **Column** | `Audiences` |
| **Highlighted text** | **"Their own targeting (adds CPM)"** |

## 💬 David ne exactly kya likha

> *"For 3P there's often a choice whether to use Amazon's targeting (may be limited in functionality i.e. only device) or to apply the targeting at the inventory source / SSP. Which is then specific to the deal that is chosen or curated."*

## 🔍 Line-by-line breakdown

| David ka hissa | Plain matlab |
|---|---|
| *"For 3P there's often a **choice**"* | 🔴 Netflix/Hulu ke liye **do raaste hote hain**, ek nahi |
| *"whether to use **Amazon's targeting**"* | **Raasta 1** — Amazon ki targeting Netflix par bhi laga sakte ho |
| *"(may be **limited in functionality** i.e. **only device**)"* | Par Amazon ki targeting wahan **poori kaam nahi karti** — sirf "device" jaisa basic level milta hai |
| *"or to apply the targeting at the **inventory source / SSP**"* | **Raasta 2** — targeting Netflix ki **apni taraf** lagao |
| *"Which is then **specific to the deal** that is chosen or curated"* | 🔴 Aur wo targeting **deal ke andar hi baithi** hoti hai — deal chuni, targeting bhi chun li |

## 📖 Naya word: SSP

**SSP = Supply Side Platform** — DSP ka jodidaar.

```
        DSP                                    SSP
   Demand Side Platform              Supply Side Platform
   = KHARIDNE walon ka software      = BECHNE walon ka software
   = Amazon DSP                      = Netflix/Hulu ka apna ad system
   = "mujhe ad slot chahiye"         = "mere paas ad slot hai"
             │                                  │
             └────────── beech me sauda ────────┘

Chain: Nike ka trader → Amazon DSP → Netflix ka SSP → TV screen
```

**David ka point:** targeting **do jagah** lag sakti hai —
- **DSP side** (Amazon ki taraf) → Amazon apni targeting lagayega
- **SSP side** (Netflix ki taraf) → Netflix apni targeting lagayega

## ❌ Document abhi kya kehta hai vs ✅ Reality

### Document abhi (galat — bahut absolute)
```
┌─────────────────┬──────────────────────────────────┐
│ 3P pre-curated  │ Their own targeting (adds CPM)   │
└─────────────────┴──────────────────────────────────┘
                    ↑
        Padhne se lagta hai: "SIRF Netflix ki targeting
        possible hai, koi choice nahi"
```

### Reality (David ke mutabik)
```
3P inventory (Netflix/Hulu) par targeting ke DO raaste:

┌─────────────────────────────────────────────────────────────┐
│  RAASTA 1: Amazon's targeting                               │
│  • Amazon DSP ki taraf se lagti hai                         │
│  • ⚠ LIMITED — "may be limited in functionality"            │
│  • Example: sirf DEVICE targeting (Connected TV/Mobile/…)    │
│  • Amazon ki 3,400 audience segments? ❌ shayad nahi         │
├─────────────────────────────────────────────────────────────┤
│  RAASTA 2: Inventory source / SSP targeting                 │
│  • Netflix/Hulu ki taraf se lagti hai                       │
│  • ✅ Zyada powerful (unka apna data)                        │
│  • 💰 CPM badha deti hai                                     │
│  • 🔴 DEAL KE ANDAR BAITHI HOTI HAI                          │
│    ("specific to the deal that is chosen or curated")        │
└─────────────────────────────────────────────────────────────┘
```

## 🔴 Sabse gehra point — "specific to the deal that is chosen or curated"

Ye David ke comment ka **sabse important hissa** hai, aur ye **poora flow badalta hai.**

### Do case

```
CASE A — "chosen" deal (3P pre-curated, jaise Netflix)
  Deal pehle se bani hui hai, aur uske andar targeting PEHLE SE hai.
  Example: "Netflix | Drama | UK - 30 | 18-34 age"
                      ↑              ↑
                   genre          targeting — DEAL ME BUILT-IN

  → Tum deal chunte ho, targeting AUTOMATICALLY aa jaati hai
  → Alag se badal nahi sakte

CASE B — "curated" deal (3P needs curation, jaise Disney+)
  Deal abhi banti hi nahi. VOW baad me banayegi.
  → Targeting ki farmaish CURATION KE WAQT deni padegi
  → Yahi wo "Curation: targeting prefs" field hai (Step 2 me)!
```

### Flow me kya problem aati hai?

```
Document ka current flow:
  Step 2: CTV INVENTORY  ← deals chuno
     ↓
  Step 5: TARGETING      ← targeting lagao (location, device, exclusions…)

→ Document maanta hai: pehle deal, PHIR targeting. Do alag steps.
```

**Par David keh raha hai — 3P ke liye ye SAATH me hota hai:**

```
Agar SSP targeting deal ke andar baithi hai, to:
Step 2 me deal chunte waqt HI targeting chun li gayi!

┌──────────────────────────────────────────────────────────────┐
│  AMAZON portion   →  Step 5 me targeting lagegi ✅            │
│  3P portion       →  targeting Step 2 me hi tay ho gayi ⚠     │
│                      (deal ke saath)                          │
└──────────────────────────────────────────────────────────────┘
```

**Yaani Step 2 aur Step 5 3P ke liye JUD jaate hain.** Ye ek asli architectural baat hai jo document me nahi hai.

## 🎯 David ne ye comment kyun kiya (uski niyat)

### Wajah 1 — Document ne ek CHOICE ko FACT bana diya
```
Document:  "Their own targeting" = ek hi raasta hai
Reality:   do raaste hain, trader ko chunna hai

→ Agar agent ye maan le ki koi choice nahi hai, to wo trader se
  poochhega hi nahi. Ek poora feature gayab.
```

### Wajah 2 — Ek trade-off chhup gaya
```
Amazon targeting  →  limited (sirf device?) par shayad sasti
SSP targeting     →  powerful par CPM badhati hai

→ Ye ek ASLI trade-off hai jo trader ko dikhna chahiye
→ Bilkul waise jaise "effective CPM" dikhana zaroori tha
```

### Wajah 3 — Schema me ek field missing hai
```
SelectedDealSchema me:
  inventory_tier    ✅
  provider          ✅
  genre             ✅
  ad_lengths        ✅
  deal_type         ✅
  targeting_source  ❌  ← YE MISSING HAI
```

## 🔧 Impact — kahan-kahan fix chahiye

| # | Jagah | Abhi kya likha hai | Kyun fix chahiye |
|---|---|---|---|
| **1** | **§2.3 tier table**, `Audiences` column *(comment yahin hai)* | "Their own targeting (adds CPM)" | Choice dikhani hai, ek option nahi |
| **2** | **Step 4 (Audiences)**, Constraints list | *"Amazon audiences only apply to Amazon-owned inventory. For Netflix/Disney, their own targeting applies"* | 🔴 **Yahi galti dobara hai** — same absolute statement |
| **3** | **Step 5 (Targeting)** | 3P ke liye targeting kahan lagti hai — kuch nahi likha | Deal-bound targeting ka zikr chahiye |
| **4** | **§5 `SelectedDealSchema`** | `targeting_source` field nahi hai | Choice ko schema me capture karna hai |
| **5** | **§5 `TargetingSchema`** | Sab fields sabhi tiers ke liye lagti dikhti hain | Scope clarify karna — Amazon portion only |

## ✍️ DOCUMENT ME DAALNE WALA NOTE (draft — baad me paste karenge)

> **📝 NOTE — Targeting for 3P inventory (David Moss, review comment)**
>
> The table above says *"Their own targeting (adds CPM)"* for 3P tiers. This is **incomplete** — it presents one option where there are actually **two**. Corrected understanding:
>
> For 3P inventory (Netflix, Hulu, Disney+), targeting can be applied in **two places**, and this is a **choice the trader makes**:
>
> | | **Option A — Amazon's targeting** | **Option B — Inventory source / SSP targeting** |
> |---|---|---|
> | **Applied at** | Amazon DSP side | The publisher's own SSP |
> | **Capability** | ⚠ **May be limited** — e.g. device-level only | Fuller, publisher-specific |
> | **Cost** | *(TBC — likely no added data fee for device-level)* | **Adds CPM** |
> | **When chosen** | Can be applied at Step 5 (Targeting) | 🔴 **Bound to the deal** — chosen at deal selection (3P pre-curated) or specified during curation (3P needs curation) |
>
> **Flow consequence:** For the 3P portion, targeting is **not** a free-standing Step 5 decision — it is coupled to Step 2 (inventory). Either the chosen deal already carries its targeting, or the targeting preference must be captured as part of the curation request. Step 5's targeting fields therefore apply in full only to the **Amazon-owned portion**.
>
> **Agent behaviour required:** When 3P inventory is selected, the agent must surface the choice with its trade-off — e.g. *"For the Netflix portion you can either use Amazon's targeting (device-level only) or Netflix's own targeting, which is richer but adds to the CPM. Which do you prefer?"*
>
> **Schema additions required:**
> ```python
> class TargetingSourceEnum(str, Enum):
>     """➕ NEW — where targeting is applied (per David's review)"""
>     AMAZON_DSP = "AMAZON_DSP"              # limited on 3P (e.g. device only)
>     INVENTORY_SOURCE = "INVENTORY_SOURCE"  # SSP-side; deal-bound; adds CPM
>
> # SelectedDealSchema:
>     targeting_source: Optional[TargetingSourceEnum] = Field(
>         None, description="Where targeting is applied for this deal")
>     source_targeting_cpm_uplift: Optional[str] = Field(
>         None, description="Added CPM if SSP targeting is used")
> ```
>
> **Also corrected in:** Step 4 constraints (same absolute phrasing repeats there), Step 5 (scope of targeting fields per tier).

## 💬 REPLY DRAFT (baad me post karenge)

> Thanks David — really useful correction.
>
> I had written this as if SSP targeting is the only option for 3P. Now clear: it's a **choice** — Amazon's targeting (limited, e.g. device only) or the inventory source's own targeting (richer, but adds CPM).
>
> Your last line is the bigger point — SSP targeting is **tied to the deal**. So for 3P, targeting is decided when the deal is chosen or curated, not later at the Targeting step. I'll document that, and note that the Targeting step applies in full only to the Amazon portion.
>
> What I'll change:
> - Correct this row to show both options and the trade-off
> - Fix the same wording in the Step 4 constraints (it repeats there)
> - Add a `targeting_source` field to the deal schema, so the agent can offer the choice to the trader
>
> Two things I'd like to confirm:
> 1. Does Amazon's targeting on 3P carry the usual audience fee, or is device-level targeting free?
> 2. For 3P pre-curated deals, can we see the built-in targeting in the deal data — so the agent can show the trader what they're getting?

## ❓ David se poochhne wale sawaal

| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | Does Amazon's targeting on 3P carry the usual audience VCPM fee, or is device-level targeting free of data cost? | Effective CPM ka ganit isi par depend karta hai |
| 2 | Beyond device — what else does Amazon's targeting support on 3P? (location? frequency cap?) | Agent ko trader ko batana hai kya milega |
| 3 | For 3P pre-curated deals, is the built-in targeting visible in the deal metadata? | Agar visible hai to agent dikha sakta hai; nahi to trader andhere me hai |

## 🏷️ Ek line me nichod

> **David keh raha hai:** *"Tumne likha 'Netflix ki apni targeting' — jaise koi option nahi hai. Par option hai: Amazon ki targeting (kamzor, sirf device jaisi) ya Netflix ki targeting (behtar, par mehngi). Aur Netflix wali targeting deal ke andar hi baithi hoti hai — alag se nahi lagti."*

**Severity: 🔴 HIGH** — missing feature (choice), missing schema field (`targeting_source`), aur flow coupling (Step 2 ↔ Step 5) jo document me nahi tha.

---
---

# 🗨️ COMMENT #2

## 📍 Location

| | |
|---|---|
| **Section** | `2.4 Audience Set Profiles` |
| **Element** | 🔄 CHANGED line |
| **Highlighted text** | **"added fee consequence"** |
| **Poori line** | *"🔄 CHANGED — renamed 'Broad' to 'Wide' per client vocabulary; **added fee consequence**."* |
| **Asar** | Neeche wala profile table + §2.4 ka poora ➕ NEW fee note |

## 💬 David ne exactly kya likha — DO comments

### Comment 2A (main)
> *"there's not necessarily a fee consequence. Fee is determined by **which audiences are used not how many**. If it's Amazon's or a 3P first party data like Lifestyle or Interest then there's a fee for using it. This is **regardless of profile**."*

### Comment 2B (uski apni reply — zyada detail)
> *"Note here that it **doesn't compound** the more audiences you use. There is just **1 fixed CPM** applied when 1P data is used for Amazon or Third party audience. **But if the user matches a segment in both you would pay both fees.**"*

## 🔍 Line-by-line breakdown

### Comment 2A
| David ka hissa | Plain matlab |
|---|---|
| *"there's **not necessarily** a fee consequence"* | 🔴 "Fee ka natija" hamesha nahi hota — tumne jo likha, wo **hamesha sach nahi** |
| *"Fee is determined by **which audiences** are used"* | Fee is baat par depend karti hai ki **kaunsi** audience use ki |
| *"**not how many**"* | **Kitni** audience use ki — isse **koi lena-dena nahi** |
| *"If it's Amazon's or a 3P first party data like **Lifestyle or Interest**"* | Agar Amazon ka data ya doosri company ka data (Lifestyle/Interest jaise segments) |
| *"then there's a **fee for using it**"* | To us **data** ke istemaal ki fee lagti hai |
| *"This is **regardless of profile**"* | 🔴 Narrow/Balanced/Wide — **profile se koi farak nahi** |

### Comment 2B
| David ka hissa | Plain matlab |
|---|---|
| *"it **doesn't compound** the more audiences you use"* | 🔴 Zyada audience use karne se fee **jud kar nahi badhti** |
| *"There is just **1 fixed CPM** applied when 1P data is used for Amazon"* | Amazon ka data use kiya = **ek hi** fixed CPM (chahe 1 segment ho ya 10) |
| *"or Third party audience"* | Third-party audience ka bhi **ek hi** fixed CPM |
| *"**But if the user matches a segment in both** you would pay **both fees**"* | 🔴 Par ek banda **dono** ke segment me aaya, to **dono** fees |

## 📖 Naye words

| Word | Matlab | Example |
|---|---|---|
| **1P data** (First-party) | Company ka **apna** data — khud ikattha kiya | Amazon ka data: "isne kya kharida, kya search kiya" |
| **3P data** (Third-party) | **Doosri company** ka data — kharida/license kiya | Experian, Oracle, ya publisher ka apna data |
| **Lifestyle segment** | Log ki **jeene ke tarike** par bana group | "Fitness Enthusiasts", "Frequent Travellers" |
| **Interest segment** | Log ki **pasand** par bana group | "Football Fans", "Cooking Enthusiasts" |
| **In-market segment** | Log jo **abhi kharidne** ki taiyari me hain | "In-market for a car" |
| **Compound** | **Jud kar badhna** (2+3+4=9 jaisa) | David: fee compound **nahi** hoti |
| **Regardless of** | **Se koi lena-dena nahi** | "regardless of profile" = profile se farak nahi |
| **Data fee** | Audience data **use karne ka kiraya** | Yahi VCPM hai |

## ❌ Document abhi kya kehta hai vs ✅ Reality

### Document ka table (abhi — galat)
```
┌───┬──────────────────────┬────────────────────────────────────────────┐
│ 1 │ Narrow               │ highly targeted, elevated intent,          │
│   │ (High Precision)     │ HIGHER AUDIENCE FEE, risk of underdelivery │
│                                    ↑ ❌ GALAT                          │
├───┼──────────────────────┼────────────────────────────────────────────┤
│ 2 │ Balanced             │ optimal blend, the usual recommendation    │
├───┼──────────────────────┼────────────────────────────────────────────┤
│ 3 │ Broad → Wide         │ broad demographic/interest reach,          │
│   │ (Maximum Scale)      │ LOWER FEE, less precision                  │
│                                    ↑ ❌ GALAT                          │
└───┴──────────────────────┴────────────────────────────────────────────┘

Aur §2.4 ka ➕ NEW note:
  "A narrow audience is both smaller and MORE EXPENSIVE per impression"
                                          ↑ ❌ YE BHI GALAT
```

### Document ne kya maan liya tha (galat model)
```
Document ki soch:
  "Narrow = kam log = specific data = MEHNGA"
  "Wide   = zyada log = general data = SASTA"

  Aur bundle ke segments dekho:
    Narrow   = 1 segment  → 1 fee
    Balanced = 2 segments → 2 fee (zyada!)
    Wide     = 3 segments → 3 fee (aur zyada!)

  ↑ Saaf-suthra, logical dikhne wala rule...
    ...PAR BANAYA HUA. Reality aisi nahi hai.
```

### ✅ Reality — naya model
```
╔══════════════════════════════════════════════════════════════════════╗
║  FEE PROFILE PAR NAHI, DATA SOURCE PAR DEPEND KARTI HAI              ║
╠══════════════════════════════════════════════════════════════════════╣
║  Sawaal ye NAHI: "kitni audience use ki?"                            ║
║  Sawaal ye HAI:  "KAUNSA DATA use kiya?"                             ║
║                                                                      ║
║  Amazon ka data (1P) use kiya? → Amazon data fee: 1 FIXED CPM        ║
║  3P ka data use kiya?          → 3P data fee: 1 FIXED CPM            ║
║  Dono use kiye + banda dono me aaya? → DONO fees                     ║
║                                                                      ║
║  Segments ki GINTI se koi farak nahi:                                ║
║    1 Amazon segment  → 1 Amazon fee                                  ║
║    5 Amazon segment  → 1 Amazon fee   ← WAHI!                        ║
║   10 Amazon segment  → 1 Amazon fee   ← WAHI!                        ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 🔴 Poora ganit — Purana (galat) vs Naya (sahi)

### Setup
```
Deal: Prime Video 30s @ £28.88 CPM
Amazon audience data fee: £1.85 (fixed, jab bhi Amazon data use ho)
3P audience data fee:     £2.10 (fixed, jab bhi 3P data use ho)
```

### ❌ PURANA (document ka model — galat)
```
┌───────────┬─────────────────────────┬─────────┬───────────────┐
│ Option    │ Segments                │ VCPM    │ Effective CPM │
├───────────┼─────────────────────────┼─────────┼───────────────┤
│ NARROW    │ Higher Ed. Seekers      │ £1.85   │ £30.73        │
│ BALANCED  │ + E-Learning            │ £1.74*  │ £30.62        │  ← *average
│ WIDE      │ + Career Advancement    │ £1.56*  │ £30.44        │  ← *average
└───────────┴─────────────────────────┴─────────┴───────────────┘
      ❌ "average VCPM" wala tarika GALAT
      ❌ "Narrow mehngi, Wide sasti" bhi GALAT
```

### ✅ NAYA (sahi) — agar sab segments Amazon ke hain
```
┌───────────┬──────────────────────┬─────────────┬──────────┬───────────────┐
│ Option    │ Segments             │ Data source │ Data fee │ Effective CPM │
├───────────┼──────────────────────┼─────────────┼──────────┼───────────────┤
│ NARROW    │ 1 × Amazon segment   │ Amazon (1P) │ £1.85    │ £30.73        │
│ BALANCED  │ 2 × Amazon segments  │ Amazon (1P) │ £1.85    │ £30.73        │
│ WIDE      │ 3 × Amazon segments  │ Amazon (1P) │ £1.85    │ £30.73        │
└───────────┴──────────────────────┴─────────────┴──────────┴───────────────┘
                                                    ↑          ↑
                                    🔴 TEENO KA FEE AUR CPM BILKUL SAME!

→ Document ka poora "fee consequence" point GAYAB
→ Narrow mehngi nahi. Wide sasti nahi. Sab BARAABAR.
```

### 🔴 MIXED SOURCE — yahan asli complexity hai
```
Balanced bundle = 2 Amazon segments + 1 3P segment (Lifestyle)

Har IMPRESSION par depend karta hai ki banda kisme matched:

┌────────────────────────────────────┬──────────┬───────────────┐
│ Impression ka case                 │ Data fee │ Effective CPM │
├────────────────────────────────────┼──────────┼───────────────┤
│ Banda sirf Amazon segment me tha   │ £1.85    │ £30.73        │
│ Banda sirf 3P segment me tha       │ £2.10    │ £30.98        │
│ Banda DONO me tha                  │ £3.95    │ £32.83        │ ← dono fees
└────────────────────────────────────┴──────────┴───────────────┘

╔═════════════════════════════════════════════════════════════════════╗
║  🔴 SABSE BADA NATEEJA:                                             ║
║  EFFECTIVE CPM EK NUMBER NAHI — EK RANGE HAI!  £30.73 – £32.83      ║
║  Kyunki depend karta hai HAR BANDA kisme match hua.                  ║
║  Aur ye pehle se pata nahi chal sakta.                               ║
╚═════════════════════════════════════════════════════════════════════╝

→ Aur ye document ke apne ➕ NEW requirement ko mushkil banata hai:
  "The agent should surface the effective CPM (deal + audience fee)"
  → Ab agent EK number nahi de sakta. Range ya blended estimate dena
    padega, aur batana padega ki ye estimate hai.
```

## 🎯 David ne ye comment kyun kiya (uski niyat)

### Wajah 1 — Document ne ek "saaf-suthra rule" BANA LIYA
```
Document ne socha:
  "Narrow = specific = mehnga"
  "Wide   = general  = sasta"

Ye SUNNE ME LOGICAL lagta hai. Ek clean, symmetric rule hai.
PAR KISI NE VERIFY NAHI KIYA. Ye ASSUMPTION thi.

🔴 Aur yahi cheez document ke #1 PRINCIPLE ke KHILAAF hai:

   "Zero-Hallucination Policy: The agent NEVER invents strategy
    parameters, metrics, targeting criteria... It only populates
    values VERIFIED against the VOW database and REST APIs."

   → Agent ko hallucinate nahi karna chahiye
   → PAR DOCUMENT NE KHUD HALLUCINATE KIYA
```

### Wajah 2 — Trader ko galat salah milegi
```
❌ Agent (galat model se):
"Main Balanced recommend karta hun. Narrow zyada MEHNGI hai
 (£30.73 vs £30.62) aur chhoti bhi hai."
→ Trader ne Balanced chuna kyunki SASTA laga
→ Par asal me dono ka SAME daam tha! GALAT WAJAH se faisla.

✅ Agent (sahi model se):
"Main Balanced recommend karta hun — Narrow se 3.7× zyada reach
 milegi, aur data fee DONO me same hai (£1.85, dono Amazon ke
 segments hain). To Narrow chunne ka koi COST faayda nahi hai."
→ Trader ko ASLI wajah pata chali
```

### Wajah 3 — Schema galat modelled hai
```python
# Abhi document me:
class SelectedAudienceSetSchema(BaseModel):
    audience_set_id: str
    name: str
    vcpm_fee: str                  # ← ❌ PER-SEGMENT fee
    profile: AudienceProfileEnum
    effective_cpm: Optional[str]   # ← ❌ EK number
    estimated_reach: Optional[int]

# Problem: vcpm_fee PER AUDIENCE SET rakhi hai.
#          Par fee PER DATA SOURCE hoti hai!
#
# Balanced = [aud_101 (£1.85), aud_102 (£1.63)]
#                     ↑             ↑
#   Do alag fee dikhti hain — par dono Amazon ke hain,
#   to EK hi fee lagegi. Schema galat model dikha raha hai.
```

## 🔴 Ek NAYA SAWAAL jo is comment se paida hota hai

David: *"There is just **1 fixed CPM** applied when 1P data is used."*

**Par document ke API example me har segment ka ALAG vcpm hai:**
```json
{"id": "aud_101", "name": "Higher Education Seekers",     "vcpm": "1.85"}
{"id": "aud_102", "name": "E-Learning & Tech Enthusiasts","vcpm": "1.63"}
{"id": "aud_103", "name": "General Career Advancement",   "vcpm": "1.20"}
                                                            ↑
                                            Teen ALAG numbers!
```

**Do sambhavna:**
```
SAMBHAVNA A: Teen segments TEEN ALAG DATA SOURCES ke hain
  aud_101 → Amazon in-market data   → £1.85
  aud_102 → 3P Lifestyle data       → £1.63
  aud_103 → basic demographic data  → £1.20
  → Phir David theek hai: fee source par depend karti hai

SAMBHAVNA B: VOW ka API per-segment rate deta hai, par Amazon
  asal me per-source charge karta hai
  → Phir API ka data MISLEADING hai, aur agent ko grouping
    karke ek fee nikalni padegi
```

> 🎯 Ye zaroori sawaal hai — iske bina agent effective CPM calculate hi nahi kar sakta.

## 🔧 Impact — kahan-kahan fix chahiye

| # | Jagah | Abhi kya likha hai | Kya karna hai |
|---|---|---|---|
| **1** | **§2.4 CHANGED line** *(comment yahin)* | "added fee consequence" | ❌ Claim **hatao** ya poori tarah re-write |
| **2** | **§2.4 table, Row 1 (Narrow)** | "**higher audience fee**, risk of underdelivery" | ❌ "higher audience fee" hatao · ✅ "risk of underdelivery" **rakho** (sach hai) |
| **3** | **§2.4 table, Row 3 (Wide)** | "**lower fee**, less precision" | ❌ "lower fee" hatao · ✅ "less precision" **rakho** |
| **4** | **§2.4 ➕ NEW note** | *"narrow audience is both smaller and **more expensive per impression**"* | ❌ "more expensive" **hatao** |
| **5** | **§2.4 ➕ NEW note** | *"the audience fee (VCPM) **stacks on top of** the deal CPM"* | ✅ **SAHI hai** — rakho. Par explain karo ki stacking **per data source** hoti hai |
| **6** | **Step 4 — Effective CPM field** | "Deal CPM + audience VCPM fee, shown per option" | 🔄 **Re-write** — per-source fee, mixed-source me **range** |
| **7** | **§5 `SelectedAudienceSetSchema`** | `vcpm_fee` per audience set | 🔄 `data_source` field add karo, fee source-level par le jao |
| **8** | **§5 `...effective_cpm`** | Ek `Optional[str]` | 🔄 Range / blended estimate ke liye modify |
| **9** | **`full_strategy_..._mastery.md`** worked example | "average VCPM £1.74" | ❌ Ganit galat — theek karna hai |

## ✍️ DOCUMENT ME DAALNE WALA NOTE (draft)

> **📝 NOTE — Audience fee model corrected (David Moss, review comment)**
>
> The line *"added fee consequence"* and the fee wording in the table below were **incorrect**. They implied a correlation between profile breadth and cost (Narrow = higher fee, Wide = lower fee). **That correlation does not exist.** Corrected model:
>
> **The fee depends on WHICH data is used, not on how many segments or which profile.**
>
> | | **What the doc said (wrong)** | **How it actually works** |
> |---|---|---|
> | What drives the fee | Profile breadth (Narrow/Balanced/Wide) | **The data source** of the segments used |
> | More segments | More fee (compounding) | ❌ **No compounding** — one fixed CPM per data source |
> | Narrow vs Wide | Narrow more expensive | **Identical**, if both use the same data source |
>
> **The rule, precisely:**
> - Using **Amazon's own (1P) audience data** → **one fixed CPM**, regardless of how many Amazon segments are in the bundle
> - Using **third-party audience data** (e.g. Lifestyle, Interest segments) → **one fixed CPM** for that source
> - If a given user **matches a segment in both** sources → **both fees** are charged for that impression
> - This is **regardless of profile** — Narrow, Balanced and Wide are all subject to the same rule
>
> **What stays correct:** the fee still **stacks on top of the deal CPM**, and Narrow still carries a genuine **risk of underdelivery** — but for reach reasons, not cost reasons.
>
> **Consequence for effective CPM (significant):**
>
> Single-source bundle → a single number:
> ```
> Deal CPM £28.88 + Amazon data fee £1.85 = £30.73
> ```
> Mixed-source bundle → a **range**, because it depends on which source each impression's user matched in:
> ```
> Matched Amazon only  → £28.88 + £1.85         = £30.73
> Matched 3P only      → £28.88 + £2.10         = £30.98
> Matched both         → £28.88 + £1.85 + £2.10 = £32.83
>
> → Effective CPM: £30.73 – £32.83
> ```
> The agent must present effective CPM as a **range or blended estimate for mixed-source bundles**, and state that it is an estimate — a single exact figure is not possible.
>
> **Schema changes required:**
> ```python
> class AudienceDataSourceEnum(str, Enum):
>     """➕ NEW — the fee is charged per data source, not per segment"""
>     AMAZON_1P = "AMAZON_1P"
>     THIRD_PARTY = "THIRD_PARTY"
>     NONE = "NONE"              # e.g. basic demographic — no data fee
>
> class SelectedAudienceSetSchema(BaseModel):
>     audience_set_id: str
>     name: str
>     data_source: AudienceDataSourceEnum    # ➕ NEW — drives the fee
>     profile: AudienceProfileEnum
>     estimated_reach: Optional[int] = None
>     # vcpm_fee REMOVED from segment level — fee is per source
>
> class AudienceFeeSchema(BaseModel):
>     """➕ NEW — fees resolved per data source, not per segment"""
>     amazon_1p_fee: Optional[str] = None
>     third_party_fee: Optional[str] = None
>     is_mixed_source: bool = False
>     effective_cpm_min: str      # only one source matched
>     effective_cpm_max: str      # matched in both
>     effective_cpm_note: str     # "range because bundle is mixed-source"
> ```
>
> **⚠ Open question raised by this correction:** the `POST /audience-sets/suggest/` response returns a **per-segment `vcpm`** (`1.85`, `1.63`, `1.20`). If the fee is one fixed CPM per data source, these values are either (a) each segment's respective source rate, or (b) misleading and need collapsing to a per-source fee by the agent. **Needs confirming against the real API.**

## 💬 REPLY DRAFT (baad me post karenge)

> Thanks David — this one changes the model, not just the wording.
>
> I had assumed a correlation that doesn't exist: narrow = specific data = higher fee, wide = general = lower fee. It looks logical, but I never verified it. Understood now: **the fee is driven by the data source, not by the profile or the number of segments.**
>
> Your second note is the part I had most wrong. I had it compounding — Narrow 1 segment, Balanced 2, Wide 3, and the fee growing with each. Now clear: **one fixed CPM per data source**, and both fees only when a user matches a segment in both Amazon and third-party data.
>
> The consequence I want to flag: for a mixed-source bundle, **effective CPM is a range, not a single number** — £30.73 if the user matched Amazon only, £32.83 if they matched both. So the agent can't show one exact figure there; it'll show a range and say it's an estimate.
>
> What I'll change:
> - Remove "higher audience fee" from Narrow and "lower fee" from Wide (keeping "risk of underdelivery" and "less precision" — those are still true)
> - Rewrite the fee note to be per-data-source, not per-profile
> - Move the fee off the segment in the schema and onto the data source, and model effective CPM as a range for mixed bundles
>
> One thing I need to check: the `suggest` endpoint returns a **different `vcpm` per segment** (1.85, 1.63, 1.20). If the fee is one fixed CPM per source, are those per-segment values just each segment's source rate — or is the API showing something we should collapse ourselves? I'll verify against the real API, but tell me if you already know.

## ❓ David se poochhne wale sawaal

| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | Suggest API per-segment `vcpm` deta hai — agar fee per-source hai, to wo numbers kya represent karte hain? | Iske bina effective CPM calculate nahi ho sakta |
| 2 | Kya koi audience type **bina fee** ki bhi hai (jaise basic demographic)? | Agar haan, to agent ek sasta option suggest kar sakta hai |
| 3 | Amazon 1P fee aur 3P fee ke **actual numbers** kya hain — fixed hain ya audience type par depend karte hain? | Forecast ke liye asli numbers chahiye |
| 4 | Mixed-source bundle me "matched in both" ka ratio typically kya hota hai? | Blended estimate dene ke liye — warna sirf range de sakte hain |

## 🏷️ Ek line me nichod

> **David keh raha hai:** *"Tumne likha 'Narrow mehngi, Wide sasti' — ye tumne bana liya, sach nahi hai. Fee is baat par depend karti hai ki KAUNSA DATA use kiya, na ki kitne segments ya kaunsa profile. Amazon ka data use kiya = ek fixed fee, chahe 1 segment ho ya 10. Aur agar banda Amazon aur 3P dono me aata hai, tab dono fees lagti hain."*

**Severity: 🔴 HIGH** — kyunki:
- **Business model galat** hai (fee ka poora logic)
- **Effective CPM ka ganit galat** hai (ek number nahi, **range** hai)
- **Schema galat** hai (`vcpm_fee` per-segment, per-source hona chahiye)
- **Agent galat salah** dega (Balanced ko "sasta" bata kar recommend karega)
- Aur ye **document ke #1 principle (Zero-Hallucination) ka apna violation** hai

---
---

# 🧩 COMMENTS #3 · #4 · #5 — EK CLUSTER

> **Teeno ek hi table par hain** (`§3 Comparison: old order vs new order`) aur **ek hi jad** se aaye hain:
> **"Tumne cheezein zaroori bana di jo asal me marzi ki hain — aur Audiences ko Targeting se alag kar diya jo alag nahi hona chahiye."**
>
> Isliye teeno pehle alag-alag, phir **ek saath** (jod ka section) samjhe gaye hain.

---
---

# 🗨️ COMMENT #3 — "Budget split is optional"

## 📍 Location
| | |
|---|---|
| **Section** | `3. The Agentic Flow` → `Comparison: old order vs new order` table |
| **Highlighted** | **"Budget split ➕ NEW"** (row 4, New column) |
| **Asar** | Step 3 ka poora field matrix |

## 💬 David ne exactly kya likha
> *"is **optional** but to give an **accurate CPM** is **preferred**"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"is **optional**"* | 🔴 Budget split **zaroori nahi** — trader skip kar sakta hai |
| *"but to give an **accurate CPM**"* | Par **sahi CPM** batane ke liye |
| *"is **preferred**"* | Ye **behtar** hai (mana nahi kar raha, recommend kar raha) |

## ❌ Document abhi kya kehta hai
```
Step 3 ka field matrix:
┌──────────────────────┬────────────────┬────────────────────────────────────┐
│ Split by inventory   │ Allocation (%) │ REQUIRED when multiple inventories │
│ Split by duration    │ Allocation (%) │ REQUIRED when multiple durations    │
└──────────────────────┴────────────────┴────────────────────────────────────┘
                                          ↑ ❌ "Required" GALAT
```

## ✅ Reality — "accurate CPM" ka matlab

### Agar budget split KIYA
```
Trader ne bataya: Prime 15s £2,340 · Prime 30s £3,660 · Netflix 30s £4,000

Agent PAKKA bata sakta hai:
  Prime 15s   →  2,340 ÷ 20.00 × 1000 =  117,000 impressions
  Prime 30s   →  3,660 ÷ 31.50 × 1000 =  116,190 impressions
  Netflix 30s →  4,000 ÷ 32.00 × 1000 =  125,000 impressions
  ──────────────────────────────────────────────────────────
  TOTAL: 358,190   ← ✅ ACCURATE, har line ka CPM pata hai
```

### Agar budget split NAHI kiya
```
Trader: "£10,000 hai, tum decide karo"

4 deals, 4 alag CPM: £20.00 · £31.50 · £32.00 · £24.00
Agent kya CPM bataye?

  Option A: average → (20+31.50+32+24)/4 = £26.88
            ❌ GALAT — agar zyada paisa 30s me gaya to asli CPM £31 ke kareeb
  Option B: range → "£20 se £32"
            🟡 Imandar, par forecast ke liye bekaar
  Option C: kuch na bataye
            ❌ Trader ko plan samajh nahi aayega

🔴 ASLI BAAT: BINA SPLIT KE, ALLOCATION AMAZON DSP KHUD KARTA HAI
   → Runtime par decide hoga kitna kahan gaya
   → Yaani asli CPM PEHLE SE PATA HI NAHI CHAL SAKTA
```

**Yahi David ka point:** split zaroori nahi, **par uske bina accurate CPM impossible hai** — aur accurate CPM ke bina accurate forecast bhi.

## 🎯 Kyun ye comment kiya (niyat)
```
Wajah 1 — Trader ko block nahi karna
  Kai baar trader kehta hai "tum decide karo, main details me nahi jaana"
  → Document usko FORCE karta hai → frustrate

Wajah 2 — Consequence batana, mana nahi karna
  David ne "optional" bola PAR reason bhi diya
  → Document ke apne pattern se match: Step 3 me likha hai
    "The agent must state which it chose and why"
  → Yahan bhi: agent bata de ki split na karne ka NUKSAAN kya hai
```

## 🔧 Kya fix karna hai
| # | Jagah | Abhi | Naya |
|---|---|---|---|
| 1 | Step 3 — Split by inventory | **Required** when multiple inventories | **Optional** (preferred for accurate CPM) |
| 2 | Step 3 — Split by duration | **Required** when multiple durations | **Optional** (preferred for accurate CPM) |
| 3 | Step 3 intro | *"The agent proposes how the total budget is divided"* | ✅ Rakho — add karo ki trader **skip** kar sakta hai |
| 4 | Step 3 — naya paragraph | — | ➕ Bina split ke kya hota hai (blended/unknown CPM, DSP auto-allocates) |
| 5 | `BudgetSplitSchema` | `budget_split: Optional[...] = None` | ✅ **Already Optional!** Sirf field table galat hai |

> 💡 **Document apne aap se contradict kar raha hai:** schema me `Optional`, table me `Required`. Ye ek aur inconsistency hai.

## 🤖 Agent ka naya behaviour
```
Agent: "Tumne 2 inventories aur 2 durations chune hain. Budget split
        propose kar raha hun:
        [table]

        Ya tum skip kar sakte ho — main Amazon DSP ko auto-allocate
        karne dunga.

        ⚠ Par dhyan do: split ke bina main accurate CPM nahi de
        paunga. Chaar deals ke CPM £20 se £32 tak hain, aur bina
        split ke pata nahi chalega kitna paisa kahan jaayega.
        Forecast bhi tab estimate hi rahega.

        Split karna hai ya skip?"
```

## ✍️ DOCUMENT NOTE (draft)
> **📝 NOTE — Budget split is optional (David Moss)**
>
> The field matrix below marks the splits as *"Required when multiple inventories/durations selected"*. **Incorrect** — budget split is **optional**. It is **preferred**, because without it an accurate CPM cannot be given.
>
> **Why the split drives CPM accuracy:** with 4 lines at £20.00, £24.00, £31.50 and £32.00, the blended CPM depends entirely on how the money is distributed. Without a split, allocation happens at runtime on the DSP side, so the effective CPM — and therefore the impression and reach forecast — cannot be stated in advance. Only a range or a blended estimate is possible.
>
> **Corrected requirements:** both split fields → **Optional**. *(Note: `budget_split: Optional[BudgetSplitSchema] = None` in §5 was already optional — only this table was wrong.)*
>
> **Agent behaviour:** propose the split as before, state the method and why (unchanged), **and offer to skip it** — while stating the consequence: *"Without a split I can't give you an accurate CPM; the forecast will be an estimate only."*

## 💬 REPLY DRAFT
> Understood — I'll change both split fields to **optional**, and note that it's preferred because the CPM can't be stated accurately without it. With four lines between £20 and £32, the blended CPM depends entirely on how the money lands, and without a split that happens at runtime on the DSP side.
>
> The agent will still propose a split and state its method, but will offer to skip — and if skipped, it'll say plainly that the forecast is an estimate only.
>
> Worth noting: `budget_split` in the schema was already `Optional` — only this table said "Required". I'll reconcile them.

## 🏷️ Nichod
> **David keh raha hai:** *"Budget split zaroori nahi hai — par uske bina sahi CPM nahi bata sakte, isliye behtar hai karna."*

**Severity: 🟡 MEDIUM** — field requirement + agent behaviour badalna hai, flow nahi.

---
---

# 🗨️ COMMENT #4 — "Audiences: optional again"

## 📍 Location
| | |
|---|---|
| **Section** | Same comparison table |
| **Highlighted** | **"mandatory"** — row: `4. Audiences (mandatory, suggestion-driven)` |
| **Asar** | §2.4 ka ➕ NEW note + Step 4 ka poora field matrix + §8 summary + state machine |

## 💬 David ne exactly kya likha
> *"**optional again**"*

Do shabd. Par bahut bada matlab.

## 🔍 "optional again" ka matlab
```
"again" = "phir se" / "wapas"

v1.1.0 me: Audiences OPTIONAL thi
v2.0 me:   MANDATORY bana di
David:     "optional AGAIN" = wapas optional karo

→ Yaani v2.0 ka ye change GALAT tha. Purana theek tha.
```

## ❌ Document abhi kya kehta hai
```
§2.4:
  "➕ NEW: audiences are MANDATORY and suggestion-driven. The agent
   always suggests three options... Nobody browses the ~3,400
   segments manually."

Step 4 field matrix:
┌──────────────────┬────────────┬──────────┬────────────────────────────┐
│ Audience options │ 3 profiles │ REQUIRED │ 🔄 CHANGED from optional   │
│                  │            │          │    to MANDATORY            │
└──────────────────┴────────────┴──────────┴────────────────────────────┘
                                    ↑ ❌ GALAT

Step 4 constraints:
  "Nobody browses — the agent uses POST /api/audience-sets/suggest/
   exclusively"
  "At least one audience set must be selected"   ← ❌ ye line hatani hai
```

**🔴 Dhyan do — David ne "suggestion-driven" par koi comment NAHI kiya:**
```
✅ "suggestion-driven"  → SAHI hai, rakho
❌ "mandatory"          → GALAT hai, hatao
```

## ✅ Reality — Audience ke BINA campaign kyun chal sakta hai?

```
Campaign: BrightPath awareness, UK, £10,000, Prime Video 30s

BINA AUDIENCE:
  Deal: Prime Video ROS @ £28.88
  Audience: KOI NAHI
  Targeting: country = GB, device = Connected TV

  → Ad har us bande ko dikhega jo Prime Video UK par dekhta hai
  → Reach: MAXIMUM (poora available inventory)
  → Data fee: £0.00  ← 🔴 KOI AUDIENCE DATA USE NAHI HUA!
  → Effective CPM: £28.88 (deal CPM hi)
  → Impressions: 10,000 ÷ 28.88 × 1000 = 346,260

AUDIENCE KE SAATH:
  Same deal + "Higher Education Seekers" (Amazon 1P data)
  → Data fee: £1.85
  → Effective CPM: £30.73
  → Impressions: 325,415   ← 20,845 KAM
  → Reach: 450,000 tak simit
```

### 🔴 Comment #2 se JUDAV
```
Comment #2 ne bataya: fee DATA SOURCE use karne par lagti hai
→ Agar KOI audience data use na karo → 💰 KOI FEE NAHI!

╔══════════════════════════════════════════════════════════════════════╗
║  "NO AUDIENCE" = SABSE SASTA OPTION AUR SABSE ZYADA REACH            ║
║                                                                      ║
║  Aur AWARENESS campaign ke liye — jahan goal MAX REACH hai —          ║
║  ye SABSE ACCHA option ho sakta hai!                                 ║
║                                                                      ║
║  🔴 DOCUMENT NE "mandatory" LIKHKAR YE POORA OPTION KHATAM KAR       ║
║     DIYA THA — aur wo bhi Awareness-only module me, jahan ye         ║
║     option sabse zyada kaam ka hai.                                  ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 🎯 Kyun ye comment kiya (niyat)
```
Wajah 1 — Ek valid, sasta, high-reach option delete ho gaya tha

Wajah 2 — Trader ki azadi
  "Postcode targeting chahiye, audience nahi" — ye legitimate hai
  (David ka apna example Comment #5 me!)

Wajah 3 — Mandatory banane ka koi business reason nahi tha
  Document ne likha "Nobody browses the 3,400 segments" — par ye
  SUGGESTION ka reason hai, MANDATORY ka nahi. Do alag baatein
  ek me mila di:
    "Agent suggest karega"  ✅ (browsing impractical hai)
    "Audience zaroori hai"  ❌ (iska koi reason nahi diya)
```

## ⚠ Kya Kareem ka deliverable khatam ho gaya? — NAHI
```
Task slide: "Narrow / broad / balanced audience options"

❌ Ye NAHI hua: feature delete
✅ Ye hua: feature OPT-IN ban gaya

Naya behaviour:
  Default → koi audience nahi (country + CTV device)
  Trader kahe "audience targeting chahiye" → agent 3 options deta hai
  Trader kahe "sirf postcode" → agent postcode lagata hai, audience nahi

→ Suggestion engine (pgvector) ZINDA
→ Narrow/Balanced/Wide ZINDA
→ Sirf "gate" hat gaya

Ye asal me BEHTAR hai — ab jo trader audience chunta hai, wo
JAAN BUJH KAR chunta hai, majboori me nahi.
```

## 🔧 Kya fix karna hai
| # | Jagah | Abhi | Naya |
|---|---|---|---|
| 1 | Comparison table row 4 | "Audiences (**mandatory**, suggestion-driven)" | "Audiences (**optional**, suggestion-driven)" |
| 2 | §2.4 ➕ NEW note | *"audiences are **mandatory** and suggestion-driven"* | *"audiences are **optional** and suggestion-driven"* |
| 3 | Step 4 — Audience options | **Required** · 🔄 CHANGED from optional to mandatory | **Optional** · ✅ UNCHANGED (v1.1.0 theek tha) |
| 4 | Step 4 — Chosen option | **Required** | **Optional** — sirf tab jab trader audience chahe |
| 5 | Step 4 constraints | *"At least one audience set must be selected"* | ❌ **Line hatao** |
| 6 | Step 4 — naya paragraph | — | ➕ "No audience" ka case: £0 data fee, max reach, awareness ke liye often best |
| 7 | `FullStrategySchema.audience_options` | `Field(default_factory=list)` | ✅ **Already optional!** |
| 8 | §8 Summary of changes | 🔄 CHANGED list me "audiences mandatory" | ❌ Entry **hatao** |
| 9 | State machine line 6 | `suggest_audiences (…; **mandatory**)` | `suggest_audiences (…; **optional**)` |

> 💡 **Phir wahi baat:** schema me `default_factory=list` = **optional**. Sirf text me "mandatory". **Schema sahi tha, prose galat.**

## ✍️ DOCUMENT NOTE (draft)
> **📝 NOTE — Audiences are optional, not mandatory (David Moss)**
>
> v2.0 changed audiences from optional (v1.1.0) to **mandatory**. **That change was wrong** — audiences are **optional**. v1.1.0 was correct on this point.
>
> **"Suggestion-driven" stays correct** — nobody browses ~3,400 segments, so the agent suggests. But suggesting is not the same as requiring.
>
> **Why "no audience" is a legitimate — often preferable — option:**
> - Reach is **maximum** (the full available deal inventory)
> - Data fee is **£0** (no audience data used — see the corrected fee model in §2.4)
> - Effective CPM = deal CPM, with nothing added
> - For an **Awareness-only** module, which this is, maximum reach at lowest cost is frequently the right answer
>
> Making audiences mandatory removed the cheapest, highest-reach option from a module whose only goal is awareness.
>
> **Corrected requirements:** Audience options → **Optional**. Chosen option → **Optional**. Remove *"At least one audience set must be selected"* from the Step 4 constraints. Remove "audiences mandatory" from §8 Summary of Changes. *(Note: `audience_options` in §5 was already optional — only the prose and tables were wrong.)*
>
> **What is retained:** the pgvector suggestion engine and the Narrow / Balanced / Wide options remain — they become **opt-in** rather than a gate.

## 💬 REPLY DRAFT
> Agreed — reverting to optional. Making it mandatory was my change in v2.0 and it was wrong.
>
> I'd conflated two things: *"nobody browses 3,400 segments so the agent should suggest"* (true) with *"therefore an audience must be selected"* (not true). The suggestion engine and the Narrow/Balanced/Wide options stay — they just become opt-in.
>
> The bigger thing I'd removed without realising: **no audience** is often the best option here. Zero data fee, maximum reach, effective CPM = deal CPM. For an Awareness-only module that's frequently the right answer — and mandatory audiences ruled it out.
>
> Same as the budget split — `audience_options` in the schema was already optional; only the prose and the field table said mandatory.

## 🏷️ Nichod
> **David keh raha hai:** *"Audience zaroori nahi hai. Wapas optional karo. Suggestion theek hai, majboori galat hai."*

**Severity: 🔴 HIGH** — ek poora valid (aur sasta, high-reach) option delete ho gaya tha, aur wo bhi Awareness-only module me.

---
---

# 🗨️ COMMENT #5 — "Audiences are part of Targeting" 🔴 SABSE BADA

## 📍 Location
| | |
|---|---|
| **Section** | Same comparison table |
| **Highlighted** | **"Targeting ➕ NEW"** (row 6, New column) |
| **Asar** | 🔴 Step 4 **aur** Step 5 dono ka poora design + flow ka structure + state machine |

## 💬 David ne exactly kya likha
> *"I would treat **audiences as part of targeting**. So once inventory decided / inferred then you are shown the **default targeting applied / suggested** like country targeting and Connected TV (CTV) device only and then you could **refine this**, define the audience segments **or accept it as sufficient**. Example: the user wants to use **only postcodes instead of audiences** for targeting"*

## 🔍 Line-by-line — sabse zaroori breakdown
| David ka hissa | Plain matlab |
|---|---|
| *"I would treat **audiences as part of targeting**"* | 🔴 Audience aur Targeting **do alag cheezein nahi** — audience targeting ki **ek kism** hai |
| *"So **once inventory decided / inferred**"* | Jab inventory tay ho jaaye (ya agent brief se **khud samajh le**) |
| *"then you are **shown the default targeting** applied / suggested"* | 🔴 Tab trader ko ek **default targeting** dikhayi jaati hai — **pehle se lagi hui** |
| *"like **country targeting** and **Connected TV (CTV) device only**"* | Default kya hai: desh + sirf CTV device. Bas itna |
| *"and then you **could refine this**"* | Uske baad trader **sudhaar** sakta hai (chahe to) |
| *"**define the audience segments**"* | Refinement ka **ek tarika** = audience segments daalna |
| *"**or accept it as sufficient**"* | 🔴 **Ya bas "theek hai" bol de** — kuch add karne ki zaroorat nahi |
| *"Example: the user wants to use **only postcodes instead of audiences**"* | 🔴 Postcode aur audience **alternatives** hain — dono "targeting" hain |

## 📖 Naye concepts
| Concept | Matlab | Example |
|---|---|---|
| **Default targeting** | Wo minimum targeting jo **khud lag jaati hai**, bina poochhe | country=GB, device=Connected TV |
| **Refine** | Sudharna / aur specific karna | "Aur London tak simit kar do" |
| **"Accept as sufficient"** | "Jo hai, theek hai — aage chalo" | Trader kuch add nahi karta |
| **Postcode targeting** | Post code (pin code) se location targeting | "SW1, SW3, W1 me dikhao" |
| **Inferred** | Agent ne **khud samajh liya** (poochha nahi) | Brief me "Prime Video" → inventory infer ho gayi |

## ❌ Document ka model vs ✅ David ka model

### Document ka model (abhi)
```
Step 2: INVENTORY
   ↓
Step 3: BUDGET SPLIT     (Required — Comment #3 ne galat bataya)
   ↓
Step 4: AUDIENCES        (MANDATORY — Comment #4 ne galat bataya)
        "Teen options — Narrow, Balanced, Wide. Ek chuno."
        → Trader ko ZAROOR chunna padega
   ↓
Step 5: TARGETING        (Optional — 5 alag KHAALI fields)
        location · instream position · content exclusions ·
        device type · mobile environment

🔴 PROBLEMS:
   • Audience aur targeting DO ALAG steps — par dono "kisko dikhana
     hai" hi batate hain!
   • Kuch bhi pre-filled nahi — trader ko sab khud bharna hai
   • Audience mandatory, baaki optional — inconsistent
   • Trader ko 6 field dekhne padte hain jab shayad kuch bhi nahi
     chahiye tha
```

### ✅ David ka model
```
Step 2: INVENTORY  (decided ya inferred)
   ↓
   ↓  🔴 Agent TURANT ek DEFAULT TARGETING dikha deta hai:
   ↓
┌────────────────────────────────────────────────────────────────┐
│  DEFAULT TARGETING (already applied)                           │
│  ✓ Country: United Kingdom (GB)      ← Step 1 se aaya          │
│  ✓ Device:  Connected TV only        ← CTV campaign hai, so    │
│  ✓ Audience: None                                              │
│                                                                │
│  Kuch aur chahiye? Tum ye add/refine kar sakte ho:             │
│    • Audience segments  (main 3 options suggest kar dunga)      │
│    • Postcodes / cities                                        │
│    • Content exclusions                                        │
│    • Instream position                                         │
│    • ... (aur bhi)                                             │
│                                                                │
│  Ya bas "theek hai" bol do — main aage badh jaunga.            │
└────────────────────────────────────────────────────────────────┘
   ↓
   Trader ka choice:
     (a) "Theek hai"                 → aage chalo, kuch add nahi hua
     (b) "Audience segments chahiye" → agent 3 options deta hai
     (c) "Sirf SW1, SW3 postcodes"   → postcode lagao, audience NAHI
     (d) "Audience + London"         → dono
```

## 🔴 Teen bade badlav

### Badlav 1 — Step 4 aur Step 5 MERGE ho jaate hain
```
❌ Purana:  Step 4 (Audiences) + Step 5 (Targeting) = do steps
✅ Naya:    Step 4 (Targeting) = ek step, jisme audiences ek TYPE hai

Naya structure:
  TARGETING
  ├── Country / market          (default: Step 1 se)
  ├── Device type               (default: Connected TV)
  ├── Audience segments         ← audiences YAHAN aa gayi
  ├── Location / postcodes
  ├── Content exclusions
  ├── Instream position
  └── Mobile environment

→ 13 steps se 12 steps ho jaayenge
```

### Badlav 2 — "Default then Refine" pattern
```
❌ Purana pattern: KHAALI FORM
   "Ye 6 fields hain. Bharo."
   → Trader ka kaam: sab sochna aur bharna

✅ Naya pattern: SENSIBLE DEFAULT + REFINE
   "Ye lag chuka hai. Kuch badalna hai?"
   → Trader ka kaam: sirf approve karna, ya jo chahiye wo badalna
```

**🔴 Aur ye document ke APNE Principle #2 se ZYADA match karta hai:**
```
Document ka Principle 2:
  "Self-Filling Form Paradigm — a form that fills itself in as you chat"

David ka model:
  Country?  → Step 1 se KHUD bhar gaya
  Device?   → CTV campaign hai, to KHUD "Connected TV" ho gaya
  Baaki?    → khaali, par trader chahe to bhare

╔═══════════════════════════════════════════════════════════════════╗
║  🎯 DAVID KA MODEL DOCUMENT KE APNE PRINCIPLE KO BEHTAR FOLLOW    ║
║     KARTA HAI — "form jo khud bharta hai"                         ║
║                                                                   ║
║  Document ne Step 5 me 5 KHAALI fields rakhe.                     ║
║  David keh raha hai: jo pata hai, wo PEHLE SE BHAR DO.            ║
╚═══════════════════════════════════════════════════════════════════╝

→ Ye reply me likhna. David ko dikhega ki tum uske point ko document
  ke apne principle se jod paa rahe ho.
```

### Badlav 3 — Audience aur Postcode ALTERNATIVES hain
```
David: "only postcodes INSTEAD OF audiences"
        "instead of" = ki JAGAH par

Trader: "Mujhe audience segments nahi chahiye. Main sirf ye
         postcodes target karna chahta hun: SW1, SW3, W1, W8"

→ Ye ek POORI targeting strategy hai
→ Kyun? BrightPath ka campus wahan hai! Ya wahan rich households hain
→ Audience data ki zaroorat nahi — location hi kaafi hai
→ 💰 Data fee bhi £0 (Comment #2 se judav)

╔═══════════════════════════════════════════════════════════════════╗
║  Document ke model me ye POSSIBLE HI NAHI THA:                    ║
║    Step 4 (Audiences) MANDATORY → trader ko audience chunni       ║
║    PADEGI → wo postcode-only strategy chala hi nahi sakta         ║
╚═══════════════════════════════════════════════════════════════════╝
```

**⚠ Aur ek zaroori gap:** document ke Step 5 me `location` field hai, par **postcode** ka zikr nahi:
```
Document: "Location | Multi-select | Optional"
          API: GET /api/strategies/locations/{market}/

Sawaal: kya ye API POSTCODES deta hai? Ya sirf cities/regions?
→ David ka example "postcodes" hai
→ Agar API postcode support nahi karta, ye ek GAP hai
→ ⚠ Confirm karna hai
```

## 🎯 Kyun ye comment kiya (niyat)
```
Wajah 1 — Conceptual galti theek karna
  Audience aur Targeting ka ek hi kaam hai: "kisko dikhana hai".
  Do alag steps se trader confuse hota hai:
    "Audience me maine education seekers chuna... ab Targeting me
     phir se kuch chunna hai? Ye alag kaise hai?"

Wajah 2 — UX behtar karna
  6 khaali fields ke bajaye: 2 pre-filled + "kuch aur chahiye?"
  → Trader ka kaam 80% kam

Wajah 3 — Config-driven requirement ko poora karna
  Client ne pehle kaha tha: "This targeting list frequently changes
  so it should be easy to add new targeting types"

  🔴 Agar audiences BHI ek targeting type hai, to wo bhi usi
     config-driven registry me aayegi!
  → Ek hi system, ek hi tarika, ek hi config
  → Naya targeting type add karna trivial ho jaayega
```

## 🔧 Kya fix karna hai (sabse bada impact)
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Comparison table** | Step 4 + Step 5 ko **ek row** me merge: "4. Targeting (audiences included; default + refine)" |
| 2 | **Step 4 (Audiences)** | Poora step **Step 5 me merge** — audiences ek targeting type ban jaaye |
| 3 | **Step 5 (Targeting)** | Naam/scope badlo — sab targeting types ek jagah |
| 4 | **Naya sub-section** | ➕ "Default targeting" — kya default lagta hai aur kahan se derive hota hai |
| 5 | **Naya sub-section** | ➕ "Accept or refine" interaction pattern |
| 6 | **`TargetingSchema`** | Audience segments isme add karo + config-driven bana do (Client ka requirement) |
| 7 | **State machine** | `suggest_audiences` + `apply_targeting` → `propose_targeting` (default) + `refine_targeting` |
| 8 | **Step 6 (Predict reach)** | 🔴 Repair loop **conditional** karo — agar koi audience nahi to "widen audience" ka matlab nahi |
| 9 | **Step 1 → default derivation** | Document karo ki country aur device default kahan se aate hain |
| 10 | **Location field** | ⚠ Confirm karo ki postcode support hai ya nahi |
| 11 | **§8 Summary of changes** | Step count 13 → 12, aur merge ko document karo |

## 🤖 Naya agent behaviour — poora example
```
(Step 2 khatam — Prime Video + Netflix deals chun li)

Agent: "Deals set ho gaye. Targeting ke liye maine ye default laga
        diya hai — jo tumhare brief se nikla:

        ┌──────────────────────────────────────────────────────┐
        │  TARGETING (applied)                                 │
        │  ✓ Country     United Kingdom (GB)                   │
        │  ✓ Device      Connected TV only                     │
        │  ✓ Audience    None — poore available inventory par  │
        │                                                      │
        │  Effective CPM: £28.88 (deal CPM hi — koi data fee   │
        │                 nahi, kyunki koi audience data use    │
        │                 nahi ho raha)                         │
        │  Estimated impressions: 346,260                       │
        └──────────────────────────────────────────────────────┘

        Tumhara KPI reach hai, aur ye setup MAXIMUM reach deta hai
        aur sabse sasta bhi hai.

        Chaaho to refine kar sakte ho:
          • Audience segments — main 3 options suggest kar dunga
            (⚠ isse data fee lagegi aur reach kam hogi)
          • Locations / postcodes — ek khaas ilaake tak simit
          • Content exclusions — kis content ke saath nahi dikhana
          • Instream position, mobile environment

        Ya bas 'theek hai' bol do — main forecast par chala jaunga."

──────────────────────────────────────────────────────────────────
Case A — Trader: "theek hai"
  → Agent Step 6 (forecast) par chala jaata hai. 4 second me kaam ho gaya.

Case B — Trader: "audience segments chahiye"
  Agent: "Theek hai, 3 options bana raha hun (pgvector se)..."
         [Narrow / Balanced / Wide table — data fee + effective CPM ke saath]

Case C — Trader: "sirf ye postcodes — SW1, SW3, W1, W8"
  Agent: "Set kar diya:
          ✓ Country: GB
          ✓ Device: Connected TV
          ✓ Postcodes: SW1, SW3, W1, W8
          ✓ Audience: None

          Data fee £0. Effective CPM £28.88.
          ⚠ Postcode targeting se available inventory kam ho jaayega —
            main forecast me exact number dikha dunga."
```

## ✍️ DOCUMENT NOTE (draft)
> **📝 NOTE — Audiences are part of targeting; default-then-refine (David Moss)**
>
> The flow separates Audiences (Step 4) and Targeting (Step 5). **They should be one step** — audiences are **one type of targeting**, not a separate concern. Corrected model:
>
> **1. Audiences merge into Targeting.** Both answer the same question — *who sees this ad*. Splitting them confuses the trader and duplicates the interaction. Audience segments become one targeting type alongside location, device, content exclusions and so on. This also satisfies the client's earlier requirement that targeting be **config-driven and easy to extend** — with audiences inside the same registry, one mechanism covers all of it.
>
> **2. Default targeting is applied automatically, then refined.** Once inventory is decided or inferred, the agent **shows a default that is already applied**, derived from what is already known:
>
> | Default | Derived from |
> |---|---|
> | Country targeting | `markets` (Step 1) |
> | Connected TV device only | CTV formats (Step 1) |
> | No audience | nothing selected — deal's full inventory |
>
> The trader then either **refines** it (add audience segments, add postcodes, add exclusions…) or **accepts it as sufficient** and moves on.
>
> **3. Audience and location targeting are alternatives, not a sequence.** Per David's example, a trader may want *"only postcodes instead of audiences"* — a complete and valid targeting strategy on its own. The previous mandatory-audience design made that impossible.
>
> **Flow consequence:** Steps 4 and 5 collapse into one (13 steps → 12). The repair loop in Step 6 becomes **conditional** — if no audience is applied, "widen the audience" has nothing to widen; the agent must instead relax other targeting or state that the reach is inventory-bound.
>
> **⚠ To confirm with David:** (a) should Targeting sit **before** Budget Split? A natural reading of *"once inventory decided… then you are shown the default targeting"* says yes, and it is also logically necessary — the audience data fee (set during targeting) is an input to the accurate CPM that the split is meant to produce. (b) Does `GET /api/strategies/locations/{market}/` support **postcodes**, or only cities/regions? The postcode example depends on it.

## 💬 REPLY DRAFT
> This is the one that changes the shape of the flow, and I think you're right.
>
> Audiences and targeting answer the same question — who sees the ad — so having them as two steps was a mistake. I'll merge them: audiences become one targeting type alongside location, device and exclusions. That also lands the config-driven requirement properly, since one registry then covers all targeting types including audiences.
>
> The default-then-refine part is the bigger improvement. My design presented empty fields; yours shows what's already applied — country from the markets, Connected TV from the format, no audience — and lets the trader either refine or accept. **That actually follows this document's own "self-filling form" principle better than my version did.**
>
> Your postcode example makes the point sharply: with mandatory audiences, a postcode-only strategy was impossible. It shouldn't be.
>
> Two things I need from you:
> 1. Should Targeting sit **before** Budget Split? Your wording suggests it comes straight after inventory, and it's also logically necessary — the audience data fee is an input to the accurate CPM the split is meant to produce.
> 2. Does `GET /api/strategies/locations/{market}/` support **postcodes**, or only cities and regions? Your example depends on it.
>
> One consequence I'll document: if no audience is applied, the repair loop has nothing to widen. It'll need to relax other targeting instead, or state that reach is bound by the inventory.

## ❓ David se poochhne wale sawaal
| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | Targeting Budget Split se **pehle** aana chahiye? | Effective CPM ke liye audience fee pata hona chahiye — jo targeting me tay hoti hai |
| 2 | `GET /api/strategies/locations/{market}/` **postcodes** support karta hai? | David ka apna example postcode ka hai |
| 3 | Agar koi audience nahi hai to repair loop kya kare? | Widen karne ke liye kuch nahi hoga |

## 🏷️ Nichod
> **David keh raha hai:** *"Audience targeting ka hissa hai, alag cheez nahi. Aur khaali form ke bajaye ek default lagao — trader accept kare ya refine kare. Postcode audience ki jagah bhi chal sakta hai."*

**Severity: 🔴🔴 VERY HIGH** — do steps merge, naya interaction pattern, 13→12 steps, repair loop conditional, state machine badalna.

---
---

# 🔗 COMMENTS #3+#4+#5 KA JOD — Naya Flow

```
╔══════════════════════════════════════════════════════════════════════════╗
║  DOCUMENT KA FLOW (abhi)                                                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║  2. Inventory                                                            ║
║  3. Budget Split      ← REQUIRED     ❌ (Comment #3: optional hai)        ║
║  4. Audiences         ← MANDATORY    ❌ (Comment #4: optional hai)        ║
║  5. Targeting         ← optional, 5 khaali fields                        ║
║                         ❌ (Comment #5: audiences isme hona chahiye,      ║
║                             aur default pre-filled hona chahiye)          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  DAVID KA FLOW                                                           ║
╠══════════════════════════════════════════════════════════════════════════╣
║  2. Inventory (decided ya inferred)                                      ║
║       ↓                                                                  ║
║  3. TARGETING — default lagaya hua, refine ya accept                     ║
║       ├── Country: GB              (default, Step 1 se)                  ║
║       ├── Device: Connected TV      (default, CTV hai to)                 ║
║       ├── Audience segments         (optional — 3 options suggest)        ║
║       ├── Postcodes / locations     (optional)                            ║
║       ├── Content exclusions        (optional)                            ║
║       └── ... (config-driven, aur types add ho sakte hain)                ║
║       ↓                                                                  ║
║  4. Budget Split — OPTIONAL (par accurate CPM ke liye preferred)         ║
║       ↓                                                                  ║
║  5. Predict Reach                                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## ⚠ Ek sawaal: Targeting Budget Split se PEHLE ya BAAD?

David ke shabd: *"once inventory decided / inferred **then** you are shown the default targeting"* — "then" se lagta hai inventory ke **turant baad**.

**Aur ek strong logical reason bhi isi order ke liye:**
```
Comment #3: budget split "accurate CPM" ke liye chahiye
Comment #2: effective CPM = deal CPM + audience data fee

→ Accurate CPM ke liye AUDIENCE DATA FEE pata hona chahiye
→ Audience fee TARGETING me tay hoti hai
→ To TARGETING PEHLE, phir BUDGET SPLIT

Order: Inventory → Targeting → Budget Split → Forecast  ✅
```

**Par ye David se confirm karna hai** — assume nahi karna.

---
---

# 🧩 COMMENTS #6 · #7 · #8 · #9 — STEP 1 CLUSTER

> **Chaaron `Step 1: Basics` par hain.** Teen (#6, #7, #9) **ek hi baat** keh rahe hain:
> **"Itne sawaal poochhna band karo — jo khud samajh sakte ho wo samajh lo."**
>
> Ek (#8) **alag kism** ka hai — wo ek **scope sawaal** hai, correction nahi.
>
> Aur teeno ka **ek hi structural fix** hai: field matrix me **"Source" column** add karna (neeche jod section me).

---
---

# 🗨️ COMMENT #6 — "Simplify for CTV and imply answers"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → `What was in v1.1.0 (Step 1 + Step 2)` |
| **Highlighted** | **Poori do-bullet list** — "Strategy name, flight dates, target markets, primary currency, formats (all four), product categories, selling location, ASINs" + "Goal (three choices), KPI (six choices), ad tag conversions, market budgets, base bids" |
| **Asar** | 🔴 Step 1 ka **poora field matrix** (14 fields) |

## 💬 David ne exactly kya likha
> *"should **review** as a lot of this is for a **non CTV strategy** - can **simplify for CTV** and **imply answers**"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"should **review**"* | Is poori list ko **dobara dekho** |
| *"a lot of this is for a **non CTV strategy**"* | 🔴 Inme se **kai fields CTV ke liye nahi** — wo Display/Online Video ke zamane se aaye |
| *"can **simplify for CTV**"* | CTV ke liye list **chhoti** karo |
| *"and **imply answers**"* | 🔴 Jo bacha, uska jawab **khud nikalo** — poochho mat |

**"Imply"** = ishaare se samajh lena / khud nikaal lena. (= infer / derive)

## 🔍 Kaunse fields "non-CTV" hain — ek-ek
```
┌────────────────────────┬──────────────────────────────────────────────────┐
│ Field                  │ CTV ke liye kya haal hai                          │
├────────────────────────┼──────────────────────────────────────────────────┤
│ Strategy name          │ 🟡 Chahiye — par AUTO-GENERATE ho sakta (#7)      │
│ Flight dates           │ ✅ Chahiye — par brief se IMPLY ho sakta          │
│ Target markets         │ ✅ Chahiye — brief se IMPLY ho sakta              │
│ Primary currency       │ 🟡 Market se IMPLY ho sakta (#9)                  │
│ Formats (ALL FOUR)     │ ❌ NON-CTV! Display + online_video scope me nahi  │
│                        │    Aur CTV module me formats poochhna kyun?        │
│                        │    streaming_tv + prime_video by definition hai    │
│ Product categories     │ 🟡 ASIN validation response me AATA hai! IMPLY    │
│ Selling location       │ 🟡 Brief se IMPLY ("website" → NOT_SOLD_ON_AMAZON)│
│ ASINs                  │ 🟡 Sirf ON_AMAZON par · Step 11 me move hua       │
│ Goal (THREE choices)   │ ❌ NON-CTV! CTV = HAMESHA Awareness               │
│                        │    Teen choices dena hi galat hai                  │
│ KPI (SIX choices)      │ ❌ NON-CTV! CTV = sirf reach/frequency            │
│                        │    Chaar KPI (ctr/cpc/cpa/cpdpv) click-based hain │
│ Ad tag conversions     │ 🟡 Step 11 me move hua                            │
│ Market budgets         │ ✅ Chahiye — brief se IMPLY ho sakta              │
│ Base bids              │ 🟡 RATE CARD se DERIVE ho sakta! Kyun poochhna?   │
└────────────────────────┴──────────────────────────────────────────────────┘

Do saaf non-CTV: `formats (all four)` aur `Goal (3) / KPI (6)`
Baaki 9 fields me se lagbhag SAB imply ho sakte hain.
```

## 🔴 Sabse bada insight — "Base bid" bhi derive ho sakta hai
```
Document abhi: "Base bids | Table | Required"
                → Trader se poochho: "max CPM kitna dena hai?"

Par agent ke paas RATE CARD hai (GET /api/rates/ctv/{market}/):
  Prime Video 30s = £28.88
  Netflix 30s     = £32.00

→ Base bid rate card se HI nikal jaata hai!
  • Deal CPM ke barabar ya thoda upar (headroom)
  • Preferred Deal me CPM fixed hai anyway

Agent: "Base bid £32 rakh raha hun — tumhare chune hue deals ke
        highest CPM (Netflix £32) ke barabar. Isse dono deals par
        bid lag payegi. Badalna hai?"

🔴 AUR DOCUMENT KHUD MAANTA HAI KI AGENT SAHI NUMBER JAANTA HAI —
   Step 6 ka repair loop kehta hai:
   "Adjust base CPM bid up to market recommended floor
    (e.g. increase from £15 to £30 for Prime Video)"

   → Agar repair time par sahi floor pata hai, to SHURU ME HI laga do.
     Poochhne ki zaroorat kya hai?
```

## ✅ Poora "implied" Step 1 kaisa dikhega
```
Trader (ek sentence):
"BrightPath ke liye UK me August me £10,000 ka Prime Video awareness
 campaign chahiye, education website hai, 30 second ka ad."

──────────────────────────────────────────────────────────────────────
AGENT NE KHUD NIKALA (kuch bhi poochha nahi):

  strategy_name     = "BrightPath_Awareness_GB_Aug2026"   ← generate (#7)
  markets           = ["GB"]                              ← "UK" se
  primary_currency  = "GBP"                               ← GB se (#9)
  flight_dates      = 2026-08-01 → 2026-08-31             ← "August" se
  market_budgets    = [{GB, "10000.00"}]                  ← "£10,000" se
  base_bid          = "28.88"                             ← rate card se
  formats           = ["prime_video"]                     ← "Prime Video" se
  durations         = ["30"]                              ← "30 second" se
  goal              = "AWARENESS"                         ← CTV = fixed
  kpi               = "reach"                             ← awareness default
  product_location  = "NOT_SOLD_ON_AMAZON"                ← "website" se
  product_categories= [1] (Education)                     ← "education" se

  → 12 me se 12 fields BHAR GAYE. Ek bhi sawaal nahi poochha.
──────────────────────────────────────────────────────────────────────

Agent: "Samajh gaya — ye plan bana raha hun:
        [table with all 12 values]
        Ye maine tumhare brief se nikala. Kuch galat ho to batao,
        warna main inventory par chala jaata hun."
```

**🔴 Ye Step 1 ko ek FORM se ek SUMMARY-TO-CONFIRM me badal deta hai.**

## 🎯 Kyun ye comment kiya
```
Wajah 1 — Field list CTV ke liye purani hai
  v1.1.0 saare formats cover karta tha. v2.0 ne scope CTV kiya PAR
  field list poori tarah CTV ke hisaab se REVIEW nahi ki.
  → "formats (all four)" aur "KPI (six choices)" ab bhi list me hain

Wajah 2 — Document apna hi Principle #2 follow nahi kar raha
  "Self-Filling Form Paradigm — a form that fills itself in as you chat"
  → Par Step 1 me 14 fields "Required" hain, jaise trader ko sab bharna hai
  → Ye ek FORM hai, "self-filling form" nahi

Wajah 3 — 14 sawaal se trader bhaag jaayega
  Purana wizard 20-30 minute leta tha. Agar agent bhi 14 sawaal
  poochhega, to faayda kya hua?
```

## 🏷️ Nichod
> **David keh raha hai:** *"Step 1 ki field list CTV ke liye review karo — kai fields non-CTV hain. Aur jo bache, unke jawab khud nikalo, poochho mat."*

**Severity: 🔴🔴 VERY HIGH** — poora Step 1 ka design badalta hai.

---
---

# 🗨️ COMMENT #7 — "Strategy name could be auto generated from brief"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Strategy name** |
| **Highlighted** | **"Required"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"could be **auto generated from brief**"*

## 🔴 Chhota comment, BADA structural insight

David ne **"Required"** highlight kiya aur kaha "auto generated ho sakta hai."

```
╔══════════════════════════════════════════════════════════════════════════╗
║  DOCUMENT KE FIELD MATRIX ME EK COLUMN GAYAB HAI                         ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Abhi jo column hai:                                                     ║
║    "Requirement"  →  kya ye value ZAROORI hai?  (Required/Optional)      ║
║                                                                          ║
║  🔴 Jo column NAHI hai:                                                  ║
║    "Source"       →  ye value KAHAN SE aayegi?                           ║
║                      (Asked / Inferred / Derived / Generated / Fixed)     ║
║                                                                          ║
║  Ye DO ALAG sawaal hain!                                                 ║
║  "Required" ka matlab NAHI hai "trader ko type karna padega."             ║
║  "Required" ka matlab hai "value maujood honi chahiye."                   ║
║  Kaun degi — ye ALAG sawaal hai.                                         ║
╚══════════════════════════════════════════════════════════════════════════╝

Strategy name ka case:
  Requirement:  Required   ✅ (naam zaroori hai)
  Source:       GENERATED  ← trader ko type karne ki zaroorat NAHI
  → Dono saath me sach hain. Koi virodh nahi.
```

## ✅ Naam kaise auto-generate hoga
```
Pattern: advertiser + goal + market + month + year

"BrightPath, UK, August 2026, Prime Video, awareness"
   → "BrightPath_Awareness_GB_Aug2026"

Ya document ka apna pattern (Season_Objective_Year):
   → "Summer_Brand_Awareness_2026"

Uniqueness check automatic:
  Agent → GET /api/strategies/check_strategy_name_uniqueness/
          ?name=BrightPath_Awareness_GB_Aug2026
       ← {"is_unique": false}
  Agent (khud): "_v2" lagata hai → dobara check → ✅
  Agent: "Naam 'BrightPath_Awareness_GB_Aug2026_v2' rakha hai
          (v1 pehle se thi). Badalna hai?"

⚠ Document ka §7.2 protocol already kehta hai:
  "append timestamp or suffix e.g. Name_v2 AND PROMPT USER"
  → Yaani auto-generate karo par DIKHA do. Consistent hai.
```

## 🎯 Kyun ye comment kiya
```
Wajah 1 — Naam ek chore hai, decision nahi
  Trader ko planning ke waqt naam ki parwah nahi. Wo baad me
  dhoondhne ke liye chahiye. Agent sensible naam bana de.

Wajah 2 — Consistent naming milegi
  Agent generate karega → sab strategies ek pattern me → dhoondhna aasan
  (Trader khud rakhega to: "test", "test2", "abc", "final_FINAL")

Wajah 3 — Ek sawaal kam (Comment #6 ka extension)
```

## 🏷️ Nichod
> **David keh raha hai:** *"Strategy name brief se khud bana lo."*

**Severity: 🟡 MEDIUM** — fix chhota hai, par jo insight isse nikla (**Required ≠ Asked**) bahut bada hai.

---
---

# 🗨️ COMMENT #8 — "Multi-market: support karenge? Flow par kya asar?"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Target markets** |
| **Highlighted** | **"Multi-select"** (Type column) |

## 💬 David ne exactly kya likha
> *"Are we going to **support multi market**? what **impact to the flow** will it have - **repeating choices for each market**?"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"Are we going to **support multi market**?"* | Ek se zyada desh **support karenge kya**? *(SCOPE sawaal)* |
| *"what **impact to the flow** will it have"* | Agar haan, to **flow par kya asar**? |
| *"**repeating choices for each market**?"* | 🔴 Kya har market ke liye **saare choices dobara** karne padenge? |

## 🔴 Ye baaki comments se ALAG KISM ka hai
```
#1,#2,#3,#4,#5,#6,#7,#9 → CORRECTION ("ye galat hai, theek karo")
#8                      → SAWAAL ("ye socha hai? design kya hai?")

→ Iska jawab "haan theek kar dunga" NAHI ho sakta
→ Iska jawab ek DESIGN DECISION hona chahiye
```

## 🔴 Multi-market poore flow ko GUNA kar deta hai
```
┌───────────────────────┬──────────────────────────────────────────────────┐
│ Cheez                 │ markets = ["GB","FR"] par kya hota hai            │
├───────────────────────┼──────────────────────────────────────────────────┤
│ market_budgets        │ ✅ Pehle se per-market (table)                    │
│ base_bids             │ ✅ Pehle se per-market                            │
├───────────────────────┼──────────────────────────────────────────────────┤
│ 🔴 DEALS              │ ALAG! Netflix GB ≠ Netflix FR                     │
│                       │ GET /api/deals/?markets={market}  ← SINGULAR      │
│ 🔴 AUDIENCES          │ ALAG segments per market                          │
│                       │ POST suggest/  {"market": "GB"}  ← 🔴 SINGULAR!   │
│ 🔴 RATE CARD          │ GET /api/rates/ctv/{market}/  ← SINGULAR          │
│ 🔴 LOCATIONS          │ London vs Paris                                   │
│                       │ GET /api/strategies/locations/{market}/ ← SINGULAR│
│ 🔴 PRODUCT CATEGORIES │ /contextual-targeting/{market}/... ← SINGULAR     │
│ 🔴 ASIN VALIDATION    │ /contextual-targeting/{market}/... ← SINGULAR     │
│ 🔴 CURRENCY           │ GB=GBP, FR=EUR — "primary" kaunsa? (#9 se juda)  │
│ 🔴 CREATIVES          │ Language! French video chahiye?                   │
│ 🔴 FORECAST           │ Alag forecast per market                          │
│ 🔴 BUDGET SPLIT       │ Ab 3 DIMENSION: market × inventory × duration     │
│ 🔴 CREATIVE APPROVAL  │ Per market? Per platform per market?              │
└───────────────────────┴──────────────────────────────────────────────────┘
```

### 🔴 Do CONCRETE GAPS jo isse nikalte hain

**Gap 1 — Saare APIs SINGULAR market lete hain, par schema PLURAL hai**
```
Schema:  markets: list[str] = ["GB", "FR"]      ← PLURAL

Par APIs:
  GET  /api/deals/?markets={market}                          ← singular template
  POST /api/audience-sets/suggest/  {"market": "GB"}          ← 🔴 SINGULAR field!
  GET  /api/rates/ctv/{market}/                              ← singular
  GET  /api/strategies/locations/{market}/                   ← singular
  GET  /api/contextual-targeting/{market}/product-categories/ ← singular
  POST /api/contextual-targeting/{market}/asin-validation/    ← singular

→ Multi-market me agent ko HAR API N BAAR call karna padega
→ Aur N sets of results manage karne padenge
→ Document ne ye KAHIN NAHI likha!
```

**Gap 2 — `BudgetSplitSchema` me `by_market` NAHI hai**
```python
class BudgetSplitSchema(BaseModel):
    method: BudgetSplitMethodEnum
    by_inventory: list[dict]      # ✅ hai
    by_duration: list[dict]       # ✅ hai
    # by_market: ???              # 🔴 NAHI HAI!

Multi-market me budget TEEN tarah se baantna padega:
  GB me kitna, FR me kitna         ← by_market (MISSING)
  Prime me kitna, Netflix me kitna ← by_inventory
  15s me kitna, 30s me kitna       ← by_duration

→ 2 markets × 2 inventories × 2 durations = 8 lines!
```

### ⚠ Dilchasp — v2.0 ne multi-market ADD kiya, par flow nahi socha
```
Document ka §7.1 (Brief Parsing):
┌───────────────┬────────────────────────┬────────────┐
│ UK and France │ markets: ["GB", "FR"]  │ ➕ NEW     │
└───────────────┴────────────────────────┴────────────┘
                                            ↑
                        v2.0 ne ye JAAN BOOJH KAR add kiya!

→ Yaani v2.0 ne multi-market explicitly SCOPE me daala
→ Par uska flow impact kahin analyse nahi kiya
→ YAHI David pakad raha hai
```

### ✅ Ek achhi khabar — reach ADD kar sakte ho (3P ke ULAT)
```
3P inventory par reach ADD nahi kar sakte
  → WAHI insaan Prime aur Netflix dono dekh sakta hai
  → cross-platform deduplication possible nahi

PAR multi-market me reach ADD KAR SAKTE HO
  → GB ka banda aur FR ka banda ALAG log hain
  → GB reach 118,000 + FR reach 82,000 = 200,000 ✅ VALID

→ Ye ek accha farak hai jo document me LIKHNA chahiye
```

## 🤔 Iska jawab — 3 options
| Option | Kya hai | Faayda | Nuksaan |
|---|---|---|---|
| **A: M1 = single market only** | Multi-market M2 me | ✅ Simple · APIs se match | ❌ v2.0 ne multi-market parsing add kiya tha — hatana padega |
| **B: M1 = full multi-market** | Sab per-market | ✅ Complete | ❌ Effort **kai guna** · N× API calls · 3D budget split · testing bahut |
| **C: N parallel plans** | Basics shared, baaki per-market | ✅ Beech ka raasta | 🟡 UI complex — side-by-side |

### 💡 Recommendation: **A ab, par schema B ke liye taiyar rakho**
```
M1 me:
  markets: list[str]   ← SCHEMA me PLURAL rakho (badalna na pade)
  Par FLOW me: agar len(markets) > 1 → agent bole:
    "Multi-market campaigns M1 me support nahi hain. Main GB ke liye
     plan banata hun. FR ke liye alag strategy banani padegi.
     Ya ek market chuno."

Kyun behtar:
  ✅ M2 me multi-market aane par schema migration nahi
  ✅ M1 jaldi deliver
  ✅ Trader ko saaf pata (Zero-Hallucination — jo nahi hai, bata do)
  ✅ APIs ke saath consistent (sab singular hain)

⚠ Par ye faisla David/client ka hai — assume nahi karna.
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | Step 1 — Target markets | Scope decision document karo: M1 me single ya multi? |
| 2 | ➕ Naya section | "Multi-market handling" — kya repeat hota hai, kya shared |
| 3 | §4 API catalogue | ⚠ Note: saare market-scoped APIs **singular** lete hain → multi-market me N calls |
| 4 | `BudgetSplitSchema` | 🔴 `by_market` field add karo (agar multi-market in scope) |
| 5 | Step 6 (forecast) | ➕ Note: cross-**market** reach ADD kar sakte ho (cross-**platform** nahi) |
| 6 | §7.1 normalisation | "UK and France" — agar M1 single-market, isko future-scope mark karo |
| 7 | Step 9 (creatives) | ⚠ Multi-market me language/creative per market ka sawaal |
| 8 | Agent behaviour | Multi-market brief aane par kya bole — define karo |

## 🏷️ Nichod
> **David puchh raha hai:** *"Multi-market support kar rahe ho? Uska flow par kya asar hai? Har market ke liye sab dobara?"*

**Severity: 🔴 HIGH** — scope decision chahiye + 2 concrete gaps nikle (singular APIs, `by_market` missing).

---
---

# 🗨️ COMMENT #9 — "Just use market currency if single market"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Primary currency** |
| **Highlighted** | **"Required"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"just use **market currency** if **single market**"*

## 🔍 Matlab
```
Agar sirf EK market hai, to us market ki currency HI use karo.
Poochhne ki zaroorat nahi.

markets = ["GB"]  →  currency = GBP    (automatic)
markets = ["US"]  →  currency = USD    (automatic)
markets = ["DE"]  →  currency = EUR    (automatic)
markets = ["FR"]  →  currency = EUR    (automatic)

markets = ["GB","FR"]  →  AB sawaal banta hai (GBP ya EUR?)
```

**"Primary currency" ka naam hi batata hai ki ye multi-market ka concept hai** — "primary" = kai me se main wali. Single market me "primary" ka koi matlab hi nahi!

## 🔴 SABSE ZAROORI — Document ye PEHLE SE karta hai!
```
Document ka §7.1 (Entity Normalisation):
┌───────┬───────────────────────────────────────────────┬────────────┐
│ Input │ Extraction                                     │ Status     │
├───────┼───────────────────────────────────────────────┼────────────┤
│ UK    │ markets: ["GB"], primary_currency: "GBP"      │ ✅ Original │
│                          ↑                                          │
│           🔴 CURRENCY MARKET SE DERIVE HO RAHI HAI — PEHLE SE!      │
└───────┴───────────────────────────────────────────────┴────────────┘

PAR Step 1 field matrix kehta hai:
  "Primary currency | Dropdown | REQUIRED | ✅ Unchanged. EUR, GBP, USD"
                       ↑           ↑
                   "Dropdown"  "Required"  → trader ko CHUNNA hai!

╔══════════════════════════════════════════════════════════════════════╗
║  🔴 DOCUMENT APNE AAP SE CONTRADICT KAR RAHA HAI:                    ║
║  §7.1 kehta hai:   "UK se currency GBP KHUD nikal jaati hai"         ║
║  Step 1 kehta hai: "Trader dropdown se currency CHUNEGA"             ║
║  Dono ek saath sach nahi ho sakte.                                   ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 🤔 Multi-market me kya rule ho? (document me kuch nahi)
```
Option A: Trader se poochho
  "GB aur FR dono hain. Reporting kis currency me?"
  ✅ Saaf · ❌ ek extra sawaal

Option B: Advertiser ke account ki default currency
  ✅ Sabse sensible — advertiser ki accounting usi me hoti hai
  ✅ Koi sawaal nahi
  ⚠ Par ye field/API document me hai hi nahi

Option C: Sabse bade budget wale market ki currency
  GB £6,000, FR £4,000 → GBP
  ✅ Koi sawaal nahi · 🟡 thoda arbitrary

💡 Suggestion: B → C → A, aur HAMESHA dikhao as assumption:
  "Reporting GBP me (advertiser ka account currency). Badalna hai?"
```

## 🔧 Kya fix karna hai
| # | Jagah | Abhi | Naya |
|---|---|---|---|
| 1 | Step 1 — Primary currency Type | **Dropdown** | **Derived** (single market) / Dropdown (multi) |
| 2 | Step 1 — Requirement | **Required** | **Required** — par Source = **DERIVED from market** |
| 3 | Step 1 — naya note | — | ➕ Single market → market currency automatic |
| 4 | ⚠ Multi-market rule | Kuch nahi likha | ➕ Rule define karo (account default → largest budget → ask) |
| 5 | §7.1 aur Step 1 | Contradict kar rahe hain | 🔄 Reconcile karo |

## 🏷️ Nichod
> **David keh raha hai:** *"Single market me us market ki currency use karo. Poochho mat."*

**Severity: 🟡 MEDIUM** — fix chhota, par document apne aap se contradict kar raha hai.

---
---

# 🔗 COMMENTS #6+#7+#9 KA JOD — Ek Structural Solution

## Teen comments ek hi cheez maang rahe hain
```
#6: "imply answers"
#7: "could be auto generated from brief"
#9: "just use market currency if single market"

→ TEENO KEH RAHE HAIN: POOCHHO MAT, NIKAALO.
```

## 💡 Ek structural fix teeno ko solve karta hai — **"Source" column**

> **Ye Kareem ki sabse achhi contribution ho sakti hai is review me.**

```
╔══════════════════════════════════════════════════════════════════════════╗
║  HAR FIELD MATRIX ME EK NAYA COLUMN: "SOURCE"                            ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Abhi:  Field | Type | Requirement | Change from v1.1.0                  ║
║  Naya:  Field | Type | Requirement | SOURCE | Change from v1.1.0         ║
║                                        ↑                                 ║
║  Source ki values:                                                       ║
║    💬 ASKED      → trader se poochhna padega                             ║
║    🧠 INFERRED   → brief ke text se nikala (parsing)                     ║
║    ⚙️ DERIVED    → doosre field se nikala (market → currency)            ║
║    🤖 GENERATED  → agent ne banaya (strategy name)                       ║
║    🔒 FIXED      → CTV ke liye constant (goal = AWARENESS)               ║
║    🔌 API        → API response se aaya (product_category ASIN se)       ║
║                                                                          ║
║  🎯 Isse "Required" aur "Asked" ka confusion KHATAM ho jaata hai         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## Naya Step 1 field matrix — Source column ke saath
```
┌─────────────────────┬────────────┬─────────────┬────────────────────────────┐
│ Field               │ Type       │ Requirement │ SOURCE                     │
├─────────────────────┼────────────┼─────────────┼────────────────────────────┤
│ Strategy name       │ String     │ Required    │ 🤖 GENERATED (editable) #7 │
│ Flight dates        │ Date range │ Required    │ 🧠 INFERRED from brief     │
│ Target markets      │ Multi-sel  │ Required    │ 🧠 INFERRED from brief     │
│ Primary currency    │ —          │ Required    │ ⚙️ DERIVED from market  #9  │
│ Creative durations  │ Multi-sel  │ Required    │ 🧠 INFERRED from brief     │
│ Goal                │ —          │ Required    │ 🔒 FIXED = AWARENESS       │
│ KPI                 │ Select     │ Required    │ ⚙️ DERIVED from goal       │
│                     │            │             │    (default: reach)         │
│ Formats             │ —          │ Required    │ 🔒 FIXED = CTV formats  #6  │
│ Product categories  │ Multi-sel  │ Required    │ 🧠 INFERRED / 🔌 API   #6   │
│ Selling location    │ Radio      │ Required    │ 🧠 INFERRED from brief     │
│ Market budgets      │ Table      │ Required    │ 🧠 INFERRED from brief     │
│ Base bids           │ Table      │ Required    │ ⚙️ DERIVED from rate card #6│
│ Frequency cap       │ Number     │ Optional    │ 💬 ASKED (if wanted)       │
│ Budget cap          │ Number     │ Optional    │ 💬 ASKED (if wanted)       │
└─────────────────────┴────────────┴─────────────┴────────────────────────────┘

🔴 DEKHO — 14 fields me se ZERO "ASKED-and-Required" hain!
   Sab inferred/derived/generated/fixed hai.
   Sirf 2 OPTIONAL fields hain jo trader chahe to bataye.

→ YAHI "self-filling form" hai. Yahi David chahta hai.
```

---

## ✍️ DOCUMENT NOTES — #6, #7, #8, #9

### Note — Comment #6 (+ #7, #9 ka structural fix)
> **📝 NOTE — Step 1 field list must be reviewed for CTV, and answers implied (David Moss)**
>
> The v1.1.0 list above carries fields that exist because v1.1.0 covered Display and Online Video. For a CTV-only module, several are either out of scope or should not be asked at all. Two corrections:
>
> **1. Fields that are non-CTV and should not be presented as choices:**
>
> | Field | Problem | Correction |
> |---|---|---|
> | `formats` (all four) | Display and online_video are out of scope; in a CTV module the formats are known | **FIXED** to `streaming_tv` / `prime_video` — not asked |
> | `goal` (three choices) | CTV is always Awareness (client-confirmed) | **FIXED** to `AWARENESS` — not asked |
> | `kpi` (six choices) | Four of the six are click-based and impossible on CTV | Scoped to `reach` / `frequency`, defaulted from goal |
>
> **2. A missing column: `Source`.** The field matrices record *whether* a value is required, but never *where it comes from*. "Required" has been read as "the trader must supply it" — these are two different things. A value can be required **and** supplied by the agent.
>
> All field matrices in this document should carry a **Source** column with one of:
>
> | Source | Meaning | Example |
> |---|---|---|
> | 💬 **ASKED** | The trader must supply it | Frequency cap (if wanted) |
> | 🧠 **INFERRED** | Parsed from the brief text | `"UK"` → `markets: ["GB"]` |
> | ⚙️ **DERIVED** | Computed from another field | `markets: ["GB"]` → `primary_currency: "GBP"` |
> | 🤖 **GENERATED** | Produced by the agent | Strategy name |
> | 🔒 **FIXED** | Constant for CTV | `goal = AWARENESS` |
> | 🔌 **API** | Returned by an API call | `product_category` from ASIN validation |
>
> **Applied to Step 1, this produces:** *(see revised matrix)* — **no field is ASKED-and-Required.** Everything is inferred, derived, generated or fixed. The only asked fields are the two optional caps. That is what "a form that fills itself in as you chat" means in practice, and the current matrix does not express it.
>
> **Additional implication — base bids.** `Base bids` is currently Required. It can be **DERIVED from the CTV rate card** (`GET /api/rates/ctv/{market}/`) — set at or just above the highest selected deal CPM. The document already assumes the agent knows the right value: Step 6's repair loop says *"increase from £15 to £30 for Prime Video."* If the agent knows the correct floor at repair time, it should apply it at the start instead of asking.

### Note — Comment #7 (Strategy name)
> **📝 NOTE — Strategy name is generated, not asked (David Moss)**
>
> `Strategy name` remains **Required** — a strategy cannot exist without one — but its **Source is GENERATED**, not asked. The agent composes it from the brief:
>
> ```
> advertiser + goal + market + month + year
> → "BrightPath_Awareness_GB_Aug2026"
> ```
>
> The uniqueness check runs automatically (`GET /api/strategies/check_strategy_name_uniqueness/`), and on collision the agent appends a suffix and **tells the trader** — consistent with the existing duplicate-name protocol in §7.2 (*"append suffix… and prompt user"*). The trader can override the generated name at any point.
>
> **Why generated rather than asked:** the name is a retrieval label, not a planning decision. Traders do not care about it while planning, and agent-generated names are consistently formatted, which makes later search reliable.

### Note — Comment #8 (Multi-market)
> **📝 NOTE — Multi-market support: scope decision required (David Moss)**
>
> `Target markets` is typed **Multi-select**, and §7.1 explicitly adds *"UK and France → `markets: ["GB", "FR"]`"* as a ➕ NEW parsing rule — so v2.0 brought multi-market into scope. **But the flow consequences were never worked through.** They are substantial.
>
> **What repeats per market:**
>
> | Already per-market | 🔴 Would need to repeat per market |
> |---|---|
> | `market_budgets` · `base_bids` | Deals · Audiences · Rate card · Locations · Product categories · ASIN validation · Forecast · Creatives (language) · Creative approval |
>
> **Two concrete gaps this exposes:**
>
> 1. **Every market-scoped API takes a single market**, not a list:
>    `GET /api/deals/?markets={market}` · `POST /audience-sets/suggest/` with `{"market": "GB"}` · `GET /api/rates/ctv/{market}/` · `GET /api/strategies/locations/{market}/` · `GET|POST /api/contextual-targeting/{market}/…`
>    Multi-market therefore means **N calls per step**, and N result sets to hold and present. The document never states this.
>
> 2. **`BudgetSplitSchema` has no `by_market`.** It has `by_inventory` and `by_duration` only. Multi-market makes the split **three-dimensional** — market × inventory × duration. Two markets, two inventories and two durations is eight lines.
>
> **One clarification worth recording:** unlike the cross-platform case, **reach can be summed across markets** — a GB viewer and an FR viewer are different people, so there is no deduplication problem. This is the opposite of the Prime + Netflix case in Step 6, and both should be stated explicitly.
>
> **Recommended decision (for David/client to confirm):** keep `markets: list[str]` in the schema so nothing has to change later, but **constrain M1 to a single market in the flow**. If a brief names more than one, the agent says so plainly and offers to plan the first market, with the others as separate strategies. This matches the single-market shape of every relevant API, keeps M1 deliverable, and avoids a schema migration when multi-market lands.

### Note — Comment #9 (Primary currency)
> **📝 NOTE — Primary currency is derived, not asked (David Moss)**
>
> `Primary currency` is currently typed **Dropdown / Required**, implying the trader selects it. **For a single market it should be derived from that market** — `GB → GBP`, `US → USD`, `DE|FR → EUR`. The term "primary" only has meaning when there is more than one currency in play.
>
> **This already contradicts §7.1**, which lists `UK → markets: ["GB"], primary_currency: "GBP"` as an original ✅ parsing rule. The parsing section derives it; the field matrix asks for it. The matrix is wrong.
>
> **Corrected:** Requirement stays **Required**; Source becomes **DERIVED from market**.
>
> **Multi-market rule (currently undefined, needs a decision):** in order of preference — (1) the advertiser account's default currency, (2) the currency of the largest-budget market, (3) ask. In all cases the agent should **show it as an assumption**: *"Reporting in GBP — the advertiser's account currency. Change it?"*

---

## 💬 REPLY DRAFTS — #6, #7, #8, #9

### Reply — Comment #6
> Agreed, and this is the right thing to pull on.
>
> Two separate problems in that list. First, some of it is genuinely non-CTV and shouldn't be a choice at all — `formats (all four)` when Display and online video are out of scope, `goal (three choices)` when CTV is always Awareness, `KPI (six choices)` when four of them are click-based. Those become fixed, not asked.
>
> Second, and the bigger one: **the field matrices record whether a value is required but never where it comes from**, and "Required" has been reading as "the trader types it". Those are different things. I'm adding a **Source** column to every matrix — `ASKED / INFERRED / DERIVED / GENERATED / FIXED / API`.
>
> When I apply that to Step 1, **no field is asked-and-required**. Name is generated, market and dates and budget are inferred from the brief, currency is derived from market, goal and formats are fixed, product category comes back from ASIN validation, and base bid can be derived from the rate card. Only the two optional caps are actually asked. That's what "a form that fills itself in" should look like, and my matrix wasn't expressing it.
>
> On base bids specifically — Step 6's repair loop already says *"increase from £15 to £30 for Prime Video"*, so the agent evidently knows the right floor. If it knows it at repair time it should apply it up front rather than asking.

### Reply — Comment #7
> Yes — I'll mark it **Required with Source = GENERATED**, composed from the brief (`advertiser_goal_market_month_year`), with the uniqueness check running automatically and a suffix appended on collision. That's already covered by the duplicate-name protocol in §7.2, which says append and prompt — so the trader always sees the name and can override it.
>
> The reasoning I'll record: the name is a retrieval label, not a planning decision. Traders don't care about it while planning, and generated names come out consistently formatted, which makes searching later actually work.

### Reply — Comment #8
> Fair question, and I hadn't worked it through. §7.1 adds *"UK and France → ["GB","FR"]"* as a new parsing rule, so v2.0 pulled multi-market into scope without me tracing the consequences.
>
> Tracing them now: **budgets and base bids are already per-market, but deals, audiences, rate card, locations, product categories, ASIN validation, forecast, creatives (language) and creative approval would all repeat.** Two concrete gaps fall out of that:
>
> 1. **Every market-scoped API takes a single market, not a list** — `/deals/?markets={market}`, `suggest/` with `{"market":"GB"}`, `/rates/ctv/{market}/`, `/locations/{market}/`, `/contextual-targeting/{market}/…`. So multi-market means N calls per step and N result sets to hold and present. Nowhere in the document says that.
> 2. **`BudgetSplitSchema` has no `by_market`** — only `by_inventory` and `by_duration`. Multi-market makes the split three-dimensional. Two markets × two inventories × two durations is eight lines.
>
> One thing worth recording either way: **reach can be summed across markets**, unlike across platforms — a GB viewer and an FR viewer are different people, so there's no dedup problem. That's the opposite of the Prime + Netflix case in Step 6 and both should be stated.
>
> **My recommendation:** keep `markets: list[str]` in the schema so nothing has to migrate later, but **constrain M1 to a single market in the flow**. If a brief names two, the agent says so and offers to plan the first, with the second as a separate strategy. That matches the single-market shape of every relevant API and keeps M1 deliverable. Happy to go the other way if you want multi-market in M1 — but it's a materially bigger build, and I'd want that decided now rather than discovered later.

### Reply — Comment #9
> Agreed — and this one already contradicts my own document. §7.1 lists `UK → markets: ["GB"], primary_currency: "GBP"` as a parsing rule, so the currency is derived there, while the Step 1 matrix says Dropdown/Required. The matrix is wrong.
>
> Changing it to **Required, Source = DERIVED from market**. "Primary" only means anything when there's more than one currency in play.
>
> For multi-market I'll define the rule, since there isn't one today: advertiser account default currency first, else the largest-budget market's currency, else ask — and always shown as an assumption the trader can change.

---
---

# 🧩 COMMENTS #10 · #11 · #12 · #13 — STEP 1 MATRIX CLUSTER (part 2)

> **Chaaron `Step 1` ke field matrix par hain** — #6–#9 ka agla hissa (wahi table, aage ke rows).
>
> **Par isme ek NAYA FLAVOUR hai:** ab tak sab comments *"hatao / loosen karo / infer karo"* the.
> **#10 pehla comment hai jo kehta hai "kuch ADD karo"** — ek missing field.
>
> **Aur #12 sabse khatarnak hai** — wo repair loop ka ek lever tod deta hai.

---
---

# 🗨️ COMMENT #10 — "If frequency then you can have kpi target too of 1-5"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **KPI** |
| **Highlighted** | **"KPI"** (Field column — poora field) |

## 💬 David ne exactly kya likha
> *"**if frequency** then you can have **kpi target too** of **1-5**"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"**if frequency**"* | Agar KPI = `frequency` chuna |
| *"then you can have **kpi target too**"* | 🔴 To ek **KPI target bhi** ho sakta hai (**naya field!**) |
| *"of **1-5**"* | Uski value **1 se 5** ke beech |

## ❌ Document me KYA GAYAB hai
```
Document abhi:
  KPI | Select | Required | 🔄 CHANGED. For CTV, reach or frequency only.

Sirf ye pata chalta hai: KAUNSA metric naapna hai
  kpi_target_type = "reach"  ya  "frequency"

Par ek aur field chahiye:
  kpi_target_value = 3        ← KITNA target hai (1-5)   ← MISSING
```

## 🔴 PROOF 1 — Field ka naam hi bata raha hai
```
Schema me field ka naam:
    kpi_target_type: KPIEnum
        ↑        ↑
      "target"  "TYPE"

  🔴 "TYPE" likha hai — matlab ek "VALUE" bhi hona chahiye!

  kpi_target_type  = "frequency"   ← KAUNSA target
  kpi_target_value = 3             ← KITNA target    ← MISSING!

→ Field ka naam khud saabit karta hai ki ek field gayab hai.
```

## 🔴 PROOF 2 — Repair loop ek target ka zikr karta hai jo EXIST NAHI KARTA
```
Document ke DO jagah "target" ka zikr hai:

1. v1.1.0 §6.2 (state machine mermaid):
   "EvaluateReach: Check if reach > 0 and FREQUENCY WITHIN TARGETS"
                                          ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

2. v1.1.0 §7.1 (repair loop):
   "If POST /api/strategies/reach-forecast/ returns
    estimated_unique_reach == 0 OR INSUFFICIENT FREQUENCY"
                                  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

╔══════════════════════════════════════════════════════════════════════╗
║  🔴 DONO JAGAH "TARGET" SE COMPARE KARNE KI BAAT HAI —                ║
║     PAR SCHEMA ME KOI TARGET FIELD HI NAHI HAI!                       ║
║                                                                      ║
║  Repair loop kaise check karega "frequency within targets"?           ║
║  Kis number se compare karega?                                        ║
║                                                                      ║
║  → Repair loop ka ek hissa IMPLEMENTABLE HI NAHI HAI                  ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 🔴 Frequency TARGET vs Frequency CAP — bilkul alag cheezein
```
╔══════════════════════════════════════════════════════════════════════════╗
║  FREQUENCY TARGET (1-5)          vs          FREQUENCY CAP               ║
╠══════════════════════════════════════════════════════════════════════════╣
║  "Main CHAHTA hun ki average             "Koi banda 3 baar se ZYADA      ║
║   frequency ~3 ho"                        na dekhe"                      ║
║                                                                          ║
║  = OPTIMISATION GOAL (nishaana)          = HARD LIMIT (chhat)            ║
║  = DSP delivery ko PACE karta hai        = DSP 4th impression BLOCK      ║
║    taaki ye average aaye                   kar deta hai                  ║
║  = "iski taraf badho"                    = "isse aage mat jao"           ║
║                                                                          ║
║  ➡ AIM                                    ➡ CEILING                      ║
╚══════════════════════════════════════════════════════════════════════════╝

Real example:
  TARGET = 3 → kuch log 1 baar, kuch 5 baar, kuch 3 baar dekhenge
               AVERAGE 3 aayega. Koi 7 baar bhi dekh sakta hai!
  CAP = 3    → KOI BHI 4th baar NAHI dekhega
               Average 3 se KAM hoga
```

### ⚠ Validation rule jo chahiye (document me nahi hai)
```
Agar target = 4 aur cap = 3?
→ 🔴 VIRODH! Average 4 kaise aayega jab maximum 3 hai?
→ Mathematically impossible

Rule: frequency_cap > kpi_target_value

🔗 Aur ye Comment #13 se juda hai — wahan David kehta hai frequency cap
   ka ADVERTISER DEFAULT hota hai.
   → Advertiser ka default cap 3, trader target 4 rakhta hai
   → Agent ko TURANT flag karna chahiye (trader ne kuch galat kiya bhi nahi!)
```

## 🔴 Kyun sirf frequency ka target, reach ka nahi?
```
FREQUENCY = CONTROLLABLE
  DSP delivery ko pace kar sakta hai. "Is bande ko 3 baar dikhao, phir
  doosre par jao." Ye DSP ki asli capability hai.
  → Tum target DE sakte ho, DSP usko HIT karne ki koshish karega

REACH = OUTCOME
  Reach depend karta hai budget, audience, inventory, CPM par.
  Tum "200,000 reach chahiye" nahi bol sakte — wo NIKALTA hai, set nahi hota.
  → Isliye reach ka numeric target nahi hota

╔══════════════════════════════════════════════════════════════════╗
║  Frequency ek DIAL hai (ghumao)                                  ║
║  Reach ek METER hai (padho)                                      ║
╚══════════════════════════════════════════════════════════════════╝

→ Isliye David ne kaha "IF frequency then..." — sirf frequency ke case
  me target ka matlab banta hai.
```

## ✅ Agent ka naya behaviour
```
Trader: "Frequency KPI chahiye"

Agent: "Theek hai, KPI = frequency. Target average frequency kitni
        rakhun? (1 se 5 ke beech)

        Guide:
          1-2  → chaudi reach, halka message (awareness ke shuru me)
          3    → 🟢 sabse aam — yaad rakhne ke liye kaafi
          4-5  → gehra impact, par kam log AUR ad fatigue ka khatra

        Main 3 recommend karta hun.

        ⚠ Dhyan do: advertiser ka default frequency CAP 3 hai. Agar
          tum target 4 rakhoge, wo hit nahi hoga (cap 3 par rok dega).
          Target 4 chahiye to cap bhi badhana padega."
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Step 1 field matrix** | ➕ Naya row: `KPI target value` · Number · **Conditional** (Required if KPI = frequency) · Range 1–5 |
| 2 | **`FullStrategySchema`** | ➕ `kpi_target_value: Optional[int] = Field(None, ge=1, le=5)` |
| 3 | **`PlanningAgentState`** | ➕ `kpi_target_value: Optional[int]` |
| 4 | **Validation rule** | ➕ Required if `kpi_target_type == frequency` · 1 ≤ value ≤ 5 |
| 5 | **Validation rule** | ➕ `frequency_cap > kpi_target_value` (warna virodh) |
| 6 | **Step 6 repair loop** | 🔄 Ab "frequency within targets" **implementable** hai |
| 7 | **➕ Naya sub-section** | Frequency **target** vs frequency **cap** ka farak saaf likho |
| 8 | **§7.1 repair loop** | "insufficient frequency" define karo — target se kitna neeche = insufficient? |

## 🏷️ Nichod
> **David keh raha hai:** *"KPI me sirf 'kaunsa metric' hai. Agar frequency chuni hai to 'kitna' bhi chahiye — 1 se 5 ke beech ek number."*

**Severity: 🔴 HIGH** — **missing field**, aur uske bina **repair loop ka frequency check implementable nahi**.

---
---

# 🗨️ COMMENT #11 — "Market budgets: single market budget?"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Market budgets** |
| **Highlighted** | **"Table"** (Type column) |

## 💬 David ne exactly kya likha
> *"**single market budget?**"*

## 🔍 Matlab
```
"Ye 'Table' kyun hai? Agar ek hi market hai, to budget bhi EK number
 hoga — table kyun?"

Table = kai rows = kai markets
Ek market = ek row = table ki zaroorat nahi
```

## 🔗 Seedha COMMENT #8 se juda
```
#8:  "Are we going to support multi market?"
#11: "single market budget?"
→ Ek hi sawaal ke DO hisse. #11 ka jawab #8 ke jawab par depend karta hai.

Agar M1 = SINGLE market:
  budget = "10000.00"              ← ek number, table nahi
  market = markets[0] se aayega

Agar M1 = MULTI market:
  market_budgets = [                ← table sahi hai
    {market: "GB", budget: "6000.00"},
    {market: "FR", budget: "4000.00"}
  ]
```

## 🔴 Gehra insight — Data model ≠ Presentation
```
╔══════════════════════════════════════════════════════════════════════════╗
║  DATA MODEL (schema)         ≠        PRESENTATION (trader kya dekhta)   ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Schema me:                            Trader ko dikhta hai:             ║
║    market_budgets: list[...]             "Budget: £10,000"                ║
║    = [{market:"GB", budget:"10000"}]     ← EK simple number               ║
║    ← LIST (length 1)                                                     ║
║                                                                          ║
║  → Dono theek hain! Koi virodh nahi.                                     ║
║  → Schema list rakho (M2 me multi-market aayega to migration nahi)       ║
║  → Par trader ko table na dikhao — ek number dikhao                      ║
╚══════════════════════════════════════════════════════════════════════════╝

🔗 Ye Comment #7 ke "Required ≠ Asked" insight ka doosra roop hai.
🔗 Aur #8 ke recommendation se perfectly match karta hai.
```

## 🔴🔴 BADI STRUCTURAL PROBLEM — "Type" column CHAAR kaam kar raha hai

David ne **"Table"** highlight kiya. Aur "Table" ek **UI widget** hai, **data type** nahi!

```
┌─────────────────────────────────────────────────────────────────────────┐
│  DATA TYPES (sahi jagah)                                                │
│    String · Number · Date range · Boolean · Timestamp · Enum · URL      │
├─────────────────────────────────────────────────────────────────────────┤
│  UI WIDGETS (ye Type column me kyun hain?!)                             │
│    Dropdown · Radio · Multi-select · TABLE · Toggle · Textarea ·         │
│    Card Select · Checkbox table · Select · Chart · Display · Upload     │
├─────────────────────────────────────────────────────────────────────────┤
│  SOURCE / BEHAVIOUR (ye bhi Type column me!)                            │
│    Fixed · Derived · Derived from file · Reference · Question · Check   │
├─────────────────────────────────────────────────────────────────────────┤
│  DOMAIN CONCEPTS (ye bhi!)                                              │
│    "3 profiles" · "Allocation (%)"                                      │
└─────────────────────────────────────────────────────────────────────────┘

🔴 Ek hi column CHAAR alag cheezein bata raha hai!
   Isliye confusion hoti hai. Isliye David ko "Table" par sawaal uthana pada.
```

### ✅ Fix — Type column ko todo
```
ABHI:     Field | Type | Requirement | Change from v1.1.0
                   ↑
              4 kaam kar raha hai

NAYA:     Field | Data type | Requirement | Source | Change from v1.1.0
                     ↑                        ↑
              sirf DATA shape         #6/#7/#9/#13 se aaya

UI widget? → Is document me HONA HI NAHI CHAHIYE.
             Wo Riddhi/Basil ke UI spec me jaayega.
             🔴 Ye document DATA CONTRACT hai, UI SPEC nahi.

Example — Market budgets ka naya row:
┌────────────────┬──────────────────────┬─────────────┬─────────────────────┐
│ Field          │ Data type            │ Requirement │ Source              │
├────────────────┼──────────────────────┼─────────────┼─────────────────────┤
│ Market budgets │ list[{market,budget}]│ Required    │ 🧠 INFERRED from    │
│                │ (M1: length 1)       │             │    brief            │
└────────────────┴──────────────────────┴─────────────┴─────────────────────┘
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | Step 1 — Market budgets Type | "Table" → `list[{market, budget}]` · M1 me length 1 |
| 2 | ➕ Note | Schema list rahegi (M2-ready), par M1 me trader ko **ek number** dikhega |
| 3 | 🔴 **SAB field matrices** | `Type` column ko **`Data type` + `Source`** me todo · UI widget hatao |
| 4 | ➕ Naya note document ke shuru me | Ye document **data contract** hai, **UI spec nahi** |
| 5 | #8 ke saath | Final jawab multi-market scope decision par depend karta hai |

## 🏷️ Nichod
> **David poochh raha hai:** *"Ek market hai to budget ek number hoga — 'Table' kyun likha hai?"*

**Severity: 🟡 MEDIUM** — par isse ek **bada structural problem** nikla (Type column 4 kaam kar raha hai).

---
---

# 🗨️ COMMENT #12 — "Base bids not required for CTV" 🔴🔴 SABSE KHATARNAK

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Base bids** |
| **Highlighted** | **"Required"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"**not required for CTV** as **defined by CPM of deals**"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"**not required for CTV**"* | 🔴 CTV ke liye base bid **chahiye hi nahi** |
| *"as **defined by CPM of deals**"* | Kyunki **daam deal me pehle se tay** hai |

## 🔴 Ye #6 se AAGE ki baat hai
```
Comment #6 me maine socha tha:
  "Base bid RATE CARD se DERIVE ho sakta hai"

David keh raha hai kuch AUR SIMPLE:
  "Base bid ki ZAROORAT HI NAHI hai"

→ Derive karne ki bhi zaroorat nahi. Field hi bekaar hai.
```

## ✅ Kyun? — Document ke apne §2.3 table se jawab

**Base bid** = *"main maximum itna CPM dene ko taiyar hun"* — ye **auction** me kaam aata hai.

**Par CTV deals me auction hota hai?** §2.3 dekho:
```
┌────────────────────────────────┬──────────────────────────┬──────────────────┐
│ Deal Type                      │ Price                    │ Base bid chahiye?│
├────────────────────────────────┼──────────────────────────┼──────────────────┤
│ Programmatic Guaranteed (PG)   │ FIXED CPM                │ ❌ NAHI          │
│                                │ + guaranteed volume      │    Daam tay hai  │
├────────────────────────────────┼──────────────────────────┼──────────────────┤
│ Preferred Deals                │ FIXED CPM                │ ❌ NAHI          │
│                                │                          │    Daam tay hai  │
├────────────────────────────────┼──────────────────────────┼──────────────────┤
│ Private Auctions               │ FLOOR CPM, COMPETITIVE   │ 🟡 SHAYAD HAAN   │
│                                │                          │    Boli lagti hai│
└────────────────────────────────┴──────────────────────────┴──────────────────┘

Aur document ke SAARE examples "Preferred" hain:
  "Prime Video | Preferred Deal | UK - 30 | £28.88"
  "Netflix | Preferred | UK - 30 | £32.00"
                ↑
          FIXED CPM. Koi bidding nahi.
```

```
╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 DOCUMENT KA APNA §2.3 TABLE JAWAB DE RAHA HAI:                       ║
║                                                                          ║
║  PG aur Preferred me "Fixed CPM" likha hai.                              ║
║  Fixed CPM = daam tay hai, boli nahi lagti.                               ║
║  Boli nahi lagti to BASE BID kis kaam ka?                                 ║
║                                                                          ║
║  → Base bid ek OPEN AUCTION / DISPLAY ka concept hai                      ║
║  → CTV pre-curated deals me bekaar                                        ║
║  → Yaani NON-CTV FIELD (bilkul #6 ke "formats (all four)" jaisa)         ║
║                                                                          ║
║  🔴 THEME #4 KA EK AUR CASE:                                             ║
║     §2.3 (business logic) sach bolta hai · Step 1 matrix galat hai        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴🔴 SABSE BADA NATEEJA — Repair Loop ka LEVER TOOT GAYA

```
Document ka repair loop (§7.1) — 3 actions:
  Action 1: Audience bundle switch/extend (Narrow → Balanced/Broad)
  Action 2: "Adjust base CPM bid up to market recommended floor
             (e.g. increase from £15 to £30 for Prime Video)"
  Action 3: Re-run forecasting engine

╔══════════════════════════════════════════════════════════════════════════╗
║  ACTION 2 (bid badhao) — 🔴 CTV KE LIYE INVALID HAI!                     ║
║                                                                          ║
║  Preferred/PG deal me CPM FIXED hai. Bid badhane se kuch nahi hoga —      ║
║  daam wahi rahega.                                                       ║
║                                                                          ║
║  → Repair loop ke 2 real levers me se 1 GAYA                              ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 🔴 Comment #5 ke saath jodo — repair loop ke paas KUCH BHI NAHI BACHTA
```
╔══════════════════════════════════════════════════════════════════════════╗
║  WORST CASE SCENARIO                                                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Situation:                                                              ║
║    • Koi audience select nahi ki (#4: audiences optional hain)            ║
║    • Deal = Preferred (Fixed CPM)                                        ║
║    • Forecast: reach bahut kam nikla                                     ║
║                                                                          ║
║  Repair loop kya kar sakta hai?                                          ║
║    Action 1: Audience widen karo   → ❌ KOI AUDIENCE HI NAHI HAI!         ║
║    Action 2: Bid badhao            → ❌ CPM FIXED HAI!                    ║
║    Action 3: Re-forecast           → ❌ Kuch badla nahi, wahi nateeja     ║
║                                                                          ║
║  🔴 REPAIR LOOP KE PAAS ZERO LEVERS HAIN!                                ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### ✅ Naya repair loop — ordered levers (document me likhna padega)
```
Purane 2 (jinme se 1 CTV me invalid ho gaya):
  ❌ Base bid badhao            → CTV me invalid (fixed CPM)
  🟡 Audience widen/extend      → sirf tab jab audience hai

Naye levers jo document me LIKHNE chahiye — is kram me:
  1. Doosri TARGETING relax karo (device → sab, location → poora market,
     content exclusions hatao)                    ← #5 se aaya, PRIMARY lever
  2. Audience extend karo                          ← agar audience hai
  3. Matching mode Exact → Similar                 ← agar audience hai
  4. AUR DEALS add karo (zyada inventory = zyada reach)
  5. Flight dates extend karo (zyada din = zyada log)
  6. Budget badhao (trader se poochh kar)
  7. Aakhri sahara: IMAANDARI se bolo
     "Is deal ke inventory se isse zyada reach possible nahi hai"
                                                   ← Zero-Hallucination

🔴 Ye ek POORA naya section hai. Aur ye Wajahat ke graph design ke liye
   critical hai — usko pata hona chahiye repair loop ke kitne edges hain.
```

## ⚠ Ek nuance — Private Auction ka case
```
David ne kaha "not required for CTV" — par §2.3 me Private Auction bhi hai,
jisme "Floor CPM, competitive" likha hai.

Poora sach:
  deal_type = Preferred        → base bid NAHI chahiye  ❌
  deal_type = PG               → base bid NAHI chahiye  ❌
  deal_type = Private Auction  → base bid SHAYAD chahiye 🟡

→ Field DELETE nahi karna — CONDITIONAL karna hai
→ ⚠ David se confirm: CTV me Private Auction deals hote hain?
  (document ke saare examples Preferred hain)
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | Step 1 — Base bids Requirement | **Required** → **Not applicable for CTV** (ya Conditional: Private Auction only) |
| 2 | `MarketBudgetBidSchema` | `base_bid: str = Field(...)` → `Optional[str] = None` |
| 3 | 🔴🔴 **Step 6 — Repair loop Action 2** | **HATAO** — "adjust base CPM bid" CTV me invalid |
| 4 | 🔴🔴 **Step 6 — Repair loop** | **POORA RE-WRITE** — naye ordered levers ke saath |
| 5 | **§7.1 — Repair loop** | Wahi rewrite (do jagah likha hai) |
| 6 | ➕ Note | Kyun base bid CTV me bekaar hai (fixed CPM deals) |
| 7 | ⚠ Confirm | CTV me Private Auction deals hote hain? |
| 8 | §2.3 vs Step 1 | Contradiction reconcile karo |

## 🏷️ Nichod
> **David keh raha hai:** *"CTV me base bid ki zaroorat nahi — daam deal me pehle se tay hai (Fixed CPM), boli nahi lagti."*

**Severity: 🔴🔴 VERY HIGH** — field hatana chhoti baat hai, **par isse repair loop ka lever toot jaata hai, aur worst case me repair loop ke paas kuch bacha hi nahi.** Poora re-write chahiye.

---
---

# 🗨️ COMMENT #13 — "Frequency cap: we have a default per advertiser"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Frequency cap** |
| **Highlighted** | **"Optional"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"we have a **default per advertiser**"*

## 🔍 Matlab
```
"Frequency cap Optional likha hai — par asal me har ADVERTISER ka ek
 DEFAULT frequency cap pehle se hota hai."

→ Field kabhi KHAALI nahi rehti
→ Advertiser ki settings se ek value AA JAATI hai
→ Trader chahe to badal sakta hai
```

## 🔴 "Optional" technically sahi, par MISLEADING
```
#3, #4 me:  Table kehta tha "Required", asal me "Optional"
            → SEEDHA GALAT

#13 me:     Table kehta hai "Optional" — aur ye SAHI hai
            (trader ko bharna zaroori nahi)
            PAR field kabhi khaali nahi rehti (default se bhar jaati hai)
            → TECHNICALLY SAHI, PRACTICALLY MISLEADING

╔══════════════════════════════════════════════════════════════════════╗
║  Phir wahi hal: "Requirement" column KAAFI NAHI HAI.                 ║
║                                                                      ║
║  Requirement: Optional          ✅ (trader ko dena zaroori nahi)     ║
║  Source:      🏢 ADVERTISER     ← advertiser ke default se            ║
║                                                                      ║
║  → SOURCE COLUMN phir zaroori nikla!                                 ║
║  → Ab CHAAR comments (#7,#9,#11,#13) isi ek fix se solve hote hain   ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 🔴🔴 SABSE BADA FINDING — "Advertiser Defaults" ek POORA MISSING CONCEPT
```
David: "we have a default per advertiser"
        ↑
    Yaani VOW me "advertiser defaults / settings" naam ki cheez HAI

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 PAR DOCUMENT ME YE CONCEPT KAHIN NAHI HAI!                           ║
║                                                                          ║
║  Document me advertiser ka zikr sirf yahan:                              ║
║    advertiser_id: str = Field(..., description="Parent advertiser UUID") ║
║    ← Bas ek ID. Settings/defaults ka koi zikr nahi.                      ║
║                                                                          ║
║  ❌ Koi schema:  AdvertiserDefaultsSchema — NAHI HAI                     ║
║  ❌ Koi API:     GET /api/advertisers/{id}/defaults/ — NAHI HAI          ║
║  ❌ Koi state:   advertiser_defaults — NAHI HAI                          ║
║  ❌ Koi mention: "advertiser settings" poore document me NAHI HAI        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 🔴 Kya AUR advertiser defaults hain?
```
David ne sirf frequency cap ka bataya. Par logically ye bhi ho sakte hain:

  ✅ Frequency cap          ← David ne CONFIRM kiya
  🟡 Currency               ← Comment #9 me maine SUGGEST kiya tha!
  🟡 Budget cap
  🟡 Attribution window     ← (14 din — configurable hai ya nahi? gap tha)
  🟡 Default targeting      ← Comment #5 se juda
  🟡 Naming convention      ← Comment #7 se juda
  🟡 Content exclusions     ← brand safety rules advertiser-level hote hain
  🟡 Approval threshold     ← Step 7 me "possibly budget-threshold-based"!
```

### 🎯 Mera Comment #9 ka anumaan CONFIRM ho gaya
```
Comment #9 me maine likha tha:
  "Option B: Advertiser ke account ki default currency use karo
   ⚠ Par ye field/API document me hai hi nahi"

Ab Comment #13 kehta hai: "we have a default per advertiser"
  → Advertiser defaults EXIST karte hain! ✅
  → To currency ka bhi default ho sakta hai
  → Mera #9 ka recommendation ab STRONG ho gaya

💡 REPLY ME YE LIKHNA — David ko dikhega ki tumne comments ko JODKAR
   samjha hai, alag-alag nahi.
```

## ✅ Agent ka naya behaviour
```
Agent: "Advertiser ki settings se ye defaults uthaye hain:

        ┌────────────────────────────────────────────────────┐
        │  Advertiser defaults (BrightPath)                  │
        │  ✓ Frequency cap:      3 per week                  │
        │  ✓ Currency:           GBP                         │
        │  ✓ Content exclusions: News, Politics              │
        └────────────────────────────────────────────────────┘

        Ye is campaign par lag gaye hain. Koi badalna hai?"

🔗 Ye bilkul Comment #5 ka "default-then-refine" pattern hai — sirf ab
   defaults ADVERTISER KE SETTINGS se aa rahe hain, na ki brief se.
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | Step 1 — Frequency cap | Requirement: **Optional** ✅ rakho · Source: **🏢 ADVERTISER default** |
| 2 | 🔴 ➕ Naya schema | `AdvertiserDefaultsSchema` — frequency cap + jo bhi aur defaults hain |
| 3 | 🔴 ➕ Naya API | `GET /api/advertisers/{id}/defaults/` — §4 catalogue me add karo |
| 4 | 🔴 ➕ `PlanningAgentState` | `advertiser_defaults: Optional[dict]` — flow ke shuru me load |
| 5 | ➕ Naya section | "Advertiser defaults" — kaunse hain, kab load hote hain, override kaise |
| 6 | State machine | ➕ Advertiser defaults load karne ka node/step |
| 7 | Comment #9 update | Currency ka default bhi advertiser se — ab confirm ho gaya |
| 8 | Step 7 (Plan approval) | "possibly budget-threshold-based" — ye bhi advertiser default ho sakta |
| 9 | ⚠ Confirm | Frequency cap ke alawa kaunse advertiser defaults hain? |

## 🏷️ Nichod
> **David keh raha hai:** *"Frequency cap khaali nahi rehti — har advertiser ka ek default hota hai jo automatically lag jaata hai."*

**Severity: 🔴 HIGH** — chhota comment, par ek **poora missing concept** (advertiser defaults) + **missing API** + **missing schema** nikla.

---
---

# 🔗 COMMENTS #10–#13 KA JOD — Teen Naye Findings

## Finding 1 — "Source" column ab CHAAR comments solve karta hai (aur ek naya type mila)
```
#7  Strategy name    → Required, Source = 🤖 GENERATED
#9  Primary currency → Required, Source = ⚙️ DERIVED from market
#11 Market budgets   → Required, Source = 🧠 INFERRED from brief
#13 Frequency cap    → Optional, Source = 🏢 ADVERTISER default
                                            ↑
                              🔴 NAYA SOURCE TYPE! Pehle 6 the, ab 7:

  💬 ASKED       trader se poochhna padega
  🧠 INFERRED    brief ke text se
  ⚙️ DERIVED     doosre field se (market → currency)
  🏢 ADVERTISER  advertiser ke defaults se        ← ➕ NEW (#13)
  🤖 GENERATED   agent ne banaya
  🔒 FIXED       CTV ke liye constant
  🔌 API         API response se
```

## Finding 2 — "Type" column ko todna padega
```
David ne #11 me "Table" par sawaal uthaya — kyunki "Table" ek UI widget hai.
Poore document ka Type column CHAAR kaam kar raha hai:

  Data types    → String, Number, Date range, Boolean, Enum, URL
  UI widgets    → Dropdown, Radio, Multi-select, Table, Toggle, Textarea,
                  Card Select, Checkbox table, Select, Chart, Display, Upload
  Source        → Fixed, Derived, Derived from file, Reference, Question, Check
  Domain terms  → "3 profiles", "Allocation (%)"

✅ FIX:
  Field | Data type | Requirement | Source | Change from v1.1.0

  UI widget → is document me NAHI. Riddhi/Basil ke UI spec me.
  🔴 Ye document DATA CONTRACT hai, UI SPEC nahi.
```

## Finding 3 — 🔴🔴 REPAIR LOOP KA POORA COLLAPSE

Teen comments (#4, #5, #12) milkar repair loop **tod dete hain**:
```
╔══════════════════════════════════════════════════════════════════════════╗
║  DOCUMENT KA REPAIR LOOP (3 actions)                                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Action 1: Audience extend/widen karo                                    ║
║            → ❌ TOOT GAYA (#4: audience optional hai — ho sakta hai       ║
║               koi audience hi na ho, phir widen kya karein?)              ║
║                                                                          ║
║  Action 2: Base CPM bid badhao (£15 → £30)                                ║
║            → ❌ TOOT GAYA (#12: CTV me CPM FIXED hai, bid bekaar)         ║
║                                                                          ║
║  Action 3: Re-run forecast                                               ║
║            → 🟡 Ye action nahi, ye sirf DOBARA CHECK karna hai            ║
║                                                                          ║
║  🔴 NATEEJA: DONO ASLI LEVERS TOOT GAYE. Repair loop KHAALI hai.         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

**Naya repair loop — ordered levers:**
```
1. Targeting relax karo (device, location, content exclusions)  ← PRIMARY (#5)
2. Audience extend karo                                         ← agar hai
3. Matching mode Exact → Similar                                ← agar hai
4. Aur deals add karo (zyada inventory)
5. Flight dates extend karo
6. Budget badhao (trader se poochh kar)
7. Aakhri: IMAANDARI se bolo — "is inventory se zyada reach possible nahi"
```

---

## ✍️ DOCUMENT NOTES — #10, #11, #12, #13

### Note — Comment #10 (KPI target)
> **📝 NOTE — KPI target value is missing (David Moss)**
>
> The matrix records `KPI` as the metric (`reach` or `frequency`) but has **no field for the target value**. Per David: **when KPI is `frequency`, a numeric target of 1–5 applies.**
>
> **Two pieces of internal evidence that this field was always needed:**
>
> 1. The schema field is named **`kpi_target_type`** — "type" implies a companion "value" that does not exist.
> 2. **The repair loop references a target that the schema cannot hold.** §6.2 says *"Check if reach > 0 and **frequency within targets**"*, and §7.1 triggers repair on *"`estimated_unique_reach == 0` **or insufficient frequency**"*. Neither is implementable — there is nothing to compare against.
>
> **Frequency target and frequency cap are different things** and the document currently has only the latter:
>
> | | **Frequency target (1–5)** | **Frequency cap** |
> |---|---|---|
> | What it is | An **optimisation goal** — the average to aim for | A **hard limit** — never exceed |
> | DSP behaviour | Paces delivery toward the average | Blocks the (n+1)th impression |
> | In one word | **Aim** | **Ceiling** |
>
> **Why only frequency has a numeric target:** frequency is **controllable** — the DSP can pace delivery to hit an average. Reach is an **outcome** — it falls out of budget, audience, inventory and CPM. You read reach; you set frequency.
>
> **Schema additions:**
> ```python
> # FullStrategySchema
> kpi_target_value: Optional[int] = Field(
>     None, ge=1, le=5,
>     description="Target average frequency. Required when kpi_target_type == frequency")
> ```
>
> **Validation rules to add:**
> - Required when `kpi_target_type == "frequency"`; must be 1–5
> - **`frequency_cap` must exceed `kpi_target_value`** — a target of 4 under a cap of 3 is mathematically unreachable. This matters because the cap has an advertiser-level default (see the note on Frequency cap), so the conflict can arise without the trader doing anything.
>
> **Consequence:** with this field in place, the repair loop's frequency check becomes implementable for the first time. §7.1 should also define what *"insufficient frequency"* means numerically — how far below target triggers repair.

### Note — Comment #11 (Market budgets / the Type column)
> **📝 NOTE — Market budgets shape, and a structural problem with the Type column (David Moss)**
>
> **On the immediate question:** if M1 is single-market (see the multi-market scope note on Target markets), the trader deals with **one budget figure**, not a table. The recommendation there — keep `markets: list[str]` in the schema, constrain the flow to one market — applies here too:
>
> | | Schema (unchanged, M2-ready) | What the trader sees in M1 |
> |---|---|---|
> | Budget | `list[{market, budget}]`, length 1 | *"Budget: £10,000"* — a single figure |
>
> **Data model shape and presentation shape are different things**, and this document should specify the former, not the latter.
>
> **Which exposes the structural problem David's highlight points at:** "Table" is a **UI widget**, not a data type. The `Type` column across this document is currently doing **four different jobs**:
>
> | Job | Values currently in the Type column |
> |---|---|
> | **Data type** ✅ belongs here | String · Number · Date range · Boolean · Timestamp · Enum · URL |
> | **UI widget** ❌ belongs in the UI spec | Dropdown · Radio · Multi-select · **Table** · Toggle · Textarea · Card Select · Checkbox table · Select · Chart · Display · Upload |
> | **Source** ❌ belongs in the new Source column | Fixed · Derived · Derived from file · Reference · Question · Check |
> | **Domain concept** ❌ | "3 profiles" · "Allocation (%)" |
>
> **Correction:** every field matrix becomes `Field | Data type | Requirement | Source | Change from v1.1.0`. UI widgets come out entirely — **this document is the data contract, not the UI specification**; widget choices belong to Riddhi's and Basil's spec.

### Note — Comment #12 (Base bids)
> **📝 NOTE — Base bids are not applicable to CTV, and the repair loop depends on them (David Moss)**
>
> `Base bids` is marked **Required**. Per David it is **not required for CTV, because the CPM is defined by the deal.**
>
> **The document's own §2.3 already says this:**
>
> | Deal type | Price | Is a base bid meaningful? |
> |---|---|---|
> | Programmatic Guaranteed | **Fixed CPM** | ❌ No — the price is set |
> | Preferred Deals | **Fixed CPM** | ❌ No — the price is set |
> | Private Auctions | Floor CPM, **competitive** | 🟡 Possibly — bidding occurs |
>
> A base bid is a maximum you are willing to pay in an **auction**. Pre-curated Preferred and PG deals have no auction, so the field has nothing to act on. Every deal example in this document is Preferred. **Base bid is an open-auction / Display concept carried over from v1.1.0** — the same class of leftover as `formats (all four)`.
>
> **Corrected:** `base_bid` → **not applicable for CTV**, or Conditional (Private Auction only). `MarketBudgetBidSchema.base_bid` becomes `Optional[str] = None`.
>
> **🔴 The significant consequence — the repair loop loses a lever.** §7.1 Action 2 reads *"Adjust base CPM bid up to market recommended floor (e.g. increase from £15 to £30 for Prime Video)."* **On a fixed-CPM deal this does nothing.** Combined with audiences becoming optional, the loop can be left with no levers at all:
>
> ```
> No audience selected + Preferred (fixed CPM) deal + low reach
>   Action 1: widen the audience  → nothing to widen
>   Action 2: raise the bid       → CPM is fixed
>   Action 3: re-forecast         → same result
>   → the repair loop has nothing to do
> ```
>
> **The repair loop therefore needs rewriting with a real, ordered lever list:**
>
> 1. **Relax other targeting** — device, location, content exclusions *(the primary lever once audiences are optional)*
> 2. **Extend the audience** — if one is applied
> 3. **Switch matching mode** Exact → Similar — if an audience is applied
> 4. **Add inventory** — more deals
> 5. **Extend flight dates**
> 6. **Increase budget** — requires the trader
> 7. **State the limit honestly** — *"this deal's inventory cannot deliver more reach than X"* (Zero-Hallucination)
>
> This rewrite is needed in both §7.1 and Step 6, and it materially affects the graph Wajahat builds — the number and shape of repair edges changes.
>
> **⚠ To confirm:** are Private Auction deals in scope for CTV M1? Every example here is Preferred. If Private Auction is in scope, `base_bid` stays as a conditional field rather than being dropped.

### Note — Comment #13 (Frequency cap / advertiser defaults)
> **📝 NOTE — Advertiser-level defaults are a missing concept (David Moss)**
>
> `Frequency cap` is marked **Optional**, implying it is empty unless the trader fills it. Per David, **there is a default per advertiser** — the field arrives pre-filled and the trader overrides it.
>
> "Optional" is technically correct (the trader need not supply it) but practically misleading (it is never empty). This is the **Source** distinction again: Requirement = **Optional**, Source = **DERIVED from advertiser default**.
>
> **🔴 The larger finding: advertiser-level defaults do not exist anywhere in this document.** `advertiser_id` appears as a UUID and nothing more. There is:
>
> - ❌ no `AdvertiserDefaultsSchema`
> - ❌ no endpoint in §4 to fetch advertiser settings
> - ❌ no `advertiser_defaults` in `PlanningAgentState`
> - ❌ no mention of "advertiser settings" anywhere in the document
>
> **Additions required:**
> ```python
> class AdvertiserDefaultsSchema(BaseModel):
>     """➕ NEW — defaults held per advertiser, loaded at session start"""
>     frequency_cap: Optional[int] = None          # confirmed by David
>     primary_currency: Optional[CurrencyEnum] = None
>     budget_cap: Optional[str] = None
>     content_category_exclusions: list[str] = Field(default_factory=list)
>     approval_threshold: Optional[str] = None
> ```
> Plus an endpoint in §4 (`GET /api/advertisers/{id}/defaults/` or the real equivalent), and `advertiser_defaults: Optional[dict]` in the planning state, loaded before field extraction.
>
> **This also resolves an open question raised elsewhere.** The note on Primary currency proposed "use the advertiser account's default currency" and flagged that no such field or API existed in the document. David's comment confirms advertiser-level defaults are real, so that recommendation now stands on something concrete rather than an assumption.
>
> **It may also resolve Step 7's open question** — *"Manager required: Configurable (possibly budget-threshold-based)"*. That threshold is plausibly an advertiser default too.
>
> **⚠ To confirm:** beyond frequency cap, which values have advertiser-level defaults? Currency? Budget cap? Content exclusions? Approval threshold?

---

## 💬 REPLY DRAFTS — #10, #11, #12, #13

### Reply — Comment #10
> Good catch — there's a field missing, not just a wording issue.
>
> I have `kpi_target_type` (`reach` / `frequency`) but no target **value**. The field name itself gives it away — "type" with no companion "value". Adding `kpi_target_value: Optional[int]`, 1–5, required when the KPI is frequency.
>
> The more serious part: **the repair loop already references a target that the schema can't hold.** §6.2 says *"check if reach > 0 and frequency within targets"* and §7.1 triggers repair on *"insufficient frequency"* — neither is implementable today, because there's nothing to compare against. So this field unblocks the loop's frequency check.
>
> I'll also spell out the distinction I'd left implicit: **frequency target is an aim, frequency cap is a ceiling.** The DSP paces toward a target; it blocks against a cap. And they need validating against each other — a target of 4 under a cap of 3 is unreachable. That matters given the cap has an advertiser default, so the conflict can appear without the trader doing anything.
>
> One thing I'll note as the reason there's no reach target: frequency is controllable, reach is an outcome. You set frequency; you read reach.

### Reply — Comment #11
> On the direct question — yes, if M1 is single-market the trader should see **one budget figure**, not a table. My recommendation on the multi-market question is to keep `markets: list[str]` in the schema so nothing migrates later, but constrain the M1 flow to one market. Same applies here: schema stays a list of length one, presentation is a single number.
>
> Your highlight points at something worse in the document, though. **"Table" is a UI widget, not a data type** — and the `Type` column is currently doing four jobs at once: real data types (String, Number, Date range), UI widgets (Dropdown, Radio, Table, Toggle, Checkbox table…), sources (Fixed, Derived, Question, Check) and domain terms ("3 profiles", "Allocation (%)").
>
> Fixing it: every matrix becomes `Field | Data type | Requirement | Source`. **Widgets come out entirely** — this document is the data contract, not the UI spec; those belong in Riddhi's and Basil's spec.

### Reply — Comment #12
> Agreed, and this one has a consequence I hadn't seen.
>
> You're right that base bid is meaningless on a fixed-CPM deal — and **my own §2.3 says so**: PG and Preferred are both "Fixed CPM", and every deal example in the document is Preferred. Base bid is an open-auction concept carried over from v1.1.0, same class of leftover as `formats (all four)`. I'll make it not-applicable for CTV, or conditional on Private Auction.
>
> **The consequence: the repair loop loses a lever.** §7.1 Action 2 is *"increase from £15 to £30 for Prime Video"* — which does nothing on a fixed CPM. And with audiences now optional, the worst case is that the loop has **nothing** left: no audience to widen, no bid to raise, so re-forecasting returns the same answer.
>
> So I'm rewriting the repair loop with a real ordered lever list — relax other targeting first (which becomes the primary lever now that audiences are optional), then extend audience / switch Exact→Similar if one is applied, then add inventory, extend flight dates, increase budget, and finally **state the limit honestly** if none of it helps. That last one matters: *"this deal's inventory can't deliver more reach than X"* is a legitimate answer.
>
> Flagging that this changes the graph Wajahat builds — the number and shape of repair edges is different.
>
> **One thing to confirm:** are Private Auction deals in scope for CTV M1? Every example here is Preferred. If they are, base bid stays as a conditional field rather than being dropped.

### Reply — Comment #13
> Useful — and this opens a bigger gap than the field itself.
>
> "Optional" is technically right (the trader needn't supply it) but misleading, because with an advertiser default the field is never actually empty. That's the Source distinction again: **Requirement = Optional, Source = derived from advertiser default.**
>
> The bigger thing: **advertiser-level defaults don't exist anywhere in this document.** `advertiser_id` is a UUID and nothing else — no defaults schema, no endpoint to fetch them, no state field, no mention. I'm adding all of that.
>
> This also settles something I'd left as an assumption. On the currency comment I proposed using "the advertiser account's default currency" and noted no such field or API appeared in the document. Your comment confirms advertiser defaults are real, so that recommendation now rests on something concrete. It may also answer Step 7's open question about the manager-approval threshold being *"possibly budget-threshold-based"* — that's plausibly an advertiser default too.
>
> **What I need from you:** beyond frequency cap, which values have advertiser-level defaults? Currency, budget cap, content exclusions, approval threshold?

---
---

# 🧩 COMMENTS #14 · #15 · #16 · #17 — STEP 1 MATRIX CLUSTER (part 3)

> **Chaaron `Step 1` field matrix par hain** — #10–#13 ka agla hissa.
>
> **Do KHAAS baatein is round me:**
> 1. 🎉 **#17 pehla comment hai jahan David v2.0 ke change se SEHMAT hai** — ab tak sab corrections the
> 2. 🎉 **#16 + #17 milkar Open Question #1 SOLVE kar dete hain** — aur is tracker ka pichhla recommendation **ulta** nikla

---
---

# 🗨️ COMMENT #14 — "Formats: is always streaming_tv"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Formats** |
| **Highlighted** | **"Required"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"is **always streaming_tv**"*

## ❌ Document abhi kya kehta hai
```
Formats | Fixed | Required | 🔄 CHANGED. For M1, streaming_tv and
                              prime_video only. Display and online_video
                              removed from scope
                              ↑
                    DO values: streaming_tv AUR prime_video

David: sirf EK value — streaming_tv
```

## 🔴 Kyun? — Ye ek LEVEL / TAXONOMY ki galti hai
```
╔══════════════════════════════════════════════════════════════════════════╗
║  FORMAT vs PROVIDER — do ALAG level hain                                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║  FORMAT = ad ka KISM / channel                                           ║
║    display · online_video · streaming_tv · audio                         ║
║    ← CTV ka format = "streaming_tv". Bas ek.                             ║
║                                                                          ║
║  PROVIDER = kaun DIKHA raha hai (publisher / supply source)               ║
║    Prime Video · Netflix · Hulu · Disney+                                ║
║    ← Ye streaming_tv ke ANDAR aate hain                                  ║
║                                                                          ║
║  🔴 Document ne dono ko EK LIST me daal diya:                            ║
║     formats = ["streaming_tv", "prime_video"]                             ║
║                      ↑              ↑                                    ║
║                   format        PROVIDER (format nahi!)                  ║
║                                                                          ║
║  ✅ Sahi:                                                                ║
║     format   = "streaming_tv"                    ← Step 1, hamesha       ║
║     provider = "Prime Video" / "Netflix" / …     ← Step 2 me tay hota hai║
╚══════════════════════════════════════════════════════════════════════════╝

Analogy:
  Format = "TV"                   ← medium
  Provider = "Star Plus", "Sony"  ← channel

  Tum ye nahi likhoge: media = ["TV", "Star Plus"]
  Tum likhoge:         media = "TV", channel = "Star Plus"
```

## 🔴 PROOF 1 — Document me `provider` field PEHLE SE hai!
```python
# SelectedDealSchema me (Step 2):
provider: str = Field(..., description="e.g. Prime Video, Netflix, Disney+")  # ➕ NEW
                                            ↑
        🔴 PRIME VIDEO YAHAN PEHLE SE HAI — provider ki tarah!

→ Step 1 me use FORMAT ki tarah dobara likhna = DUPLICATION, galat level par
```

## 🔴 PROOF 2 — Document ka apna Step 2 API call David se SEHMAT hai!
```
Step 2 (CTV Inventory) me likha hai:
  "Fetched via GET /api/deals/?markets={market}&formats=streaming_tv"
                                                        ↑↑↑↑↑↑↑↑↑↑↑↑
                            🔴 SIRF streaming_tv! prime_video NAHI!

╔══════════════════════════════════════════════════════════════════════╗
║  Step 1 kehta hai:  formats = ["streaming_tv", "prime_video"]         ║
║  Step 2 ka API:     formats=streaming_tv                             ║
║                                                                      ║
║  → DOCUMENT APNE AAP SE CONTRADICT KAR RAHA HAI                      ║
║  → Aur Step 2 SAHI hai (David se match karta hai)                    ║
╚══════════════════════════════════════════════════════════════════════╝
```

## ⚠ Imaandari ki baat — v1.1.0 kuch aur kehta hai
```
v1.1.0 ke create payload example me:
  "formats": ["prime_video"]        ← prime_video ko FORMAT ki tarah bheja

Aur v1.1.0 ke deals table ka heading:
  "Deals (Step 3 of 5) - Prime Video Deals"

→ v1.1.0 ne prime_video ko format maana tha
→ David keh raha hai wo GALAT tha
→ v2.0 ka Step 2 (streaming_tv only) David se sehmat hai

⚠ CONFIRM karna zaroori: Amazon DSP ka API asal me kaunsi values
  accept karta hai — streaming_tv only, ya prime_video bhi?
```

## 🔗 Comment #6 se judav
```
#6 ne kaha: "formats non-CTV hai, FIXED hona chahiye"
    → Maine socha tha: fixed = ["streaming_tv", "prime_video"] (do values)

#14 aur specific hai: "always streaming_tv" (EK value)
    → Yaani field ek CONSTANT hai
    → Aur constant ko field matrix me rakhna hi galat hai
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Step 1 — Formats row** | Requirement: Required → **System constant** = `["streaming_tv"]` · ya row **poori hatao** |
| 2 | **Step 1 — Change note** | "streaming_tv and prime_video only" → **"always streaming_tv"** |
| 3 | **`FormatEnum`** | `PRIME_VIDEO` → `# not a format — provider (see SelectedDealSchema.provider)` |
| 4 | ➕ Naya note | **Format vs Provider** ka farak saaf likho — level confusion clear karo |
| 5 | §8 Summary | 🔄 "formats scoped to 2" → "formats is a constant: streaming_tv" |
| 6 | v1.1.0 create payload example | `"formats": ["prime_video"]` → `["streaming_tv"]` |
| 7 | ⚠ Confirm | Amazon DSP API kaunsi format values accept karta hai? |

## 🏷️ Nichod
> **David keh raha hai:** *"Format hamesha `streaming_tv` hai. Prime Video ek format nahi — wo ek provider hai, jo Step 2 me tay hota hai."*

**Severity: 🟡 MEDIUM** — par ye ek **taxonomy/level ki galti** hai jo confusion phailati hai, aur document apne aap se contradict kar raha hai.

---
---

# 🗨️ COMMENT #15 — "Product categories: default on advertiser, or imply from brief"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Product categories** |
| **Highlighted** | **"Required for video"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"we have a **default on the advertiser**, or maybe could **imply from the brief**"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"we have a **default on the advertiser**"* | 🏢 Advertiser ke record me pehle se ek default hai |
| *"or maybe could **imply from the brief**"* | 🧠 Ya brief se khud nikaal lo |

**Do sources diye — dono trader se poochhne se behtar.**

## 🔴 SABSE BADI BAAT — Advertiser defaults ka DOOSRA confirmation
```
Comment #13: "we have a default per advertiser"     ← frequency cap
Comment #15: "we have a default on the advertiser"  ← product categories

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 AB DO FIELDS CONFIRM HO GAYE HAIN:                                   ║
║     • frequency_cap       (#13)                                          ║
║     • product_categories  (#15)                                          ║
║                                                                          ║
║  → "Advertiser defaults" ek ASLI, BADA concept hai                        ║
║  → Aur document me wo POORA GAYAB hai                                    ║
║  → #13 ka AdvertiserDefaultsSchema recommendation ab BAHUT STRONG hai    ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 Kyun product category advertiser-level hai?
```
Sochо — kya BrightPath ki product category HAR CAMPAIGN me badalti hai?

  BrightPath  → hamesha "Education"
  Nike        → hamesha "Apparel / Footwear"
  Coca-Cola   → hamesha "Food & Beverage"

  🔴 NAHI BADALTI! Ye ADVERTISER ka guṇ hai, CAMPAIGN ka nahi.

╔══════════════════════════════════════════════════════════════════════════╗
║  Product category = ADVERTISER ka attribute                              ║
║  Isko HAR CAMPAIGN me dobara poochhna CONCEPTUALLY GALAT hai              ║
║                                                                          ║
║  Bilkul jaise: tum bank me har transaction par apna naam nahi likhte —   ║
║  wo account me pehle se hai.                                             ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## ✅ Poora fallback chain — TEEN sources (do David ne diye, ek document me chhupa tha)
```
1️⃣ ADVERTISER DEFAULT (best)          ← David ne bataya
   Advertiser record se: BrightPath → Education
   ✅ Sabse reliable — advertiser ka guṇ hai
        ↓ (agar advertiser default na ho)

2️⃣ BRIEF SE IMPLY                     ← David ne bataya
   "education website" → Education
        ↓ (agar brief me clear na ho)

3️⃣ ASIN VALIDATION RESPONSE           ← 🔴 DOCUMENT ME PEHLE SE HAI!
   POST /api/contextual-targeting/GB/asin-validation/
   ← {"valid_asins": [{
        "asin": "B08N5WRWNW",
        "title": "...",
        "brand": "AudioBrand",
        "product_category": "Electronics"     ← 🔴 YAHAN!
      }]}
   ✅ Muft me mil jaata hai jab ASIN validate karte hain
        ↓ (agar kuch bhi na mile)

4️⃣ TAB trader se poochho (aakhri sahara)

🔴 Source 3 document me §4.2 me PEHLE SE hai — par kabhi USE nahi kiya gaya.
```

## 🔗 "Required for video" ka matlab
```
Document: "Required for video"

Par CTV HAMESHA video hai! (#14: format always streaming_tv)
→ "Required for video" = "hamesha Required"

Yaani "for video" wali condition BEKAAR hai is document me —
wo v1.1.0 se aayi hai jahan Display bhi tha.

✅ Sahi: Requirement = Required
         Source      = 🏢 ADVERTISER → 🧠 INFERRED → 🔌 API
```

## ✅ Agent ka naya behaviour
```
(Advertiser defaults load hue — flow ke shuru me)

Agent: "BrightPath ke record se product category 'Education' uthayi hai.
        Brief se bhi ('education website') yahi confirm hota hai.

        Ye contextual targeting ke liye use hogi — ad education/
        documentary content ke saath dikhega, horror ke saath nahi.

        Theek hai, ya badalna hai?"

→ Trader se kuch poochha nahi gaya, sirf CONFIRM karna hai
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | Step 1 — Product categories | Requirement: "Required for video" → **Required** (CTV hamesha video) |
| 2 | Step 1 — Product categories | Source: **🏢 ADVERTISER → 🧠 INFERRED → 🔌 API** (fallback chain) |
| 3 | `AdvertiserDefaultsSchema` | ➕ `product_categories: list[int]` add karo |
| 4 | ➕ Naya note | Product category **advertiser ka attribute** hai, campaign ka nahi |
| 5 | ➕ Fallback chain document karo | Advertiser → brief → ASIN response → poochho |
| 6 | §4.2 ASIN validation | ➕ Note: response ka `product_category` is field ko auto-fill kar sakta hai |
| 7 | ⚠ Confirm | Advertiser record me product category kaise store hai — ek ya kai? |

## 🏷️ Nichod
> **David keh raha hai:** *"Product category advertiser ke record me pehle se hoti hai — ya brief se nikal aati hai. Poochhne ki zaroorat nahi."*

**Severity: 🔴 HIGH** — **advertiser defaults ka doosra confirmation**, jo ek poora missing concept saabit karta hai.

---
---

# 🗨️ COMMENT #16 — "Selling location: can leave out"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Selling location** |
| **Highlighted** | **"Required"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"**can leave out**"*

## 🔍 Matlab
```
"Can leave out" = "isko Step 1 se HATA DO"

Selling location (ON_AMAZON / NOT_SOLD_ON_AMAZON) ka sawaal
Step 1 me hona hi nahi chahiye.
```

## 🔴 Kyun? — Do wajah

### Wajah 1 — Ye TRACKING ka sawaal hai, PLANNING ka nahi
```
Step 1 ka maksad: "PLAN kya hai?" (naam, budget, dates, market, duration)
Selling location:  "MEASUREMENT kaise hoga?" (ASIN ya ad tag)

→ Do alag kaam
→ v2.0 ne already ASIN aur ad-tag conversions Step 11 me bheje hain
→ To selling location bhi unke SAATH jaana chahiye
```

### Wajah 2 — 🔴 Ye bhi ADVERTISER ka attribute hai
```
Sochо — kya "Amazon par bechta hai ya nahi" HAR CAMPAIGN me badalta hai?

  BrightPath → courses apni website par (aur ek book Amazon par)
  Nike       → Amazon par bhi bechta hai
  UK Govt    → kuch bechta hi nahi

  → Mostly ADVERTISER ka guṇ hai, campaign ka nahi!

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 AB TEEN FIELDS EK PATTERN BANA RAHE HAIN:                             ║
║                                                                          ║
║  #13  frequency_cap        → advertiser default   ✅ David ne confirm     ║
║  #15  product_categories   → advertiser default   ✅ David ne confirm     ║
║  #16  selling location     → advertiser attribute 🟡 anumaan              ║
║  #9   primary_currency     → advertiser account   🟡 anumaan              ║
║                                                                          ║
║  → Document ne ADVERTISER-LEVEL attributes ko STRATEGY schema me         ║
║    mila diya hai. Ye ek STRUCTURAL galti hai. (→ THEME 9)                ║
╚══════════════════════════════════════════════════════════════════════════╝

⚠ Nuance: ek advertiser ek campaign Amazon par aur doosra apni website par
  chala sakta hai. To ye ADVERTISER DEFAULT hai, par per-campaign OVERRIDE
  ho sakta hai — bilkul frequency cap jaisa.
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Step 1 — Selling location row** | 🔴 **HATAO** — Step 11 me le jao (ya advertiser se derive karo) |
| 2 | Step 11 (Tracking setup) | ✅ Wahan "Sells on Amazon?" pehle se hai — Step 1 se duplicate hatao |
| 3 | `AdvertiserDefaultsSchema` | ➕ `product_location: Optional[ProductLocationEnum]` add karo |
| 4 | ➕ Naya note | Selling location advertiser-level default hai, per-campaign override possible |
| 5 | ⚠ Confirm | Advertiser record me ye store hota hai? Ya Step 11 me poochhna hai? |
| 6 | Step 8 payload | `product_location` Step 8 me chahiye — kahan se aayega? (neeche dekho) |

## 🏷️ Nichod
> **David keh raha hai:** *"Selling location ka sawaal Step 1 se hata do."*

**Severity: 🔴 HIGH** — **Open Question #1 ka aadha jawab** + advertiser-attribute pattern strong karta hai.

---
---

# 🗨️ COMMENT #17 — "Product ASINs: comes later"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 1: Basics` → field matrix |
| **Row** | **Product ASINs** |
| **Highlighted** | **"Conditional"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"**comes later**"*

## 🎉 Ye PEHLA comment hai jahan David v2.0 se SEHMAT hai!
```
Document abhi:
  Product ASINs | Textarea | Conditional | 🔄 MOVED. Still required if
                                            ON_AMAZON, but the validation
                                            and collection now happens at
                                            Step 11 (tracking setup).
                                            See open question below

David: "comes later"
       ↑
   WAHI BAAT! v2.0 ne ASIN ko Step 11 me bheja — David SEHMAT hai.

→ 16 comments ke baad, pehli baar David keh raha hai "haan ye theek hai"
→ Bas: agar wo baad me aata hai, to Step 1 ke table me LIST hi mat karo
```

**Chhoti baat:** document ne row ko Step 1 me **rakha** hai (note ke saath). David keh raha hai — **table se nikaal do.** Jo baad me aata hai, wo Step 1 ki list me nahi hona chahiye.

---
---

# 🎉 #16 + #17 = OPEN QUESTION #1 SOLVE HO GAYA

## Document ka Open Question #1 (do baar likha gaya tha — page 8 aur page 18)

> *"⚠ Open question: `product_location` and `asin_numbers` are fields in the `POST /strategies/` payload called at Step 8. If ASINs are collected at Step 11 (after Step 8), they'd need to be **patched** onto the strategy afterwards. **Alternatively**, the ASIN question **stays early** (it's a plan field) and only the ad-tag check moves late. Confirm with client."*

**Do options the:**
| Option | Kya hai |
|---|---|
| **A** | Step 8 me bina ASIN create karo, Step 11 me **PATCH** karo |
| **B** | ASIN **Step 1 me hi rakho** (kyunki wo "plan field" hai) |

## ⚠ Is tracker ka pichhla recommendation ULTA nikla
```
Comment #1 ke section me likha gaya tha:
  "Main Option B recommend karta hun" — ASIN Step 1 me rakho

David ne Option A chuna:
  #16: "selling location can leave out"      → Step 1 se hatao
  #17: "product ASINs comes later"           → Step 1 se hatao

🔴 To wo recommendation GALAT tha. David ne question ANSWER kar diya:
   → OPTION A. Dono Step 1 se hatao.

💡 Reply me ye SAAF maano — "I'd recommended keeping it early;
   you've answered otherwise, so Option A it is."
```

## ✅ Par Step 8 ka problem kaise solve hoga? — Document me hi JAWAB hai
```
v1.1.0 ke create payload example ko dhyan se dekho:

  POST /api/strategies/
  {
    "product_location": "NOT_SOLD_ON_AMAZON",
    "product_asins": [],                    ← 🔴 KHAALI ARRAY!
    ...
  }

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 DOCUMENT KA APNA EXAMPLE DIKHATA HAI KI product_asins KHAALI         ║
║     BHEJA JA SAKTA HAI!                                                  ║
║                                                                          ║
║  → ASIN Step 8 par ZAROORI NAHI hai                                      ║
║  → Step 8 me [] bhejo, Step 11 me PATCH karo                             ║
║  → Option A KAAM KARTA HAI, aur document ne KHUD saabit kiya!            ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Aur `product_location` kahan se aayega Step 8 par?
```
Do possible jawab:

1️⃣ ADVERTISER RECORD se (#16 ka anumaan)
   → Advertiser ka guṇ hai, to Step 8 par pehle se pata hoga
   → Koi patch ki zaroorat nahi
   ✅ Sabse clean

2️⃣ Ya create payload me ye bhi OPTIONAL ho
   → Step 11 me patch ho jaaye
   🟡 Ek extra call

⚠ David se confirm karna hai
```

## ✅ Poora resolution
```
╔══════════════════════════════════════════════════════════════════════════╗
║  OPEN QUESTION #1 — RESOLVED (David's comments #16 + #17)                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ANSWER: Option A — dono Step 1 se hatao                                 ║
║                                                                          ║
║  Step 1:   ❌ selling location — HATAO                                    ║
║            ❌ product ASINs — HATAO                                       ║
║                                                                          ║
║  Step 8:   product_location  → 🏢 advertiser record se (poochhna nahi)   ║
║            product_asins     → [] khaali bhejo                           ║
║            (document ka apna example yahi dikhata hai)                    ║
║                                                                          ║
║  Step 11:  ✅ Sells on Amazon? (confirm karo, advertiser default se)      ║
║            ✅ Product ASINs collect + validate karo                       ║
║            ✅ PATCH /api/strategies/{id}/ se ASIN chipkao                 ║
║            ✅ Ad tag check + conversions                                  ║
║                                                                          ║
║  🔴 NAYA GAP: PATCH /api/strategies/{id}/ §4 catalogue me HAI HI NAHI!    ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Step 1 — Product ASINs row** | 🔴 **HATAO** — Step 11 me already hai |
| 2 | **Open Question #1 (page 8)** | ✅ **RESOLVED mark karo** — Option A, David ne confirm kiya |
| 3 | **Open Question #1 (page 18, repeated)** | ✅ Wo bhi RESOLVED mark karo |
| 4 | Step 8 | ➕ Note: `product_asins: []` bhejo · `product_location` advertiser se |
| 5 | Step 11 | ➕ `PATCH /api/strategies/{id}/` ka step add karo |
| 6 | 🔴 **§4 API catalogue** | ➕ `PATCH /api/strategies/{id}/` — **catalogue me hai hi nahi!** |

## 🏷️ Nichod
> **David keh raha hai:** *"ASIN baad me aata hai — to Step 1 ke table me list hi mat karo."*

**Severity: 🟡 MEDIUM** akele me — **par #16 ke saath milkar 🔴 HIGH**, kyunki dono Open Question #1 resolve karte hain.

---
---

# 🔗 COMMENTS #14–#17 KA JOD — Naya Theme + Revised Step 1

## 🔴 NAYA THEME 9 — "Advertiser attributes strategy schema me mila diye"
```
╔══════════════════════════════════════════════════════════════════════════╗
║  THEME 9: ADVERTISER ATTRIBUTES vs STRATEGY FIELDS                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Kuch fields ADVERTISER ke guṇ hain, CAMPAIGN ke nahi —                   ║
║  par document ne unhe Strategy schema me daal diya hai:                   ║
║                                                                          ║
║  #13  frequency_cap        → advertiser default  ✅ David ne confirm      ║
║  #15  product_categories   → advertiser default  ✅ David ne confirm      ║
║  #16  selling location     → advertiser attribute 🟡 anumaan              ║
║  #9   primary_currency     → advertiser account default 🟡 anumaan        ║
║                                                                          ║
║  🔴 TEST: "Kya ye value HAR CAMPAIGN me badalti hai?"                     ║
║     Agar NAHI → wo advertiser ka attribute hai, strategy ka nahi         ║
║                                                                          ║
║  Example:                                                                ║
║    BrightPath ki product category → hamesha "Education" (nahi badalti)   ║
║    BrightPath ka budget           → har campaign me alag (badalti hai)   ║
║                                                                          ║
║  💡 Baaki 11 comments padhte waqt YE TEST lagao.                         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 Source types ab AATH ho gaye
```
  💬 ASKED       trader se poochhna padega
  🧠 INFERRED    brief ke text se
  ⚙️ DERIVED     doosre field se (market → currency)
  🏢 ADVERTISER  advertiser ke defaults/record se     ← #13, #15, #16
  🤖 GENERATED   agent ne banaya                      ← #7
  🔒 FIXED       CTV ke liye constant                 ← #14 (streaming_tv)
  🔌 API         API response se                      ← #15 (ASIN → category)
  ⏭️ LATER       baad ke step me collect hota hai      ← ➕ NEW (#16, #17)
                 (Step 1 ke matrix me list hi nahi karna)
```

---

## 🎯 REVISED STEP 1 — Gyaarah comments ka nateeja

**11 comments** (#6, #7, #9, #10, #11, #12, #13, #14, #15, #16, #17) sirf **is ek table** par hain:

```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  STEP 1: BASICS — REVISED (David's comments #6–#17)                                  ║
╠═══════════════════════┬──────────────────────┬─────────────┬─────────────────────────╣
║ Field                 │ Data type            │ Requirement │ Source                  ║
╠═══════════════════════┼──────────────────────┼─────────────┼─────────────────────────╣
║ Strategy name         │ str                  │ Required    │ 🤖 GENERATED (#7)       ║
║ Flight dates          │ {lower, upper,       │ Required    │ 🧠 INFERRED             ║
║                       │  bounds}             │             │                         ║
║ Target markets        │ list[str] (M1: len 1)│ Required    │ 🧠 INFERRED (#8)        ║
║ Primary currency      │ CurrencyEnum         │ Required    │ ⚙️ DERIVED from market   ║
║                       │                      │             │    🏢 or advertiser (#9) ║
║ Creative durations    │ list[DurationEnum]   │ Required    │ 🧠 INFERRED             ║
║ Goal                  │ GoalEnum             │ Required    │ 🔒 FIXED = AWARENESS(#6)║
║ KPI                   │ KPIEnum              │ Required    │ ⚙️ DERIVED from goal(#6) ║
║ ➕ KPI target value   │ int (1–5)            │ Conditional │ 💬 ASKED (#10)          ║
║                       │                      │ (if freq)   │                         ║
║ Market budgets        │ list[{market,budget}]│ Required    │ 🧠 INFERRED (#11)       ║
║                       │ (M1: len 1)          │             │                         ║
║ Product categories    │ list[int]            │ Required    │ 🏢 ADVERTISER → 🧠 brief ║
║                       │                      │             │    → 🔌 ASIN API (#15)  ║
║ Frequency cap         │ int                  │ Optional    │ 🏢 ADVERTISER (#13)     ║
║ Budget cap            │ str                  │ Optional    │ 🏢 ADVERTISER / 💬 ASKED║
╠═══════════════════════┴──────────────────────┴─────────────┴─────────────────────────╣
║  ❌ HATAYE GAYE (5 fields):                                                          ║
║     Formats          → 🔒 system constant = ["streaming_tv"]        (#14)             ║
║     Base bids        → CTV me applicable nahi (fixed CPM deals)     (#12)             ║
║     Selling location → ⏭️ Step 11 / 🏢 advertiser                    (#16)             ║
║     Product ASINs    → ⏭️ Step 11                                   (#17)             ║
║     Ad tag conv.     → ⏭️ Step 11 (v2.0 ne pehle hi hataya tha)                       ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  📊 NATEEJA:                                                                         ║
║     Pehle:  14 fields · saare "Required" · sab trader se poochhne wale               ║
║     Ab:     12 fields · sirf 1 "ASKED" (KPI target, aur wo bhi conditional)          ║
║                                                                                      ║
║     🔴 ZERO fields "ASKED-and-Required" hain.                                        ║
║     → YAHI "a form that fills itself in as you chat" hai                             ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

> 💡 **Ye Kareem ka sabse strong deliverable hoga** — David dekhega ki uske 11 comments ek saaf, coherent naye design me badal gaye. Ek-ek comment ka alag jawab dene se ye bahut behtar hai.

---

## ✍️ DOCUMENT NOTES — #14, #15, #16, #17

### Note — Comment #14 (Formats)
> **📝 NOTE — Format is always `streaming_tv`; Prime Video is a provider (David Moss)**
>
> The matrix lists `formats` as *"streaming_tv and prime_video only"*. Per David it is **always `streaming_tv`** — a single value, not two.
>
> **The reason is a level error:** `prime_video` is not a format. It is a **provider** (supply source) *within* streaming TV.
>
> | Level | Values | Where it is decided |
> |---|---|---|
> | **Format** | `streaming_tv` | Step 1 — constant for a CTV module |
> | **Provider** | Prime Video · Netflix · Hulu · Disney+ | **Step 2** (inventory selection) |
>
> **This is already modelled correctly elsewhere in the document** — `SelectedDealSchema.provider` carries *"e.g. Prime Video, Netflix, Disney+"*. Listing Prime Video again as a format duplicates it at the wrong level.
>
> **And Step 2's own API example agrees with David:** `GET /api/deals/?markets={market}&formats=streaming_tv` — `streaming_tv` only. Step 1 and Step 2 currently contradict each other, and Step 2 is right.
>
> **Corrected:** `formats` becomes a **system constant** (`["streaming_tv"]`) rather than a field with choices — arguably it should not appear in the field matrix at all. `FormatEnum.PRIME_VIDEO` should be annotated as *"not a format — see `SelectedDealSchema.provider`"*.
>
> **⚠ To confirm:** v1.1.0's create payload used `"formats": ["prime_video"]`, so the Amazon DSP API may historically accept it. Which values does the real endpoint take?

### Note — Comment #15 (Product categories)
> **📝 NOTE — Product categories come from the advertiser, not the trader (David Moss)**
>
> `Product categories` is marked *"Required for video"*, implying the trader selects it per campaign. Per David, **there is a default on the advertiser, and it can also be implied from the brief.**
>
> **This is the second confirmation of advertiser-level defaults** (the first being Frequency cap), which makes the missing `AdvertiserDefaultsSchema` a firm requirement rather than a suggestion.
>
> **Why product category belongs to the advertiser:** it does not vary by campaign. BrightPath is always Education; Nike is always Apparel. Asking for it on every strategy is conceptually wrong — it is an attribute of the advertiser, not of the plan.
>
> **Resolution order (fallback chain):**
>
> | Priority | Source | Example |
> |---|---|---|
> | 1 | 🏢 **Advertiser default** | BrightPath → Education |
> | 2 | 🧠 **Inferred from brief** | *"education website"* → Education |
> | 3 | 🔌 **ASIN validation response** | the response returns `"product_category": "Electronics"` |
> | 4 | 💬 Ask the trader | last resort only |
>
> **Source 3 already exists in this document and has never been used** — §4.2's ASIN validation example returns `product_category` per ASIN. That should be wired to auto-fill this field.
>
> **Also:** *"Required for video"* is a v1.1.0 artefact. CTV is always video (see the Formats note), so the qualifier is redundant — it is simply **Required**.

### Note — Comment #16 (Selling location)
> **📝 NOTE — Selling location leaves Step 1 (David Moss)**
>
> Per David, this field **can be left out** of Step 1. Two reasons support it:
>
> 1. **It is a tracking question, not a planning question.** v2.0 already moved ASIN collection and ad-tag conversions to Step 11; selling location belongs with them.
> 2. **It is largely an advertiser attribute, not a campaign one.** Whether a brand sells on Amazon does not change per campaign. This makes it the third field in a row — after Frequency cap and Product categories — that is really an advertiser-level value.
>
> **Corrected:** remove the row from Step 1. Add `product_location` to `AdvertiserDefaultsSchema` as the default, overridable per campaign, with confirmation happening at Step 11 where the existing *"Sells on Amazon?"* question already sits.
>
> **⚠ To confirm:** is `product_location` held on the advertiser record, or should it simply be asked at Step 11?

### Note — Comment #17 (Product ASINs) — and Open Question #1 resolved
> **📝 NOTE — Product ASINs leave Step 1; this resolves Open Question #1 (David Moss)**
>
> Per David, ASINs **come later** — confirming v2.0's move to Step 11. The row should therefore not appear in the Step 1 matrix at all.
>
> **🎉 Taken together with the Selling location comment, this answers the open question raised twice in this document** (at Step 1 and again at Step 11):
>
> > *"`product_location` and `asin_numbers` are fields in the `POST /strategies/` payload called at Step 8. If ASINs are collected at Step 11, they'd need to be patched afterwards. Alternatively, the ASIN question stays early…"*
>
> **The answer is Option A — collect later and patch.** *(This document previously leaned toward Option B, keeping ASINs early. David's comments override that.)*
>
> **And the document already demonstrates that Option A works.** §4.2's create payload example sends:
> ```json
> "product_location": "NOT_SOLD_ON_AMAZON",
> "product_asins": [],          ← empty array
> ```
> So `POST /api/strategies/` accepts an empty ASIN list. The sequence becomes:
>
> | Step | What happens |
> |---|---|
> | **8** | `POST /api/strategies/` with `product_asins: []`; `product_location` taken from the advertiser record |
> | **11** | Collect and validate ASINs, then `PATCH /api/strategies/{id}/` to attach them, plus the ad-tag check and conversions |
>
> **🔴 One gap this exposes: `PATCH /api/strategies/{id}/` is not in the §4 API catalogue.** It needs adding, since the resolution depends on it.
>
> Both instances of the ⚠ open question (Step 1 and Step 11) should now be marked **RESOLVED**.

---

## 💬 REPLY DRAFTS — #14, #15, #16, #17

### Reply — Comment #14
> Agreed — and this is a level error on my part, not just a scoping one.
>
> `prime_video` isn't a format; it's a **provider** within streaming TV. And the document already models that correctly — `SelectedDealSchema.provider` carries *"e.g. Prime Video, Netflix, Disney+"*. So I'd listed Prime Video twice, once at the wrong level.
>
> **Step 2's own API example already agrees with you:** `GET /api/deals/?…&formats=streaming_tv`. Step 1 and Step 2 were contradicting each other and Step 2 was right.
>
> Making `formats` a system constant (`["streaming_tv"]`) rather than a field with choices, and annotating `FormatEnum.PRIME_VIDEO` as a provider, not a format.
>
> **One thing to confirm:** v1.1.0's create payload sent `"formats": ["prime_video"]`, so the DSP API may historically accept it. Which values does the real endpoint take?

### Reply — Comment #15
> Understood — and this is the second time advertiser defaults have come up, which tells me I've missed a whole concept. There's no advertiser-defaults schema, no endpoint and no state field anywhere in the document; I'm adding all of it.
>
> On product category specifically, you're right that it shouldn't be a per-campaign question at all — **it doesn't vary by campaign.** BrightPath is always Education. It's an attribute of the advertiser, not of the plan.
>
> I'll document a fallback chain: **advertiser default → infer from brief → ASIN validation response → ask.** That third one is worth flagging: §4.2's ASIN validation example already returns `"product_category"` per ASIN, and the document never uses it. Free signal we're throwing away.
>
> Also removing the *"for video"* qualifier — CTV is always video, so it's simply Required.

### Reply — Comment #16
> Will do. Two reasons it belongs out of Step 1:
>
> First, it's a **tracking** question, not a planning one — and v2.0 already moved ASINs and ad-tag conversions to Step 11, so this should go with them.
>
> Second, and I think more importantly: **it's mostly an advertiser attribute, not a campaign one.** Whether a brand sells on Amazon doesn't change per campaign. That makes it the third field in a row — after frequency cap and product categories — that's really an advertiser-level value that I'd put in the strategy schema. I'm treating that as a pattern and going back through the document for others.
>
> **To confirm:** is `product_location` held on the advertiser record, or should it just be asked at Step 11?

### Reply — Comment #17
> Confirmed — and taken with your selling-location comment, **this answers the open question I'd raised twice** (at Step 1 and again at Step 11) about ASINs being needed at Step 8 but collected at Step 11.
>
> I'd leaned toward the other option — keeping ASINs early because they're a plan field. **You've answered it the other way, so it's collect-later-and-patch.**
>
> And the document already shows that works: §4.2's create payload sends `"product_asins": []`. So `POST /strategies/` accepts an empty list. Sequence becomes: Step 8 creates with `[]` and takes `product_location` from the advertiser record; Step 11 collects and validates ASINs, then patches them on.
>
> **One gap that exposes:** `PATCH /api/strategies/{id}/` isn't in the API catalogue. Adding it, since the resolution depends on it.
>
> Marking both instances of that ⚠ open question resolved.

---
---

# 🗨️ COMMENT #18 — "Remove the technical need to select deals from a table" 🔴🔴

> **Ye ab tak ka SABSE BADA comment hai.** Ye poore Step 2 ka **interaction model** badal deta hai — sirf ek field nahi.
> Aur ye ab tak ke pattern ("poochho mat, nikaalo") ka **sabse bada instance** hai.

## 📍 Location
| | |
|---|---|
| **Section** | `Step 2: CTV Inventory (the tier fork)` → field matrix |
| **Row** | **Selected deals** |
| **Highlighted** | **"Checkbox table"** (Type column) |
| **Asar** | 🔴 Poora Step 2 ka design + Step 2 ke API calls + Basil ka canvas + state machine node |

## 💬 David ne exactly kya likha
> *"In majority of cases **we want to pick the deals based on the requirements of the brief** which we can do if we know the **market, duration and channel**. Optional **ROS / genre** and the different **targeting types** mentioned later. They **may provide a deal id if they have 1 in mind** but we want to **remove the technical need to select deals from a table**. **We don't surface the underlying deal choices to the user - only the CPM**"*

## 🔍 Line-by-line — SAAT alag claims hain isme
| # | David ka hissa | Matlab |
|---|---|---|
| 1 | *"In majority of cases **we want to pick the deals**"* | 🔴 **AGENT deals chunega**, trader nahi |
| 2 | *"based on the **requirements of the brief**"* | Brief se requirements nikaal kar match karega |
| 3 | *"which we can do if we know the **market, duration and channel**"* | Teen input kaafi hain deal chunne ke liye |
| 4 | *"Optional **ROS / genre** and the different **targeting types**"* | Plus optional refinements |
| 5 | *"They **may provide a deal id** if they have 1 in mind"* | ⚙️ **Escape hatch** — trader chahe to deal ID de sakta hai |
| 6 | *"we want to **remove the technical need to select deals from a table**"* | 🔴 **Table HATAO** |
| 7 | *"**We don't surface the underlying deal choices** to the user - **only the CPM**"* | 🔴🔴 **Trader ko deals DIKHENGI HI NAHI. Sirf CPM.** |

## ❌ Document ka model vs ✅ David ka model

### Document abhi (v1.1.0 se aaya hua)
```
Step 2: DEALS TABLE dikhao, trader checkbox tick kare

┌──────────────────────────────────────────┬───────────┬────────┬─────┐
│ Deal Name                                │ Deal Type │ CPM    │ [x] │
├──────────────────────────────────────────┼───────────┼────────┼─────┤
│ Prime Video | Preferred Deal | UK - 30   │ Preferred │ £28.88 │ [x] │
│ Prime Video | Education | UK - 30        │ Preferred │ £31.50 │ [ ] │
│ Netflix | Preferred | UK - 30            │ Preferred │ £32.00 │ [x] │
└──────────────────────────────────────────┴───────────┴────────┴─────┘

Trader ka kaam:
  • Deal ke naam padho
  • Samjho "Preferred Deal" ka matlab kya hai · "ROS" kya hai
  • CPM compare karo · Checkbox tick karo

🔴 Ye TECHNICAL kaam hai, STRATEGIC nahi.
```

### David ka model
```
Step 2: Agent KHUD deals chunta hai. Trader ko sirf CPM dikhta hai.

Agent ke paas ye pehle se hai:
  market   = GB          ← Step 1 se
  duration = 30s         ← Step 1 se
  channel  = Prime Video ← trader ne platform chuna
  + brief: "education courses"

Agent (peeche se, chup-chaap):
  → GET /api/deals/?markets=GB&formats=streaming_tv
  → 8 deals mile
  → Brief "education" hai → Education genre deal best match
  → Deal EXT7P75718S8MNR chun li (£31.50)
  → Trader ko DEAL DIKHAYI HI NAHI

Trader ko dikhta hai:
  ┌──────────────────────────────────────────────────┐
  │  Prime Video                                     │
  │  CPM: £31.50                                     │
  │  Estimated impressions: 190,476                  │
  └──────────────────────────────────────────────────┘
      ↑ Bas itna. Koi deal name, koi deal ID, koi table.
```

## 🔴 Sabse gehri baat — FLOW ULTA HO GAYA
```
╔══════════════════════════════════════════════════════════════════════════╗
║  ❌ DOCUMENT KA FLOW:  DEAL PEHLE, TARGETING BAAD ME                     ║
║     Trader deal chunta hai (table se)                                    ║
║          ↓                                                               ║
║     Us deal me jo targeting hai, wo mil jaati hai                        ║
║          ↓                                                               ║
║     Trader ko BAAD ME pata chalta hai kya mila                            ║
║     🔴 Problem: trader ko deal NAAM se GUESS karna padta hai (#1 ka issue)║
╠══════════════════════════════════════════════════════════════════════════╣
║  ✅ DAVID KA FLOW:  REQUIREMENTS PEHLE, DEAL BAAD ME                     ║
║     Trader apni ZAROORAT batata hai                                      ║
║       (market, duration, channel, genre, targeting)                       ║
║          ↓                                                               ║
║     Agent us zaroorat se MATCHING deal DHOONDHTA hai                      ║
║          ↓                                                               ║
║     Trader ko CPM dikhta hai                                             ║
║     ✅ Faayda: trader ko technical detail se matlab hi nahi               ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🎉 Ye COMMENT #1 ki tension SOLVE kar deta hai
```
Comment #1 me David ne kaha tha:
  "[SSP targeting] is specific to the deal that is chosen or curated"

Aur maine problem uthaya tha:
  "agar deal ki targeting dikhti nahi, to trader ANDHERE me kharid raha hai"

╔══════════════════════════════════════════════════════════════════════════╗
║  🎉 COMMENT #18 US PROBLEM KA JAWAB HAI:                                 ║
║                                                                          ║
║  Trader ko deal ki targeting SAMAJHNE ki zaroorat NAHI hai —              ║
║  kyunki wo apni targeting ki ZAROORAT PEHLE batata hai,                   ║
║  aur agent us zaroorat se matching deal dhoondhta hai.                    ║
║                                                                          ║
║  Trader:  "Mujhe 25-45 age, Drama content chahiye"                       ║
║  Agent:   [matching deal dhoondhta hai] → "£35.50 CPM"                   ║
║           ↑ Trader ko deal ka naam padhne ki zaroorat NAHI                ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 🔴 PAR — isse Comment #1 ka SAWAAL #2 **BLOCKING** ban jaata hai
```
Comment #1 ka sawaal tha:
  "For 3P pre-curated deals, can we see the built-in targeting in the deal data?"

Pehle ye sawaal "TRADER KO DIKHANE ke liye" tha (nice-to-have).
AB ye sawaal "AGENT KE MATCHING KE LIYE" hai — aur wo BLOCKING hai!

Kyun?
  Agent ko deals MATCH karne hain requirements se
  → Uske liye agent ko HAR DEAL ki targeting PADHNI padegi
  → Agar wo structured metadata me nahi hai...

  ❌ Agent ko deal ke NAAM se parse karna padega:
     "Netflix | UK - 30 - Drama - A18-34"
     → "Drama" nikaalo, "A18-34" nikaalo
     → 🔴 String parsing = FRAGILE = Zero-Hallucination ke KHILAAF

  ✅ Structured metadata chahiye:
     {"built_in_targeting": {"genres": ["Drama"], "age": "18-34"}}

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 David ka #18 model KAAM HI NAHI KAREGA agar deal ki targeting        ║
║     structured data me nahi hai.                                         ║
║  → Comment #1 ka sawaal #2: OPTIONAL se BLOCKING ban gaya                 ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Reply me ye zaroor likhna — David ko dikhega ki tumne uske DO comments
   ko JODKAR dekha aur ek dependency nikaal li.
```

## 🔍 "Channel" ka matlab — ⚠ Naming collision
```
David ne teen inputs diye: market, duration, aur "channel"

Par document me "channel" ke DO matlab hain:

╔══════════════════════════════════════════════════════════════════════════╗
║  MATLAB 1 — ChannelTypeEnum                                              ║
║    DSP = "dsp"  ·  SPONSORED = "sponsored"                               ║
║    → Ye "buying channel" hai (DSP vs Amazon search ads)                  ║
║                                                                          ║
║  MATLAB 2 — Rate card ka "channel"                                       ║
║    GET /api/rates/ctv/{market}/  →  "channels, durations, CPMs"          ║
║    → Ye PROVIDER hai: Prime Video, Netflix, Disney+                      ║
╚══════════════════════════════════════════════════════════════════════════╝

David ka matlab: MATLAB 2 = provider (Prime Video / Netflix / Disney+)
  Kyunki wahi rate card me use hota hai, aur wahi deal chunne ke liye chahiye

⚠ Par schema me field ka naam `provider` hai, "channel" nahi.
  → Ek hi cheez ke TEEN naam: "channel" (David), "channels" (rate card),
    "provider" (schema)
  → Aur `ChannelTypeEnum` "channel" ko kisi AUR cheez ke liye use karta hai
  → Ek naam par settle karna padega
```

## 🔴 Trader kya chunta hai vs Agent kya chunta hai — naya batwara
```
╔══════════════════════════════════════════════════════════════════════════╗
║  TRADER KA KAAM (strategic)          │  AGENT KA KAAM (technical)         ║
╠══════════════════════════════════════┼════════════════════════════════════╣
║  ✅ Kaunse PLATFORMS?                │  ✅ Kaunsi DEAL ID?                ║
║     Prime? Netflix? Disney+?         │     EXT7P75718S8MNR                ║
║     ← ASLI faisla: alag audience,    │     ← Technical detail             ║
║       alag capabilities, alag CPM    │                                    ║
║  ✅ ROS ya specific GENRE?           │  ✅ Us genre ki kaunsi deal?       ║
║  ✅ Kaunsi TARGETING?                │  ✅ Kaunsi deal wo support karti   ║
║  ✅ Kitna BUDGET?                    │  ✅ Deal type · inventory tier     ║
║  ⚙️ (Optional) specific deal ID      │                                    ║
╚══════════════════════════════════════┴════════════════════════════════════╝

🎯 Trader "KYA CHAHIYE" batata hai. Agent "KAISE MILEGA" nikaalta hai.
```

## 🎉 KAREEM NE YE PATTERN PEHLE HI BANA LIYA THA — sirf generalize nahi kiya
```
Document ka Tier 3 (Disney+ — "3P needs curation") treatment dekho:

  "➕ NEW — Curation capture (for 3P-needs-curation tier): When deals
   can't be selected yet (Disney+ etc.), the agent captures what VOW
   needs to curate later: genres, durations, targeting preferences,
   budget, flight dates."

  Curation fields:
    Curation: genres          ← trader ki ZAROORAT
    Curation: durations       ← trader ki ZAROORAT
    Curation: targeting prefs ← trader ki ZAROORAT
    Curation: budget · flight dates

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 YE BILKUL DAVID KA MODEL HAI!                                        ║
║                                                                          ║
║  Tier 3 me: "deal nahi hai, to trader ki REQUIREMENTS lo"                ║
║  David keh raha hai: "SAB TIERS me requirements lo, deals mat dikhao"     ║
║                                                                          ║
║  → Kareem ne SAHI pattern bana liya tha (Tier 3 ke liye)                 ║
║  → Bas usko Tier 1 aur Tier 2 par apply nahi kiya                        ║
║  → Wahan purana "checkbox table" model chhod diya (v1.1.0 se)             ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Reply me ye likhna BAHUT strong hoga — ownership dikhata hai.
```

## 🔗 COMMENT #11 se judav — aur ek gehra sabak
```
David ne PHIR SE "Type" column ki value highlight ki:

  #11: "Table"          (Market budgets ka Type)   → UI widget hai
  #18: "Checkbox table" (Selected deals ka Type)   → UI widget hai

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 GEHRA SABAK:                                                         ║
║                                                                          ║
║  Kyunki document ne "Checkbox table" ko Type column me daala,             ║
║  usne GALTI SE EK INTERACTION MODEL SPECIFY KAR DIYA —                   ║
║  aur wo interaction model GALAT hai.                                     ║
║                                                                          ║
║  Agar Type me sirf likha hota:                                           ║
║    "Selected deals | list[SelectedDealSchema] | Required"                ║
║  → To koi "checkbox table" hi nahi hoti jispar objection ho              ║
║  → Aur UI ka faisla Riddhi/Basil karte, jo SAHI hai                      ║
║                                                                          ║
║  💡 UI widgets DATA CONTRACT me nahi hone chahiye — kyunki wo             ║
║     CHUP-CHAAP galat design LOCK kar dete hain.                           ║
╚══════════════════════════════════════════════════════════════════════════╝

→ Ye #11 ke "Type column todo" recommendation ko BAHUT strong bana deta hai,
  kyunki ab uska nuksaan CONCRETE hai, sirf theory nahi.
```

## ✅ Kya SURFACE hoga, kya HIDE hoga
```
┌─────────────────────────────────┬────────────────────────────────────────┐
│ ✅ TRADER KO DIKHEGA            │ ❌ TRADER KO NAHI DIKHEGA              │
├─────────────────────────────────┼────────────────────────────────────────┤
│ Provider / channel              │ Deal name                              │
│   "Prime Video"                 │   "Prime Video | Preferred Deal | …"   │
│ CPM  "£31.50"                   │ Deal ID  "EXT7P75718S8MNR"             │
│ Estimated impressions           │ Deal type (Preferred/PG/Private)       │
│   "190,476"                     │   ⚠ PAR PG ka WARNING dena zaroori hai!│
│ Genre (agar specific hai)       │ Poori deals ki LIST                    │
│   "Education content"           │   (8 deals thi, ek chuni)              │
│ 🔴 TIER-based capability        │ Deal ke ad_lengths, internal fields    │
│   "reach forecast available"     │                                        │
│   "reach not available"          │                                        │
│   ← ZAROORI HAI (honesty rule)   │                                        │
└─────────────────────────────────┴────────────────────────────────────────┘
```

### ⚠ Ek EXCEPTION — PG deal ka warning
```
Comment #12 ke context me: PG deal me "poora budget owed" aur "pause nahi
kar sakte" (§2.3).

Agar agent CHUP-CHAAP ek PG deal chun le, aur trader ko deal type dikhe hi
nahi — to trader ko pata hi nahi chalega ki uska £6,000 COMMIT ho gaya hai!

🔴 Isliye: deal IDENTITY hide karo, par COMMITMENT ka warning DENA ZAROORI:

  Agent: "Prime Video, CPM £31.50, 190,476 impressions.
          ⚠ Ye ek Programmatic Guaranteed deal hai — poora £6,000 commit
            ho jaayega aur pause nahi kar sakte. Preferred deal chahiye
            (pause-able, thoda mehnga £33.20)?"

→ Ye "only the CPM" ka apwaad hai, par zaroori hai
→ ⚠ David se confirm karna chahiye — ya agent PG kabhi auto-select na kare?
```

## ✅ Genre upsell logic BACH JAATA HAI
```
Document ka genre upsell (➕ NEW in v2.0):
  "Prime Video ROS at $18.22 vs Action at $22.07 — the agent should
   recommend when the brief implies a genre match"

Agent: "Do options hain:
          Prime Video, koi specific content nahi:  £18.22 CPM → 439,000 imp
          Prime Video, Sports content:             £22.07 CPM → 362,000 imp
        Tumhara product gym-goers ke liye hai — main Sports recommend karta hun."

╔══════════════════════════════════════════════════════════════════════════╗
║  ✅ Isme koi DEAL NAME nahi, koi DEAL ID nahi. Sirf: CONTENT TYPE + CPM. ║
║  → David ke "only the CPM" se BILKUL match karta hai                     ║
║  → Genre upsell feature ZINDA rehta hai                                  ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🎯 NAYA STEP 2 — poora field matrix
```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  STEP 2: CTV INVENTORY — REVISED (David's #18 + #1 + #11 + #14)                       ║
╠═══════════════════════════┬───────────────────────┬─────────────┬────────────────────╣
║ Field                     │ Data type             │ Requirement │ Source             ║
╠═══════════════════════════┼───────────────────────┼─────────────┼────────────────────╣
║ ➕ Channel / provider     │ list[str]             │ Required    │ 🧠 INFERRED from   ║
║   (Prime/Netflix/Disney)  │                       │             │    brief · 💬 ASKED║
║                           │                       │             │    ← STRATEGIC     ║
║ ➕ ROS or genre pref      │ Optional[str]         │ Optional    │ 🧠 INFERRED        ║
║ ➕ Targeting requirements │ dict                  │ Optional    │ ⏭️ Targeting step   ║
║                           │                       │             │    se aata hai (#5)║
║ 🔄 Selected deals         │ list[SelectedDeal     │ Required    │ 🤖 AUTO-MATCHED    ║
║   (NOT SURFACED)          │      Schema]          │             │    (market+duration║
║                           │                       │             │    +channel se)    ║
║ ➕ Specific deal ID       │ Optional[str]         │ Optional    │ 💬 ASKED           ║
║   (escape hatch)          │                       │             │    (agar mind me)  ║
║ ✅ Inventory tier         │ InventoryTierEnum     │ Derived     │ 🔌 API             ║
║ ✅ CTV rate card          │ reference             │ Read        │ 🔌 API             ║
║ ✅ Curation fields (×5)   │ CurationRequirements  │ Required if │ 💬 ASKED / 🧠      ║
║   (Tier 3 only)           │      Schema           │ Tier 3      │    INFERRED        ║
╠═══════════════════════════┴───────────────────────┴─────────────┴────────────────────╣
║  ❌ HATAYA GAYA:                                                                     ║
║     "Checkbox table" — UI widget tha, data type nahi (#11, #18)                       ║
║     Deal browsing/selection interaction — agent karega (#18)                          ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  🔴 SURFACED: provider · CPM · impressions · tier capability                          ║
║     ⚠ + PG commitment warning (agar PG deal chuni)                                   ║
║  🔴 NOT SURFACED: deal name · deal ID · deal type · deals ki list                    ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

## 🔧 Schema changes
```python
class SelectedDealSchema(BaseModel):
    """🔄 CHANGED — deals are auto-matched, not trader-selected (#18)"""
    deal_id: str
    name: str                    # internal only — not surfaced
    cpm: str                     # ✅ SURFACED
    inventory_tier: InventoryTierEnum   # ✅ SURFACED (capability ke liye)
    provider: str                # ✅ SURFACED
    genre: Optional[str]         # ✅ SURFACED (agar specific hai)
    ad_lengths: list[str]        # internal only
    deal_type: str               # internal — ⚠ PAR PG ka warning surface karo

    # ➕ NEW (#18)
    selection_method: str = Field("AUTO_MATCHED",
        description="AUTO_MATCHED | TRADER_SPECIFIED")
    matched_on: Optional[dict] = Field(None,
        description="Criteria used: market, duration, channel, genre, targeting")
    is_surfaced_to_trader: bool = Field(False,
        description="Deal identity is internal; only CPM is surfaced")


class DealMatchCriteriaSchema(BaseModel):
    """➕ NEW — what the agent matches deals against (#18)"""
    market: str
    duration: DurationEnum
    channel: str                              # provider — ⚠ naming resolve karo
    ros_or_genre: Optional[str] = None
    targeting_requirements: Optional[dict] = None
    trader_specified_deal_id: Optional[str] = None    # escape hatch
```

## 🎯 Kyun ye comment kiya (David ki niyat)
```
Wajah 1 — Deal selection ek TECHNICAL kaam hai, STRATEGIC nahi
  Trader ka asli faisla: "Prime Video par chalao, education content ke saath"
  Deal ID chunna: bas plumbing hai
  → Insaan ka time strategic faislon me lagna chahiye

Wajah 2 — 🔴 YAHI POORE PRODUCT KA MAKSAD HAI
  Task slide: "a form that fills itself in as you chat"
  → Agar trader ko phir bhi table se checkbox tick karna pade,
    to product ne KUCH NAHI BADLA — bas wizard ko chat me daal diya

  🔴 Ye David ka SABSE FUNDAMENTAL point hai. #4,#5,#6,#7,#9,#13,#15,#16
     sab isi taraf ishara kar rahe the — par #18 ek POORA STEP ki
     interaction hata deta hai, sirf ek field nahi.

Wajah 3 — Deal names insaan ke padhne ke liye nahi bane
  "Prime Video | Preferred Deal | UK - 30 - ROS"
  → "ROS" kya hai? "Preferred" kya hai? Naye trader ko samajh nahi aayega
  → Aur galat deal tick karne se poora plan galat ho jaayega

Wajah 4 — Escape hatch se azadi bachi rehti hai
  "They may provide a deal id if they have 1 in mind"
  → Jo trader jaanta hai, wo override kar sakta hai
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | Step 2 — Selected deals Type | "Checkbox table" → `list[SelectedDealSchema]` (#11 ka fix bhi) |
| 2 | Step 2 — Selected deals Source | 🔴 **🤖 AUTO-MATCHED** (market + duration + channel se) |
| 3 | Step 2 — ➕ naya field | `Channel / provider` — **STRATEGIC choice**, trader chunta hai |
| 4 | Step 2 — ➕ naya field | `ROS or genre preference` (Optional, inferred) |
| 5 | Step 2 — ➕ naya field | `Specific deal ID` — **escape hatch** (Optional) |
| 6 | 🔴 Step 2 — ➕ naya sub-section | **"Deal matching, not deal selection"** — poora naya interaction model |
| 7 | 🔴 Step 2 — ➕ naya sub-section | **"What is surfaced vs internal"** — CPM haan, deal identity nahi |
| 8 | `SelectedDealSchema` | ➕ `selection_method`, `matched_on`, `is_surfaced_to_trader` |
| 9 | ➕ Naya schema | `DealMatchCriteriaSchema` |
| 10 | Step 2 — Curation section | ➕ Note: **ye pattern SAB tiers par lagta hai**, sirf Tier 3 par nahi |
| 11 | `GET /api/deals/filter-properties/` | Purpose badla — filter UI ke liye nahi, **matching ke liye** |
| 12 | State machine `select_inventory` | 🔄 Rename → **`match_inventory`** |
| 13 | ⚠ Naming | "channel" vs "channels" vs "provider" — ek naam par settle karo |
| 14 | ⚠ PG warning | Deal type hide hai, par PG commitment ka warning surface karo |
| 15 | 🔴 Comment #1 se link | Deal ki built-in targeting **structured metadata me chahiye** — warna matching kaam nahi karegi |
| 16 | Basil ka adaptive canvas | Step 2 ka artifact badla — deals table nahi, **CPM summary** |

## ✍️ DOCUMENT NOTE (draft)

> **📝 NOTE — Deals are matched by the agent, not selected by the trader (David Moss)**
>
> `Selected deals` is typed **"Checkbox table"**, which specifies an interaction the trader should not have to perform. Per David: *"we want to **remove the technical need to select deals from a table**… **We don't surface the underlying deal choices to the user — only the CPM**."*
>
> **The flow inverts.** Currently the trader picks a deal and inherits whatever it carries. Instead, the trader states requirements and the agent finds the deal that satisfies them:
>
> | | **Was (v1.1.0 model, retained in v2.0)** | **Now** |
> |---|---|---|
> | Trader does | Browses a deal table, reads deal names, ticks checkboxes | States requirements: channel, genre/ROS, targeting |
> | Agent does | Renders the table | **Matches deals** from market + duration + channel |
> | Trader sees | Deal names, deal IDs, deal types, CPMs | **Provider, CPM, impressions, tier capability** |
> | Escape hatch | — | Trader **may supply a deal ID** if they have one in mind |
>
> **The division of labour:**
>
> | Trader — strategic | Agent — technical |
> |---|---|
> | Which platforms (Prime / Netflix / Disney+) | Which deal ID |
> | ROS or a specific genre | Which deal in that genre |
> | Targeting requirements | Which deal supports that targeting |
> | Budget | Deal type, inventory tier derivation |
>
> **This document already contains the correct pattern — it just was not generalised.** The Tier 3 (3P-needs-curation) treatment captures *"genres, durations, targeting preferences, budget, flight dates"* rather than presenting deals, because Disney+ deals do not exist yet. That is exactly the model David is describing. Tiers 1 and 2 kept the v1.1.0 checkbox table instead of adopting it.
>
> **What is surfaced vs internal:**
>
> | ✅ Surfaced | ❌ Internal |
> |---|---|
> | Provider / channel · CPM · estimated impressions · genre (if specific) · **tier capability** (whether reach is forecastable) | Deal name · deal ID · deals list · `ad_lengths` |
>
> **⚠ One necessary exception to "only the CPM":** deal *type* must not be silently hidden. A **Programmatic Guaranteed** deal commits the full budget and cannot be paused (§2.3). If the agent selects one without saying so, the trader commits spend without knowing. The agent must surface the **commitment consequence** even while hiding the deal identity.
>
> **Genre upsell survives unchanged.** The ➕ NEW genre-upsell logic (*"Prime Video ROS at $18.22 vs Action at $22.07"*) presents content type and CPM only — no deal identity. It already conforms to this model.
>
> **🔴 A dependency this creates.** For the agent to match deals against stated targeting requirements, it must be able to **read each deal's built-in targeting from structured metadata**. If that targeting exists only inside the deal *name* (`"Netflix | UK - 30 - Drama - A18-34"`), the agent would have to parse strings — fragile, and contrary to the Zero-Hallucination principle. **This turns the open question raised on the tier table — whether 3P deals expose their built-in targeting — from a display concern into a blocking prerequisite for this step.**
>
> **Schema additions:**
> ```python
> # SelectedDealSchema
> selection_method: str = Field("AUTO_MATCHED",
>     description="AUTO_MATCHED | TRADER_SPECIFIED")
> matched_on: Optional[dict] = Field(None,
>     description="Criteria used: market, duration, channel, genre, targeting")
>
> class DealMatchCriteriaSchema(BaseModel):
>     """➕ NEW — what the agent matches deals against"""
>     market: str
>     duration: DurationEnum
>     channel: str                    # provider
>     ros_or_genre: Optional[str] = None
>     targeting_requirements: Optional[dict] = None
>     trader_specified_deal_id: Optional[str] = None   # escape hatch
> ```
>
> **Also:** the state-machine node `select_inventory` should become `match_inventory`, and `GET /api/deals/filter-properties/` changes purpose — it no longer populates filter dropdowns for a table, it tells the agent which genres and lengths are available to match against.
>
> **⚠ Naming to resolve:** David uses **"channel"**, the rate card endpoint uses **"channels"**, and `SelectedDealSchema` uses **`provider`** — all for the same thing (Prime Video / Netflix / Disney+). Meanwhile `ChannelTypeEnum` uses "channel" for something else entirely (`dsp` / `sponsored`). One term should be chosen.

## 💬 REPLY DRAFT

> This is the biggest one so far, and I think it's the point the whole product turns on.
>
> You're right that picking a deal from a table is plumbing, not a decision. **The flow should invert**: the trader states requirements — channel, ROS or genre, targeting — and the agent finds the deal that satisfies them. What surfaces is provider, CPM, impressions and whether reach is forecastable. Deal names, IDs and the table itself go away, with a deal ID accepted as an override when the trader has one in mind.
>
> **The thing I want to own: I already wrote this pattern and didn't generalise it.** The Tier 3 curation capture — genres, durations, targeting preferences, budget, dates — is exactly what you're describing. I applied it to Disney+ because those deals don't exist yet, and left the v1.1.0 checkbox table on Tiers 1 and 2 where they do. It should have been the model for all three.
>
> Two things I need to flag:
>
> **1. This makes an earlier open question blocking.** On the tier table you noted that SSP targeting is *"specific to the deal that is chosen or curated"*, and I asked whether that built-in targeting is visible in the deal data. That was a display question then. Now it's a prerequisite — **if the agent is matching deals against targeting requirements, it has to read each deal's targeting from structured metadata.** If it only exists in the deal name (`"Netflix | UK - 30 - Drama - A18-34"`), we'd be parsing strings to make buying decisions, which I don't want to do.
>
> **2. One exception to "only the CPM".** Deal *type* shouldn't be silently hidden. A PG deal commits the full budget and can't be paused. If the agent picks one without saying so, the trader commits spend without knowing. I'll hide the deal identity but surface the commitment — *"this is guaranteed inventory; the full £6,000 is committed and can't be paused."* Tell me if you'd rather it never auto-select PG at all.
>
> Genre upsell survives as-is — it already presents content type and CPM with no deal identity.
>
> Also worth settling: you say **"channel"**, the rate card says **"channels"**, and my schema says **`provider`** — all the same thing. And `ChannelTypeEnum` uses "channel" for `dsp`/`sponsored`. I'll pick one term unless you have a preference.

## ❓ David se poochhne wale sawaal
| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | 🔴 Deal ki built-in targeting **structured metadata** me hai? (Comment #1 ka sawaal — ab BLOCKING) | Iske bina auto-matching kaam nahi karegi |
| 2 | PG deal auto-select karna chahiye, ya kabhi nahi? Aur warning kaisa ho? | Paisa commit ho jaata hai |
| 3 | "channel" / "channels" / "provider" — kaunsa naam final? | Naming consistency |
| 4 | Agar kai deals match karein, agent kaise pick kare — sabse sasta? Sabse relevant? | Matching logic define karni hai |
| 5 | Agar KOI deal match na kare, agent kya kare? | Failure protocol |

## 🏷️ Nichod
> **David keh raha hai:** *"Trader ko deals ki table se checkbox tick karwana technical kaam hai. Agent ko brief se khud deal chunni chahiye — market, duration aur channel pata hai to ho jaayega. Trader ko deal ka naam ya ID dikhana hi nahi — sirf CPM. Haan, agar trader ke paas koi khaas deal ID hai to wo de sakta hai."*

**Severity: 🔴🔴 VERY HIGH** — kyunki:
- **Poore Step 2 ka interaction model** badalta hai
- **Naye fields** chahiye (channel, genre pref, deal ID escape hatch, selection_method, matched_on)
- **Comment #1 ka sawaal BLOCKING** ban jaata hai (structured deal targeting metadata)
- **Basil ka canvas** badalta hai (deals table nahi, CPM summary)
- **State machine node** rename hota hai (`select_inventory` → `match_inventory`)
- Aur ye **poore product ke maksad** ko touch karta hai

---
---

# 🗨️ COMMENT #19 — "Netflix/Disney can use Amazon audiences too"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 4: Audiences` → **Constraints for CTV** |
| **Highlighted** | **"Netflix/Disney"** |
| **Poori line** | *"Amazon audiences **only apply to Amazon-owned inventory**. For Netflix/Disney, their own targeting applies"* |

## 💬 David ne exactly kya likha
> *"**can use amazon audiences too**"*

## 🎯 Ye wahi galti hai jo #1 me thi — DOOSRI jagah
```
Comment #1  → §2.3 tier table ka "Audiences" column
Comment #19 → Step 4 ka "Constraints for CTV" list

DONO me SAME absolute statement tha.

✅ Aur Note 1 me ye PEHLE SE flag kiya gaya tha:
   "Also corrected in: the Targeting step constraints, where the same
    absolute phrasing appeared."

→ David ne ab us doosri jagah par bhi comment kar diya
→ Prediction sahi tha
```

## 🔴 PAR #19 me NAYA bhi hai — aur Note 1 ka ek claim GALAT tha
```
COMMENT #1 me David ne likha:
  "whether to use Amazon's targeting (MAY BE LIMITED in functionality
   i.e. only device)"
                    ↑
              "MAY BE limited" — "IS limited" NAHI!

COMMENT #19 me David ne likha:
  "can use amazon AUDIENCES too"
                     ↑
        "audiences" — sirf "targeting" nahi!
```

### ⚠ Note 1 me maine over-claim kar diya tha
```
Note 1 me maine likha tha:
  "On 3P inventory the publisher does not pass viewer identity — only
   what appears in the bid request (device, coarse geo). Amazon can
   THEREFORE ONLY target on what the publisher sends, which is why
   device-level is the reliable case."

🔴 Ye claim GALAT / bahut strong hai.

Maine maan liya tha: "identity nahi milti to audience targeting IMPOSSIBLE"
Par David keh raha hai Amazon audiences 3P par KAAM KARTI HAIN.

→ Amazon ke paas koi tarika hai (identity resolution / device graph /
  publisher data partnership). Wo mechanism mujhe nahi pata, par EXIST
  karta hai.

✅ SAHI framing:
   Amazon audiences 3P par lag SAKTI hain
   Par capability "MAY BE limited" — deal/provider ke hisaab se
   Ye ek CHOICE hai, ek DEEWAR nahi

💡 Reply me ye saaf maanna hai. Apni galat wajah defend nahi karni.
```

## ❌ Document abhi vs ✅ Reality
```
Document (galat):
  "Amazon audiences ONLY APPLY to Amazon-owned inventory.
   For Netflix/Disney, their own targeting applies"
                ↑
        ❌ "ONLY" — absolute aur galat

╔══════════════════════════════════════════════════════════════════════════╗
║  REALITY: AMAZON AUDIENCES 3P PAR BHI LAG SAKTI HAIN                     ║
║                                                                          ║
║   Option A: AMAZON AUDIENCES                                             ║
║     ✅ Lag SAKTI hain (David ne confirm kiya)                             ║
║     ⚠ Capability "may be limited" — deal/provider ke hisaab se           ║
║     💰 Amazon 1P data fee lagegi (Comment #2 ka rule)                     ║
║                                                                          ║
║   Option B: SSP / PUBLISHER KI APNI TARGETING                            ║
║     ✅ Zyada powerful (unka apna data)                                    ║
║     🔴 DEAL ME BANDHI hui (Comment #1)                                    ║
║     💰 CPM badhati hai                                                    ║
║                                                                          ║
║  → Ya DONO? (⚠ poochhna hai)                                             ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 Tier table ka "Audiences" column ab DIFFERENTIATOR NAHI hai
```
❌ PEHLE:
┌──────────────────┬────────────────┬──────────────────────────────┐
│ Tier             │ Reach forecast │ Audiences                    │
├──────────────────┼────────────────┼──────────────────────────────┤
│ Amazon owned     │ ✅ Available    │ Amazon audiences             │
│ 3P pre-curated   │ ❌ Not avail.  │ Their own targeting          │ ← ❌ GALAT
│ 3P needs curat.  │ ❌ Not avail.  │ Their own targeting          │ ← ❌ GALAT
└──────────────────┴────────────────┴──────────────────────────────┘
        ↑ "Audiences" column tiers ko ALAG batata tha

✅ AB — Audiences column tiers me farak NAHI karta:
┌──────────────────┬────────────────┬────────────────┬──────────────────────┐
│ Tier             │ Deals          │ Reach forecast │ Audiences/Targeting  │
├──────────────────┼────────────────┼────────────────┼──────────────────────┤
│ Amazon owned     │ Selectable now │ ✅ Available    │ Amazon audiences     │
│ 3P pre-curated   │ Selectable now │ ❌ Not avail.  │ CHOICE: Amazon       │
│                  │                │                │ (may be limited)     │
│                  │                │                │ or SSP-side          │
│ 3P needs curat.  │ Rate card only │ ❌ Not avail.  │ Same choice —        │
│                  │ (curate later) │                │ at curation          │
└──────────────────┴────────────────┴────────────────┴──────────────────────┘

🔴 Tiers me ASLI farak sirf DO cheezon ka hai:
   1. Reach forecast milta hai ya nahi
   2. Deal abhi available hai ya curate karani padegi

→ Table SIMPLER aur SAHI ho jaata hai
```

## 🔴🔴 BADA nateeja — Effective CPM ka ganit badalta hai
```
Comment #2 ka rule: "Amazon 1P data use kiya → Amazon data fee lagegi"
Aur #19: Amazon audiences 3P par bhi lag sakti hain

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 NETFLIX PORTION PAR BHI AMAZON DATA FEE LAG SAKTI HAI!               ║
║  Document (aur Note 2 ka example) maanta tha ki audience fee sirf         ║
║  AMAZON portion par lagti hai. Wo assumption GALAT hai.                   ║
╚══════════════════════════════════════════════════════════════════════════╝

Setup: Prime £6,000 @ £28.88 · Netflix £4,000 @ £32.00
       Amazon 1P data fee £1.85 · Netflix SSP uplift £2.50 (maan lo)

┌──────────────────────────────────────────────────────────────────────────┐
│ SCENARIO 1 — Koi audience nahi                                           │
│   Prime £28.88 → 207,756  ·  Netflix £32.00 → 125,000                    │
│   Total 332,756 · Data fee £0                                            │
│   ← 🟢 Sabse sasta, sabse zyada reach (#4 ka point)                       │
├──────────────────────────────────────────────────────────────────────────┤
│ SCENARIO 2 — Amazon audiences DONO par  ← #19 ka NAYA option             │
│   Prime £30.73 → 195,249  ·  Netflix £33.85 → 118,168                    │
│                                      ↑ 🔴 NAYA! Pehle possible nahi tha  │
│   Total 313,417 · fee dono par                                           │
│   ← ⚠ Netflix par capability "may be limited"                             │
├──────────────────────────────────────────────────────────────────────────┤
│ SCENARIO 3 — Amazon on Prime, SSP on Netflix                             │
│   Prime £30.73 → 195,249  ·  Netflix £34.50 → 115,942                    │
│   Total 311,191                                                          │
└──────────────────────────────────────────────────────────────────────────┘

🔴 Agent ko ab TEEN options compare karke dikhane padenge, do nahi.
```

## 🤔 Repair loop par asar
```
Sawaal: Ab jab Amazon audiences 3P par lagti hain, 3P par repair ho sakta hai?

Jawab: AUDIENCE WIDEN kar sakte ho, PAR VERIFY nahi kar sakte.

  Prime:   widen → forecast dobara → reach 22,000 → 68,000 ✅ CONFIRM
  Netflix: widen → forecast? ❌ NAHI HAI → pata nahi chalega asar hua ya nahi

→ Note 12 ka lever list BADALTA NAHI
→ PAR agent ko imaandari se batana chahiye:
  "Maine Netflix portion par bhi audience chaudi ki, par uska asar
   confirm nahi kar sakta — Netflix reach report nahi karta."
```

## ⚠ AMC audiences ka kya?
```
Document ki agli line: "AMC audiences are conditional — only when the
                        advertiser has prior campaign data"

AMC = Amazon Marketing Cloud = Amazon ka data
Agar Amazon audiences 3P par lagti hain, to AMC bhi?
  → Logically haan (wo bhi Amazon 1P data hai)
  → Par "may be limited" caveat lag sakta hai
  → ⚠ Poochhna hai
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Step 4 constraint (comment yahin)** | ❌ *"only apply to Amazon-owned inventory"* **hatao** · choice likho |
| 2 | **§2.3 tier table** | Audiences column: dono 3P rows me **choice** dikhao (Note 1 ka fix, ab confirm) |
| 3 | 🔴 **§2.3 tier table** | ➕ Note: Audiences column ab tiers ko differentiate **nahi** karta |
| 4 | 🔴 **§2.4 + Step 4 Effective CPM** | 3P par bhi Amazon data fee — **teen scenarios** ka comparison |
| 5 | ⚠ **Note 1 ka explanation** | *"identity nahi milti to impossible"* — **claim theek karo** |
| 6 | **Step 5 repair loop wording** | ➕ Nuance: 3P par widen kar sakte, verify nahi |
| 7 | ⚠ **AMC audiences line** | Clarify — AMC bhi 3P par lagti hai? |

## ✍️ DOCUMENT NOTE (draft)
> **📝 REVIEW NOTE 19 — Amazon audiences do apply to 3P inventory (David Moss)**
>
> The Step 4 constraint read: *"Amazon audiences **only apply to Amazon-owned inventory**. For Netflix/Disney, their own targeting applies."* Per David: **"can use amazon audiences too."**
>
> This is the **same absolute statement corrected in Review Note 1**, in its second location. Note 1 flagged that it appeared here too; David has now commented on it directly.
>
> **But this comment says more than Note 1 did, and corrects part of it.** Note 1 explained the limitation by asserting that 3P publishers do not pass viewer identity, so Amazon *cannot* apply audience segments. **That explanation over-claimed.** David's original wording was *"may be limited"*, not "is limited" — and this comment confirms Amazon audiences do work on 3P inventory. The mechanism is Amazon's, and the constraint is a matter of degree, not a hard barrier.
>
> **Corrected picture for 3P inventory — two options, and possibly both:**
>
> | | **Amazon audiences** | **SSP / publisher targeting** |
> |---|---|---|
> | Available on 3P | ✅ **Yes** | ✅ Yes |
> | Capability | ⚠ *May be* limited by deal/provider | Fuller, publisher-specific |
> | Cost | **Amazon 1P data fee applies** | Adds CPM |
> | When chosen | At the Targeting step | 🔴 Bound to the deal (Note 1) |
>
> **Consequence 1 — the tier table's Audiences column is no longer a differentiator.** What actually distinguishes the tiers is (a) whether reach can be forecast and (b) whether the deal is selectable now.
>
> **Consequence 2 — the effective-CPM model widens.** Note 2 established that the fee follows the data source. Since Amazon audiences can be applied to the 3P portion, **the Amazon 1P data fee can apply there too** — which the document (and Note 2's example) did not allow for. The agent now has three configurations to compare rather than two.
>
> **Consequence 3 — a nuance for the repair loop.** The audience can now be widened on the 3P portion as well, but the effect **cannot be verified** — 3P still reports no reach. The agent must say so. The lever list itself (Note 12) is unchanged.
>
> **⚠ To confirm:** (a) can both Amazon audiences *and* SSP targeting apply to the same 3P deal? (b) Does the same apply to **AMC audiences**?

## 💬 REPLY DRAFT
> Correcting this, and correcting myself.
>
> I'd already flagged that this same absolute phrasing appeared in two places — the tier table and this constraint — so the fix applies to both.
>
> **But my explanation for the tier table was wrong.** I'd justified the limitation by saying 3P publishers don't pass viewer identity, so Amazon *can't* apply audience segments there. Your original wording was *"may be limited"*, and this comment confirms Amazon audiences do work on 3P. So it's a matter of degree, not a barrier — I'll take that reasoning out.
>
> Two consequences worth flagging:
>
> **1. The tier table's Audiences column stops being a differentiator.** If Amazon audiences apply everywhere, what actually separates the tiers is whether reach can be forecast and whether the deal is selectable now. That makes the table simpler and more accurate.
>
> **2. The effective-CPM model widens.** Per your earlier comment the fee follows the data source — so if Amazon audiences apply to the Netflix portion, **the Amazon 1P fee applies there too.** My worked example only charged it on the Amazon portion. The agent now has three configurations to compare, not two: no audience anywhere, Amazon audiences on both portions, or Amazon on Prime and SSP targeting on Netflix.
>
> One nuance for the repair loop: the audience can now be widened on the 3P portion as well, but the effect can't be verified since 3P reports no reach. The agent will say so rather than imply it helped.
>
> **Two things to confirm:** can Amazon audiences *and* SSP targeting both apply to the same 3P deal, or is it one or the other? And does the same hold for **AMC audiences** — the next constraint line calls them conditional.

## 🏷️ Nichod
> **David keh raha hai:** *"Tumne likha Amazon audiences SIRF Amazon inventory par lagti hain — galat. Wo Netflix/Disney par bhi lag sakti hain."*

**Severity: 🔴 HIGH** — absolute statement galat (doosri jagah) · tier table ka column apna matlab kho deta hai · effective CPM ka ganit badalta hai · aur Note 1 ka technical explanation over-claimed tha.

---
---

# 🗨️ COMMENT #20 — "bundles.narrow/balanced/broad: not currently supported"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 4: Audiences` → ⚠ **Open question** |
| **Highlighted** | **`bundles.narrow/balanced/broad`** |
| **Poori line** | *"⚠ Open question: the suggest endpoint's response shape. v1.1.0 assumed it returns `bundles.narrow/balanced/broad`. The real endpoint may return a flat list that we group ourselves. Confirm against the real API."* |

## 💬 David ne exactly kya likha
> *"**not currently supported**"*

## 🎉 DOOSRA OPEN QUESTION RESOLVE HO GAYA
```
╔══════════════════════════════════════════════════════════════════════════╗
║  Document ne KHUD ye sawaal poochha tha — David ne JAWAB de diya.         ║
║                                                                          ║
║  Sawaal: "Kya suggest endpoint bundles.narrow/balanced/broad deta hai?"   ║
║  Jawab:  "NOT CURRENTLY SUPPORTED" — nahi deta.                           ║
║                                                                          ║
║  ✅ RESOLVED — Open Question #2                                           ║
║     (Pehla tha OQ-1, ASIN timing, #16+#17 se)                            ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 💡 Ye ek JEET bhi hai
```
Tumne v2.0 me ye ASSUME karke aage nahi badha — ⚠ flag kiya:
  "v1.1.0 assumed it returns bundles… The real endpoint MAY return a
   flat list… Confirm against the real API."

Aur wahi hua — assumption GALAT thi.

🔴 Agar tumne flag na kiya hota:
   → Schema `bundles` shape ke hisaab se ban jaati
   → Wajahat code likh deta
   → Build time par API se kuch aur aata
   → Poora audience module dobara likhna padta

✅ Tumne flag kiya, to code likhne se PEHLE pata chal gaya.

💡 Reply me ye likhna — "flag karo, assume mat karo" ki practice validate
   hoti hai. David ko dikhega ki ⚠ markers kaam ke hain.
```

## 🔴 "Not currently supported" ka exact matlab
```
"currently" shabd important hai:
  → "abhi nahi" (not "kabhi nahi")
  → Aage support ho sakta hai
  → To hamara solution ek WORKAROUND hai, permanent design nahi

❌ Document ka assumption:
POST /api/audience-sets/suggest/
← { "bundles": { "narrow": [1 seg], "balanced": [2 seg], "broad": [3 seg] } }
  ↑ API ne PEHLE SE grouping kar di

✅ Reality (bundles support nahi hai):
POST /api/audience-sets/suggest/
← { "suggestions": [        ← shayad aisa (⚠ exact shape CONFIRM karna hai)
      {"id": "aud_101", "name": "…", "vcpm": "1.85", "score": 0.94},
      {"id": "aud_102", "name": "…", "vcpm": "1.63", "score": 0.91},
      … aur bhi … ] }
  ↑ FLAT list. Grouping HUM karenge.
```

## 🔴 Sabse bada nateeja — 3 profiles ek AGENT-SIDE construct hain
```
╔══════════════════════════════════════════════════════════════════════════╗
║  DOCUMENT MAANTA THA: Narrow/Balanced/Wide ek API FEATURE hai              ║
║  REALITY: Narrow/Balanced/Wide ek AGENT-SIDE PRESENTATION hai              ║
║                                                                          ║
║  → API sirf ek flat list deta hai (relevance score ke saath)              ║
║  → Agent us list se TEEN options BANATA hai                               ║
║  → Ye agent ki logic hai, VOW backend ki nahi                             ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Teen comments milkar 3 profiles ka matlab POORA badal dete hain
```
┌──────────────┬──────────────────────────────┬────────────────────────────┐
│ Comment      │ Pehle kya tha                │ Ab kya hai                 │
├──────────────┼──────────────────────────────┼────────────────────────────┤
│ #2           │ Profiles cost me alag hain   │ ❌ Cost SAME hai (same     │
│              │ (Narrow mehngi, Wide sasti)  │    data source par)        │
│ #4           │ Ek profile chunna MANDATORY  │ ❌ OPTIONAL hai            │
│ #20          │ API profiles DETA hai        │ ❌ AGENT banata hai        │
└──────────────┴──────────────────────────────┴────────────────────────────┘

🔴 3 profiles ab ye hain:
   • Ek AGENT-SIDE presentation device (API feature nahi)
   • Sirf REACH aur PRECISION me alag (COST me nahi)
   • Aur OPT-IN (mandatory nahi)

→ Document ke current description se BAHUT alag
```

## 🔧 Grouping logic — ab HAMARA kaam hai (document me nahi hai)
```
API se flat list aayi:
  aud_101  Higher Education Seekers        score 0.94   reach   450,000
  aud_102  E-Learning & Tech Enthusiasts   score 0.91   reach 1,200,000
  aud_103  General Career Advancement      score 0.78   reach 3,500,000
  aud_104  Adult Learners 25-45            score 0.71   reach 2,100,000
  … 10 more …

🔴 TEEN DESIGN SAWAAL jinka jawab document me nahi hai:

1️⃣ Grouping ka BASIS kya hai?
   A: relevance score se (top 1 / top 2 / top 3)
   B: cumulative reach target se (~500K / ~1.5M / ~5M)
   C: data source se (Amazon-only / mixed)
   💡 Suggestion: CUMULATIVE REACH — kyunki reach hi asli farak hai
      (#2 ne cost ka farak khatam kar diya)

2️⃣ NESTED hain ya INDEPENDENT?
   Document ka example NESTED tha:
     narrow=[101] · balanced=[101,102] · broad=[101,102,103]
   💡 Suggestion: NESTED rakho — trader ko samajh aata hai ki
      "Balanced me Narrow bhi shamil hai"

3️⃣ Har profile me KITNE segments?
   Fixed (1/2/3)? Ya reach target tak jitne lagein?
   💡 Suggestion: REACH TARGET — segments ki reach har brief me alag hogi

⚠ Ye teen faisle document me LIKHNE padenge — ab ye agent ki responsibility hai.
```

## 🔴 Ek NAYA BLOCKING sawaal
```
David ne bataya ki bundles shape support NAHI hai.
Par NAHI bataya ki ASLI shape kya hai!

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 AB YE SABSE BLOCKING SAWAAL HAI:                                      ║
║     "To suggest endpoint ASAL ME kya return karta hai?"                   ║
║                                                                          ║
║  Iske bina:                                                              ║
║    ❌ Grouping logic nahi likh sakte (kis field par group karein?)        ║
║    ❌ Effective CPM nahi calculate kar sakte (#2 ka sawaal bhi yahi hai)  ║
║    ❌ Schema final nahi kar sakte                                         ║
║    ❌ Wajahat/Vishal kaam shuru nahi kar sakte                            ║
║                                                                          ║
║  → Ek ASLI RESPONSE SAMPLE chahiye. Ek asli API call ka output.           ║
║  → Ye EK artefact #2 aur #20 dono ke sawaal solve kar dega                ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Step 4 ⚠ Open question** | ✅ **RESOLVED mark karo** |
| 2 | 🔴 **§4.2 API example** | ❌ `bundles.narrow/balanced/broad` wala **poora example galat hai** — hatao ya "INCORRECT" mark karo |
| 3 | 🔴 ➕ **Naya sub-section** | **"Bundle construction (agent-side)"** — grouping logic define karo |
| 4 | 🔴 **§2.4** | ➕ Note: 3 profiles ek **agent-side construct** hain, API feature nahi |
| 5 | **Step 4 field matrix** | "Audience options \| 3 profiles" → Source: **🤖 GENERATED (agent-side grouping)** |
| 6 | **`bundles.broad` vs `WIDE`** | ✅ Ye inconsistency ab **khatam** — koi `bundles` hi nahi hai! |
| 7 | 🔴 ⚠ **Naya BLOCKING question** | Suggest endpoint ka **asli response shape** — sample chahiye |
| 8 | **§8 Summary** | ➕ Entry: bundles assumption galat nikli |

## ✍️ DOCUMENT NOTE (draft)
> **📝 REVIEW NOTE 20 — ✅ RESOLVED: the `bundles` response shape does not exist**
>
> v2.0 raised this as an open question: *"the suggest endpoint's response shape. v1.1.0 assumed it returns `bundles.narrow/balanced/broad`. The real endpoint may return a flat list that we group ourselves."* David's answer: **"not currently supported."**
>
> The assumption carried from v1.1.0 was wrong. **The API does not return pre-grouped bundles.**
>
> **The significant consequence: the three profiles are an agent-side construct, not an API feature.** Narrow / Balanced / Wide are built by the agent from whatever the endpoint returns — they are a presentation device, and the grouping logic is our responsibility.
>
> Combined with two earlier corrections, what the three profiles *are* has changed substantially:
>
> | | v2.0 said | After review |
> |---|---|---|
> | Cost | Narrow costs more, Wide less | **Identical** on the same data source (Note 2) |
> | Requirement | One must be chosen | **Optional** (Note 4) |
> | Origin | Returned by the API | **Constructed by the agent** (this note) |
>
> So the profiles differ on **reach and precision only**, they are **opt-in**, and they are **ours to build**.
>
> **Grouping logic now needs specifying:**
>
> | Decision | Options | Recommendation |
> |---|---|---|
> | Grouping basis | Relevance score · cumulative reach · data source | **Cumulative reach** — the only real differentiator now |
> | Nested or independent | `balanced ⊇ narrow`, or separate sets | **Nested**, as v2.0's example showed — easier to explain |
> | Segments per profile | Fixed 1/2/3 · or as many as needed to hit a reach target | **Reach target** — segment sizes vary by brief |
>
> **Also resolved by this:** the `bundles.broad` vs `WIDE` naming inconsistency disappears — there is no `bundles` object to disagree with.
>
> > ### 🔴 ⚠ NEW BLOCKING QUESTION — what does the endpoint actually return?
> >
> > This comment closes one question and opens a more urgent one. Knowing the `bundles` shape is wrong does not tell us the right shape, and **three things are blocked until we have it**: the grouping logic, the effective-CPM calculation (Note 2's open question about per-segment `vcpm`), and finalising the schema.
> >
> > **The ask is a single real response sample from `POST /api/audience-sets/suggest/`.** That one artefact answers this and Note 2's question together.

## 💬 REPLY DRAFT
> Thanks — that closes the question, and it's the reason I flagged it rather than building on the assumption.
>
> The `bundles` shape came from v1.1.0 and was never verified. **The important consequence: Narrow / Balanced / Wide are an agent-side construct, not an API feature.** We build them from whatever the endpoint returns, and the grouping logic is ours to define.
>
> Put together with your two earlier comments, what the profiles actually are has changed a lot — they cost the same on the same data source, they're optional, and now they're ours to construct. So they differ on **reach and precision only**.
>
> I'll add a *"Bundle construction"* section covering the three decisions the document never had to make before: group on cumulative reach (reach being the only real differentiator now), keep them nested as the original example showed, and size each profile to a reach target rather than a fixed segment count. Push back if you'd do it differently.
>
> This also cleans up a smaller inconsistency — the `bundles.broad` vs `WIDE` mismatch I'd flagged in §2.4 disappears, since there's no `bundles` object.
>
> **One ask, and it's now the blocking one:** knowing `bundles` is wrong doesn't tell me the right shape. **Could I get one real response sample from `POST /api/audience-sets/suggest/`?** That single artefact unblocks the grouping logic, the effective-CPM calculation (your fee comment raised the same question about the per-segment `vcpm`), and finalising the schema.

## 🏷️ Nichod
> **David keh raha hai:** *"Jo `bundles.narrow/balanced/broad` structure tumne maana tha — wo API me nahi hai."*

**Severity: 🔴 HIGH** — API assumption galat nikli · 3 profiles ek naya agent-side feature ban gaye · §4.2 ka ek poora example galat · naya BLOCKING sawaal khula.
**✅ Par ye ek jeet bhi hai** — assume nahi kiya, flag kiya, aur code likhne se pehle pata chal gaya.

---
---

# 🗨️ COMMENT #21 — "Location: defaults to market country"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 5: Targeting` → field matrix |
| **Row** | **Location** |
| **Highlighted** | **"Optional"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"**defaults to market country**"*

## 🎯 Ye Comment #5 ka FIELD-LEVEL confirmation hai
```
Comment #5 me David ne kaha tha:
  "you are shown the DEFAULT TARGETING applied / suggested like
   COUNTRY TARGETING and Connected TV (CTV) device only"
                        ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

Comment #21 wahi baat, us khaas field par:
  "Location defaults to market country"

→ #5 = principle · #21 = us principle ka concrete application

✅ Aur ye SOURCE column ki zaroorat ko 5vi baar confirm karta hai
   (#7, #9, #11, #13, ab #21)
```

## ❌ Document abhi vs ✅ Reality
```
Document:
  Location | Multi-select | Optional
  → "khaali rahegi jab tak trader na bhare"

Reality:
  Location | list[str] | Optional | Source: ⚙️ DERIVED — market country se
  → Pehle se bhari hui aati hai (GB)
  → Trader chahe to NARROW kare (London, ya postcodes)

→ Phir wahi pattern jo #13 (frequency cap) me tha:
  "Optional" technically sahi, par field KABHI KHAALI NAHI rehti
```

## 🔴 Confusion clear karo — `markets` vs `location`
```
╔══════════════════════════════════════════════════════════════════════════╗
║  DONO me "GB" hota hai — par DO ALAG kaam karte hain                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  markets = ["GB"]           (Step 1)                                     ║
║    → BUYING SCOPE: "kaunse market ka inventory kharidna hai?"             ║
║    → Isse tay: kaunse deals, kaunsa rate card, kaunsi audiences,         ║
║      kaunsi currency                                                     ║
║                                                                          ║
║  location = ["GB"]          (Targeting step — DEFAULT)                   ║
║    → DELIVERY FILTER: "ad kahan dikhna chahiye?"                         ║
║    → Isse tay: geo targeting                                             ║
║                                                                          ║
║  → Default me DONO same · PAR diverge ho sakte hain!                     ║
╚══════════════════════════════════════════════════════════════════════════╝

Real example jahan alag hote hain:
  markets  = ["GB"]                      ← GB ka inventory kharido
  location = ["London", "Manchester"]    ← par sirf in do cities me dikhao
```

## 🔴 Location ek HIERARCHY hai — default sabse upar
```
Country      GB                        ← 🟢 DEFAULT (markets se)
   ↓ narrow karo
Region       England, Scotland
   ↓ narrow karo
City         London, Manchester
   ↓ narrow karo
Postcode     SW1, SW3, W1, W8          ← David ka example (#5 se)

→ Agent default me sabse UPAR wala level lagata hai
→ Trader chahe to neeche jaa sakta hai
→ Neeche jaane se reach KAM hoti hai (agent ko batana chahiye)

⚠ Aur wahi sawaal phir se: kya locations API POSTCODES deta hai?
  (#5 me bhi khula tha, ab bhi khula hai)
```

## ✅ Poora Targeting step — sab defaults ke saath
`#4`, `#5`, `#19`, `#20`, `#21` milkar Targeting step ka poora default set:
```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  TARGETING STEP — DEFAULTS AND SOURCES                                                ║
╠═══════════════════════════┬──────────────────┬─────────────┬─────────────────────────╣
║ Targeting type            │ Default applied  │ Requirement │ Source                  ║
╠═══════════════════════════┼──────────────────┼─────────────┼─────────────────────────╣
║ Location                  │ ✅ Market country │ Optional    │ ⚙️ DERIVED from markets ║
║                           │    (GB)          │             │    (#21)                ║
║ Device type               │ ✅ Connected TV   │ Optional    │ 🔒 FIXED — CTV (#5)     ║
║                           │    only          │             │                         ║
║ Audience segments         │ ✅ None           │ Optional    │ 🤖 Agent suggests 3     ║
║                           │                  │             │    (#4, #20)            ║
║                           │                  │             │    ⚠ 3P par bhi (#19)   ║
║ Content exclusions        │ 🟡 Advertiser     │ Optional    │ 🏢 ADVERTISER default?  ║
║                           │    brand safety? │             │    (⚠ confirm — #13)    ║
║ Instream position         │ ❌ None           │ Optional    │ 💬 ASKED                ║
║ Mobile environment        │ ❌ None           │ Optional    │ 💬 ASKED                ║
║ ➕ Targeting source (3P)   │ 🟡 Amazon?        │ Optional    │ 💬 ASKED (#1, #19)      ║
╠═══════════════════════════┴══════════════════┴═════════════┴═════════════════════════╣
║  🔴 Do defaults PEHLE SE lagte hain (location + device)                               ║
║  🔴 Trader ka kaam: "theek hai" bolna, ya refine karna                                ║
║  🔴 Ek bhi field ASKED-and-Required nahi hai                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Targeting step — Location** | Requirement: **Optional** ✅ · Source: **⚙️ DERIVED — market country** |
| 2 | 🔴 ➕ **Naya note** | `markets` vs `location` ka farak — buying scope vs delivery filter |
| 3 | ➕ **Location hierarchy** | Country → region → city → postcode · default sabse upar |
| 4 | 🔴 **Targeting step — default table** | Upar wala poora table document me daalo |
| 5 | **Content exclusions** | ⚠ Ye bhi advertiser default ho sakta hai (brand safety) — confirm |
| 6 | **Agent behaviour** | Location narrow karne par reach kam hoti hai — batao |
| 7 | ⚠ **Postcode support** | locations API postcodes deta hai? (#5 se khula) |

## ✍️ DOCUMENT NOTE (draft)
> **📝 REVIEW NOTE 21 — Location defaults to the market country**
>
> `Location` is marked **Optional**, implying it is empty unless the trader fills it. Per David it **defaults to the market country.** Requirement stays Optional; **Source becomes ⚙️ DERIVED from `markets`.**
>
> This is the field-level confirmation of Review Note 5, where David described the default targeting as *"country targeting and Connected TV (CTV) device only."* It is also the fifth field whose Requirement was right and Source was missing.
>
> **A distinction worth stating, because the document never has:** `markets` and `location` can both hold `"GB"` but do different jobs.
>
> | | `markets` (Basics) | `location` (Targeting) |
> |---|---|---|
> | What it is | **Buying scope** — whose inventory, rate card, audiences and currency | **Delivery filter** — where the ad may be shown |
> | Default relationship | — | Defaults to the same country |
> | Can they diverge? | — | ✅ Yes: buy GB inventory, deliver only to London |
>
> **Location is a hierarchy**, and the default sits at the top of it: Country → Region → City → Postcode. Narrowing reduces available inventory, so the agent should state the effect when the trader refines downward.
>
> **The Targeting step's full default set** *(from Notes 4, 5, 19, 20, 21)* — two defaults apply automatically; nothing is asked-and-required. The trader accepts or refines.
>
> **⚠ Still to confirm:** does `GET /api/strategies/locations/{market}/` support **postcodes**, or only cities and regions? Raised in Note 5, still open — and David's own example depends on it.

## 💬 REPLY DRAFT
> Will do — Optional stays, but the Source becomes **derived from the market country.** This is the fifth field where the requirement was right and the source was missing, which is what the new Source column is for.
>
> It also lets me state something the document never has: **`markets` and `location` both hold "GB" but do different jobs.** `markets` is the buying scope — whose inventory, rate card, audiences and currency. `location` is the delivery filter. They coincide by default but can diverge: buy GB inventory, deliver only to London. I'll write that down, since it reads like duplication otherwise.
>
> Location is a hierarchy — country → region → city → postcode — with the default at the top. Narrowing reduces available inventory, so the agent will state the effect when the trader goes down a level.
>
> With this plus your targeting comment, the Targeting step now has a complete default set: **country and Connected TV applied automatically, no audience, everything else empty and optional.** Nothing is asked-and-required.
>
> **Still open from your targeting comment:** does `GET /api/strategies/locations/{market}/` support **postcodes**, or only cities and regions? Your postcode example depends on it. And should **content exclusions** default from the advertiser's brand-safety rules, the way frequency cap does?

## 🏷️ Nichod
> **David keh raha hai:** *"Location khaali nahi rehti — wo market ke country par default ho jaati hai."*

**Severity: 🟡 MEDIUM** — chhota fix, par **#5 ke default-then-refine model ka concrete confirmation**, aur Source column ki zaroorat 5vi baar saabit.

---
---

# 🗨️ COMMENT #22 — "Some advertisers only want CTV only — set at advertiser level"

> Chhota comment, **teen bade kaam** karta hai — aur mere **Note 21 ko theek** karta hai.

## 📍 Location
| | |
|---|---|
| **Section** | `Step 5: Targeting` → field matrix |
| **Row** | **Device type** |
| **Highlighted** | **"Optional"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"Some advertisers only want **CTV only** - **set at advertiser level**"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"**Some** advertisers"* | 🔴 **"Some"** — baaki advertisers ko aur devices bhi chahiye. Sabke liye same nahi |
| *"only want **CTV only**"* | Sirf Connected TV par ad chahiye — mobile/tablet par nahi |
| *"**set at advertiser level**"* | 🏢 **Advertiser ke record** me set hota hai, campaign me nahi |

---

## 🎉 Kaam 1 — ADVERTISER DEFAULTS ka TEESRA confirmation
```
╔══════════════════════════════════════════════════════════════════════════╗
║  DAVID NE AB TEEN BAAR ADVERTISER-LEVEL VALUES CONFIRM KI HAIN:           ║
║                                                                          ║
║   #13  frequency cap        "we have a default PER ADVERTISER"      ✅    ║
║   #15  product categories   "we have a default ON THE ADVERTISER"   ✅    ║
║   #22  device type          "set AT ADVERTISER LEVEL"               ✅    ║
║                                                                          ║
║  Plus mere anumaan (abhi confirm nahi):                                  ║
║   #16  selling location     (advertiser ka guṇ hai)                 🟡    ║
║   #9   primary currency     (account default)                       🟡    ║
║   content exclusions        (brand safety — ab ZYADA likely)         🟡    ║
║                                                                          ║
║  🔴 TEEN EXPLICIT confirmations ke baad "advertiser defaults" ek          ║
║     UNDENIABLE missing concept hai — suggestion nahi, REQUIREMENT hai.     ║
╚══════════════════════════════════════════════════════════════════════════╝

Aur document me ABHI BHI: koi AdvertiserDefaultsSchema nahi · koi endpoint
nahi · koi state field nahi · "advertiser settings" ka EK ZIKR BHI nahi.
```

---

## 🔴 Kaam 2 — Mera Note 21 GALAT tha
```
❌ NOTE 21 ME MAINE LIKHA THA:
   Device type | ✅ Connected TV only | Optional | 🔒 FIXED — CTV module (#5)
                                                    ↑
                     "FIXED" — socha ye ek CONSTANT hai
                     (CTV module hai to device Connected TV hoga)

✅ REALITY (#22):
   Device type | 🏢 Advertiser ka setting | Optional | 🏢 ADVERTISER
                                                        ↑
                     Advertiser ke hisaab se BADALTA hai
```

### Kyun ye farak matter karta hai?
```
🔒 FIXED              = badal hi nahi sakte, constant hai
🏢 ADVERTISER default = pehle se bhara hua, PAR override ho sakta hai

David ne kaha "SOME advertisers only want CTV only"
   ↑
"SOME" = baaki advertisers ko mobile/tablet bhi chahiye

  Advertiser A (luxury brand):  device_types = ["Connected TV"]
  Advertiser B (app company):   device_types = ["Connected TV","Mobile","Tablet"]

→ Default ADVERTISER ke hisaab se badalta hai → CONSTANT nahi ho sakta
```

**Reply me saaf maanna hai — ye doosra self-correction hai (pehla #19 me).**

---

## 🔴🔴 Kaam 3 (SABSE BADA) — "CTV" ke DO matlab hain, document ne mila diye
```
╔══════════════════════════════════════════════════════════════════════════╗
║  "CTV" — FORMAT hai ya DEVICE hai?                                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  FORMAT ke roop me:   streaming_tv                                       ║
║    → CONTENT ka kism: streaming video (Prime Video, Netflix ka content)   ║
║    → Step 1 me tay · #14 ke hisaab se HAMESHA streaming_tv                ║
║                                                                          ║
║  DEVICE ke roop me:   Connected TV                                       ║
║    → SCREEN jispar ad dikhta hai                                         ║
║    → Targeting step me tay · advertiser ke hisaab se badalta hai          ║
║                                                                          ║
║  🔴 YE DO ALAG CHEEZEIN HAIN!                                            ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Kyun? Streaming content MOBILE par bhi chalta hai
```
streaming_tv / prime_video ka content in devices par chal sakta hai:

  📺 Connected TV     Smart TV · Fire Stick · Roku · Apple TV
                      ← YE "CTV" hai asli maane me
  📱 Mobile phone     Prime Video app phone par · Netflix app phone par
                      ← YE BHI streaming_tv inventory hai! Par CTV nahi
  📱 Tablet           iPad par Prime Video
  💻 Desktop          Browser me Netflix

🔴 formats = ["streaming_tv"] ka matlab NAHI hai ki device = Connected TV.
   Streaming TV inventory kharid sakte ho aur wo PHONE par deliver ho.
   → Device filter ZAROORI hai aur redundant NAHI hai
```

### 🔴 PROOF document ke ANDAR hi hai!
```
Document ke Step 5 me ek field hai:
  Mobile environment | Select | Optional
       ↑  Values: "in-app" ya "mobile web"

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 AGAR "CTV" KA MATLAB HOTA "SIRF CONNECTED TV DEVICE" —                ║
║     TO "MOBILE ENVIRONMENT" FIELD KA MATLAB HI KYA HOTA?!                 ║
║                                                                          ║
║  Mobile environment field ka EXIST karna hi saabit karta hai ki           ║
║  MOBILE DELIVERY POSSIBLE HAI.                                           ║
║                                                                          ║
║  → Document ne khud ye field rakhi, par format-vs-device ka farak         ║
║    kahin explain nahi kiya                                               ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Ye ek BAHUT STRONG internal proof hai — reply me zaroor likhna.
```

---

## 🤔 Advertiser CTV-only kyun chahega? (business wajah)
| Wajah | Matlab |
|---|---|
| **Brand positioning** | Luxury brand bada screen chahta hai — chhote phone par nahi |
| **Creative quality** | 4K TV ad TV par shandar, phone par bekaar |
| **Attention / viewability** | CTV me completion rate zyada · mobile video mostly muted/skipped |
| **Measurement consistency** | Devices mix karne se reporting gadbad |
| **Client contract** | Media plan me likha hai "CTV" — to CTV hi dena hai |

---

## 🔴 Teen consequences

### Consequence 1 — Reach par bada asar
```
Prime Video ka bahut viewing MOBILE par hota hai.
CTV-only se available inventory KAAFI kam:

  device_types = ["Connected TV","Mobile","Tablet"]  → poora inventory
  device_types = ["Connected TV"] only               → shayad 50-60% hi

→ Reach forecast KAM aayega → agent ko trader ko BATANA chahiye
```

### Consequence 2 — CPM par asar
```
Connected TV inventory mobile se MEHNGI hoti hai (premium screen)
→ CTV-only = zyada CPM = kam impressions
→ Ye ek TRADE-OFF hai jo agent ko surface karna chahiye
```

### 🔴 Consequence 3 — Repair loop ka PRIMARY lever LOCK ho sakta hai
```
Note 12 ke levers, is order me:
  1. Relax other targeting — DEVICE, location, content exclusions
     ↑ MAINE ISKO PRIMARY LEVER banaya tha
  2. Extend the audience (agar hai)
  3. Exact → Similar (agar hai)
  4. Add inventory · 5. Extend dates · 6. Increase budget
  7. Imaandari se limit batao

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 AGAR DEVICE ADVERTISER-LEVEL POLICY HAI —                             ║
║     TO AGENT USE RELAX KAR HI NAHI SAKTA!                                 ║
║                                                                          ║
║  Naya worst case:                                                        ║
║    • Koi audience nahi (#4)             → levers 2, 3 gaye                ║
║    • Preferred fixed-CPM deal (#12)     → bid lever gaya                  ║
║    • Advertiser: CTV device only (#22)  → 🔴 PRIMARY lever LOCK           ║
║                                                                          ║
║  Bache: location, content exclusions, add deals, extend dates, budget     ║
║  → Repair loop AUR kamzor ho gaya                                        ║
╚══════════════════════════════════════════════════════════════════════════╝

→ Lever list me ek NAYA COLUMN chahiye: "kya ye lever lock ho sakta hai?"
```

---

## 🔴🔴 NAYA CONCEPT — "Default" vs "Constraint"
```
David ne kaha "SOME advertisers ONLY WANT CTV only"
Sawaal: kya ye ek DEFAULT hai ya ek POLICY hai?

╔══════════════════════════════════════════════════════════════════════════╗
║  🏢 ADVERTISER DEFAULT       vs      🔒 ADVERTISER CONSTRAINT             ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Pehle se bhara hua                  Pehle se bhara hua                  ║
║  Trader OVERRIDE kar sakta hai       Trader override NAHI kar sakta      ║
║  Repair loop RELAX kar sakta hai     Repair loop CHHOO NAHI SAKTA        ║
║                                                                          ║
║  Example: frequency cap (#13)         Example: device policy (#22)?      ║
║    "3 default hai, badal lo"           "CTV only — brand policy hai"     ║
╚══════════════════════════════════════════════════════════════════════════╝
```

**Schema me express karna padega:**
```python
# ❌ Abhi (Note 13 se) — sirf values, koi lock nahi
class AdvertiserDefaultsSchema(BaseModel):
    frequency_cap: Optional[int] = None
    device_types: list[str] = Field(default_factory=list)
    # ↑ Default hai ya policy? Pata nahi chalta

# ✅ Behtar — har setting ke saath uska lock status
class AdvertiserSetting(BaseModel):
    """➕ NEW — an advertiser-level value plus whether it can be overridden"""
    value: Any
    is_locked: bool = Field(False,
        description="True = brand policy; trader cannot override and "
                    "the repair loop cannot relax it")
    reason: Optional[str] = Field(None,
        description="Shown to the trader when locked, e.g. 'brand policy: CTV only'")

class AdvertiserDefaultsSchema(BaseModel):
    frequency_cap: Optional[AdvertiserSetting] = None
    device_types: Optional[AdvertiserSetting] = None            # #22
    product_categories: Optional[AdvertiserSetting] = None      # #15
    product_location: Optional[AdvertiserSetting] = None        # #16
    primary_currency: Optional[AdvertiserSetting] = None        # #9
    content_category_exclusions: Optional[AdvertiserSetting] = None
    approval_threshold: Optional[AdvertiserSetting] = None
```

> ⚠ **David se poochhna:** device setting ek **default** hai (override ho sakta) ya ek **constraint** (locked)?

---

## ⚠ Chhoti dependency jo document me nahi hai
```
Step 5 ke do fields ka rishta:
  device_types        = ["Connected TV"]      ← Mobile shamil NAHI
  mobile_environment  = "in-app"              ← 🔴 Iska matlab kya?

→ Agar device_types me "Mobile" NAHI hai, mobile_environment BEKAAR hai
→ Ye ek CONDITIONAL field hai — par document me nahi likha

✅ Rule: mobile_environment sirf tab applicable jab "Mobile" ∈ device_types
```

---

## ✅ Targeting step ka CORRECTED default table
```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  TARGETING STEP — DEFAULTS AND SOURCES (corrected by #22)                              ║
╠═══════════════════════════┬──────────────────┬─────────────┬─────────────────────────╣
║ Targeting type            │ Default applied  │ Requirement │ Source                  ║
╠═══════════════════════════┼──────────────────┼─────────────┼─────────────────────────╣
║ Location                  │ ✅ Market country │ Optional    │ ⚙️ DERIVED (#21)        ║
║ Device type               │ ✅ Advertiser ka  │ Optional    │ 🏢 ADVERTISER (#22)     ║
║                           │    setting        │             │  ← 🔴 CORRECTED         ║
║                           │    (often CTV     │             │  fallback: Connected TV ║
║                           │    only)          │             │  ⚠ LOCKED ho sakta hai  ║
║ Audience segments         │ ✅ None           │ Optional    │ 🤖 Agent suggests 3     ║
║                           │                  │             │  (#4,#20) ⚠ 3P bhi (#19)║
║ Content exclusions        │ 🟡 Advertiser     │ Optional    │ 🏢 ADVERTISER default?  ║
║                           │    brand safety? │             │  ⚠ #22 ke baad ZYADA    ║
║                           │                  │             │    likely               ║
║ Instream position         │ ❌ None           │ Optional    │ 💬 ASKED                ║
║ Mobile environment        │ ❌ None           │ CONDITIONAL │ 💬 ASKED — sirf jab     ║
║                           │                  │  ← 🔴 NAYA  │  Mobile ∈ device_types  ║
║ ➕ Targeting source (3P)   │ 🟡 Amazon?        │ Optional    │ 💬 ASKED (#1,#19)       ║
╠═══════════════════════════┴══════════════════┴═════════════┴═════════════════════════╣
║  🔴 Do defaults advertiser se (device ✅ · content exclusions 🟡)                       ║
║  🔴 Ek default derive hota hai (location)                                             ║
║  🔴 Aur kuch defaults LOCKED ho sakte hain — repair loop chhoo nahi sakta              ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

---

## 🤖 Agent ka naya behaviour
```
Agent: "Inventory set. Targeting ke defaults:

        ┌──────────────────────────────────────────────────────────────┐
        │  TARGETING (applied)                                         │
        │  ✓ Country    United Kingdom (GB)      — market se derive    │
        │  🔒 Device    Connected TV only         — BrightPath ki       │
        │                                           brand policy       │
        │  ✓ Audience   None                                           │
        │  Effective CPM £28.88 · Impressions 346,260                  │
        └──────────────────────────────────────────────────────────────┘

        ⚠ BrightPath ke account me 'Connected TV only' set hai. Ad phone
          ya tablet par nahi chalega, sirf TV screen par. Isse available
          inventory kam hota hai (aur CPM thoda zyada), par brand ko
          bada screen milta hai.

          Ye advertiser-level policy hai — main isko is campaign ke liye
          badal nahi sakta. Badalna hai to account settings me jaana padega.

        Kuch aur refine karna hai? Ya 'theek hai' bol do."

──────────────────────────────────────────────────────────────────────
Repair loop ke waqt:

Agent: "Reach kam nikla (68,000). Maine ye try kiya:
          ✅ Location poore UK par ki (pehle London tak thi)
          ✅ Content exclusions kam kiye
          🔒 Device relax NAHI kar saka — 'Connected TV only' advertiser
             policy hai, main chhoo nahi sakta

        Reach ab 94,000. Aur badhana hai to:
          • Budget badhao, ya
          • Aur deals add karo, ya
          • Account settings me device policy dhili karwao"
```

---

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Targeting step — Device type** | Requirement: **Optional** ✅ · Source: **🏢 ADVERTISER** (fallback: Connected TV only) |
| 2 | 🔴 **Note 21 ka default table** | Device type: ~~🔒 FIXED~~ → **🏢 ADVERTISER** — mera claim theek karo |
| 3 | 🔴🔴 ➕ **Naya note** | **"CTV as a format vs CTV as a device"** · `mobile_environment` field iska proof hai |
| 4 | 🔴🔴 **`AdvertiserDefaultsSchema`** | ➕ `device_types` · **aur `AdvertiserSetting` wrapper** (`value` + `is_locked` + `reason`) |
| 5 | 🔴 **Note 12 repair loop levers** | ➕ Naya column: **"kya ye lever lock ho sakta hai?"** |
| 6 | **Step 5 — Mobile environment** | Optional → **Conditional** (sirf jab Mobile ∈ device_types) |
| 7 | **Step 6 (forecast)** | ➕ Note: CTV-only se inventory aur reach kam · CPM zyada |
| 8 | **Content exclusions** | 🟡 Ab **zyada likely** hai ki ye bhi advertiser default hai — confirm |
| 9 | **Agent behaviour** | Locked settings 🔒 dikhao + wajah batao · repair loop me batao kya chhoo nahi sake |
| 10 | ⚠ **Confirm** | Device setting **default** hai ya **constraint** (locked)? |

---

## ✍️ DOCUMENT NOTE (draft)

> **📝 REVIEW NOTE 22 — Device type comes from the advertiser, and may be a policy rather than a default**
>
> **David's comment:** *"Some advertisers only want CTV only - set at advertiser level"*
>
> `Device type` is marked **Optional**, implying it is empty unless the trader fills it. It comes from the **advertiser record**, and for some advertisers it restricts delivery to Connected TV only.
>
> ### This is the third confirmation of advertiser-level defaults
>
> | Note | Field | David's wording |
> |---|---|---|
> | 13 | Frequency cap | *"we have a default per advertiser"* |
> | 15 | Product categories | *"we have a default on the advertiser"* |
> | **22** | **Device type** | *"set at advertiser level"* |
>
> Three explicit confirmations make `AdvertiserDefaultsSchema` a firm requirement, not a suggestion.
>
> ### ⚠ CORRECTION to Review Note 21
>
> Note 21's default table listed **Device type** as **🔒 FIXED — CTV module**, on the assumption that a CTV module implies Connected TV delivery. **That was wrong.** David's *"**some** advertisers"* means it varies by advertiser — so the source is **🏢 ADVERTISER**, not a constant.
>
> ### 🔴 The underlying conceptual fix: "CTV" as a format is not "CTV" as a device
>
> | | **Format** | **Device** |
> |---|---|---|
> | Value | `streaming_tv` | `Connected TV` |
> | What it means | The **content type** — streaming video inventory | The **screen** the ad is delivered to |
> | Decided at | Step 1 — always `streaming_tv` (Note 14) | Targeting — varies by advertiser (this note) |
>
> Streaming TV inventory can be delivered to a **Connected TV, a phone, a tablet or a desktop browser** — the Prime Video and Netflix apps run on all of them. So `formats = ["streaming_tv"]` does **not** imply Connected TV delivery, and the device filter is neither redundant nor derivable from the format.
>
> **The document already proves this to itself:** Step 5 includes a **`Mobile environment`** field (in-app vs mobile web). That field would be meaningless if delivery were restricted to Connected TV by definition. Its existence establishes that mobile delivery is possible — the format-vs-device distinction was simply never written down.
>
> ### Consequences
>
> **Reach and CPM.** A large share of Prime Video viewing is on mobile, so restricting to Connected TV materially reduces available inventory — lower reach — while Connected TV inventory is typically **more expensive** — higher CPM, fewer impressions. The agent should surface both effects, since the trader did not choose this restriction.
>
> **🔴 The repair loop's primary lever may be locked.** Note 12's lever list puts *"relax other targeting — device, location, content exclusions"* first, precisely because audiences became optional. **If device type is an advertiser policy, the agent cannot relax it.** The worst case is now:
>
> ```
> No audience selected            (Note 4)   → levers 2 and 3 unavailable
> Preferred fixed-CPM deal        (Note 12)  → the bid lever does nothing
> Advertiser policy: CTV only     (Note 22)  → 🔒 the primary lever is locked
>
> Remaining: location, content exclusions, add inventory,
>            extend dates, increase budget
> ```
>
> The lever list needs a **"can this be locked?"** column.
>
> ### 🔴 A new distinction the schema needs: default vs constraint
>
> | | 🏢 **Advertiser default** | 🔒 **Advertiser constraint** |
> |---|---|---|
> | Pre-filled | ✅ | ✅ |
> | Trader can override | ✅ Yes | ❌ No — it is brand policy |
> | Repair loop can relax it | ✅ Yes | ❌ No |
> | Example | Frequency cap (Note 13) | Device policy — *"CTV only"* |
>
> ```python
> class AdvertiserSetting(BaseModel):
>     """➕ NEW — an advertiser-level value plus whether it can be overridden"""
>     value: Any
>     is_locked: bool = Field(False,
>         description="True = brand policy; the trader cannot override and "
>                     "the repair loop cannot relax it")
>     reason: Optional[str] = Field(None,
>         description="Shown to the trader when locked, e.g. 'brand policy: CTV only'")
> ```
>
> The agent must know which values it is allowed to touch — and must tell the trader when it is not.
>
> ### A dependency the document does not state
>
> **`Mobile environment` is conditional on `Device type`.** If `Mobile` is not among the selected device types, in-app vs mobile web is meaningless. Requirement should be **Conditional**, not Optional.
>
> ### ⚠ To confirm
> 1. **Is the advertiser device setting a default (overridable) or a constraint (locked)?**
> 2. Should **content exclusions** also come from the advertiser? Brand-safety rules are normally set at brand level, and this comment makes that more likely.
> 3. What is the fallback when an advertiser has no device setting — Connected TV only, or all devices?

---

## 💬 REPLY DRAFT

> Understood — and this corrects something I'd got wrong.
>
> In my targeting default table I'd marked **Device type as fixed**, on the assumption that a CTV module implies Connected TV delivery. Your *"some advertisers"* makes clear it varies — so it's an **advertiser-level value**, not a constant.
>
> **That exposes a conflation I should have caught: "CTV" as a format isn't "CTV" as a device.** `streaming_tv` is the content type; Connected TV is the screen. Prime Video and Netflix both run on phones and tablets, so streaming inventory can be delivered to a small screen. **And the document proves this to itself** — Step 5 has a `Mobile environment` field, which would be meaningless if delivery were Connected TV by definition. I'll write the distinction down; it was never stated.
>
> Two consequences worth raising:
>
> **1. It affects reach and CPM, and the trader didn't choose it.** A lot of Prime Video viewing is mobile, so CTV-only cuts available inventory and pushes CPM up. The agent should surface both effects rather than just applying the setting silently.
>
> **2. It may lock the repair loop's primary lever.** After audiences became optional and the bid lever turned out not to work on fixed-CPM deals, *"relax other targeting — device first"* became the main lever I had left. **If device is advertiser policy, the agent can't touch it.** Worst case is now no audience, a Preferred deal, and a locked device policy — leaving only location, exclusions, more inventory, longer flight or more budget.
>
> That leads to something I want to add to the schema: **advertiser values aren't all the same kind.** A frequency cap default is overridable; a "CTV only" brand policy probably isn't. I'll wrap each advertiser setting as `{value, is_locked, reason}` so the agent knows what it may change, and can tell the trader when it can't.
>
> This is also the third advertiser-level value you've flagged — frequency cap, product categories, now device type — so I'm treating the advertiser-defaults schema and endpoint as required rather than proposed.
>
> **Three things to confirm:**
> 1. Is the device setting a **default** the trader can override, or a **locked policy**?
> 2. Should **content exclusions** come from the advertiser too? Brand-safety rules usually sit at brand level.
> 3. What's the fallback when an advertiser has no device setting — Connected TV only, or all devices?

## ❓ David se poochhne wale sawaal
| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | 🔴 Device setting **default** (overridable) hai ya **constraint** (locked)? | Repair loop ise chhoo sakta hai ya nahi — ye tay karta hai |
| 2 | Content exclusions bhi advertiser se aati hain? (brand safety) | Ab #22 ke baad zyada likely |
| 3 | Agar advertiser ka koi device setting nahi — fallback kya? | Default behaviour define karna hai |
| 4 | Aur kaunse advertiser settings LOCKED ho sakti hain? | `is_locked` kis-kis par lagega |

## 🏷️ Nichod
> **David keh raha hai:** *"Device type khaali nahi rehti — wo advertiser ke account me set hoti hai. Aur kuch advertisers sirf Connected TV chahte hain, mobile par nahi."*

**Severity: 🔴 HIGH** — kyunki:
- **Advertiser defaults ka teesra confirmation** — ab undeniable
- **Mera Note 21 galat tha** (FIXED → ADVERTISER)
- 🔴🔴 **"CTV format vs CTV device" ka conceptual fix** — document ka apna `mobile_environment` field iska proof
- 🔴 **Repair loop ka primary lever lock ho sakta hai** — loop aur kamzor
- 🔴 **Naya schema concept:** default vs constraint (`is_locked`)
- ➕ `mobile_environment` ki conditional dependency

---
---

# 🗨️ COMMENT #23 — "We simplified this — just a status change, no manager approval for now"

> 🔴 **Ye pehla comment hai jo FEATURE HATATA hai** — aur ye baaki sab se **alag kism** ka hai.

## 📍 Location
| | |
|---|---|
| **Section** | `Step 7: Plan Approval` |
| **Highlighted** | **"Plan Approval"** — poora **step ka naam** |
| **Asar** | 🔴 Poora Step 7 · state machine · do loop edges · ek open question |

## 💬 David ne exactly kya likha
> *"we **simplified this** so it's **just a status changed** to finalise the plan - **no manager approval required for now**"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"**we simplified this**"* | 🔴 "WE" — team/client ne **faisla liya hai**. Ye tumhari galti nahi |
| *"so it's **just a status changed**"* | Poora approval workflow ek **status change** ban gaya |
| *"to **finalise the plan**"* | Maksad: plan **final mark karna** — approve karana nahi |
| *"**no manager approval** required"* | Manager routing **hataya gaya** |
| *"**for now**"* | ⚠ Abhi nahi — **baad me wapas aa sakta hai** |

---

## 🎯 SABSE PEHLE — ye comment BAAKI SAB SE ALAG hai
```
╔══════════════════════════════════════════════════════════════════════════╗
║  #1 – #22  →  "ye GALAT hai" ya "ye MISSING hai"                         ║
║               (corrections aur gaps — tumhari samajh theek karna)         ║
║  #17       →  "haan ye theek hai" (agreement)                            ║
║  #23       →  🔴 "hum ne DESIGN BADAL DIYA hai"                          ║
║               (ye NEWS hai, correction nahi)                              ║
╚══════════════════════════════════════════════════════════════════════════╝

"WE simplified this" — yaani:
  • Ye faisla v2.0 LIKHNE KE BAAD liya gaya
  • Tum us meeting me nahi the
  • Document GALAT nahi tha — document PURANA ho gaya

🔴 ISLIYE REPLY KA TONE ALAG:
   ❌ "Sorry, meri galti" — kyunki galti nahi hai
   ✅ "Good to know — main isko simplify kar deta hun"
```

---

## ❌ Document abhi vs ✅ Ab kya hoga

### Document abhi (poora approval workflow)
```
Step 7: Plan Approval
Client: "approval gates the plan, before it is finalised. Not before
         launch. OPTIONALLY ROUTES TO A MANAGER."

┌─────────────────────┬────────────────┬──────────────────────────────────┐
│ Approval status     │ Enum           │ Required — PENDING → APPROVED    │
│                     │                │            or REJECTED           │
│ Approved by         │ String (user)  │ Set on approval                  │
│ Approved at         │ Timestamp      │ Set on approval                  │
│ Manager required    │ Boolean        │ Configurable (possibly budget-   │
│                     │                │ threshold-based)                 │
│ Rejection reason    │ Text           │ Required on reject               │
└─────────────────────┴────────────────┴──────────────────────────────────┘

Implementation: LangGraph interrupt(). Graph PHYSICALLY STOPS aur state
persist karti hai. Budget LOCK — "nothing launches that a person hasn't
approved."
On rejection: flow Step 4 (audiences) par wapas.
```

### Ab (simple status change)
```
Step 7: Finalise Plan          ← naam badalna chahiye

Trader plan dekhta hai → "Finalise" bolta hai → status badal jaata hai. Bas.

┌─────────────────────┬────────────────┬──────────────────────────────────┐
│ Plan status         │ Enum           │ DRAFT → FINALISED                │
│ Finalised by        │ String (user)  │ Set on finalise                  │
│ Finalised at        │ Timestamp      │ Set on finalise                  │
│ ~~Manager required~~│ —              │ ❌ REMOVED (for now)             │
│ ~~Rejection reason~~│ —              │ ❌ REMOVED — koi reject nahi     │
└─────────────────────┴────────────────┴──────────────────────────────────┘
```

---

## 🔴 Char badlav

### Badlav 1 — `Manager required` field HAT GAYA
```
Seedha. manager_required: Boolean ka koi matlab nahi jab manager approval
hi nahi hai.

✅ AUR ISSE EK OPEN QUESTION KHATAM HO GAYA:
   Document: "Manager required | Configurable (POSSIBLY budget-threshold-based)"
   Maine #13 me suggest kiya tha ki ye advertiser default ho sakta hai.
   → AB YE SAWAAL MOOT — M1 me manager approval hi nahi hai
   → "Resolved by de-scoping"
```

### Badlav 2 — `REJECTED` state aur `Rejection reason` HAT GAYE
```
Trader KHUD apna plan finalise kar raha hai —
to wo apne aap ko "reject" kaise karega?

  PENDING → APPROVED | REJECTED     (3 states — external approver)
       ↓
  DRAFT → FINALISED                  (2 states — self-service)

→ "REJECTED" ka koi matlab nahi
→ "Rejection reason" ka koi matlab nahi
→ Plan pasand nahi aaya to trader bas EDIT karta rahega, finalise nahi karega
```

### 🔴 Badlav 3 — Ek LOOP EDGE gaayab
```
Document: "On rejection: the flow returns to Step 4 (audiences)"

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 KOI REJECTION NAHI = KOI LOOP EDGE NAHI                              ║
║                                                                          ║
║  Purana:  Step 7 → [rejected] → Step 4       (gate se wapas)             ║
║  Naya:    trader ne finalise nahi kiya → wo bas targeting me refine       ║
║           karta rehta hai                                                ║
║                                                                          ║
║  → Ye "gate se rejection" nahi, "abhi finalise nahi kiya" hai              ║
║  → Graph me ek edge KAM (Wajahat ke liye direct impact)                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 🔴🔴 Badlav 4 (SABSE BADA) — `interrupt()` ki zaroorat KHATAM
```
╔══════════════════════════════════════════════════════════════════════════╗
║  interrupt() KYUN CHAHIYE THA?                                            ║
║  Kyunki MANAGER ek ALAG INSAAN hai jo conversation me NAHI hai.            ║
║                                                                          ║
║  Trader chat me hai  →  Manager dashboard par (kahin aur)                  ║
║  → Agent ko RUKNA padta hai                                              ║
║  → State DISK par save · BAHAR se signal ka intezaar                      ║
║  → Ghante ya din lag sakte hain                                          ║
║                                                                          ║
║  🔴 interrupt() ka asli maksad: EXTERNAL, ASYNC signal                    ║
╚══════════════════════════════════════════════════════════════════════════╝

AB — trader KHUD finalise kar raha hai. Wo CONVERSATION ME HI hai.
  Agent: "Plan taiyar hai. Finalise karun?"
  Trader: "Haan"
       ↑ Ye ek AAM CONVERSATION TURN hai. Koi external signal nahi.

→ interrupt() ki ZAROORAT NAHI
```

### ⚠ Zaroori nuance — state persistence phir bhi hoti hai
```
Sawaal: "Trader Monday plan banaye, Wednesday finalise kare — tab state
         save honi chahiye na?"
Jawab: HAAN — par wo interrupt() ka kaam NAHI hai.

╔══════════════════════════════════════════════════════════════════════════╗
║  CHECKPOINTER  = "session yaad rakho"           ← HAMESHA chalta hai      ║
║  interrupt()   = "bahar se signal ka intezaar"  ← sirf external gate      ║
╚══════════════════════════════════════════════════════════════════════════╝

Trader do din baad wapas aaye → CHECKPOINTER handle karta hai,
interrupt() nahi.
```

---

## 🔴 Dilchasp nateeja — M1 me ASLI interrupt sirf EK jagah bacha
```
Document me do jagah human wait tha:
  Step 7  — Plan approval              → interrupt() (manager ka intezaar)
  Step 10 — Platform creative approval → Amazon/Netflix/Disney ka review

╔══════════════════════════════════════════════════════════════════════════╗
║  #23 ke baad:                                                            ║
║  Step 7  → ❌ interrupt nahi chahiye (trader khud, conversation me)        ║
║  Step 10 → ✅ interrupt CHAHIYE (Amazon/Netflix review GENUINELY           ║
║              external + async — 48 ghante lag sakte hain)                 ║
║                                                                          ║
║  🔴 M1 me interrupt() ka asli use case sirf STEP 10 hai — Step 7 nahi.    ║
║  → interrupt() design se nahi hata — apni SAHI JAGAH par chala gaya       ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Reply me likhna — dikhega ki tumne ARCHITECTURE level par socha.
```

---

## 💡 Recommendation — mechanism hatao, SEAM rakho
```
David ne kaha "for now" — manager approval BAAD ME AA SAKTA HAI.

╔══════════════════════════════════════════════════════════════════════════╗
║  ❌ Option A: Poora approval node hata do                                 ║
║     Ab: sabse kam kaam                                                    ║
║     Baad me: poora node + edges dobara — RE-ARCHITECTURE                  ║
║                                                                          ║
║  ✅ Option B: Node RAKHO, mechanism SIMPLIFY karo                         ║
║     Ab: alag node jo sirf status change karta hai (no interrupt)          ║
║     Baad me: usi node me interrupt() + manager routing add karo            ║
║              → sirf ROUTING change, architecture change nahi               ║
║                                                                          ║
║  💡 SEAM rakho, MECHANISM hatao.                                         ║
╚══════════════════════════════════════════════════════════════════════════╝

class PlanStatusEnum(str, Enum):
    """➕ NEW — simplified for M1; manager approval deferred"""
    DRAFT = "DRAFT"
    FINALISED = "FINALISED"
    # PENDING_APPROVAL = "PENDING_APPROVAL"   # future — manager routing
    # APPROVED = "APPROVED"                    # future
    # REJECTED = "REJECTED"                    # future

⚠ ApprovalStatusEnum RAKHO — Step 10 ko chahiye (wahan asli approval hai)
```

---

## ⚠ Ek CONTROL kho gaya — document karna zaroori
```
╔══════════════════════════════════════════════════════════════════════════╗
║  DOCUMENT KI LINE THI:                                                   ║
║    "The budget is locked at this moment — NOTHING LAUNCHES THAT A         ║
║     PERSON HASN'T APPROVED."                                             ║
║                                                                          ║
║  Purana model (separation of duties):                                     ║
║    Trader plan banata  →  MANAGER approve karta                           ║
║    → Do alag log · ek independent check                                   ║
║    → Trader approval ke baad chup-chaap badal nahi sakta                   ║
║                                                                          ║
║  Naya model (self-service):                                              ║
║    Trader plan banata  →  TRADER khud finalise karta                      ║
║    → Ek hi banda · koi independent check nahi                             ║
║                                                                          ║
║  🔴 "SEPARATION OF DUTIES" wala control HAT GAYA                          ║
╚══════════════════════════════════════════════════════════════════════════╝

⚠ PAR spend ka gate PHIR BHI hai: Step 13 (Activate) trader ke explicit
  action se hota hai. "Galti se kharch" nahi hoga.
  Jo hata hai wo DOOSRE INSAAN ka check hai.

M1 ke liye theek hai (chhoti team, chhote budgets). Par jab budgets bade
honge, koi poochhega "is £50,000 ko kisne approve kiya?" — jawab hoga
"jisne banaya usi ne."

→ Isliye ye LIKHNA zaroori: ye JAAN-BOOJH KAR deferred hai, bhoola hua nahi
```

---

## 🔴 Do LOOPS ka character badla (par bache hain)
```
Loop A — Step 9 (Duration mismatch)
  Document: "This triggers RE-APPROVAL (return to Step 7 with amended plan)"
  Ab: "re-approval" → "RE-CONFIRMATION"
  Agent: "Video 30s ka hai, plan 15s ka tha. Impressions 500,000 se
          346,260 ho gaye. Plan phir se finalise karna padega — confirm?"
  → Loop BACHA (bachna chahiye — economics badla)
  → Character badla: "manager se approval" → "trader se confirm"

Loop B — Step 12 (Credit insufficient → budget kam karna)
  Wahi treatment: "re-approve" → "re-finalise"
  → Loop bacha, character badla

Loop C — Plan rejection → Step 4
  🔴 GAAYAB (Badlav 3)

Net: teen loops the → do bache, ek gaya
```

---

## ✅ Naya Step 7 — poora
```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  STEP 7: FINALISE PLAN  (was "Plan Approval")                                          ║
║  🔄 SIMPLIFIED per David's review — manager approval deferred                           ║
╠═══════════════════════════┬──────────────────┬─────────────┬─────────────────────────╣
║ Field                     │ Data type        │ Requirement │ Source                  ║
╠═══════════════════════════┼──────────────────┼─────────────┼─────────────────────────╣
║ Plan status               │ PlanStatusEnum   │ Required    │ 💬 ASKED — trader        ║
║                           │ DRAFT→FINALISED  │             │    confirms              ║
║ Finalised by              │ str (user)       │ Set on      │ 🔌 Session (the trader)  ║
║                           │                  │ finalise    │                         ║
║ Finalised at              │ timestamp        │ Set on      │ 🔌 System                ║
║                           │                  │ finalise    │                         ║
╠═══════════════════════════┴══════════════════┴═════════════┴═════════════════════════╣
║  ❌ REMOVED (for now):                                                                ║
║     Manager required   → no manager approval in M1                                    ║
║     Rejection reason   → no rejection; trader simply doesn't finalise yet              ║
║     Approval status    → replaced by the simpler plan status                           ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  🔄 NO interrupt() needed — the trader is in the conversation.                          ║
║     Session state persists via the checkpointer regardless.                            ║
║     ⚠ Keep as a DISTINCT NODE so manager routing can be added later.                   ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

## 🤖 Agent ka naya behaviour
```
Agent: "Plan taiyar hai:

        ┌──────────────────────────────────────────────────────────┐
        │  BrightPath_Awareness_GB_Aug2026                          │
        │  £10,000 · 1–30 Aug 2026 · United Kingdom                 │
        │                                                          │
        │  Prime Video   £6,000  →  195,249 imp  ·  118,000 reach   │
        │  Netflix       £4,000  →  125,000 imp  ·  reach N/A       │
        │  Total impressions: 320,249                              │
        │  ⚠ Total reach add nahi kar sakte (no cross-platform dedup)│
        └──────────────────────────────────────────────────────────┘

        Plan finalise karun? Iske baad main strategy bana dunga.
        (Abhi tak kuch kharch nahi hua — kharch sirf activate par shuru.)"

Trader: "Haan, finalise kar do"

Agent: "✅ Plan finalised — Kareem, 30 Jul 09:35. Ab strategy bana raha hun."

→ Ye ek AAM conversation turn hai. Koi "manager ka intezaar" nahi,
  koi "graph ruk gaya" nahi.
```

---

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | 🔴 **Step 7 ka naam** | "Plan Approval" → **"Finalise Plan"** |
| 2 | 🔴 **Step 7 intro** | Client quote update — *"optionally routes to a manager"* ab galat |
| 3 | 🔴 **Step 7 field matrix** | ❌ `Manager required` · ❌ `Rejection reason` · 🔄 `Approval status` → `Plan status` |
| 4 | **Field naming** | `approved_by/at` → **`finalised_by/at`** |
| 5 | 🔴 **Enums** | Naya `PlanStatusEnum` (DRAFT/FINALISED) · `ApprovalStatusEnum` **Step 10 ke liye rakho** |
| 6 | 🔴🔴 **Step 7 Implementation** | `interrupt()` **nahi chahiye** — par **node alag rakho** (seam) |
| 7 | 🔴 **"On rejection: return to Step 4"** | ❌ **Hatao** |
| 8 | 🔴 **§6 state machine line 13-14** | `⏸ PLAN APPROVAL (interrupt)` → `finalise_plan (status change)` · rejection edge hatao |
| 9 | **Step 9 duration mismatch** | "re-approval" → **"re-confirmation"** |
| 10 | **Step 12 budget reduction** | "re-approve" → "re-finalise" |
| 11 | ⚠ ➕ **Naya note** | **Separation of duties deliberately deferred** — likhna zaroori |
| 12 | ✅ **Open question** | *"Manager-approval threshold per advertiser/global/role?"* → **MOOT** |
| 13 | ⚠ **Audit trail question** | Kam critical, par `finalised_by/at` record karna hai |
| 14 | **§8 Summary** | "plan approval" → "plan finalisation (simplified)" |
| 15 | 🔴 ➕ **Naya note** | M1 me **asli interrupt sirf Step 10** hai |
| 16 | **`AdvertiserSetting.approval_threshold`** | Abhi zaroorat nahi — future ke liye commented rakho |

---

## ✍️ DOCUMENT NOTE (draft)

> **📝 REVIEW NOTE 23 — Plan approval simplified to a status change; manager routing deferred**
>
> **David's comment:** *"we simplified this so it's just a status changed to finalise the plan - no manager approval required for now"*
>
> **This is not a correction — it is a design change made after v2.0 was written.** The approval workflow described here reflects what the client confirmed at the time; the team has since simplified it. The step still exists, but it is now a **status change the trader makes**, not an approval another person grants.
>
> ### What the step becomes
>
> | | **Was** | **Now** |
> |---|---|---|
> | Step name | Plan Approval | **Finalise Plan** |
> | Who acts | Trader submits, optionally a **manager** approves | **The trader**, self-service |
> | States | `PENDING` → `APPROVED` \| `REJECTED` | `DRAFT` → `FINALISED` |
> | `Manager required` | Configurable, possibly budget-threshold-based | ❌ **Removed for now** |
> | `Rejection reason` | Required on reject | ❌ **Removed** — there is no rejection |
> | Implementation | LangGraph `interrupt()` — graph stops, awaits an external signal | **A normal conversational turn** |
> | On rejection | Return to the Targeting step | ❌ **Edge removed** |
>
> ### 🔴 `interrupt()` is no longer needed at this step
>
> `interrupt()` exists to **stop the graph and wait for a signal from outside the conversation.** That was justified when a **manager** — a different person, working from a dashboard — had to approve. With the trader finalising their own plan **from within the conversation**, the signal is just the next message.
>
> **A distinction worth keeping clear**, because the two are often conflated:
>
> | | What it does | When it applies |
> |---|---|---|
> | **Checkpointer** | Persists session state so a trader can leave and return | **Always** — independent of this change |
> | **`interrupt()`** | Stops the graph pending an **external, asynchronous** signal | Only where a genuine external gate exists |
>
> A trader returning two days later to finalise is handled by the checkpointer, not by `interrupt()`.
>
> **Consequently, the only genuine `interrupt()` in M1 is platform creative approval.** Amazon, Netflix and Disney review independently, on their own timelines, outside the conversation. That is what an interrupt is for. `interrupt()` has not left the design; it has moved to where it belongs.
>
> ### Recommendation: remove the mechanism, keep the seam
>
> David's *"for now"* implies manager approval returns later.
>
> | | Effort now | Effort when manager approval returns |
> |---|---|---|
> | Remove the step entirely | Least | Rebuild the node and its edges — a structural change |
> | **Keep a distinct node, simplify its mechanism** | Slightly more | **Add `interrupt()` and routing to an existing node** — a routing change |
>
> The second is recommended. Keeping `finalise_plan` as its own node **is** the seam that manager approval slots into later.
>
> ```python
> class PlanStatusEnum(str, Enum):
>     """➕ NEW — simplified for M1; manager approval deferred"""
>     DRAFT = "DRAFT"
>     FINALISED = "FINALISED"
>     # PENDING_APPROVAL = "PENDING_APPROVAL"   # future — manager routing
>     # APPROVED = "APPROVED"                   # future
>     # REJECTED = "REJECTED"                   # future
> ```
>
> `ApprovalStatusEnum` is retained — **platform creative approval still needs it**, since that is a genuine three-way approval.
>
> ### ⚠ A control has been deliberately given up, and should be recorded as such
>
> This step previously carried: *"The budget is locked at this moment — nothing launches that a person hasn't approved."*
>
> | | Old model | New model |
> |---|---|---|
> | Who plans | Trader | Trader |
> | Who approves | **A manager** — a second person | **The same trader** |
> | Independent check | ✅ Yes | ❌ No |
>
> **The spend gate itself remains** — Activate still requires an explicit trader action, so nothing launches accidentally. What has gone is **separation of duties**: the second pair of eyes.
>
> For M1 this is a reasonable trade — small team, contained budgets. It is recorded here so that nobody later assumes a control exists that does not. When budgets grow, *"who approved this £50,000?"* will have the answer *"the person who built it,"* and the manager routing will need reinstating.
>
> ### Two loops survive, one disappears
>
> | Loop | Status |
> |---|---|
> | **Duration mismatch → re-confirm the plan** | ✅ **Survives** — the economics genuinely changed. *"Re-approval"* becomes *"re-confirmation"* |
> | **Budget reduced at credit check → re-confirm** | ✅ **Survives**, same treatment |
> | **Plan rejected → return to Targeting** | ❌ **Removed** — there is no rejection. A trader who is not satisfied simply keeps refining |
>
> ### ✅ This also closes an open question
>
> *"Is the manager-approval threshold per advertiser, global, or per role?"* — **moot for M1**. It returns if the routing does.

## 💬 REPLY DRAFT

> Good to know — I'll simplify it. Worth saying that this one isn't a correction: the approval workflow was what had been confirmed when I wrote v2.0, and the simplification came after. So I'm updating rather than fixing.
>
> **What I'll change:** the step becomes **Finalise Plan**, `DRAFT → FINALISED`, set by the trader. `Manager required` and `Rejection reason` come out, `approved_by/at` become `finalised_by/at`, and the *"on rejection, return to Targeting"* edge goes — there's no rejection any more, a trader who isn't happy just keeps refining.
>
> **The architectural consequence is the interesting one: `interrupt()` isn't needed here.** It exists to stop the graph pending a signal from **outside** the conversation — which was the manager on a dashboard. With the trader finalising in-conversation, that's just the next message. Worth separating two things that get conflated: the **checkpointer** persists session state so a trader can leave and come back, and it does that regardless; **`interrupt()`** is specifically for an external, asynchronous gate.
>
> Which means **the only genuine interrupt left in M1 is platform creative approval** — Amazon, Netflix and Disney reviewing independently on their own timelines, outside the conversation. So `interrupt()` hasn't left the design, it's moved to where it actually belongs. Flagging that because it changes what Wajahat builds.
>
> **On "for now" — I'll keep the seam.** Rather than removing the step, I'll keep `finalise_plan` as its own node with a simplified mechanism, so reinstating manager approval later is a routing change rather than a restructure. Same with the enum: `DRAFT`/`FINALISED` live, with the approval states commented as future. `ApprovalStatusEnum` stays as-is, since platform approval still needs a real three-way status.
>
> **One thing I want to record rather than pass over.** The step used to carry *"nothing launches that a person hasn't approved."* With self-finalisation, the spend gate remains — activation is still an explicit action — but **separation of duties** doesn't. Same person plans and finalises. That's a fair trade for M1, and I'll note it as a deliberate deferral rather than leave it implicit, so nobody later assumes a control exists that doesn't. Two loops survive as re-confirmations: duration mismatch, and a budget reduced at credit check.
>
> This also makes one of my open questions moot — whether the manager-approval threshold sits per advertiser, globally or per role. It comes back if the routing does.

## ❓ David se poochhne wale sawaal
| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | `finalised_by` / `finalised_at` record karne ki zaroorat hai? (audit ke liye) | Agar nahi, to do fields aur hat sakti hain |
| 2 | Trader plan finalise karke **un-finalise** kar sakta hai? | Loop design par asar |
| 3 | Manager approval kab wapas aayega — M2? | Seam kitna strong rakhna hai |

## 🏷️ Nichod
> **David keh raha hai:** *"Humne isko simple kar diya — ab ye sirf ek status change hai plan ko final karne ke liye. Manager ka approval abhi nahi chahiye."*

**Severity: 🔴 HIGH** — kyunki:
- **Do fields hat gaye** (`manager_required`, `rejection_reason`)
- **Ek loop edge hat gaya** (rejection → Targeting)
- 🔴🔴 **`interrupt()` ki zaroorat khatam** — M1 me asli interrupt sirf **Step 10** bacha
- 🔴 **Separation of duties ka control** deliberately hat gaya — document karna zaroori
- ✅ **Ek open question moot**
- Aur ye **pehla scope-REDUCTION comment** hai — kaam ghatta hai, badhta nahi

---
---

# 🧩 COMMENTS #24 · #25 · #26 — STEPS 8, 9, 10

> Teeno ek screenshot me the. Teen alag steps par.
> **#24** = ⚠ hint (verify karna hai) · **#25** = ✅ mera flagged gap band · **#26** = ✅ mera fix confirm + extend

---
---

# 🗨️ COMMENT #24 — "Probably more likely simple-strategies endpoint"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 8: Create the Real Strategy` → **API calls at this step** |
| **Highlighted** | **`api/strategies`** |
| **Poori line** | *"API calls at this step: `POST /api/strategies/`, audience-set creation via CTV endpoint"* |

## 💬 David ne exactly kya likha
> *"probably more likely **simple-strategies** endpoint"* *(edited)*

## 🔍 Do zaroori baatein pehle
```
1️⃣ "probably more likely" — David PAKKA nahi hai
   → Ye ek HINT hai, confirmation nahi
   → "Check karo" keh raha hai, "ye badal do" nahi
   → Reply me assume nahi karna, VERIFY karna hai

2️⃣ "(edited)" — David ne apna comment SUDHARA
   → Yaani wo bhi soch raha tha
   → Ye ek genuine uncertainty hai unke liye bhi
```

---

## 🔴 Ye ek bade pattern ka ishara — "CTV endpoint family"
```
Document me PEHLE SE ek jagah ye ishara maujood tha:

Step 4 (Audiences) constraints:
  "The audience set does not need to be created before forecasting —
   it's created later at strategy creation via a SIMPLIFIED CTV ENDPOINT"
                                                  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
Step 8:
  "API calls: POST /api/strategies/, audience-set creation via CTV ENDPOINT"

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 DOCUMENT NE AUDIENCE KE LIYE "SIMPLIFIED CTV ENDPOINT" MAANA —        ║
║     PAR STRATEGY KE LIYE PURANA POORA ENDPOINT.                           ║
║  → Ye INTERNALLY INCONSISTENT hai!                                        ║
║                                                                          ║
║  David: strategy ka bhi ek "simple" version hai.                          ║
║                                                                          ║
║  → VOW me shayad ek POORA PARALLEL FAMILY hai:                            ║
║                                                                          ║
║     FULL endpoints              vs   SIMPLE / CTV endpoints               ║
║     ─────────────────                ─────────────────────                ║
║     POST /api/strategies/            POST /api/simple-strategies/ ?        ║
║     (6-step wizard, sab formats)     (CTV, chhota payload)                 ║
║     audience-set creation            "simplified CTV endpoint" (naam TBC)  ║
║     …aur bhi?                        …aur bhi?                            ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🎯 SABSE ZABARDAST BAAT — Ye 6 pichhle comments se JUD jaata hai
```
Sochо — `simple-strategies` KYUN exist karega?
Kyunki poora endpoint bahut kuch maangta hai jo CTV me nahi hai.

Aur dekho David ne KYA-KYA hataya hai ab tak:

╔══════════════════════════════════════════════════════════════════════════╗
║   #12  base_bid            → CTV me applicable nahi (fixed CPM)           ║
║   #14  formats (4 choices) → hamesha streaming_tv                         ║
║   #16  selling location    → Step 1 se hatao                              ║
║   #17  product ASINs       → baad me aata hai                             ║
║   #6   goal (3), kpi (6)   → fixed / derived                              ║
║   #23  manager approval    → hataya                                       ║
║   #25  click-through URL   → optional (naya!)                             ║
║                                                                          ║
║  🔴 PAYLOAD LAGATAAR CHHOTA HOTA JA RAHA HAI.                             ║
║                                                                          ║
║  Aur ab #24 batata hai ki EK ENDPOINT PEHLE SE HAI                        ║
║  jo EXACTLY IS CHHOTE PAYLOAD KE LIYE BANA HAI.                           ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Reply me ye likhna — dikhata hai ki tumne comments ko JODKAR dekha
   aur ek pattern pakda.
```

---

## ⚠ Mera Note 17 ka SABOOT kamzor ho gaya
```
Note 17 me maine Open Question #1 solve kiya tha. Mera SABOOT ye tha:

  "The document already demonstrates that Option A works. §4.2's create
   payload example sends: product_asins: []  ← empty array
   So POST /api/strategies/ accepts an empty ASIN list."

🔴 PAR — wo example `POST /api/strategies/` ka tha.
   Agar hum `simple-strategies` use kar rahe hain,
   to us example ka is endpoint se koi lena-dena nahi!

✅ Mera CONCLUSION theek hai (David ne #16+#17 me khud bataya)
❌ Mera SABOOT galat endpoint ka tha

→ Ye "conclusion galat" NAHI hai — "justification kamzor" hai.
  Reply me ye distinction SAAF karni hai, warna lagega poora resolution
  galat tha.
```

---

## 🔴 Theme 12 ka ESCALATION — ab endpoint bhi galat nikla
```
Pehle Theme 12 tha: "API ka RESPONSE SHAPE maan liya, verify nahi kiya"
Ab wo BADH gaya: "ENDPOINT NAME bhi maan liya"

╔══════════════════════════════════════════════════════════════════════════╗
║  §4 KA KITNA HISSA SUSPECT HAI — ab tak                                   ║
╠══════════════════════════════════════════════════════════════════════════╣
║  #20  audience-sets/suggest/  →  ❌ RESPONSE SHAPE galat (CONFIRMED)      ║
║  #24  POST /api/strategies/   →  ⚠ ENDPOINT hi galat ho sakta hai         ║
║       Audience-set creation   →  ⚠ "simplified CTV endpoint, name TBC"    ║
║       PATCH /strategies/{id}/ →  ❌ Catalogue me HAI HI NAHI (Note 17)     ║
║       Reach forecast          →  ⚠ DO endpoints + ek "TBC" — kaunsa kab?  ║
║       9 naye v2.0 endpoints   →  ❌ Koi spec hi nahi                      ║
║                                                                          ║
║  🔴 §4 ka poora catalogue ek ASSUMPTION hai, CONTRACT nahi                ║
╚══════════════════════════════════════════════════════════════════════════╝
```

**Isliye sawaal ek endpoint ka nahi hona chahiye — poore FAMILY ka:**
> ⚠ *"Kya VOW me CTV ke liye ek alag endpoint family hai? Agar haan, poori list chahiye — kyunki document ne wizard-era endpoints assume kar liye hain."*

**Ye ek ACHHA sawaal hai** — 6 chhote sawaal ek me samet leta hai.

---

## 🔧 Kya fix karna hai — #24
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Step 8 — API calls** | `POST /api/strategies/` → ⚠ **`POST /api/simple-strategies/`** *(naam confirm karna hai)* |
| 2 | 🔴 **§4 API catalogue** | ➕ **"CTV endpoint family"** section — kaunse endpoints ke simple/CTV versions hain |
| 3 | ⚠ **Note 17 ka evidence** | Saaf karo ki `product_asins: []` example **poore endpoint** ka tha |
| 4 | 🔴 **§4 verification markers** | `POST /api/strategies/` ko **⚠ ASSUMED** mark karo |
| 5 | **Audience-set creation** | ⚠ Naam ab **zaroori** hai — pattern confirm ho gaya |
| 6 | ⚠ **Naming** | `/api/simple-strategies/` ya `/api/strategies/simple/`? |
| 7 | 🔴 **§4 vs Step 4 inconsistency** | Document ne audience ke liye CTV endpoint maana, strategy ke liye nahi — reconcile karo |

## ✍️ DOCUMENT NOTE (draft)
> **📝 REVIEW NOTE 24 — The create endpoint is probably `simple-strategies`, and this points at a wider gap**
>
> **David's comment:** *"probably more likely simple-strategies endpoint"* (edited)
>
> Noting the hedge — *"probably more likely"* — this is a **hint to verify**, not a confirmed correction. It is recorded as an unresolved item rather than applied as fact.
>
> ### The document already contained half of this signal
>
> The Targeting step states that the audience set is *"created later at strategy creation via a **simplified CTV endpoint**"*, and this step says *"audience-set creation via **CTV endpoint**"*. So the document already assumed a **CTV-specific endpoint for audiences** — while using the **full wizard-era endpoint for the strategy itself.** That is internally inconsistent, and David's comment suggests both have simplified variants.
>
> ### Why a simplified endpoint would exist — and why it matters here
>
> `POST /api/strategies/` was built for the six-step wizard covering all four formats. The review has progressively removed most of what that payload expects:
>
> | Removed by | What went |
> |---|---|
> | Note 12 | `base_bid` — not applicable to CTV |
> | Note 14 | `formats` as a four-way choice — always `streaming_tv` |
> | Note 16 | `product_location` — moves to the advertiser record |
> | Note 17 | `product_asins` — collected later |
> | Note 6 | `goal` and `kpi` as multi-choice — fixed and derived |
> | Note 23 | The approval workflow |
> | Note 25 | `click_through_url` — now optional |
>
> **The payload has been shrinking with every comment — and an endpoint apparently already exists built for exactly that reduced shape.**
>
> ### ⚠ This weakens the evidence in Review Note 17
>
> Note 17 resolved the ASIN-timing open question and cited §4.2's create payload — `"product_asins": []` — as proof that creating without ASINs works. **That example is for `POST /api/strategies/`.** If the CTV path uses `simple-strategies`, the example does not apply.
>
> **The conclusion still stands** — it came from David's own comments — but the supporting evidence needs re-verifying against the correct endpoint. The answer is right; the justification was for the wrong endpoint.
>
> ### 🔴 This escalates the API-verification problem
>
> Previously the concern was that §4.2's **response shapes** were assumptions. It now extends to **endpoint names**:
>
> | Endpoint | Status |
> |---|---|
> | `POST /audience-sets/suggest/` | ❌ Response shape confirmed wrong (Note 20) |
> | `POST /api/strategies/` | ⚠ **Endpoint itself may be wrong** (this note) |
> | Audience-set creation | ⚠ *"simplified CTV endpoint, name TBC"* — never named |
> | `PATCH /api/strategies/{id}/` | ❌ Not in the catalogue at all (Note 17) |
> | Reach forecast | ⚠ Two listed plus a third "TBC" — which applies when is unstated |
> | The nine v2.0 endpoints | ❌ No specifications |
>
> **§4 should be treated as a set of assumptions, not a contract.**
>
> ### ⚠ The question to ask is bigger than one endpoint
>
> **Is there a CTV-specific endpoint family in VOW, and what is in it?** One answer resolves six of the items above. Also to confirm: is it `/api/simple-strategies/` or `/api/strategies/simple/`?

## 💬 REPLY DRAFT
> Thanks — I'll verify rather than assume, given the hedge.
>
> **What makes this likely: the document already contained half the signal.** The Targeting step says the audience set is created *"via a simplified CTV endpoint"* — so I'd already assumed a CTV-specific endpoint for audiences, while using the full wizard-era endpoint for the strategy itself. That's inconsistent, and your comment suggests both have simplified variants.
>
> It also fits everything else in this review. **The create payload has been shrinking with every comment** — base bid gone, formats fixed, selling location and ASINs moved out, goal and KPI derived, approval workflow simplified, click-through URL now optional. It would make sense that an endpoint already exists built for exactly that reduced shape.
>
> **One correction I need to make.** When I resolved the ASIN-timing question, I cited §4.2's create payload showing `"product_asins": []` as proof that creating without ASINs works. **That example is for `POST /api/strategies/`** — if the CTV path uses `simple-strategies`, it doesn't apply. The conclusion still stands, since it came from your comments, but the evidence needs re-checking against the right endpoint.
>
> **And the bigger ask, since one answer covers several of my open items:** **is there a CTV-specific endpoint family, and what's in it?** Right now `POST /strategies/` may be wrong, the audience-set creation endpoint is unnamed, `PATCH /strategies/{id}/` isn't in the catalogue at all, there are two reach-forecast endpoints plus a third marked TBC, and the nine new v2.0 endpoints have no specs. I'd rather map the family once than chase them individually.
>
> Minor: is it `/api/simple-strategies/` or `/api/strategies/simple/`?

## 🏷️ #24 ka nichod
> **David keh raha hai:** *"Jo `POST /api/strategies/` tumne likha — shayad wo galat endpoint hai. CTV ke liye ek `simple-strategies` endpoint hai."*

**Severity: 🔴 HIGH** — galat endpoint = Step 8 kaam nahi karega · **poore CTV endpoint family** ka ishara · Note 17 ka evidence kamzor · **Theme 12 escalate**

---
---

# 🗨️ COMMENT #25 — "Click-through URL: optional for streaming tv"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 9: Upload Video Creative` → field matrix |
| **Row** | **Click-through URL** |
| **Highlighted** | **"Required"** (Requirement column) |

## 💬 David ne exactly kya likha
> *"**optional for streaming tv**"*

## 🎉 YE EK GAP HAI JO MAINE PEHLE FLAG KIYA THA — jawab mil gaya
```
Reviewed document ke Step 8 me maine likha tha:

  "⚠ ITEMS FLAGGED HERE
   1. Click-through URL is Required, unexplained. CTV has no click. The
      field is ✅ UNCHANGED from v1.1.0 where Display was in scope.
      EITHER Amazon DSP mandates it even for CTV (in which case say so),
      OR IT SHOULD BE OPTIONAL FOR CTV."
                ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

✅ David ne DOOSRA option confirm kiya: OPTIONAL for streaming TV.

╔══════════════════════════════════════════════════════════════════════════╗
║  🎯 AUR YE MERE PREDICTION KO VALIDATE KARTA HAI                          ║
║                                                                          ║
║  §11 (Remaining Review Work) me maine likha tha:                          ║
║    "Step 8 — Upload creative: … the CLICK-THROUGH URL REQUIREMENT IS      ║
║     UNEXPLAINED FOR CTV …"                                               ║
║                                                                          ║
║  → Us step ke 3 predictions the, ek LAND ho gaya                          ║
║  → Prediction approach kaam kar raha hai                                  ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Reply me likhna — David ko dikhega ki tumne ye gap KHUD pakda tha.
```

## 🔍 Kyun Optional? (business wajah)
```
CTV me remote se CLICK nahi hota.

  📺 TV par ad chal raha hai
  → Tum remote uthao
  → Kya karo? Koi cursor nahi, koi tap nahi
  → CLICK POSSIBLE HI NAHI

To click-through URL kis kaam ka?
  • Kuch CTV formats me QR code / interactive overlay (rare)
  • Kuch advertisers reporting consistency ke liye rakhte hain
  • Par MOSTLY — bekaar

→ Isliye OPTIONAL, na ki Required
```

## 🔗 "for streaming tv" — format-conditional hai
```
David ne "optional for STREAMING TV" kaha — format specify kiya.
Aur #14 se: CTV ka format HAMESHA streaming_tv hai.

  formats = ["streaming_tv"]  →  click_through_url OPTIONAL
  formats = ["display"]        →  click_through_url REQUIRED
                                  (par display scope me nahi)

🔴 M1 me ye EFFECTIVELY HAMESHA OPTIONAL hai.

→ Aur ye THEME 8 ka ek aur case hai: "non-CTV leftover"
  Bilkul jaise base_bid (#12) aur formats-4-choices (#14)
```

## 🔴 Design sawaal — agent ko POOCHHNA chahiye?
```
Ab tak ka pattern (#6, #7, #9, #13, #21): jo zaroori nahi, wo poochho mat.

❌ Agent poochhe:
   "Click-through URL kya rakhun?"
   → Trader: "CTV me click hi nahi hota, ye kyun poochh rahe ho?"

✅ Agent na poochhe, par ACCEPT kare agar trader de:
   Agent: "30-second video register ho gaya (asset_44521).
           Duration approved plan se match karti hai. ✅"
   → Bas. Click-through URL ka zikr hi nahi.
   → Par trader khud kahe to accept kar le

💡 Rule: Optional + mostly useless on CTV = DON'T ASK, but ACCEPT if offered
```

## 🔧 Kya fix karna hai — #25
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | **Step 9 — Click-through URL** | Requirement: **Required → Optional** |
| 2 | **Step 9 — Change column** | ~~✅ Unchanged~~ → **🔄 CHANGED — Optional for CTV** |
| 3 | 🔴 **`SelectedCreativeSchema`** | `click_through_url: HttpUrl = Field(...)` → **`Optional[HttpUrl] = None`** |
| 4 | ➕ **Naya note** | **Kyun** optional — CTV me click nahi hota · Display-era field hai |
| 5 | **Agent behaviour** | **Poochho mat** — par trader de to accept karo |
| 6 | ✅ **Step 8 flagged item #1** | **RESOLVED mark karo** |
| 7 | **§4.2 create payload** | Example theek hai, par field optional hai (note add karo) |

## ✍️ DOCUMENT NOTE (draft)
> **📝 REVIEW NOTE 25 — ✅ Click-through URL is optional for streaming TV**
>
> **David's comment:** *"optional for streaming tv"*
>
> This closes a gap flagged earlier in this revision. The Upload Creative step noted:
>
> > *"Click-through URL is Required, unexplained. CTV has no click. The field is ✅ UNCHANGED from v1.1.0 where Display was in scope. Either Amazon DSP mandates it even for CTV (in which case say so), **or it should be Optional for CTV**."*
>
> **The second reading was correct.**
>
> ### Why
>
> There is no click on a television. No cursor, no tap. A click-through URL has no mechanism to act on for the great majority of CTV delivery. It may still be useful in narrow cases — interactive overlays, QR codes, reporting consistency — but it cannot be required.
>
> **This is another v1.1.0 leftover**, in the same class as `base_bid` (Note 12) and the four-way `formats` choice (Note 14): fields that made sense when Display was in scope and do not now.
>
> ### Requirement is conditional on format
>
> | Format | Click-through URL |
> |---|---|
> | `streaming_tv` | **Optional** |
> | `display` | Required — *but out of scope* |
>
> Since the format is always `streaming_tv` (Note 14), it is **effectively always optional in M1**.
>
> ### Agent behaviour: do not ask, but accept
>
> Consistent with the pattern established across Notes 6, 7, 9, 13 and 21 — do not ask for something that is not needed. The agent should not prompt for a click-through URL; if the trader volunteers one, it is accepted.
>
> ### Schema change
>
> ```python
> # SelectedCreativeSchema
> click_through_url: Optional[HttpUrl] = Field(
>     None, description="Optional for streaming TV — no click mechanism on CTV")
> ```

## 💬 REPLY DRAFT
> Confirmed — and this was one I'd flagged as unresolved at that step: *"either Amazon DSP mandates it even for CTV, or it should be optional for CTV."* You've answered the second way, so I'll make it optional.
>
> The reasoning I'll record: **there's no click on a television** — no cursor, no tap. It may still matter for interactive overlays or QR codes, but it can't be required. It's another v1.1.0 leftover, same class as base bid and the four-way formats choice — fields that made sense when Display was in scope.
>
> Since the format is always `streaming_tv`, it's effectively always optional in M1. `click_through_url` becomes `Optional[HttpUrl] = None`.
>
> One behaviour decision, consistent with the rest of the review: **the agent won't ask for it.** Asking for a click destination on a TV ad invites the obvious question. If a trader volunteers one, it's accepted.

## 🏷️ #25 ka nichod
> **David keh raha hai:** *"Click-through URL streaming TV ke liye optional hai, required nahi."*

**Severity: 🟡 MEDIUM** — saaf, contained fix. **Par ye ek gap band karta hai jo maine khud flag kiya tha.**

---
---

# 🗨️ COMMENT #26 — "It's just a single status for each channel — could be paramount or channel 4"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 10: Platform Creative Approval` → **poora field table** |
| **Highlighted** | *"Amazon approval status / Netflix approval status (if Netflix inventory) / Disney approval status (if Disney inventory)"* |

## 💬 David ne exactly kya likha
> *"It's just a **single status for each channel** not necessary netflix or disney - **could be paramount or channel 4**"*

## 🔍 Do baatein ek me
```
1️⃣ "It's just a SINGLE STATUS FOR EACH CHANNEL"
   → Confirm: per-channel ek status. Ye theek hai.

2️⃣ "NOT NECESSARY netflix or disney - could be PARAMOUNT or CHANNEL 4"
   → 🔴 Channel list FIX NAHI hai!
   → Netflix/Disney hard-code karna GALAT hai
```

## 🎉 Ye mere PROPOSED FIX ko CONFIRM karta hai
```
Reviewed document ke Step 9 me maine likha tha:

  "📋 REVIEW NOTE — The schema holds one status; this step needs three
   creative_approval_statuses: dict[str, ApprovalStatusEnum]
   # {"Amazon": "APPROVED", "Netflix": "PENDING", "Disney+": "REJECTED"}"

✅ David ka "single status for each channel" — BILKUL YAHI hai!

╔══════════════════════════════════════════════════════════════════════════╗
║  🎯 Aur DICT ka faayda ab DOUBLE ho gaya:                                 ║
║                                                                          ║
║  Pehle: "teen statuses chahiye, ek nahi"                                  ║
║  Ab bhi: "channel list KHULI hai — Paramount, Channel 4, jo bhi"          ║
║                                                                          ║
║  → Ek dict DONO solve karta hai                                          ║
║  → ENUM se ye possible NAHI hota (enum me values fix hoti hain)            ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 CTV ki duniya bahut BADI hai
```
Document ne teen channels maane: Amazon, Netflix, Disney+
David: "could be PARAMOUNT or CHANNEL 4"

Asli CTV landscape (khaas kar UK me):
  📺 Amazon Prime Video · Netflix · Disney+
  📺 Paramount+          ← David ne mention kiya
  📺 Channel 4 (All 4)   ← David ne mention kiya · UK broadcaster
  📺 ITVX · Sky/NOW      ← UK
  📺 Hulu                ← document me §2.3 me PEHLE SE hai!

🔴 DOCUMENT APNE AAP SE INCONSISTENT HAI:
   §2.3 tier table kehta hai "Netflix, HULU, OTHERS"
   Step 10 me sirf teen hard-coded
   → §2.3 SAHI tha
```

## 🔗 Ye CLIENT ke ek PURANE requirement se judta hai
```
Document ke Step 5 me client ka critical note:
  "This targeting list FREQUENTLY CHANGES so it should be easy to add
   new targeting types."
  → the implementation must be CONFIG-DRIVEN, not hard-coded.

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 DAVID KA #26 WAHI PRINCIPLE HAI — CHANNELS PAR                        ║
║                                                                          ║
║  "Targeting list badalti rehti hai"  →  config-driven  (client)           ║
║  "Channel list fix nahi hai"          →  config-driven  (#26)             ║
║                                                                          ║
║  💡 Yaani config-driven requirement SIRF targeting ka nahi tha —          ║
║     wo ek GENERAL PRINCIPLE hai.                                         ║
║                                                                          ║
║  Aur kahan lag sakta hai?                                                 ║
║    ✅ Targeting types         (client — confirmed)                         ║
║    ✅ Channels / providers    (#26 — confirmed)                           ║
║    🟡 Audience data sources?  (#2 — Amazon 1P, 3P… aur?)                  ║
║    🟡 Deal types?             (PG, Preferred, Private Auction… aur?)       ║
║    🟡 Inventory tiers?        (teen… aur ho sakte hain?)                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 Channel list kahan se aayegi? — DERIVE karo, hard-code nahi
```
Approval statuses kaunse channels ke liye chahiye?
  → Jo channels PLAN ME HAIN!

  selected_deals = [
    {channel: "Prime Video", …},
    {channel: "Netflix", …},
  ]
       ↓ derive
  creative_approval_statuses = {
    "Prime Video": "PENDING",
    "Netflix": "PENDING"
  }

→ Koi hard-coded list nahi
→ Koi "(if Netflix inventory)" condition nahi (automatically handle ho gayi)
→ Paramount+ add karo → automatically kaam karega

🔴 Aur dekho — document ka "(if Netflix inventory)" qualifier bhi GAAYAB
   ho jaata hai, kyunki dict me sirf plan ke channels honge. Elegant.
```

## ✅ NAMING ka jawab mil gaya
```
Comment #18 me maine open question uthaya tha:
  ⚠ "channel" (David) vs "channels" (rate card) vs `provider` (schema)

Ab dekho David ne "channel" KITNI BAAR use kiya:
  #18: "if we know the market, duration and CHANNEL"
  §4:  rate card returns "CHANNELS, durations, CPMs"  (document me)
  #26: "a single status for each CHANNEL"

🔴 TEEN BAAR "channel". EK BAAR BHI "provider" nahi.

✅ JAWAB: "channel" — `provider` ko rename karna chahiye
→ Aur `ChannelTypeEnum` (jo dsp/sponsored ke liye hai) ko bhi rename
  karna padega taaki collision na ho
→ Ek open question RESOLVE ho gaya
```

## 🔧 Kya fix karna hai — #26
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | 🔴 **Step 10 field table** | Teen hard-coded rows → **ek row: "Approval status per channel"** |
| 2 | 🔴 **`FullStrategySchema`** | `creative_approval_status` → **`creative_approval_statuses: dict[str, ApprovalStatusEnum]`** *(pehle proposed, ab confirm)* |
| 3 | ✅ **Keys ka source** | **Derive** from `selected_deals[].channel` — hard-code nahi |
| 4 | ➕ **Naya note** | **Channel list KHULI hai** — Paramount+, Channel 4, ITVX, Sky, Hulu… |
| 5 | 🔴 **§2.3 vs Step 10** | §2.3 kehta hai *"Netflix, Hulu, others"* — reconcile karo |
| 6 | 🔴 ➕ **Naya note** | **Config-driven requirement channels par bhi** — sirf targeting par nahi |
| 7 | ✅ **Naming resolve** | **"channel"** par settle · `provider` rename · `ChannelTypeEnum` rename |
| 8 | **Step 10 *"(if Netflix inventory)"*** | Qualifier hatao — dict expresses it |
| 9 | ⚠ **Audit** | Aur kahan fixed list hai jo khuli honi chahiye? |

## ✍️ DOCUMENT NOTE (draft)
> **📝 REVIEW NOTE 26 — One status per channel, and the channel list is open**
>
> **David's comment:** *"It's just a single status for each channel not necessary netflix or disney - could be paramount or channel 4"*
>
> Two things, one confirmed and one corrected.
>
> ### Confirmed: one status per channel
>
> This validates the fix already proposed at this step. `FullStrategySchema.creative_approval_status` was a single value while the step's table specified three; the proposed replacement was a dictionary keyed by channel. David's *"a single status for each channel"* is exactly that.
>
> ### Corrected: the channel list is not Amazon / Netflix / Disney
>
> The table hard-coded three channels. **The real list is open** — Paramount+, Channel 4, ITVX, Sky, Hulu and others.
>
> **The document is inconsistent with itself here:** §2.3's tier table says *"Netflix, Hulu, **others**"*, while this step names exactly three. The tier table was right.
>
> ### The keys should be derived, not declared
>
> ```python
> creative_approval_statuses: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
> # keys derived from selected_deals[].channel
> # {"Prime Video": "APPROVED", "Netflix": "PENDING"}
> ```
>
> A dictionary handles both requirements at once — independent per-channel statuses **and** an open channel list. An enum could not.
>
> It also **removes the *"(if Netflix inventory)"* qualifiers**: the dictionary contains only the channels actually in the plan, so the condition is expressed by the data rather than by a note.
>
> ### 🔴 The config-driven requirement is broader than targeting
>
> The Targeting step records the client's requirement: *"This targeting list frequently changes so it should be easy to add new targeting types"* — config-driven, not hard-coded. **This comment applies the same principle to channels.**
>
> That suggests it was never a rule about targeting specifically, but a **general principle**. Other places the document declares a closed list that may not be:
>
> | List | Status |
> |---|---|
> | Targeting types | ✅ Confirmed open — client |
> | **Channels / providers** | ✅ **Confirmed open — this note** |
> | Audience data sources | 🟡 Amazon 1P, third-party… and others? |
> | Deal types | 🟡 PG, Preferred, Private Auction… and others? |
> | Inventory tiers | 🟡 Three — could there be more? |
>
> **A pass over the document is needed to find every fixed list that should be open.**
>
> ### ✅ This also settles a naming question
>
> The naming conflict raised earlier — *"channel"* vs *"channels"* vs `provider` — resolves in favour of **"channel"**. David has used it three times, the rate-card endpoint returns *"channels"*, and *"provider"* appears only in this document's own schema. **`provider` should be renamed to `channel`**, and `ChannelTypeEnum` — which uses "channel" for `dsp`/`sponsored` — renamed to avoid the collision.

## 💬 REPLY DRAFT
> Both parts useful — one confirms something, one corrects it.
>
> **Confirmed:** one status per channel is what I'd proposed at that step. The schema had a single `creative_approval_status` while the table specified three, and my fix was a dictionary keyed by channel. *"A single status for each channel"* is exactly that.
>
> **Corrected: the channel list is open, and I'd hard-coded three.** Paramount+, Channel 4 — and the document contradicts itself here, because §2.3's tier table says *"Netflix, Hulu, **others**"* while this step names exactly three. The tier table was right.
>
> So the dictionary keys get **derived from the channels in the plan** rather than declared, which also removes the *"(if Netflix inventory)"* qualifiers — the data expresses the condition instead of a note.
>
> **The wider point I want to raise.** The Targeting step records the client's requirement that *"this targeting list frequently changes so it should be easy to add new targeting types"* — config-driven, not hard-coded. **Your comment applies the same principle to channels,** which tells me it was never a rule about targeting specifically. I'll do a pass for every other fixed list in the document that should be open — audience data sources, deal types, possibly the inventory tiers themselves.
>
> This also settles a naming question I'd raised. You've used **"channel"** three times, the rate-card endpoint returns *"channels"*, and *"provider"* only appears in my own schema. So `provider` becomes `channel`, and I'll rename `ChannelTypeEnum` — which currently uses "channel" for `dsp`/`sponsored` — to avoid the collision.

## 🏷️ #26 ka nichod
> **David keh raha hai:** *"Har channel ka ek status — theek hai. Par Netflix/Disney hard-code karna galat — Paramount+ ya Channel 4 bhi ho sakta hai."*

**Severity: 🔴 HIGH** — hard-coded channel names ek asli schema defect · ✅ mera dict fix confirm · 🔴 config-driven requirement channels par bhi · ✅ naming resolve · §2.3 vs Step 10 inconsistency

---
---

# 🔗 COMMENTS #24–#26 KA JOD

## Do naye structural findings

### Finding 1 — "CTV endpoint family" (from #24)
```
Document ne WIZARD-ERA endpoints assume kiye.
Par CTV ke liye ek chhota, alag family exist karta hai:

  Audience-set creation  →  "simplified CTV endpoint" (document me PEHLE SE!)
  Strategy creation      →  "simple-strategies"       (#24)
  …aur kya?              →  ⚠ POOCHHNA HAI

🔴 Aur document APNE AAP SE inconsistent tha — audience ke liye CTV
   endpoint maana, strategy ke liye nahi.

→ Ek sawaal 6 chhote sawaal solve kar dega
```

### Finding 2 — "Config-driven" sirf targeting ka nahi tha (from #26)
```
Client: "targeting list frequently changes → config-driven"
#26:    "channel list fix nahi hai → config-driven"

🔴 Ye ek GENERAL PRINCIPLE hai, ek field ka rule nahi.

→ Poore document ka AUDIT chahiye: "kahan-kahan maine ek FIX LIST
  likhi hai jo asal me KHULI hai?"
```

## ✅ Do cheezein RESOLVE ho gayi
| Kya | Jawab | Via |
|---|---|---|
| Click-through URL CTV me required hai? | **Nahi — optional** | #25 |
| "channel" vs "channels" vs `provider` | **"channel"** | #26 |

---
---

# 🗨️ COMMENT #27 — "Tracking Setup could be done before creatives — no order necessary"

## 📍 Location
| | |
|---|---|
| **Section** | `Step 11: Tracking Setup` |
| **Highlighted** | **"Tracking Setup"** — poora **step ka naam** |
| **Asar** | 🔴🔴 Poore flow ka **structure** · state model · Basil ka canvas |

## 💬 David ne exactly kya likha
> *"could be done **before creatives** if they are no available yet - **no order necessary**"*

## 🔍 Line-by-line
| Hissa | Matlab |
|---|---|
| *"could be done **before creatives**"* | Tracking setup creative upload **se pehle** ho sakta hai |
| *"if they are **no available yet**"* | Agar creative abhi taiyar nahi *(typo — "not available yet")* |
| *"**no order necessary**"* | 🔴 **Kram ki koi zaroorat nahi** — sabse bada hissa |

## ❌ Document abhi kya kehta hai
```
Document ka flow ek SEEDHI LINE hai:
  7. Plan approval → 8. Create → 9. Upload creative → 10. Platform approval
  → 11. Tracking setup → 12. Credit check → 13. Activate

Aur Step 11 ka text SAAF kehta hai:
  "Both now sit here, AFTER CREATIVE APPROVAL and before tracking is attached."
                       ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
              Document ne EXPLICITLY tracking ko creative ke BAAD rakha
```

---

## 🔴 SABSE BADA POINT — Document ne SABSE LAMBA kaam SABSE AAKHIR me rakha
```
╔══════════════════════════════════════════════════════════════════════════╗
║  KAAM                        KITNA TIME      KISPAR DEPEND KARTA HAI      ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Plan banana (Steps 1-6)     minute          Agent — turant               ║
║  Finalise + Create           second          Trader ka ek click           ║
║  Creative upload             🕐 DIN           Agency video bana rahi hai    ║
║  Platform approval           🕐 24-48 ghante  External (Amazon/Netflix)    ║
║  🔴 AD TAG INSTALL           🕐🕐 DIN/HAFTE   Advertiser ka DEV TEAM       ║
║  Credit top-up               minute-ghante    Finance/card                 ║
╚══════════════════════════════════════════════════════════════════════════╝

🔴 AD TAG SABSE LAMBA KAAM HAI — aur document ne use SABSE AAKHIR me rakha!
```

### Document KHUD batata hai ki ad tag kitna critical hai
```
Step 11 ka apna warning:
  "the tag must be installed BEFORE the campaign runs
   (tracking only records activity AFTER IT GOES LIVE)"

Yaani: tag late laga → us se pehle ka data HAMESHA KE LIYE GAYA

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 DOCUMENT NE EK AISA KAAM AAKHIR ME RAKHA JO:                          ║
║     1. Sabse ZYADA time leta hai (dev team chahiye)                       ║
║     2. Kisi AUR TEAM par depend karta hai (advertiser ka developer)        ║
║     3. Late hua to nuksaan IRREVERSIBLE hai                               ║
║                                                                          ║
║  → Aakhir me rakhne se ye SABSE ZYADA jaldi-jaldi ya SKIP hone ka          ║
║    khatra rakhta hai                                                     ║
║                                                                          ║
║  → David ka comment sirf "flexibility" nahi de raha — wo ek ASLI RISK      ║
║    KAM kar raha hai                                                      ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Reply me ye likhna — dikhata hai ki tumne comment ka ASLI FAAYDA samjha.
```

---

## 🔴🔴 Flow ka MODEL badal jaata hai — LINE se BRANCHES
```
╔══════════════════════════════════════════════════════════════════════════╗
║  ❌ DOCUMENT KA MODEL — LINEAR CHAIN                                      ║
║   Create → Creative → Platform → Tracking → Credit → Activate            ║
║      (har step AGLE ko gate karta hai)                                    ║
║                                                                          ║
║   🔴 Problem: creative atka → TRACKING BHI ATKA                           ║
║              par tracking ka creative se KOI LENA-DENA NAHI!              ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ✅ DAVID KA MODEL — PREREQUISITES SET (parallel branches)                 ║
║                                                                          ║
║   Create ──┬──→ Creative upload ──→ Platform approval ──┐                 ║
║            ├──→ Tracking setup ─────────────────────────┤──→ 💰 ACTIVATE  ║
║            └──→ Credit check ───────────────────────────┘                 ║
║                                                                          ║
║   → Teen SWATANTRA branches                                              ║
║   → Activate ek JOIN NODE hai — sabka intezaar karta hai                  ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Asli dependencies — kaunsa step kispar depend karta hai?
```
1.  Basics → Inventory              ✅ HAAN (market/duration chahiye deal match ke liye)
2.  Inventory → Targeting           ✅ HAAN (tier tay karta hai targeting — #1)
3.  Targeting → Budget split        ✅ HAAN (audience fee accurate CPM ka input)
4.  Budget split → Forecast         ✅ HAAN (per-line budget chahiye)
5.  Forecast → Finalise             ✅ HAAN
6.  Finalise → Create               ✅ HAAN
────────────────────────────────────────────────────────────────────────────
7.  Create → Creative upload        🟡 Shayad (asset attach ke liye strategy ID?)
8.  Create → ASIN patch             ✅ HAAN (PATCH ke liye strategy ID — Note 17)
9.  Create → Credit check           ❌ NAHI — credit poori tarah swatantra
10. Creative → Platform approval    ✅ HAAN (jo upload nahi hua, review kaise?)
11. Tracking ↔ Creative             ❌ NAHI — inka koi rishta hi nahi!
12. Sab kuch → Activate             ✅ HAAN (sab prerequisites)

🔴 NATEEJA: Create ke BAAD teen cheezein SWATANTRA ho jaati hain
```

---

## 🔴 Tracking Setup KHUD do-teen hisson me bat jaata hai
```
Step 11 me teen kaam hain — unki dependencies ALAG hain:

╔══════════════════════════════════════════════════════════════════════════╗
║  A) AD TAG INSTALLATION                                                   ║
║     → Advertiser ki WEBSITE par code lagta hai                            ║
║     → Strategy se KOI LENA-DENA NAHI                                      ║
║     → 🔴 YE DIN 1 SE HO SAKTA HAI — plan banne se bhi PEHLE!              ║
║                                                                          ║
║  B) ASIN COLLECTION + PATCH                                               ║
║     → PATCH /api/strategies/{id}/ ke liye strategy ID chahiye             ║
║     → Create ke BAAD (Note 17 se)                                         ║
║                                                                          ║
║  C) CONVERSION EVENTS chunna                                              ║
║     → Ad tag ka exist karna zaroori · A ke baad                           ║
╚══════════════════════════════════════════════════════════════════════════╝
```

**Aur (A) ka koi dependency nahi — to wo SABSE PEHLE ho sakta hai:**
```
🔴 Agar advertiser ke paas ad tag NAHI hai aur usme HAFTE lagte hain —
   to ye DIN 1 par pata chalna chahiye, Step 11 par nahi!

Agent ka behaviour (mera SUGGESTION — David ne itna nahi kaha):

  Session ke shuru me, advertiser defaults load karte waqt (#13):
    Agent: "Ek baat pehle — BrightPath ka ad tag registered nahi hai.
            Tumne bataya apni website par bechte ho, to conversions
            track karne ke liye tag lagana padega.

            ⚠ Ye advertiser ke dev team ka kaam hai, din/hafte lag sakte
              hain. Aur tag lagne SE PEHLE ka data recover nahi hota.

            Main plan banata rahunga — tum ye kaam PARALLEL me shuru
            kar do. Setup instructions: […]"

→ Trader ka plan banta rahega, dev team ka kaam SAATH ME chalega

⚠ Ye David ne NAHI kaha — mera extension hai uske lead-time logic se.
  Isko SUGGESTION ki tarah pesh karna, confirmation nahi.
```

---

## 🔴 Ek asli problem — `current_stage` TOOT jaata hai (Basil ke liye)
```
Document ka state me hai:
  current_stage: str        # "for the adaptive canvas"

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 AGAR TEEN CHEEZEIN EK SAATH CHAL RAHI HAIN — "current_stage" KYA HOGA?║
║                                                                          ║
║  Creative: platform approval ka intezaar                                  ║
║  Tracking: ad tag ka intezaar                                            ║
║  Credit:   top-up ho gaya ✅                                              ║
║                                                                          ║
║  → current_stage = "creative_approval"? "tracking"? Dono?                 ║
║  → EK STRING TEEN PARALLEL STATES EXPRESS NAHI KAR SAKTI                  ║
╚══════════════════════════════════════════════════════════════════════════╝

✅ FIX — do cheezein alag karo:
  current_focus: str                    # trader ABHI kis par kaam kar raha hai
  activation_prerequisites: {…}         # kya-kya bacha hai (map)
```

```python
class ActivationPrerequisitesSchema(BaseModel):
    """➕ NEW (Note 27) — these run independently; activation joins them"""
    creative_uploaded: dict[str, bool] = Field(default_factory=dict)
    # per duration: {"30": True, "15": False}   ← Step 9 ka partial-upload gap bhi cover!

    creative_approved: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
    # per channel — Note 26

    ad_tag_registered: Optional[bool] = None
    asins_attached: bool = False
    conversions_selected: bool = False
    tracking_skipped: bool = False        # trader ne jaan-boojh kar skip kiya
    credit_sufficient: Optional[bool] = None

    @property
    def outstanding(self) -> list[str]: ...
    @property
    def ready_to_activate(self) -> bool: ...
```

**🎉 Side benefit:** `creative_uploaded` ko `dict[str, bool]` banane se **Step 9 ka wo gap bhi band** ho jaata hai jo maine flag kiya tha (*"multiple durations, partial upload is not covered"*). **Ek fix, do problems.**

---

## ✅ Loops — bache rehte hain, par apni branch me
```
🔁 Creative rejected → wapas upload
   → CREATIVE BRANCH ke andar · baaki branches par asar nahi
   ✅ BEHTAR hua — pehle poora flow atakta tha

🔁 Credit insufficient → top-up
   → CREDIT BRANCH ke andar  ✅ Behtar

🔁 Duration mismatch → wapas Finalise
   → 🔴 CROSS-BRANCH — creative branch se UPSTREAM (finalise) tak
   → Kyunki plan ka ganit badla, sab branches affect ho sakti hain
   ⚠ Ye ek genuine cross-branch loop hai — document karna zaroori
```

---

## 🤖 Agent ka naya behaviour — "kram" ki jagah "kya bacha hai"
```
❌ PURANA (linear):
Agent: "Strategy ban gayi. Ab creative upload karo."
Trader: "Agency ne video nahi diya abhi."
Agent: "Creative ke bina aage nahi badh sakte."
Trader: "Par main ad tag ka kaam shuru kar sakta hun na?"
Agent: "Wo Step 11 me aata hai. Pehle creative."
        ↑ 😡 Bekaar block

✅ NAYA (prerequisites):
Agent: "✅ Strategy VMA2026412 ban gayi.

        Activate karne se pehle teen cheezein baaki — ye SWATANTRA hain,
        kisi bhi kram me:

        ┌────────────────────────────────────────────────────────────┐
        │ 📹 CREATIVE                                                 │
        │    30s video   ⬜ upload nahi hua                            │
        │    15s video   ⬜ upload nahi hua                            │
        │    Platform approval — upload ke baad, 24-48 ghante          │
        │ 📊 TRACKING                                                 │
        │    Ad tag      ⬜ registered nahi                            │
        │    ASINs       ⬜ collect nahi hue                           │
        │ 💳 CREDIT                                                   │
        │    £7,500 available · £10,000 chahiye                        │
        └────────────────────────────────────────────────────────────┘

        💡 Suggestion: AD TAG se shuru karo. Wo advertiser ke dev team ka
           kaam hai aur sabse zyada time leta hai. Aur agar campaign shuru
           hone ke baad laga, to pehle ka data hamesha ke liye chala jaayega.

           Creative ka intezaar karte hue ye parallel me chal sakta hai.

        Kis par kaam karna hai?"

🔴 Dhyan do — agent ne "ad tag pehle karo" ki SALAH di. Ye agent ka
   EXPERTISE hai, sirf processing nahi. Task slide ke "owns the brain"
   role se match karta hai.
```

---

## 🔗 Flow structure ka poora safar — teen comments milkar
```
╔══════════════════════════════════════════════════════════════════════════╗
║  FLOW STRUCTURE — TEEN COMMENTS NE PROGRESSIVELY DHEELA KIYA               ║
╠══════════════════════════════════════════════════════════════════════════╣
║  v2.0 original:  13 rigid steps, seedhi line + loops                      ║
║                                                                          ║
║  #5   →  Steps 4+5 MERGE           → 12 steps                            ║
║  #23  →  Step 7 ka GATE hata       → ek loop edge kam                     ║
║  #27  →  Tail steps UNORDERED      → parallel branches + join             ║
║                                                                          ║
║  🔴 NATEEJA:                                                             ║
║     Pehle:  13 steps · rigid chain · 5 loops · 2 interrupts               ║
║     Ab:     ~9 sequential + 3 parallel branches · join at Activate        ║
║             · 4 loops (ek branch-local) · 1 interrupt (platform approval)  ║
╚══════════════════════════════════════════════════════════════════════════╝

→ Wajahat ke liye BADI baat — graph ka SHAPE hi badal gaya
```

## ✅ Naya flow — poora
```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  REVISED FLOW (after #5, #23, #27)                                                     ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║  SEQUENTIAL — har step agle ko genuinely chahiye                                       ║
║   1. Basics · 2. CTV Inventory · 3. Targeting · 4. Budget Split                        ║
║   5. Predict Reach · 6. Finalise Plan · 7. Create Strategy                             ║
║                                                                                       ║
║  ─────────── 🔀 PARALLEL — kisi bhi kram me, ek saath ───────────                      ║
║   Branch A: 📹 Upload creative ──→ Platform approval (per channel)                      ║
║             🔁 rejected → wapas upload                                                 ║
║             🔁 duration mismatch → ⬆ wapas Finalise (cross-branch)                     ║
║             ⏸ interrupt() — M1 ka EK HI asli interrupt                                 ║
║   Branch B: 📊 Tracking setup                                                          ║
║             • Ad tag check + install  ← 🔴 NO dependency, sabse pehle                   ║
║             • ASIN collect + PATCH    ← Create ke baad                                  ║
║             • Conversion events       ← ad tag ke baad                                  ║
║   Branch C: 💳 Credit check                                                            ║
║             🔁 insufficient → top-up                                                    ║
║                                                                                       ║
║  ─────────── 🔗 JOIN — sab branches ka intezaar ───────────                            ║
║   💰 ACTIVATE  (the single spend action)                                                ║
║      ⚠ Agent batata hai kya adhoora hai (e.g. 15s creative pending)                     ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

---

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | 🔴🔴 **§3 flow structure** | Linear chain → **sequential head + parallel tail + join at Activate** |
| 2 | 🔴 **Step 11 intro** | ❌ *"Both now sit here, **after creative approval**"* — **hatao** |
| 3 | 🔴 **Step 11** | ➕ Note: **kram zaroori nahi** · creative se pehle bhi ho sakta hai |
| 4 | 🔴🔴 ➕ **Naya section** | **"Activation prerequisites"** — teen branches, join at Activate |
| 5 | 🔴 ➕ **Naya section** | **"Lead times"** — kaunsa kaam sabse lamba (ad tag), kyun jaldi shuru karo |
| 6 | 🔴 **Tracking setup ko todo** | Ad tag (no dep) · ASIN+PATCH (Create ke baad) · conversions (tag ke baad) |
| 7 | 🔴🔴 ➕ **`ActivationPrerequisitesSchema`** | Naya schema — per-branch completion |
| 8 | 🔴 **`current_stage`** | Ek string parallel states express nahi kar sakti → `current_focus` + prerequisites map |
| 9 | ✅ **Step 9 partial-upload gap** | `creative_uploaded: dict[str, bool]` isko bhi cover kar deta hai |
| 10 | 🔴 **§6 state machine** | Parallel branches + join node dikhao — line nahi |
| 11 | **Loops** | Branch-local mark karo · duration-mismatch ko **cross-branch** |
| 12 | 🔴 **Agent behaviour** | *"Ab ye karo"* → **"ye bacha hai, kisi bhi kram me"** + lead-time salah |
| 13 | ⚠ **Basil ka canvas** | Post-create UI ek **checklist** hona chahiye, linear stage nahi |
| 14 | ⚠ **Mera suggestion** | Ad tag check **session ke shuru me**? (David se confirm) |

---

## ✍️ DOCUMENT NOTE (draft)

> **📝 REVIEW NOTE 27 — The tail of the flow is unordered; tracking is not gated on creatives**
>
> **David's comment:** *"could be done before creatives if they are no available yet - no order necessary"*
>
> This step's introduction states that ASIN validation and ad-tag conversions *"now sit here, **after creative approval** and before tracking is attached."* **That ordering is not necessary** — and putting it last is actively harmful.
>
> ### The document placed the longest-lead-time task last
>
> | Task | Typical duration | Depends on |
> |---|---|---|
> | Plan (Basics → Forecast) | Minutes | The agent |
> | Finalise and create | Seconds | One trader action |
> | Creative upload | **Days** | The agency producing the video |
> | Platform approval | **24–48 hours** | The channels — external |
> | 🔴 **Ad tag installation** | **Days to weeks** | The **advertiser's development team** |
> | Credit top-up | Minutes to hours | Finance |
>
> **The ad tag is the longest task in the flow, depends on a third team, and its consequence of being late is irreversible** — this step's own warning says *"tracking only records activity after it goes live."* Data before installation is permanently lost.
>
> Placing it last maximises the chance it is rushed or skipped. David's comment is not only about flexibility; it **reduces a real risk.**
>
> ### The flow model changes: a chain becomes a set of prerequisites
>
> ```
> ❌ As written — a linear chain, each step gating the next
>    Create → Creative → Platform approval → Tracking → Credit → Activate
>    If the creative is delayed, tracking is blocked — despite having
>    no relationship to it.
>
> ✅ Corrected — three independent branches joining at activation
>    Create ──┬──→ Creative upload ──→ Platform approval ──┐
>             ├──→ Tracking setup ─────────────────────────┤──→ 💰 Activate
>             └──→ Credit check ──────────────────────────┘
> ```
>
> **The real dependencies, traced:**
>
> | Dependency | Genuine? |
> |---|---|
> | Basics → Inventory → Targeting → Budget split → Forecast → Finalise → Create | ✅ Each genuinely requires the previous |
> | Create → ASIN patch | ✅ Needs the strategy ID (Note 17) |
> | Creative upload → Platform approval | ✅ Nothing to review until uploaded |
> | Create → Credit check | ❌ Credit is entirely independent |
> | **Tracking ↔ Creative** | ❌ **No relationship whatsoever** |
> | Everything → Activate | ✅ Activation is a **join** |
>
> ### Tracking setup itself splits into three, with different dependencies
>
> | Sub-task | Depends on | Earliest possible |
> |---|---|---|
> | **Ad tag installation** | Nothing — the tag lives on the advertiser's own site | 🔴 **Immediately** |
> | ASIN collection and `PATCH` | The strategy must exist | After Create |
> | Conversion event selection | The ad tag must exist | After the tag |
>
> **⚠ A suggestion going beyond David's comment:** since ad-tag installation has *no* dependency and the longest lead time, the **check** for whether a tag exists could run at the very start of the session — alongside loading advertiser defaults (Note 13). If the advertiser has no tag and needs one, that is a multi-day dependency the trader should learn on day one, not at the end. *This is an extension of David's lead-time logic, not something he stated — to confirm.*
>
> ### 🔴 `current_stage` cannot express this
>
> `PlanningAgentState.current_stage: str` drives the adaptive canvas. **Once three branches are in flight, there is no single stage** — the creative may be awaiting platform approval while tracking awaits a tag and credit is already settled. One string cannot represent that.
>
> ```python
> # Was
> current_stage: str
>
> # Needs
> current_focus: str                        # what the trader is working on now
> activation_prerequisites: dict            # what remains outstanding
> ```
>
> ```python
> class ActivationPrerequisitesSchema(BaseModel):
>     """➕ NEW — these run independently; activation joins them"""
>     creative_uploaded: dict[str, bool] = Field(default_factory=dict)
>     # per duration: {"30": True, "15": False}
>     creative_approved: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
>     # per channel — Note 26
>     ad_tag_registered: Optional[bool] = None
>     asins_attached: bool = False
>     conversions_selected: bool = False
>     tracking_skipped: bool = False        # explicitly declined by the trader
>     credit_sufficient: Optional[bool] = None
>
>     @property
>     def outstanding(self) -> list[str]: ...
>     @property
>     def ready_to_activate(self) -> bool: ...
> ```
>
> **A side benefit:** making `creative_uploaded` a per-duration map also closes the gap flagged at the Upload Creative step — *"multiple durations, partial upload is not covered."* One change, two problems.
>
> ### Loops become branch-local, with one exception
>
> | Loop | Scope |
> |---|---|
> | Creative rejected → re-upload | **Within Branch A** — other branches unaffected |
> | Credit insufficient → top-up | **Within Branch C** |
> | **Duration mismatch → re-confirm the plan** | 🔴 **Cross-branch** — it returns upstream of all three, because the plan's economics changed |
>
> Previously a rejection anywhere stalled the whole chain. Now only its own branch stalls.
>
> ### Agent behaviour: report what is outstanding, not what is next
>
> ```
> Agent: "✅ Strategy VMA2026412 created.
>
>         Three things remain before activation. They're independent —
>         any order:
>
>         📹 CREATIVE   30s ⬜ not uploaded · 15s ⬜ not uploaded
>                       Platform approval follows upload — 24–48 hours
>         📊 TRACKING   Ad tag ⬜ not registered · ASINs ⬜ not collected
>         💳 CREDIT     £7,500 available, £10,000 needed
>
>         I'd start with the ad tag. It's your development team's work,
>         it takes the longest, and if it's installed after the campaign
>         starts, the data before that point is lost permanently.
>
>         It can run in parallel while you wait for the creative.
>
>         Which would you like to work on?"
> ```
>
> The lead-time recommendation matters: it is the agent contributing judgement rather than sequencing steps.
>
> ### Flow structure across three comments
>
> | | Steps | Structure | Loops | Interrupts |
> |---|---|---|---|---|
> | v2.0 as written | 13 | Rigid chain | 5 | 2 |
> | After Notes 5, 23, 27 | **~9 sequential + 3 parallel** | **Head + branches + join** | 4 *(one branch-local)* | **1** — platform approval only |

## 💬 REPLY DRAFT

> Agreed, and this is a bigger correction than the wording suggests.
>
> **The document explicitly put tracking after creative approval** — *"both now sit here, after creative approval"* — and there's no dependency between them at all. A delayed creative shouldn't block ad-tag work.
>
> **The part I'd got backwards: I put the longest-lead-time task last.** The ad tag needs the advertiser's development team, takes days or weeks, and this step's own warning says tracking only records activity *after* the tag goes live — so data before that is lost permanently. Putting it at the end of the sequence maximises the chance it gets rushed or skipped. Your comment isn't just about flexibility; it reduces a real risk.
>
> **So the tail of the flow becomes three independent branches joining at activation** rather than a chain: creative → platform approval, tracking, and credit. Tracing the real dependencies, only three post-create links are genuine — the ASIN patch needs the strategy ID, platform approval needs an uploaded creative, and activation needs all of it. Credit and tracking depend on nothing else.
>
> **Tracking itself splits three ways.** Ad-tag installation has *no* dependency — the tag lives on the advertiser's own site. ASIN collection and the patch need the strategy. Conversion selection needs the tag. So they don't even move as one unit.
>
> **One thing that breaks, and it affects Basil:** `current_stage` is a single string driving the adaptive canvas. With three branches in flight there is no single stage — creative awaiting approval, tracking awaiting a tag, credit already settled. I'll split it into `current_focus` plus an `activation_prerequisites` map. Making the creative side a per-duration map also closes a gap I'd flagged separately — partial upload across multiple durations.
>
> The agent's behaviour changes too: instead of *"now do X"* it reports what's outstanding and recommends starting with the ad tag, since that's the long pole.
>
> **One suggestion beyond your comment:** since the ad-tag *check* has no dependency at all, could it run at the very start of the session, alongside loading the advertiser defaults? If an advertiser has no tag and needs one, that's a multi-day dependency the trader should hear about on day one rather than at the end. Happy to leave it where it is if you'd rather not front-load it.

## ❓ David se poochhne wale sawaal
| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | Ad tag **check** session ke shuru me ho sakta hai? (lead-time ke liye) | Mera suggestion — confirm chahiye |
| 2 | Creative upload ko strategy ID chahiye, ya wo bhi Create se pehle ho sakta hai? | Branch A ka dependency |
| 3 | Trader tracking ko **explicitly skip** kar sakta hai (bina conversion tracking chalao)? | `tracking_skipped` field ke liye |

## 🏷️ Nichod
> **David keh raha hai:** *"Tracking setup creative se pehle bhi ho sakta hai — agar creative abhi taiyar nahi hai. Kram ki koi zaroorat nahi hai."*

**Severity: 🔴 HIGH** — kyunki:
- 🔴🔴 **Flow ka model badalta hai** — linear chain se **parallel branches + join**
- 🔴 **Document ne sabse lamba kaam (ad tag) aakhir me rakha** — ek asli risk
- 🔴 **`current_stage` toot jaata hai** — Basil ke canvas par direct impact
- 🔴 **Naya schema chahiye** — `ActivationPrerequisitesSchema`
- ✅ **Ek purana gap band** ho jaata hai (partial creative upload)
- 🔴 **Tracking setup khud teen hisson me** bat jaata hai

---
---

# 🗨️ COMMENT #28 — "No, they can be updated on the strategy after creation" 🎉 AAKHRI

## 📍 Location
| | |
|---|---|
| **Section** | `Step 11: Tracking Setup` → ⚠ **Open question (repeated from Step 1)** |
| **Highlighted** | **"Confirm with client"** |
| **Poora OQ** | *"⚠ Open question (repeated from Step 1): since `product_location` and `asin_numbers` are fields in `POST /strategies/` (called at Step 8), they may need to be collected before Step 8 and only the ad-tag check moves here. **Confirm with client.**"* |

## 💬 David ne exactly kya likha
> *"**no** they can be **updated on the strategy after creation**"*

---

## 🎉 Document ke SABSE BADE open question ka SEEDHA jawab
```
Ye sawaal document me DO BAAR likha gaya tha (page 8 aur page 18).
v2.0 ka sabse zyada dohraya gaya ⚠ tha.

Ab David ne SEEDHA jawab de diya: "NO."
```

### Is ek sawaal ka poora safar
```
╔══════════════════════════════════════════════════════════════════════════╗
║  STAGE 1 — v2.0 ne sawaal uthaya (DO BAAR)                                ║
║    "ASIN Step 8 me chahiye par Step 11 me collect ho rahi —               ║
║     Option A (patch later) ya Option B (early rakho)? Confirm karo."      ║
║                                                                          ║
║  STAGE 2 — Maine Option B recommend kiya                                  ║
║    ❌ GALAT — ASIN ko Step 1 me rakhne ka suggestion diya                  ║
║                                                                          ║
║  STAGE 3 — #16 + #17 (David)                                             ║
║    "selling location can leave out" + "ASINs comes later"                 ║
║    → Option A IMPLIED · maine OQ-1 RESOLVED mark kiya                     ║
║    → Aur `product_asins: []` example ko SABOOT bataya                     ║
║                                                                          ║
║  STAGE 4 — #24 (David)                                                   ║
║    "probably simple-strategies endpoint"                                  ║
║    ⚠ Mera SABOOT kamzor — wo galat endpoint ka example tha                 ║
║                                                                          ║
║  STAGE 5 — #28 (AAKHRI) 🎉                                               ║
║    "no they can be updated on the strategy after creation"                ║
║    ✅ SEEDHA, EXPLICIT jawab — Option A                                   ║
║    ✅ Aur MECHANISM bhi confirm — "update after creation"                  ║
║                                                                          ║
║  🔴 NATEEJA: Ab mere kamzor saboot ki ZAROORAT HI NAHI —                  ║
║     David ne khud bata diya. AUTHORITY STATEMENT > INFERENCE.              ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🔴🔴 Ek BADA insight chhupa hai — "Strategy MUTABLE hai"
```
David ke shabd dhyan se padho:
  "they can be UPDATED ON THE STRATEGY AFTER CREATION"
                       ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

Ye sirf ASIN ke baare me nahi — ye ek GENERAL capability hai:
  🔴 STRATEGY CREATE HONE KE BAAD BHI BADLI JA SAKTI HAI
```

### 🔴 Aur yahi wo cheez hai jo **#27 ko possible banati hai!**
```
╔══════════════════════════════════════════════════════════════════════════╗
║  #27 ne kaha:  "tail parallel hai — creative, tracking, credit           ║
║                 swatantra hain"                                          ║
║                                                                          ║
║  🔴 PAR RUKO — WO KAISE POSSIBLE HAI?                                    ║
║     Agar Create ke waqt SAB KUCH chahiye, to parallel kaise honge?        ║
║     Sab kuch Create se PEHLE ready hona padta!                            ║
║                                                                          ║
║  #28 ka jawab:  "updated on the strategy after creation"                  ║
║                                                                          ║
║  ✅ YAHI MECHANISM HAI JO #27 KI ARCHITECTURE KO CHALATA HAI!             ║
╚══════════════════════════════════════════════════════════════════════════╝

→ #27 ne ARCHITECTURE batayi · #28 ne MECHANISM confirm kiya
→ Dono ek doosre ke bina adhoore hain

💡 Reply me ye likhna — dikhata hai ki tumne DO comments ko JODKAR dekha
```

---

## ✅ Naya pattern — "Create minimal, attach later"
```
╔══════════════════════════════════════════════════════════════════════════╗
║  FINALISE  →  CREATE (minimal)  →  attach in parallel  →  ACTIVATE        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Create ke waqt SIRF ye chahiye:                                         ║
║    ✅ name · flight dates · market · currency · durations                 ║
║    ✅ goal · kpi · budget                                                 ║
║    ✅ selected deals (channels)                                           ║
║    ✅ targeting (jo bhi apply hui)                                        ║
║                                                                          ║
║  Create ke BAAD attach hota hai:                                         ║
║    ⏭️ product_asins            (#17, #28)                                 ║
║    ⏭️ product_location          (#16, #28) — ya advertiser se aa jaaye     ║
║    ⏭️ ad_tag_conversions        (#28)                                     ║
║    ⏭️ selected_creatives        (Step 8 — pehle se aisa hi hai)            ║
║    ⏭️ creative approval status  (Step 9 — external se aata hai)            ║
║                                                                          ║
║  🔴 Strategy ek MUTABLE record hai activation tak — frozen artefact nahi  ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Aur ye "costless plan" idea ko poora karta hai
```
Document ka claim: "Steps 1-12 free, Step 13 hi spend"

Poora picture ab:
  • Plan banane tak — koi record nahi, sab state me
  • Create ke baad  — record hai, PAR mutable, aur kharch NAHI ho raha
  • Activate        — 💰 kharch shuru, aur ab record settle ho jaata hai

🔴 "created" status ka matlab: "record maujood hai, badla ja sakta hai,
   par kharch nahi ho raha"

→ Ye #23 ke status: "created" (draft nahi) ko support karta hai
→ Aur OQ-3 ka jawab dene me MADAD karta hai — par poora jawab nahi
```

---

## 🔴 Kya confirm hua, kya NAHI
```
✅ CONFIRM: Strategy creation ke BAAD update ki CAPABILITY exist karti hai

❌ CONFIRM NAHI: Us update ka ENDPOINT kya hai?

David ne kaha "updated on the strategy" — par kaise?
  • PATCH /api/strategies/{id}/            ?
  • PUT /api/strategies/{id}/              ?
  • POST /api/strategies/{id}/tracking/    ?
  • Ya simple-strategies ka koi variant?   ← #24 se juda!

🔴 #24 ne bataya CREATE endpoint bhi shayad `simple-strategies` hai —
   to UPDATE endpoint ka bhi CTV variant ho sakta hai

→ Ye ek NAYA sawaal nahi hai — #24 ke "CTV endpoint family" sawaal me
  ek AUR item add karta hai
```

---

## 🎉 AUR EK BADI BAAT — Document ke ⚠ MARKERS ne KAAM KIYA
```
v2.0 me PAANCH ⚠ Open Questions the:

  OQ-1  ASIN timing conflict              → ✅ #16, #17, #28 ne RESOLVE kiya
  OQ-2  Suggest endpoint response shape   → ✅ #20 ne RESOLVE kiya
  OQ-3  Created strategy ka status        → ⬜ khula
  OQ-4  3P creative review status in API  → ⬜ khula
  OQ-5  Simplified CTV forecast endpoint  → ⬜ khula, aur #24 ne widen kiya

╔══════════════════════════════════════════════════════════════════════════╗
║  🎉 DAVID NE DO ⚠ MARKERS PAR SEEDHA COMMENT KIYA:                        ║
║     #20 → OQ-2 par  ·  #28 → OQ-1 par                                    ║
║                                                                          ║
║  → ⚠ MARKERS NE REVIEWER KA DHYAN THEEK WAHIN KHEENCHA                    ║
║    JAHAN CLARITY KI ZAROORAT THI                                         ║
║                                                                          ║
║  💡 "Assume mat karo, FLAG karo" wali practice ka POORA VALIDATION:        ║
║     Agar assume kar liya hota —                                          ║
║       • OQ-1 par galat direction (Option B) me jaate                       ║
║       • OQ-2 par poora audience module galat shape me banta                 ║
║                                                                          ║
║  → 2 out of 5 resolve hue, aur DONO wahi jo BLOCKING the                  ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Reply me ZAROOR likhna — David ko dikhega ki ⚠ markers ka maksad tha
   aur wo kaam aaye. Aage bhi wo unhe respect karega.
```

---

## 🔧 Kya fix karna hai
| # | Jagah | Kya karna hai |
|---|---|---|
| 1 | 🎉 **OQ-1 (page 8, Step 1)** | ✅ **RESOLVED mark karo** |
| 2 | 🎉 **OQ-1 (page 18, Step 11)** | ✅ **RESOLVED mark karo** — dono jagah |
| 3 | ⚠ **Note 17 ka evidence** | Ab **zaroorat nahi** — David ka direct statement replace kar deta hai |
| 4 | 🔴 ➕ **Naya note** | **"Strategy is mutable after creation"** — general capability, sirf ASIN ka rule nahi |
| 5 | 🔴 ➕ **Naya note** | **#28 = #27 ka mechanism** — post-creation update hi parallel branches possible banata hai |
| 6 | 🔴 **Step 7 (Create) payload** | Minimal karo — `product_location`, `product_asins` **omit** |
| 7 | ➕ **Naya section** | **"Create minimal, attach later"** |
| 8 | ⚠ **Update endpoint** | Naam nahi pata → **#24 ke CTV endpoint family sawaal me add karo** |
| 9 | **§4 catalogue** | `PATCH /api/strategies/{id}/` → **capability confirmed, naam TBC** |
| 10 | **OQ-3 (created status)** | Isse madad milti hai (created = mutable, not spending) par poora jawab nahi |
| 11 | 🎉 **§8 Summary** | ➕ **2 of 5 ⚠ markers resolve hue** — practice ne kaam kiya |

## ✍️ DOCUMENT NOTE (draft)

> **📝 REVIEW NOTE 28 — ✅ RESOLVED: `product_location` and ASINs can be updated after creation**
>
> **David's comment on this document's own open question:** *"no they can be updated on the strategy after creation"*
>
> This answers the question raised **twice** in v2.0 — at Step 1 and repeated here — the most-repeated ⚠ marker in the document. **The answer is Option A: collect later and update.**
>
> ### The full history of this one question
>
> | Stage | What happened |
> |---|---|
> | v2.0 | Raised the question twice, with two options and *"Confirm with client"* |
> | This revision, initially | Leaned toward **Option B** — keep ASINs early. **Wrong** |
> | Notes 16, 17 | *"Can leave out"* and *"comes later"* — Option A **implied**; cited `product_asins: []` as supporting evidence |
> | Note 24 | Showed that evidence was for `POST /api/strategies/`, which may be the wrong endpoint — **the justification weakened** |
> | **Note 28** | **Direct, explicit confirmation.** The weakened evidence is no longer needed — the answer is stated by the client |
>
> ### 🔴 The larger point: the strategy is mutable after creation
>
> David's wording is general — *"they can be **updated on the strategy after creation**."* This is not a rule about ASINs; it is a **capability of the strategy record.**
>
> **And this is the mechanism that makes Review Note 27 possible.** Note 27 established that creative, tracking and credit are independent branches converging at activation — but that only works if the strategy does not need to be complete at creation. This comment confirms it does not.
>
> The two notes are complementary: **27 describes the architecture, 28 confirms the capability it rests on.**
>
> ### The resulting pattern: create minimal, attach later
>
> ```
> Finalise  →  Create (minimal)  →  attach in parallel  →  Activate
> ```
>
> | Required at creation | Attached after creation |
> |---|---|
> | Name · flight dates · market · currency · durations | `product_asins` — Notes 17, 28 |
> | Goal · KPI · budget | `product_location` — Notes 16, 28 *(or from the advertiser record)* |
> | Selected deals (channels) | `ad_tag_conversions` — Note 28 |
> | Targeting, as applied | `selected_creatives` and their approval statuses |
>
> **The strategy is therefore a mutable record until activation, not a frozen artefact.** That also completes the *"costless plan"* principle: after creation the record exists and can still be changed, and no spend has occurred. Activation is both the spend action and the point at which the plan settles.
>
> ### ⚠ What is confirmed, and what is not
>
> | | Status |
> |---|---|
> | Post-creation update **capability** | ✅ **Confirmed** |
> | The **endpoint** for it | ⚠ **Still unnamed** — `PATCH`, `PUT`, or a dedicated route? |
>
> Given Note 24, the update endpoint may also have a CTV-specific variant. **This is therefore not a new question — it is one more item in the CTV endpoint family question.**
>
> ### 🎉 Two of this document's five open questions are now resolved — and the ⚠ markers are why
>
> | # | Open question | Status |
> |---|---|---|
> | 1 | ASIN and `product_location` timing | ✅ **Resolved** — Notes 16, 17, 28 |
> | 2 | Suggest endpoint response shape | ✅ **Resolved** — Note 20 |
> | 3 | What status does a created strategy land in? | ⬜ Open *(this note helps: created means mutable and not spending)* |
> | 4 | Do channel creative review statuses surface in VOW's API? | ⬜ Open |
> | 5 | What is the simplified CTV forecast endpoint called? | ⬜ Open — and Note 24 widened it |
>
> **David commented directly on two of the five ⚠ markers** (Notes 20 and 28). The markers drew the reviewer's attention precisely where clarity was missing — and both resolved questions were **blocking** ones. Had either been assumed instead of flagged, the audience module would have been built against a response shape that does not exist, and the ASIN handling would have gone in the wrong direction.

## 💬 REPLY DRAFT

> Thank you — that settles the question I'd raised twice, and it's the one I most needed answered.
>
> **Recording the full path honestly:** I initially recommended the *other* option — keeping ASINs at Step 1. Your earlier comments (*"can leave out"*, *"comes later"*) pointed the other way, and I marked it resolved citing `"product_asins": []` from the create payload example as evidence. Your `simple-strategies` comment then showed that example was for a different endpoint, so the evidence didn't hold. **This comment makes the evidence unnecessary — you've answered it directly.**
>
> **The bigger thing in your wording:** *"they can be updated on the strategy after creation"* is general — it's a property of the strategy record, not a rule about ASINs. **And that's the mechanism that makes the parallel-branch structure work.** Your tracking comment established that creative, tracking and credit are independent and converge at activation — but that only holds if the strategy doesn't have to be complete at creation. This confirms it doesn't. The two comments fit together: one describes the shape, this one confirms what it rests on.
>
> So the pattern becomes **create minimal, attach later**: name, dates, market, budget, deals and targeting at creation; ASINs, selling location, conversions and creatives attached afterwards. The strategy is a mutable record until activation, which also makes the "costless plan" idea complete — the record exists, it can still change, and nothing has been spent.
>
> **One thing still open, and it folds into an existing question:** the update **capability** is confirmed but the **endpoint** isn't named — `PATCH`, `PUT`, or something dedicated. Given your `simple-strategies` comment, it may also have a CTV variant. So I'll add it to the CTV endpoint family question rather than raise it separately.
>
> **And a note on the ⚠ markers, since this is the last comment.** You answered two of the five open questions I'd flagged — this one and the `bundles` response shape. Both were blocking. If I'd assumed instead of flagging, the audience module would have been built against a response shape that doesn't exist, and the ASIN handling would have gone the wrong way. I'll keep marking uncertainty rather than resolving it silently.

## ❓ David se poochhne wale sawaal
| # | Sawaal | Kyun |
|---|---|---|
| 1 | Update ka **endpoint** kya hai — `PATCH`, `PUT`, ya dedicated? | #24 ke CTV endpoint family sawaal me add karo |
| 2 | Kya **budget** bhi create ke baad update ho sakta hai? | Agar haan, to #23 ka re-finalise loop chahiye hoga |

## 🏷️ Nichod
> **David keh raha hai:** *"Nahi — ASIN aur selling location Step 8 se pehle collect karne ki zaroorat nahi. Wo strategy banne ke BAAD update ho sakte hain."*

**Severity: 🟡 MEDIUM** naye kaam ke hisaab se (ye #16/#17 ka conclusion **confirm** karta hai).
**Par ✅ VALUE bahut HIGH:**
- Document ka **sabse dohraya gaya open question** solve
- Mera **kamzor evidence** ki zaroorat khatam
- 🔴 **#27 ki poori architecture isi capability par tiki hai** — **load-bearing** confirmation
- 🎉 Saabit hua ki **⚠ markers kaam karte hain**

---
---

# 🔁 CROSS-CUTTING THEMES
### Jaise-jaise comments aayenge, patterns yahan jama honge

| Theme | Comments | Kya pattern hai |
|---|---|---|
| 🔴 **THEME 1: FABRICATED TIDY CORRELATION** | **#1, #2** | Document ne ek saaf-suthra, symmetric rule **bana liya** jo padhne me logical lagta hai — par kisi ne verify nahi kiya |
| 🔴 **THEME 2: OVER-CONSTRAINING** | **#3, #4** | Zaroori bana diya jo asal me marzi ka tha. **Aur dono case me SCHEMA SAHI THA** — sirf prose/table galat |
| 🔴 **THEME 3: EMPTY FORM vs DEFAULT+REFINE** | **#5, #6, #7, #9, #13** | Khaali fields diye jab values **derive** ho sakti thi. David ka model document ke apne Principle #2 se behtar match karta hai |
| 🔴 **THEME 4: FIELD MATRICES SABSE KAMZOR HISSA** | **#3, #4, #6, #9, #12, #13** | Matrices v1.1.0 se copy hue aur document ke baaki hisson se **reconcile nahi kiye** |
| 🟡 **THEME 5: SCOPE ADD KIYA, FLOW NAHI SOCHA** | **#8** | v2.0 ne feature scope me daala (multi-market) par uska flow impact analyse nahi kiya |
| 🔴 **THEME 6: DATA MODEL ≠ INTERACTION/PRESENTATION** | **#7, #11, #13** | Document ek hi column me do-teen alag concerns mila deta hai (Required vs Asked · Data type vs UI widget · Optional vs pre-filled) |
| 🔴🔴 **THEME 7: DOCUMENT APNE HI LOGIC KO SUPPORT NAHI KARTA** | **#10, #12** | Repair loop ek target ka zikr karta hai jiska field nahi hai (#10) · Repair loop ek lever use karta hai jo CTV me invalid hai (#12) |
| 🟡 **THEME 8: NON-CTV LEFTOVERS** | **#6, #12, #14, #15** | v1.1.0 ke Display/open-auction concepts CTV document me reh gaye (`formats (all four)`, `base_bid`, `"Required for video"`) |
| 🔴🔴 **THEME 9: ADVERTISER ATTRIBUTES STRATEGY SCHEMA ME MILA DIYE** | **#9, #13, #15, #16, #22** | Jo values HAR CAMPAIGN me nahi badalti, wo advertiser ka attribute hain — par strategy schema me daali gayi. **3× explicitly confirmed** |
| 🔴 **THEME 10: LEVEL / TAXONOMY CONFUSION** | **#11, #14, #21, #22** | **4 baar** — do alag level ki cheezein ek me mila di. Ek consistent blind spot |
| 🔴🔴 **THEME 11: EK POORA STEP KI INTERACTION GALAT HAI** | **#5, #6, #18** | Ab tak comments FIELDS ke baare me the — ye teen POORE STEPS ka interaction model badalte hain |
| 🔴🔴 **THEME 12: API SHAPE *AUR ENDPOINT* MAAN LIYA, VERIFY NAHI KIYA** | **#20, #24** *(confirmed)*, #1, #2, #17 | §4 ke endpoints **aur** §4.2 ke examples — dono v1.1.0 ke **assumptions** the. **#24 ne escalate kiya: ab endpoint NAME bhi suspect hai** |
| 🟡 **THEME 8 EXTENDED: NON-CTV LEFTOVERS** | #6, #12, #14, #15, **#25** | Display-era fields CTV document me reh gaye — `base_bid`, `formats` 4-choices, *"Required for video"*, **`click_through_url` Required** |
| 🔴 **THEME 14: FIXED LIST LIKHI JAHAN LIST KHULI HAI** | **#26** *(confirmed)*, client's targeting note | Document ne closed lists likhi jo asal me open hain — channels, targeting types… aur shayad aur bhi |
| 🔴🔴 **THEME 15: SEQUENCE MAAN LI JAHAN DEPENDENCY NAHI THI** | **#27** | Document ne flow ko ek LINE ki tarah socha — par kuch cheezein **parallel** hoti hain. Aur sabse lamba kaam aakhir me rakha |

---

## 🔴🔴 THEME #15 ko detail me — "sequence vs dependency"

```
╔══════════════════════════════════════════════════════════════════════════╗
║  #27  →  Tracking ko creative ke baad rakha — koi dependency nahi thi     ║
║                                                                          ║
║  🔴 Ye THEME 11 ("poora step ka interaction galat") ka BHAAI hai:        ║
║     #5, #6, #18 → INTERACTION galat thi                                   ║
║     #27          → SEQUENCE galat thi                                     ║
║                                                                          ║
║  💡 SABAK: v2.0 ne UI wizard ki jagah agentic flow banaya — par phir     ║
║     bhi usko ek LINE ki tarah socha. Asli agentic flow me kuch cheezein   ║
║     PARALLEL hoti hain, aur kuch ka koi kram hi nahi hota.                ║
║                                                                          ║
║  ⚠ Aakhri comment (#28) padhte waqt POOCHHO:                             ║
║     "Kya main yahan ek SEQUENCE maan raha hun jahan asal me DEPENDENCY    ║
║      nahi hai?"                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 🔴 Flow structure ka poora safar — teen comments
```
v2.0 original:  13 rigid steps, seedhi line + 5 loops + 2 interrupts

  #5   →  Steps 4+5 MERGE           → 12 steps
  #23  →  Step 7 ka GATE hata       → ek loop edge kam, ek interrupt kam
  #27  →  Tail steps UNORDERED      → parallel branches + join

AB:  ~9 sequential + 3 parallel branches · join at Activate
     · 4 loops (ek branch-local, ek cross-branch) · 1 interrupt

🔴 Graph ka SHAPE hi badal gaya — Wajahat ke liye badi baat
```
| 🔵 **THEME 13: DESIGN BADAL GAYA — DOCUMENT PURANA HO GAYA** | **#23** | Team ne v2.0 ke **baad** faisla liya. Ye **correction nahi, NEWS hai** — reply ka tone alag hona chahiye |

---

## 🔵 THEME #13 ko detail me — "correction" vs "design change"

```
╔══════════════════════════════════════════════════════════════════════════╗
║  #23  →  "we simplified this" — team ne v2.0 ke BAAD faisla liya          ║
║                                                                          ║
║  🔴 Ye BAAKI 22 comments se BILKUL ALAG kism hai:                        ║
║     • Ye tumhari galti NAHI hai                                          ║
║     • Document GALAT nahi tha — PURANA ho gaya                            ║
║     • Reply ka tone: "good to know" — "sorry" NAHI                        ║
║                                                                          ║
║  💡 Baaki 5 comments me DHOONDHO:                                        ║
║     Kaunse "correction" hain aur kaunse "design change"?                  ║
║     Dono ka reply ALAG hona chahiye:                                     ║
║                                                                          ║
║     CORRECTION   → "sahi catch, main theek karta hun"                    ║
║     DESIGN CHANGE → "good to know, main update karta hun"                ║
║                                                                          ║
║  ⚠ AUR EK SABAK:                                                        ║
║     v2.0 ka status "For client verification" tha — yaani decisions        ║
║     BADALTE rehte hain. Document ko ek LIVING CONTRACT ki tarah treat     ║
║     karna padega, ek final artefact ki tarah nahi.                        ║
║     → Har section par "last confirmed: <date>" jaisa marker useful hoga   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🔴🔴 THEME #12 ko detail me — "API shape assumed, not verified"

```
╔══════════════════════════════════════════════════════════════════════════╗
║  §4.2 ke API examples ASSUMPTIONS the, verified contracts NAHI.           ║
║                                                                          ║
║  Ab tak jo mila:                                                         ║
║   #20  bundles.narrow/balanced/broad  →  ❌ SUPPORT NAHI HAI (CONFIRMED)  ║
║   #2   per-segment vcpm               →  ⚠ shayad galat model            ║
║   #1   deal built-in targeting        →  ⚠ pata nahi exist karta hai     ║
║   #17  product_asins: [] accepted     →  ⚠ example se inference          ║
║   §4   9 naye endpoints               →  ❌ koi spec hi nahi hai          ║
║   §2.4 bundles.broad vs WIDE          →  ✅ #20 ne khatam kar diya        ║
║                                                                          ║
║  🔴 EK "CONTRACT DOCUMENT" ke liye ye SERIOUS hai —                      ║
║     Wajahat aur Vishal in examples se code likhenge.                      ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 🔴 THEME 14 ko detail me — "fixed list vs open list"
```
╔══════════════════════════════════════════════════════════════════════════╗
║  Client ne kaha (Step 5 ka critical note):                                ║
║    "This targeting list FREQUENTLY CHANGES so it should be easy to add     ║
║     new targeting types" → config-driven, NOT hard-coded                   ║
║                                                                          ║
║  #26 ne WAHI principle CHANNELS par lagaya:                               ║
║    "not necessary netflix or disney - could be paramount or channel 4"     ║
║                                                                          ║
║  🔴 Yaani config-driven SIRF targeting ka rule nahi tha —                  ║
║     wo ek GENERAL PRINCIPLE hai.                                         ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KAHAN-KAHAN LAG SAKTA HAI — audit karna hai:                             ║
║    ✅ Targeting types         (client — CONFIRMED open)                    ║
║    ✅ Channels / providers    (#26 — CONFIRMED open)                      ║
║    🟡 Audience data sources   (#2 — Amazon 1P, 3P… aur?)                  ║
║    🟡 Deal types              (PG, Preferred, Private Auction… aur?)       ║
║    🟡 Inventory tiers         (teen… aur ho sakte hain?)                   ║
║    🟡 Creative durations      (10/15/20/30… aur?)                          ║
║    🟡 Currencies              (EUR/GBP/USD… aur markets aayenge to?)       ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 SAWAAL jo poore document par lagao:
   "Kya main yahan ek FIX LIST likh raha hun jo asal me KHULI hai?"
```

---

### 💡 FIX — har API example par ek verification marker lagao
```
✅ VERIFIED   — real API se check kiya gaya
⚠ ASSUMED    — abhi verify nahi hua
❌ INCORRECT  — real shape alag hai (jaise bundles)

→ Isse Wajahat/Vishal ko pata rahega ki kis example par bharosa karein
→ Aur kaunse pehle confirm karne padenge
```

### 💡 Reply me ye structural suggestion dena
Ye David ko dikhayega ki tumne problem ki **jad** pakadi hai, sirf ek example nahi:

> *"§4.2's examples came from v1.1.0 and were assumptions, not verified contracts — the `bundles` shape is the one that's now confirmed wrong, but the same applies to the per-segment `vcpm`, the deal targeting metadata, and the nine v2.0 endpoints that have no spec at all. I'm adding a verification marker to every example — VERIFIED / ASSUMED / INCORRECT — so Wajahat and Vishal know which ones they can build against."*

---

## 🔴🔴 THEME #11 ko detail me — "Poora step ka interaction galat"

```
╔══════════════════════════════════════════════════════════════════════════╗
║  TEEN STEPS ka interaction model badal gaya hai:                          ║
║                                                                          ║
║  #5   Step 4+5 → merge + "default lagao, phir refine"                     ║
║  #6   Step 1   → form se "summary-to-confirm"                             ║
║  #18  Step 2   → deals table se "agent auto-matches, sirf CPM dikhao"     ║
║                                                                          ║
║  🔴 Ye ab "field fixes" nahi hain — POORA REDESIGN hai.                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 💡 PREDICTION — baaki 10 comments me kahan aayega

**Document me `"Checkbox table"` aur table-based interaction kahan-kahan hai?**

| Step | Field | Type | 🔮 Risk |
|---|---|---|---|
| **Step 4** | Selected audience sets | *Checkbox table* (v1.1.0) → "3 profiles" (v2.0) | 🟡 v2.0 ne already thoda theek kiya (#5 ne poora kar diya) |
| **Step 9** | Selected assets | *Checkbox table* (v1.1.0) | 🔴 **ZYADA CHANCE** — v2.0 ne ise "Upload" kiya, par browse hataya hai |
| **Step 2** | Selected deals | Checkbox table | ✅ #18 ne cover kiya |
| **Step 3** | Split by inventory/duration | "Allocation (%)" | 🟡 Ye bhi manual entry hai — agent propose karta hai (theek hai) |
| **Step 6** | Reach curve | Chart | ✅ Read-only, theek hai |

**🔮 Sabse zyada chance: Step 9 (Creatives) aur Step 5 (Targeting).**
Wahan bhi "trader ko sab dikhao aur chunwao" wala model ho sakta hai.

**💡 Aage badhne se pehle ye check karo:** har step me poochho —
*"Kya ye interaction trader ke liye STRATEGIC hai, ya TECHNICAL plumbing hai?"*
Agar plumbing hai → wahan David ka comment aayega.
| **Absolute statements** — "choice" ko "fact" bana diya | #1 | Jahan trader ke paas option hai, document ne ek hi raasta likha |
| **Same galti kai jagah repeat** | #1 (§2.3 + Step 4) · #2 (§2.4 line + table + note) · #4 (table + §2.4 + Step 4 + §8 + state machine) | Ek concept kai jagah likha — sab theek karne padenge |
| **3P / non-Amazon ki adhoori samajh** | #1, #2 | Netflix/Disney ke rules Amazon se alag hain — document ne simplify kar diya |
| **Ek number vs ek range** | #2, #3 | Reality me kuch cheezein exact nahi hoti (mixed-source effective CPM · bina split ka CPM) — document ne single value maan liya |
| **Concepts jo alag kar diye jo alag nahi hain** | #5 | Audience aur Targeting ek hi sawaal ka jawab dete hain — do steps galat the |

---

## 🔴 THEME #1 ko detail me samjho — "Fabricated Tidy Correlation"

Ye **sabse important pattern** hai. Do comments, ek hi galti:

```
╔══════════════════════════════════════════════════════════════════════════╗
║  Comment #1: "3P = their own targeting"                                  ║
║              → Reality: CHOICE hai, do raaste hain                       ║
║              → Document ne ek option ko "sirf ek option" bana diya       ║
║                                                                          ║
║  Comment #2: "Narrow = higher fee, Wide = lower fee"                     ║
║              → Reality: fee data SOURCE par depend karti hai             ║
║              → Document ne ek correlation BANA LI jo exist nahi karti    ║
║                                                                          ║
║  DONO me same galti:                                                     ║
║  Document ne reality ko SIMPLIFY karke SYMMETRIC bana diya —             ║
║  kyunki wo padhne me accha lagta hai. Par VERIFY nahi kiya.              ║
║                                                                          ║
║  🔴 AUR YE DOCUMENT KE APNE PRINCIPLE #1 KA VIOLATION HAI:               ║
║     "Zero-Hallucination: NEVER invents... only populates values          ║
║      VERIFIED against the VOW database and REST APIs"                    ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 💡 Baaki 26 comments padhte waqt ye DHOONDHO

Har jagah check karo:
- Kahin document ne ek **"A = zyada, B = kam"** jaisa clean rule likha hai?
- Kahin **"X hamesha Y hota hai"** likha hai (bina "usually" / "may" ke)?
- Kahin ek **symmetric table** banaya hai jo bahut hi perfect lagta hai?

**Agar haan → wahan David ka comment aane ka chance zyada hai.**

### 💡 Reply me ye pattern MAANO

David ko dikhega ki tumne **pattern** samajh liya, sirf ek-ek comment nahi. Ek line kaafi hai:

> *"I can see the pattern in your comments — I'd simplified a few areas into clean symmetric rules that read well but weren't verified. I'll go through the document for the same class of assumption."*

---

## 🔴 THEME #2 ko detail me — "Over-constraining"

```
╔══════════════════════════════════════════════════════════════════════════╗
║  Comment #3: Budget split → Required  ❌ (asal me Optional)               ║
║  Comment #4: Audiences → Mandatory    ❌ (asal me Optional)               ║
║                                                                          ║
║  🔴 AUR SABSE DILCHASP BAAT:                                             ║
║     DONO CASE ME SCHEMA SAHI THA!                                        ║
║       budget_split: Optional[BudgetSplitSchema] = None       ← ✅         ║
║       audience_options: list[...] = Field(default_factory=list) ← ✅      ║
║                                                                          ║
║     Sirf PROSE aur FIELD TABLES me "Required/Mandatory" likha gaya.      ║
║     Yaani code sahi tha, likhawat galat thi.                             ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 💡 Baaki comments me DHOONDHO
**Har "Required" / "Mandatory" ko schema se cross-check karo.**
Agar schema `Optional` hai par table "Required" kehta hai — **ek to galat hai.**

Abhi tak jo mile:
| Field | Table kehta hai | Schema kehta hai | Kaun sahi |
|---|---|---|---|
| `budget_split` | Required | `Optional[...] = None` | **Schema** (#3) |
| `audience_options` | Required / Mandatory | `default_factory=list` | **Schema** (#4) |

---

## 🔴 THEME #3 ko detail me — "Empty form vs Default + Refine"

```
╔══════════════════════════════════════════════════════════════════════════╗
║  Comment #5: Document 5 KHAALI fields deta hai (Step 5).                 ║
║              David chahta hai: jo pata hai wo PEHLE SE BHAR DO,          ║
║              phir trader accept kare ya refine kare.                     ║
║                                                                          ║
║  🎯 Aur ye document ke apne Principle #2 se ZYADA match karta hai:        ║
║     "Self-Filling Form Paradigm — a form that fills itself in"           ║
║                                                                          ║
║  Ironic: document ne apna hi principle Step 5 me follow nahi kiya.       ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 💡 Baaki comments me DHOONDHO
**Kahan-kahan document trader se poochh raha hai jab wo cheez DERIVE ho sakti hai?**

Abhi tak jo dikha:
| Field | Document poochhta hai | Par derive ho sakta hai | Comment |
|---|---|---|---|
| Device type | Step 5 khaali field | CTV campaign hai → `Connected TV` | #5 |
| Country targeting | Step 5 khaali field | Step 1 ka `markets` | #5 |
| Product categories | Step 1 field | ASIN validation response me `product_category` aata hai! | #6 |
| Goal | Step 1 field (3 choices) | CTV = fixed `AWARENESS` | #6 |
| KPI | Step 1 field (6 choices) | Goal se derive (awareness → reach) | #6 |
| Formats | Step 1 field (4 choices) | CTV module = `streaming_tv` + `prime_video` | #6 |
| **Base bids** | Step 1 Required field | 🔴 **Ya bilkul chahiye hi nahi** (#12: fixed CPM deals) | #6, #12 |
| **Strategy name** | Step 1 Required field | **Generate karo** brief se | #7 |
| **Primary currency** | Step 1 Dropdown | **Market se** (`GB → GBP`) — §7.1 pehle se karta hai! | #9 |
| **Frequency cap** | Step 1 "Optional" (khaali) | 🏢 **Advertiser default se** — kabhi khaali nahi rehti | #13 |
| Selling location | Step 1 Radio | Brief se ("website" → `NOT_SOLD_ON_AMAZON`) | #6 |
| Flight dates | Step 1 Required | Brief se ("August" → Aug 1–31) | #6 |
| Market budgets | Step 1 Required | Brief se ("£10,000") | #6 |

### 🏢 Source types ab AATH ho gaye
```
  💬 ASKED       trader se poochhna padega
  🧠 INFERRED    brief ke text se
  ⚙️ DERIVED     doosre field se (market → currency)
  🏢 ADVERTISER  advertiser ke defaults/record se     ← #13, #15, #16
  🤖 GENERATED   agent ne banaya                      ← #7
  🔒 FIXED       CTV ke liye constant                 ← #14 (streaming_tv)
  🔌 API         API response se                      ← #15 (ASIN → category)
  ⏭️ LATER       baad ke step me collect hota hai      ← #16, #17
                 (Step 1 ke matrix me list hi nahi karna)

⚠ Aur "advertiser defaults" ek POORA MISSING CONCEPT hai —
  koi schema nahi, koi API nahi, koi state field nahi.
  🔴 DO BAAR confirm ho gaya: #13 (frequency cap) aur #15 (product categories)
```

### 🔴 THEME 9 ka TEST — baaki comments par lagao
```
╔══════════════════════════════════════════════════════════════════════════╗
║  SAWAAL: "Kya ye value HAR CAMPAIGN me badalti hai?"                     ║
║                                                                          ║
║  Agar NAHI badalti → wo ADVERTISER ka attribute hai, strategy ka nahi    ║
║                                                                          ║
║  Example:                                                                ║
║    BrightPath ki product category → hamesha "Education" ❌ nahi badalti   ║
║    BrightPath ka "Amazon par bechta hai?" → ❌ nahi badalta               ║
║    BrightPath ka frequency cap → ❌ nahi badalta (policy hai)             ║
║    BrightPath ka device policy → ❌ nahi badalta (brand policy) ← #22     ║
║    BrightPath ka budget → ✅ har campaign me alag                         ║
║    BrightPath ka flight dates → ✅ har campaign me alag                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 🔴 THEME 9 ka SUB-CONCEPT (#22 se naya) — "default" vs "constraint"
```
Sab advertiser values override nahi ho sakti:

  🏢 DEFAULT     → pre-filled, trader override kar sakta hai
                   (frequency cap — #13)
  🔒 CONSTRAINT  → pre-filled, trader override NAHI kar sakta (brand policy)
                   (device "CTV only" — #22?)

🔴 Ye repair loop ke liye CRITICAL hai — agent ko pata hona chahiye ki
   kaunsi cheez wo relax kar sakta hai aur kaunsi nahi.

→ Schema me: AdvertiserSetting { value, is_locked, reason }
```

---

## 🔴 THEME 10 ko detail me — chaar baar level confusion
```
╔══════════════════════════════════════════════════════════════════════════╗
║  DOCUMENT NE CHAAR BAAR DO ALAG LEVEL KI CHEEZEIN MILA DI HAIN:            ║
║                                                                          ║
║   #11  data type   vs  UI widget          (Type column me "Table")        ║
║   #14  format      vs  provider           (formats me "prime_video")      ║
║   #21  buying scope vs delivery filter    (markets vs location)           ║
║   #22  format      vs  device             (streaming_tv vs Connected TV)  ║
║                                                                          ║
║  🔴 Ye ek CONSISTENT BLIND SPOT hai — ek pattern, chaar jagah.             ║
║                                                                          ║
║  💡 Baaki 6 comments padhte waqt POOCHHO:                                 ║
║     "Kya ye do cheezein ek hi LEVEL par hain, ya main unhe mila raha hun?"║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🔴 THEME #4 ko detail me — "Field matrices sabse kamzor hissa hain"

```
╔══════════════════════════════════════════════════════════════════════════╗
║  Ab PAANCH jagah field matrix galat nikla:                               ║
║                                                                          ║
║  #3  budget_split       table: Required    →  schema: Optional           ║
║  #4  audience_options   table: Mandatory   →  schema: Optional           ║
║  #9  primary_currency   table: Dropdown    →  §7.1: derived from market  ║
║  #6  formats            table: 4 choices   →  §2: CTV me 2 fixed        ║
║  #6  goal / kpi         table: 3/6 choices →  Step 1 text: fixed/scoped  ║
║                                                                          ║
║  🔴 WAJAH: Field matrices v1.1.0 se COPY hue. Document ke baaki hisse    ║
║     (schema §5, §7.1 parsing, §2 business logic) UPDATE ho gaye — par    ║
║     matrices purane reh gaye.                                            ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 🔴 Ab CHHE jagah field matrix galat nikla
| # | Field | Table kehta hai | Sach kya hai | Sach kahan likha hai |
|---|---|---|---|---|
| #3 | `budget_split` | Required | Optional | **Schema §5** me |
| #4 | `audience_options` | Required / Mandatory | Optional | **Schema §5** me |
| #9 | `primary_currency` | Dropdown, Required | Market se derive hoti hai | **§7.1 parsing** me |
| #6 | `formats` | Required (4 choices) | CTV ke liye fixed 2 | **§2 + enum comments** me |
| #6 | `goal`, `kpi` | Required (3/6 choices) | Fixed / scoped | **Step 1 ka apna text** me! |
| #12 | `base_bid` | Required | CTV me applicable nahi | **§2.3 deal types table** me |
| #13 | `frequency_cap` | Optional (khaali) | Advertiser default se bharta hai | **David ne bataya** (document me kahin nahi) |

### 💡 CHECKING TOOL — baaki 15 comments padhte waqt use karo

**Har field matrix row ko document ke 4 hisson se CROSS-CHECK karo:**

| Check | Sawaal |
|---|---|
| 1️⃣ **Schema (§5)** | Matrix "Required" kehta hai — schema me `Field(...)` hai ya `Optional`? |
| 2️⃣ **§7.1 parsing rules** | Ye value brief se derive hoti hai? Phir "Required/Dropdown" galat hai |
| 3️⃣ **§2 business logic** | Business rule kehta hai ye fixed hai? Phir "choices" galat hai |
| 4️⃣ **Us step ka apna text** | Text kuch aur kehta hai, table kuch aur? |

**Agar koi mismatch mile → wahan David ka comment aane ka chance zyada hai.**
Isse tum David se **pehle** galtiyan dhoondh sakte ho.

---

# 📋 MASTER ACTION LIST
### Sab comments samajhne ke baad ye poori list document me lagegi

## Schema changes
| # | Change | Comment |
|---|---|---|
| 1 | `TargetingSourceEnum` add karo (`AMAZON_DSP` / `INVENTORY_SOURCE`) | #1 |
| 2 | `SelectedDealSchema.targeting_source` add karo | #1 |
| 3 | `SelectedDealSchema.source_targeting_cpm_uplift` add karo | #1 |
| 4 | `SelectedDealSchema.built_in_targeting` add karo (agar visible hai) | #1 |
| 5 | 🔴 `AudienceDataSourceEnum` add karo (`AMAZON_1P` / `THIRD_PARTY` / `NONE`) | #2 |
| 6 | 🔴 `SelectedAudienceSetSchema.vcpm_fee` **HATAO** — fee segment-level par nahi hoti | #2 |
| 7 | 🔴 `SelectedAudienceSetSchema.data_source` add karo | #2 |
| 8 | 🔴 `AudienceFeeSchema` naya banao — per-source fees + effective CPM **range** | #2 |
| 9 | `SelectedAudienceSetSchema.effective_cpm` ko range/blended model me badlo | #2 |
| 10 | 🔴 `TargetingSchema` me **audience segments** add karo (audiences targeting ka hissa) | #5 |
| 11 | 🔴 `TargetingSchema` ko **config-driven** bana do (`selections: dict[str, list[str]]`) — Client + #5 dono ka requirement | #5 |
| 12 | ➕ `TargetingDefaultsSchema` — kaunse defaults lagte hain aur kahan se derive hote hain | #5 |
| 13 | ➕ `targeting_accepted_as_default: bool` — trader ne refine kiya ya accept kiya | #5 |
| 14 | 🔴 `BudgetSplitSchema.by_market` add karo (agar multi-market in scope) | #8 |
| 15 | ⚠ `markets: list[str]` — schema plural rakho, par M1 flow single-market ho | #8 |
| 16 | ➕ `strategy_name_generated: bool` — naam agent ne banaya ya trader ne diya | #7 |
| 17 | ➕ `field_sources: dict[str, str]` (ya per-field metadata) — kaunsa field kahan se aaya (ASKED/INFERRED/DERIVED/**ADVERTISER**/GENERATED/FIXED/API) | #6, #7, #9, #13 |
| 18 | 🔴 ➕ `kpi_target_value: Optional[int] = Field(None, ge=1, le=5)` — **MISSING FIELD** | #10 |
| 19 | ➕ Validation: `kpi_target_value` Required if `kpi_target_type == frequency` | #10 |
| 20 | ➕ Validation: `frequency_cap > kpi_target_value` (warna mathematically impossible) | #10 |
| 21 | 🔴 `MarketBudgetBidSchema.base_bid`: `str = Field(...)` → `Optional[str] = None` | #12 |
| 22 | 🔴🔴 ➕ `AdvertiserDefaultsSchema` — **poora naya schema** (frequency cap, currency, budget cap, content exclusions, approval threshold) | #13 |
| 23 | 🔴 ➕ `PlanningAgentState.advertiser_defaults: Optional[dict]` | #13 |
| 24 | ➕ `PlanningAgentState.kpi_target_value: Optional[int]` | #10 |
| 25 | `FormatEnum.PRIME_VIDEO` → annotate: *"not a format — provider, see SelectedDealSchema.provider"* | #14 |
| 26 | `FullStrategySchema.formats` → system constant `["streaming_tv"]` (field nahi) | #14 |
| 27 | 🔴 `AdvertiserDefaultsSchema` me ➕ `product_categories: list[int]` | #15 |
| 28 | 🔴 `AdvertiserDefaultsSchema` me ➕ `product_location: Optional[ProductLocationEnum]` | #16 |
| 29 | `FullStrategySchema.product_asins` → Step 8 par `[]` bhejo, Step 11 me patch | #17 |
| 30 | 🔴 `SelectedDealSchema` → ➕ `selection_method` (`AUTO_MATCHED`/`TRADER_SPECIFIED`) | #18 |
| 31 | 🔴 `SelectedDealSchema` → ➕ `matched_on: Optional[dict]` (matching criteria) | #18 |
| 32 | 🔴 `SelectedDealSchema` → ➕ `is_surfaced_to_trader: bool = False` | #18 |
| 33 | 🔴🔴 ➕ **`DealMatchCriteriaSchema`** — poora naya schema (market, duration, channel, genre, targeting, escape-hatch deal ID) | #18 |
| 34 | ➕ Step 2 field: `channel/provider` (strategic choice) · `ros_or_genre` · `specific_deal_id` | #18 |
| 35 | 🔴 `AudienceFeeSchema` — 3P portion par bhi Amazon 1P fee lag sakti hai (model widen karo) | #19 |
| 36 | 🔴 ➕ `AudienceBundleConstructionSchema` — grouping basis, nested flag, reach targets | #20 |
| 37 | `SelectedAudienceSetSchema` → ➕ `applies_to_providers: list[str]` (kaunse portion par lagi) | #19 |
| 38 | `TargetingSchema.defaults_applied` → ➕ location default (market country) record karo | #21 |
| 39 | 🔴🔴 ➕ **`AdvertiserSetting`** wrapper — `{value, is_locked, reason}` · sab advertiser defaults isme wrap karo | #22 |
| 40 | 🔴 `AdvertiserDefaultsSchema` → ➕ `device_types` (fallback: Connected TV only) | #22 |
| 41 | `TargetingSchema` → `mobile_environment` **Conditional** karo (sirf jab Mobile ∈ device_types) | #22 |
| 42 | 🔴 ➕ **`PlanStatusEnum`** (DRAFT/FINALISED) · approval states commented rakho (future) | #23 |
| 43 | 🔴 `FullStrategySchema` → ❌ `manager_required`, `rejection_reason` hatao · `approved_by/at` → **`finalised_by/at`** · `approval_status` → `plan_status` | #23 |
| 44 | ⚠ `ApprovalStatusEnum` **RAKHO** — Step 10 (platform approval) ko chahiye | #23 |
| 45 | `PlanningAgentState` → `approval_status/approved_by/approved_at` → `plan_status/finalised_by/finalised_at` | #23 |
| 46 | 🔴 `SelectedCreativeSchema.click_through_url` → `HttpUrl = Field(...)` → **`Optional[HttpUrl] = None`** | #25 |
| 47 | 🔴 `FullStrategySchema.creative_approval_status` → **`creative_approval_statuses: dict[str, ApprovalStatusEnum]`** · keys `selected_deals[].channel` se derive | #26 |
| 48 | 🔴 `SelectedDealSchema.provider` → **rename `channel`** (naming resolved) | #26 |
| 49 | 🔴 `ChannelTypeEnum` → **rename** (collision: `dsp`/`sponsored` vs channel names) | #26 |
| 50 | ⚠ Audit: kaunse enums **khule** hone chahiye (data sources · deal types · tiers · durations · currencies) | #26 |
| 51 | 🔴🔴 ➕ **`ActivationPrerequisitesSchema`** — per-branch completion tracking | #27 |
| 52 | 🔴 `PlanningAgentState.current_stage` → **`current_focus` + `activation_prerequisites`** | #27 |
| 53 | ✅ `creative_uploaded: dict[str, bool]` (per duration) — Step 9 ka partial-upload gap bhi band | #27 |

## Text / wording fixes
| # | Fix | Comment |
|---|---|---|
| 1 | §2.3 tier table — `Audiences` column me choice dikhao | #1 |
| 2 | Step 4 constraints — absolute phrasing theek karo | #1 |
| 3 | Step 5 — clarify ki targeting fields sirf Amazon portion par poori lagti hain | #1 |
| 4 | 🔴 §2.4 CHANGED line — "added fee consequence" claim **hatao** / re-write | #2 |
| 5 | 🔴 §2.4 table Row 1 — "higher audience fee" **hatao** (underdelivery risk rakho) | #2 |
| 6 | 🔴 §2.4 table Row 3 — "lower fee" **hatao** (less precision rakho) | #2 |
| 7 | 🔴 §2.4 ➕ NEW note — "more expensive per impression" **hatao** | #2 |
| 8 | §2.4 ➕ NEW note — "stacks on top" ✅ rakho, par **per data source** explain karo | #2 |
| 9 | Step 4 Effective CPM field — per-source + mixed-source range ke saath re-write | #2 |
| 10 | Step 3 — Split by inventory: **Required → Optional** | #3 |
| 11 | Step 3 — Split by duration: **Required → Optional** | #3 |
| 12 | Step 3 — ➕ naya paragraph: bina split ke kya hota hai (DSP auto-allocates, CPM unknown) | #3 |
| 13 | Comparison table row 4 — "mandatory" → **"optional"** | #4 |
| 14 | §2.4 ➕ NEW note — "audiences are mandatory" → **"optional"** | #4 |
| 15 | Step 4 — Audience options: **Required → Optional** · Chosen option: **Required → Optional** | #4 |
| 16 | Step 4 constraints — ❌ *"At least one audience set must be selected"* **hatao** | #4 |
| 17 | Step 4 — ➕ "No audience" ka case document karo (£0 fee, max reach, awareness ke liye often best) | #4 |
| 18 | §8 Summary of changes — 🔄 list se "audiences mandatory" **hatao** | #4 |
| 19 | State machine line 6 — `suggest_audiences (…mandatory)` → `(…optional)` | #4 |
| 20 | 🔴 Comparison table — Step 4 + Step 5 ko **ek row** me merge karo | #5 |
| 21 | 🔴 Step 4 ka poora content Step 5 me **merge** karo | #5 |
| 22 | ➕ Naya sub-section: **"Default targeting"** — kya default lagta hai, kahan se derive hota hai | #5 |
| 23 | ➕ Naya sub-section: **"Accept or refine"** interaction pattern | #5 |
| 24 | §8 Summary — step count **13 → 12**, aur merge document karo | #5 |
| 25 | 🔴🔴 **SAB field matrices me "Source" column add karo** (ASKED/INFERRED/DERIVED/GENERATED/FIXED/API) | #6, #7, #9 |
| 26 | Step 1 — `formats`: 4 choices → **FIXED** (streaming_tv + prime_video) | #6 |
| 27 | Step 1 — `goal`: 3 choices → **FIXED** = AWARENESS | #6 |
| 28 | Step 1 — `kpi`: 6 choices → **DERIVED** from goal (default reach) | #6 |
| 29 | Step 1 — `base_bids`: Required/asked → **DERIVED from rate card** | #6 |
| 30 | Step 1 — `strategy_name`: Source = **GENERATED** (editable) | #7 |
| 31 | Step 1 — `primary_currency`: Dropdown/Required → **DERIVED from market** | #9 |
| 32 | Step 1 — ➕ multi-market currency rule (account default → largest budget → ask) | #9 |
| 33 | §7.1 aur Step 1 matrix — currency ka contradiction **reconcile** karo | #9 |
| 34 | ➕ Naya section: **"Multi-market handling"** — kya repeat hota hai, kya shared | #8 |
| 35 | §4 API catalogue — ⚠ note: saare market-scoped APIs **singular** lete hain | #8 |
| 36 | Step 6 — ➕ note: cross-**market** reach ADD kar sakte ho (cross-**platform** nahi) | #8 |
| 37 | §7.1 — "UK and France" rule: agar M1 single-market hai to **future-scope** mark karo | #8 |
| 38 | Step 9 — ⚠ multi-market me creative language ka sawaal address karo | #8 |
| 39 | 🔴 Step 1 — ➕ naya row: `KPI target value` (Conditional, 1–5) | #10 |
| 40 | ➕ Naya sub-section: **frequency TARGET vs frequency CAP** ka farak | #10 |
| 41 | §7.1 — "insufficient frequency" ko **numerically define** karo | #10 |
| 42 | Step 1 — Market budgets Type: "Table" → `list[{market, budget}]` | #11 |
| 43 | 🔴🔴 **SAB matrices — `Type` column ko `Data type` + `Source` me todo** · UI widgets **hatao** | #11 |
| 44 | ➕ Document ke shuru me note: **ye DATA CONTRACT hai, UI SPEC nahi** | #11 |
| 45 | 🔴 Step 1 — Base bids: **Required → Not applicable for CTV** (ya Private Auction only) | #12 |
| 46 | ➕ Note: kyun base bid CTV me bekaar hai (fixed CPM deals) · §2.3 se link karo | #12 |
| 47 | 🔴 Step 1 — Frequency cap Source: **🏢 ADVERTISER default** | #13 |
| 48 | 🔴🔴 ➕ **Naya section: "Advertiser defaults"** — kaunse hain, kab load, override kaise | #13 |
| 49 | 🔴 §4 API catalogue — ➕ `GET /api/advertisers/{id}/defaults/` (ya asli endpoint) | #13 |
| 50 | Step 7 — "possibly budget-threshold-based" → shayad ye bhi advertiser default hai | #13 |
| 51 | Step 1 — Formats: Required → **system constant `["streaming_tv"]`** (ya row hatao) | #14 |
| 52 | Step 1 — Formats change note: "streaming_tv and prime_video only" → **"always streaming_tv"** | #14 |
| 53 | ➕ Naya note: **Format vs Provider** ka farak (level confusion) | #14 |
| 54 | v1.1.0 create payload example: `"formats": ["prime_video"]` → `["streaming_tv"]` | #14 |
| 55 | Step 1 — Product categories: "Required for video" → **Required** (CTV hamesha video) | #15 |
| 56 | Step 1 — Product categories Source: **🏢 ADVERTISER → 🧠 brief → 🔌 ASIN API** | #15 |
| 57 | §4.2 ASIN validation — ➕ note: response ka `product_category` auto-fill kar sakta hai | #15 |
| 58 | 🔴 Step 1 — **Selling location row HATAO** | #16 |
| 59 | 🔴 Step 1 — **Product ASINs row HATAO** | #17 |
| 60 | 🎉 **Open Question #1 (page 8) → RESOLVED mark karo** (Option A) | #16+#17 |
| 61 | 🎉 **Open Question #1 (page 18, repeated) → RESOLVED mark karo** | #16+#17 |
| 62 | Step 8 — ➕ note: `product_asins: []` bhejo · `product_location` advertiser se | #17 |
| 63 | Step 11 — ➕ `PATCH /api/strategies/{id}/` ka step add karo | #17 |
| 64 | 🔴 §4 API catalogue — ➕ `PATCH /api/strategies/{id}/` (**catalogue me hai hi nahi!**) | #17 |
| 65 | 🔴🔴 **REVISED STEP 1 MATRIX** poora replace karo (11 comments ka nateeja) | #6–#17 |
| 66 | 🔴 Step 2 — Selected deals Type: "Checkbox table" → `list[SelectedDealSchema]` | #18 (+#11) |
| 67 | 🔴 Step 2 — Selected deals Source: **🤖 AUTO-MATCHED** | #18 |
| 68 | 🔴🔴 Step 2 — ➕ naya sub-section: **"Deal matching, not deal selection"** | #18 |
| 69 | 🔴🔴 Step 2 — ➕ naya sub-section: **"What is surfaced vs internal"** | #18 |
| 70 | Step 2 — Curation section: ➕ note ki **ye pattern SAB tiers par lagta hai** | #18 |
| 71 | 🔴 §4 — `GET /api/deals/filter-properties/` ka **purpose badla** (filter UI → matching) | #18 |
| 72 | ⚠ **Naming resolve karo**: "channel" (David) vs "channels" (rate card) vs `provider` (schema) | #18 |
| 73 | ⚠ Step 2 — **PG commitment warning** surface karo (deal identity hide karte hue) | #18 (+#12) |
| 74 | 🔴🔴 **REVISED STEP 2 MATRIX** poora replace karo | #18 |
| 75 | 🔴 Step 4 constraint — *"Amazon audiences only apply to Amazon-owned"* **hatao** · choice likho | #19 |
| 76 | 🔴 §2.3 tier table — ➕ note: Audiences column ab tiers ko **differentiate nahi karta** | #19 |
| 77 | 🔴 §2.4 + Step 4 — **teen effective-CPM scenarios** ka comparison (3P par bhi fee) | #19 |
| 78 | ⚠ Note 1 ka explanation theek karo — *"identity nahi milti to impossible"* over-claim tha | #19 |
| 79 | Step 5 repair loop — ➕ nuance: 3P par widen kar sakte, verify nahi | #19 |
| 80 | ⚠ AMC audiences line — clarify ki AMC bhi 3P par lagti hai? | #19 |
| 81 | ✅ Step 4 ⚠ Open question — **RESOLVED mark karo** (bundles support nahi) | #20 |
| 82 | 🔴 §4.2 — `bundles` wala **poora example ❌ INCORRECT mark karo** ya hatao | #20 |
| 83 | 🔴 ➕ Naya sub-section: **"Bundle construction (agent-side)"** — grouping logic | #20 |
| 84 | 🔴 §2.4 — ➕ note: 3 profiles ek **agent-side construct** hain, API feature nahi | #20 |
| 85 | Step 4 — `Audience options` Source: **🤖 GENERATED (agent-side grouping)** | #20 |
| 86 | 🔴🔴 **§4.2 ke SAB examples par verification marker** lagao (VERIFIED/ASSUMED/INCORRECT) | #20 → Theme 12 |
| 87 | Targeting step — Location Source: **⚙️ DERIVED — market country** | #21 |
| 88 | 🔴 ➕ Naya note: **`markets` vs `location`** ka farak (buying scope vs delivery filter) | #21 |
| 89 | ➕ Location **hierarchy** document karo (country → region → city → postcode) | #21 |
| 90 | 🔴 **Targeting step ka poora DEFAULT TABLE** daalo (7 rows, sources ke saath) | #4,#5,#19,#20,#21 |
| 91 | ⚠ Content exclusions — advertiser brand-safety default ho sakta hai? confirm | #21 (+#13) |
| 92 | 🔴 Targeting step — Device type Source: **🏢 ADVERTISER** (fallback Connected TV only) | #22 |
| 93 | 🔴 **Note 21 ka default table THEEK karo** — Device: ~~FIXED~~ → ADVERTISER | #22 |
| 94 | 🔴🔴 ➕ **Naya note: "CTV as a format vs CTV as a device"** — `mobile_environment` iska proof | #22 |
| 95 | 🔴 **Note 12 repair loop levers** — ➕ column: *"can this lever be locked?"* | #22 |
| 96 | Step 5 — Mobile environment: Optional → **Conditional** | #22 |
| 97 | Step 6 (forecast) — ➕ note: CTV-only se inventory/reach kam, CPM zyada | #22 |
| 98 | ➕ **"Advertiser defaults" section me `default` vs `constraint`** ka farak likho | #22 |
| 99 | 🔴 **Step 7 ka naam**: "Plan Approval" → **"Finalise Plan"** | #23 |
| 100 | 🔴 Step 7 intro — client quote update (*"optionally routes to a manager"* ab galat) | #23 |
| 101 | 🔴 Step 7 field matrix — ❌ Manager required · ❌ Rejection reason · 🔄 Approval→Plan status | #23 |
| 102 | 🔴🔴 Step 7 Implementation — **`interrupt()` hatao**, par **node alag rakho (seam)** | #23 |
| 103 | 🔴 Step 7 — ❌ *"On rejection: return to Step 4"* **hatao** | #23 |
| 104 | 🔴 §6 state machine — `⏸ PLAN APPROVAL (interrupt)` → `finalise_plan (status change)` · rejection edge hatao | #23 |
| 105 | Step 9 duration mismatch — "re-approval" → **"re-confirmation"** | #23 |
| 106 | Step 12 budget reduction — "re-approve" → **"re-finalise"** | #23 |
| 107 | ⚠ ➕ **Naya note: separation of duties DELIBERATELY DEFERRED** | #23 |
| 108 | 🔴 ➕ **Naya note: M1 me asli `interrupt()` sirf Step 10** hai | #23 |
| 109 | ✅ Open question *"manager-approval threshold?"* → **MOOT mark karo** | #23 |
| 110 | §8 Summary — "plan approval" → "plan finalisation (simplified)" | #23 |
| 111 | ⚠ Step 8 — API calls: `POST /api/strategies/` → **`simple-strategies`** *(naam confirm)* | #24 |
| 112 | 🔴 §4 — ➕ **"CTV endpoint family"** section | #24 |
| 113 | ⚠ Note 17 ka evidence — saaf karo ki wo example **poore endpoint** ka tha | #24 |
| 114 | 🔴 §4 — `POST /api/strategies/` ko **⚠ ASSUMED** mark karo | #24 |
| 115 | 🔴 §4 vs Step 4 inconsistency — audience ke liye CTV endpoint, strategy ke liye nahi | #24 |
| 116 | 🔴 Step 9 — Click-through URL: **Required → Optional** · Change: ✅ Unchanged → 🔄 CHANGED | #25 |
| 117 | ✅ Step 9 flagged item #1 — **RESOLVED mark karo** | #25 |
| 118 | ➕ Note: kyun click-through URL optional hai (CTV me click nahi hota) | #25 |
| 119 | 🔴 Step 10 — teen hard-coded rows → **ek row: "Approval status per channel"** | #26 |
| 120 | 🔴 Step 10 — *"(if Netflix inventory)"* qualifiers **hatao** | #26 |
| 121 | 🔴 ➕ Note: **channel list KHULI hai** (Paramount+, Channel 4, ITVX, Sky, Hulu…) | #26 |
| 122 | 🔴 §2.3 vs Step 10 inconsistency — §2.3 kehta hai *"Netflix, Hulu, others"* | #26 |
| 123 | 🔴 ➕ Note: **config-driven principle channels par bhi** lagta hai, sirf targeting par nahi | #26 |
| 124 | ✅ Naming — poore document me `provider` → **`channel`** | #26 |
| 125 | 🔴🔴 **§3 flow structure** — linear chain → **sequential head + parallel tail + join** | #27 |
| 126 | 🔴 Step 11 intro — ❌ *"Both now sit here, **after creative approval**"* **hatao** | #27 |
| 127 | 🔴 Step 11 — ➕ note: **kram zaroori nahi**, creative se pehle bhi ho sakta hai | #27 |
| 128 | 🔴🔴 ➕ **Naya section: "Activation prerequisites"** — teen branches, join at Activate | #27 |
| 129 | 🔴 ➕ **Naya section: "Lead times"** — ad tag sabse lamba, jaldi shuru karo | #27 |
| 130 | 🔴 **Tracking setup ko todo** — ad tag (no dep) · ASIN+PATCH (Create ke baad) · conversions (tag ke baad) | #27 |
| 131 | 🔴 §6 state machine — **parallel branches + join node** dikhao, line nahi | #27 |
| 132 | Loops — branch-local mark karo · duration-mismatch ko **cross-branch** | #27 |
| 133 | ⚠ Mera suggestion — ad tag check **session ke shuru me**? (confirm chahiye) | #27 |

## Flow / architecture changes
| # | Change | Comment |
|---|---|---|
| 1 | Step 2 ↔ Step 5 coupling document karo (3P ke liye targeting deal-bound hai) | #1 |
| 2 | Agent behaviour: 3P select hone par targeting-source choice poochho | #1 |
| 3 | 🔴 Agent behaviour: audience recommendation ki **wajah badlo** — cost par nahi, reach/precision par | #2 |
| 4 | 🔴 Agent behaviour: mixed-source bundle par effective CPM **range** dikhao + "estimate" batao | #2 |
| 5 | Agent behaviour: budget split **skip karne ka option** do + consequence batao | #3 |
| 6 | Agent behaviour: **"no audience"** ko ek valid, recommended-for-awareness option ki tarah pesh karo | #4 |
| 7 | 🔴🔴 **Step 4 + Step 5 MERGE** — 13 steps se **12 steps** | #5 |
| 8 | 🔴 **Default-then-refine** pattern implement karo (khaali form nahi) | #5 |
| 9 | 🔴 State machine: `suggest_audiences` + `apply_targeting` → `propose_targeting` + `refine_targeting` | #5 |
| 10 | 🔴 Step 6 **repair loop CONDITIONAL** karo — bina audience ke "widen" ka matlab nahi | #5 |
| 11 | ⚠ Step order confirm karo: **Inventory → Targeting → Budget Split → Forecast** (audience fee accurate CPM ka input hai) | #3+#5 |
| 12 | 🔴🔴 **Step 1 = FORM se SUMMARY-TO-CONFIRM** — 14 fields infer/derive karo, phir dikhao | #6 |
| 13 | 🔴 Agent behaviour: strategy name generate + uniqueness auto-handle + trader ko dikhao | #7 |
| 14 | 🔴 Multi-market **scope decision** — M1 single ya multi? (recommendation: single, schema plural) | #8 |
| 15 | Agent behaviour: multi-market brief aane par kya bole — define karo | #8 |
| 16 | Agent behaviour: currency ko **assumption** ki tarah dikhao ("GBP — badalna hai?") | #9 |
| 17 | 🔴🔴 **REPAIR LOOP POORA RE-WRITE** — Action 2 (bid badhao) invalid hai, naye ordered levers chahiye | #12 (+#4, #5) |
| 18 | 🔴 Repair loop ke naye levers: targeting relax → audience extend → Exact→Similar → deals add → dates extend → budget → **imaandari se limit batao** | #12 |
| 19 | 🔴 State machine — repair loop ke edges badalne padenge (Wajahat ke liye critical) | #12 |
| 20 | 🔴 Flow ke shuru me **advertiser defaults LOAD** karo (naya node/step) | #13 |
| 21 | Agent behaviour: advertiser defaults dikhao + override ka option do | #13 |
| 22 | Agent behaviour: frequency target poochho (1–5 guide ke saath) jab KPI = frequency | #10 |
| 23 | Agent behaviour: target vs cap ka conflict **turant flag** karo | #10 (+#13) |
| 24 | Agent behaviour: product category advertiser default se dikhao, confirm maango | #15 |
| 25 | 🔴 Step 8 → Step 11 me **PATCH flow** add karo (ASIN attach karne ke liye) | #17 |
| 26 | 🔴 THEME 9 ka **audit** — poore document me advertiser-level attributes dhoondho | #9,#13,#15,#16 |
| 27 | 🔴🔴 **Step 2 ka poora interaction redesign** — deals table hatao, auto-matching lao | #18 |
| 28 | 🔴 State machine: `select_inventory` → **`match_inventory`** rename | #18 |
| 29 | 🔴 Basil ka canvas: Step 2 ka artifact badla — deals table nahi, **CPM summary** | #18 |
| 30 | 🔴 Agent behaviour: deal matching logic define karo (kai deals match karein to kya?) | #18 |
| 31 | Agent behaviour: escape hatch — trader ka deal ID accept karo aur use karo | #18 |
| 32 | 🔴 THEME 11 ka **audit** — har step me poochho: interaction STRATEGIC hai ya TECHNICAL? | #5,#6,#18 |
| 33 | 🔴 Agent behaviour: **teen** audience configurations compare karke dikhao (do nahi) | #19 |
| 34 | 🔴 Agent behaviour: 3P par audience widen kiya to **imaandari se batao ki verify nahi kar sakte** | #19 |
| 35 | 🔴🔴 **Bundle construction logic** likhni padegi — 3 profiles ab agent banata hai | #20 |
| 36 | Agent behaviour: location narrow karne par reach kam hoti hai — batao | #21 |
| 37 | 🔴 THEME 12 ka **audit** — §4.2 ke sab examples verify karo ya mark karo | #20 |
| 38 | 🔴 Agent behaviour: **locked settings 🔒 dikhao** + wajah batao ("brand policy") | #22 |
| 39 | 🔴 Agent behaviour: repair loop me batao **kaunsa lever chhoo nahi sake** aur kyun | #22 |
| 40 | Agent behaviour: CTV-only ka reach/CPM asar surface karo (trader ne ye choose nahi kiya) | #22 |
| 41 | 🔴 THEME 10 ka **audit** — poore document me level-confusion dhoondho (4 already mile) | #11,#14,#21,#22 |
| 42 | 🔴🔴 **Step 7 se `interrupt()` hatao** — sirf Step 10 me rakho (asli external gate) | #23 |
| 43 | 🔴 **Ek loop edge hatao** — plan rejection → Targeting | #23 |
| 44 | Do loops ka character badlo — "re-approval" → "re-confirmation" (Step 9, Step 12) | #23 |
| 45 | Agent behaviour: plan finalise ek **aam conversation turn** hai, koi wait nahi | #23 |
| 46 | ⚠ Step 7 ko **alag node rakho** (seam) — manager approval baad me aayega | #23 |
| 47 | Agent behaviour: click-through URL **poochho mat** — par trader de to accept karo | #25 |
| 48 | 🔴 Approval statuses ke keys **plan se derive** karo, hard-code nahi | #26 |
| 49 | 🔴 THEME 14 ka **audit** — poore document me fixed lists dhoondho jo khuli honi chahiye | #26 |
| 50 | 🔴 THEME 12 ka **audit escalate** — endpoints bhi verify karo, sirf response shapes nahi | #24 |
| 51 | 🔴🔴 **Flow: linear chain → parallel branches + join at Activate** | #27 |
| 52 | 🔴 Agent behaviour: *"ab ye karo"* → **"ye bacha hai, kisi bhi kram me"** + lead-time salah | #27 |
| 53 | 🔴 Basil ka canvas: post-create UI ek **checklist** hona chahiye, linear stage nahi | #27 |
| 54 | 🔴 THEME 15 ka **audit** — kahan sequence maan li jahan dependency nahi hai? | #27 |

## Questions for David / client
| # | Question | Comment |
|---|---|---|
| 1 | Amazon targeting on 3P — VCPM fee lagti hai ya device-level free hai? | #1 |
| 2 | Amazon targeting on 3P — device ke alawa kya support karta hai? | #1 |
| 3 | 3P pre-curated deals — built-in targeting deal metadata me visible hai? | #1 |
| 4 | 🔴 Suggest API per-segment `vcpm` deta hai — agar fee per-source hai to wo numbers kya hain? | #2 |
| 5 | Koi audience type **bina fee** ki bhi hai (basic demographic)? | #2 |
| 6 | Amazon 1P fee aur 3P fee ke **actual numbers** kya hain? Fixed ya type-dependent? | #2 |
| 7 | Mixed-source bundle me "matched in both" ka typical ratio kya hota hai? | #2 |
| 8 | 🔴 Targeting **Budget Split se pehle** aana chahiye? (audience fee accurate CPM ka input hai) | #3+#5 |
| 9 | 🔴 `GET /api/strategies/locations/{market}/` **postcodes** support karta hai, ya sirf cities/regions? | #5 |
| 10 | Agar koi audience nahi hai to repair loop kya kare — kaunsi targeting relax kare? | #5 |
| 11 | Bina budget split ke, Amazon DSP allocation kaise karta hai — koi rule hai ya pure auction-driven? | #3 |
| 12 | 🔴 **Multi-market M1 me chahiye ya M2 me?** (ye scope + effort ka faisla hai) | #8 |
| 13 | Multi-market me creative language per market chahiye? | #8 |
| 14 | Multi-market me currency ka rule kya ho — advertiser account default? | #9 |
| 15 | Advertiser ke account me ek default currency field hai? (document me nahi hai) | #9 |
| 16 | Base bid rate card se derive karna theek hai — ya trader ka input zaroori hai? | #6 |
| 17 | Strategy name ka naming convention koi standard hai jo follow karna chahiye? | #7 |
| 18 | "Insufficient frequency" ka matlab kya — target se kitna neeche = repair trigger? | #10 |
| 19 | 🔴 **CTV me Private Auction deals hote hain?** (saare examples Preferred hain — agar haan to base bid conditional rahega) | #12 |
| 20 | 🔴 **Frequency cap ke alawa kaunse advertiser defaults hain?** (currency? budget cap? content exclusions? approval threshold?) | #13 |
| 21 | Advertiser defaults fetch karne ka asli endpoint kya hai? | #13 |
| 22 | Frequency cap ka default weekly hai ya daily ya lifetime? | #13 (+#10) |
| 23 | Repair loop me jab koi lever na bache — tab agent ko kya karna chahiye? | #12 |
| 24 | 🔴 Amazon DSP API kaunsi **format values** accept karta hai — `streaming_tv` only ya `prime_video` bhi? | #14 |
| 25 | Advertiser record me **product category** kaise store hai — ek ya kai? | #15 |
| 26 | 🔴 `product_location` **advertiser record me** hai, ya Step 11 me poochhna hai? | #16 |
| 27 | 🔴 `PATCH /api/strategies/{id}/` endpoint exist karta hai? (catalogue me nahi hai) | #17 |
| 28 | `POST /strategies/` me `product_location` **Optional** hai? (ya advertiser se aayega) | #17 |
| 29 | 🔴🔴 **Deal ki built-in targeting structured metadata me hai?** — ab **BLOCKING** (auto-matching iske bina kaam nahi karegi) | #18 (+#1) |
| 30 | 🔴 PG deal auto-select karna chahiye ya kabhi nahi? Warning kaisa ho? | #18 (+#12) |
| 31 | ⚠ "channel" / "channels" / "provider" — kaunsa naam final? | #18 |
| 32 | Agar KAI deals match karein — agent kaise pick kare? (sabse sasta? sabse relevant?) | #18 |
| 33 | Agar KOI deal match na kare — agent kya kare? (failure protocol) | #18 |
| 34 | 🔴 Amazon audiences aur SSP targeting **DONO** same 3P deal par lag sakti hain, ya ek hi? | #19 |
| 35 | 🔴 **AMC audiences** bhi 3P par lagti hain? (Amazon audiences ki tarah) | #19 |
| 36 | 3P par Amazon audience ki capability kitni limited hai — exact list kya hai? | #19 (+#1) |
| 37 | 🔴🔴 **`POST /api/audience-sets/suggest/` ka ASLI response sample chahiye** — ye #2 aur #20 dono unblock karega | #20 |
| 38 | Grouping basis kya ho — relevance score, cumulative reach, ya data source? | #20 |
| 39 | `bundles` support **kab** aayega? ("not CURRENTLY" — future me hoga?) | #20 |
| 40 | Content exclusions advertiser ke brand-safety rules se default hone chahiye? | #21 (+#13), #22 |
| 41 | 🔴 **Device setting `default` (overridable) hai ya `constraint` (locked)?** | #22 |
| 42 | Agar advertiser ka koi device setting nahi — fallback kya? (Connected TV only, ya sab?) | #22 |
| 43 | Aur kaunse advertiser settings **LOCKED** ho sakti hain? | #22 |
| 44 | `finalised_by` / `finalised_at` record karne ki zaroorat hai? (audit ke liye) | #23 |
| 45 | Trader plan finalise karke **un-finalise** kar sakta hai? | #23 |
| 46 | Manager approval kab wapas aayega — M2? (seam kitna strong rakhna hai) | #23 |
| 47 | 🔴🔴 **Kya VOW me CTV ke liye ek alag ENDPOINT FAMILY hai? Poori list chahiye** — ye ek sawaal 6 chhote sawaal solve karega | #24 |
| 48 | `/api/simple-strategies/` ya `/api/strategies/simple/`? | #24 |
| 49 | `simple-strategies` ka payload shape kya hai? (`product_asins` optional hai?) | #24 |
| 50 | Approval status ke channel keys kaise aayenge — deal metadata se? | #26 |
| 51 | Aur kaunsi "fixed lists" asal me khuli hain? (data sources · deal types · tiers) | #26 |
| 52 | ⚠ Ad tag **check** session ke shuru me ho sakta hai? (lead-time ke liye) | #27 |
| 53 | Creative upload ko strategy ID chahiye, ya Create se pehle bhi ho sakta hai? | #27 |
| 54 | Trader tracking ko **explicitly skip** kar sakta hai (bina conversion tracking)? | #27 |

## Mastery file me fix karne wali cheezein
`full_strategy_schema_registery_mastery.md` me jo maine David ke comments se pehle likha tha, wo document follow karta hai — isliye kuch jagah **galat** hai:

| # | Kahan | Kya galat hai | Comment |
|---|---|---|---|
| 1 | Part 1.C — VCPM stacking section | "Narrow do tarah se buri — chhoti aur mehngi" | #2 |
| 2 | Part 4.4 — Audience profiles | "Narrow → higher fee, Wide → lower fee" | #2 |
| 3 | Part 5 Step 4 — Effective CPM table | "VCPM £1.74 (avg)", "£1.56 (avg)" — average nikalna galat | #2 |
| 4 | Part 12 — Worked example Turn 5 | Balanced ka VCPM £1.74 avg dikhaya | #2 |
| 5 | Part 4.3 / Step 4 — 3P audiences | "Netflix apni targeting deta hai" (choice nahi dikhayi) | #1 |
| 6 | Part 5 Step 3 — Budget Split field matrix | "Required when multiple inventories/durations" | #3 |
| 7 | Part 4.4 + Part 5 Step 4 — Audiences | "MANDATORY", "audience choose kiye bina aage nahi badh sakte" | #4 |
| 8 | Part 1.F — Audience section | "ab mandatory hai" | #4 |
| 9 | Part 5 Step 4/5 — do alag steps | Audience aur Targeting alag samjhaye gaye | #5 |
| 10 | Part 5.14 — flow ka naksha | 13 steps dikhaya, ab 12 honge | #5 |
| 11 | Part 12 — Worked example Turn 5/6 | Audience mandatory maan kar chalaya, default targeting nahi dikhaya | #4, #5 |
| 12 | Part 14 — Self-test Q | Kuch jawab purane model par based hain | #2, #4, #5 |
| 13 | Part 5 Step 1 — poora field matrix | 14 fields "Required" dikhaye, Source column nahi | #6, #7, #9 |
| 14 | Part 5 Step 1 — Primary currency | "Required, trader chunta hai" | #9 |
| 15 | Part 5 Step 1 — Base bid | "Required, trader batata hai" | #6 |
| 16 | Part 5 Step 1 — Strategy name | "Trader naam batata hai" | #7 |
| 17 | Part 5 Step 1 — Target markets (multi-market) | Multi-market ko normal maan kar samjhaya | #8 |
| 18 | Part 12 — Worked example Turn 1-2 | Agent ne naam aur base bid POOCHHA — dono derive ho sakte the | #6, #7 |
| 19 | Part 5 Step 1 — KPI section | KPI target value ka zikr nahi (missing field) | #10 |
| 20 | Part 1.C / Part 5 Step 1 — Frequency cap | Target vs cap ka farak nahi samjhaya | #10 |
| 21 | Part 5 Step 1 — Base bid ka poora explanation | "Base bid zaroori hai, budget vs bid ka farak" — CTV me bekaar hai | #12 |
| 22 | Part 5 Step 6 — Repair loop | Action 2 (bid £15→£30) dikhaya — CTV me invalid hai | #12 |
| 23 | Part 12 — Worked example Turn 1 | Sarah se base bid £32 poochha | #12 |
| 24 | Poori file — Advertiser defaults | Concept hi nahi hai (kyunki document me nahi tha) | #13 |
| 25 | Part 1.J — Source types | 8 source types ka concept add karna hai | #6-#17 |
| 26 | Part 1.B — Formats section | `prime_video` ko format ki tarah samjhaya — wo provider hai | #14 |
| 27 | Part 5 Step 1 — Product categories | "trader chunta hai" — advertiser default se aati hai | #15 |
| 28 | Part 5 Step 1 — Selling location | Step 1 ka field bataya — Step 11 me jaana chahiye | #16 |
| 29 | Part 5 Step 1 — Product ASINs (field #11) | Poora explanation Step 1 ke context me | #17 |
| 30 | Part 11 — Open Question #1 ka analysis | Maine **Option B** recommend kiya tha — David ne **Option A** chuna | #16+#17 |
| 31 | Part 12 — Worked example Turn 1-2 | Selling location aur product category poochhe/infer kiye | #15,#16 |
| 32 | Part 4.1 — Selling location section | Campaign-level bataya — advertiser-level hai | #16 |
| 33 | Part 5 Step 2 — poora section | Deals table dikhaya, trader ko checkbox tick karwaya | #18 |
| 34 | Part 12 — Worked example Turn 3 | Sarah ko deals ki table dikhayi aur usne chuna | #18 |
| 35 | Part 5 Step 2 — Genre upsell example | Deal names dikhaye — sirf content type + CPM dikhana chahiye | #18 |
| 36 | Part 1.E — Deal section | "Trader deal chunta hai" bataya — agent match karta hai | #18 |
| 37 | Part 5.14 — flow ka naksha | Step 2 me "deals chuno" likha — "agent match karta hai" hona chahiye | #18 |
| 38 | Part 4.3 / Part 5 Step 4 — 3P audiences | "Amazon audiences 3P par nahi lagti" — **lagti hain** | #19 |
| 39 | Part 1.F / Part 5 Step 4 — audience fee | Fee sirf Amazon portion par dikhayi — 3P par bhi lag sakti hai | #19 |
| 40 | Part 12 — Worked example Turn 5 | Netflix ke liye "Amazon audiences apply nahi hoti" likha | #19 |
| 41 | Part 6 §6.2 / Part 5 Step 4 — suggest API | `bundles` shape ko sach maan kar samjhaya — wo exist nahi karta | #20 |
| 42 | Part 1.F — 3 audience profiles | API feature bataya — **agent-side construct** hai | #20 |
| 43 | Part 5 Step 5 — Location field | "Optional, khaali" — market country par default hoti hai | #21 |
| 44 | Part 1.B — CTV section | "CTV = internet se juda TV" — format vs device ka farak nahi bataya | #22 |
| 45 | Part 5 Step 5 — Device type field | "CTV campaign hai to Connected TV" — advertiser se aata hai | #22 |
| 46 | Part 1.J / Part 5 Step 1 — Source types | ➕ `default` vs `constraint` ka farak add karna hai | #22 |
| 47 | Part 5 Step 7 — poora Plan Approval section | Manager approval, interrupt(), rejection loop — sab simplify hona hai | #23 |
| 48 | Part 1.J — `interrupt()` ka explanation | "Manager ka intezaar" example diya — ab wo Step 10 ka case hai | #23 |
| 49 | Part 12 — Worked example Step 7 | 19-ghante ka David approval wala scene — ab sirf trader confirm karega | #23 |
| 50 | Part 5.14 — flow naksha | ⏸ PLAN APPROVAL → finalise_plan · rejection edge hatao | #23 |
| 51 | Part 14 — Self-test Q25, Q26 | interrupt() aur "budget locked" wale jawab purane model par hain | #23 |
| 52 | Part 6 §4 — API catalogue | `POST /api/strategies/` ko sach maan kar samjhaya — `simple-strategies` ho sakta hai | #24 |
| 53 | Part 1.G / Part 5 Step 9 — Click-through URL | "Required hai, par CTV me click nahi hota — gap hai" → ab **Optional confirm** | #25 |
| 54 | Part 5 Step 10 — Platform approval | Teen channels (Amazon/Netflix/Disney) hard-code kiye | #26 |
| 55 | Part 1.A / Part 7.3 — `provider` word | Poore file me `provider` use kiya — ab **`channel`** hona chahiye | #26 |
| 56 | Part 12 — Worked example Step 10 | Amazon/Netflix/Disney ke teen statuses dikhaye — dict hona chahiye | #26 |
| 57 | Part 5.14 — flow naksha | Linear chain dikhaya — **parallel branches + join** hona chahiye | #27 |
| 58 | Part 5 Step 11 — Tracking setup | "creative approval ke baad" bataya — kram zaroori nahi | #27 |
| 59 | Part 12 — Worked example Steps 9–12 | Sequential chalaya (creative → approval → tracking → credit) | #27 |
| 60 | Part 8.4 — `current_stage` | Ek string bataya — parallel states express nahi kar sakti | #27 |
| 61 | Part 1.H — Ad tag warning | Warning hai par **lead-time** ka point nahi (sabse lamba kaam) | #27 |

*(Ye baad me theek karenge — pehle sab 28 comments samajhne ke baad, taaki ek hi baar me poora fix ho.)*

---

# 📈 RUNNING SUMMARY

| | Count |
|---|---|
| Comments samjhe | **28 / 28** 🎉 **COMPLETE** |
| 🔴🔴 VERY HIGH | 4 (#5, #6, #12, #18) |
| 🔴 HIGH | 16 (#1, #2, #4, #8, #10, #13, #15, #16, #19, #20, #22, #23, #24, #26, #27) |
| 🟡 MEDIUM | 9 (#3, #7, #9, #11, #14, #17, #21, #25, **#28**) |
| ✅ Open Questions RESOLVED | **4** (OQ-1 ASIN timing · OQ-2 bundles shape · click-through URL · naming "channel") |
| ✅ Open Questions **MOOT** | **1** (manager-approval threshold — de-scoped via #23) |
| 🔴 Open Questions **BLOCKING** | **3** (suggest response sample · deal targeting metadata · CTV endpoint family) |
| ⚠ Self-corrections | **4** (Note 1 explanation · OQ-1 recommendation · Note 21 device · Note 17 evidence) |
| 🎉 Mere flagged gaps jo review ne band kiye | **3** (click-through URL #25 · approval dict #26 · partial upload #27) |
| 🎉 v2.0 ke ⚠ markers jinpar David ne seedha jawab diya | **2 of 5** (#20 → OQ-2 · #28 → OQ-1) |
| Schema changes needed | **~53** |
| Text/wording fixes needed | **~145** |
| Flow/architecture changes | **~56** |
| Questions for David | **~56** |
| Mastery-file fixes | **~63** |

## 🔵 Comments ki KISM (naya breakdown)
| Kism | Count | Comments | Reply ka tone |
|---|---|---|---|
| **Correction** — galat tha | 19 | #1–#16, #19–#22 | *"Sahi catch, theek karta hun"* |
| **Missing** — kuch gayab tha | 2 | #10, #13 | *"Ye field/concept add kar raha hun"* |
| **Scope question** | 1 | #8 | *"Ye decision chahiye"* |
| **Agreement** | 1 | #17 | *"Confirmed, thanks"* |
| 🔵 **Design change** — news, correction nahi | **1** | **#23** | *"Good to know, update kar raha hun"* |

## 📍 Comments ka distribution
```
§2.3 Tier table          1 comment   (#1)
§2.4 Audience profiles   1 comment   (#2)
§3  Comparison table     3 comments  (#3, #4, #5)
Step 1 field matrix     12 comments  (#6–#17)  ← 🔴 SABSE ZYADA!
Step 2 field matrix      1 comment   (#18)     ← 🔴🔴 par SABSE BADA
Step 4 (Audiences)       2 comments  (#19, #20)
Step 5 (Targeting)       2 comments  (#21, #22)
Step 7 (Plan Approval)   1 comment   (#23)  ← 🔵 scope reduction
Step 8 (Create)          1 comment   (#24)
Step 9 (Creative)        1 comment   (#25)  ← ✅ mera flagged gap
Step 10 (Platform appr.) 1 comment   (#26)  ← ✅ mera fix confirm
Step 11 (Tracking)       2 comments  (#27, #28)  ← 🔴🔴 flow structure + OQ resolve
─────────────────────────────────────────────
Total                   28 comments  ✅ COMPLETE

📊 Distribution ka nateeja:
   • Step 1 field matrix par 12 comments (43%) — sabse kamzor hissa
   • Steps 12-13 (Credit/Activate) par ZERO comments
     → Ya wo theek the, ya David ne unhe review nahi kiya
     → ⚠ Poochhne layak: "Credit aur Activate steps theek lage?"

🔴 12 comments EK HI TABLE par (Step 1 matrix) → Theme #4 confirm
🔴 #18 akela poora Step 2 ka redesign maang raha hai → Theme #11
🔴 #19 + #21 dono "absolute/khaali" wale pattern ka repeat hain (#1, #5 ka)

📊 Teen saaf deliverables ban gaye hain:
   1. REVISED STEP 1 MATRIX      (11 comments ka nateeja)
   2. REVISED STEP 2 MATRIX      (#18 ka nateeja)
   3. TARGETING DEFAULT TABLE    (#4, #5, #19, #20, #21 ka nateeja)
```

## Sabse bade structural badlav (abhi tak)
0. 🔴🔴 **TEEN STEPS KA INTERACTION MODEL BADAL GAYA** — Step 1 (form→summary), Step 2 (table→auto-match), Step 4+5 (merge+default) — **ye ab field fixes nahi, POORA REDESIGN hai** (#5, #6, #18)
1. 🔴🔴 **REVISED STEP 1 MATRIX** — 11 comments ka ek saaf nateeja · 14 fields → 12 · **ZERO asked-and-required** (#6–#17)
2. 🔴🔴 **REVISED STEP 2 MATRIX** — deals table hatao, agent auto-match kare, sirf CPM surface karo (#18)
3. 🔴🔴 **REPAIR LOOP POORA COLLAPSE** — dono levers toot gaye, re-write chahiye (#4+#5+#12)
3. 🔴🔴 **Step 4 + Step 5 merge** → 13 steps se **12 steps** (#5)
4. 🔴🔴 **"Source" column** sab field matrices me — Required ≠ Asked · **8 source types** (#6,#7,#9,#13,#14,#15,#16,#17)
5. 🔴🔴 **"Type" column todo** — Data type + Source · UI widgets hatao (#11)
6. 🔴🔴 **ADVERTISER DEFAULTS ek poora missing concept** — schema, API, state · **2× confirmed** (#13, #15)
7. 🔴 **`kpi_target_value` missing field** — repair loop iske bina kaam nahi karta (#10)
8. 🔴 **Default-then-refine** pattern — khaali form ki jagah (#5, #13)
9. 🔴 **Audience fee model** poora badla — per data source, compound nahi (#2)
10. 🔴 **Effective CPM ek RANGE hai**, ek number nahi (mixed-source par) (#2)
11. 🔴 **Step 2 ↔ Targeting coupling** — 3P ke liye targeting deal-bound hai (#1)
12. 🔴 **Multi-market scope decision** — M1 single ya multi? (#8)
13. 🟡 **Format vs Provider** level fix — `prime_video` provider hai, format nahi (#14)
14. ✅ **Open Question #1 RESOLVED** — Option A (collect later + PATCH) (#16+#17)
15. ✅ **Open Question #2 RESOLVED** — `bundles` shape API me nahi hai (#20)
16. 🔴🔴 **3 audience profiles ek AGENT-SIDE construct** hain — grouping logic likhni hai (#20)
17. 🔴 **Amazon audiences 3P par bhi lagti hain** — tier table ka column matlab kho deta hai, effective CPM widen hota hai (#19)
18. 🔴🔴 **§4.2 ke API examples verify karne padenge** — ek confirmed galat nikla (#20 → Theme 12)
19. 🔴🔴 **"CTV format ≠ CTV device"** — conceptual fix, aur document ka apna `mobile_environment` field iska proof (#22)
20. 🔴 **`AdvertiserSetting` wrapper** — advertiser values me `default` vs `constraint` ka farak (#22)
21. 🔴 **Repair loop ke levers LOCK ho sakte hain** — advertiser policy se (#22)
22. 🔴🔴 **Step 7 se `interrupt()` hat gaya** — M1 me asli interrupt sirf **Step 10** bacha (#23)
23. 🔴 **Manager approval + rejection loop hat gaya** — separation of duties deliberately deferred (#23)
24. 🔴🔴 **CTV ENDPOINT FAMILY** — `POST /api/strategies/` shayad galat endpoint hai; poori family ka pata karna hai (#24)
25. 🔴 **Config-driven principle sirf targeting ka nahi tha** — channels par bhi lagta hai, aur shayad aur jagah (#26)
26. ✅ **Naming resolved** — `provider` → **`channel`** (#26)
27. 🔴🔴 **FLOW LINEAR CHAIN SE PARALLEL BRANCHES BAN GAYA** — teen swatantra branches, join at Activate (#27)
28. 🔴 **`current_stage` toot gaya** — parallel states ek string me nahi aa sakti (#27)
29. 🔴 **Ad tag sabse lamba kaam hai** — document ne use aakhir me rakha tha (#27)
30. ⚠ **Step order** shayad badlega — Targeting, Budget Split se pehle (#3+#5)

## 🎯 Ab tak ka sabse bada sabak

```
DAVID KE 13 COMMENTS TEEN KISM KE HAIN:

╔══════════════════════════════════════════════════════════════════════════╗
║  KISM 1 — "REALITY SIMPLIFY KAR DI" (2 comments)                         ║
║    #1  ek choice ko ek option bana diya                                  ║
║    #2  ek correlation bana li jo exist nahi karti                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 2 — "ZYADA POOCHH RAHA HAI / ZYADA BAANDH DIYA" (7 comments)       ║
║    #3  optional ko required bana diya                                    ║
║    #4  optional ko mandatory bana diya                                   ║
║    #5  khaali form diya, default nahi                                    ║
║    #6  14 sawaal poochhe jo derive ho sakte the                          ║
║    #7  naam poochha jo generate ho sakta tha                             ║
║    #9  currency poochhi jo market se nikalti hai                         ║
║    #13 frequency cap khaali dikhaya jo advertiser default se bharta hai   ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 3 — "KUCH GAYAB / GALAT HAI" (4 comments)                          ║
║    #10 kpi_target_value field GAYAB hai                                  ║
║    #11 Type column 4 kaam kar raha hai                                   ║
║    #12 base_bid CTV me bekaar hai (aur repair loop tod deta hai)          ║
║    #14 prime_video format nahi, provider hai (level galti)                ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 4 — "SCOPE SAWAAL" (1 comment)                                     ║
║    #8  multi-market support karenge?                                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 5 — "ADVERTISER KA ATTRIBUTE HAI, CAMPAIGN KA NAHI" (3)             ║
║    #15 product categories → advertiser default                           ║
║    #16 selling location → can leave out (advertiser-level)                ║
║    #22 device type → set at advertiser level (aur shayad LOCKED)          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 6 — "SEHMAT HUN" (1 comment)  ← 🎉 PEHLI BAAR                       ║
║    #17 product ASINs "comes later" — v2.0 ka change sahi tha              ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 7 — "POORA STEP KA INTERACTION GALAT HAI" (1)  ← 🔴🔴 SABSE BADA    ║
║    #18 deals table hatao — agent match kare, sirf CPM dikhao               ║
║        (#5 aur #6 bhi isi kism ke, par wo field-level se shuru hue)        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 8 — "API KA SHAPE GALAT MAAN LIYA" (1)                              ║
║    #20 bundles.narrow/balanced/broad support nahi hai                      ║
║        → §4.2 ke SAB examples ab suspect hain (Theme 12)                    ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 9 — "DESIGN BADAL GAYA" (1)  ← 🔵 CORRECTION NAHI                    ║
║    #23 plan approval simplify kar diya — manager approval hataya            ║
║        → Ye tumhari galti nahi. Document PURANA ho gaya, GALAT nahi tha.    ║
║        → Reply ka tone: "good to know", "sorry" nahi                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 10 — "HINT — VERIFY KARO" (1)  ← NAYI KISM                          ║
║    #24 "probably more likely simple-strategies endpoint"                    ║
║        → David bhi PAKKA nahi hai ("probably", aur comment "edited" hai)    ║
║        → Reply: "verify karunga", "badal diya" nahi                         ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM 11 — "TUMHARA FLAG/FIX SAHI THA" (2)  ← 🎉 NAYI KISM                ║
║    #25 click-through URL → maine gap flag kiya tha, David ne answer diya    ║
║    #26 approval status dict → maine fix propose kiya tha, David ne confirm  ║
║        → Reply: "ye maine flag kiya tha, confirm hone ka shukriya"          ║
╚══════════════════════════════════════════════════════════════════════════╝

## 🎉 EK ACHHI KHABAR — do baar tum SAHI the, David se PEHLE

```
#25  Click-through URL
     Maine likha tha: "either DSP mandates it, OR IT SHOULD BE OPTIONAL"
     David: "optional for streaming tv"  → doosra option sahi tha ✅

#26  Creative approval statuses
     Maine likha tha: "dict[str, ApprovalStatusEnum] hona chahiye,
                       ek single field nahi"
     David: "single status for each channel"  → bilkul wahi ✅

💡 REPLY ME YE MENTION KARNA — par ghamand se nahi, seedhe:
   "This was one I'd flagged as unresolved…" / "This validates the fix
    already proposed…"

→ Ye David ko dikhata hai ki tum sirf react nahi kar rahe — tum khud
  problems dhoondh rahe ho. Aur wahi ek reviewer sabse zyada value karta hai.
```

## ⚠ AUR EK BAAT — DO comments ne is tracker ko HI galat batayaib

```
#16 + #17  →  Maine OQ-1 ka Option B recommend kiya tha, David ne Option A chuna
#19        →  Maine Note 1 me over-claim kiya tha ("identity nahi milti to
              audience targeting impossible") — Amazon audiences 3P par kaam karti hain

💡 Reply me ye SAAF maanna hai. Do fayde:
   1. David ko dikhega ki tum apni galti pakadte ho, defend nahi karte
   2. Aur ye tumhare BAAKI analysis ko zyada credible banata hai
```

💡 REPLY ME YE PATTERN MAANNA — David ko dikhega ki tumne poora
   picture samajh liya, ek-ek comment nahi.
```

## 🔴 SABSE ZAROORI FINDING — Repair Loop TOOT GAYA

```
Teen comments milkar repair loop ko khatam kar dete hain:

  #4  audiences OPTIONAL     → "audience widen karo" lever kabhi kabhi nahi hota
  #5  audiences = targeting  → widen ka matlab badal gaya
  #12 base bid CTV me bekaar → "bid badhao" lever HAMESHA invalid hai

Worst case: koi audience nahi + Preferred deal (fixed CPM)
  → Repair loop ke paas ZERO levers hain

🔴 Ye Wajahat ke graph design ko SEEDHA affect karta hai.
   Usko repair loop ke naye edges pata hone chahiye.
   → Ye reply me flag karna zaroori hai.
```

---

## 🎯 17 comments ka NICHOD — ek jumle me

```
╔══════════════════════════════════════════════════════════════════════════╗
║  "Document ne reality ko SIMPLIFY kiya, cheezein ZAROORI banayi jo       ║
║   marzi ki thi, aur agent ko INSAAN se ZYADA POOCHHNE wala bana diya.   ║
║   Aur DO ASLI GAP hain: advertiser defaults ka poora concept gayab hai,  ║
║   aur repair loop ke levers CTV me kaam nahi karte.                       ║
║                                                                          ║
║   #18 se ek NAYA aur BADA sach nikla: teen steps ka INTERACTION MODEL    ║
║   hi galat hai — document ne WIZARD ko chat me daal diya, usko AGENT     ║
║   me nahi badla."                                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔮 AGE KE 10 COMMENTS KA ANUMAAN

Ab pattern itna saaf hai ki **predict kar sakte hain** kahan comments aayenge:

| Jagah | Kya risk hai | Kaunsa theme |
|---|---|---|
| **Step 9 (Creatives)** | v1.1.0 me "Checkbox table" tha (browse assets) — v2.0 ne upload kiya, par kya poora theek kiya? | #18 jaisa |
| **Step 5 (Targeting)** | 5 khaali optional fields | #5, #6 jaisa |
| **Step 6 (Predict reach)** | Repair loop ke levers | #12 jaisa (already toota hua) |
| **Step 7 (Plan approval)** | "possibly budget-threshold-based" — advertiser default? | #13, #15 jaisa |
| **Step 11 (Tracking)** | ASIN + ad tag — kitna trader se poochhna hai? | #6 jaisa |
| **Step 3 (Budget split)** | "Allocation (%)" manual entry | #18 jaisa? |
| **§5 Pydantic models** | `list[dict]` untyped fields, `matching_mode: str` | schema quality |
| **§6 State machine** | Repair loop edges, `interrupt()` | #12 ka nateeja |

**💡 Ye anumaan reply likhne me kaam aayega** — tum pehle se bol sakte ho ki *"maine ye class ki galtiyan poore document me dhoondh li hain"*.

---

---
---

# 🎉 REVIEW COMPLETE — 28 / 28

## Poora nichod

```
╔══════════════════════════════════════════════════════════════════════════╗
║  DAVID KE 28 COMMENTS — FINAL TALLY                                       ║
╠══════════════════════════════════════════════════════════════════════════╣
║  KISM                                                                    ║
║    Correction (galat tha)              19                                ║
║    Missing (kuch gayab tha)             2    #10, #13                    ║
║    Scope question                       1    #8                          ║
║    Agreement / confirmation             2    #17, #28                    ║
║    🔵 Design change (news, not error)   1    #23                          ║
║    ⚠ Hint (verify karo)                 1    #24                          ║
║    🎉 Mera flag/fix sahi tha             2    #25, #26                    ║
╠══════════════════════════════════════════════════════════════════════════╣
║  OUTCOMES                                                                ║
║    ✅ Open questions RESOLVED           4    (+1 moot by de-scoping)      ║
║    🔴 Blocking questions BAKI            3                                ║
║    ⚠ Self-corrections logged            4                                ║
║    🎉 Mere flagged gaps band hue        3    #25, #26, #27                ║
║    🎉 v2.0 ke ⚠ markers jinka jawab     2/5  #20, #28                     ║
║    📊 Cross-cutting themes             15                                 ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 CHAAR cheezein jo poore review ka nichod hain

```
1️⃣ FLOW KA SHAPE BADAL GAYA
   13 rigid steps → ~7 sequential + 3 parallel branches + join
   #5  Steps 4+5 merge
   #23 Step 7 ka gate hata (interrupt hata)
   #27 Tail parallel ho gaya
   #28 Mechanism confirm (strategy mutable hai)

2️⃣ AGENT KO ZYADA SOCHNA HAI, KAM POOCHHNA HAI
   Step 1:    14 required fields → ZERO asked-and-required
   Step 2:    deals table → agent auto-matches, sirf CPM dikhata hai
   Targeting: khaali form → default lagao, phir refine
   #6,#7,#9,#13,#15,#16,#18,#21,#22,#25

3️⃣ DO POORE CONCEPTS GAYAB THE
   • Advertiser defaults (3× confirmed) — schema, API, state — kuch nahi tha
   • Config-driven lists — sirf targeting ka nahi, GENERAL principle hai
   #13,#15,#22,#26

4️⃣ §4 API CATALOGUE SABSE BADA RISK HAI
   Endpoint NAMES bhi suspect hain, sirf response shapes nahi
   → Ek sawaal: "CTV endpoint family me kya hai?" — 7 items solve karega
   #20,#24,#28
```

## 🔴 TEEN BLOCKING questions — inke bina build shuru nahi ho sakta

| # | Sawaal | Kya unblock hoga |
|---|---|---|
| **1** | `POST /api/audience-sets/suggest/` ka **ek real response sample** | Bundle grouping logic (#20) · effective CPM (#2) · audience schema |
| **2** | Deal ki **built-in targeting structured metadata** me hai? | Agent-side deal matching (#18) — iske bina kaam nahi karega |
| **3** | **CTV endpoint family** me kya hai? | 7 API items ek saath (#20, #24, #28 + 4 gaps) |

**Plus ek SCOPE DECISION:**
| **4** | **Multi-market M1 me hai ya M2?** (#8) | Step order · budget split dimensions · N× API calls · effort estimate |

---

# 🎯 AB KYA KARNA HAI — teen kaam

## Kaam 1 — Confluence document update karo
```
✅ Taiyar hai: strategy_schema_documentation_v2.0_reviewed.md
   → 28 review notes inline, apni-apni jagah par
   → §9 Consolidated Action List (schema · document · agent behaviour)
   → §10 Open Questions (resolved · blocking · naming)
   → §12 "What the Team Should Take From This" (Wajahat / Vishal / Basil)

⚠ Publish karne se pehle: body PDF export se reconstruct hui hai —
  Confluence ke original se ek nazar mila lena (khaas kar §4 aur §5 code blocks)
```

## Kaam 2 — David ke 28 comments par replies post karo
```
✅ Taiyar hain: is file me har comment ka "💬 REPLY DRAFT"
   → Sab English me, professional, ready-to-paste

⚠ Reply karte waqt TONE ka dhyan:
   Correction (#1-#16, #19-#22)  → "Sahi catch, theek karta hun"
   Design change (#23)           → "Good to know, update kar raha hun"
                                     ← "sorry" NAHI
   Hint (#24)                    → "Verify karunga"
                                     ← "badal diya" NAHI
   Mera flag sahi tha (#25, #26) → "This was one I'd flagged…"
                                     ← seedhe, ghamand se nahi
   Confirmation (#17, #28)       → "Confirmed, thanks"
```

## Kaam 3 — Mastery file theek karo
```
⚠ full_strategy_schema_registery_mastery.md me ~63 jagah purane model par hai
   (kyunki wo document follow karti thi, aur document galat tha)

→ Poori list is file ke "Mastery-file me fix karne wali cheezein" section me
→ Ek hi baar me fix karna behtar hai, 28 baar nahi
```

## 💡 Aur ek chauthi cheez — consolidated question list bhejo
```
~56 sawaal jama ho gaye hain. Sab ek saath bhejna bekaar hoga.

✅ Behtar tarika:
   1. TEEN blocking questions alag, sabse upar, saaf highlight
   2. Ek scope decision (multi-market)
   3. Baaki ~52 ek appendix me, grouped by topic

→ David 3 sawaalon ka jawab 10 minute me de dega
→ 56 dekhkar wo baad ke liye chhod dega
```

---

*Review complete: Comments #1–#28 recorded, analysed, and drafted. **Ab replies post karne aur document publish karne ka waqt hai.***
