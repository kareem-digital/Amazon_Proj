# VOW Platform — Strategy Schema v2.0 Complete Beginner-to-Master Deep Guide (Hinglish Version)

**Document Name:** `vow_strategy_schema_v2_deep_explanation_hinglish.md`  
**Target Audience:** Kareem (Planning Agent Lead Developer) & Whole VOW Engineering Team.  
**Purpose:** Strategy Schema (v2.0) Confluence Document ka **ek-ek section, har ek field, aur har ek technical word** ko zero-level se samjhnaye wala master guide. Isme koi complex noise nahi hai — sirf real-life daily examples, deep logic, aur step-by-step masterclass hai.

---

## 📌 PART 1: Core Fundamentals & Real-World Concept

### 1.1 Advertising Strategy Kya Hoti Hai? (Real-Life Example)
Maano ek **Online Education Platform** (jaise Unacademy ya Coursera) ka owner aapke paas aata hai aur bolta hai:  
> *"Mujhe UK (United Kingdom) me logon ke Smart TV par apne naye Data Science Course ke ad dikhane hain. Mera budget £10,000 hai aur campaign August 2026 me chalega."*

Is poore plan ko Digital Advertising ki bhasha me **"Campaign Strategy"** bolte hain.

### 1.2 Schema aur Registry Kya Hota Hai?
- **Schema (Blueprint / Rulebook):** Data ko kis format me store karna hai uski rules list. Jaise College Admission Form me `Name`, `DOB`, `Marks` fix slots hote hain, waise hi VOW Platform me Strategy ka ek fixed **Pydantic Schema** hota hai.
- **Registry (Central Store):** Platform ke paas pehle se available Deals, Audience Lists, aur Currencies ka central data repository.

### 1.3 Planning Agent Ka Asli Kaam Kya Hai? (Kareem's Task)
Legacy system me advertiser ko 15+ complex forms manually bharne padte the. Naye system me aapka **Planning Agent** ek aisa **Smart Assistant** hai jo chat ke zariye user se baat karke:
- User se sirf **3 Core Inputs** poochhta hai: **Flight Dates, Target Market, Budget**.
- Baaki saari cheezein (Name, Currency, Format, Category, Base Bid) **apne aap (Auto-Infer)** kar leta hai.

---

## 🧭 PART 2: Step-by-Step Section-by-Section Deep Masterclass

---

### 🟢 STEP 2: SECTION 1 — Strategy Details Setup (Step 1 of Schema)

Pehle hum Section 1 ke **saare Technical Words** ko samjhenge, uske baad pure section ki working dekhenge:

#### 📖 Technical Terms Explained First:
1. **Flight Dates (Campaign Duration):** Campaign start hone ki date aur end hone ki date (e.g., `01/08/2026` to `31/08/2026`).
2. **ISO Country Code:** International 2-letter country code. UK ke liye **`GB`**, Germany ke liye **`DE`**, USA ke liye **`US`**.
3. **Automated Currency Inference:** Target market country ke basis par currency khud chunna. Agar market `GB` hai to currency automatic **`GBP` (£)** set hogi.
4. **Ad Format (Ad Ka Type):**
   - **`streaming_tv`:** Smart TV (Connected TV) par aane wale 15-30 second ke video ads.
   - **`display`:** Websites par dikhne wale image banner ads.
   - **`online_video` (OLV):** Websites ya YouTube par chalne wale video ads.
5. **Product Category:** Product kis industry ka hai (e.g. Education, Automotive, Electronics).
6. **ASIN (Amazon Standard Identification Number):** Amazon par bikne wale har product ka unique 10-character code (Jaise human ka Aadhaar Card number).
7. **Product Location:** Product kahan bikta hai? `ON_AMAZON` (Amazon store par) ya `NOT_SOLD_ON_AMAZON` (apni website/app par).

---

#### ⚙️ Section 1 Ki Working & Logic:

```
[User Chat Brief] ──► [Dates, Market, Budget Inputs] ──► [Agent Auto-Infers Name, Currency, Format, Category]
```

##### 1. Strategy Name Ka Auto-Generation & Auto-Repair Logic:
- User se Strategy ka naam nahi poochna hai. System khud Name generate karega:
  $$\text{Strategy Name} = \text{Category}_{\text{MarketISO}}_{\text{Goal}}_{\text{MonthYear}}$$
  - *Example:* Education category, UK market (`GB`), Awareness goal, August 2026 $\rightarrow$ **`Education_UK_Awareness_Aug2026`**.
- **Auto-Repair (`_v2`):** Agent API hit karke check karega ki kya ye naam pehle se database me hai? Agar name pehle se exist karta hai, to system bina user ko pareshaan kiye auto-repair karega: **`Education_UK_Awareness_Aug2026_v2`**.

##### 2. Deferred Fields (Post-Creation `PATCH` Rule):
- **Boht Important Rule:** `product_location` aur `product_asins` initial strategy creation ko **STUCK / BLOCK nahi karte**.
- Agar kisi brand ke paas initial chat ke waqt ASINs nahi hain, to bhi strategy create ho jayegi. ASINs baad me **`PATCH /api/strategies/{id}/`** API endpoint se attach kiye ja sakte hain.

---

### 🔵 STEP 3: SECTION 2 — Goal, KPI & Budget Allocation (Step 2 of Schema)

#### 📖 Technical Terms Explained First:
1. **Strategy Goal (Campaign Ka Maqsad):**
   - **`AWARENESS`:** Max-to-max naye logon ko brand dikhana (Smart TV ads ke liye sabse main goal).
   - **`CONSIDERATION`:** Logon ko product me interest dilana (clicks / detail page views).
   - **`CONVERSION`:** Direct sale ya form fill-up karwana.
2. **KPI (Key Performance Indicator / Measure):** Success naapne ka tareeqa:
   - **`reach`:** Kitne alag-alag (unique) logon ne ad dekha.
   - **`frequency`:** Ek aadmi ne avg kitni baar ad dekha.
3. **Frequency Capping:** Ek customer ko 24 ghante me max 2-3 baar se zyada ad na dikhana taaki wo irritates na ho.
4. **Base CPM Bid:** 1,000 ad impressions ke liye advertiser max kitna paisa dene ko tayyar hai.
5. **Single Numeric Budget:** Single country campaign ke liye ek single numeric budget amount (e.g. `10000.00`).

---

#### ⚙️ Section 2 Ki Working & Logic:

1. **CTV Defaults:** Connected TV strategies ke liye Goal default **`AWARENESS`** aur KPI default **`reach`** hota hai.
2. **Frequency Range Limitation:** Agar user frequency KPI choose karta hai, to value range **`1 to 5`** ke beech hi allowed hai (e.g. frequency target = 3).
3. **Frequency Capping Inheritance:** User se complex frequency rules nahi lene hain. Advertiser Profile me set default capping automatically apply hogi.
4. **Base CPM Bid Omission for CTV:** Smart TV (CTV) inventory fixed rate card / floor rate deals par chalti hai. Isliye user se manual Base Bid nahi manga jata; bid rate selected deal se derive hota hai.
5. **Tracked Conversion Pixels:** Conversion tracking pixels (e.g., `APPLICATION`, `PAGE_VIEW`) deferred hote hain aur creation ke baad `PATCH` API se add hote hain.

---

### 🟣 STEP 4: SECTION 3 — Inventory Deals & CPM Pricing (Step 3 of Schema)

#### 📖 Technical Terms Explained First:
1. **Inventory (Ad Slots):** TV Channels ya Streaming Apps par ad dikhane ki jagah (e.g., Prime Video, Netflix, Paramount+, Hulu, Disney+).
2. **Rate Card CPM / Floor Rate:** Publisher (Jaise Prime Video ya Netflix) ka fixed rate price per 1,000 views (e.g., £25.00 CPM).
3. **CPM Pricing Abstraction:** User ko complex technical Deal IDs (`EXT7P75718S8MNR`) na dikha kar seedha clean Publisher Name (Paramount+) aur Price (£25.33) dikhana.
4. **Inventory Tier:**
   - **`AMAZON_OWNED`:** Amazon ke apne properties (Prime Video, Freevee).
   - **`THREE_P_PRE_CURATED`:** Premium 3rd party partners (Netflix, Disney+).
   - **`THREE_P_NEEDS_CURATION`:** Open web supply needing review.

---

#### ⚙️ Section 3 Ki Working & Logic:

##### 1. Background Deal Matching:
User jab market (`GB`) aur format (`streaming_tv`) batata hai, to Planning Agent background me VOW API **`GET /api/deals/?markets=GB`** call karta hai aur best matching deals khud pick karta hai.

##### 2. Blended Effective CPM Formula:
$$\text{Blended Effective CPM} = \text{Base Deal CPM} + \text{Stacked Audience Data Fees}$$
- *Example:* Paramount+ Deal CPM (£25.33) + Amazon 1P Data Fee (£2.00) = **£27.33 Effective CPM**.

---

### 🟠 STEP 5: SECTION 4 — Unified Baseline Targeting Architecture (Step 4 of Schema)

#### 📖 Technical Terms Explained First:
1. **Default Baseline Targeting:** Strategic baseline jo har CTV strategy me automatically lag jata hai bina user ke mange:
   - **Country Geo:** Target Market Country (`GB` = UK).
   - **Device Environment:** Living Room Connected TV Devices (`CTV` Smart TV / Fire TV).
2. **1P Data (First-Party Data):** Amazon ka apna actual shopping data (e.g., Amazon par Education books/courses dhoondhne wale log).
3. **3P Data (Third-Party Data):** External data companies ka data (e.g. Experian income data).
4. **VCPM Data Fee:** Extra data charge per 1,000 views (e.g. £2.00 VCPM).

---

#### ⚙️ Section 4 Ki Working & Logic:

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

##### Audience Data Fee Rules & Naming:
1. **Vocabulary:** Client Vocabulary me Profile Name **"Wide"** bolenge (Broad nahi).
2. **Single Fixed Fee per Provider:** Amazon 1P data ke 10 segments bhi chunenge to fee **1 hi baar** lagegi (£2.00 VCPM - same provider me compounding nahi hoti).
3. **Cross-Provider Stacking:** Agar Amazon 1P (£2.00) + Experian 3P (£1.50) dono chunenge to dono fees stack hongi (£3.50 VCPM total data fee).
4. **Flat List Shape:** Audience suggest API (`POST /api/audience-sets/suggest/`) ka output response shape **Flat List** (`List[AudienceSet]`) hota hai using prompt parameter.

---

### 🔴 STEP 6: SECTION 5 & 6 — Creatives Binding & Direct Strategy Publication

#### 📖 Technical Terms Explained First:
1. **Media Asset:** Video ad file (.mp4 15s/30s) jo Smart TV par chalegi.
2. **Click-Through URL:** Landing page website link. (Smart TV ads ke liye URL **OPTIONAL** hota hai kyunki TV screen par log click nahi karte!).
3. **Channel Approvals Map:** Publisher partners (Amazon, Netflix, Disney+, Paramount+) se creative video file ki approval report.
4. **`POST /api/simple-strategies/`:** Strategy publish karne ka primary creation API endpoint.
5. **`PATCH /api/strategies/{id}/`:** Existing strategy par specific fields update karne ka endpoint.

---

#### ⚙️ Section 5 & 6 Ki Working & Logic:

##### 1. Dynamic Per-Channel Approval Map:
Static fields ki jagah dynamic dictionary map banaya gaya hai:
$$\text{channel\_approval\_statuses}: \text{Dict[str, ApprovalStatusEnum]}$$
- *Example:* `{'amazon': 'APPROVED', 'netflix': 'PENDING', 'disney_plus': 'APPROVED', 'paramount_plus': 'PENDING'}`

##### 2. Direct Publication (`draft` $\rightarrow$ `finalised`):
Manager approval loops hataye gaye hain. User jab chat proposal approve karta hai, to system seedha **`POST /api/simple-strategies/`** execute karta hai aur strategy status direct **`finalised`** ho jata hai.

##### 3. Non-Sequential Downstream Setup:
Strategy finalize hone ke baad 2 downstream modules hote hain:
- **Module A (Creatives Binding & Approvals)**
- **Module B (Tracking Setup & Conversion Pixels)**
Dono modules decoupled hain aur kisi bhi order me **`PATCH /api/strategies/{id}/`** API call karke update kiye ja sakte hain.

---

## 💻 PART 3: Codebase Pydantic Models Quick Reference (`schemas.py`)

```python
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class Step1DetailsSlotSchema(BaseModel):
    name: Optional[str] = Field(None, description="Auto-generated e.g. Education_UK_Awareness_Aug2026")
    flight_dates: Dict[str, str] = Field(..., description="{'lower': '2026-08-01', 'upper': '2026-08-31'}")
    markets: List[str] = Field(default=["GB"])
    primary_currency: Optional[str] = Field(None, description="Inferred GB -> GBP")
    formats: List[str] = Field(default=["streaming_tv"])
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
    channel_approval_statuses: Dict[str, str] = Field(default_factory=dict)

class FullStrategySchema(BaseModel):
    id: Optional[str] = None
    advertiser_id: str
    details: Step1DetailsSlotSchema
    goal_kpi_bid: Step2GoalKPIBidSlotSchema
    deals: List[SelectedDealSchema]
    targeting: UnifiedTargetingSlotSchema
    creatives: List[SelectedCreativeSchema]
    status: str = "finalised"
```

---

## 🎯 PART 4: Summary Checklist for Kareem

- [x] Basic Advertising Concepts samajh aa gaye hain (Strategy, Campaign, CPM, CTV).
- [x] Agent Inputs (Dates, Market, Budget) vs Agent Inferences (Name, Currency, Format, Category) clear hain.
- [x] Name auto-generation (`{Category}_{Market}_{Goal}_{MonthYear}`) aur `_v2` auto-repair clear hai.
- [x] Deferred fields (`product_location`, `product_asins`, tracking pixels) aur `PATCH` API mechanism clear hai.
- [x] Baseline Targeting (`Country Geo` + `CTV Devices`) aur Data Fee Stacking rules clear hain.
- [x] Dynamic Channel Approval Map (`channel_approval_statuses`) aur Direct Publication (`draft` $\rightarrow$ `finalised`) clear hain.
