# vow__agent Codebase Architecture & Setup Guide (Hinglish Version)

**Document Name:** `vow_agent_architecture_and_setup_guide_hinglish.md`  
**Location:** `vow docs/`  
**Purpose:** Naye developer ya tester ke liye `vow__agent` codebase ka complete Hinglish breakdown, folder explanation, Virtual Environment setup, aur app run karne ki step-by-step guide.  

---

## 📌 1. vow__agent Complete Folder Structure & Functionality Breakdown

Aapke `vow__agent` codebase ko professional **FastAPI + LangGraph Architecture** par design kiya gaya hai. Har folder aur file ka specific purpose aur functionality neeche detail me samjhayi gayi hai:

```
vow__agent/
├── 📄 Dockerfile                     <-- Containerisation Build (Production deployment image)
├── 📄 pyproject.toml                 <-- Project metadata & dependency definitions
├── 📄 requirements.txt               <-- Main Python packages (FastAPI, LangGraph, Pydantic, etc.)
├── 📄 requirements-dev.txt           <-- Development & Testing packages (pytest, ruff, mypy)
├── 📁 venv/                          <-- Python Virtual Environment (Isolated dependencies)
└── 📁 app/                           <-- MAIN APPLICATION SOURCE CODE
    ├── 📄 __init__.py                <-- Package version marker ("0.1.0")
    ├── 📄 main.py                    <-- FastAPI App Entry point & Server Lifespan manager
    ├── 📄 config.py                  <-- Central Settings & Env Variables Loader (.env)
    │
    ├── 📁 agent/                     <-- 🧠 LANGGRAPH AGENT ENGINE (The Conversational Brain)
    │   ├── 📄 __init__.py
    │   ├── 📄 state.py               <-- Agent State Definition (PlanningState / TypedDict)
    │   ├── 📄 graph.py               <-- LangGraph StateGraph Construction & Node Edges
    │   ├── 📄 checkpointer.py        <-- Session MemorySaver / Postgres State Persistence
    │   └── 📁 nodes/                 <-- Individual State Nodes (Parse, Validate, Forecast, Create)
    │
    ├── 📁 api/                       <-- 🌐 FASTAPI REST ROUTERS & ENDPOINTS
    │   ├── 📄 __init__.py
    │   ├── 📄 routes.py              <-- Central API Router Aggregator
    │   ├── 📄 health.py              <-- Liveness (/health/live) & Readiness (/health/ready) Probes
    │   └── 📄 sessions.py            <-- Chat Session API (/sessions/chat & /sessions/{id})
    │
    ├── 📁 tools/                     <-- 🛠️ VOW PLATFORM REST API WRAPPERS & TOOLS
    │   ├── 📄 __init__.py
    │   ├── 📄 base.py                <-- Base VOW API HTTPX Client (Auth, Headers, Retries, Pagination)
    │   ├── 📄 auth.py                <-- VOW Authentication Providers (StubAuth / SessionTokenAuth)
    │   └── 📄 deals.py               <-- Deals API Tool (Fetch deals, rate cards, filter properties)
    │
    ├── 📁 core/                      <-- ⚙️ CORE UTILITIES & EXCEPTIONS
    │   ├── 📄 __init__.py
    │   ├── 📄 exceptions.py          <-- Custom Exception Hierarchy (VowApiError, GroundingError)
    │   └── 📄 logging.py             <-- Structured JSON Logging Formatter
    │
    ├── 📁 governance/                <-- 🔒 Guardrails, Approval Policies & Safety Checks
    └── 📁 knowledge/                 <-- 📚 RAG Vector Search & Schema Registries
```

---

### 🔍 Har Subsystem Ka Purpose & Functionality Explained

#### 1. `app/agent/` (LangGraph Planning Agent Engine)
- **Kyun Banaya Gaya:** Ye AI Agent ka **Main Brain** hai. Ye user ke chat brief ko receive karta hai aur step-by-step state nodes ke zariye strategy proposal tayyar karta hai.
- **Key Files:**
  - `state.py`: Agent ki memory state (`PlanningState`) jisme saare messages aur strategy slots (Dates, Market, Budget) store hote hain.
  - `graph.py`: LangGraph StateGraph compiled loop jo decide karta hai ki ek node ke baad agla node kon sa chalega.
  - `checkpointer.py`: Conversational memory persistence manager (In-memory memory saver ya Postgres database saver).

#### 2. `app/api/` (FastAPI REST Endpoints)
- **Kyun Banaya Gaya:** UI (Riddhi / Frontend) aur external clients ko Agent ke sath connect karne ke liye REST APIs provide karta hai.
- **Key Files:**
  - `health.py`: Server health check endpoints (`/api/v1/health/live` & `/api/v1/health/ready`).
  - `sessions.py`: Multi-turn chat session endpoints (`POST /api/v1/sessions/chat`) jahan user prompt bhejta hai aur agent ka response haasil karta hai.

#### 3. `app/tools/` (VOW Platform REST Tool Wrappers)
- **Kyun Banaya Gaya:** Agent ko actual VOW Platform APIs (Deals, Audiences, ASIN Validation, Reach Forecast, Strategy Creation) ke sath connect karta hai.
- **Key Files:**
  - `base.py`: Automatic HTTP client jo auth headers, retries, error handling, aur pagination automatically handle karta hai.
  - `deals.py`: Deals fetch karne aur rate card pricing nikalne ka tool (`GET /deals/`, `GET /rates/ctv/{market}/`).

#### 4. `app/core/` (Logging & Exception Handling)
- **Kyun Banaya Gaya:** Platform ke custom error classes (jaise `VowApiError`, `VowAuthError`) aur Production-grade Structured JSON logging set up karne ke liye.

---

## 🛠️ 2. Step-by-Step Virtual Environment Setup & App Run Guide

First-time user ya naye developer ko application start karne ke liye in simple steps ko follow karna hoga:

### Step 1: `vow__agent` Folder Me Navigate Karein
```bash
cd "e:\VOW Agent\vow__agent"
```

### Step 2: Python Virtual Environment (`venv`) Create Karein
```bash
# Windows Command:
python -m venv venv

# macOS / Linux Command:
python3 -m venv venv
```

### Step 3: Virtual Environment Activate Karein
```bash
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Windows Command Prompt (cmd):
.\venv\Scripts\activate.bat

# macOS / Linux Terminal:
source venv/bin/activate
```

### Step 4: Dependencies Install Karein
```bash
pip install -r requirements.txt
```

### Step 5: Application Server Start / Run Karein
```bash
# Uvicorn Development Server with Auto-Reload:
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

---

## 🧪 3. APIs Test & Verify Kaise Karein?

Application run hone ke baad aap 2 tareeqo se test kar sakte hain:

### Option A: Interactive Swagger API Documentation (Browser Me)
Open your browser and navigate to:
👉 **`http://127.0.0.1:8000/docs`**

Yahan aapko live interactive Swagger UI dikhega jahan se aap endpoints ko click karke test kar sakte hain!

### Option B: Terminal / Python Test Commands

#### 1. Test Server Health (Liveness Probe):
```bash
python -c "import httpx; print(httpx.get('http://127.0.0.1:8000/api/v1/health/live').json())"
```
**Expected Response:**
```json
{"status": "ok", "service": "vow-agent", "environment": "local", "version": "0.1.0"}
```

#### 2. Test LangGraph Agent Chat Session Endpoint:
```bash
python -c "import httpx; print(httpx.post('http://127.0.0.1:8000/api/v1/sessions/chat', json={'message': 'Hello, I want to plan a CTV campaign for UK with £10000 budget'}).json())"
```
**Expected Response:**
```json
{
  "session_id": "44d59973-6159-4a92-8443-f1437643c6d0",
  "reply": "Hello! I am the VOW planning agent. Tell me about the CTV campaign you would like to plan..."
}
```

---

## 📄 Related Project Documents
- 📄 **Implementation Pre-Requisites Guide:** [implementation_pre_requisites_hinglish.md](file:///e:/VOW%20Agent/vow%20docs/implementation_pre_requisites_hinglish.md)
- 📄 **Beginner Terms Glossary:** [vow_technical_glossary_hinglish.md](file:///e:/VOW%20Agent/vow%20docs/vow_technical_glossary_hinglish.md)
- 📄 **Master Technical Specification:** [update_strategy_schema_registry.md](file:///e:/VOW%20Agent/vow%20docs/update_strategy_schema_registry.md)
