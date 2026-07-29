# David ke 28 Comments — Poora Explanation
### Padho aur kisi ko bhi samjha do

> **Ye file kis liye hai?**
> Tumne Confluence par `Strategy Schema documentation v2.0` share kiya. David Moss ne **28 comments** kiye.
> Ye file har comment ko **saat cheezon** ke saath kholti hai — taaki tum kisi bhi meeting me, kisi ko bhi, confidently explain kar sako.

## 📐 Har comment me ye 7 cheezein milengi

| # | Kya | Kyun zaroori |
|---|---|---|
| 1 | 📄 **Document me pehle kya tha** | Exact wording — taaki context clear rahe |
| 2 | 💬 **David ne kya likha** | Uske asli shabd, badle bina |
| 3 | 🔍 **Comment ka matlab** | Ekdum simple bhasha me |
| 4 | 🎯 **Unki requirement** | Concretely — kya karna hai |
| 5 | ❓ **Unka purpose** | Ye comment **kyun** kiya |
| 6 | 🙋 **Wo humse ye pooch sakte hain** | Sawaal + tayyar jawab |
| 7 | 🙋 **Hum unse ye pooch sakte hain** | Jo clarity chahiye |

## 🗂️ Is file ka naksha

| Part | Kya |
|---|---|
| **1** | Background — 2 minute me poora context |
| **2** | 🔴 **Bade themes** — meeting me yahi se shuru karo |
| **3** | **28 comments**, ek-ek, saat dimensions ke saath |
| **4** | Overall summary — kya-kya badla |
| **5** | 🙋 **Anticipated questions bank** — meeting ke liye consolidated Q&A |
| **6** | Cheat sheet — ek page me sab 28 |

## ⏱️ Kitna time hai? Utna padho

| Time | Kya padho |
|---|---|
| **2 minute** | Part 1 + Part 2 ka pehla box |
| **10 minute** | Part 1 + Part 2 poora + Part 6 cheat sheet |
| **30 minute** | + Part 5 (questions bank) |
| **Poora** | Part 3 — sab 28 comments |

---

# PART 1 — Background (2 minute me poora context)

## Kya ho raha hai
```
Kareem ne likha:  Strategy Schema documentation v1.1.0
                  (6-step UI wizard, saare ad formats)
                          ↓
Client ne kaha:   "Pehle sirf CTV karo, aur ye naye requirements hain"
                          ↓
Kareem ne likha:  Strategy Schema documentation v2.0
                  (13-step agentic flow, sirf CTV)
                  Status: "For client verification"
                          ↓
David Moss ne:    28 comments Confluence par
                          ↓
Ab:               Comments samajh kar document theek karna hai
```

## Ye document kya hai, aur kyun matter karta hai
```
Ye ek CONTRACT hai. Document ke aakhri page par likha hai:

  "Once confirmed, it becomes the shared contract that
   Wajahat (state + graph), Vishal (registry), and
   Basil (adaptive canvas) build against."

🔴 Yaani CHAAR log is document se code likhenge:
   • Wajahat  — LangGraph state aur graph
   • Vishal   — schema registry
   • Basil    — adaptive canvas (UI jo chat ke saath badalta hai)
   • Kareem   — Planning Agent ka dimaag

→ Agar schema me galti reh gayi, chaar logon ka kaam galat banega
→ Isliye David itna dhyan se review kar raha hai
```

## David kaun hai, aur wo kya kar raha hai
```
David Moss — Manager. Aur wo domain ka jaankaar hai (CTV/DSP ka).

🔴 ZAROORI SAMAJHNA:
   Wo document REJECT nahi kar raha.
   Wo CONTRACT THEEK karwa raha hai — code likhne SE PEHLE.

   Aur 28 comments me se:
     • 19 corrections hain (kuch galat tha)
     •  2 missing items (kuch gayab tha)
     •  1 scope sawaal
     •  2 agreements (v2.0 sahi tha)
     •  1 design change (unhone design badal diya — Kareem ki galti nahi)
     •  1 hint ("verify karo")
     •  2 jahan Kareem ka flag/fix SAHI tha 🎉
```

## Ek line me — 28 comments ka nichod
```
╔══════════════════════════════════════════════════════════════════════════╗
║  "Document ne reality ko simplify kar diya, cheezein zaroori bana di      ║
║   jo marzi ki thi, aur agent ko insaan se ZYADA POOCHHNE wala bana        ║
║   diya. Aur do poore concepts gayab the."                                 ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

# PART 2 — 🔴 BADE THEMES
### Meeting me YAHI se shuru karo — details baad me

Agar tumhe 2 minute me poora review explain karna hai, ye char boxes bol do.

---

## 🔴 THEME 1 — "Agent ko poochhna nahi, NIKALNA chahiye"

**10 comments isi ek baat ke hain.** Ye sabse bada theme hai.

```
❌ DOCUMENT ME KYA THA
   Step 1 me 14 fields, saare "Required"
   Step 2 me deals ki table, trader checkbox tick kare
   Targeting me 5 khaali fields, trader bhare

   → Ye ek FORM hai. Trader ko sab bharna hai.

✅ DAVID KYA CHAHTA HAI
   Step 1:    brief se sab nikaal lo, confirm karwao
   Step 2:    agent khud deal match kare, sirf CPM dikhao
   Targeting: default laga do, trader accept ya refine kare

   → Ye ek CONVERSATION hai. Agent sochta hai, trader confirm karta hai.

🎯 NATEEJA
   Step 1: 14 required fields → ZERO "asked-and-required"
```

**Sabse strong baat jo tum bol sakte ho:**
> *"Document ka apna Principle #2 kehta hai 'a form that fills itself in as you chat.' Par Step 1 me 14 required fields the. David ka har comment usi principle ko lagu karwa raha hai jo document ne khud likha tha."*

**Comments:** #6, #7, #9, #13, #15, #16, #18, #21, #22, #25

---

## 🔴 THEME 2 — "Flow ek seedhi line nahi hai"

**Char comments milkar poore flow ka shape badal dete hain.**

```
❌ DOCUMENT ME KYA THA
   13 steps, ek seedhi line:
   1→2→3→4→5→6→7→8→9→10→11→12→13
   Har step agle ko rokta tha

✅ AB KYA HAI
   ~7 sequential steps, phir TEEN PARALLEL branches:

   Create ──┬──→ Creative → Platform approval ──┐
            ├──→ Tracking setup ────────────────┤──→ 💰 Activate
            └──→ Credit check ──────────────────┘

🎯 NATEEJA
   Ye ab "field fixes" nahi hain — POORA REDESIGN hai
```

**Kaise pahuncha:**
| Comment | Kya kiya |
|---|---|
| **#5** | Steps 4+5 merge — 13 se 12 steps |
| **#23** | Step 7 ka approval gate hata — ek loop aur ek interrupt gaya |
| **#27** | Tail ke steps ka kram zaroori nahi — parallel ho gaye |
| **#28** | Mechanism confirm — strategy create ke baad bhi badalti hai |

**Sabse strong baat:**
> *"#27 ne bataya ki tail parallel hai. Par wo possible kaise? #28 ne jawab diya — 'strategy create hone ke baad update ho sakti hai.' Do comments ek doosre ka jawab hain."*

---

## 🔴 THEME 3 — "Do poore concepts gayab the"

```
❌ CONCEPT 1 — ADVERTISER DEFAULTS
   David ne TEEN BAAR bataya ki kuch values ADVERTISER ke record me hoti hain:
     #13  frequency cap        "we have a default per advertiser"
     #15  product categories   "we have a default on the advertiser"
     #22  device type          "set at advertiser level"

   🔴 Par document me:
     • Koi AdvertiserDefaultsSchema nahi
     • Koi endpoint nahi
     • Koi state field nahi
     • "advertiser settings" ka EK ZIKR BHI nahi

   Sirf `advertiser_id: str` — ek UUID, aur bas.

   🔴 TEST jo lagana chahiye tha:
      "Kya ye value HAR CAMPAIGN me badalti hai?"
      Agar nahi → wo advertiser ka attribute hai, strategy ka nahi

      BrightPath ki product category → hamesha "Education"  ❌ nahi badalti
      BrightPath ka budget           → har campaign me alag  ✅ badalta hai
```

```
❌ CONCEPT 2 — CONFIG-DRIVEN LISTS
   Client ne pehle kaha tha:
     "This targeting list frequently changes so it should be easy to add
      new targeting types" → config-driven, not hard-coded

   #26 ne WAHI principle CHANNELS par lagaya:
     "not necessary netflix or disney - could be paramount or channel 4"

   🔴 Yaani config-driven SIRF targeting ka rule nahi tha —
      wo ek GENERAL PRINCIPLE hai.

   → Aur document me abhi bhi kai FIXED lists hain jo khuli honi chahiye:
     audience data sources · deal types · inventory tiers ·
     durations · currencies
```

---

## 🔴 THEME 4 — "API catalogue sabse bada risk hai"

```
❌ PEHLE lagta tha: sirf RESPONSE SHAPES verify karne hain
✅ AB pata chala: ENDPOINT NAMES bhi galat ho sakte hain

╔══════════════════════════════════════════════════════════════════════════╗
║  #20  POST /audience-sets/suggest/  →  ❌ RESPONSE SHAPE galat (CONFIRMED)║
║  #24  POST /api/strategies/         →  ⚠ ENDPOINT hi galat ho sakta hai   ║
║       Audience-set creation         →  ⚠ "CTV endpoint, name TBC"         ║
║       Update endpoint (#28)         →  ⚠ capability confirm, naam nahi    ║
║       Reach forecast                →  ⚠ DO endpoints + ek "TBC"          ║
║       9 naye v2.0 endpoints         →  ❌ Koi spec hi nahi                ║
╚══════════════════════════════════════════════════════════════════════════╝

🔴 Ek "contract document" ke liye ye serious hai — Wajahat aur Vishal
   in examples se code likhenge.

✅ FIX: har API example par ek marker lagao —
   ✅ VERIFIED   real API se check kiya
   ⚠ ASSUMED    verify nahi hua — build mat karo
   ❌ INCORRECT  real shape alag hai
```

---

## 🎉 AUR EK BAAT — teen jagah Kareem SAHI tha, David se PEHLE

Ye meeting me bolna zaroori hai — kyunki ye dikhata hai ki review ek **dialogue** thi, ek **correction list** nahi.

```
#25  Click-through URL
     v2.0 me flag kiya tha: "Required hai par CTV me click nahi hota —
                             either DSP mandates it, OR it should be optional"
     David: "optional for streaming tv"     → ✅ doosra option sahi tha

#26  Creative approval statuses
     v2.0 review me propose kiya tha: "dict[str, ApprovalStatusEnum] hona
                                       chahiye, ek single field nahi"
     David: "single status for each channel" → ✅ bilkul wahi

#27  Partial creative upload
     Flag kiya tha: "multiple durations, partial upload is not covered"
     → #27 ke per-duration map se ye gap BAND ho gaya
```

**Aur ye bhi:**
```
v2.0 me PAANCH ⚠ open questions the.
David ne DO par SEEDHA jawab diya (#20 aur #28) — aur DONO BLOCKING the.

🎯 Yaani ⚠ markers ne reviewer ka dhyan THEEK WAHIN kheencha
   jahan clarity ki zaroorat thi.

   Agar assume kar liya hota:
     • Audience module galat response shape par ban jaata
     • ASIN handling galat direction me chali jaati
```

---

# PART 3 — 28 COMMENTS, EK-EK

---
---

# COMMENT #1 — 3P targeting ek choice hai, aur wo deal se bandhi hai

**📍 Kahan:** §2.3 Three inventory tiers → tier table → `3P pre-curated` row → **Audiences** column

## 📄 Document me pehle kya tha
```
Tier table ka "Audiences" column:

  Amazon owned      →  Amazon audiences
  3P pre-curated    →  "Their own targeting (adds CPM)"
  3P needs curation →  "Their own targeting (adds CPM)"
                        ↑
                Padhne se lagta hai: "SIRF Netflix ki targeting
                possible hai, koi choice nahi"
```

## 💬 David ne kya likha
> *"For 3P there's often a choice whether to use Amazon's targeting (may be limited in functionality i.e. only device) or to apply the targeting at the inventory source / SSP. Which is then specific to the deal that is chosen or curated."*

## 🔍 Comment ka matlab
```
Netflix/Disney par targeting ke DO raaste hain — ek nahi:

  Raasta 1: AMAZON ki targeting lagao
            → Amazon DSP ki taraf se
            → Par capability "may be limited" — shayad sirf device level

  Raasta 2: NETFLIX ki apni targeting (SSP side)
            → Zyada powerful (unka apna data)
            → 💰 CPM badhati hai
            → 🔴 DEAL KE ANDAR BAITHI HOTI HAI

Aur "SSP" = Supply Side Platform = bechne walon ka software
(DSP ka ulta — DSP kharidne walon ka)
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Tier table me **choice** dikhao, ek option nahi |
| 2 | Trader ko trade-off batao (limited vs mehnga) |
| 3 | Schema me `targeting_source` field add karo (`AMAZON_DSP` / `INVENTORY_SOURCE`) |
| 4 | 🔴 Document karo ki 3P ki targeting **deal ke saath bandhi** hai — alag se nahi lagti |

## ❓ Unka purpose
```
1. Ek CHOICE ko FACT bana diya gaya tha
   → Agar agent maane ki koi option nahi, wo trader se poochhega hi nahi
   → Ek poora feature gayab

2. Ek trade-off chhup gaya
   → Amazon: limited par shayad sasta
   → SSP: powerful par CPM badhata hai
   → Ye trader ko dikhna chahiye

3. Flow me ek coupling chhupi thi
   → "Specific to the deal that is chosen or curated"
   → Yaani 3P ki targeting Step 2 (inventory) me tay hoti hai, Step 5 me nahi
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| *"Agar targeting deal ke andar hai, to trader ko kaise pata chalega kya mila?"* | Comment #18 ne isko solve kar diya — trader apni **requirements** batata hai, agent matching deal dhoondhta hai. Trader ko deal padhne ki zaroorat nahi. |
| *"To Step 5 (Targeting) 3P ke liye bekaar hai?"* | Poori tarah nahi. Amazon audiences 3P par bhi lagti hain (#19). Par SSP-side targeting deal-bound hai — wo Step 2 me tay hoti hai. |
| *"Ye do options me se default kya hoga?"* | Abhi tay nahi — ye ek open question hai. Mera suggestion: Amazon audiences default, kyunki wo Step 5 me flexible hai. Par confirm karna hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | Amazon audiences **aur** SSP targeting — dono ek hi 3P deal par lag sakti hain, ya ek hi? | Schema me `targeting_source` single value hai ya list — ye tay karega |
| 2 | 3P par Amazon targeting kitni "limited" hai — exact list kya hai? | Trader ko batana hai kya milega |
| 3 | 🔴 3P deal ki **built-in targeting structured metadata me dikhti hai**? | **BLOCKING** — #18 ki auto-matching iske bina kaam nahi karegi |

## 🏷️ Ek line me
> *"Tumne likha 'Netflix ki apni targeting' — jaise koi option nahi. Par option hai: Amazon ki (kamzor) ya Netflix ki (behtar par mehngi). Aur Netflix wali deal ke andar baithi hai."*

**Severity:** 🔴 HIGH — missing feature + missing schema field + flow coupling

---
---

# COMMENT #2 — Audience fee profile par nahi, DATA SOURCE par depend karti hai

**📍 Kahan:** §2.4 Audience Set Profiles → 🔄 CHANGED line → **"added fee consequence"**

## 📄 Document me pehle kya tha
```
§2.4 ki line:
  "🔄 CHANGED — renamed 'Broad' to 'Wide' per client vocabulary;
   ADDED FEE CONSEQUENCE."

Aur table:
  Narrow   → "highly targeted, elevated intent, HIGHER AUDIENCE FEE,
              risk of underdelivery"
  Balanced → "optimal blend, the usual recommendation"
  Wide     → "broad demographic/interest reach, LOWER FEE, less precision"

Aur ek ➕ NEW note:
  "A narrow audience is both smaller and MORE EXPENSIVE per impression."
```

## 💬 David ne kya likha
> *"there's not necessarily a fee consequence. Fee is determined by which audiences are used not how many. If it's Amazon's or a 3P first party data like Lifestyle or Interest then there's a fee for using it. This is regardless of profile."*

> *"Note here that it doesn't compound the more audiences you use. There is just 1 fixed CPM applied when 1P data is used for Amazon or Third party audience. But if the user matches a segment in both you would pay both fees."*

## 🔍 Comment ka matlab
```
Document ne ek RULE BANA LIYA jo asal me exist nahi karta:

❌ Document ki soch:
   "Narrow = specific data = MEHNGA"
   "Wide   = general data  = SASTA"
   Aur: 1 segment = 1 fee · 2 segments = 2 fee · 3 = 3 fee

✅ Reality:
   Fee is baat par depend karti hai ki KAUNSA DATA use kiya:
     Amazon ka data (1P) use kiya  → 1 FIXED CPM
     3P ka data use kiya           → 1 FIXED CPM
     Banda DONO me aaya            → DONO fees

   🔴 Segments ki GINTI se koi farak nahi:
      1 Amazon segment  → 1 fee
      10 Amazon segment → 1 fee   ← WAHI!
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | "higher fee" (Narrow) aur "lower fee" (Wide) — **hatao** |
| 2 | "more expensive per impression" — **hatao** |
| 3 | Fee ko **per data source** model karo, per segment nahi |
| 4 | 🔴 Mixed-source bundle par effective CPM ek **RANGE** hai — ek number nahi |
| 5 | `SelectedAudienceSetSchema.vcpm_fee` hatao → `data_source` add karo |

## ❓ Unka purpose
```
1. Ek galat rule se galat salah milegi
   ❌ "Balanced recommend karta hun, Narrow zyada MEHNGI hai"
      → Par asal me dono ka SAME daam tha!
      → Trader ne GALAT WAJAH se faisla liya

2. Effective CPM ka poora ganit galat tha
   Single source:  £28.88 + £1.85 = £30.73        ← ek number
   Mixed source:   £30.73 se £32.83 tak           ← ek RANGE
   (depend karta hai ki banda kisme match hua)

3. 🔴 Aur ye document ke #1 PRINCIPLE ke khilaaf hai
   "Zero-Hallucination: NEVER invents... only VERIFIED values"
   → Par document ne KHUD ek correlation bana li jo verify nahi ki
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| *"To Balanced kyun recommend karte ho, agar cost same hai?"* | **Reach** ke liye. Balanced me 1.65M available reach hai, Narrow me 450K — aur same data source par cost bilkul same. To Narrow chunne ka koi cost faayda nahi. |
| *"Range dikhana confusing nahi hoga trader ke liye?"* | Range sirf **mixed-source** bundle me aati hai. Single-source me ek number hi hai. Aur range ke saath agent batata hai ki ye estimate hai — jo Zero-Hallucination principle ke hisaab se sahi hai. |
| *"Kitna farak padta hai practically?"* | £30.73 se £32.83 — £2.10 ka farak. £10,000 par ~20,000 impressions ka farak. Chhota nahi hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun zaroori |
|---|---|---|
| 1 | 🔴 Suggest API **per-segment `vcpm`** deta hai (1.85, 1.63, 1.20) — agar fee per-source hai to wo numbers kya hain? | **Effective CPM calculate nahi kar sakte** iske bina |
| 2 | Amazon 1P fee aur 3P fee ke **actual numbers** kya hain? Fixed ya audience-type par depend? | Forecast ke liye asli numbers chahiye |
| 3 | Koi audience type **bina fee** ki bhi hai (basic demographic)? | Agar haan, agent sasta option suggest kar sakta hai |
| 4 | Mixed-source me "matched in both" ka typical ratio? | Range ki jagah blended estimate dene ke liye |

## 🏷️ Ek line me
> *"Tumne likha 'Narrow mehngi, Wide sasti' — ye tumne bana liya. Fee is baat par depend karti hai ki kaunsa DATA use kiya, na ki kitne segments."*

**Severity:** 🔴 HIGH — business model galat, effective CPM ka ganit galat, schema galat

---
---

# COMMENT #3 — Budget split OPTIONAL hai, Required nahi

**📍 Kahan:** §3 Comparison table → **"Budget split ➕ NEW"** row

## 📄 Document me pehle kya tha
```
Step 3 ka field matrix:
  Split by inventory | Allocation (%) | REQUIRED when multiple inventories
  Split by duration  | Allocation (%) | REQUIRED when multiple durations
                                        ↑
                                  "Required" likha tha
```

## 💬 David ne kya likha
> *"is optional but to give an accurate CPM is preferred"*

## 🔍 Comment ka matlab
```
Budget split ZAROORI nahi hai — trader skip kar sakta hai.
Par BEHTAR hai karna, kyunki uske bina SAHI CPM nahi bata sakte.

Kyun?
  4 deals ke 4 alag CPM: £20.00 · £24.00 · £31.50 · £32.00

  Split KIYA:
    Prime 15s £2,340 ÷ 20.00 × 1000 = 117,000 impressions
    Prime 30s £3,660 ÷ 31.50 × 1000 = 116,190 impressions
    → Total 358,190 — ✅ ACCURATE, har line ka CPM pata hai

  Split NAHI kiya:
    → Amazon DSP RUNTIME par decide karega kitna kahan gaya
    → Yaani asli CPM PEHLE SE PATA HI NAHI CHAL SAKTA
    → Sirf range de sakte hain (£20–£32) ya blended estimate
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Dono split fields: **Required → Optional** |
| 2 | Agent split propose kare, **par skip ka option** bhi de |
| 3 | Skip karne ka **nuksaan batao** — "accurate CPM nahi de paunga" |

## ❓ Unka purpose
```
1. Trader ko block nahi karna
   Kai baar trader kehta hai "tum decide karo, main details me nahi jaana"
   → Document usko FORCE karta tha
   → Wo frustrate hota

2. Consequence batana, mana nahi karna
   David ne "optional" bola PAR reason bhi diya
   → Ye document ke apne pattern se match karta hai:
     Step 3 me likha hai "The agent must state which it chose and why"
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"Schema me ye Required tha?"* | 🔴 **Nahi** — `budget_split: Optional[BudgetSplitSchema] = None` schema me pehle se optional tha. **Sirf field table galat tha.** Document apne aap se contradict kar raha tha. |
| *"To agent split karega ya nahi?"* | Karega — propose karega, method batayega, aur skip ka option dega. Sirf force nahi karega. |
| *"Skip karne par forecast kaise dega?"* | Blended estimate ya range — aur saaf batayega ki ye estimate hai, exact nahi. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Bina split ke Amazon DSP allocation kaise karta hai — koi rule hai ya pure auction-driven? |
| 2 | Agar multi-market scope me hai, to `BudgetSplitSchema` me `by_market` bhi chahiye — confirm? |

## 🏷️ Ek line me
> *"Budget split zaroori nahi hai — par uske bina sahi CPM nahi bata sakte, isliye behtar hai karna."*

**Severity:** 🟡 MEDIUM — field requirement + agent behaviour, flow nahi badalta

---
---

# COMMENT #4 — Audiences OPTIONAL hai, mandatory nahi

**📍 Kahan:** §3 Comparison table → **"mandatory"** (Audiences row me)

## 📄 Document me pehle kya tha
```
Comparison table:
  "4. Audiences (MANDATORY, suggestion-driven)"

§2.4 me:
  "➕ NEW: audiences are MANDATORY and suggestion-driven. The agent always
   suggests three options... Nobody browses the ~3,400 segments manually."

Step 4 field matrix:
  Audience options | 3 profiles | REQUIRED | 🔄 CHANGED from optional to MANDATORY

Step 4 constraints:
  "At least one audience set must be selected"
```

## 💬 David ne kya likha
> *"optional again"*

Do shabd. Par bada matlab — **"again"** = "phir se" = wapas optional karo (v1.1.0 me optional thi).

## 🔍 Comment ka matlab
```
v1.1.0 me: Audiences OPTIONAL thi
v2.0 me:   MANDATORY bana di
David:     wapas OPTIONAL karo — v2.0 ka ye change GALAT tha

🔴 Dhyan do — David ne "suggestion-driven" par KOI comment nahi kiya:
   ✅ "suggestion-driven"  → SAHI hai, rakho
   ❌ "mandatory"          → GALAT hai, hatao

Do alag baatein ek me mila di gayi thi:
   "Agent suggest karega"  ✅ (kyunki 3,400 browse karna impractical)
   "Audience zaroori hai"  ❌ (iska koi reason nahi diya gaya)
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Audience options: **Required → Optional** |
| 2 | Chosen option: **Required → Optional** |
| 3 | *"At least one audience set must be selected"* — **hatao** |
| 4 | §8 Summary se "audiences mandatory" entry **hatao** |
| 5 | ➕ "No audience" ka case document karo |

## ❓ Unka purpose
```
🔴 SABSE BADI WAJAH — ek valid, SASTA, HIGH-REACH option delete ho gaya tha

Bina audience:
  Deal: Prime Video ROS @ £28.88 · Audience: KOI NAHI
  → Reach: MAXIMUM (poora available inventory)
  → Data fee: £0.00  ← koi audience data use nahi hua (#2 ka rule)
  → Effective CPM: £28.88 (deal CPM hi)
  → Impressions: 346,260

Audience ke saath:
  Same deal + "Higher Education Seekers"
  → Data fee: £1.85 · Effective CPM: £30.73
  → Impressions: 325,415  ← 20,845 KAM
  → Reach: 450,000 tak simit

╔══════════════════════════════════════════════════════════════════════════╗
║  "NO AUDIENCE" = SABSE SASTA + SABSE ZYADA REACH                          ║
║                                                                          ║
║  Aur CTV ka goal FIXED "AWARENESS" hai — jahan max reach chahiye.          ║
║  Yaani ye SABSE ACCHA option ho sakta hai!                                 ║
║                                                                          ║
║  🔴 Document ne "mandatory" likhkar ye poora option KHATAM kar diya —      ║
║     aur wo bhi Awareness-only module me                                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| ⚠ *"To Kareem ka 'narrow/balanced/wide' deliverable khatam ho gaya?"* | **Nahi.** Feature delete nahi hua — **OPT-IN** ban gaya. pgvector suggestion engine zinda hai, teen profiles zinda hain. Sirf "gate" hat gaya. Aur ye behtar hai — ab jo trader audience chunta hai, wo **jaan-boojh kar** chunta hai. |
| *"Schema me mandatory tha?"* | 🔴 **Nahi** — `audience_options: list[...] = Field(default_factory=list)` schema me optional tha. **Sirf prose aur table me "mandatory" likha tha.** Schema sahi tha. |
| *"Agar audience nahi hai to targeting kya karegi?"* | Country + device default lagta hai (#5, #21). Aur postcode-only strategy bhi possible hai (#5 ka David ka example). |
| *"Repair loop par asar?"* | 🔴 Haan — bada asar. Agar koi audience nahi hai, to "widen the audience" lever hi nahi hai. Detail #12 me. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | "No audience" ko agent **default** rakhe (aur audience opt-in ho), ya trader se poochhe? |
| 2 | Kya kuch advertisers ke liye audience **zaroori** ho sakti hai (policy)? |

## 🏷️ Ek line me
> *"Audience zaroori nahi hai. Wapas optional karo. Suggestion theek hai, majboori galat hai."*

**Severity:** 🔴 HIGH — ek poora valid, sasta, high-reach option delete ho gaya tha

---
---

# COMMENT #5 — Audiences TARGETING ka hissa hai · default lagao, phir refine

**📍 Kahan:** §3 Comparison table → **"Targeting ➕ NEW"** row

## 📄 Document me pehle kya tha
```
DO ALAG STEPS the:

Step 4 — Audiences (MANDATORY)
  "Teen options hain — Narrow, Balanced, Wide. Ek chuno."
  → Trader ko ZAROOR chunna padega

Step 5 — Targeting (Optional, 5 KHAALI fields)
  Location · Instream position · Content exclusions ·
  Device type · Mobile environment
  → Sab khaali, trader bhare
```

## 💬 David ne kya likha
> *"I would treat audiences as part of targeting. So once inventory decided / inferred then you are shown the default targeting applied / suggested like country targeting and Connected TV (CTV) device only and then you could refine this, define the audience segments or accept it as sufficient. Example: the user wants to use only postcodes instead of audiences for targeting"*

## 🔍 Comment ka matlab
```
TEEN baatein ek comment me:

1️⃣ AUDIENCES = TARGETING KA HISSA
   Dono ek hi sawaal ka jawab dete hain: "KISKO dikhana hai?"
   → Do alag steps banane se trader confuse hota hai
   → Audience segments = ek TARGETING TYPE, alag step nahi

2️⃣ DEFAULT LAGAO, PHIR REFINE
   ❌ Purana: 5 KHAALI fields, trader bhare
   ✅ Naya:   default PEHLE SE laga hua dikhao —
              ✓ Country: GB              (Step 1 se derive)
              ✓ Device: Connected TV     (CTV hai to)
              ✓ Audience: None
              "Kuch badalna hai? Ya 'theek hai' bol do."

3️⃣ AUDIENCE AUR POSTCODE ALTERNATIVES HAIN
   "only postcodes INSTEAD OF audiences"
   → "instead of" = ki JAGAH par
   → Trader keh sakta hai: "audience nahi chahiye, sirf SW1, SW3, W1"
   → Ye ek POORI valid strategy hai
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | 🔴 **Step 4 aur Step 5 MERGE karo** — 13 steps se 12 |
| 2 | Audiences ko ek **targeting type** banao |
| 3 | ➕ **Default targeting** section — kya default lagta hai, kahan se derive |
| 4 | ➕ **"Accept or refine"** interaction pattern |
| 5 | 🔴 `TargetingSchema` ko **sach me config-driven** banao (abhi 5 hard-coded fields hain) |
| 6 | Repair loop **conditional** karo — bina audience ke widen karne ko kuch nahi |

## ❓ Unka purpose
```
1. Conceptual galti theek karna
   Trader confuse hota tha: "Audience me education seekers chuna...
   ab Targeting me phir se kuch chunna hai? Ye alag kaise hai?"

2. UX behtar karna
   6 khaali fields → 2 pre-filled + "kuch aur chahiye?"
   → Trader ka kaam 80% kam

3. Config-driven requirement poora karna
   Client ne kaha tha: "targeting list frequently changes → config-driven"
   🔴 Agar audiences BHI ek targeting type hai, to wo bhi usi registry me
   → Ek hi system, ek hi tarika

4. 🔴 AUR SABSE ZAROORI — document ke APNE Principle #2 se match
   Principle 2: "Self-Filling Form Paradigm — a form that fills itself in"
   Par Step 5 me 5 KHAALI fields the!
   → David ka model document ke apne principle ko BEHTAR follow karta hai
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"Targeting Budget Split se pehle aana chahiye?"* | Haan, do wajah se: (1) David ka wording — *"once inventory decided… then default targeting"* — inventory ke turant baad. (2) Logically — audience **data fee** targeting me tay hoti hai, aur wo fee accurate CPM ka input hai (#3). **Par ye confirm karna hai.** |
| *"`TargetingSchema` config-driven hai?"* | 🔴 **Nahi.** Uska docstring kehta hai *"config-driven, extensible"* par code me **5 hard-coded fields** hain. Ye client ke explicit requirement ka violation hai. Fix: `selections: dict[str, list[str]]` + registry. |
| *"Repair loop par kya asar?"* | Bada. Agar koi audience nahi hai to "widen audience" lever nahi hai. Primary lever ban jaata hai "doosri targeting relax karo." Detail #12 me. |
| *"12 steps me se aur kuch merge hoga?"* | #23 ne ek gate hataya, #27 ne tail parallel kar diya. To final structure ~7 sequential + 3 parallel branches hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | Targeting **Budget Split se pehle** aaye? | Step order confirm karna hai |
| 2 | `GET /api/strategies/locations/{market}/` **postcodes** support karta hai? | David ka apna example postcode ka hai — iske bina wo case kaam nahi karega |
| 3 | Agar koi audience nahi hai, repair loop kaunsi targeting pehle relax kare? | Lever order define karna hai |

## 🏷️ Ek line me
> *"Audience targeting ka hissa hai, alag cheez nahi. Aur khaali form ke bajaye ek default lagao — trader accept kare ya refine kare."*

**Severity:** 🔴🔴 VERY HIGH — do steps merge, naya interaction pattern, 13→12 steps, repair loop conditional

---
---

# 🧩 COMMENTS #6–#17 — SAB STEP 1 KE FIELD MATRIX PAR

> **12 comments ek hi table par.** Ye document ka sabse kamzor hissa nikla — poore review ka **43%**.
>
> **Aur inka ek saaf nateeja hai:** Step 1 ek FORM se ek SUMMARY-TO-CONFIRM ban jaata hai.
> 14 fields → 12 fields, aur **ek bhi field "asked-and-required" nahi**.

---
---

# COMMENT #6 — Field list CTV ke liye review karo, aur jawab KHUD nikalo

**📍 Kahan:** Step 1: Basics → *"What was in v1.1.0"* ki poori list

## 📄 Document me pehle kya tha
```
"What was in v1.1.0 (Step 1 + Step 2):
  • Strategy name, flight dates, target markets, primary currency,
    FORMATS (ALL FOUR), product categories, selling location, ASINs
  • GOAL (THREE CHOICES), KPI (SIX CHOICES), ad tag conversions,
    market budgets, base bids"

Aur naya field matrix: 14 fields, lagbhag sab "Required"
```

## 💬 David ne kya likha
> *"should review as a lot of this is for a non CTV strategy - can simplify for CTV and imply answers"*

## 🔍 Comment ka matlab
```
DO alag baatein:

1️⃣ "a lot of this is for a NON CTV strategy"
   Kai fields Display/Online Video ke zamane se aaye hain:
     formats (ALL FOUR)     → Display aur online_video scope me nahi hain
     goal (THREE choices)   → CTV hamesha AWARENESS hai
     KPI (SIX choices)      → chaar KPI click-based hain, CTV me click nahi

2️⃣ "can IMPLY answers"
   Jo bache, unke jawab AGENT khud nikaale — trader se poochho mat
   ("imply" = ishaare se samajh lena / khud nikaal lena)
```

## 🎯 Unki requirement
```
Ek POORA structural fix chahiye — field matrix me ek NAYA COLUMN:

╔══════════════════════════════════════════════════════════════════════════╗
║  ABHI:  Field | Type | Requirement | Change from v1.1.0                   ║
║  NAYA:  Field | Type | Requirement | SOURCE | Change from v1.1.0          ║
║                                        ↑                                 ║
║  Kyunki "Requirement" ye batata hai ki value ZAROORI hai ya nahi —         ║
║  par ye NAHI batata ki value KAHAN SE aayegi.                              ║
║                                                                          ║
║  🔴 "Required" ka matlab NAHI hai "trader ko type karna padega."           ║
║     "Required" = "value maujood honi chahiye."                             ║
║     KAUN degi — ye ALAG sawaal hai.                                       ║
╚══════════════════════════════════════════════════════════════════════════╝

Source ke 8 types (poore review se):
  💬 ASKED       trader se poochhna padega
  🧠 INFERRED    brief ke text se nikala
  ⚙️ DERIVED     doosre field se (market → currency)
  🏢 ADVERTISER  advertiser ke record se
  🤖 GENERATED   agent ne banaya
  🔒 FIXED       CTV ke liye constant
  🔌 API         API response se
  ⏭️ LATER       baad ke step me — Step 1 me list hi nahi karna
```

## ❓ Unka purpose
```
1. Field list CTV ke liye poori tarah review nahi hui thi
   v2.0 ne scope CTV kiya PAR list purani chhod di

2. 🔴 Document apna hi Principle #2 follow nahi kar raha tha
   "Self-Filling Form Paradigm — a form that fills itself in as you chat"
   → Par 14 fields "Required" the, jaise trader ko sab bharna hai

3. 14 sawaal se trader bhaag jaayega
   Purana wizard 20-30 minute leta tha.
   Agar agent bhi 14 sawaal poochhega — faayda kya hua?
```

## ✅ Poora "implied" Step 1 kaisa dikhega
```
Trader (ek sentence):
"BrightPath ke liye UK me August me £10,000 ka Prime Video awareness
 campaign, education website, 30 second ka ad."

AGENT NE KHUD NIKALA (kuch bhi poochha nahi):
  strategy_name     = "BrightPath_Awareness_GB_Aug2026"   ← generate (#7)
  markets           = ["GB"]                              ← "UK" se
  primary_currency  = "GBP"                               ← GB se (#9)
  flight_dates      = 1–31 Aug 2026                       ← "August" se
  market_budgets    = £10,000                             ← "£10,000" se
  formats           = ["streaming_tv"]                    ← constant (#14)
  durations         = ["30"]                              ← "30 second" se
  goal              = "AWARENESS"                         ← CTV = fixed
  kpi               = "reach"                             ← awareness default
  product_categories= [1] Education                       ← advertiser (#15)
  frequency_cap     = 3                                   ← advertiser (#13)

→ 11 fields BHAR GAYE. Ek bhi sawaal nahi poochha.
→ Agent bas dikhata hai aur confirm karwata hai
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| *"Agar agent galat infer kare to?"* | Isi liye §7.4 ka *"Did I understand correctly?"* mechanism hai — agent jo samjha wo **dikhata** hai, aur assumptions alag highlight karta hai. Trader turant pakad sakta hai. Document isko *"the single most important trust mechanism"* kehta hai. |
| *"Base bid bhi derive ho sakta hai?"* | **#12 ne isse aage ja kar bataya** — CTV me base bid ki **zaroorat hi nahi** hai, kyunki CPM deal me fixed hai. Detail #12 me. |
| *"Ye "Source" column extra kaam nahi hai?"* | Ulta — ye kaam **kam** karta hai. Uske bina har field par bahas hoti hai ki "ye poochhna hai ya nahi." Column se ek baar likh diya, aur Wajahat/Basil ko saaf pata rahega. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Base bid rate card se derive karna theek hai, ya trader ka input zaroori hai? *(#12 ne isko aage solve kiya)* |
| 2 | Strategy name ka koi standard naming convention hai jo follow karna chahiye? |

## 🏷️ Ek line me
> *"Step 1 ki field list CTV ke liye review karo — kai fields non-CTV hain. Aur jo bache, unke jawab khud nikalo, poochho mat."*

**Severity:** 🔴🔴 VERY HIGH — poora Step 1 ka design badalta hai

---
---

# COMMENT #7 — Strategy name brief se auto-generate ho sakta hai

**📍 Kahan:** Step 1 → **Strategy name** → **"Required"**

## 📄 Document me pehle kya tha
```
Strategy name | String | REQUIRED | ✅ Unchanged. Validated via
                                    GET /api/strategies/check_strategy_name_uniqueness/
```

## 💬 David ne kya likha
> *"could be auto generated from brief"*

## 🔍 Comment ka matlab
```
Naam trader se poochhne ki zaroorat nahi — agent brief se bana sakta hai:

  "BrightPath, UK, August 2026, Prime Video, awareness"
       ↓
  "BrightPath_Awareness_GB_Aug2026"

Aur uniqueness check bhi automatic:
  Agent → check_strategy_name_uniqueness → {"is_unique": false}
  Agent (khud) → "_v2" lagata hai → dobara check → ✅
  Agent → "Naam 'BrightPath_Awareness_GB_Aug2026_v2' rakha hai
           (v1 pehle se thi). Badalna hai?"
```

## 🎯 Unki requirement
```
Requirement: Required  ✅ RAHEGA (bina naam ki strategy nahi ban sakti)
Source:      🤖 GENERATED  ← trader ko type karne ki zaroorat NAHI

→ Dono saath me sach hain. Koi virodh nahi.
```

## ❓ Unka purpose
```
1. Naam ek CHORE hai, DECISION nahi
   Trader ko planning ke waqt naam ki parwah nahi hoti
   Wo baad me dhoondhne ke liye chahiye

2. Consistent naming milegi
   Agent generate karega → sab strategies ek pattern me → dhoondhna aasan
   (Trader khud rakhega to: "test", "test2", "abc", "final_FINAL")

3. Ek sawaal kam (Comment #6 ka extension)
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"Agar trader ko naam pasand na aaye?"* | Wo badal sakta hai — agent generate karta hai par **dikhata** hai. Aur duplicate case me document ka §7.2 protocol pehle se kehta hai *"append suffix… **and prompt user**"* — yaani chup-chaap nahi badalna. |
| *"Ye field ab Required nahi hai?"* | Required **rahega** — naam zaroori hai. Sirf uska **source** badla: trader se → agent se. Ye "Required ≠ Asked" ka pehla saaf example hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Koi naming convention hai jo follow karna chahiye (e.g. `Advertiser_Objective_Market_Month`)? |

## 🏷️ Ek line me
> *"Strategy name brief se khud bana lo — trader se poochhne ki zaroorat nahi."*

**Severity:** 🟡 MEDIUM — fix chhota, par insight bada (**Required ≠ Asked**)

---
---

# COMMENT #8 — Multi-market support karenge? Flow par kya asar?

**📍 Kahan:** Step 1 → **Target markets** → **"Multi-select"**

## 📄 Document me pehle kya tha
```
Target markets | MULTI-SELECT | Required | ✅ Unchanged. ISO country codes

Aur §7.1 (Brief Parsing) me:
  "UK and France → markets: ["GB", "FR"]"   ➕ NEW
   ↑ v2.0 ne multi-market EXPLICITLY scope me daala
```

## 💬 David ne kya likha
> *"Are we going to support multi market? what impact to the flow will it have - repeating choices for each market?"*

## 🔍 Comment ka matlab
```
🔴 Ye baaki comments se ALAG KISM ka hai — ye ek SAWAAL hai, correction nahi.

David poochh raha hai:
  1. Multi-market support karenge kya?
  2. Agar haan, flow par kya asar?
  3. Har market ke liye saare choices DOBARA karne padenge?

Aur uska jawab "haan main theek kar dunga" nahi ho sakta —
uska jawab ek DESIGN DECISION hona chahiye.
```

## 🔍 Multi-market poore flow ko GUNA kar deta hai
```
markets = ["GB", "FR"] hone par:

✅ Pehle se per-market hai:
   market_budgets · base_bids

🔴 DOBARA karna padega:
   Deals · Audiences · Rate card · Locations · Product categories ·
   ASIN validation · Forecast · Creatives (language!) · Creative approval
```

## 🔴 Do concrete GAPS jo isse nikle
```
GAP 1 — Saare market-scoped APIs SINGULAR market lete hain
   Schema:  markets: list[str] = ["GB", "FR"]      ← PLURAL
   Par APIs:
     GET  /api/deals/?markets={market}                    ← singular
     POST /api/audience-sets/suggest/  {"market": "GB"}   ← 🔴 SINGULAR!
     GET  /api/rates/ctv/{market}/                        ← singular
     GET  /api/strategies/locations/{market}/             ← singular
     GET  /api/contextual-targeting/{market}/...          ← singular

   → Multi-market me HAR API N BAAR call karna padega
   → Aur N sets of results manage karne padenge
   → Document ne ye KAHIN nahi likha

GAP 2 — BudgetSplitSchema me `by_market` NAHI hai
   Abhi: by_inventory ✅ · by_duration ✅ · by_market ❌
   Par multi-market me split TEEN dimension ka ho jaata hai:
     2 markets × 2 inventories × 2 durations = 8 lines!
```

## 🎯 Unki requirement
```
Ek SCOPE DECISION chahiye. Teen options:

A) M1 = single market only      → simple, APIs se match, par v2.0 ka
                                   multi-market parsing hatana padega
B) M1 = full multi-market       → complete, par effort KAI GUNA
C) N parallel plans             → beech ka raasta, par UI complex

💡 RECOMMENDATION: A ab, par SCHEMA B ke liye taiyar rakho
   → markets: list[str] schema me PLURAL rakho (migration na pade)
   → Par M1 flow me: len(markets) > 1 → agent bole
     "Multi-market M1 me support nahi hai. Main GB ka plan banata hun.
      FR ke liye alag strategy banani padegi."
```

## ❓ Unka purpose
```
🔴 Effort aur estimate ka faisla hai.

v2.0 ne multi-market parsing ADD kiya (§7.1 me ➕ NEW)
Par uska flow impact KAHIN analyse nahi kiya.

→ Agar M1 me multi-market hai, to effort kai guna
→ Aur ye BUILD SE PEHLE tay hona chahiye, build ke beech me discover nahi
```

## ✅ Ek achhi khabar jo isse nikli
```
🔴 3P inventory par reach ADD nahi kar sakte
   (wahi insaan Prime aur Netflix dono dekh sakta hai — double counting)

✅ PAR multi-market me reach ADD KAR SAKTE HO
   (GB ka banda aur FR ka banda ALAG log hain)
   GB reach 118,000 + FR reach 82,000 = 200,000 ✅ VALID

→ Ye document me likhna chahiye — do similar-lagne wale case, ulte jawab
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| *"v2.0 me multi-market tha ya nahi?"* | Parsing me **tha** — §7.1 me *"UK and France → ["GB","FR"]"* ➕ NEW likha hai. Par uska **flow impact analyse nahi kiya gaya.** Wahi gap hai. |
| *"Kitna extra kaam hai?"* | Har market-scoped API N baar call, N result sets manage, budget split 3-dimensional, creatives per language, forecast per market. **Materially bigger build.** |
| *"To M1 me kar sakte hain?"* | Ho sakta hai, par mera recommendation nahi — schema plural rakho, flow single-market rakho. Isse M2 me migration nahi lagega aur M1 jaldi deliver hoga. |
| *"Reach add kar sakte hain multi-market me?"* | ✅ Haan — GB aur FR ke log alag hain. Ye 3P case ka **ulta** hai, jahan add nahi kar sakte. Dono document me likhne chahiye. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | 🔴 **Multi-market M1 me hai ya M2?** | **Ye ek decision hai** — step order, budget split dimensions, N× API calls, aur estimate — sab isi par depend karte hain |
| 2 | Multi-market me creative per language chahiye? | Step 9 ka scope |
| 3 | Multi-market me currency ka rule kya ho? | #9 se juda |

## 🏷️ Ek line me
> *"Multi-market support kar rahe ho? Uska flow par kya asar hai? Har market ke liye sab dobara?"*

**Severity:** 🔴 HIGH — scope decision + do concrete gaps

---
---

# COMMENT #9 — Single market me market ki currency use karo

**📍 Kahan:** Step 1 → **Primary currency** → **"Required"**

## 📄 Document me pehle kya tha
```
Primary currency | DROPDOWN | REQUIRED | ✅ Unchanged. EUR, GBP, USD
                    ↑           ↑
              "Dropdown" + "Required" = trader ko chunna hai
```

## 💬 David ne kya likha
> *"just use market currency if single market"*

## 🔍 Comment ka matlab
```
Agar sirf EK market hai, to us market ki currency HI use karo:
  markets = ["GB"]  →  currency = GBP    (automatic)
  markets = ["US"]  →  currency = USD
  markets = ["DE"]  →  currency = EUR

Poochhne ki zaroorat nahi.

🔴 Aur dhyan do — "PRIMARY currency" ka naam hi batata hai ki
   ye MULTI-market ka concept hai. "Primary" = kai me se main wali.
   Single market me "primary" ka koi matlab hi nahi!
```

## 🔴 Aur SABSE ZAROORI — document ye PEHLE SE karta hai!
```
§7.1 (Entity Normalisation) me:
  | UK | markets: ["GB"], primary_currency: "GBP" | ✅ Original |
                           ↑
        🔴 CURRENCY MARKET SE DERIVE HO RAHI HAI — PEHLE SE!

Par Step 1 ka field matrix kehta hai "Dropdown | Required"

╔══════════════════════════════════════════════════════════════════════════╗
║  DOCUMENT APNE AAP SE CONTRADICT KAR RAHA HAI:                            ║
║  §7.1 kehta hai:   "UK se currency GBP KHUD nikal jaati hai"              ║
║  Step 1 kehta hai: "Trader dropdown se currency CHUNEGA"                  ║
║  Dono ek saath sach nahi ho sakte.                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Requirement: **Required** ✅ rahega · Source: **⚙️ DERIVED from market** |
| 2 | Type: "Dropdown" → hatao (wo UI widget hai) |
| 3 | ➕ Multi-market ka **rule define karo** — abhi kahin nahi hai |
| 4 | §7.1 aur Step 1 ka contradiction **reconcile karo** |

## ❓ Unka purpose
```
Ek bekaar sawaal hatana.

Aur multi-market me rule chahiye (abhi nahi hai):
  Option A: Trader se poochho
  Option B: Advertiser ke account ki default currency   ← 💡 best
  Option C: Sabse bade budget wale market ki currency

  💡 Suggestion: B → C → A, aur hamesha ASSUMPTION ki tarah dikhao:
     "Reporting GBP me (advertiser ka account currency). Badalna hai?"
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"Agar US company UK me campaign chala rahi hai par USD me reporting chahti hai?"* | Isi liye ye **assumption ki tarah dikhana** chahiye, chup-chaap set nahi karna: *"UK campaign — main GBP me reporting maan raha hun. Theek hai?"* Trader override kar sakta hai. |
| *"Multi-market me kya karoge?"* | Rule abhi nahi hai — main define karunga. Preference: advertiser account default → largest-budget market → poochho. Aur **#13 ne confirm kiya** ki advertiser-level defaults exist karte hain, to option B ab concrete hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Advertiser ke account me ek **default currency** field hai? *(#13 ke baad ye likely lagta hai)* |
| 2 | Multi-market me currency ka rule kya ho? |

## 🏷️ Ek line me
> *"Single market me us market ki currency use karo. Poochho mat."*

**Severity:** 🟡 MEDIUM — chhota fix, par document apne aap se contradict kar raha tha

---
---

# COMMENT #10 — KPI target value GAYAB hai

**📍 Kahan:** Step 1 → **KPI** (poora field)

## 📄 Document me pehle kya tha
```
KPI | Select | Required | 🔄 CHANGED. For CTV, reach or frequency only.
                          Was six choices; others scoped out

Yaani sirf ye pata chalta tha: KAUNSA metric naapna hai
  kpi_target_type = "reach"  ya  "frequency"
```

## 💬 David ne kya likha
> *"if frequency then you can have kpi target too of 1-5"*

## 🔍 Comment ka matlab
```
Ek NAYA FIELD chahiye:
  kpi_target_type  = "frequency"   ← KAUNSA target  (pehle se hai)
  kpi_target_value = 3             ← KITNA target   ← 🔴 MISSING!

Aur value 1 se 5 ke beech hogi.
```

## 🔴 DO PROOF ki ye field pehle se chahiye thi
```
PROOF 1 — Field ka NAAM hi bata raha hai
  Schema me: kpi_target_TYPE
                     ↑
  "TYPE" likha hai — matlab ek "VALUE" bhi hona chahiye!

PROOF 2 — Repair loop ek target ka zikr karta hai jo EXIST NAHI KARTA
  §6.2 (state machine):
    "EvaluateReach: Check if reach > 0 and FREQUENCY WITHIN TARGETS"
  §7.1 (repair loop):
    "returns estimated_unique_reach == 0 OR INSUFFICIENT FREQUENCY"

  🔴 Dono jagah TARGET se compare karne ki baat hai —
     par schema me koi target field HI NAHI!
  → Repair loop ka ek hissa IMPLEMENTABLE HI NAHI THA
```

## 🔴 Frequency TARGET vs frequency CAP — bilkul alag cheezein
```
Document me `frequency_cap` PEHLE SE hai. To kya ye wahi hai? NAHI!

╔══════════════════════════════════════════════════════════════════════════╗
║  FREQUENCY TARGET (1-5)              FREQUENCY CAP                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  "Main CHAHTA hun average ~3 ho"     "Koi 3 baar se ZYADA na dekhe"       ║
║  = OPTIMISATION GOAL (nishaana)      = HARD LIMIT (chhat)                  ║
║  DSP delivery ko PACE karta hai      DSP 4th impression BLOCK karta hai    ║
║  ➡ AIM                                ➡ CEILING                           ║
╚══════════════════════════════════════════════════════════════════════════╝

Example:
  TARGET = 3 → kuch log 1 baar, kuch 5 baar · AVERAGE 3 aayega
               Koi 7 baar bhi dekh sakta hai
  CAP = 3    → KOI BHI 4th baar NAHI dekhega
               Average 3 se KAM hoga
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | ➕ Naya field: `kpi_target_value: Optional[int] = Field(None, ge=1, le=5)` |
| 2 | Validation: Required **if** `kpi_target_type == "frequency"` |
| 3 | 🔴 Validation: `frequency_cap > kpi_target_value` (warna virodh) |
| 4 | ➕ Document karo: frequency **target** vs frequency **cap** ka farak |
| 5 | §7.1 me *"insufficient frequency"* ko **numerically define** karo |

## ❓ Unka purpose
```
1. Ek genuinely MISSING field hai
   Aur uske bina repair loop ka frequency check IMPLEMENTABLE nahi

2. Do concepts confuse ho rahe the (target vs cap)

3. Aur validation ka ek asli case hai:
   Agar target = 4 aur cap = 3 → mathematically IMPOSSIBLE
   Aur cap ka ADVERTISER DEFAULT hota hai (#13) —
   to ye virodh trader ke kuch karne ke BINA bhi ho sakta hai!
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"Reach ka bhi target hota hai?"* | **Nahi** — aur ye ek gehri baat hai. **Frequency CONTROLLABLE hai** — DSP delivery pace kar sakta hai. **Reach OUTCOME hai** — wo budget, audience, inventory aur CPM se NIKALTA hai, set nahi hota. Frequency ek **dial** hai, reach ek **meter**. |
| *"1-5 ke bahar bhi ja sakte hain?"* | David ne 1-5 kaha. 5 se upar ad fatigue territory hai. Main `ge=1, le=5` validation lagaunga. |
| *"Ye field kaise bharega — poochhega ya derive karega?"* | Ye **ASKED** hai (conditional) — kyunki ye ek genuine strategic choice hai. Par agent guidance dega: *"1-2 = chaudi reach · 3 = sabse aam · 4-5 = gehra impact par ad fatigue ka khatra. Main 3 recommend karta hun."* |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | *"Insufficient frequency"* ka matlab kya — target se **kitna neeche** repair trigger kare? |
| 2 | Frequency cap **weekly, daily ya lifetime** hai? *(Pydantic comment "weekly" kehta hai par field table me nahi likha)* |

## 🏷️ Ek line me
> *"KPI me sirf 'kaunsa metric' hai. Agar frequency chuni hai to 'kitna' bhi chahiye — 1 se 5 ke beech."*

**Severity:** 🔴 HIGH — missing field, aur uske bina repair loop ka ek hissa kaam nahi karta

---
---

# COMMENT #11 — Single market me budget ek number hai, "Table" nahi

**📍 Kahan:** Step 1 → **Market budgets** → **"Table"** (Type column)

## 📄 Document me pehle kya tha
```
Market budgets | TABLE | Required | ✅ Unchanged. Per-market budget, must be > 0
```

## 💬 David ne kya likha
> *"single market budget?"*

## 🔍 Comment ka matlab
```
"Ye 'Table' kyun hai? Agar ek hi market hai, to budget bhi EK NUMBER hoga."

Table = kai rows = kai markets
Ek market = ek row = table ki zaroorat nahi
```

## 🔴 Aur isse ek BADA structural problem nikla — "Type" column CHAAR kaam kar raha hai
```
"Table" ek UI WIDGET hai, DATA TYPE nahi!

Poore document ke Type column ki values dekho:

┌─────────────────────────────────────────────────────────────────────────┐
│ DATA TYPES (sahi jagah)                                                 │
│   String · Number · Date range · Boolean · Timestamp · Enum · URL       │
├─────────────────────────────────────────────────────────────────────────┤
│ UI WIDGETS (ye Type column me kyun hain?!)                              │
│   Dropdown · Radio · Multi-select · TABLE · Toggle · Textarea ·          │
│   Card Select · Checkbox table · Select · Chart · Display · Upload      │
├─────────────────────────────────────────────────────────────────────────┤
│ SOURCE / BEHAVIOUR (ye bhi!)                                            │
│   Fixed · Derived · Derived from file · Reference · Question · Check    │
├─────────────────────────────────────────────────────────────────────────┤
│ DOMAIN CONCEPTS (ye bhi!)                                               │
│   "3 profiles" · "Allocation (%)"                                       │
└─────────────────────────────────────────────────────────────────────────┘

🔴 Ek hi column CHAAR alag cheezein bata raha hai!
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Market budgets Type: "Table" → `list[{market, budget}]` (M1 me length 1) |
| 2 | ➕ Note: schema list rahegi (M2-ready), par trader ko **ek number** dikhega |
| 3 | 🔴 **Sab field matrices** me `Type` ko **`Data type` + `Source`** me todo |
| 4 | 🔴 **UI widgets hatao** — ye document DATA CONTRACT hai, UI SPEC nahi |

## ❓ Unka purpose
```
1. Data model shape ≠ Presentation shape
   Schema:  market_budgets: list[...] (length 1)
   Trader:  "Budget: £10,000"  ← ek simple number
   → Dono theek hain! Schema list rakho (M2 me migration na pade),
     par trader ko table na dikhao

2. 🔴 AUR EK GEHRA SABAK (jo #18 ne aur strong kiya):
   Kyunki UI widget Type column me tha, document ne GALTI SE ek
   INTERACTION MODEL specify kar diya — aur wo galat tha.

   Agar Type me sirf "list[{market, budget}]" likha hota, to
   koi "table" hi nahi hoti jispar objection ho.

   💡 UI widgets DATA CONTRACT me nahi hone chahiye — kyunki wo
      CHUP-CHAAP galat design LOCK kar dete hain
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"To schema me list rakhoge ya single value?"* | **List** — length 1 M1 me. Isse M2 me multi-market aane par koi migration nahi lagegi. Par trader ko UI me ek number dikhega. |
| *"UI widgets document se hata denge to Riddhi/Basil ko kaise pata chalega?"* | Unke **UI spec** me. Ye document data contract hai. Widget choices UI ka faisla hai, aur wahin document hone chahiye. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Ye #8 (multi-market scope) par depend karta hai — wo decision pehle chahiye |

## 🏷️ Ek line me
> *"Ek market hai to budget ek number hoga — 'Table' kyun likha hai?"*

**Severity:** 🟡 MEDIUM — par isse ek bada structural problem nikla

---
---

# COMMENT #12 — Base bid CTV me BEKAAR hai — aur repair loop tod deta hai

**📍 Kahan:** Step 1 → **Base bids** → **"Required"**

## 📄 Document me pehle kya tha
```
Base bids | Table | REQUIRED | ✅ Unchanged. Per-market base CPM bid
```

## 💬 David ne kya likha
> *"not required for CTV as defined by CPM of deals"*

## 🔍 Comment ka matlab
```
CTV me base bid ki ZAROORAT HI NAHI — kyunki daam DEAL me pehle se tay hai.

Base bid ka matlab: "main max itna CPM dene ko taiyar hun"
→ Ye AUCTION me kaam aata hai, jahan compete karna padta hai

Par CTV deals me auction hota hai?
```

## 🔴 Document ke APNE §2.3 table se jawab
```
┌────────────────────────────────┬──────────────────────────┬──────────────────┐
│ Deal Type                      │ Price                    │ Base bid chahiye?│
├────────────────────────────────┼──────────────────────────┼──────────────────┤
│ Programmatic Guaranteed (PG)   │ FIXED CPM                │ ❌ NAHI          │
│ Preferred Deals                │ FIXED CPM                │ ❌ NAHI          │
│ Private Auctions               │ FLOOR CPM, COMPETITIVE   │ 🟡 SHAYAD HAAN   │
└────────────────────────────────┴──────────────────────────┴──────────────────┘

Aur document ke SAARE deal examples "Preferred" hain:
  "Prime Video | Preferred Deal | UK - 30 | £28.88"
  "Netflix | Preferred | UK - 30 | £32.00"
                ↑ FIXED CPM. Koi bidding nahi.

🔴 To base bid ek OPEN AUCTION / DISPLAY ka concept hai —
   CTV pre-curated deals me bekaar. Yaani NON-CTV FIELD.

🔴 Aur §2.3 (business logic) SACH bolta tha, Step 1 matrix GALAT tha.
```

## 🔴🔴 SABSE BADA NATEEJA — Repair loop ka ek LEVER TOOT GAYA
```
Document ka repair loop (§7.1) — teen actions:
  Action 1: Audience bundle switch/extend
  Action 2: "Adjust base CPM bid up to market recommended floor
             (e.g. increase from £15 to £30 for Prime Video)"
  Action 3: Re-run forecasting engine

╔══════════════════════════════════════════════════════════════════════════╗
║  ACTION 2 (bid badhao) — 🔴 CTV KE LIYE INVALID HAI!                     ║
║  Preferred/PG deal me CPM FIXED hai. Bid badhane se KUCH nahi hoga.       ║
╚══════════════════════════════════════════════════════════════════════════╝

Aur #4 (audiences optional) ke saath jodo:

╔══════════════════════════════════════════════════════════════════════════╗
║  WORST CASE                                                              ║
║    • Koi audience nahi (#4)          → Action 1 nahi ho sakta             ║
║    • Preferred fixed-CPM deal (#12)  → Action 2 bekaar                    ║
║    • Re-forecast                     → wahi nateeja                       ║
║                                                                          ║
║  🔴 REPAIR LOOP KE PAAS ZERO LEVERS HAIN!                                ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Base bids: **Required → Not applicable for CTV** (ya Conditional: Private Auction only) |
| 2 | `MarketBudgetBidSchema.base_bid` → `Optional[str] = None` |
| 3 | 🔴🔴 **Repair loop Action 2 HATAO** |
| 4 | 🔴🔴 **Repair loop POORA RE-WRITE** — naye ordered levers ke saath |

## ✅ Naya repair loop — 7 ordered levers
| # | Lever | Kab lagta hai | Lock ho sakta hai? |
|---|---|---|---|
| 1 | **Doosri targeting relax karo** — location, exclusions, device | Hamesha — *PRIMARY lever* | 🔒 **Haan** (#22 — advertiser policy) |
| 2 | Audience extend karo | Agar audience hai | Nahi |
| 3 | Matching mode Exact → Similar | Agar audience hai | Nahi |
| 4 | Aur deals add karo | Hamesha | 🟡 Shayad |
| 5 | Flight dates extend karo | Hamesha | Nahi |
| 6 | Budget badhao | Trader chahiye | Nahi |
| 7 | 🔴 **Imaandari se limit batao** — *"is inventory se zyada reach possible nahi"* | Jab kuch na bache | — |

## ❓ Unka purpose
```
1. Ek bekaar field hatana (non-CTV leftover)

2. 🔴 PAR ASLI WAJAH — repair loop ka ek lever GALAT tha
   → Aur wo Wajahat ke graph me edges ban chuka hota
   → Build time par pata chalta ki wo edge kuch nahi karta
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"To repair loop kaam karega hi nahi?"* | Karega — par **naye levers** se. Primary lever ab "doosri targeting relax karo" hai. Aur agar kuch na bache, to agent **imaandari se batayega** ki is inventory se zyada reach possible nahi — jo Zero-Hallucination ke hisaab se sahi jawab hai. |
| *"Private Auction deals CTV me hote hain?"* | ⚠ Pata nahi — **poochhna hai.** Document ke saare examples Preferred hain. Agar Private Auction scope me hai to `base_bid` **conditional** rahega, delete nahi hoga. |
| *"Wajahat ka kaam kitna badlega?"* | Repair loop ke **edges** badlenge — 3 actions se 7 levers, aur kuch conditional (#22 se lock ho sakte hain). Ye ek asli graph change hai, wording nahi. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | 🔴 **Private Auction deals CTV M1 me hain?** | Agar haan, `base_bid` conditional rahega |
| 2 | Jab repair loop ke paas koi lever na bache — agent ko kya karna chahiye? | Failure behaviour define karna hai |

## 🏷️ Ek line me
> *"CTV me base bid ki zaroorat nahi — daam deal me pehle se tay hai (Fixed CPM), boli nahi lagti."*

**Severity:** 🔴🔴 VERY HIGH — field hatana chhota, par **repair loop ka lever toot jaata hai**

---
---

# COMMENT #13 — Frequency cap ka ADVERTISER-LEVEL default hota hai

**📍 Kahan:** Step 1 → **Frequency cap** → **"Optional"**

## 📄 Document me pehle kya tha
```
Frequency cap | Number | OPTIONAL | ➕ NEW. Was absent; client confirmed optional
                          ↑
              "khaali rahegi jab tak trader na bhare"
```

## 💬 David ne kya likha
> *"we have a default per advertiser"*

## 🔍 Comment ka matlab
```
Frequency cap khaali NAHI rehti — har ADVERTISER ka ek DEFAULT hota hai.

→ Advertiser ki settings se ek value AA JAATI hai
→ Trader chahe to badal sakta hai

🔴 "Optional" technically SAHI hai (trader ko bharna zaroori nahi)
   Par PRACTICALLY misleading hai (field kabhi khaali nahi rehti)

→ Phir wahi hal: Requirement kaafi nahi, SOURCE bhi chahiye
   Requirement: Optional  ✅
   Source:      🏢 ADVERTISER default
```

## 🔴🔴 SABSE BADA FINDING — "Advertiser Defaults" ek POORA MISSING CONCEPT hai
```
David: "we have a default per advertiser"
        ↑ Yaani VOW me "advertiser defaults" naam ki cheez HAI

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 PAR DOCUMENT ME YE CONCEPT KAHIN NAHI HAI!                           ║
║                                                                          ║
║  Document me advertiser ka zikr sirf yahan:                              ║
║    advertiser_id: str = Field(..., description="Parent advertiser UUID") ║
║    ← Bas ek ID. Settings/defaults ka koi zikr nahi.                      ║
║                                                                          ║
║  ❌ Koi AdvertiserDefaultsSchema — NAHI HAI                              ║
║  ❌ Koi endpoint — NAHI HAI                                              ║
║  ❌ Koi state field — NAHI HAI                                           ║
║  ❌ "advertiser settings" ka EK ZIKR BHI — NAHI HAI                      ║
╚══════════════════════════════════════════════════════════════════════════╝

🔴 Aur David ne ye TEEN BAAR confirm kiya:
   #13  frequency cap        "we have a default PER ADVERTISER"
   #15  product categories   "we have a default ON THE ADVERTISER"
   #22  device type          "set AT ADVERTISER LEVEL"

→ Teen explicit confirmations ke baad ye ek UNDENIABLE requirement hai
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Frequency cap: Requirement **Optional** ✅ · Source **🏢 ADVERTISER default** |
| 2 | 🔴 ➕ **`AdvertiserDefaultsSchema`** banao — poora naya schema |
| 3 | 🔴 ➕ **Naya endpoint** `GET /api/advertisers/{id}/defaults/` (ya asli naam) |
| 4 | 🔴 ➕ `PlanningAgentState.advertiser_defaults` — flow ke **shuru me load** |
| 5 | ➕ Naya section: "Advertiser defaults" — kaunse, kab load, override kaise |

## ❓ Unka purpose
```
1. Field ka source galat bataya gaya tha

2. 🔴 PAR ASLI WAJAH — ek POORA concept gayab tha
   Agar agent advertiser defaults load nahi karta, to:
     • Frequency cap khaali rahegi (galat)
     • Product category poochhega (bekaar — #15)
     • Device type poochhega (bekaar — #22)
     • Currency poochhega (bekaar — #9)
   → Chaar bekaar sawaal, sirf ek missing concept ki wajah se
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| *"Ye kab load hoga?"* | Flow ke **sabse shuru me** — brief extract karne se **pehle**. Kyunki kai fields inhi defaults se resolve hote hain. Isliye state machine me ek naya node chahiye: `load_advertiser_defaults`. |
| *"Trader override kar sakta hai?"* | Frequency cap — haan. Par **#22 ne ek naya farak bataya**: kuch advertiser values **DEFAULT** hain (override ho sakti hain) aur kuch **CONSTRAINT** (brand policy — override nahi). Isliye har setting ke saath `is_locked` flag chahiye. |
| *"Aur kya-kya advertiser defaults hain?"* | Teen confirmed hain (frequency cap, product categories, device type). Do likely (currency, selling location). Ek possible (approval threshold). **Poori list poochhni hai.** |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | 🔴 **Frequency cap ke alawa kaunse advertiser defaults hain?** | Schema define karne ke liye |
| 2 | Advertiser defaults fetch karne ka **asli endpoint** kya hai? | §4 catalogue me add karna hai |
| 3 | Frequency cap ka default **weekly, daily ya lifetime**? | Pydantic comment "weekly" kehta hai, field table me nahi likha |
| 4 | Kaunse settings **LOCKED** ho sakte hain (override nahi)? | #22 se juda |

## 🏷️ Ek line me
> *"Frequency cap khaali nahi rehti — har advertiser ka ek default hota hai jo automatically lag jaata hai."*

**Severity:** 🔴 HIGH — chhota comment, par ek **poora missing concept** + missing API + missing schema

---
---

# COMMENT #14 — Format hamesha `streaming_tv` hai · Prime Video ek PROVIDER hai

**📍 Kahan:** Step 1 → **Formats** → **"Required"**

## 📄 Document me pehle kya tha
```
Formats | Fixed | Required | 🔄 CHANGED. For M1, STREAMING_TV AND PRIME_VIDEO
                             ONLY. Display and online_video removed from scope
                             ↑
                        DO values
```

## 💬 David ne kya likha
> *"is always streaming_tv"*

## 🔍 Comment ka matlab — ye ek LEVEL ki galti hai
```
`prime_video` ek FORMAT nahi hai — wo ek PROVIDER hai!

╔══════════════════════════════════════════════════════════════════════════╗
║  FORMAT = ad ka KISM / channel                                            ║
║    display · online_video · streaming_tv · audio                          ║
║    ← CTV ka format = "streaming_tv". Bas ek.                              ║
║                                                                          ║
║  PROVIDER = kaun DIKHA raha hai                                           ║
║    Prime Video · Netflix · Hulu · Disney+                                  ║
║    ← Ye streaming_tv ke ANDAR aate hain                                   ║
╚══════════════════════════════════════════════════════════════════════════╝

Analogy:
  Format = "TV"                   ← medium
  Provider = "Star Plus", "Sony"  ← channel

  Tum ye nahi likhoge: media = ["TV", "Star Plus"]
  Tum likhoge:         media = "TV", channel = "Star Plus"
```

## 🔴 DO PROOF document ke ANDAR
```
PROOF 1 — `provider` field PEHLE SE hai
  SelectedDealSchema me:
    provider: str = Field(..., description="e.g. Prime Video, Netflix, Disney+")
                                                ↑
        🔴 PRIME VIDEO YAHAN PEHLE SE HAI — provider ki tarah!
  → Step 1 me use FORMAT ki tarah dobara likhna = DUPLICATION, galat level par

PROOF 2 — Step 2 ka apna API call David se SEHMAT hai
  Step 2 me likha hai:
    "Fetched via GET /api/deals/?markets={market}&formats=streaming_tv"
                                                    ↑↑↑↑↑↑↑↑↑↑↑↑
                              🔴 SIRF streaming_tv! prime_video NAHI!

  Step 1 kehta hai: formats = ["streaming_tv", "prime_video"]
  Step 2 ka API:    formats=streaming_tv
  → DOCUMENT APNE AAP SE CONTRADICT KAR RAHA HAI — aur Step 2 sahi hai
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Formats: Required → **system constant `["streaming_tv"]`** (ya row hi hatao) |
| 2 | `FormatEnum.PRIME_VIDEO` → annotate: *"not a format — provider, see SelectedDealSchema"* |
| 3 | ➕ Naya note: **Format vs Provider** ka farak |
| 4 | v1.1.0 create payload example theek karo: `"formats": ["prime_video"]` → `["streaming_tv"]` |

## ❓ Unka purpose
```
Ek TAXONOMY galti confusion phailati hai.

Agar prime_video ko format maana, to:
  • Trader confuse hoga ("Netflix ka format kya hai?")
  • Schema me duplication (format + provider dono me Prime Video)
  • API call galat ban sakti hai

Aur ye ek CONSISTENT BLIND SPOT hai — David ne 4 baar level-confusion pakdi:
  #11  data type vs UI widget          (Type column me "Table")
  #14  format vs provider              (ye)
  #21  buying scope vs delivery filter (markets vs location)
  #22  format vs device                (streaming_tv vs Connected TV)
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"Par v1.1.0 me `"formats": ["prime_video"]` bheja gaya tha?"* | Haan — aur wo galat tha. v1.1.0 me deals table ka heading bhi *"Prime Video Deals"* tha. **v2.0 ka Step 2 sahi hai** (`formats=streaming_tv`), Step 1 galat. ⚠ Par confirm karna hai ki Amazon DSP API kaunsi values accept karta hai. |
| *"To Prime Video vs Netflix ka farak kahan capture hoga?"* | Step 2 me — `SelectedDealSchema.channel` (jo `provider` se rename hoga, #26). Aur `inventory_tier` bhi wahin hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Amazon DSP API kaunsi **format values** accept karta hai — `streaming_tv` only, ya `prime_video` bhi? |

## 🏷️ Ek line me
> *"Format hamesha `streaming_tv` hai. Prime Video ek format nahi — wo ek provider hai, jo Step 2 me tay hota hai."*

**Severity:** 🟡 MEDIUM — par ek taxonomy galti, aur document apne aap se contradict kar raha tha

---
---

# COMMENT #15 — Product category ADVERTISER se aati hai, trader se nahi

**📍 Kahan:** Step 1 → **Product categories** → **"Required for video"**

## 📄 Document me pehle kya tha
```
Product categories | Multi-select | REQUIRED FOR VIDEO | ✅ Unchanged.
                     Fetched via GET /api/contextual-targeting/{market}/product-categories/
```

## 💬 David ne kya likha
> *"we have a default on the advertiser, or maybe could imply from the brief"*

## 🔍 Comment ka matlab
```
Do sources diye — dono trader se poochhne se BEHTAR:
  1. 🏢 Advertiser ke record me pehle se ek default hai
  2. 🧠 Ya brief se khud nikaal lo

🔴 Aur ye ADVERTISER DEFAULTS ka DOOSRA confirmation hai (#13 ke baad)
```

## 🔍 Kyun product category advertiser-level hai?
```
Sochо — kya BrightPath ki product category HAR CAMPAIGN me badalti hai?

  BrightPath  → hamesha "Education"
  Nike        → hamesha "Apparel / Footwear"
  Coca-Cola   → hamesha "Food & Beverage"

  🔴 NAHI BADALTI! Ye ADVERTISER ka guṇ hai, CAMPAIGN ka nahi.

╔══════════════════════════════════════════════════════════════════════════╗
║  Isko HAR CAMPAIGN me dobara poochhna CONCEPTUALLY GALAT hai               ║
║  Bilkul jaise: tum bank me har transaction par apna naam nahi likhte —     ║
║  wo account me pehle se hota hai                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## ✅ Poora fallback chain — TEEN sources
```
1️⃣ 🏢 ADVERTISER DEFAULT (best)     ← David ne bataya
   BrightPath → Education
        ↓ (agar na ho)
2️⃣ 🧠 BRIEF SE IMPLY               ← David ne bataya
   "education website" → Education
        ↓ (agar brief me clear na ho)
3️⃣ 🔌 ASIN VALIDATION RESPONSE      ← 🔴 DOCUMENT ME PEHLE SE HAI!
   POST /api/contextual-targeting/GB/asin-validation/
   ← {"valid_asins": [{"asin": "B08N5WRWNW", "title": "...",
                        "product_category": "Electronics"}]}
                                        ↑ 🔴 YAHAN!
        ↓ (agar kuch na mile)
4️⃣ 💬 TAB trader se poochho (aakhri sahara)

🔴 Source 3 §4.2 me PEHLE SE hai — par kabhi USE nahi kiya gaya!
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Requirement: *"Required for video"* → **Required** (CTV hamesha video hai — #14) |
| 2 | Source: **🏢 ADVERTISER → 🧠 INFERRED → 🔌 API** (fallback chain) |
| 3 | `AdvertiserDefaultsSchema` me `product_categories` add karo |
| 4 | §4.2 ASIN validation me note: response ka `product_category` is field ko auto-fill kar sakta hai |

## ❓ Unka purpose
```
1. Ek bekaar sawaal hatana

2. 🔴 Advertiser defaults ka DOOSRA confirmation — concept undeniable ban gaya

3. Ek free signal use nahi ho raha tha
   ASIN validate karne par product_category MUFT me mil jaati hai —
   par document ne use kabhi wire nahi kiya
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"Ek advertiser ki kai categories ho sakti hain?"* | Ho sakti hain — schema `list[int]` hai. Par default advertiser record se aayega, aur trader add/remove kar sakta hai. |
| *"'Required for video' kyun hataya?"* | CTV **hamesha** video hai (#14 — format constant `streaming_tv`). To "for video" wali condition **redundant** hai — wo v1.1.0 se aayi jahan Display bhi tha. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Advertiser record me product category kaise store hai — ek ya kai? |
| 2 | ASIN validation ka `product_category` field is Step 1 field ko auto-fill karne ke liye reliable hai? |

## 🏷️ Ek line me
> *"Product category advertiser ke record me pehle se hoti hai — ya brief se nikal aati hai. Poochhne ki zaroorat nahi."*

**Severity:** 🔴 HIGH — advertiser defaults ka doosra confirmation

---
---

# COMMENT #16 — Selling location Step 1 se HATAO

**📍 Kahan:** Step 1 → **Selling location** → **"Required"**

## 📄 Document me pehle kya tha
```
Selling location | Radio | REQUIRED | ✅ Unchanged.
                                      ON_AMAZON or NOT_SOLD_ON_AMAZON
```

## 💬 David ne kya likha
> *"can leave out"*

## 🔍 Comment ka matlab
```
"Can leave out" = isko Step 1 se HATA DO.

Do wajah:

1️⃣ Ye TRACKING ka sawaal hai, PLANNING ka nahi
   Step 1 ka maksad: "PLAN kya hai?" (naam, budget, dates, market)
   Selling location:  "MEASUREMENT kaise hoga?" (ASIN ya ad tag)
   → v2.0 ne already ASIN aur ad-tag conversions Step 11 me bheje hain
   → To selling location bhi unke SAATH jaana chahiye

2️⃣ 🔴 Ye bhi ADVERTISER ka attribute hai
   Kya "Amazon par bechta hai ya nahi" HAR CAMPAIGN me badalta hai?
     BrightPath → courses apni website par (aur ek book Amazon par)
     Nike       → Amazon par bhi bechta hai
     UK Govt    → kuch bechta hi nahi
   → Mostly ADVERTISER ka guṇ hai, campaign ka nahi!
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | 🔴 Step 1 se **row HATAO** |
| 2 | Step 11 me le jao — wahan *"Sells on Amazon?"* question pehle se hai |
| 3 | `AdvertiserDefaultsSchema` me `product_location` add karo (default, override possible) |

## ❓ Unka purpose
```
1. Step 1 ka scope saaf karna — planning vs measurement

2. 🔴 AUR ISSE Open Question #1 SOLVE HONE LAGA
   Document ka sabse dohraya gaya ⚠ (do baar likha gaya):
     "product_location aur asin_numbers POST /strategies/ me chahiye
      (Step 8), par Step 11 me collect ho rahe hain — timing conflict"

   #16 + #17 ne Option A imply kiya (collect later + patch)
   Aur #28 ne SEEDHA confirm kiya

3. Ye ADVERTISER-ATTRIBUTE pattern ka teesra case hai (#13, #15, #16)
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"Par Step 8 ka `POST /strategies/` `product_location` maangta hai?"* | Isi ka timing conflict tha. **#28 ne answer diya**: *"they can be updated on the strategy after creation."* To Step 8 me advertiser record se aa jaayega, ya baad me patch ho jaayega. |
| *"Ek advertiser ke do campaigns me alag selling location ho sakti hai?"* | Ho sakti hai (ek Amazon par, ek D2C site par). Isliye ye ek **advertiser default** hai jo **per-campaign override** ho sakta hai — frequency cap jaisa. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | `product_location` **advertiser record me** store hota hai, ya Step 11 me poochhna hai? |

## 🏷️ Ek line me
> *"Selling location ka sawaal Step 1 se hata do."*

**Severity:** 🔴 HIGH — Open Question #1 ka aadha jawab + advertiser-attribute pattern

---
---

# COMMENT #17 — Product ASINs baad me aate hain

**📍 Kahan:** Step 1 → **Product ASINs** → **"Conditional"**

## 📄 Document me pehle kya tha
```
Product ASINs | Textarea | CONDITIONAL | 🔄 MOVED. Still required if
                ON_AMAZON, but the validation and collection now happens
                at Step 11 (tracking setup). SEE OPEN QUESTION BELOW
```

## 💬 David ne kya likha
> *"comes later"*

## 🎉 Ye PEHLA comment hai jahan David v2.0 se SEHMAT hai!
```
Document ne already kaha tha ki ASIN Step 11 me move hua.
David: "comes later" — WAHI baat!

→ 16 comments ke baad, pehli baar David keh raha hai "haan ye theek hai"

🔴 Bas ek chhoti baat: agar wo BAAD me aata hai,
   to Step 1 ke table me LIST hi mat karo.

Document ne row ko Step 1 me RAKHA tha (note ke saath).
David keh raha hai — table se NIKAAL do.
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Step 1 se **row hatao** — Step 11 me already hai |
| 2 | ✅ **Open Question #1 RESOLVED mark karo** (dono jagah — page 8 aur page 18) |

## ❓ Unka purpose
```
Jo cheez baad me aati hai, wo Step 1 ki list me confusion paida karti hai.

Aur #16 ke saath milkar ye document ka SABSE BADA open question solve karta hai:

╔══════════════════════════════════════════════════════════════════════════╗
║  OPEN QUESTION #1 — RESOLVED                                             ║
║  ANSWER: Option A — collect later + update                                ║
║                                                                          ║
║  Step 1:   ❌ selling location HATAO  ·  ❌ product ASINs HATAO            ║
║  Step 8:   product_asins: [] · product_location advertiser record se      ║
║  Step 11:  ASIN collect + validate → UPDATE strategy · ad tag + conversions║
╚══════════════════════════════════════════════════════════════════════════╝
```

## ⚠ Ek self-correction jo ismein hui
```
Pehle maine Option B recommend kiya tha (ASIN Step 1 me rakho) — GALAT tha.

Aur jab maine Option A accept kiya, maine saboot ye diya:
  "§4.2 ka create payload example `product_asins: []` bhejta hai —
   yaani khaali ASIN accept hota hai"

🔴 PAR #24 ne bataya ki wo example `POST /api/strategies/` ka tha,
   aur CTV ke liye shayad `simple-strategies` use hoga.
   → Mera SABOOT galat endpoint ka tha

✅ Phir #28 ne SEEDHA jawab de diya — to saboot ki zaroorat hi nahi rahi

💡 Reply me ye distinction saaf karni chahiye:
   "Conclusion sahi tha, justification galat endpoint ka tha"
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"To Step 8 ke payload me ASIN kya bhejenge?"* | `[]` — khaali array. Aur #28 ne confirm kar diya ki baad me update ho sakta hai. |
| *"Update kaise hoga?"* | `PATCH /api/strategies/{id}/` — par ⚠ **ye endpoint §4 catalogue me hai hi nahi.** Add karna padega. Aur #24 ke baad, iska bhi CTV variant ho sakta hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Update ka endpoint kya hai — `PATCH`, `PUT`, ya dedicated? *(#24 ke CTV family sawaal me add karo)* |

## 🏷️ Ek line me
> *"ASIN baad me aata hai — to Step 1 ke table me list hi mat karo."*

**Severity:** 🟡 MEDIUM akele me — **par #16 ke saath 🔴 HIGH**, kyunki dono Open Question #1 resolve karte hain

---
---

# COMMENT #18 — Deals ki TABLE hatao — agent khud match kare

**📍 Kahan:** Step 2: CTV Inventory → **Selected deals** → **"Checkbox table"**

## 📄 Document me pehle kya tha
```
Selected deals | CHECKBOX TABLE | Required | ✅ Core concept unchanged.
                 Fetched via GET /api/deals/?markets={market}&formats=streaming_tv

Aur v1.1.0 ka table example:
┌──────────────────────────────────────────┬───────────┬────────┬─────┐
│ Deal Name                                │ Deal Type │ CPM    │ [x] │
├──────────────────────────────────────────┼───────────┼────────┼─────┤
│ Prime Video | Preferred Deal | UK - 30   │ Preferred │ £28.88 │ [x] │
└──────────────────────────────────────────┴───────────┴────────┴─────┘
                                                          ↑
                            Trader deal ke naam padhe, CPM compare kare,
                            checkbox tick kare
```

## 💬 David ne kya likha
> *"In majority of cases we want to pick the deals based on the requirements of the brief which we can do if we know the market, duration and channel. Optional ROS / genre and the different targeting types mentioned later. They may provide a deal id if they have 1 in mind but we want to remove the technical need to select deals from a table. We don't surface the underlying deal choices to the user - only the CPM"*

## 🔍 Comment ka matlab — SAAT claims ek me
| # | David ka hissa | Matlab |
|---|---|---|
| 1 | *"we want to pick the deals"* | 🔴 **AGENT** deals chunega, trader nahi |
| 2 | *"based on the requirements of the brief"* | Brief se requirements nikaal kar match karega |
| 3 | *"if we know the market, duration and channel"* | Teen input kaafi hain |
| 4 | *"Optional ROS / genre and targeting types"* | Plus optional refinements |
| 5 | *"may provide a deal id if they have 1 in mind"* | ⚙️ **Escape hatch** — trader deal ID de sakta hai |
| 6 | *"remove the technical need to select deals from a table"* | 🔴 **Table HATAO** |
| 7 | *"We don't surface the underlying deal choices — only the CPM"* | 🔴🔴 **Trader ko deals DIKHENGI HI NAHI** |

## 🔴 Flow ULTA ho jaata hai
```
╔══════════════════════════════════════════════════════════════════════════╗
║  ❌ DOCUMENT:  DEAL PEHLE, TARGETING BAAD ME                              ║
║     Trader deal chunta hai (table se)                                    ║
║     → Us deal me jo targeting hai, wo mil jaati hai                       ║
║     → Trader ko BAAD ME pata chalta hai kya mila                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ✅ DAVID:  REQUIREMENTS PEHLE, DEAL BAAD ME                             ║
║     Trader apni ZAROORAT batata hai (channel, genre, targeting)           ║
║     → Agent us zaroorat se MATCHING deal DHOONDHTA hai                    ║
║     → Trader ko CPM dikhta hai                                           ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 Trader kya chunta hai vs agent kya chunta hai
| TRADER — strategic | AGENT — technical |
|---|---|
| Kaunse **platforms**? (Prime / Netflix / Disney+) | Kaunsi **deal ID**? |
| ROS ya specific **genre**? | Us genre ki kaunsi deal? |
| Kaunsi **targeting**? | Kaunsi deal wo support karti hai |
| Kitna **budget**? | Deal type · inventory tier derive karna |

**🎯 Trader "KYA CHAHIYE" batata hai. Agent "KAISE MILEGA" nikaalta hai.**

## 🎉 AUR EK ZABARDAST BAAT — Kareem ne ye pattern PEHLE HI bana liya tha!
```
Document ka Tier 3 (Disney+) treatment dekho:

  "➕ NEW — Curation capture (for 3P-needs-curation tier): When deals
   can't be selected yet (Disney+ etc.), the agent captures what VOW
   needs to curate later: genres, durations, targeting preferences,
   budget, flight dates."

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 YE BILKUL DAVID KA MODEL HAI!                                        ║
║                                                                          ║
║  Tier 3 me: "deal nahi hai, to trader ki REQUIREMENTS lo"                ║
║  David: "SAB TIERS me requirements lo, deals mat dikhao"                  ║
║                                                                          ║
║  → Kareem ne SAHI pattern likha tha (Tier 3 ke liye)                     ║
║  → Bas usko Tier 1 aur 2 par apply nahi kiya                             ║
║  → Wahan v1.1.0 ka checkbox table chhod diya                             ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Reply me ye likhna BAHUT strong hoga — ownership dikhata hai
```

## ✅ Kya SURFACE hoga, kya HIDE
| ✅ Trader ko dikhega | ❌ Trader ko nahi dikhega |
|---|---|
| Channel / provider — *"Prime Video"* | Deal name |
| CPM — *"£31.50"* | Deal ID |
| Estimated impressions | Deals ki poori list |
| Genre (agar specific hai) | `ad_lengths`, internal fields |
| 🔴 **Tier capability** (reach forecast milega ya nahi) | Deal type — ⚠ **par PG ka warning dena zaroori** |

## ⚠ Ek EXCEPTION — PG deal ka warning
```
#12 ke context me: PG deal me "poora budget owed" aur "pause nahi kar sakte"

Agar agent CHUP-CHAAP PG deal chun le, aur deal type dikhe hi nahi —
to trader ko pata hi nahi chalega ki uska £6,000 COMMIT ho gaya!

🔴 Isliye: deal IDENTITY hide karo, par COMMITMENT ka warning DO:
  "Prime Video, CPM £31.50, 190,476 impressions.
   ⚠ Ye ek Programmatic Guaranteed deal hai — poora £6,000 commit ho
     jaayega aur pause nahi kar sakte. Preferred deal chahiye (£33.20)?"
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Selected deals Type: "Checkbox table" → `list[SelectedDealSchema]` |
| 2 | Source: 🔴 **🤖 AUTO-MATCHED** (market + duration + channel se) |
| 3 | ➕ Naye fields: `channel` (strategic choice) · `ros_or_genre` · `specific_deal_id` (escape hatch) |
| 4 | ➕ Naya schema: `DealMatchCriteriaSchema` |
| 5 | ➕ Sub-sections: *"Deal matching, not deal selection"* aur *"What is surfaced vs internal"* |
| 6 | State machine: `select_inventory` → **`match_inventory`** |

## ❓ Unka purpose
```
1. Deal selection ek TECHNICAL kaam hai, STRATEGIC nahi
   Trader ka asli faisla: "Prime Video par chalao, education content ke saath"
   Deal ID chunna: bas plumbing hai

2. 🔴 YAHI POORE PRODUCT KA MAKSAD HAI
   Task slide: "a form that fills itself in as you chat"
   → Agar trader ko phir bhi table se checkbox tick karna pade,
     to product ne KUCH NAHI BADLA — bas wizard ko chat me daal diya

3. Deal names insaan ke padhne ke liye nahi bane
   "Prime Video | Preferred Deal | UK - 30 - ROS"
   → "ROS" kya hai? "Preferred" kya hai? Naye trader ko samajh nahi aayega
   → Aur galat deal tick karne se poora plan galat

4. Escape hatch se azadi bachi rehti hai
   Jo trader jaanta hai, wo deal ID de kar override kar sakta hai
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"Agar agent galat deal chun le to?"* | Trader ko CPM aur impressions dikhte hain — galat deal turant CPM me dikhega. Aur escape hatch hai: trader specific deal ID de sakta hai. Plus tier capability dikhti hai (reach forecast milega ya nahi). |
| 🔴 *"Trader ko pata kaise chalega ki usse kya mila?"* | Provider, CPM, impressions aur tier capability — chaar cheezein dikhti hain. **Deal ka NAAM us se koi extra information nahi deta** — wo bas ek code hai. Aur genre bhi dikhta hai agar specific hai. |
| *"Agar kai deals match karein?"* | ⚠ **Ye ek open question hai** — matching logic define karni padegi. Sabse sasta? Sabse relevant? Best forecast? **Poochhna hai.** |
| *"Agar koi deal match na kare?"* | ⚠ Bhi open — failure protocol chahiye. |
| *"Genre upsell feature khatam ho gaya?"* | **Nahi** — wo bach jaata hai. Genre upsell content type + CPM dikhata hai, deal identity nahi: *"Prime Video ROS £18.22 → 439,000 imp vs Sports £22.07 → 362,000 imp."* David ke *"only the CPM"* se bilkul match karta hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | 🔴🔴 **Deal ki built-in targeting structured metadata me hai?** | **BLOCKING** — agar sirf deal ke NAAM me hai, to agent ko string parse karni padegi, jo Zero-Hallucination ke khilaaf hai |
| 2 | PG deal auto-select karna chahiye ya kabhi nahi? | Paisa commit ho jaata hai |
| 3 | Agar kai deals match karein — kaise pick kare? | Matching logic |
| 4 | Agar koi deal match na kare — kya kare? | Failure protocol |
| 5 | Naming: "channel" / "channels" / `provider` — kaunsa? | *(#26 ne resolve kiya: **channel**)* |

## 🏷️ Ek line me
> *"Trader ko deals ki table se checkbox tick karwana technical kaam hai. Agent ko brief se khud deal chunni chahiye. Trader ko deal ka naam nahi — sirf CPM."*

**Severity:** 🔴🔴 VERY HIGH — poora Step 2 ka interaction model badalta hai

---
---

# COMMENT #19 — Amazon audiences 3P par BHI lagti hain

**📍 Kahan:** Step 4 Audiences → **Constraints for CTV** → **"Netflix/Disney"**

## 📄 Document me pehle kya tha
```
Constraints for CTV:
  • "Amazon audiences ONLY APPLY to Amazon-owned inventory.
     For Netflix/Disney, their own targeting applies"
                ↑
        "ONLY" — ek absolute statement
```

## 💬 David ne kya likha
> *"can use amazon audiences too"*

## 🔍 Comment ka matlab
```
Amazon audiences Netflix/Disney par BHI lag sakti hain.
"ONLY apply to Amazon-owned" — GALAT hai.

🔴 Aur ye wahi galti hai jo #1 me thi — DOOSRI jagah:
   #1  → §2.3 tier table ka "Audiences" column
   #19 → Step 4 ka "Constraints" list

   ✅ Aur Note 1 me ye PEHLE SE flag kiya gaya tha:
      "Also corrected in: the Targeting step constraints"
   → Prediction sahi tha
```

## ⚠ Aur ye mere ek claim ko GALAT batata hai
```
Note 1 me maine likha tha:
  "On 3P inventory the publisher does not pass viewer identity...
   Amazon can THEREFORE ONLY target on what the publisher sends,
   which is why device-level is the reliable case."

🔴 Ye claim OVER-CLAIM tha.

Maine maan liya tha: "identity nahi milti to audience targeting IMPOSSIBLE"
Par David keh raha hai Amazon audiences 3P par KAAM KARTI HAIN.

→ Amazon ke paas koi tarika hai (identity resolution / device graph /
  data partnership). Wo mechanism mujhe nahi pata, par EXIST karta hai.

✅ SAHI framing:
   Amazon audiences 3P par lag SAKTI hain
   Par capability "MAY BE limited" — deal/provider ke hisaab se
   Ye ek CHOICE hai, ek DEEWAR nahi

💡 Reply me ye SAAF maanna hai — apni galat wajah defend nahi karni
```

## 🔴 Do bade consequences
```
CONSEQUENCE 1 — Tier table ka "Audiences" column DIFFERENTIATOR nahi raha
  Agar Amazon audiences sab tiers par lagti hain, to tiers me ASLI farak
  sirf DO cheezon ka hai:
    1. Reach forecast milta hai ya nahi
    2. Deal abhi available hai ya curate karani padegi
  → Table SIMPLER aur SAHI ho jaata hai

CONSEQUENCE 2 — 🔴 Effective CPM ka ganit WIDEN hota hai
  #2 ka rule: fee DATA SOURCE use karne par lagti hai
  Aur ab Amazon audiences 3P par bhi lag sakti hain
  → To NETFLIX PORTION PAR BHI AMAZON DATA FEE LAG SAKTI HAI!

  Document (aur mera #2 ka example) maanta tha ki fee sirf Amazon
  portion par lagti hai. Wo assumption GALAT tha.

  Ab TEEN scenarios compare karne padenge:
    1. Koi audience nahi        → 332,756 imp · fee £0
    2. Amazon audiences DONO par → 313,417 imp · fee dono par  ← NAYA
    3. Amazon on Prime, SSP on Netflix → 311,191 imp
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | *"Amazon audiences only apply to Amazon-owned"* — **hatao**, choice likho |
| 2 | §2.3 tier table: Audiences column me choice dikhao (dono 3P rows) |
| 3 | ➕ Note: Audiences column ab tiers ko **differentiate nahi karta** |
| 4 | 🔴 **Teen effective-CPM scenarios** ka comparison |
| 5 | ⚠ Note 1 ka explanation theek karo (over-claim tha) |
| 6 | Repair loop wording: 3P par widen kar sakte, **verify nahi** |

## ❓ Unka purpose
```
1. Ek absolute statement galat tha — aur wo DO jagah tha

2. Ek option chhup gaya tha
   Agar agent maane ki 3P par Amazon audiences nahi lagti,
   to wo trader ko wo option DIKHAYEGA HI NAHI

3. Effective CPM ka ganit galat tha
   → Aur wo trader ke faisle par seedha asar daalta hai
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"To tier table me Audiences column ki zaroorat hi nahi?"* | Column reh sakta hai (choice dikhane ke liye), par wo ab **differentiator nahi** hai. Asli farak reach forecast aur deal availability ka hai. |
| 🔴 *"To 3P par repair loop kaam karega?"* | Audience **widen kar sakte ho**, par effect **verify nahi kar sakte** — 3P reach report nahi karta. Isliye agent imaandari se batayega: *"Maine Netflix portion par bhi audience chaudi ki, par uska asar confirm nahi kar sakta."* |
| *"Netflix par Amazon audience lagane se kya milega exactly?"* | ⚠ **Pata nahi** — capability "may be limited" hai. Exact list poochhni hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Amazon audiences **aur** SSP targeting — dono ek hi 3P deal par lag sakti hain? |
| 2 | **AMC audiences** bhi 3P par lagti hain? (constraint list unhe "conditional" kehti hai) |
| 3 | 3P par Amazon targeting kitni limited hai — exact capability list? |

## 🏷️ Ek line me
> *"Tumne likha Amazon audiences SIRF Amazon inventory par lagti hain — galat. Wo Netflix/Disney par bhi lag sakti hain."*

**Severity:** 🔴 HIGH — absolute statement galat + effective CPM ka ganit widen hota hai

---
---

# COMMENT #20 — `bundles.narrow/balanced/broad` API me NAHI hai

**📍 Kahan:** Step 4 Audiences → ⚠ **Open question** → **`bundles.narrow/balanced/broad`**

## 📄 Document me pehle kya tha
```
⚠ Open question: the suggest endpoint's response shape. v1.1.0 assumed it
  returns bundles.narrow/balanced/broad. The real endpoint may return a
  flat list that we group ourselves. Confirm against the real API.

Aur §4.2 me poora example:
  POST /api/audience-sets/suggest/
  ← { "bundles": {
        "narrow":   [{"id": "aud_101", "vcpm": "1.85", ...}],
        "balanced": [{...}, {...}],
        "broad":    [{...}, {...}, {...}]
      } }
```

## 💬 David ne kya likha
> *"not currently supported"*

## 🎉 Ye DOOSRA OPEN QUESTION RESOLVE ho gaya
```
Document ne KHUD ye sawaal poochha tha — David ne JAWAB de diya.

Sawaal: "Kya suggest endpoint bundles shape deta hai?"
Jawab:  "NOT CURRENTLY SUPPORTED" — nahi deta.

💡 AUR YE EK JEET HAI:
   Tumne v2.0 me ye ASSUME karke aage nahi badha — ⚠ FLAG kiya.

   🔴 Agar flag na kiya hota:
      → Schema `bundles` shape ke hisaab se ban jaati
      → Wajahat code likh deta
      → Build time par API se kuch aur aata
      → POORA AUDIENCE MODULE DOBARA LIKHNA PADTA

   ✅ Flag kiya, to code likhne se PEHLE pata chal gaya
```

## 🔍 Comment ka matlab
```
❌ Document ka assumption:
   API PEHLE SE grouping karke deta hai (narrow/balanced/broad)

✅ Reality:
   API ek FLAT LIST deta hai. Grouping HUM karenge.

🔴 SABSE BADA NATEEJA:
   TEEN PROFILES EK AGENT-SIDE CONSTRUCT HAIN — API FEATURE NAHI!
```

## 🔴 Teen comments milkar 3 profiles ka matlab POORA badal dete hain
| Comment | Pehle kya tha | Ab kya hai |
|---|---|---|
| **#2** | Profiles **cost** me alag hain | ❌ Cost **SAME** (same data source par) |
| **#4** | Ek profile chunna **MANDATORY** | ❌ **OPTIONAL** |
| **#20** | API profiles **DETA** hai | ❌ **AGENT banata** hai |

```
🔴 To 3 profiles ab ye hain:
   • Ek AGENT-SIDE presentation device (API feature nahi)
   • Sirf REACH aur PRECISION me alag (COST me nahi)
   • Aur OPT-IN (mandatory nahi)

→ Document ke current description se BAHUT alag
```

## 🎯 Unki requirement — grouping logic likhni padegi
```
API se flat list aayi:
  aud_101  Higher Education Seekers      score 0.94  reach   450,000
  aud_102  E-Learning & Tech Enthusiasts score 0.91  reach 1,200,000
  aud_103  General Career Advancement    score 0.78  reach 3,500,000
  … 10 more …

🔴 TEEN DESIGN SAWAAL jinka jawab document me NAHI hai:

1️⃣ Grouping ka BASIS kya hai?
   💡 Suggestion: CUMULATIVE REACH — kyunki #2 ne cost ka farak khatam
      kar diya, to reach hi asli differentiator hai

2️⃣ NESTED hain ya INDEPENDENT?
   💡 Suggestion: NESTED (document ke example jaisa) —
      "Balanced me Narrow bhi shamil hai" samajhna aasan

3️⃣ Har profile me KITNE segments?
   💡 Suggestion: REACH TARGET tak — fixed count se inconsistent results
```

## ❓ Unka purpose
```
1. Ek galat assumption pakadna — code likhne se pehle

2. Aur ye ek BADI baat batata hai:
   §4.2 ke API examples ASSUMPTIONS the, VERIFIED CONTRACTS nahi.
   → Aur wo v1.1.0 se v2.0 me chale aaye
   → Ek "contract document" ke liye ye serious hai
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"To grouping kaun karega?"* | **Agent.** Aur grouping logic humein define karni padegi — document me nahi hai, kyunki maana gaya tha ki API karega. Mera suggestion: cumulative reach par group karo, nested rakho, reach target tak segments jodo. |
| 🔴 *"To API asal me kya deta hai?"* | ⚠ **Pata nahi!** David ne bataya ki `bundles` **nahi** hai — par sahi shape nahi bataya. **Ye ab sabse blocking sawaal hai.** |
| *"`bundles.broad` vs `WIDE` ka mismatch?"* | ✅ **Khatam ho gaya** — koi `bundles` object hi nahi hai, to mismatch bhi nahi. `WIDE` enum me stand karta hai. |
| *"Baad me support aayega?"* | David ne *"not **currently** supported"* kaha — "currently" se lagta hai baad me aa sakta hai. Isliye grouping logic **swap-able** likhni chahiye. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | 🔴🔴 **`POST /api/audience-sets/suggest/` ka EK REAL RESPONSE SAMPLE** | **SABSE BLOCKING** — grouping logic + effective CPM (#2) + audience schema — **teeno** unblock ho jaayenge |
| 2 | Grouping basis kya ho — relevance score, cumulative reach, ya data source? | Design decision |
| 3 | `bundles` support **kab** aayega? | Workaround kitna permanent hai |

## 🏷️ Ek line me
> *"Jo `bundles.narrow/balanced/broad` structure tumne maana tha — wo API me nahi hai."*

**Severity:** 🔴 HIGH — API assumption galat, aur 3 profiles ek naya agent-side feature ban gaye

---
---

# COMMENT #21 — Location market ke country par DEFAULT hoti hai

**📍 Kahan:** Step 5 Targeting → **Location** → **"Optional"**

## 📄 Document me pehle kya tha
```
Location | Multi-select | OPTIONAL |
           ↑
    "khaali rahegi jab tak trader na bhare"
```

## 💬 David ne kya likha
> *"defaults to market country"*

## 🔍 Comment ka matlab
```
Location khaali NAHI rehti — market ke country par DEFAULT ho jaati hai.

  markets = ["GB"]  →  location default = ["GB"]
  Trader chahe to NARROW kare (London, ya postcodes)

🔴 Ye #5 ke default-then-refine model ka FIELD-LEVEL confirmation hai.
   #5 me David ne kaha tha: "default targeting like COUNTRY TARGETING
   and Connected TV device only"
   #21 wahi baat, us khaas field par.

✅ Aur ye SOURCE column ki zaroorat ko 5vi baar confirm karta hai
   (#7, #9, #11, #13, ab #21)
```

## 🔴 Ek confusion clear karni zaroori hai — `markets` vs `location`
```
Dono me "GB" hota hai — par DO ALAG kaam karte hain:

╔══════════════════════════════════════════════════════════════════════════╗
║  markets = ["GB"]           (Step 1)                                     ║
║    → BUYING SCOPE: "kaunse market ka inventory kharidna hai?"             ║
║    → Isse tay: kaunse deals, kaunsa rate card, kaunsi audiences, currency ║
║                                                                          ║
║  location = ["GB"]          (Targeting — DEFAULT)                        ║
║    → DELIVERY FILTER: "ad kahan dikhna chahiye?"                         ║
║    → Isse tay: geo targeting                                             ║
║                                                                          ║
║  → Default me dono same · PAR diverge ho sakte hain!                      ║
╚══════════════════════════════════════════════════════════════════════════╝

Real example jahan alag hote hain:
  markets  = ["GB"]                      ← GB ka inventory kharido
  location = ["London", "Manchester"]    ← par sirf in do cities me dikhao
```

## 🔍 Location ek HIERARCHY hai — default sabse upar
```
Country      GB                        ← 🟢 DEFAULT (markets se)
   ↓ narrow karo
Region       England, Scotland
   ↓ narrow karo
City         London, Manchester
   ↓ narrow karo
Postcode     SW1, SW3, W1, W8          ← David ka example (#5 se)

→ Neeche jaane se reach KAM hoti hai (agent ko batana chahiye)
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Requirement: **Optional** ✅ · Source: **⚙️ DERIVED — market country** |
| 2 | ➕ Naya note: `markets` vs `location` ka farak |
| 3 | ➕ Location hierarchy document karo |
| 4 | 🔴 Targeting step ka **poora default table** daalo |
| 5 | Agent behaviour: narrow karne par reach kam hoti hai — batao |

## ✅ Targeting step ka poora default set (#4, #5, #19, #20, #21, #22 se)
| Targeting type | Default | Requirement | Source |
|---|---|---|---|
| **Location** | ✅ Market country (GB) | Optional | ⚙️ DERIVED — #21 |
| **Device type** | ✅ Advertiser ka setting | Optional | 🏢 ADVERTISER — #22 · ⚠ lock ho sakta |
| **Audience segments** | ✅ None | Optional | 🤖 Agent 3 options suggest kare — #4, #20 · 3P par bhi — #19 |
| **Content exclusions** | 🟡 Advertiser brand-safety? | Optional | 🏢 ADVERTISER? — ⚠ confirm |
| **Instream position** | ❌ None | Optional | 💬 ASKED |
| **Mobile environment** | ❌ None | **Conditional** — sirf jab Mobile ∈ device_types | 💬 ASKED — #22 |
| ➕ **Targeting source** (3P) | 🟡 Amazon? | Optional | 💬 ASKED — #1, #19 |

**Do defaults pehle se lagte hain. Ek bhi field asked-and-required nahi.**

## ❓ Unka purpose
```
1. Default-then-refine model ko concrete banana

2. Ek bekaar khaali field hatana

3. Aur `markets` vs `location` ka farak — jo document ne kabhi likha hi nahi
   → Bina explain kiye ye duplication lagta hai
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"`markets` aur `location` duplication nahi hai?"* | Nahi — `markets` **buying scope** hai (kaunsa inventory kharido), `location` **delivery filter** hai (ad kahan dikhe). Default me same hote hain par diverge ho sakte hain: GB ka inventory kharido, sirf London me deliver karo. |
| *"Postcode targeting support hai?"* | ⚠ **Pata nahi** — `GET /api/strategies/locations/{market}/` postcodes deta hai ya sirf cities/regions? **David ka apna example postcode ka hai**, to ye confirm karna zaroori hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | `GET /api/strategies/locations/{market}/` **postcodes** support karta hai? *(#5 se khula hai)* |
| 2 | **Content exclusions** advertiser ke brand-safety rules se default hone chahiye? |

## 🏷️ Ek line me
> *"Location khaali nahi rehti — wo market ke country par default ho jaati hai."*

**Severity:** 🟡 MEDIUM — chhota fix, par default-then-refine ka concrete confirmation

---
---

# COMMENT #22 — Device type ADVERTISER level par set hota hai

**📍 Kahan:** Step 5 Targeting → **Device type** → **"Optional"**

## 📄 Document me pehle kya tha
```
Device type | Multi-select | OPTIONAL |
```

## 💬 David ne kya likha
> *"Some advertisers only want CTV only - set at advertiser level"*

## 🔍 Comment ka matlab — teen baatein
```
1️⃣ "SOME advertisers"
   → Baaki advertisers ko aur devices bhi chahiye. Sabke liye same nahi.

2️⃣ "only want CTV only"
   → Sirf Connected TV par ad chahiye — mobile/tablet par nahi

3️⃣ "set at ADVERTISER LEVEL"
   → 🏢 Advertiser ke record me set hota hai, campaign me nahi
   → Ye ADVERTISER DEFAULTS ka TEESRA confirmation hai
```

## ⚠ Aur ye mere Note 21 ko theek karta hai
```
Note 21 ke default table me maine likha tha:
  Device type | Connected TV only | Optional | 🔒 FIXED — CTV module
                                                ↑
                  Socha ki ye CONSTANT hai (CTV module hai to Connected TV)

✅ Reality: 🏢 ADVERTISER — advertiser ke hisaab se BADALTA hai

Kyun farak matter karta hai:
  🔒 FIXED             = badal hi nahi sakte
  🏢 ADVERTISER default = pehle se bhara hua, PAR override ho sakta hai
```

## 🔴🔴 SABSE BADA — "CTV" ke DO matlab hain, aur document ne mila diye
```
╔══════════════════════════════════════════════════════════════════════════╗
║  FORMAT ke roop me:  streaming_tv                                        ║
║    → CONTENT ka kism (Prime Video, Netflix ka content)                    ║
║    → Step 1 me tay · #14 ke hisaab se HAMESHA streaming_tv                ║
║                                                                          ║
║  DEVICE ke roop me:  Connected TV                                        ║
║    → SCREEN jispar ad dikhta hai                                         ║
║    → Targeting me tay · advertiser ke hisaab se badalta hai               ║
║                                                                          ║
║  🔴 YE DO ALAG CHEEZEIN HAIN!                                            ║
╚══════════════════════════════════════════════════════════════════════════╝

Kyun? Streaming content MOBILE par bhi chalta hai:
  📺 Connected TV     Smart TV · Fire Stick · Roku    ← "CTV" asli maane me
  📱 Mobile phone     Prime Video app phone par        ← BHI streaming_tv!
  📱 Tablet           iPad par Prime Video
  💻 Desktop          Browser me Netflix

→ formats = ["streaming_tv"] ka matlab NAHI ki device = Connected TV
```

## 🔴 PROOF document ke ANDAR hi hai!
```
Step 5 me ek field hai:
  Mobile environment | Select | Optional
       ↑  Values: "in-app" ya "mobile web"

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 AGAR "CTV" KA MATLAB HOTA "SIRF CONNECTED TV DEVICE" —                ║
║     TO "MOBILE ENVIRONMENT" FIELD KA MATLAB HI KYA HOTA?!                 ║
║                                                                          ║
║  Us field ka EXIST karna hi saabit karta hai ki MOBILE DELIVERY           ║
║  POSSIBLE HAI.                                                           ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Ye ek BAHUT STRONG internal proof hai — reply me zaroor likhna
```

## 🔴 Teen consequences
```
1️⃣ REACH par bada asar
   Prime Video ka bahut viewing MOBILE par hota hai
   → CTV-only se available inventory KAAFI kam (shayad 50-60%)
   → Reach forecast KAM aayega

2️⃣ CPM par asar
   Connected TV inventory mobile se MEHNGI hoti hai (premium screen)
   → CTV-only = zyada CPM = kam impressions

3️⃣ 🔴 REPAIR LOOP ka PRIMARY lever LOCK ho sakta hai
   Note 12 ka lever #1: "doosri targeting relax karo — DEVICE, location,
   content exclusions" ← PRIMARY lever

   🔴 PAR agar device advertiser POLICY hai, agent use relax kar hi
      nahi sakta!

   Naya worst case:
     • Koi audience nahi (#4)          → lever 2, 3 gaye
     • Preferred fixed-CPM deal (#12)  → bid lever gaya
     • Advertiser: CTV device only     → 🔴 PRIMARY lever LOCK
```

## 🔴🔴 NAYA CONCEPT — "Default" vs "Constraint"
```
David ne kaha "SOME advertisers ONLY WANT CTV only"
Sawaal: kya ye ek DEFAULT hai ya ek POLICY hai?

╔══════════════════════════════════════════════════════════════════════════╗
║  🏢 ADVERTISER DEFAULT          vs    🔒 ADVERTISER CONSTRAINT            ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Pehle se bhara hua                   Pehle se bhara hua                 ║
║  Trader OVERRIDE kar sakta hai        Trader override NAHI kar sakta      ║
║  Repair loop RELAX kar sakta hai      Repair loop CHHOO NAHI SAKTA        ║
║                                                                          ║
║  Example: frequency cap (#13)          Example: device policy (#22)?      ║
╚══════════════════════════════════════════════════════════════════════════╝

Schema me express karna padega:

class AdvertiserSetting(BaseModel):
    value: Any
    is_locked: bool = False    # brand policy? override nahi
    reason: Optional[str]      # "brand policy: CTV only"
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Device type Source: **🏢 ADVERTISER** (fallback: Connected TV only) |
| 2 | ⚠ Note 21 ka table theek karo — FIXED → ADVERTISER |
| 3 | 🔴🔴 ➕ Naya note: **"CTV as a format vs CTV as a device"** |
| 4 | 🔴🔴 ➕ **`AdvertiserSetting` wrapper** (`value` + `is_locked` + `reason`) |
| 5 | 🔴 Repair loop lever list me naya column: **"lock ho sakta hai?"** |
| 6 | `Mobile environment`: Optional → **Conditional** (sirf jab Mobile ∈ device_types) |

## ❓ Unka purpose
```
1. Ek bekaar sawaal hatana (advertiser se aa jaata hai)

2. 🔴 Aur ek CONCEPTUAL galti theek karna — format vs device

3. 🔴 Aur repair loop ko honest banana
   Agent ko pata hona chahiye ki kaunsi cheez wo CHHOO SAKTA HAI
   aur kaunsi NAHI — aur trader ko batana chahiye jab wo na chhoo sake
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"CTV module me device Connected TV nahi hoga to kya hoga?"* | **Format aur device do alag cheezein hain.** `streaming_tv` content ka kism hai; Connected TV screen hai. Prime Video app phone par bhi chalta hai. **Aur document khud ye saabit karta hai** — Step 5 me `Mobile environment` field hai, jo bemaani hoti agar delivery sirf TV par hoti. |
| *"To CTV-only karne se kya nuksaan hai?"* | Reach kam (Prime ka bahut viewing mobile par hai) aur CPM zyada (CTV inventory premium hai). **Trader ne ye choose nahi kiya** — advertiser policy hai. To agent ko dono asar **batane** chahiye. |
| 🔴 *"Repair loop device relax kar sakta hai?"* | ⚠ **Ye depend karta hai ki wo DEFAULT hai ya CONSTRAINT.** Agar brand policy hai — nahi. Isliye `is_locked` flag chahiye, aur agent ko batana chahiye ki wo kaunsa lever use **nahi** kar saka. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | 🔴 Device setting **default** (overridable) hai ya **constraint** (locked)? | Repair loop ise chhoo sakta hai ya nahi |
| 2 | Aur kaunse advertiser settings **locked** ho sakte hain? | `is_locked` kis-kis par lagega |
| 3 | Agar advertiser ka koi device setting nahi — fallback kya? | Default behaviour |
| 4 | Content exclusions bhi advertiser se? (brand safety) | Ab zyada likely lagta hai |

## 🏷️ Ek line me
> *"Device type khaali nahi rehti — wo advertiser ke account me set hoti hai. Aur kuch advertisers sirf Connected TV chahte hain."*

**Severity:** 🔴 HIGH — advertiser defaults ka teesra confirmation + format/device conceptual fix + repair loop lever lock

---
---

# COMMENT #23 — Manager approval khatam · sirf ek STATUS

**📍 Kahan:** Step 7: **Plan Approval** (poora step)

## 📄 Document me pehle kya tha
```
Step 7 — Plan Approval
  "The plan is presented for approval. Manager approval gate for
   plans above a threshold."

Aur state machine me:
  present_plan → AWAIT_APPROVAL → create_strategy
                        ↑
              Ek BLOCKING GATE — jab tak manager approve na kare, aage nahi
```

## 💬 David ne kya likha
> *"we simplified this so it's just a status changed to finalise the plan - no manager approval required for now"*

## 🔍 Comment ka matlab
```
❌ Pehle:
   Plan bana → MANAGER ka wait → manager approve kare → tab strategy bane
                     ↑
        Ek DOOSRA INSAAN chahiye. Ho sakta hai wo kal aaye.

✅ Ab:
   Plan bana → status DRAFT se FINALISED → strategy bane
                     ↑
        Wahi trader kar sakta hai. Koi wait nahi.

🔴 Teen shabd important hain:
   "we SIMPLIFIED"      → jaan-boojh kar design decision, galti nahi
   "just a STATUS"      → ek field, ek approval workflow nahi
   "for NOW"            → 🔴 baad me wapas aa sakta hai
```

## 🔍 "Approval gate" vs "status change" — technically kya farak?
```
╔══════════════════════════════════════════════════════════════════════════╗
║  ❌ APPROVAL GATE (blocking)                                             ║
║    • Ek DOOSRA insaan chahiye                                            ║
║    • Notification bhejni padegi                                          ║
║    • Agent RUK jaata hai — session shayad ghanton/dinon tak khula        ║
║    • Reject hone par kya? Wapas kaunse step par?                         ║
║    • Threshold logic chahiye (kitne budget se upar?)                      ║
║    • Kaun approve kar sakta hai? Roles chahiye                            ║
║    • Audit trail chahiye                                                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ✅ STATUS CHANGE (non-blocking)                                         ║
║    • Wahi trader kar sakta hai                                           ║
║    • Ek field: DRAFT → FINALISED                                         ║
║    • Agent turant aage badh jaata hai                                    ║
║    • Ek enum, bas                                                        ║
╚══════════════════════════════════════════════════════════════════════════╝

🔴 Notice: bayen taraf ka POORA COLUMN M1 se GAYAB ho gaya.
   Ye bahut kaam bacha — notifications, roles, audit, reject-recovery.
```

## 🔴 State machine par asar — DOOSRA `interrupt()` khatam
```
❌ PEHLE (do interrupts):
   ... → present_plan → 🛑 AWAIT_APPROVAL → create_strategy → ...
                              ↑
                    Ye ek interrupt() tha jahan agent
                    KISI DOOSRE ka wait karta

✅ AB (ek interrupt):
   ... → present_plan → set_status(FINALISED) → create_strategy → ...
                              ↑
                    Koi interrupt nahi — bas ek field update

🔴 Ab poore flow me SIRF EK asli interrupt bacha:
   AWAIT_INPUT — jab agent trader se kuch poochhta hai
```

## ⚠ PAR — Advertiser approval threshold #22 ke baad WAAPAS aa sakta hai
```
David: "no manager approval required FOR NOW"

Aur #13/#15/#22 ne advertiser defaults ka concept diya.
To ek possibility hai:

  Ek advertiser ka rule ho sakta hai:
    "£10,000 se upar ke plans par mere approval chahiye"

  → Wo MANAGER approval nahi hai (VOW ke andar)
  → Wo ADVERTISER-LEVEL policy hai

╔══════════════════════════════════════════════════════════════════════════╗
║  Isliye schema me space chhod do:                                        ║
║    AdvertiserDefaultsSchema:                                             ║
║      approval_threshold: Optional[AdvertiserSetting]  # M2               ║
║                                                                          ║
║  M1 me use NAHI karna — par field ka concept document me rakhna,          ║
║  taaki baad me add karna refactor na bane                                ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Step 7 rename: "Plan Approval" → **"Plan Finalisation"** |
| 2 | 🔴 *"Manager approval gate for plans above a threshold"* — **HATAO** |
| 3 | ➕ `PlanStatusEnum { DRAFT, FINALISED }` |
| 4 | 🔴 State machine: `AWAIT_APPROVAL` state **hatao** |
| 5 | ➕ Note: *"Approval was simplified — status only, for now"* (rationale + future) |
| 6 | ⚠ `approval_threshold` future field ka mention (M2) |

## ❓ Unka purpose
```
1. M1 SHIP karna hai
   Approval workflow me bahut kaam hai — notifications, roles, audit,
   reject-recovery, threshold config. Ye SAB M1 se bahar.

2. 🔴 Agent ka flow BLOCK nahi hona chahiye
   Agar agent kisi doosre insaan ka wait kare, to conversation TOOT jaati hai.
   Trader ne shuru kiya, manager kal aayega — session ka kya hoga?

3. Product ka promise
   "10 minute me plan" — agar 6 ghante manager ka wait karo, to promise toota.
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| *"To koi bhi bina check ke £50,000 ka plan launch kar dega?"* | M1 me haan — David ne ye jaan-boojh kar simplify kiya. **Par safety poori nahi gayi**: (a) FINALISED ek explicit action hai — accidental nahi; (b) plan ka poora breakdown pehle dikhta hai; (c) activation ke apne 6 prerequisites hain (#27); (d) baad me advertiser-level `approval_threshold` add ho sakta hai. |
| *"'For now' ka matlab baad me wapas aayega?"* | Haan, possibly. Isliye schema me `PlanStatusEnum` extensible rakhenge (`PENDING_APPROVAL` baad me add ho sakta hai) aur `approval_threshold` ka concept document me note kar rahe hain — taaki baad me refactor na ho. |
| *"FINALISED ke baad plan badal sakta hai?"* | ⚠ **Ye open hai.** #28 ne kaha ki strategy create ke baad fields update ho sakti hain — par kya FINALISED ke baad **plan** ka budget/deal badal sakta hai? Ye poochhna hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Status change ka **endpoint** kya hai? `PATCH /api/plans/{id}/status/`? |
| 2 | `PlanStatusEnum` me sirf DRAFT/FINALISED, ya aur values? |
| 3 | FINALISED ke baad plan **DRAFT** me wapas ja sakta hai? |
| 4 | Advertiser-level `approval_threshold` M2 me plan me hai? |

## 🏷️ Ek line me
> *"Manager approval hata diya — bas ek status DRAFT se FINALISED. Filhaal ke liye."*

**Severity:** 🟢 LOW-MEDIUM — kaam kam hota hai, par state machine se ek interrupt nikalta hai

---
---

# COMMENT #24 — `simple-strategies` endpoint, `strategies` nahi

**📍 Kahan:** Step 8: Strategy Creation → **`POST /api/strategies/`**

## 📄 Document me pehle kya tha
```
Step 8 — Strategy Creation
  "POST /api/strategies/ creates the strategy"

Aur §4.2 me poora payload example:
  POST /api/strategies/
  { "name": "...", "budget": "...", "product_asins": [], ... }
```

## 💬 David ne kya likha
> *"probably more likely simple-strategies endpoint"*

## 🔍 Comment ka matlab
```
Strategy banane ka endpoint galat likha hai.
Sahi shayad:  POST /api/simple-strategies/

🔴 "PROBABLY MORE LIKELY" — David bhi 100% sure nahi hai!
   Do matlab:
   1. Actual endpoint verify karna padega (koi bhi 100% nahi jaanta)
   2. Aur "simple" ka matlab hai ki DO endpoint families hain
```

## 🔍 "simple-strategies" kya hoga?
```
Naam se lagta hai:

  /api/strategies/          → FULL strategy — sab formats, sab options
                               (display + video + streaming + audio)
                               Bahut fields, bahut complexity

  /api/simple-strategies/   → SIMPLIFIED — kam fields, kam options
                               Shayad CTV/streaming-focused
                               Bahut kuch pre-set ya derive ho jaata hai

Aur ye #14 se PERFECTLY match karta hai:
  #14: "format hamesha streaming_tv hai"
  → To jab format constant hai, ek SIMPLER endpoint samajh me aata hai
```

## 🔴🔴 SABSE BADA CONSEQUENCE — §4 KA POORA CATALOGUE SHAK ME AA GAYA
```
Ab tak §4 ke baare me 3 comments aaye:

  #20  → response SHAPE galat (bundles nahi hai)
  #24  → ENDPOINT NAME shayad galat (strategies vs simple-strategies)
  #28  → ek endpoint MISSING hai (update endpoint ka naam nahi)

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 Ek DEEPER sawaal khulta hai:                                         ║
║                                                                          ║
║  Agar strategy creation ka apna CTV variant hai,                          ║
║  to KYA BAAKI ENDPOINTS KA BHI HAI?                                      ║
║                                                                          ║
║    /api/strategies/audience-sets/suggest/  → CTV variant?                 ║
║    /api/deals/                             → CTV variant?                 ║
║    /api/strategies/locations/{market}/     → CTV variant?                 ║
║    /api/contextual-targeting/...           → CTV variant?                 ║
║    PATCH endpoint (#28)                    → naam kya?                    ║
║                                                                          ║
║  → Ye pata NAHI. Aur ye ek "contract document" ke liye serious hai.      ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## ⚠ Aur ye mere ek SABOOT ko todta hai
```
#17 (ASIN timing) me maine likha tha:
  "§4.2 ka create payload example `product_asins: []` bhejta hai —
   yaani khaali ASIN accept hota hai. Isliye Option A safe hai."

🔴 PAR agar wo example GALAT ENDPOINT ka hai, to mera saboot bekaar hai.
   simple-strategies ka payload BILKUL ALAG ho sakta hai.

✅ Conclusion sahi tha (#28 ne seedha confirm kiya)
❌ Justification galat endpoint par based tha

💡 Reply me ye distinction saaf karni chahiye — imaandari se
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Endpoint: `POST /api/strategies/` → `POST /api/simple-strategies/` **(⚠ pending verification)** |
| 2 | §4.1 catalogue table me update karo |
| 3 | §4.2 payload example ⚠ mark karo — *"endpoint under verification"* |
| 4 | 🔴 ➕ Naya note: **"Endpoint verification required"** — sab endpoints ki list, kaunsa CTV variant ho sakta hai |
| 5 | ⚠ Note 17 ka evidence paragraph theek karo |

## ❓ Unka purpose
```
1. Galat endpoint = code kaam hi nahi karega
   Wajahat `/api/strategies/` par POST karega → 404 ya galat behaviour

2. 🔴 Aur ek AADAT ka issue pakadna
   §4 ke examples v1.1.0 se AS-IS chale aaye — kabhi verify nahi hue.
   "Contract document" me unverified assumptions khatarnaak hain.

3. Aur ye ek DESIGN clue bhi deta hai
   Agar simple-strategies exist karta hai, to backend ne already
   CTV ko simplify kar rakha hai — humein us shape ke saath align hona chahiye
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"To payload shape kya hai?"* | ⚠ **Pata nahi.** Isliye humein `simple-strategies` ka **actual OpenAPI spec / sample request** chahiye. Ye ab ek blocking item hai. |
| 🔴 *"Aur baaki endpoints?"* | **Yahi mera sawaal hai.** Agar strategy creation ka CTV variant hai, to deals, audience-sets, locations, contextual-targeting ka bhi ho sakta hai. **Poori CTV endpoint family ki list chahiye.** |
| *"Document me galat endpoint kaise aa gaya?"* | v1.1.0 se as-is chala aaya, aur v2.0 me maine flow change kiya par API catalogue re-verify nahi kiya. **Ye meri galti hai** — aur isliye ab main poori list verify karwa raha hoon. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | 🔴🔴 **CTV/streaming ke liye poori endpoint family kya hai?** | **BLOCKING** — §4 ka poora catalogue is par depend karta hai |
| 2 | `simple-strategies` ka OpenAPI spec / sample payload? | Schema exact banane ke liye |
| 3 | `simple-strategies` vs `strategies` — farak kya hai? | Kaunsa kab use karein |
| 4 | Update/patch endpoint ka naam? (#28 se) | Post-creation updates |

## 🏷️ Ek line me
> *"Strategy banane ka endpoint shayad `simple-strategies` hai, `strategies` nahi."*

**Severity:** 🔴 HIGH — §4 ka poora API catalogue verification maangta hai

---
---

# COMMENT #25 — Click-through URL streaming TV ke liye OPTIONAL

**📍 Kahan:** Step 10: Creative Upload → **Click-through URL** → **"Required"**

## 📄 Document me pehle kya tha
```
Click-through URL | HttpUrl | REQUIRED |
```

## 💬 David ne kya likha
> *"optional for streaming tv"*

## 🔍 Comment ka matlab — ye TECHNICAL REALITY hai
```
Streaming TV par click-through URL ka koi matlab NAHI hai.

Kyun? Sochо:

  📱 Mobile / 💻 Desktop par ad:
     User ad par TAP/CLICK karta hai → browser khulta hai → website
     ✅ Click-through URL ka matlab hai

  📺 TV par ad (Smart TV / Fire Stick):
     User ke haath me REMOTE hai — mouse nahi, touch nahi
     Kya wo TV par "click" karega? 🔴 NAHI KAR SAKTA!
     ❌ Click-through URL BEKAAR hai

╔══════════════════════════════════════════════════════════════════════════╗
║  Isliye CTV ads me "call to action" DIFFERENT hoti hai:                   ║
║    • QR code screen par (phone se scan karo)                              ║
║    • "Search for BrightPath" (voice/search prompt)                        ║
║    • Brand recall — bas naam yaad rahe                                    ║
║    • Amazon par: "Add to cart" via Fire TV remote (kuch formats me)        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## ⚠ PAR ek nuance — #22 ke baad
```
#22 ne bataya ki streaming_tv MOBILE par bhi deliver ho sakta hai!

  Agar device_types me Mobile hai:
    → User phone par Prime Video dekh raha hai
    → Wo ad par TAP KAR SAKTA HAI
    → 🔴 To click-through URL ka MATLAB hai!

╔══════════════════════════════════════════════════════════════════════════╗
║  To sahi rule "optional for streaming tv" se ZYADA NUANCED hai:           ║
║                                                                          ║
║    device_types = [CONNECTED_TV]  only    → Optional (bekaar)             ║
║    device_types me Mobile/Tablet/Desktop  → Recommended (kaam karega)      ║
║                                                                          ║
║  💡 Ye ek acchi baat hai David se poochhne ke liye — dikhata hai          ║
║     ki humne #22 aur #25 ko JOD kar socha                                ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | Click-through URL: **Required → Optional** |
| 2 | Schema: `click_through_url: Optional[HttpUrl] = None` |
| 3 | ➕ Note: **kyun** optional hai (remote se click nahi hota) |
| 4 | ⚠ ➕ Nuance: device_types me mobile ho to recommended |
| 5 | Validation: agar diya hai to valid URL hona chahiye (`HttpUrl` ye kar deta hai) |

## ❓ Unka purpose
```
1. Ek IMPOSSIBLE requirement hatana
   Agar required rakha, aur trader ke paas landing page nahi —
   to wo BLOCK ho jaayega ek field par jiska CTV me matlab hi nahi

2. Ye #14 (format = streaming_tv) ka natural nateeja hai
   Jab format constant hai, to us format ki ADAT ke hisaab se
   fields adjust honi chahiye — jo v1.1.0 me display ke liye required thi
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| *"To CTV me call-to-action kaise hoga?"* | QR code creative me, ya "search for X" prompt, ya bas brand recall. Aur measurement ad tag / ASIN conversions se hota hai (Step 11) — click se nahi. |
| 🔴 *"Agar campaign mobile par bhi chal raha ho?"* | **Bahut acha point** — aur #22 ke baad ye real hai. Mera suggestion: agar `device_types` me Mobile/Tablet/Desktop hai to URL **recommend** karo (block mat karo). Sirf CONNECTED_TV-only me poori tarah optional. **Ye confirm karna chahenge.** |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Agar `device_types` me Mobile hai — click-through URL **recommended** karna chahiye? |
| 2 | CTV creatives me QR code allowed hai? Koi spec? |
| 3 | Aur koi field jo streaming TV ke liye required se optional hona chahiye? |

## 🏷️ Ek line me
> *"Click-through URL streaming TV ke liye optional hai — TV remote se koi click nahi karta."*

**Severity:** 🟢 LOW — chhota fix, par technical reality ka acha example

---
---

# COMMENT #26 — Approval status per CHANNEL — Netflix/Disney hard-code mat karo

**📍 Kahan:** Step 10: Creative Upload → **Approval status fields**

## 📄 Document me pehle kya tha
```
Amazon approval status    | enum | Read-only |
Netflix approval status   | enum | Read-only |
Disney approval status    | enum | Read-only |
     ↑
🔴 TEEN ALAG FIELDS, provider ke NAAM HARD-CODED
```

## 💬 David ne kya likha
> *"It's just a single status for each channel not necessary netflix or disney - could be paramount or channel 4"*

## 🔍 Comment ka matlab
```
❌ GALAT (hard-coded):
   class CreativeSchema:
       amazon_approval_status:  ApprovalStatusEnum
       netflix_approval_status: ApprovalStatusEnum
       disney_approval_status:  ApprovalStatusEnum

   🔴 Problem: Paramount+ add karna hai?
      → SCHEMA badalni padegi
      → Migration
      → Wajahat ka code badlega
      → Vishal ka UI badlega
      → Basil ke tests badlenge
      → RELEASE chahiye ek naya publisher add karne ke liye!

✅ SAHI (config-driven):
   class CreativeSchema:
       approval_statuses: dict[str, ApprovalStatusEnum]
       # {"amazon": "APPROVED", "netflix": "PENDING", "paramount": "PENDING"}

   ✅ Paramount+ add karna hai? → Bas DATA me ek channel jud gaya
      Koi code change nahi. Koi migration nahi. Koi release nahi.
```

## 🔍 "Channel 4" ka example bahut jaan-boojh kar diya gaya
```
David ne SPECIFICALLY "channel 4" kaha — ye ek UK broadcaster hai.

Kya batata hai:
  1. Ye ek PLAN hai, guess nahi — UK me Channel 4 ka streaming (All 4)
     ek real CTV inventory source hai
  2. Publisher list MARKET ke hisaab se badlegi:
       UK  → Prime Video, Netflix, Disney+, Channel 4, ITVX
       US  → Prime Video, Netflix, Hulu, Paramount+, Peacock
       DE  → Prime Video, Netflix, Joyn, RTL+
  3. To hard-coding SIRF galat design nahi — wo SCALE HI NAHI karegi
```

## 🔴🔴 AUR YE EK GENERAL PRINCIPLE hai — sirf ye field nahi
```
David ka comment ek field par hai, par PRINCIPLE poore document par lagta hai.

Document me kahan-kahan lists HARD-CODE hui hain:

  1. Approval status fields              ← David ne pakda (#26)
  2. §2.3 tier table: "Prime Video, Netflix/Disney"  ← same problem
  3. Step 2 deal table: "Prime Video Deals"          ← same problem
  4. FormatEnum me PRIME_VIDEO                       ← #14 ne pakda
  5. Genre lists                                     ← API se aani chahiye
  6. Market lists                                    ← API se aani chahiye

╔══════════════════════════════════════════════════════════════════════════╗
║  🔴 RULE:                                                                ║
║  Jo cheez BADAL sakti hai wo CONFIG/API se aani chahiye — CODE me nahi.   ║
║                                                                          ║
║  CODE me hona chahiye:    CONFIG/API se aana chahiye:                    ║
║    • Approval STATES        • Publisher/channel LIST                     ║
║      (PENDING/APPROVED/     • Market LIST                                ║
║       REJECTED)             • Genre LIST                                 ║
║    • Deal TYPES             • Audience segment LIST                      ║
║    • Source TYPES           • Product category LIST                      ║
╚══════════════════════════════════════════════════════════════════════════╝

💡 Aur ye ek gap band karta hai jo maine v2.0 me FLAG kiya tha
   (Gap: "config-driven vs hard-coded ka koi rule nahi hai")
```

## 🔍 Naming bhi resolve hui — "channel"
```
David ka shabd: "for each CHANNEL"

Document me is cheez ke 3 naam the:
  provider    (SelectedDealSchema.provider)
  channel     (David ka shabd)
  channels    (Step 2 me kahin)

✅ David ne "channel" use kiya → to STANDARD "channel" hona chahiye
   → SelectedDealSchema.provider → SelectedDealSchema.channel
   → Aur #18 ka naya field bhi `channel`
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | 🔴 Teen hard-coded fields → **`approval_statuses: dict[str, ApprovalStatusEnum]`** |
| 2 | ➕ Naya note: **"Channels are config-driven"** — kyun aur kaise |
| 3 | 🔴 ➕ Naya note: **"Config-driven vs hard-coded"** — general rule, poori list |
| 4 | §2.3 tier table: publisher naam **examples** ki tarah likho, exhaustive nahi |
| 5 | Naming: `provider` → **`channel`** (sab jagah) |
| 6 | Step 2 heading: *"Prime Video Deals"* → *"CTV Deals"* |

## ❓ Unka purpose
```
1. Naye publisher add karna ek DATA change ho, CODE change nahi

2. Market expansion ke liye ye ZAROORI hai
   Har market ki publisher list alag hai — hard-code karo to
   har naye market par schema change

3. Aur ek DESIGN DISCIPLINE sikha rahe hain
   "Jo cheez badal sakti hai wo config se aaye" — ye poore
   document par lagta hai, sirf is field par nahi
```

## 🙋 Wo humse ye pooch sakte hain
| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"Channel list kahan se aayegi?"* | Ideally ek API se — `GET /api/channels/?market=GB`. Agar wo endpoint nahi hai, to matched deals se derive kar sakte hain (`SelectedDealSchema.channel` se unique list). **Poochhna hai ki channel list ka apna endpoint hai ya nahi.** |
| *"Approval STATES bhi config-driven hone chahiye?"* | **Nahi** — states (PENDING/APPROVED/REJECTED) FINITE aur stable hain, aur agent ka logic un par depend karta hai. **Un par enum sahi hai.** Sirf **LIST** (kaunse channels) config-driven honi chahiye. Ye distinction important hai. |
| *"UI kaise render hoga jab list dynamic hai?"* | UI ko `approval_statuses` dict par loop karna hoga — jo channels present hain unke rows dikhaye. Ye Vishal ke liye ek note hai. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Channel list ka koi **API endpoint** hai? (`GET /api/channels/`) |
| 2 | Approval status per channel milta hai ya per **creative-channel pair**? |
| 3 | Aur kaunsi lists config se aani chahiye — genres, markets, categories? |
| 4 | Naming confirm: **"channel"** hi standard hai? |

## 🏷️ Ek line me
> *"Netflix aur Disney ke naam schema me mat likho — har channel ke liye ek status rakho. Kal Paramount ya Channel 4 bhi aa sakta hai."*

**Severity:** 🔴 HIGH — schema design principle, sirf ek field ka fix nahi

---
---

# COMMENT #27 — Tracking creatives se PEHLE bhi ho sakta hai · KOI ORDER NAHI

**📍 Kahan:** Step 11: **Tracking Setup** (poora step)

## 📄 Document me pehle kya tha
```
13 STEPS — EK FIXED CHAIN:
  Step 9  → Credit Check
  Step 10 → Creative Upload      ← PEHLE creatives
  Step 11 → Tracking Setup       ← PHIR tracking
  Step 12 → Activate
     ↑
 Numbers ne ORDER imply kiya
```

## 💬 David ne kya likha
> *"could be done before creatives if they are no available yet - no order necessary"*

## 🔍 Comment ka matlab
```
Tracking setup creatives se PEHLE bhi ho sakta hai.
Koi fixed order nahi hai.

Real duniya ka scenario:
  Monday:  Trader plan banata hai. Creatives? Agency bana rahi hai —
           Wednesday tak aayenge.
           🔴 Purane model me: trader RUK jaata hai
           ✅ Naye model me:   tracking setup kar lo (ASIN, ad tag,
                               conversions) — creatives baad me

  Wednesday: Creatives aaye → upload karo → Activate
```

## 🔴🔴 SABSE BADA — "13 STEPS" ka POORA MODEL TOOT GAYA
```
╔══════════════════════════════════════════════════════════════════════════╗
║  ❌ PURANA MODEL — EK SEEDHI LINE                                        ║
║                                                                          ║
║   1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13                  ║
║   Har step apne se pehle wale par depend karta hai                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ✅ NAYA MODEL — SEQUENTIAL SPINE + PARALLEL TAIL                        ║
║                                                                          ║
║   Brief → Inventory → Budget → Targeting → Forecast → Plan → Create      ║
║     ↑ ye SEQUENTIAL hai (har ek pichle ka output chahta hai)              ║
║                            │                                             ║
║              ┌─────────────┼─────────────┐                              ║
║              ↓             ↓             ↓                              ║
║          CREATIVES     TRACKING      CREDIT CHECK                        ║
║          (koi bhi     (koi bhi      (koi bhi                             ║
║           kram)         kram)         kram)                              ║
║              └─────────────┼─────────────┘                              ║
║                            ↓                                             ║
║                       🚦 ACTIVATE                                        ║
║                    (sab prerequisites check)                             ║
╚══════════════════════════════════════════════════════════════════════════╝

Aur ye 4 comments ka combined nateeja hai:
  #5   → do steps MERGE hue (13 → 12)
  #23  → ek approval GATE hata (interrupt gaya)
  #27  → tail UNORDERED hua (ye)
  #28  → fields BAAD ME update ho sakti hain (mechanism)
```

## 🔴 Isliye ACTIVATION GATE chahiye — ek naya concept
```
Agar order fix nahi hai, to Activate se pehle kisi ko CHECK karna hoga
ki sab kuch ready hai.

╔══════════════════════════════════════════════════════════════════════════╗
║  ACTIVATION PREREQUISITES — 6 checks                                     ║
║                                                                          ║
║  1. ✅ Creatives uploaded — HAR duration ke liye                          ║
║       (agar 15s aur 30s dono kharide, to dono chahiye)                    ║
║  2. ✅ Creatives approved — HAR channel se (#26)                          ║
║       {"amazon": APPROVED, "netflix": APPROVED, ...}                      ║
║  3. ✅ Ad tag registered — agar advertiser Amazon par nahi bechta          ║
║  4. ✅ ASINs attached — agar Amazon par bechta hai (#16, #17)              ║
║  5. ✅ Conversions selected — YA explicitly skip kiya gaya                ║
║  6. ✅ Credit sufficient — Step 9                                        ║
╚══════════════════════════════════════════════════════════════════════════╝

Aur agent ko HAR waqt bata sakna chahiye:
  "Activate karne ke liye 2 cheezein baaki hain:
     ✅ Tracking setup — ho gaya
     ⏳ Creatives — 30s ka missing hai
     ⏳ Netflix approval — pending
   Baaki sab ready hai."
```

## 🎉 Aur ye ek GAP band karta hai jo maine FLAG kiya tha
```
v2.0 me maine likha tha:
  "Gap: There is no explicit 'what must be true before Activate' checklist."

David ke #27 ne wahi cheez CONFIRM kar di — kyunki jab order khatam ho
jaata hai, to checklist ZAROORI ho jaati hai.

→ Ye TEESRA gap hai jo David ke comments ne band kiya (#25, #26, #27)
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | 🔴 Steps 9/10/11 → **"parallel branches, no order"** |
| 2 | 🔴 ➕ Naya section: **Activation Prerequisites** (6 checks) |
| 3 | ➕ `ActivationPrerequisitesSchema` |
| 4 | 🔴 Flow diagram: 13-step chain → spine + parallel tail |
| 5 | State machine: rigid sequence → **conditional edges** (jo missing hai wo poochho) |
| 6 | ➕ Note: agent ko har waqt "kya baaki hai" batana chahiye |

## ❓ Unka purpose
```
1. ASLI DUNIYA aisi hi chalti hai
   Creatives agency banati hai — wo late aati hain. Ad tag advertiser
   ke tech team se aata hai. Ye chizein APNI raftaar se aati hain.

2. 🔴 Trader ko BLOCK nahi karna
   Agar order fix ho, to ek missing cheez POORE kaam ko rok deti hai

3. Aur ye "self-filling form" ke saath consistent hai
   Ek form me tum kisi bhi field ko kisi bhi kram me bhar sakte ho.
   Submit se pehle validation hoti hai.
   → Bilkul yahi: koi bhi kram, Activate par validation
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"To agent ko kaise pata chalega kya baaki hai?"* | **Activation prerequisites checklist** se — 6 checks. Agent state me har ek ka status rakhega aur trader ko kabhi bhi bata sakta hai. Ye ek naya section hai jo main document me add kar raha hoon. |
| 🔴 *"To 13 steps ka numbering galat hai?"* | Haan — numbering ne ek chain imply ki jo asal me chain nahi hai. Naya model: **~7 sequential steps + 3 parallel branches** jo Activate par milti hain. **#5, #23, #27, #28 — chaaron isi taraf point karte hain.** |
| *"Credit check bhi order-free hai?"* | Logically haan (credit strategy ke bina bhi check ho sakta hai), par uska result **budget** par asar daal sakta hai — to ideally plan se pehle ya saath. ⚠ Ye confirm karna hai. |
| *"Kya trader bina creatives Activate kar sakta hai?"* | **Nahi** — prerequisite #1 aur #2 fail honge. Par wo **baaki sab kuch** kar sakta hai aur ruk nahi jaata. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal |
|---|---|
| 1 | Activation prerequisites ki list **complete** hai — 6 kaafi hain? |
| 2 | Credit check bhi order-free hai, ya plan se pehle hona chahiye? |
| 3 | Conversions **skip** kar sakte hain (bina select kiye activate)? |
| 4 | Kya koi endpoint hai jo activation readiness bata de? |

## 🏷️ Ek line me
> *"Tracking setup creatives se pehle bhi ho sakta hai — koi fixed order nahi. Jo pehle ready ho, wo pehle."*

**Severity:** 🔴🔴 VERY HIGH — 13-step model hi toot jaata hai + naya activation gate concept

---
---

# COMMENT #28 — Fields strategy banne ke BAAD update ho sakti hain

**📍 Kahan:** Step 11 → **"Confirm with client"** (ya similar wording)

## 📄 Document me pehle kya tha
```
Step 11 ke aas-paas:
  "Confirm with client"
     ↑
  Ye imply karta hai ki agar Step 8 me strategy ban gayi
  aur Step 11 me kuch naya pata chala, to CLIENT se confirm karo
  (yaani: badalna mushkil hai, pehle hi sab pakka kar lo)
```

## 💬 David ne kya likha
> *"no they can be updated on the strategy after creation"*

## 🔍 Comment ka matlab
```
"NO" se shuru — seedha rejection.

❌ Document ka mental model:
   Strategy ban gayi = PATTHAR PAR LIKH DI
   Badalna hai? Client se confirm karo, dobara plan karo

✅ Reality:
   Strategy MUTABLE hai — banne ke baad bhi fields update ho sakti hain

╔══════════════════════════════════════════════════════════════════════════╗
║  Yaani flow ye ho sakta hai:                                             ║
║    Step 8:  strategy banao — jo pata hai us se (ASIN khaali)              ║
║    Step 11: ASIN pata chala → strategy UPDATE karo                       ║
║    ✅ Koi client confirmation nahi. Koi re-planning nahi.                 ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🎉 YE OPEN QUESTION #1 KA FINAL, DIRECT JAWAB HAI
```
Document ka sabse dohraya gaya ⚠ (DO baar likha gaya — page 8 aur page 18):

  "product_location aur asin_numbers POST /strategies/ me chahiye (Step 8),
   par Step 11 me collect ho rahe hain — timing conflict.
   Option A: create karo, baad me patch karo
   Option B: Step 1 me ASIN maango"

  #16 → "selling location can leave out"     → Option A imply
  #17 → "ASIN comes later"                   → Option A imply
  #28 → "they can be updated after creation" → 🔴 OPTION A CONFIRMED

╔══════════════════════════════════════════════════════════════════════════╗
║  ✅ FINAL ANSWER: OPTION A                                               ║
║                                                                          ║
║  Step 8:  strategy banao — product_asins: []                             ║
║  Step 11: ASIN collect + validate → UPDATE strategy                      ║
║                                                                          ║
║  Aur David ne MECHANISM bhi bata diya: "updated on the strategy"          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 AUR YE #27 KA MECHANISM HAI
```
#27 ne kaha: "koi order zaroori nahi"
Par ek sawaal reh gaya: TECHNICALLY kaise possible hai?

  Agar strategy Step 8 me ban jaati hai aur IMMUTABLE hai,
  to Step 10/11 ka data kaise andar jaayega?

#28 ne jawab diya: STRATEGY MUTABLE HAI.

╔══════════════════════════════════════════════════════════════════════════╗
║  #27 = "order khatam ho gaya"        (WHAT)                              ║
║  #28 = "kyunki strategy update hoti hai"  (HOW)                          ║
║                                                                          ║
║  → Dono milkar poora naya flow model banate hain                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## 🔴 Ek NAYA sawaal khulta hai — KYA update ho sakta hai?
```
David ne kaha "THEY can be updated" — "they" = ASIN, product_location
(jo us context me discuss ho rahe the)

Par ye kitna DOOR tak jaata hai?

  ✅ SAFE — clearly updatable (David ne kaha):
     • product_asins
     • product_location
     • ad tag / conversions
     • creatives

  🟡 SHAYAD — poochhna chahiye:
     • targeting (location, device, audiences)
     • frequency cap

  🔴 SHAYAD NAHI — commercial commitment:
     • budget          (PG deal me poora budget owed! — #12)
     • flight dates    (deal booking se juda)
     • selected deals  (deal already book ho chuki)
     • market          (poori planning badal jaati hai)

💡 Ye ek BAHUT ACHA sawaal hai David se poochhne ke liye —
   dikhata hai ki hum commercial implications samajh rahe hain
```

## 🎯 Unki requirement
| # | Kya karna hai |
|---|---|
| 1 | *"Confirm with client"* wording **hatao** → *"can be updated on the strategy after creation"* |
| 2 | ✅ **Open Question #1 RESOLVED = Option A** (dono jagah mark karo) |
| 3 | 🔴 ➕ Naya note: **"Post-creation mutability"** — kya update ho sakta hai |
| 4 | 🔴 §4 me **update endpoint** add karo — ⚠ naam pata nahi (#24 ka sawaal) |
| 5 | Step 11 me explicit likho: ASIN validate hone ke baad strategy update hoti hai |
| 6 | Flow diagram: Step 8 se Step 11 tak **feedback arrow** dikhao |

## ❓ Unka purpose
```
1. Ek MISLEADING wording hatana
   "Confirm with client" se lagta hai ki badalna mushkil hai —
   jo asal me nahi hai

2. 🔴 Aur #27 ko TECHNICALLY possible banana
   Order-free flow ke liye mutability ZAROORI hai

3. Ek bekaar friction hatana
   Client ko dobara call karna = ghante/din barbaad
```

## 🙋 Wo humse ye pooch sakte hain

| Sawaal | Tayyar jawab |
|---|---|
| 🔴 *"To update ka endpoint kya hai?"* | ⚠ **Document me nahi hai** — ye ek gap hai jo main add kar raha hoon. Shayad `PATCH /api/simple-strategies/{id}/`, par #24 ke baad exact naam confirm karna hai. **Ye mera blocking sawaal hai.** |
| 🔴 *"Kya kuch bhi update ho sakta hai — budget bhi?"* | **Yahi main poochhna chahta hoon.** ASIN aur location clearly updatable hain. Par **budget aur deals commercial commitment** hain — PG deal me poora budget owed hota hai (#12). To un par restriction honi chahiye. **Guardrails chahiye.** |
| *"Activation ke BAAD bhi update ho sakta hai?"* | ⚠ Pata nahi — David ne "after creation" kaha, "after activation" nahi. Live campaign ka update ek alag baat hai. **Poochhna hai.** |
| *"To Step 8 kya bhejega?"* | Jo pata hai wo — `product_asins: []`, aur `product_location` advertiser record se ya khaali. Baaki Step 11 me patch. |

## 🙋 Hum unse ye pooch sakte hain
| # | Sawaal | Kyun |
|---|---|---|
| 1 | 🔴 Update endpoint ka **exact naam** kya hai? | §4 me add karna hai |
| 2 | 🔴 **Kaunsi fields** update ho sakti hain, kaunsi nahi? | Guardrails — budget/deals commercial hain |
| 3 | **Activation ke baad** bhi update possible hai? | Live campaign ka case |
| 4 | Update par validation/re-forecast hota hai? | Agent ko batana chahiye |

## 🏷️ Ek line me
> *"'Client se confirm karo' ki zaroorat nahi — strategy banne ke baad bhi fields update ho sakti hain."*

**Severity:** 🔴 HIGH — Open Question #1 ka final jawab + #27 ka enabling mechanism

---
---

═══════════════════════════════════════════════════════════════════════════════

# PART 4 — POORA REVIEW EK NAZAR ME

═══════════════════════════════════════════════════════════════════════════════

## 4.1 — 28 comments kahan-kahan gire?

```
Step 1 (Strategy Setup)   ████████████  12 comments   43%  ← 🔴 SABSE ZYADA
Step 4/5 (Audiences+Targ) ██████         6 comments    21%
Step 2 (Inventory)        ██             2 comments     7%
Step 10 (Creatives)       ██             2 comments     7%
§2.3 (Tier table)         ██             2 comments     7%
Step 11 (Tracking)        ██             2 comments     7%
Step 7 (Approval)         █              1 comment      4%
Step 8 (Creation)         █              1 comment      4%
```

**Sabse bada sabak:** aadhe se zyada review EK TABLE par gira — Step 1 ka field table. Wo table poori conversation ka pehla contact point hai, isliye wahan ki har galti trader ko turant chubhti hai.

## 4.2 — Comments ka KISM ke hisaab se breakdown

| Kism | Kitne | Kaunse |
|---|---|---|
| 🔴 **Design change** (model badalta hai) | 8 | #1, #2, #5, #18, #20, #22, #26, #27 |
| ✏️ **Factual correction** (galat tha) | 7 | #11, #14, #19, #21, #24, #25, #28 |
| 📉 **Requirement de-escalation** (required → optional/derived) | 9 | #3, #4, #6, #7, #8, #9, #10, #12, #15 |
| 🗑️ **Scope removal** (hatao) | 3 | #16, #17, #23 |
| ➕ **Missing concept** (nahi tha) | 1 | #13 |

## 4.3 — Step 1 ka BEFORE / AFTER — sabse dramatic transformation

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    STEP 1 — PEHLE (Document v2.0)                            ║
╠═══════════════════════════════════╤══════════════╤═══════════════════════════╣
║ Field                             │ Requirement  │ Kaun bharta hai           ║
╠═══════════════════════════════════╪══════════════╪═══════════════════════════╣
║ Strategy name                     │ Required     │ 💬 Trader                 ║
║ Advertiser                        │ Required     │ 💬 Trader                 ║
║ Brand                             │ Required     │ 💬 Trader                 ║
║ Markets                           │ Required     │ 💬 Trader                 ║
║ Budget                            │ Required     │ 💬 Trader                 ║
║ Budget split                      │ Required     │ 💬 Trader                 ║
║ Currency                          │ Required     │ 💬 Trader                 ║
║ Flight dates                      │ Required     │ 💬 Trader                 ║
║ KPI                               │ Required     │ 💬 Trader                 ║
║ Frequency cap                     │ Required     │ 💬 Trader                 ║
║ Formats                           │ Required     │ 💬 Trader                 ║
║ Product categories                │ Req for video│ 💬 Trader                 ║
║ Selling location                  │ Required     │ 💬 Trader                 ║
║ Product ASINs                     │ Conditional  │ 💬 Trader                 ║
╠═══════════════════════════════════╧══════════════╧═══════════════════════════╣
║  🔴 14 FIELDS · 13 REQUIRED · SAB TRADER SE                                  ║
║  🔴 Trader 13 sawaalon ka jawab de — TAB pehla plan dikhe                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

                                    ⬇  28 comments  ⬇

╔══════════════════════════════════════════════════════════════════════════════╗
║                    STEP 1 — AB (David ke comments ke baad)                    ║
╠═══════════════════════════════════╤══════════════╤═══════════════════════════╣
║ Field                             │ Requirement  │ Kaun bharta hai           ║
╠═══════════════════════════════════╪══════════════╪═══════════════════════════╣
║ Strategy name                     │ Optional     │ ⚙️ GENERATED (#6)         ║
║ Advertiser                        │ Required     │ 🧠 INFERRED (brief se)    ║
║ Brand                             │ Optional     │ 🧠 INFERRED / 🏢 ADVERTISER║
║ Markets                           │ Required     │ 🧠 INFERRED (#3, #8)      ║
║ Budget                            │ Required     │ 🧠 INFERRED (brief se)    ║
║ Budget split                      │ Optional     │ ⚙️ DERIVED — equal (#3)   ║
║ Currency                          │ Optional     │ ⚙️ DERIVED — market (#7)  ║
║ Flight dates                      │ Optional     │ 🧠 INFERRED (#6)          ║
║ KPI                               │ Optional     │ 🧠 INFERRED (#9)          ║
║   └─ kpi_target_value (1–5) ➕NEW │ Conditional  │ 💬 ASKED (#10)            ║
║ Frequency cap                     │ Optional     │ 🏢 ADVERTISER (#13)       ║
║ Formats                           │ —            │ 🔒 FIXED "streaming_tv"(#14)║
║ Product categories                │ Required     │ 🏢 ADVERTISER → 🧠 (#15)  ║
║ ~~Selling location~~              │ 🗑️ HATAYA    │ Step 11 (#16)             ║
║ ~~Product ASINs~~                 │ 🗑️ HATAYA    │ Step 11 (#17)             ║
╠═══════════════════════════════════╧══════════════╧═══════════════════════════╣
║  ✅ 12 FIELDS · 3 REQUIRED · ZERO ASKED-AND-REQUIRED                         ║
║  ✅ Trader ek paragraph likhe — plan turant dikhe                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

**Ye transformation ek line me:**
> Pehle: *form jo trader bharta hai.*  Ab: **form jo KHUD BHARTA HAI.**

## 4.4 — Flow model ka BEFORE / AFTER

```
❌ PEHLE — 13 STEPS, EK SEEDHI LINE
  1  Strategy Setup
  2  CTV Inventory
  3  Budget Allocation
  4  Audiences
  5  Targeting                ← #5 ne 3+4 merge kiya... (v2.0 me already)
  6  Reach Forecast
  7  Plan Approval            ← #23 ne GATE hataya
  8  Strategy Creation
  9  Credit Check      ┐
  10 Creative Upload   ├─ #27 ne ORDER hataya
  11 Tracking Setup    ┘
  12 Activate
  13 Confirm           ← #28 ne "confirm with client" hataya

✅ AB — SEQUENTIAL SPINE + PARALLEL TAIL

  ┌─────────────────── SEQUENTIAL SPINE (~7 steps) ────────────────────┐
  │                                                                     │
  │  Brief → Inventory → Budget → Targeting → Forecast → Plan → Create  │
  │  parse   (matched,    (split   (defaults   (repair    (status  (asin│
  │  (infer   not          derived) applied)    loop)      only)    = [])│
  │   all)    selected)                                                 │
  └──────────────────────────────┬──────────────────────────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ↓                  ↓                  ↓
      ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
      │  CREATIVES    │  │   TRACKING    │  │ CREDIT CHECK  │
      │  upload +     │  │   asin/adtag  │  │               │
      │  approval     │  │  + conversions│  │               │
      │  per channel  │  │  → UPDATE     │  │               │
      └───────┬───────┘  └───────┬───────┘  └───────┬───────┘
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 ↓
                      ╔══════════════════════╗
                      ║   🚦  ACTIVATE       ║
                      ║  6 prerequisites     ║
                      ║  sab check hone par  ║
                      ╚══════════════════════╝
```

## 4.5 — Interrupts ka before/after

| | Pehle | Ab |
|---|---|---|
| `AWAIT_INPUT` (trader se poochhna) | ✅ | ✅ **bacha** |
| `AWAIT_APPROVAL` (manager ka wait) | ✅ | ❌ **gaya** (#23) |
| **Kul asli blocking points** | 2 | **1** |

## 4.6 — Naye SOURCE TYPES — jo document me the hi nahi

```
Document me sirf DO implicit sources the: "trader bharta hai" ya "API se aata hai"
28 comments ne AATH sources demand kiye:

  💬 ASKED       trader se poochhna hi padega        (kam se kam!)
  🧠 INFERRED    brief ke text se nikala             #3, #6, #8, #9, #15
  ⚙️ DERIVED     doosri field se calculate kiya       #3, #7, #21
  🏢 ADVERTISER  advertiser record se aaya            #13, #15, #16, #22
  ⚙️ GENERATED   system ne banaya (naam)             #6
  🔒 FIXED       system constant                      #14
  🔌 API         API se pre-populated                 #1, #15
  ⏳ LATER       is step me nahi — baad me            #16, #17

🔴 Isliye SCHEMA me ek naya column chahiye: SOURCE
   Ye 5 comments ne independently demand kiya (#7, #9, #11, #13, #21)
```

## 4.7 — Score card

| | Kitne |
|---|---|
| Kul comments | **28** |
| Poori tarah samjhe | **28 / 28** ✅ |
| 🔴 Schema changes chahiye | ~53 |
| ✏️ Wording changes chahiye | ~145 |
| 🔀 Flow/state machine changes | ~56 |
| ❓ David se poochhne wale sawaal | ~56 (3 blocking) |
| 📝 Mastery file me fix karne wali cheezein | ~63 |
| ✅ Open questions RESOLVED | 4 (#1, bundles, ASIN timing, broad/WIDE) |
| 🎉 Gaps jo Kareem ne pehle flag kiye aur David ne confirm kiye | 3 (#25, #26, #27) |
| 🎉 v2.0 ke ⚠ markers jinka David ne seedha jawab diya | 2 (#20, #28) |
| ⚠ Meri apni self-corrections | 4 |
| 🔴 Baaki blocking sawaal | **3** |

═══════════════════════════════════════════════════════════════════════════════

# PART 5 — SAWAAL BANK — MEETING KE LIYE TAYYAR

═══════════════════════════════════════════════════════════════════════════════

Ye section meeting ke liye hai. Kisi ne kuch pooch liya — jawab yahan hai.

## 5.1 — 🔴 TEEN BLOCKING SAWAAL (David ko bhejne hain)

Ye teen sawaal ke bina schema **finalise nahi ho sakti**:

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  🔴 BLOCKER 1 — Audience suggest endpoint ka REAL response sample            ║
║                                                                              ║
║  Sawaal: POST /api/audience-sets/suggest/ ka ek actual response de dijiye?    ║
║  Kyun:   #20 ne bataya `bundles` shape nahi hai — par sahi shape kya hai?     ║
║  Kya unblock hoga: (a) grouping logic, (b) effective CPM ka ganit (#2),        ║
║                    (c) AudienceSchema ka poora shape                          ║
║  Isse rukka hua kaam: Audience module ka poora design                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  🔴 BLOCKER 2 — Deal ki built-in targeting STRUCTURED metadata me hai?        ║
║                                                                              ║
║  Sawaal: Jab GET /api/deals/ se deal aati hai, uski built-in targeting        ║
║          (genre, ROS, audience) structured fields me hai — ya sirf deal ke    ║
║          NAAM me? ("Prime Video | Preferred | UK - 30 - ROS")                 ║
║  Kyun:   #18 kehta hai agent deals MATCH kare. Agar targeting sirf naam me    ║
║          hai, to agent ko STRING PARSE karni padegi — jo Zero-Hallucination   ║
║          Policy ke SEEDHA KHILAAF hai                                        ║
║  Kya unblock hoga: Deal matching logic — ya to possible hai ya nahi           ║
║  Isse rukka hua kaam: Step 2 ka poora naya model                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  🔴 BLOCKER 3 — CTV endpoint family me KYA-KYA hai?                          ║
║                                                                              ║
║  Sawaal: #24 ne bataya strategy creation ka CTV variant hai                   ║
║          (simple-strategies). Baaki endpoints ka bhi hai?                     ║
║            • deals · audience-sets/suggest · locations                        ║
║            • contextual-targeting · reach forecast                            ║
║            • aur UPDATE endpoint ka naam kya hai? (#28)                       ║
║  Kyun:   §4 ka poora API catalogue is par depend karta hai                    ║
║  Kya unblock hoga: §4 ka verification — jo ab poori tarah shak me hai         ║
║  Isse rukka hua kaam: Wajahat ka backend integration                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Plus ek **scope decision** (blocker nahi, par jaldi chahiye):
> **Multi-market M1 me hai ya M2 me?** — #3 aur #8 ne multi-market ko real bana diya (budget split, market inference). Agar M1 me hai to per-market currency, per-market deals, per-market reach summing sab design karna hoga.

## 5.2 — Sawaal jo koi bhi pooch sakta hai (aur jawab)

### A. Poore review ke baare me

| Sawaal | Jawab |
|---|---|
| **"28 comments = document bekaar tha?"** | Nahi. **Core architecture bilkul bacha** — 3 principles (Zero-Hallucination, Self-Filling Form, API-Driven), 3 inventory tiers, deal types ka logic, reach/frequency ka ganit, repair loop, change ledger — sab intact. Comments **interaction model** par hain: kaun kya bharta hai, kis kram me. Ek bhi comment ne architecture ko challenge nahi kiya. |
| **"Sabse bada seekhna kya hai?"** | Ek line: **"Required" ka matlab "Asked" nahi hota.** Field zaroori ho sakti hai — par uski value **infer, derive, ya advertiser record se** aa sakti hai. Document ne dono ko mila diya tha, isliye 12 fields galat tarah se "trader se poochho" ban gaye. |
| **"Ye galtiyan kahan se aayin?"** | Do jagah se: (1) **v1.1.0 ka form-wizard model** — wo ek UI form ke liye likha gaya tha jahan trader HI bharta hai. v2.0 ne flow badla par field requirements as-is chhod diye. (2) **v1.1.0 ke API examples** kabhi re-verify nahi hue (#20, #24). |
| **"Aage kaise rokenge?"** | Teen cheezein: (a) **SOURCE column** — har field par likho ki value kahan se aati hai, to "required = asked" ki galti dobara na ho; (b) **API examples par verification date** — unverified ho to ⚠ mark ho; (c) **config-driven rule** (#26) — jo badal sakta hai wo code me na ho. |

### B. Schema ke baare me

| Sawaal | Jawab |
|---|---|
| **"Kitni schema badlegi?"** | ~53 changes. Bade wale: 6 naye schemas (`AdvertiserDefaultsSchema`, `AdvertiserSetting`, `DealMatchCriteriaSchema`, `AudienceBundleConstructionSchema`, `ActivationPrerequisitesSchema`, `PlanStatusEnum`), 2 naye enums (`TargetingSourceEnum`, `AudienceDataSourceEnum`), ~12 fields ka requirement badalna, 2 fields hatana, 3 hard-coded fields → ek dict. |
| **"Wajahat ka kaam barbaad hua?"** | **Nahi — bacha.** Isliye ye review **code likhne se pehle** hua. Agar `bundles` shape par module ban jaata (#20), ya `/api/strategies/` par integration (#24) — to POORA module dobara likhna padta. |
| **"Advertiser defaults kya hai — naya module?"** | Ek naya **concept** hai jo document me tha hi nahi. David ne **3 baar** confirm kiya (#13 frequency cap, #15 product category, #22 device type). Aur #16 ne chautha add kiya (product location). Ek `AdvertiserDefaultsSchema` chahiye jisme har setting `AdvertiserSetting` (value + is_locked + reason) me wrapped ho. |
| **"`is_locked` kyun chahiye?"** | Kyunki #22 me David ne kaha *"Some advertisers ONLY WANT CTV only"* — ye ek **policy** ho sakti hai, ek **default** nahi. Farak: default trader override kar sakta hai aur repair loop relax kar sakta hai; **constraint nahi kar sakta**. Repair loop ko pata hona chahiye ki kaunsa lever locked hai. |

### C. Agent behaviour ke baare me

| Sawaal | Jawab |
|---|---|
| **"Agent kitna INFER karega — hallucination ka risk?"** | Infer ≠ invent. Agent brief ke **text** se nikaalta hai (*"education website"* → Education category), API ke **response** se leta hai, ya **advertiser record** se. Ye teeno **verifiable sources** hain. Zero-Hallucination Policy bachi rehti hai: agent kabhi CPM ya reach ka number khud nahi banata — wo hamesha API se aata hai. |
| **"Agar agent galat infer kare?"** | Do safety: (1) agent jo infer kiya wo **dikhata** hai (*"Maine GB market maan liya kyunki brief me 'UK' likha hai"*), (2) trader **override** kar sakta hai. Ye "ask nahi karna" nahi hai — "**default bharo, confirm karne do**" hai. |
| **"Repair loop ab bhi kaam karega?"** | Kaam karega par **levers kam ho gaye**: audience optional hai to wo lever kabhi na ho (#4); fixed-CPM deals me bid lever nahi (#12); device advertiser-locked ho sakta hai (#22); 3P par effect verify nahi hota (#19). Isliye agent ko **imaandar** hona chahiye: *"Maine ye kiya, par asar confirm nahi kar sakta"* / *"Device relax karna chahta tha par advertiser policy locked hai."* |
| **"Trader ka control kam ho gaya?"** | Nahi — **badla**. Pehle: 13 sawaalon ke jawab do. Ab: bharaa hua plan dekho aur jo galat hai wo badlo. Aur escape hatches hain — deal ID de sakte ho (#18), sab defaults override kar sakte ho. **Control** wahi hai, **shuruati mehnat** kam hai. |

### D. Team ke liye specific

| Kaun | Kya jaanna chahiye |
|---|---|
| **Wajahat (backend/agent)** | Step 1 ke 12 fields ka source badla — 3 hi required hain. Deal selection → **matching** (naya `DealMatchCriteriaSchema`). Advertiser defaults ka **naya lookup** chahiye. State machine: `AWAIT_APPROVAL` hata, tail unordered hai (conditional edges). Audience grouping **hum** karenge, API nahi (#20). §4 endpoints **verify hone tak integration mat likho**. |
| **Vishal (frontend)** | Deals ki **checkbox table nahi banani** (#18) — sirf channel + CPM dikhana hai. Approval status **dynamic list** hai (#26) — dict par loop karo, 3 fixed rows nahi. Plan approval ek **status toggle** hai, approval workflow nahi (#23). Creative/tracking/credit **kisi bhi kram** me — UI ko order enforce nahi karna (#27). |
| **Basil (QA)** | Test cases badlenge: Step 1 me **zero asked-and-required** field. Activation ke **6 prerequisites** test karne hain (#27). Advertiser defaults ka **override aur lock** dono test karo (#22). Unordered tail ke **permutations** test karo. |
| **Kareem (mera kaam)** | Document ke ~145 wording + ~53 schema fixes. Mastery file ke ~63 fixes. 3 blocking sawaal David ko. 28 replies Confluence par. |

## 5.3 — TEEN cheezein jo ek line me yaad rakhni hain

```
1️⃣  "Required" ≠ "Asked"
    Field zaroori ho sakti hai, par uski value infer/derive/advertiser
    se aa sakti hai. Ye 12 comments ki jad hai.

2️⃣  Trader "KYA CHAHIYE" batata hai — agent "KAISE MILEGA" nikaalta hai
    Deal ID, currency, budget split, strategy name — sab technical.
    Trader ka kaam: brief, channel, genre, budget.

3️⃣  Jo cheez badal sakti hai, wo CODE me nahi honi chahiye
    Publisher list, market list, genre list — config/API se.
    Sirf STATES (PENDING/APPROVED) code me.
```

═══════════════════════════════════════════════════════════════════════════════

# PART 6 — SAB 28 EK PAGE PAR (CHEAT SHEET)

═══════════════════════════════════════════════════════════════════════════════

Meeting me ye ek page kholo — pura review yahan hai.

| # | Kahan | David ne kya kaha | Matlab | Sev |
|---|---|---|---|---|
| 1 | §2.3 tier · Audiences | *"amazon dsp or the inventory source"* | 3P par targeting DONO se aa sakti — Amazon ya SSP. Naya `TargetingSourceEnum`. | 🔴 |
| 2 | §2.3 tier · Data fee | *"only if using amazon audiences"* | Fee **data source** par lagti, segment count par nahi. → 3 profiles ka cost farak KHATAM | 🔴 |
| 3 | Step 1 · Budget split | *"NEW"* + *"mandatory"* | Split **derive** karo (equal), poochho mat. Multi-market real hai. | 🔴 |
| 4 | Step 1 · Targeting | *"NEW"* | Audience **optional** hai — mandatory nahi. Repair loop ka lever ja sakta hai. | 🔴 |
| 5 | Step 3+4 | *"default targeting like country + CTV device"* | Targeting **pehle se bhari** aati hai. Do steps merge. | 🔴 |
| 6 | Step 1 · Name + dates | *"Strategy name, flight dates"* | Naam **generate** karo, dates **infer** karo. Dono optional. | 🟡 |
| 7 | Step 1 · Currency | *"Required"* | Currency **market se derive** hoti hai — poochho mat. Multi-market me conflict. | 🟡 |
| 8 | Step 1 · Markets | *"Multi-select"* | Market **brief se infer** karo. Multi-market design chahiye. | 🟡 |
| 9 | Step 1 · KPI | *"Required"* | KPI **brief se infer** karo. | 🟡 |
| 10 | Step 1 · KPI | *"if frequency then kpi target 1-5"* | ➕ Naya conditional field `kpi_target_value` (1–5). | 🟡 |
| 11 | Step 1 · Budget | *"Table (single market budget?)"* | "Table" ek **UI widget** hai, data type nahi. Level confusion. | 🟡 |
| 12 | Step 1 · Frequency | *"not required for CTV as defined by CPM of deals"* | Frequency **deal ke CPM se derive** hoti. Fixed-CPM = bid lever nahi. | 🔴 |
| 13 | Step 1 · Freq cap | *"we have a default per advertiser"* | 🔴 **ADVERTISER DEFAULTS** — poora naya concept (1st of 3). | 🔴 |
| 14 | Step 1 · Formats | *"is always streaming_tv"* | Prime Video ek **provider** hai, format nahi. Document self-contradicting tha. | 🟡 |
| 15 | Step 1 · Categories | *"default on advertiser, or imply from brief"* | Advertiser default → brief → ASIN response. (2nd advertiser confirm) | 🔴 |
| 16 | Step 1 · Selling loc | *"can leave out"* | Step 1 se **hatao** → Step 11. OQ-1 ka aadha jawab. | 🔴 |
| 17 | Step 1 · ASINs | *"comes later"* | Step 1 se **hatao**. OQ-1 RESOLVED = Option A. | 🟡 |
| 18 | Step 2 · Deals | *"remove technical need to select deals... only the CPM"* | 🔴🔴 Deals **match** karo, table dikhao mat. Trader ko sirf CPM. | 🔴🔴 |
| 19 | Step 4 · Constraints | *"can use amazon audiences too"* | Amazon audiences **3P par bhi** lagti. Effective CPM ka ganit widen. | 🔴 |
| 20 | Step 4 · ⚠ Open Q | *"not currently supported"* | `bundles.narrow/balanced/broad` API me **nahi**. Grouping HUM karenge. | 🔴 |
| 21 | Step 5 · Location | *"defaults to market country"* | Location **market country** par default. `markets` ≠ `location`. | 🟡 |
| 22 | Step 5 · Device | *"Some advertisers only want CTV only - advertiser level"* | Advertiser level (3rd confirm). **Format vs device** ka fix. `is_locked`. | 🔴 |
| 23 | Step 7 · Approval | *"just a status... no manager approval for now"* | Manager gate **hata**. `PlanStatusEnum{DRAFT,FINALISED}`. Interrupt gaya. | 🟢 |
| 24 | Step 8 · Endpoint | *"probably more likely simple-strategies"* | Endpoint **naam galat**. §4 ka poora catalogue shak me. | 🔴 |
| 25 | Step 10 · CTA URL | *"optional for streaming tv"* | TV remote se click nahi hota. Required → Optional. | 🟢 |
| 26 | Step 10 · Approvals | *"single status for each channel... could be paramount or channel 4"* | Hard-coded naam **hatao** → `dict[str, ApprovalStatusEnum]`. **Config-driven rule.** | 🔴 |
| 27 | Step 11 · Tracking | *"could be done before creatives... no order necessary"* | 🔴🔴 **13-step chain toot gaya.** Spine + parallel tail + activation gate. | 🔴🔴 |
| 28 | Step 11 · Confirm | *"no they can be updated after creation"* | Strategy **mutable** hai. OQ-1 ka final jawab + #27 ka mechanism. | 🔴 |

---

## 🎉 TEEN JAGAH JAHAN KAREEM SAHI THA — DAVID SE PEHLE

```
1️⃣  #18 — Deal matching ka pattern
    v2.0 me Tier 3 (Disney+) ke liye maine likha tha:
      "agent captures what VOW needs to curate later: genres, durations,
       targeting preferences, budget, flight dates"
    → Ye BILKUL David ka model hai. Bas Tier 1/2 par apply nahi kiya.

2️⃣  #19 — Note 1 me prediction
    Maine likha tha: "Also corrected in: the Targeting step constraints"
    → David ne exactly wahi jagah #19 me pakdi.

3️⃣  #27 — Activation gate ka gap
    Maine flag kiya tha: "There is no explicit 'what must be true
    before Activate' checklist."
    → #27 ne wahi confirm kiya.
```

## ✅ DO JAGAH JAHAN "⚠ FLAG KARNA" NE BADA NUKSAAN BACHAYA

```
#20 — Maine likha tha: "⚠ Open question: the suggest endpoint's response
      shape. v1.1.0 assumed bundles... Confirm against the real API."
      → David: "not currently supported" — flag SAHI tha
      → Agar assume kar liya hota: poora audience module dobara likhna padta

#28 — Maine likha tha (do baar): "⚠ product_location aur asin_numbers ka
      timing conflict. Option A ya Option B?"
      → David: "they can be updated after creation" — seedha jawab
      → Sawaal poochha, isliye jawab mila
```

**Sabak:** jahan pakka na ho, wahan **⚠ flag karo** — assume mat karo. Dono baar wo bacha liya.

---

## 📊 AB AAGE KYA — 5 KAAM

```
1️⃣  🔴 David ko 3 blocking sawaal bhejo (Part 5.1) — short message
     + multi-market M1/M2 ka scope decision

2️⃣  📄 Reviewed document Confluence par publish karo
     File: strategy_schema_documentation_v2.0_reviewed.md (49 review notes)
     ⚠ §4 aur §5 ke code blocks original se verify kar lo

3️⃣  💬 28 replies Confluence par post karo
     Sab drafts david_comments_tracker.md me tayyar hain
     Tone guide: correction / design change / hint / "maine flag kiya tha"

4️⃣  📝 Mastery file ke ~63 fixes
     List: tracker ka "Mastery-file me fix karne wali cheezein" section

5️⃣  🔧 Schema v2.1 likhna — SIRF blocking sawaalon ke jawab ke BAAD
     ~53 changes, 6 naye schemas, 2 naye enums
```

---

**Review complete: 28 / 28 ✅**

*Is file ka maksad: koi bhi comment koi bhi pooche — jawab yahan hai.*







