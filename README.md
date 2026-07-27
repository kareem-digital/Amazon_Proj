# VOW Advertising Platform - Planning Agent & Strategy Schema Registry

![Status](https://img.shields.io/badge/Status-Approved_Architecture-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-State_Machine-purple)
![API](https://img.shields.io/badge/VOW_API-OpenAPI_2.0-orange)

## 📌 Executive Overview

This repository contains the official **Technical Architecture Specifications, Schema Registry, Field Reference Guides, and Python API Integration Test Suite** for the **Strategy Module** and **LangGraph Planning Agent** within the VOW Advertising Platform.

The VOW Strategy Module automates Amazon DSP (Demand-Side Platform) and Prime Video campaign creation by translating natural language briefs into structured, API-validated ad strategy cards.

```
                  +-------------------------------------------------------+
                  |               USER INTERFACE / BRIEF INPUT            |
                  +-------------------------------------------------------+
                                              |
                                              v
                  +-------------------------------------------------------+
                  |         LANGGRAPH PLANNING AGENT (STATE ENGINE)        |
                  |  - Stateful Slot Filling & Slot Verification          |
                  |  - Schema Validation via Pydantic Data Models         |
                  |  - Automated Natural Language Brief Extractor         |
                  +-------------------------------------------------------+
                                              |
                                              v
                  +-------------------------------------------------------+
                  |              VOW REST API ENGINE / TOOLS              |
                  |  - Uniqueness & ASIN Validation Calls                 |
                  |  - Audience Vector Search & Suggestion Engine         |
                  |  - Reach & Frequency Forecasting Engine               |
                  |  - Amazon DSP Campaign Entity Creation                |
                  +-------------------------------------------------------+
                                              |
                                              v
                  +-------------------------------------------------------+
                  |             DATABASE & AMAZON DSP SYNC ENGINE         |
                  +-------------------------------------------------------+
```

---

## 📁 Repository Structure

```
.
├── README.md                      # Repository overview & quick start guide
├── strategy_schema_registry.md    # Master technical architecture, REST APIs & Pydantic models (SSOT)
├── strategy_module_explained.md   # Field-by-field functional reference guide (Steps 0-5)
├── strategy_apis_testing_guide.md # OpenAPI endpoint catalog & API payload documentation
├── test_strategy_apis.py          # Production Python API test suite for 15 Strategy endpoints
├── requests.py                    # Modular Staging API test runner
├── VOW Platform Screen/           # UI workflow screen captures (Step 1 to Overview)
└── .gitignore                     # Git exclusion rules
```

---

## 🎯 Core Architectural Principles

1. **Zero-Hallucination Policy**: The Planning Agent NEVER invents strategy parameters, metrics, targeting criteria, or deal IDs out of its LLM weights. It only populates values verified against the VOW Database and official REST APIs.
2. **Self-Filling Form Paradigm**: The agent operates as a stateful slot-filling engine backed by **LangGraph**. Inputs received via natural language chat or uploaded brief documents are parsed into registered Pydantic slot schemas.
3. **API-Driven Tool Execution**: Every step of the strategy workflow maps directly to official VOW API endpoints for choice retrieval, validation, audience suggestion, reach forecasting, and campaign draft persistence.

---

## 🔄 The 6-Step Strategy Creation Workflow

| Step Index | Wizard Step | Core Functions | REST APIs Called |
| :--- | :--- | :--- | :--- |
| **Step 0** | **Strategy Details** | Strategy Name, Flight Dates, Target Markets, Primary Currency, Ad Formats, Product Categories, Product Location (`ON_AMAZON` vs `NOT_SOLD_ON_AMAZON`), Product ASINs. | `GET /api/strategies/choices/`<br>`GET /api/strategies/check_strategy_name_uniqueness/`<br>`POST /api/contextual-targeting/{market}/asin-validation/`<br>`GET /api/contextual-targeting/{market}/product-categories/` |
| **Step 1** | **Goal, KPI & Bid** | Strategy Goal (`AWARENESS`, `CONSIDERATION`, `CONVERSION`), Primary KPI Target, Ad Tag Conversion Pixel Events, Market Budgets, Base CPM Bids. | `GET /api/conversions/definitions/` |
| **Step 2** | **Deals Selection** | Prime Video Programmatic Guaranteed (PG), Preferred Deals, Private Auction Inventory Selection & Filters. | `GET /api/deals/`<br>`GET /api/deals/filter-properties/` |
| **Step 3** | **Audience Sets** | In-market & behavioral audience targeting bundles (Narrow, Balanced, Broad), VCPM Data Fees, Matching Mode (`Exact` vs `Similar`). | `GET /api/audience-sets/`<br>`POST /api/audience-sets/suggest/` |
| **Step 4** | **Creatives Binding** | 16:9 Video & Display Asset Binding, Amazon DSP Approval Status Verification, Click-Through Landing Page URLs. | `GET /api/assets/`<br>`GET /api/creatives/` |
| **Step 5** | **Summary & Forecast** | Strategy Card Review, Automated Reach & Frequency Forecast Curves, Strategy Entity Persistence (`201 Created`), Background Amazon DSP Sync. | `POST /api/strategies/reach-forecast/`<br>`POST /api/strategies/draft/`<br>`POST /api/strategies/`<br>`GET /api/strategies/{id}/` |

---

## 🚀 Quick Start & API Testing Guide

### Prerequisites
- Python 3.10+
- `requests` library

```bash
pip install requests pydantic
```

### Running the API Test Suite

1. Open `test_strategy_apis.py` and input your active VOW Staging session cookies:
   ```python
   COOKIES = {
       "sessionid": "YOUR_STAGING_SESSIONID",
       "csrftoken": "YOUR_STAGING_CSRFTOKEN"
   }
   ```

2. Execute the test runner:
   ```bash
   python test_strategy_apis.py
   ```

---

## 📖 Key Specification Documents

- 📄 **[Technical Specification & Registry (`strategy_schema_registry.md`)](./strategy_schema_registry.md)**: Includes Pydantic schemas, API contracts, LangGraph State Machine dictionary, and zero-reach auto-widening recovery loops.
- 📄 **[Field-by-Field Reference Guide (`strategy_module_explained.md`)](./strategy_module_explained.md)**: Complete business explanation for every form field, brief parsing heuristics, and multi-market budget distribution rules.
- 📄 **[API Catalog & Test Specs (`strategy_apis_testing_guide.md`)](./strategy_apis_testing_guide.md)**: Deep dive into all 15 required REST API endpoints.

---

## 🛡️ License & Confidentiality

Private Repository — Proprietary software owned by VOW Advertising Platform. All rights reserved.
