# VOW Platform - Strategy Module Explained & Field-by-Field Reference Guide

**Document Version:** 1.2.0 (Updated with Data Fee & Profile Naming Rules)  
**Target Audience:** Product Managers, AI Engineers, Backend Engineers, Frontend Developers, QA Testers  
**Purpose:** Comprehensive business & functional explanation of the VOW Strategy Module and all fields across the 6 wizard steps.

---

## 1. What is the Strategy Module?

### 1.1 High-Level Overview
In the VOW Advertising Platform, a **Strategy** is the top-level blueprint for executing digital ad campaigns across **Amazon DSP** (Demand-Side Platform) and **Prime Video**. 

Instead of forcing advertisers to manually log into Amazon DSP and configure hundreds of complex settings (line items, ad groups, bid strategies, audience targeting rules, inventory deals, and creative tags), the **VOW Strategy Module** simplifies campaign creation into a streamlined, automated 6-step workflow.

```
+---------------------------------------------------------------------------------------------------+
|                                      VOW STRATEGY MODULE                                          |
|                                                                                                   |
|  [Step 1: Strategy Details]  -> Basic Setup (Name, Dates, Markets, Currency, Selling Location)     |
|  [Step 2: Goal, KPI & Bid]   -> Campaign Objective (Awareness/Conversion), Budget & Max CPM Bids  |
|  [Step 3: Deals]             -> Premium Inventory Deals (Prime Video, Preferred Deals, Auctions) |
|  [Step 4: Audiences]         -> Amazon In-Market, Demographics & Behavioral Target Bundles         |
|  [Step 5: Creatives]         -> Video/Display Media Assets & Landing Page Click-Through URLs      |
|  [Step 6: Summary]           -> Automated Reach Forecasting & Background Amazon DSP Sync         |
+---------------------------------------------------------------------------------------------------+
```

### 1.2 Role of the Planning Agent in the Strategy Module
The **Planning Agent** is an AI conversational assistant powered by **LangGraph**. Its job is to interact with users (via text chat or uploaded brief documents) and automatically fill in all required fields of the Strategy Module. 

Once all fields are filled and verified against official VOW APIs, the Planning Agent presents a complete Strategy Card that the user can execute with a single click.

---

## 2. Comprehensive Field-by-Field Breakdown (All 6 Steps)

---

### Step 1: Strategy Details (`step=0`)

Step 1 collects the fundamental identity, scheduling, geographical targeting, and product attribution parameters of the ad campaign.

```
+---------------------------------------------------------------------------------------------------+
|  Step 1: Strategy Details                                                                        |
+---------------------------------------------------------------------------------------------------+
|  1. Strategy name               : [ Summer_Brand_Awareness_2026                             ] |
|  2. Flight dates                : [ 01/08/2026 - 31/08/2026                                 ] |
|  3. Target markets              : [ United Kingdom (GB)                                     ] |
|  4. Primary currency            : [ £ - GBP                                                 ] |
|  5. Formats                     : [ Prime Video                                             ] |
|  6. Product Categories          : [ Education (1)                                           ] |
|  7. Where do you sell products? : ( ) On Amazon  (x) Off Amazon                                   |
|  8. Type or paste product ASINs : [ B08N5WRWNW                                            ] |
+---------------------------------------------------------------------------------------------------+
```

#### Detailed Field Explanations:

1. **Strategy Name**
   - **What it is**: A unique textual title assigned to the strategy (e.g., `Summer_Brand_Awareness_2026`).
   - **Why it is used**: Uniquely identifies this campaign strategy across the advertiser’s account and correlates all reporting metrics.
   - **Business Purpose**: Prevents duplicate strategy names. Validated via `GET /api/strategies/check_strategy_name_uniqueness/`.

2. **Flight Dates**
   - **What it is**: The scheduled start date (`lower`) and end date (`upper`) during which ads will run.
   - **Why it is used**: Controls the active operational period of the campaign in Amazon DSP.
   - **Business Purpose**: Ensures ads only spend budget within the specified timeframe. Start date cannot be in the past.

3. **Target Markets**
   - **What it is**: The target countries where ads will be served, represented as ISO 2-letter codes (e.g., `GB` for United Kingdom, `US` for United States).
   - **Why it is used**: Restricts ad delivery to users residing within those specific geographical countries.
   - **Business Purpose**: Automatically filters available media assets, audience segments, and inventory deals for that specific country.

4. **Primary Currency**
   - **What it is**: The official currency used for financial reporting (e.g., `GBP - £`, `EUR - €`, `USD - $`).
   - **Why it is used**: Standardizes financial metrics across multi-country campaigns.
   - **Business Purpose**: All budget amounts, CPM bids, and spend reporting will be displayed in this currency.

5. **Formats & Product Categories (Ad Formats)**
   - **What it is**: Selection of ad placements and inventory channels (`Display`, `Online Video`, `Streaming TV`, `Prime Video`).
   - **Why it is used**: Tells the DSP what types of creative assets (images vs videos) and placements will be needed.
   - **Business Purpose**: Selecting `Prime Video` or `Streaming TV` opens premium video inventory deals in Step 3.

6. **Product Categories**
   - **What it is**: Industry/vertical classification of the advertised product (e.g., `Education (1)`, `Electronics`, `Beauty`).
   - **Why it is used**: Contextual targeting requirement for video and Prime Video publisher deals.
   - **Business Purpose**: Matches ad campaigns with contextually relevant video content (e.g., placing education ads in educational programming).

7. **Where do you sell products? (Product Location)**
   - **What it is**: A binary choice between **On Amazon (`ON_AMAZON`)** [Endemic] and **Off Amazon (`NOT_SOLD_ON_AMAZON`)** [Non-Endemic].
   - **Why it is used**: Defines the conversion destination and measurement model of the campaign.
   - **Business Purpose**:
     - `ON_AMAZON`: Drives shoppers directly to Amazon product listing pages.
     - `NOT_SOLD_ON_AMAZON`: Drives traffic to external D2C websites, landing pages, or mobile apps.

8. **Type or paste product ASINs**
   - **What it is**: A text box to enter Amazon Standard Identification Numbers (ASINs, e.g., `B08N5WRWNW`).
   - **Why it is used**: Identifies the specific Amazon products associated with the campaign.
   - **Business Purpose**:
     - **If `ON_AMAZON` (Required)**: Tracks Detail Page Views (DPV), Add to Cart (ATC), direct purchases, and ROAS on Amazon.
     - **If `NOT_SOLD_ON_AMAZON` (Optional)**: Measures organic Amazon "halo sales" (tracking if users who saw off-Amazon ads later bought the brand's products on Amazon).

---

### Step 2: Goal, KPI & Bid (`step=1`)

Step 2 defines the marketing objective, primary success metric, tracking pixels, total budget, and maximum bidding prices.

```
+---------------------------------------------------------------------------------------------------+
|  Step 2: Goal, KPI & Bid                                                                          |
+---------------------------------------------------------------------------------------------------+
|  1. Goal Selection                     : [x] Awareness    [ ] Consideration    [ ] Conversion     |
|  2. KPI Target                         : [x] Reach        [ ] Frequency                           |
|  3. Ad Tag Conversions (Off-Amazon)    : [x] Page view    [x] Checkout    [x] Add to cart         |
|  4. Market Budget                      : Market: United Kingdom (GB) -> Budget: £10,000.00         |
|  5. Base Bid (CPM)                     : Market: United Kingdom (GB) -> Base Bid: £30.00          |
+---------------------------------------------------------------------------------------------------+
```

#### Detailed Field Explanations:

1. **What goal would you like to achieve? (Strategy Goal)**
   - **What it is**: The overarching marketing objective of the campaign (`Awareness`, `Consideration`, `Conversion`).
   - **Why it is used**: Configures Amazon DSP bidding algorithms and optimization models.
   - **Business Purpose**:
     - `Awareness`: Maximizes overall ad reach and impression volume.
     - `Consideration`: Drives qualified traffic and product page engagement.
     - `Conversion`: Maximizes purchases, sales leads, and return on ad spend.

2. **KPI Target (Key Performance Indicator)**
   - **What it is**: The primary quantitative metric used to measure success (`Reach`, `Frequency`, `CTR`, `CPC`, `CPA`, `CPDPV`).
   - **Why it is used**: Defines how campaign performance will be evaluated in reporting dashboards.
   - **Business Purpose**: Guides automated bidding algorithms to optimize for the chosen KPI (e.g., lowest Cost Per Reach or highest Click-Through Rate).

3. **Choose conversions to track via Ad Tag**
   - **What it is**: A dropdown to select website tracking events (`Page view`, `Add to shopping cart`, `Checkout`, `Application`).
   - **Why it is used**: Active when **Off Amazon** is selected in Step 1.
   - **Business Purpose**: Uses VOW JavaScript Ad Tags (pixels) on the advertiser's website to attribute off-Amazon conversions back to ad impressions.

4. **Market Budget Allocation**
   - **What it is**: Total monetary expenditure allocated to each target market (e.g., `£10,000.00` for UK).
   - **Why it is used**: Sets the hard spending cap for campaign ad delivery.
   - **Business Purpose**: Prevents overspending and ensures budget is distributed appropriately across selected countries.

5. **Base Bid (CPM)**
   - **What it is**: The maximum Cost-Per-Mille (cost per 1,000 impressions) bid price the advertiser is willing to pay (e.g., `£30.00`).
   - **Why it is used**: Controls bidding competitiveness in programmatic real-time auctions.
   - **Business Purpose**: Ensures the DSP does not enter auctions above the advertiser's maximum bid limit. Premium video formats (like Prime Video) typically require higher base bids (£25–£35).

---

### Step 3: Deals Selection (`step=2`)

Step 3 enables advertisers to select premium, pre-negotiated inventory deals on platforms like Amazon Prime Video.

```
+---------------------------------------------------------------------------------------------------+
|  Step 3: Deals Selection                                                                         |
+---------------------------------------------------------------------------------------------------+
|  Filters: [Market: GB] [Ad length: All] [Genre: All] [Deal type: All]                             |
|  Deals Table:                                                                                     |
|  - Prime Video | Preferred Deal | UK - 30 - ROS | Type: Preferred Deal | CPM: £28.88 Fixed  [x]   |
+---------------------------------------------------------------------------------------------------+
```

#### Detailed Field Explanations:

1. **Curated Deals Table**
   - **What it is**: A catalog of pre-negotiated inventory agreements with publishers, specifically Amazon Prime Video.
   - **Why it is used**: Gives access to high-value, exclusive ad placements (such as non-skippable 15s/30s video ads on Prime Video).
   - **Business Purpose**: Guarantees placement on premium content. Includes three deal types:
     - *Programmatic Guaranteed (PG)*: Guaranteed impression volume at a fixed CPM.
     - *Preferred Deals*: Fixed CPM price without guaranteed impression volume.
     - *Private Auctions*: Floor-priced private bidding.

2. **Ad Length, Genre & Deal Type Filters**
   - **What it is**: Faceted search dropdowns to filter available deals by video length (15s, 30s), content genre (Action, Comedy, Drama), and deal type.
   - **Why it is used**: Helps advertisers quickly locate deals matching their video creative specs and audience programming preferences.
   - **Business Purpose**: Streamlines deal discovery across thousands of available supply options.

3. **Selected Deals Summary Pane**
   - **What it is**: A side panel displaying all deals selected for each market.
   - **Why it is used**: Confirms which inventory sources will be bound to the campaign.
   - **Business Purpose**: Ensures at least one deal is selected before proceeding to audience configuration.

---

### Step 4: Audience Sets (`step=3`)

Step 4 selects the target demographic, in-market, lifestyle, and behavioral audience segments created in Amazon DSP.

```
+---------------------------------------------------------------------------------------------------+
|  Step 4: Audience Sets                                                                           |
+---------------------------------------------------------------------------------------------------+
|  Filters: [Fee: All] [Goal: Awareness]                                                            |
|  Audience Table:                                                                                  |
|  - Healthy snacks | VCPM: £1.63 | Market: 🇬🇧 | Goal: Awareness                          [x]   |
|  Selected Audiences Mode: [Similar] [x Exact]                                                     |
+---------------------------------------------------------------------------------------------------+
```

#### Detailed Field Explanations:

1. **Audience Sets Table & Three Profiles**
   - **What it is**: A list of pre-curated audience target groups built from Amazon's 3,400+ consumer data segments (e.g., `Healthy snacks`, `E-Learning Seekers`). The agent produces three target profiles:
     - **Narrow**: High intent, elevated precision, potential underdelivery risk.
     - **Balanced**: Optimal mix, client recommendation.
     - **Wide**: *(Renamed from Broad)* Maximum reach across demographic & broad interest groups.
   - **Why it is used**: Defines *who* will see the ads based on purchase history, browsing behavior, and lifestyle interests.
   - **Business Purpose**: Reaches consumers with demonstrated buying intent. Shows VCPM fee.

2. **Audience Data Fee (VCPM) Rules** *(David Moss Update)*
   - **Data Source Determines Fee**: Data fees are triggered whenever **Amazon 1P data** (Lifestyle/Interest) or **3P Data Providers** (Experian) are used. Demographic targeting incurs no data fee.
   - **No Compounding Within Provider**: Adding multiple 1P segments from Amazon incurs **1 fixed CPM data fee**, regardless of how many 1P segments are selected.
   - **Cross-Provider Stacking**: Data fees stack **only** when matching segments across *different* data providers (e.g. Amazon 1P + Experian 3P).
   - **Effective CPM Formula**: $\text{Effective CPM} = \text{Base Deal CPM} + \text{Stacked VCPM Data Fees}$.

3. **Matching Mode (`Similar` vs `Exact`)**
   - **What it is**: A toggle switch between `Exact` matching and `Similar` (lookalike) expansion.
   - **Why it is used**: Controls audience targeting strictness.
   - **Business Purpose**:
     - `Exact`: Targets only consumers strictly within the selected audience segment.
     - `Similar`: Uses Amazon ML models to expand reach to lookalike users with similar behaviors.

---

### Step 5: Creatives Binding (`step=4`)

Step 5 attaches actual video or display media assets to the strategy and assigns click-through landing page URLs.

```
+---------------------------------------------------------------------------------------------------+
|  Step 5: Creatives Binding                                                                        |
+---------------------------------------------------------------------------------------------------+
|  Creatives Table:                                                                                 |
|  - SC_WGY_30s_HEART_Online_16x9_v02 | Language: English | Market: 🇬🇧                      [x]   |
|  Selected Creatives Card:                                                                         |
|  - Insert click-through URL: [ https://example.com/landing                                      ] |
+---------------------------------------------------------------------------------------------------+
```

#### Detailed Field Explanations:

1. **Creatives Selection Table**
   - **What it is**: A list of uploaded video and image media assets available in the advertiser’s library (e.g., `SC_WGY_30s_HEART_Online_16x9_v02`).
   - **Why it is used**: Selects the visual ad content that users will see on screen.
   - **Business Purpose**: Matches video asset specifications (aspect ratio 16:9, length 30s) with selected Prime Video deal specs.

2. **Approved Creative Verification (Network Call)**
   - **What it is**: Background verification API call (`GET /api/creatives/?approval_status=APPROVED`).
   - **Why it is used**: Checks if the selected creative asset has passed Amazon DSP policy and technical review.
   - **Business Purpose**: Prevents launching campaigns with rejected or unapproved ad creatives.

3. **Insert Click-Through URL**
   - **What it is**: A text input box to enter the destination website landing page URL (e.g., `https://example.com/landing`).
   - **Why it is used**: Specifies where users are taken when they click on the ad.
   - **Business Purpose**: Essential for driving traffic and tracking conversions on off-Amazon websites.

---

### Step 6: Summary & Reach Forecasting (`step=5`)

Step 6 calculates reach forecasts, summarizes all strategy choices, and publishes the campaign to Amazon DSP.

```
+---------------------------------------------------------------------------------------------------+
|  Step 6: Summary & Reach Forecasting                                                             |
+---------------------------------------------------------------------------------------------------+
|  Summary Cards:                                                                                   |
|  1. Strategy Details [Edit] : Name: Summer_Brand_Awareness_2026 | Dates: 01/08/26 - 31/08/26     |
|  2. Goal, KPI & Bid [Edit]   : Goal: Awareness | Budget: £10,000.00 | Base bid: £30.00             |
|  3. Deals [Edit]             : UK -> Prime Video Preferred Deal (£28.88 CPM)                      |
|  4. Audience Sets [Edit]     : UK -> Healthy snacks, E-Learning Seekers                            |
|  5. Creatives [Edit]         : UK -> SC_WGY_30s_HEART_Online_16x9_v02                             |
|                                                                                                   |
|  [Back]                                                                         [Create Strategy] |
+---------------------------------------------------------------------------------------------------+
```

#### Detailed Field Explanations:

1. **Summary Overview Cards**
   - **What it is**: Five editable summary cards displaying all choices made across Steps 1 to 5.
   - **Why it is used**: Provides a complete pre-launch review of the strategy configuration.
   - **Business Purpose**: Allows users to inspect and edit any parameter before committing budget.

2. **Reach & Frequency Forecasting Engine**
   - **What it is**: Predictive analytics call (`POST /api/strategies/reach-forecast/`).
   - **Why it is used**: Estimates unique audience reach, total impression volume, and average frequency curves.
   - **Business Purpose**: Gives advertisers empirical projections of performance before spending real money.

3. **"Create Strategy" Button & Background Sync**
   - **What it is**: The final confirmation action button that triggers `POST /api/strategies/` (`201 Created`).
   - **Why it is used**: Persists the strategy into the database and launches background DSP campaign generation.
   - **Business Purpose**: Automatically builds Amazon DSP campaigns, ad groups, targeting rules, and creative bindings without manual human intervention.

---

## 3. Natural Language Brief-to-Slot Parsing Heuristic

Below is an end-to-end example showing how an incoming natural language prompt is mapped into Strategy Module fields by the Planning Agent:

**User Brief Input**:  
> *"Create an awareness campaign for my online learning platform in the UK spending £15,000 in August 2026 using Prime Video ads. My landing page is https://learnonline.co.uk"*

**Agent Field Mapping**:
- `Strategy Name` $\rightarrow$ `Online_Learning_UK_Awareness_Aug2026` (Generated & validated)
- `Flight Dates` $\rightarrow$ `2026-08-01` to `2026-08-31`
- `Target Markets` $\rightarrow$ `['GB']`
- `Primary Currency` $\rightarrow$ `GBP (£)`
- `Ad Formats` $\rightarrow$ `['prime_video']`
- `Product Categories` $\rightarrow$ `[1]` (`Education`)
- `Product Location` $\rightarrow$ `NOT_SOLD_ON_AMAZON` (Non-Endemic)
- `Goal` $\rightarrow` `AWARENESS`
- `KPI Target` $\rightarrow` `reach`
- `Market Budget` $\rightarrow` `£15,000.00`
- `Base Bid` $\rightarrow` `£30.00` (Inferred for Prime Video)
- `Ad Tag Conversions` $\rightarrow` `['Page view', 'Checkout']`
- `Click-Through URL` $\rightarrow` `https://learnonline.co.uk`

---

## 4. Multi-Market & Multi-Format Budget Distribution Rules

When a strategy contains multiple markets (e.g., `GB` and `DE`) or multiple ad formats (`Prime Video` AND `Display`):

1. **Equal Default Budget Split**: If total budget is £20,000 for 2 markets (`GB` & `DE`), the agent defaults to £10,000 per market, editable by the user.
2. **Format Bid Differential**:
   - `Prime Video` / `Streaming TV` Base Bid: Default `£30.00` CPM (premium video pricing).
   - `Display` Base Bid: Default `£5.00` CPM (standard display pricing).
3. **Market-Specific Deal Binding**: Deals fetched in Step 3 are strictly isolated per market (`markets=GB` vs `markets=DE`).

---

## 5. Quick Reference Matrix (All Fields across 6 Steps)

| Step | Field Name | Input Type | Required? | Primary Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Strategy Name** | Text Input | **Yes** | Unique identifier for strategy tracking and reporting. |
| **1** | **Flight Dates** | Date Range | **Yes** | Defines campaign start and end operational dates. |
| **1** | **Target Markets** | Multi-Select | **Yes** | Restricts ad delivery to specified country ISO codes. |
| **1** | **Primary Currency** | Dropdown | **Yes** | Standardizes reporting currency (£, €, $). |
| **1** | **Ad Formats** | Multi-Select | **Yes** | Selects placements (`display`, `online_video`, `prime_video`). |
| **1** | **Product Categories** | Multi-Select | **Conditional** | Contextual video targeting taxonomy. |
| **1** | **Selling Location** | Radio | **Yes** | Distinguishes `ON_AMAZON` (Endemic) vs `NOT_SOLD_ON_AMAZON`. |
| **1** | **Product ASINs** | Textarea | **Conditional** | Measures DPV/ATC (`ON_AMAZON`) or organic halo sales (`Off Amazon`). |
| **2** | **Strategy Goal** | Card Select | **Yes** | Configures DSP bidding objective (`Awareness`, `Conversion`). |
| **2** | **KPI Target** | Card Select | **Yes** | Sets target metric (`Reach`, `CTR`, `CPC`, `CPA`). |
| **2** | **Ad Tag Conversions** | Multi-Select | **Off-Amazon** | Tracks off-Amazon website events (Page view, Checkout). |
| **2** | **Market Budget** | Currency Input | **Yes** | Hard spending limit per target country. |
| **2** | **Base Bid (CPM)** | Currency Input | **Yes** | Maximum CPM auction bidding limit. |
| **3** | **Selected Deals** | Checkbox Table | **Yes (Video)** | Binds Prime Video PG/Preferred/Auction inventory deals. |
| **4** | **Audience Sets** | Checkbox Table | **Yes** | Target consumer demographics and behavioral segments. |
| **4** | **Matching Mode** | Toggle | **Yes** | Selects `Exact` segment matching vs `Similar` lookalike expansion. |
| **5** | **Selected Assets** | Checkbox Table | **Yes** | Selects approved video/image media assets. |
| **5** | **Click-Through URL** | Text Input | **Yes** | Destination landing page URL for ad click traffic. |
| **6** | **Summary Cards** | Overview Cards | **Yes** | Pre-launch audit of all strategy choices. |
| **6** | **Reach Forecast** | Analytics Chart | **Yes** | Predicts unique reach, total impressions, and frequency curve. |
| **6** | **Create Strategy** | Action Button | **Yes** | Executes `POST /api/strategies/` (`201 Created`) & background sync. |
