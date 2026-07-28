# VOW Platform - Strategy Schema Registry (Hinglish Version & Team Guide)

**Document Name:** `update_schema_registery_hinglish.md`  
**Purpose:** Team Guide in Hinglish explaining all 28 comments & architectural updates provided during the Strategy Module review.  
**Target Audience:** Non-native English team members, QA Engineers, Backend/Frontend Developers, Product Owners.  

---

## 📌 Introduction (Yeh Document Kis Liye Hai?)

Is document me humne David Moss aur client review ke **saare 28 comments** ko simple **Hinglish** (Hindi + English) me detail ke sath explain kiya hai. 

Har comment ke baare me 4 baatein batayi gayi hain:
1. **Comment Number & Topic Name** (Kis feature ya section ki baat ho rahi hai)
2. **Document Location / Field Name** (David ne document me kahan par comment kiya tha)
3. **David Ka Comment Kya Tha?** (Review screenshot me kya feedback mila tha)
4. **Final System Update & Client Requirement** (Client ke kehne par system me kya badlaav/rules lagaye gaye hain)

Is document ko padhkar aapki team ka koi bhi member easily samajh jayega ki hamare VOW Advertising Platform me kya change hua hai aur AI Planning Agent kaise kaam karega!

---

## 📋 Detail Breakdown of All 28 Comments (Hinglish Explanation)

---

### 🔹 Comment 1: 3P Inventory Targeting & Fees (Netflix, Hulu, Disney+)
- **Document Location / Field:** Section 2.5 (Inventory Tiers & 3P Targeting)
- **David Ka Comment Kya Tha:** 3P inventory (Netflix, Disney+, Hulu) me publisher-side targeting ke alawa Amazon DSP targeting kaise kaam karti hai aur extra fees lagti hai ya nahi?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - 3P inventory par advertisers ke paas 2 options hain: **Amazon DSP Targeting** (device/geo) ya **Publisher / SSP Supply-Side Targeting** (deal-specific).
  - Supply-side targeting karne se koi automatic extra CPM fee nahi lagti. Fee sirf tabhi lagti hai jab aap extra Audience Data (like Amazon 1P segments) use karte hain.

---

### 🔹 Comment 2: Audience Data Fees & Profile Naming ("Broad" $\rightarrow$ "Wide")
- **Document Location / Field:** Section 2.4 (Audience Profiles & Fee Structure)
- **David Ka Comment Kya Tha:** Profile name "Broad" ko badlo, aur data fees per segment multiply nahi hoti.
- **Kya Badlaav Hua Hai (Client Requirement):**
  - **Naming Change:** "Broad" profile ka naam badal kar **"Wide"** kar diya gaya hai.
  - **Data Fee Rules:** Audience data fee profile ki narrowness ya segment count par depend nahi karti. Single data provider (jaise Amazon 1P Lifestyle/Interest) use karne par **1 fixed CPM data fee** lagti hai (saare 1P segments par ek hi fee).
  - **Stacking Rule:** Data fees tabhi judti (stack hoti) hain jab alag-alag providers mix hon (jaise Amazon 1P + Experian 3P).
  - **Formula:** $\text{Effective CPM} = \text{Base Deal CPM} + \text{Stacked VCPM Data Fees}$.

---

### 🔹 Comment 3: Budget Split Step Optionality
- **Document Location / Field:** Section 2.6 (CTV-First Agentic Flow & Budget Split)
- **David Ka Comment Kya Tha:** Budget split step conversation me compulsory hai ya optional?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Conversation me Budget Split step **OPTIONAL** hai (AI Agent user ko manually deal budget split karne ke liye force nahi karega).
  - Lekin alag-alag deals (jaise Prime Video PG £28.88 aur Netflix £22.00) ke liye **Blended Effective CPM** accurately calculate karne ke liye budget split **PREFERRED** hai.

---

### 🔹 Comment 4: Audience Selection Requirement (Optional Again)
- **Document Location / Field:** Section 2.6 & Section 3.4 (Audience Selection)
- **David Ka Comment Kya Tha:** Strategy create karne ke liye audience select karna zaroori hai kya?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Audience targeting **compulsory nahi hai**.
  - Connected TV (CTV) aur Prime Video campaigns bina kisi audience segment ke seedha **Run-of-Service (ROS) / Contextual Deal Targeting** par chal sakte hain.
  - Agar audience choose nahi ki, to VCPM data fee **£0.00 (Zero)** rahegi.

---

### 🔹 Comment 5: Unified Targeting & Default Baseline Architecture
- **Document Location / Field:** Section 2.7 (Unified Targeting & Baseline Defaults)
- **David Ka Comment Kya Tha:** Audiences ko alag step rakhne ke bajaye overall targeting me kaise combine karein?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Audiences ko isolated step ke bajaye **Unified Targeting** ka hissā banaya gaya hai.
  - CTV Inventory select hote hi system **Default Baseline Targeting** automatically apply kar deta hai:
    1. **Country Geo-Targeting:** ISO Market Country (e.g. `GB` -> United Kingdom)
    2. **Device Environment:** Connected TV (CTV) / Living Room Devices
  - Optional Refinement ke liye user Audience Segments ya Postcodes (e.g. `SW1A 1AA`) add kar sakta hai.

---

### 🔹 Comment 6: CTV Strategy Simplification (Eliminating 15+ Form Fields)
- **Document Location / Field:** Section 2.8 (CTV Strategy Simplification)
- **David Ka Comment Kya Tha:** CTV strategies ke liye itne saare form questions (15+ fields) user se poochne ki zaroorat nahi hai.
- **Kya Badlaav Hua Hai (Client Requirement):**
  - CTV strategies ke liye saare redundant form questions khatam kar diye gaye hain.
  - AI Agent user se sirf **3-4 simple core parameters** poochhega: **Strategy Name, Flight Dates, Target Market, Total Budget**.
  - Baaki saare parameters internally default ho jayenge (Goal $\rightarrow$ `AWARENESS`, KPI $\rightarrow$ `reach`, Format $\rightarrow$ `streaming_tv`, Base Bid $\rightarrow$ deal rate card CPM).

---

### 🔹 Comment 7: Auto-Generated Strategy Naming Architecture
- **Document Location / Field:** Section 3.1 (Auto-Generated Strategy Naming)
- **David Ka Comment Kya Tha:** Strategy Name user se prompt karke poochne ki zaroorat nahi hai.
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Strategy Name input user ke liye blocking prompt nahi hai.
  - AI Agent brief context padhkar automatically name generate karega: `{Category}_{Market}_{Goal}_{MonthYear}` (e.g. `Education_UK_Awareness_Aug2026`).
  - Agar backend check me duplicate name milta hai, to agent bina user ko distrub kiye auto-repair karke `_v2` suffix laga dega.

---

### 🔹 Comment 8: Multi-Market Execution & Repeat-Prevention
- **Document Location / Field:** Section 2.9 (Multi-Market Agentic Architecture)
- **David Ka Comment Kya Tha:** Jab campaign me multiple markets (countries) hon, to kya agent har country ke liye alag-alag sawal repeat karega?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Agent conversation me **kabhi bhi country-by-country repetitive prompt loops nahi chalayega**.
  - **Mode 1 (Single Market Primary):** Primary market ke liye 1 Strategy Card banega; doosri country me expand karne ke liye 1-Click "Duplicate Strategy for DE" button milega.
  - **Mode 2 (Parallel Aggregation):** Agar user start me hi multiple markets bole (`markets=GB,DE`), to agent tool calls parallel me run karke budget ko countries me equally split kar dega.

---

### 🔹 Comment 9: Automated Currency Inference from Market Code
- **Document Location / Field:** Section 3.1 (Automated Currency Inference)
- **David Ka Comment Kya Tha:** User se primary currency dropdown me select karwane ki zaroorat nahi hai.
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Currency prompt completely remove kar diya gaya hai.
  - Primary currency Target Market ISO Code se automatic derive ho jayegi:
    - `GB` $\rightarrow$ **GBP (£)**
    - `DE` / `FR` / `ES` / `IT` $\rightarrow$ **EUR (€)**
    - `US` $\rightarrow$ **USD ($)**

---

### 🔹 Comment 10: Frequency KPI Target Value Range (1–5)
- **Document Location / Field:** Section 3.2 (Frequency KPI Target Value Range)
- **David Ka Comment Kya Tha:** Frequency KPI ke liye target value kya rakhi ja sakti hai?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Jab KPI target type `frequency` choose kiya jaye, to explicit numeric target value **`1` se `5`** impressions per user set ki ja sakti hai.
  - Default Frequency Target: **`3`** (standard CTV branding cap).

---

### 🔹 Comment 11: Single Market Budget Input Architecture
- **Document Location / Field:** Section 3.2 (Single Market Budget Input)
- **David Ka Comment Kya Tha:** Single market campaigns ke liye screen par multi-row table UI widget dikhane ki zaroorat nahi hai.
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Single-market campaign me budget enter karne ke liye multi-row table widget hata diya gaya hai.
  - User sirf ek **single numeric input** dega (e.g. `Total Budget: £10,000.00`). Multi-row table sirf tabhi dikhega jab multi-market aggregated mode active ho.

---

### 🔹 Comment 12: Base CPM Bid Omission for CTV Strategies
- **Document Location / Field:** Section 3.2 (Base CPM Bid Omission)
- **David Ka Comment Kya Tha:** CTV campaigns me manual base bid enter karwane ki zaroorat hai kya?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - CTV / Prime Video strategies ke liye **Base Bid input omit kar diya gaya hai**.
  - Pricing poori tarah se selected inventory deals ke fixed rate-card CPM se tay hoti hai (e.g. Prime Video PG @ £28.88). Agent manual base bid nahi poochhega.

---

### 🔹 Comment 13: Advertiser Default Frequency Cap Inheritance
- **Document Location / Field:** Section 3.2 (Advertiser Default Frequency Cap)
- **David Ka Comment Kya Tha:** Agar user frequency cap input na de to kya hoga?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Frequency cap user prompt me optional hai.
  - Agar user ignore kar de, to system automatically **Advertiser Profile Default Capping Settings** (e.g. 3 impressions per 24 hours) pull karke apply kar dega.

---

### 🔹 Comment 14: Automated Format Default (`streaming_tv`)
- **Document Location / Field:** Section 3.1 & 3.2 (Automated Format Default)
- **David Ka Comment Kya Tha:** Ad Formats select karne ka dropdown prompt hatana hai.
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Amazon DSP CTV strategies ke liye Ad Format hamesha **`streaming_tv`** (Connected TV format) par default rahega. Manual format dropdown prompt hataye gaye hain.

---

### 🔹 Comment 15: Product Category Brief Inference & Default
- **Document Location / Field:** Section 3.1 (Product Category Brief Inference)
- **David Ka Comment Kya Tha:** Product category select karna user ke liye blocking prompt nahi hona chahiye.
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Product Category prompt remove kar diya gaya hai.
  - Agent category ko brief text context se infer karega (e.g. "Degree program" $\rightarrow$ Education) ya advertiser profile default category apply kar dega.

---

### 🔹 Comment 16: Selling Location Omission for CTV Strategies
- **Document Location / Field:** Section 3.1 (Selling Location Omission)
- **David Ka Comment Kya Tha:** CTV branding campaigns me Selling Location (`ON_AMAZON` vs `NOT_SOLD_ON_AMAZON`) poochhna zaroori hai kya?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Upper-funnel CTV branding campaigns ke liye selling location prompt omit kar diya gaya hai.
  - Internal backend state me ye default `NOT_SOLD_ON_AMAZON` ya null rahega.

---

### 🔹 Comment 17: Deferred ASIN Collection Architecture ("Comes Later")
- **Document Location / Field:** Section 3.1 (Deferred ASIN Collection)
- **David Ka Comment Kya Tha:** ASINs initial strategy creation ke wqt mangna compulsory hai kya?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Initial setup aur brief parsing ke wqt ASINs enter karna compulsory nahi hai (**"Comes Later"** rule).
  - ASIN collection aur validation campaign finalise hone ke baad downstream tracking setup phase me handle hoga.

---

### 🔹 Comment 18: Automated Deal Selection & CPM Pricing Abstraction
- **Document Location / Field:** Section 2.5 & Section 3.3 (Automated Deal Selection)
- **David Ka Comment Kya Tha:** Technical deals checkbox table UI se hatao aur pricing dikhao.
- **Kya Badlaav Hua Hai (Client Requirement):**
  - **Checkbox Table Removed:** UI se technical deal tables aur checkboxes hata diye gaye hain.
  - **Background Match:** Agent brief parameters (`market`, `duration`, `channel=streaming_tv`, `genre`) ke basis par optimal deals backend me auto-match karega.
  - **CPM Abstraction:** Technical Deal IDs user se chhupa di gayi hain. Screen par sirf final **Effective Rate Card CPM** (e.g. £28.88) dikhega.

---

### 🔹 Comment 19: Amazon Audience Applicability to 3P Inventory
- **Document Location / Field:** Section 2.4, 2.5 & Section 3.4 (Amazon Audience Applicability)
- **David Ka Comment Kya Tha:** Kya Amazon native 1P audiences 3P inventory deals (Netflix, Disney+, Hulu) par lag sakti hain?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Yes! Advertisers Amazon DSP ke zariye 3P inventory deals (Netflix, Disney+, Hulu, Roku) par **Amazon 1P native audiences** (In-Market, Lifestyle, Demographic) apply kar sakte hain. Standard 1P VCPM data fee lagi rahegi.

---

### 🔹 Comment 20: Audience Suggestion API Flat List Response Shape
- **Document Location / Field:** Section 2.4, Section 3.4 & Section 4.1 (Audience API Shape)
- **David Ka Comment Kya Tha:** Kya Audience Suggest API `POST /api/audience-sets/suggest/` nested bundles (`bundles.narrow/balanced/broad`) bhejta hai?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Backend API abhi nested bundle objects support nahi karta.
  - Endpoint `POST /api/audience-sets/suggest/` recommended audience sets ki **FLAT LIST** (`List[AudienceSet]`) return karta hai. Agent in audience sets ko directly flat list me present karega.

---

### 🔹 Comment 21: Location Geo-Targeting Market Country Default
- **Document Location / Field:** Section 2.7 & Section 3.4 (Location Geo-Targeting Default)
- **David Ka Comment Kya Tha:** Geo-targeting prompt optional hone par default location kya hogi?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Geo-targeting prompt optional hai.
  - Agar sub-regions / postcodes nahi diye gaye, to location targeting automatically poori **Target Market Country** (e.g. `GB` $\rightarrow$ United Kingdom) par default ho jayegi.

---

### 🔹 Comment 22: Device Type Advertiser Level Setting & Inheritance
- **Document Location / Field:** Section 2.7 & Section 3.4 (Device Type Inheritance)
- **David Ka Comment Kya Tha:** Device type targeting select nahi kiye jaane par kya apply hoga?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Device type targeting optional hai.
  - Agar user skip karta hai, to system **Advertiser Profile Preference** (e.g. `CTV only` / Living Room Devices) ko auto-inherit kar lega.

---

### 🔹 Comment 23: Simplified Plan Approval & Direct Status Transition
- **Document Location / Field:** Section 2.6, Section 3.6 & Section 6.0 (Plan Approval)
- **David Ka Comment Kya Tha:** Strategy plan finalise karne ke liye Manager Approval workflow zaroori hai kya?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Manager approval routing workflow hata diya gaya hai.
  - Strategy plan approval ko ek simple **Status Update** (`draft` $\rightarrow$ `finalised` / `active`) me convert kar diya gaya hai.

---

### 🔹 Comment 24: Simplified Strategy Creation Endpoint (`POST /api/simple-strategies/`)
- **Document Location / Field:** Section 3.6, Section 4.1 & Section 6.0 (Creation Endpoint)
- **David Ka Comment Kya Tha:** CTV strategies create karne ke liye kon sa API endpoint use hoga?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Simplified CTV strategies create karne ke liye dedicated REST endpoint **`POST /api/simple-strategies/`** use hota hai.
  - Ye endpoint lean Pydantic payload accept karta hai jisme redundant multi-channel form fields nahi hote.

---

### 🔹 Comment 25: Click-Through URL Optionality for Streaming TV
- **Document Location / Field:** Section 2.8 & Section 3.5 (Click-Through URL Optionality)
- **David Ka Comment Kya Tha:** Streaming TV / CTV assets ke liye Click-Through URL enter karna compulsory hai kya?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Connected TV (`streaming_tv`) living room ads non-clickable branding experiences hote hain, isliye Click-Through landing page URL **OPTIONAL** hai. Required sirf Display/OLV ke liye hai.

---

### 🔹 Comment 26: Dynamic Channel-Level Creative Approval Status Architecture
- **Document Location / Field:** Section 3.5 & Section 5.0 (Creative Approval Status)
- **David Ka Comment Kya Tha:** Creative approval status me Amazon/Netflix/Disney approval status ko hardcode karne ke bajaye kya design hona chahiye?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Hardcoded publisher status fields ko hata kar dynamic per-channel approval dictionary map banaya gaya hai:
    `channel_approval_statuses: Dict[str, ApprovalStatusEnum]`
  - Example: `{"amazon": "APPROVED", "paramount_plus": "PENDING", "channel_4": "APPROVED"}`. Ye kisi bhi naye channel partner par easily scale hota hai.

---

### 27: Flexible Non-Sequential Downstream Execution Architecture
- **Document Location / Field:** Section 2.6, Section 2.8 & Section 6.0 (Downstream Execution Order)
- **David Ka Comment Kya Tha:** Tracking setup (ASINs/pixels) aur Creatives binding ke beech execution order kya hona chahiye?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Downstream post-finalization modules (**Tracking Setup** vs **Creatives Binding**) ke beech koi rigid sequence nahi hai.
  - Agar video creatives abhi production me hain, to advertiser pehle Tracking Setup (ASINs / Conversion pixels) kar sakta hai, ya iska opposite bhi kar sakta hai.

---

### 🔹 Comment 28: Post-Creation Strategy Field Updates Architecture
- **Document Location / Field:** Section 2.1, Section 2.8 & Section 4.1 (Post-Creation Field Updates)
- **David Ka Comment Kya Tha:** Kya `product_location` aur `product_asins` strategy banne se pehle mangna zaroori hai?
- **Kya Badlaav Hua Hai (Client Requirement):**
  - Nahi! Open question resolve ho gaya hai.
  - Strategy ko pehle create aur publish kiya ja sakta hai (status `finalised` via `POST /api/simple-strategies/`), aur `product_location`, `product_asins` ya tracking details strategy banne ke baad **`PATCH /api/strategies/{id}/`** call karke update kiye ja sakte hain.

---

## 🎯 Quick Summary Table (Team Reference)

| # | System Area | Kya Prompts Hataye Gaye? | System Me Ab Kya Rules Hain? |
| :-: | :--- | :--- | :--- |
| **1-5** | Targeting & Fees | Extra fee assumptions & Isolated steps | Amazon 1P fee 1 fixed CPM par rahegi; baseline targeting (`Country` + `CTV`) auto-apply hoga. |
| **6-9** | Identity & Inferences | Name, Currency, Formats & Category prompts | AI Agent context se Name generate karega, Market code se Currency & Category infer karega. |
| **10-13** | Budget & Bidding | Multi-row table & Manual base bid prompts | Single numeric budget input (`£10k`); Base bid deal CPM se derive hogi; Frequency cap profile se inherit hogi. |
| **14-18** | Deals & Inventory | Technical Deal Checkbox Tables | Agent backend me deals match karega; screen par sirf final **Effective Rate Card CPM** dikhega. |
| **19-22** | Audience & Devices | Complex device & geo prompts | Amazon 1P data 3P deals par chalega; Geo country par default hoga; Audience suggest flat list aayegi. |
| **23-28** | API & Downstream | Manager approval & Strict step order | Status seedha `finalised` hoga; `POST /api/simple-strategies/` endpoint use hoga; Downstream steps flexible rahenge; Fields `PATCH` se update honge. |

---

## 📄 Related Specification Files
- 📄 **Main Technical Specification Document (v2.0):** [update_strategy_schema_registry.md](file:///e:/VOW%20Agent/update_strategy_schema_registry.md)
- 📄 **Official Audit & Architecture Change Registry:** [updated_schema_registry.md](file:///e:/VOW%20Agent/updated_schema_registry.md)
