# VOW Strategy Module - API Catalog & Python Testing Guide

**Document Version:** 1.0.0  
**Target Audience:** QA Engineers, Backend Developers, AI Developers  
**Purpose:** Comprehensive guide listing all REST APIs required for the Strategy Module, complete with Python test scripts and payload specifications.

---

## 1. Overview of Strategy Module APIs

Out of the total endpoints in the VOW OpenAPI 2.0 Swagger specification, **15 key APIs** are required to operate the Strategy Module and power the Planning Agent.

```
+---------------------------------------------------------------------------------------------------+
|                                  STRATEGY MODULE API PIPELINE                                     |
+---------------------------------------------------------------------------------------------------+
|  [Step 1] GET /strategies/choices/                        -> Fetch Goals, KPIs, Channels          |
|  [Step 1] GET /strategies/check_strategy_name_uniqueness/ -> Validate Strategy Name Uniqueness   |
|  [Step 1] POST /contextual-targeting/{market}/asin-val/   -> Validate ASIN List                  |
|  [Step 1] GET /contextual-targeting/{market}/product-cat/ -> Fetch Product Categories            |
|  [Step 2] GET /conversions/definitions/                   -> Fetch Ad Tag Conversion Pixel events |
|  [Step 3] GET /deals/                                     -> List Prime Video & PG Deals          |
|  [Step 3] GET /deals/filter-properties/                   -> Fetch Deal Facet Filters             |
|  [Step 4] GET /audience-sets/                             -> List Pre-curated Audience Sets       |
|  [Step 4] POST /audience-sets/suggest/                    -> Suggest Audience Bundles (Vector)    |
|  [Step 5] GET /assets/                                    -> List Registered Video/Image Assets   |
|  [Step 5] GET /creatives/                                 -> Validate Approved Amazon DSP Tags    |
|  [Step 6] POST /strategies/reach-forecast/                -> Calculate Reach & Frequency Curve    |
|  [Step 6] POST /strategies/draft/                         -> Save Partial Strategy Draft          |
|  [Step 6] POST /strategies/                               -> Persist & Sync Full Strategy (201)   |
|  [Post]   GET /strategies/{id}/                           -> Read Created Strategy Overview       |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Master API Specifications & Parameters

### Step 1 APIs: Strategy Details Setup

#### 1. Fetch Choices (`strategies_choices_list`)
- **Method / Endpoint**: `GET /api/strategies/choices/`
- **Query Params**: None
- **Purpose**: Returns enum choices for strategy goals, KPI target types, currencies, channels, and product locations.

#### 2. Check Name Uniqueness (`strategies_check_strategy_name_uniqueness`)
- **Method / Endpoint**: `GET /api/strategies/check_strategy_name_uniqueness/`
- **Query Params**: `name` (String, required e.g., `Summer_Brand_Awareness_2026`)
- **Purpose**: Confirms strategy name is unique across advertiser account.

#### 3. ASIN Validation (`contextual-targeting_asin-validation_create`)
- **Method / Endpoint**: `POST /api/contextual-targeting/{market}/asin-validation/`
- **Path Params**: `market` (ISO Country Code e.g. `GB`)
- **Request Payload**: `{"asins": ["B08N5WRWNW"]}`
- **Purpose**: Validates ASIN existence and returns product titles, brands, and categories.

#### 4. Product Categories (`contextual-targeting_product-categories_list`)
- **Method / Endpoint**: `GET /api/contextual-targeting/{market}/product-categories/`
- **Path Params**: `market` (ISO Country Code e.g. `GB`)
- **Purpose**: Fetches product categories for contextual video deal targeting.

---

### Step 2 APIs: Goal, KPI & Bid Allocation

#### 5. Ad Tag Conversion Definitions (`conversions_definitions_list`)
- **Method / Endpoint**: `GET /api/conversions/definitions/`
- **Query Params**: `selected_advertiser_id` (UUID, required e.g., `353eea43-bc42-456f-ba4f-3d3e20ea6bc8`)
- **Purpose**: Returns active website event definitions (`Page view`, `Checkout`, `Application`) for off-Amazon attribution.

---

### Step 3 APIs: Deals Selection

#### 6. List Inventory Deals (`deals_list`)
- **Method / Endpoint**: `GET /api/deals/`
- **Query Params**: `markets` (`GB`), `formats` (`prime_video`), `search`, `page_size` (`25`)
- **Purpose**: Fetches Prime Video PG deals, preferred deals, and private auction inventory.

#### 7. Deal Filter Properties (`deals_filter_properties`)
- **Method / Endpoint**: `GET /api/deals/filter-properties/`
- **Query Params**: `markets` (`GB`), `formats` (`prime_video`)
- **Purpose**: Returns filter options for video length, content genre, and pricing model.

---

### Step 4 APIs: Audience Sets

#### 8. List Pre-Curated Audience Sets (`audience-sets_list`)
- **Method / Endpoint**: `GET /api/audience-sets/`
- **Query Params**: `markets` (`GB`), `search`, `page_size` (`25`)
- **Purpose**: Lists pre-existing audience sets and VCPM data fees.

#### 9. Audience Suggestion Engine (`audience-sets_suggest_create`)
- **Method / Endpoint**: `POST /api/audience-sets/suggest/`
- **Request Payload**:
```json
{
  "market": "GB",
  "goal": "AWARENESS",
  "product_categories": [1],
  "brief_text": "Education platform awareness campaign"
}
```
- **Purpose**: Vector similarity search generating `narrow`, `balanced`, and `broad` audience bundles.

---

### Step 5 APIs: Creatives Binding

#### 10. List Media Assets (`assets_list`)
- **Method / Endpoint**: `GET /api/assets/`
- **Query Params**: `target_types` (`video`), `search`, `page_size` (`25`)
- **Purpose**: Lists uploaded 16:9 30s video assets.

#### 11. Validate Approved Creatives (`creatives_list`)
- **Method / Endpoint**: `GET /api/creatives/`
- **Query Params**: `approval_status` (`APPROVED`), `markets` (`GB`), `asset_id`
- **Purpose**: Confirms selected creative asset is approved by Amazon DSP.

---

### Step 6 APIs: Forecasting & Strategy Creation

#### 12. Reach & Frequency Forecast (`strategies_reach_forecast`)
- **Method / Endpoint**: `POST /api/strategies/reach-forecast/`
- **Request Payload**:
```json
{
  "markets": ["GB"],
  "budget": "10000.00",
  "base_bid": "30.00",
  "formats": ["prime_video"],
  "audience_set_ids": ["aud_101"],
  "flight_dates": {"lower": "2026-08-01", "upper": "2026-08-31"}
}
```
- **Purpose**: Calculates estimated impressions, unique reach, and reach curves.

#### 13. Create Strategy (`strategies_create`)
- **Method / Endpoint**: `POST /api/strategies/`
- **Request Payload**: Full Strategy JSON Card.
- **Purpose**: Creates strategy record (`201 Created`) and launches background Amazon DSP sync.

#### 14. Read Strategy Overview (`strategies_read`)
- **Method / Endpoint**: `GET /api/strategies/{id}/`
- **Purpose**: Reads created strategy card for the Overview page.

---

## 3. How to Test Strategy APIs in Python

Below is the complete testing framework. You can run `python test_strategy_apis.py` to execute all 15 Strategy Module endpoints against the VOW Staging API environment.
