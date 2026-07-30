# VOW Platform — Strategy Schema (Revised v2.0) Complete Mastery Guide (Hinglish Version)

**Document Name:** `vow_strategy_schema_v2_mastery_hinglish.md`  
**Source Specification:** Confluence Document: *VOW Platform — Strategy Schema (Revised v2.0)* (`VOWAgent-Strategy Schema documentation v2.0-300726-065820.pdf`)  
**Target Audience:** Kareem (Planning Agent Owner), Wajahat, Vishal, Backend/Frontend Engineers, QA Lead, Product Managers.  
**Purpose:** Strategy Schema Registry aur Confluence Specification v2.0 ki 100% complete A-to-Z mastery. Is document ke baad aap poori team ke kisi bhi sawaal ka instant, 100% accurate javab de sakenge!

---

## 📌 PART 1: Executive Overview & Project Background

### 1.1 Ye Document Kyun Banaya Gaya? (What is Confluence v2.0?)
Pehle legacy VOW UI me strategy creation me **15+ manual form fields** hote the, manager approval ke rigid prompt loops the, aur pricing/deals complex checkboxes me bhari rehti thi.

Client Representative (**David Moss**) ne 28 review comments diye. Un 28 comments ko resolve karke jo final technical specification bani, use Confluence par **`Strategy Schema documentation v2.0`** ke roop me upload kiya gaya hai. 

**Puri engineering team (Frontend, Backend, AI Agent, QA) isi document se kaam karegi.**

### 1.2 Planning Agent Ka Role Kya Hai? (Kareem's Core Task)
Slide ke plain terms me: **"A form that fills itself in as you chat."**

User jab natural language me campaign brief bolega (e.g., *"I want a £10k CTV campaign for UK in August"*), to Planning Agent:
1. User se **sirf 3-4 simple inputs** poochhega (Dates, Market, Budget).
2. Baaki sab **auto-infer** karega (Name, Currency, Format, Category, Base Bid).
3. Background me VOW APIs se **Deals** match karega aur **CPM prices** calculate karega.
4. **Reach Forecast** chalayega aur kam reach aane par auto-widen repair loop chalayega.
5. Final Strategy Card banakar status **`finalised`** karke UI (Riddhi) ko hand-over karega.

---

## 🧭 PART 2: Section-by-Section Deep Dive (Section 1 to 6)

---

### 🟢 SECTION 1: Strategy Details Setup (Step 1)

#### 1. Automated Naming Convention & `_v2` Auto-Repair (Comment #7)
- **Rule:** User se Strategy Name nahi poochna hai. System context se auto-name generate karega:
  $$\text{Strategy Name} = \text{\{Category\}}_{\text{\{MarketISO\}}}_{\text{\{Goal\}}}_{\text{\{MonthYear\}}}$$
  - *Example:* Education category, UK market, Awareness goal, Aug 2026 $\rightarrow$ `Education_UK_Awareness_Aug2026`.
- **Duplicate Repair:** Agent pehle `GET /api/strategies/check_strategy_name_uniqueness/` call karega. Agar name pehle se exist karta hai, to system bina user ko disturb kiye auto-append karega: `Education_UK_Awareness_Aug2026_v2`.

#### 2. Campaign Flight Dates & Interval Notation
- **Input:** Flight dates ISO format me hoti hain (`2026-08-01` to `2026-08-31`).
- **Interval Bounds:** API `[)` bounds notation use karti hai (lower inclusive, upper exclusive).

#### 3. Market Country ISO & Automated Currency Inference (Comments #9, 21)
- **Rule:** User se Currency nahi poochni hai. Target Market ISO se currency auto-infer hogi:
  - `GB` (United Kingdom) $\rightarrow$ **`GBP` (£)**
  - `DE` / `FR` / `ES` / `IT` (EU Markets) $\rightarrow$ **`EUR` (€)**
  - `US` (United States) $\rightarrow$ **`USD` ($)**

#### 4. Automated Format Defaulting (Comment #15)
- **Rule:** CTV-first strategies ke liye Ad Format default list **`['streaming_tv']`** hogi.

#### 5. Product Category Brief Inference (Comment #16)
- User ke brief text ya advertiser profile se category ID auto-infer hogi (e.g. *"Online Course"* $\rightarrow$ Category `Education`).

#### 6. Deferred Fields (Post-Creation `PATCH` Collection - Comments #17, 28)
- **Crucial Rule:** `product_location` (ON_AMAZON / NOT_SOLD_ON_AMAZON) aur `product_asins` initial strategy creation ko **BLOCK nahi karte**. Ye inputs optional/deferred hain aur strategy create hone ke baad **`PATCH /api/strategies/{id}/`** endpoint se update kiye ja sakte hain.

---

### 🔵 SECTION 2: Goal, KPI & Budget Allocation (Step 2)

#### 1. Strategy Goal & Default KPI (Comments #10, 15)
- **Goal Default:** CTV campaigns ke liye default Goal **`AWARENESS`** hota hai.
- **KPI Target:** Default KPI **`reach`** hota hai.

#### 2. Frequency KPI Target Value Range (Comment #10)
- Agar user KPI me `frequency` choose karta hai, to valid target value range **`1 to 5`** ke beech me honi chahiye (e.g. target frequency = 3 views per user).

#### 3. Frequency Capping Advertiser Profile Inheritance (Comment #14)
- User se complex frequency capping rules (e.g., *2 impressions per 24 hours*) nahi lene hain. System Advertiser Profile ke default capping rules inherit karega.

#### 4. Base CPM Bid Omission for CTV (Comment #13)
- CTV inventory fixed rate card / floor rate deals par chalti hai. Manual Base CPM Bid Input **omit** kar diya gaya hai; bid amount selected deal ke CPM rate se derive hoga.

#### 5. Single Numeric Budget Input (Comment #12)
- Single market campaign me user se ek hi total budget float input (e.g. `10000.00`) liya jayega.

#### 6. Tracked Ad Tag Conversions (Comments #4, 28)
- Web conversion pixels (e.g. `PAGE_VIEW`, `APPLICATION`) deferred hote hain aur strategy creation ke baad `PATCH` API se attach kiye ja sakte hain.

---

### 🟣 SECTION 3: Inventory Deals & Pricing Abstraction (Step 3)

#### 1. Background Deal Matching (Comment #18)
- **Rule:** Legacy UI ke complex technical deal checkbox tables hataye gaye hain.
- Planning Agent background me VOW API `GET /api/deals/?markets={market}&formats=streaming_tv` hit karke optimal deals khud select karega.

#### 2. CPM Pricing Abstraction (Comment #19)
- User ko complex technical Deal IDs (jaise `EXT7P75718S8MNR`) nahi dikhani hain.
- Screen par sirf Publisher Name (e.g., **Paramount+**, **Prime Video**) aur final **Rate Card CPM** (e.g. **£25.33**) dikhana hai.

#### 3. Blended Effective CPM Calculation (Comment #2)
$$\text{Blended Effective CPM} = \text{Base Deal Rate Card CPM} + \text{Stacked VCPM Data Fees}$$
- *Example:* Prime Video Deal CPM (£25.00) + Amazon 1P Data Fee (£2.00) = **£27.00 Effective CPM**.

#### 4. Inventory Tiers & Supply Locations (Comment #1)
- **Inventory Tiers:** `AMAZON_OWNED` (Prime Video), `THREE_P_PRE_CURATED` (Netflix/Disney+ curated), `THREE_P_NEEDS_CURATION`.
- **Targeting Choice:** Advertisers choose between `AMAZON_DSP` (DSP-side device/geo) or `SUPPLY_SIDE_SSP` (publisher supply deal).

---

### 🟠 SECTION 4: Unified Baseline Targeting Architecture (Step 4)

#### 1. Automated Default Baseline (Comments #5, 21, 22)
Inventory select hote hi **Default Baseline Targeting** automatically apply ho jata hai:
- **Country Geo-Targeting:** ISO Country Code (Defaults to Target Market Country e.g. `GB`).
- **Device Environment:** Connected TV (`CTV` Living Room Devices inherited from Advertiser Profile).

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

#### 2. Audience Data Fee Rules & Profile Naming (Comments #2, 20)
- **Vocabulary:** Client Vocabulary me profile name **"Wide"** use hoga (Broad nahi).
- **Single Fixed CPM per Data Provider:** Amazon 1P data (Lifestyle/In-market) use karne par 1 fixed CPM fee lagti hai (£2.00 VCPM), chahe kitne bhi 1P segments select kiye gaye hon (same provider me compounding nahi hoti).
- **Cross-Provider Stacking:** Agar Amazon 1P + 3P Experian Data dono select kiye, to dono fees stack hongi (£2.00 + £1.50 = £3.50 VCPM).
- **Flat List API Response:** `POST /api/audience-sets/suggest/` endpoint response shape **Flat List** (`List[AudienceSet]`) hoti hai.

---

### 🔴 SECTION 5: Creatives Binding & Dynamic Channel Approvals (Step 5)

#### 1. Media Asset Binding & Click-Through URL Optionality (Comments #25)
- Strategy finalize karne ke baad media assets bind hote hain.
- **Click-Through URL:** Ad format `streaming_tv` ke liye Landing Page URL **OPTIONAL** hota hai (Display/OLV ke liye REQUIRED).

#### 2. Dynamic Per-Channel Creative Approval Status Map (Comment #26)
- Static publisher fields remove karke dynamic map implementation hua hai:
  $$\text{channel\_approval\_statuses}: \text{Dict[str, ApprovalStatusEnum]}$$
- *Example:* `{'amazon': 'APPROVED', 'netflix': 'PENDING', 'disney_plus': 'APPROVED', 'paramount_plus': 'PENDING'}`

---

### 🟡 SECTION 6: Simplified Plan Approval & Publication Flow

#### 1. Direct Strategy Publication (Comments #23, 24)
- Legacy manager approval loops hataye gaye hain.
- Strategy proposal finalize hote hi seedha **`POST /api/simple-strategies/`** hit hota hai aur strategy status direct **`finalised`** ho jata hai.

#### 2. Non-Sequential Downstream Execution Order (Comment #28)
- Strategy publish hone ke baad 2 downstream modules hote hain:
  - **Module A (Creatives Binding & Approvals):** Video assets upload aur channel approvals.
  - **Module B (Tracking Setup):** ASIN validation aur conversion pixels.
- Dono modules **decoupled aur non-sequential** hain. Video ready na ho to pehle Tracking Setup kar sakte hain, ya vice-versa.
- Downstream fields post-creation **`PATCH /api/strategies/{id}/`** endpoint se update hote hain.

---

## 💻 PART 3: Complete Pydantic Schema Registry (Code Models)

Developer team ke liye production-ready Pydantic Models (`schemas.py`):

```python
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class FormatEnum(str, Enum):
    STREAMING_TV = "streaming_tv"
    PRIME_VIDEO = "prime_video"

class CurrencyEnum(str, Enum):
    GBP = "GBP"
    EUR = "EUR"
    USD = "USD"

class StrategyStatusEnum(str, Enum):
    DRAFT = "draft"
    FINALISED = "finalised"
    ACTIVE = "active"

class ApprovalStatusEnum(str, Enum):
    APPROVED = "APPROVED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    NOT_SUBMITTED = "NOT_SUBMITTED"

class Step1DetailsSlotSchema(BaseModel):
    name: Optional[str] = Field(None, description="Auto-generated if omitted e.g. Education_UK_Awareness_Aug2026")
    flight_dates: Dict[str, str] = Field(..., description="{'lower': '2026-08-01', 'upper': '2026-08-31'}")
    markets: List[str] = Field(..., description="['GB']")
    primary_currency: Optional[CurrencyEnum] = Field(None, description="Inferred GB -> GBP")
    formats: List[FormatEnum] = Field(default=[FormatEnum.STREAMING_TV])
    product_categories: List[int] = Field(default_factory=list)
    product_location: Optional[str] = Field(None, description="Deferred - updated via PATCH")
    product_asins: List[str] = Field(default_factory=list, description="Deferred - updated via PATCH")

class Step2GoalKPIBidSlotSchema(BaseModel):
    goal: str = Field("AWARENESS")
    kpi_target_type: str = Field("reach")
    kpi_target_value: Optional[int] = Field(default=3, ge=1, le=5)
    market_budgets: List[Dict[str, str]] = Field(..., description="[{'market': 'GB', 'budget': '10000.00'}]")

class SelectedDealSchema(BaseModel):
    deal_id: str
    name: str
    cpm: str
    inventory_tier: str = "AMAZON_OWNED"

class UnifiedTargetingSlotSchema(BaseModel):
    locations: List[str] = Field(default=["GB"])
    device_types: List[str] = Field(default=["CTV"])
    selected_audience_sets: List[Dict[str, str]] = Field(default_factory=list)

class SelectedCreativeSchema(BaseModel):
    asset_id: str
    asset_name: str
    click_through_url: Optional[str] = None
    channel_approval_statuses: Dict[str, ApprovalStatusEnum] = Field(default_factory=dict)

class FullStrategySchema(BaseModel):
    id: Optional[str] = None
    advertiser_id: str
    details: Step1DetailsSlotSchema
    goal_kpi_bid: Step2GoalKPIBidSlotSchema
    deals: List[SelectedDealSchema]
    targeting: UnifiedTargetingSlotSchema
    creatives: List[SelectedCreativeSchema]
    status: StrategyStatusEnum = StrategyStatusEnum.FINALISED
```

---

## 🔌 PART 4: Core REST API Catalog & Integration Matrix

| Endpoint Path | HTTP Method | Input Payload / Params | Response & Execution Logic |
| :--- | :---: | :--- | :--- |
| **`/api/strategies/choices/`** | `GET` | Headers: `Vowmade-Advertiser-Id` | Returns choices & existing strategy list (`VMA2026365`) for name uniqueness check. |
| **`/api/deals/`** | `GET` | `markets=GB&formats=streaming_tv` | Returns 62 UK CTV Deals with floor rates (e.g. Paramount+ @ £25.33 CPM) for auto-matching. |
| **`/api/audience-sets/suggest/`** | `POST` | `{"market": "GB", "goal": "AWARENESS", "prompt": "..."}` | Async Vector Search returning HTTP 202 Accepted `task_id` for flat list audience sets. |
| **`/api/conversions/definitions/`** | `GET` | `selected_advertiser_id={id}` | Returns tracking pixels (`APPLICATION`, `PAGE_VIEW`, `CHECKOUT`). |
| **`/api/simple-strategies/`** | `POST` | `FullStrategySchema` JSON | Strategy Creation & Publication with status `finalised`. |
| **`/api/strategies/{id}/`** | `PATCH` | `{"product_asins": [...], "ad_tag_conversions": [...]}` | Post-creation partial update for deferred fields. |

---

## 🧠 PART 5: LangGraph State Engine & Node Workflow

```
[START]
   │
   ▼
[Node 1: ParseUserBriefNode]      ──► User message se Flight Dates, Market, Budget extract karna
   │
   ▼
[Node 2: ValidateAndInferNode]    ──► Auto-infer Name, Currency, Format, Category & Pydantic validation
   │
   ▼
[Node 3: AutoMatchDealsNode]      ──► GET /api/deals/ hit karke optimal CTV deal pick karna & CPM surface karna
   │
   ▼
[Node 4: ReachForecastRepairNode]  ──► POST /api/strategies/reach-forecast/ hit karna; agar reach zero aati hai 
   │                                   to audience profile ko Narrow se Wide karke re-forecast karna
   ▼
[Node 5: PresentProposalCardNode]  ──► Executable Strategy Card JSON render karna
   │
   ▼
[Node 6: ExecuteStrategyCreateNode]──► POST /api/simple-strategies/ hit karke status 'finalised' karna
   │
   ▼
[END] (Handover to UI / Riddhi)
```

---

## 📖 PART 6: Beginner Technical Glossary (With Real-World Analogies)

1. **Amazon DSP (Demand-Side Platform):** Swiggy/Zomato app example jahan se advertiser ek hi jagah baith kar Prime Video, Netflix aur Web Portals ke ads buy karta hai.
2. **CTV (Connected TV):** Smart TV + Home Wi-Fi example (e.g. Prime Video movie ke beech me aane wala 15-sec ad).
3. **ASIN (Amazon Standard Identification Number):** Product ka unique "Aadhaar Card / Passport Number" (`B08N5WRWNW`).
4. **CPM (Cost Per Mille):** 1,000 Ad views ka kharcha (e.g. £25 CPM = 1,000 impressions par £25 cost).
5. **eCPM (Effective CPM):** $\text{Base CPM} + \text{Data Fee}$ (e.g. £25 Deal + £2 Data Fee = £27 eCPM).
6. **ROS (Run-of-Service):** TV News channel example jahan bina show restrict kiye poore platform par ad chalte hain.
7. **1P vs 3P Data:** Amazon ka apna shopping data vs External data companies ka data (Experian).
8. **VCPM Data Fee:** Audience data use karne ka extra charge (Single fixed fee per provider).

---

## 💬 PART 7: Team Q&A Cheat Sheet (Instant Answers for Kareem)

### Q1: Wajahat / Backend Engineer: *"Kareem, initial strategy creation me ASINs aur Product Location nahi mile to kya strategy create hogi?"*
👉 **Kareem's Answer:** *"Haan, 100% create hogi! Client Comment #17 & #28 ke mutabiq ASINs aur Product Location creation ko block nahi karte. Strategy `POST /api/simple-strategies/` se create ho jayegi aur baad me `PATCH /api/strategies/{id}/` endpoint se ye fields update ho jayenge."*

### Q2: Frontend Engineer (Riddhi): *"Strategy create hone par status kya hoga? Kya manager approval ke liye wait karna hoga?"*
👉 **Kareem's Answer:** *"Nahi, manager approval loop remove kar diya gaya hai (Comment #23 & #24). Strategy create hote hi status direct **`finalised`** ho jata hai."*

### Q3: QA Lead: *"Strategy Name user se input kyu nahi le rahe?"*
👉 **Kareem's Answer:** *"Comment #7 ke mutabiq name system auto-generate karta hai (`{Category}_{Market}_{Goal}_{MonthYear}`). Agar same name pehle se exist karta hai, to system check_strategy_name_uniqueness API se verify karke auto `_v2` append kar deta hai."*

### Q4: Architect: *"3P Publishers (Netflix/Disney+) ke liye publisher approval kaise track ho raha hai?"*
👉 **Kareem's Answer:** *"Comment #26 ke mutabiq, static approval fields hatakar dynamic dictionary map `channel_approval_statuses: Dict[str, ApprovalStatusEnum]` apply kiya gaya hai, jo har channel (Amazon, Netflix, Disney+, Paramount+) ka approval status separately track karta hai."*

### Q5: Backend Lead: *"Audience Data Fees compounding kaise hoti hai?"*
👉 **Kareem's Answer:** *"Comment #2 ke mutabiq, same provider (e.g. Amazon 1P) ke 5 segments lene par bhi 1 hi fixed CPM fee lagti hai (£2.00 VCPM). Compounding tabhi hoti hai jab 2 alag-alag providers (e.g. Amazon 1P + Experian 3P) use kiye jayein."*

---

## 📄 Related Master Documents in Workspace
- 📄 **Full Strategy Schema Mastery:** [full_strategy_schema_registery_mastery.md](file:///e:/VOW%20Agent/vow%20docs/full_strategy_schema_registery_mastery.md)
- 📄 **David Comments Final Breakdown:** [david_comments_explained_final.md](file:///e:/VOW%20Agent/vow%20docs/david_comments_explained_final.md)
- 📄 **Implementation Pre-Requisites:** [implementation_pre_requisites_hinglish.md](file:///e:/VOW%20Agent/vow%20docs/implementation_pre_requisites_hinglish.md)
- 📄 **Codebase Architecture & Setup Guide:** [vow_agent_architecture_and_setup_guide_hinglish.md](file:///e:/VOW%20Agent/vow%20docs/vow_agent_architecture_and_setup_guide_hinglish.md)
