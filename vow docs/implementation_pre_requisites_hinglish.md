# VOW Platform - Implementation Pre-Requisites & Key Concepts (Hinglish Guide)

**Document Name:** `implementation_pre_requisites_hinglish.md`  
**Purpose:** Implementation se pehle jante hone wale 6 sabse important technical & architectural concepts ka complete breakdown.  
**Target Audience:** Developers, QA Engineers, System Architects, Technical Project Managers.  

---

## 📌 Executive Summary (Implementation Se Pehle Ye 6 Baatein Jaanna Kyun Zaroori Hain?)

Coding ya testing start karne se pehle VOW Platform ke **6 core pillars** ko samajhna zaroori hai. 

Is document me bataya gaya hai ki **System Backend kaise sochta hai**, **AI Agent state kaise maintain karta hai**, aur **APIs aapas me kaise communicate karti hain**.

---

## 🧭 1. LangGraph State Machine & Pydantic Validation (System Engine)

### Kya Jaanna Zaroori Hai?
VOW Agent ek normal ChatGPT-like chatbot nahi hai. Ye **LangGraph State Machine** engine par chalta hai.

```
[User Message / Brief] 
        │
        ▼
[Parse & Extract] ──► [Pydantic Schema Validation] ──► [VOW REST Tool Execution] ──► [Strategy Creation]
```

### Key Technical Rules:
1. **Zero-Hallucination Policy:** AI Agent apni taraf se koi fake Deal ID, Currency, ya Pricing numbers guess nahi karega. Wo sirf VOW REST APIs se milne wale data ko hi use karega.
2. **Self-Filling Slot Engine:** Har conversation step me agent **Pydantic Data Models** ke slots fill karta hai. Jab tak mandatory slots (Dates, Market, Budget) nahi bhar jate, strategy finalise nahi ho sakti.

---

## 🎯 2. CTV Simplification & Inferred Defaults Paradigm

### Kya Jaanna Zaroori Hai?
Old legacy UI me user ko 15+ form fields manually bharne padte the. Naye VOW CTV Architecture me **user se sirf 3-4 simple inputs** liye jate hain.

### Flow Breakdown:
- **User Inputs (Agent poochhega):**
  1. Campaign Flight Dates (e.g. `01/08/2026` to `31/08/2026`)
  2. Target Market Country ISO (e.g. `GB` for UK)
  3. Total Campaign Budget (e.g. `£10,000.00`)
- **System Inferences (Agent khud auto-fill karega):**
  - **Strategy Name:** `{Category}_{Market}_{Goal}_{MonthYear}` (e.g. `Education_UK_Awareness_Aug2026`). Duplicate milne par auto `_v2` add karega.
  - **Primary Currency:** Market ISO se infer karega (`GB` $\rightarrow$ `GBP` £, `DE` $\rightarrow$ `EUR` €).
  - **Ad Formats:** Defaulted to `['streaming_tv']`.
  - **Goal & KPI:** Goal defaults to `AWARENESS`, KPI defaults to `reach` (ya `frequency` range `1-5`).
  - **Base CPM Bid:** Manual input omit; seedha selected deal rate card CPM se calculate hoga.

---

## 💰 3. Background Deal Matching & CPM Pricing Abstraction

### Kya Jaanna Zaroori Hai?
System me technical deals ke **checkbox tables hataye gaye hain**.

### How Pricing Works:
1. **Background Deal Match:** User market aur dates batata hai. Agent backend API `GET /api/deals/?markets={market}` call karke optimal deals khud select karta hai.
2. **CPM Abstraction:** User ko complex technical Deal IDs (jaise `EXT7P75718S8MNR`) nahi dikhani hoti. Screen par sirf final **Rate Card CPM** (e.g. `£28.88`) dikhaya jata hai.
3. **Blended Effective CPM Calculation:**
   $$\text{Blended Effective CPM} = \text{Base Deal CPM} + \text{Stacked VCPM Data Fees}$$

---

## 🗺️ 4. Unified Baseline Targeting Architecture

### Kya Jaanna Zaroori Hai?
Targeting ko isolated steps me divide nahi kiya gaya hai. System me **Default Baseline** ka concept hai.

```
+---------------------------------------------------------------------------------------------------+
|                            UNIFIED TARGETING ARCHITECTURE                                         |
+---------------------------------------------------------------------------------------------------+
|  [AUTOMATED DEFAULT BASELINE]:                                                                    |
|  1. Country Geo-Targeting : ISO Country Code (Defaults to Target Market Country e.g. GB / UK)     |
|  2. Device Environment    : Connected TV (CTV) / Living Room Devices (Inherited from Advertiser)  |
|                                                                                                   |
|  [OPTIONAL TARGETING REFINEMENT BRANCHES]:                                                       |
|  - Branch A: Add Audience Segments  (Amazon 1P / 3P data fees stack per provider)                |
|  - Branch B: Geo/Postcode Targeting (Specify Postcodes e.g. SW1A 1AA - No data fees)              |
|  - Branch C: Accept Baseline        (Run on ROS / Contextual deal targeting without extra filters)|
+---------------------------------------------------------------------------------------------------+
```

---

## 🔄 5. Flexible Downstream Modular Execution & Post-Creation `PATCH` Updates

### Kya Jaanna Zaroori Hai?
Strategy creation aur downstream setup me **dono baatein sabse important hain**:

1. **Direct Strategy Publication:**
   - Strategy plan finalise hone par seedha **`POST /api/simple-strategies/`** execute hota hai aur status **`finalised`** ho jata hai (Manager approval ki zaroorat nahi hai).
2. **Flexible Downstream Execution Order:**
   - Strategy finalise hone ke baad 2 downstream modules hote hain:
     - **Module A (Creatives Binding & Approvals):** Video assets upload aur channel approvals.
     - **Module B (Tracking Setup):** ASIN validation aur conversion pixels.
   - Dono modules **decoupled aur non-sequential** hain. Video ready na ho to pehle Tracking Setup kar sakte hain, ya vice-versa.
3. **Post-Creation Field Updates (`PATCH` API):**
   - `product_location`, `product_asins`, aur tracking details initial strategy creation ko block nahi karte.
   - Platform strategy publish hone ke baad **`PATCH /api/strategies/{id}/`** API call karke in fields ko kisi bhi time update karne ki permission deta hai.

---

## 🔌 6. Core REST API Catalog Quick Reference

Developer team ko implementation ke wqt in **4 primary REST Endpoints** ka contract pata hona chahiye:

| Endpoint Path | HTTP Method | Purpose & Payload Shape |
| :--- | :--- | :--- |
| **`/api/simple-strategies/`** | `POST` | **Strategy Creation**: Lean Pydantic payload containing Dates, Market, Budget, Auto-Deals, and Baseline Targeting. Creates strategy with status `finalised`. |
| **`/api/strategies/{id}/`** | `PATCH` | **Post-Creation Update**: Used to attach deferred ASINs, selling location, and conversion pixels to an existing strategy post-creation. |
| **`/api/audience-sets/suggest/`** | `POST` | **Audience Suggestion**: Vector search endpoint that returns a **Flat List** (`List[AudienceSet]`) of recommended audience sets. |
| **`/api/strategies/reach-forecast/`** | `POST` | **Reach Curve Forecasting**: Calculates expected unique reach and frequency distribution for the strategy card. |

---

## 📝 Check-List Before Code Implementation

- [ ] Pydantic Schemas check kar liye hain (`Step1DetailsSlotSchema`, `Step2GoalKPIBidSlotSchema`, `UnifiedTargetingSlotSchema`, `SelectedCreativeSchema`).
- [ ] Direct Creation Endpoint `POST /api/simple-strategies/` implement karne ka logic clear hai.
- [ ] Post-Creation Updates ke liye `PATCH /api/strategies/{id}/` operational path test kar liya hai.
- [ ] Dynamic Channel Approvals (`channel_approval_statuses: Dict[str, ApprovalStatusEnum]`) model design samajh aa gaya hai.
- [ ] Agent Inferences (Name, Currency, Formats, Category) test-driven logic ready hai.

---

## 📄 Related Project Specification Documents
- 📄 **Beginner Glossary Document:** [vow_technical_glossary_hinglish.md](file:///e:/VOW%20Agent/vow_technical_glossary_hinglish.md)
- 📄 **Hinglish Review Guide (28 Comments):** [update_schema_registery_hinglish.md](file:///e:/VOW%20Agent/update_schema_registery_hinglish.md)
- 📄 **Main Technical Specification:** [update_strategy_schema_registry.md](file:///e:/VOW%20Agent/update_strategy_schema_registry.md)
- 📄 **Formal Change Audit Registry:** [updated_schema_registry.md](file:///e:/VOW%20Agent/updated_schema_registry.md)
