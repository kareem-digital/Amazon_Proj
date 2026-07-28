"""
VOW Platform - Registries API Inspection & Test Suite
Location: vow__agent/tests/test_registries_api.py

Tests all 5 VOW Registries against Live Endpoints:
1. Strategy Choices & Enumerations Registry (/api/strategies/choices/)
2. Deals & Inventory Rate Cards Registry (/api/deals/ & /api/deals/filter-properties/)
3. Audience Sets & Vector Suggestions Registry (/api/audience-sets/ & /api/audience-sets/suggest/)
4. Ad Tag Conversion Pixel Registry (/api/conversions/definitions/)
5. Local VOW Agent Health & Session API Registry (http://127.0.0.1:8080/api/v1/health/live)
"""

import sys
import json
import httpx
from typing import Any

# Ensure UTF-8 output on Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Staging VOW API Base URL
VOW_STAGING_BASE_URL = "https://staging.vowmade.dev/api"
LOCAL_AGENT_BASE_URL = "http://127.0.0.1:8080/api/v1"
TEST_ADVERTISER_ID = "353eea43-bc42-456f-ba4f-3d3e20ea6bc8"

# Optional Staging Cookies (Paste active sessionid & csrftoken from browser to hit live staging)
COOKIES = {
    "sessionid": "k9tb3b3dtprkhob30d9uyhjvft268l4y",
    "csrftoken": "79KrzvPtXupDDZwmqjLzv4afHakDRZL5"
}

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Vowmade-Advertiser-Id": TEST_ADVERTISER_ID,
    "X-CSRFToken": COOKIES["csrftoken"] if COOKIES["csrftoken"] else ""
}

def print_header(title: str):
    print("\n" + "=" * 90)
    print(f" [REGISTRY CHECK] {title}")
    print("=" * 90)

def print_result(status_code: int, data: Any):
    print(f"  STATUS CODE : {status_code}")
    if status_code in [200, 201, 202]:
        print("  [SUCCESS] LIVE RESPONSE DATA SHAPE:")
        print(json.dumps(data, indent=2))
    else:
        print(f"  [NOTICE] HTTP RESPONSE ({status_code}): {str(data)[:250]}")

def test_registry_1_choices():
    """Registry 1: Choices & Enumerations (/strategies/choices/)"""
    print_header("1. Strategy Choices & Enumerations Registry")
    endpoint = f"{VOW_STAGING_BASE_URL}/strategies/choices/"
    try:
        with httpx.Client(timeout=10.0, cookies=COOKIES if COOKIES["sessionid"] else None) as client:
            res = client.get(endpoint, headers=HEADERS)
            print_result(res.status_code, res.json() if res.status_code == 200 else res.text)
    except Exception as e:
        print(f"  [EXCEPTION] Connection error: {e}")

def test_registry_2_deals():
    """Registry 2: Deals & Rate Cards (/deals/ & /deals/filter-properties/)"""
    print_header("2. Deals & Inventory Rate Cards Registry")
    endpoint_deals = f"{VOW_STAGING_BASE_URL}/deals/"
    params = {"markets": "GB", "formats": "streaming_tv", "page_size": 5}
    try:
        with httpx.Client(timeout=10.0, cookies=COOKIES if COOKIES["sessionid"] else None) as client:
            print("  --> Calling GET /api/deals/?markets=GB...")
            res = client.get(endpoint_deals, headers=HEADERS, params=params)
            print_result(res.status_code, res.json() if res.status_code == 200 else res.text)
    except Exception as e:
        print(f"  [EXCEPTION] Connection error: {e}")

def test_registry_3_audiences():
    """Registry 3: Audience Sets & Vector Suggestions (/audience-sets/ & /suggest/)"""
    print_header("3. Audience Sets & Vector Suggestions Registry")
    try:
        with httpx.Client(timeout=10.0, cookies=COOKIES if COOKIES["sessionid"] else None) as client:
            print("  --> Calling POST /api/audience-sets/suggest/...")
            suggest_payload = {
                "market": "GB",
                "goal": "AWARENESS",
                "product_categories": [1],
                "prompt": "Higher education online learning campaign in UK"
            }
            res_sug = client.post(f"{VOW_STAGING_BASE_URL}/audience-sets/suggest/", headers=HEADERS, json=suggest_payload)
            print_result(res_sug.status_code, res_sug.json() if res_sug.status_code in [200, 201, 202] else res_sug.text)
    except Exception as e:
        print(f"  [EXCEPTION] Connection error: {e}")

def test_registry_4_conversions():
    """Registry 4: Conversion Tracking Pixel Definitions (/conversions/definitions/)"""
    print_header("4. Conversion Tracking Pixel Registry")
    endpoint = f"{VOW_STAGING_BASE_URL}/conversions/definitions/"
    try:
        with httpx.Client(timeout=10.0, cookies=COOKIES if COOKIES["sessionid"] else None) as client:
            res = client.get(endpoint, headers=HEADERS, params={"selected_advertiser_id": TEST_ADVERTISER_ID})
            print_result(res.status_code, res.json() if res.status_code == 200 else res.text)
    except Exception as e:
        print(f"  [EXCEPTION] Connection error: {e}")

def test_registry_5_local_agent():
    """Registry 5: Local FastAPI VOW Agent Health & Session API Registry (http://127.0.0.1:8080/api/v1/)"""
    print_header("5. Local VOW Agent Health & Session API Registry")
    try:
        with httpx.Client(timeout=5.0) as client:
            print("  --> Calling GET http://127.0.0.1:8080/api/v1/health/live...")
            res_health = client.get(f"{LOCAL_AGENT_BASE_URL}/health/live")
            print_result(res_health.status_code, res_health.json() if res_health.status_code == 200 else res_health.text)

            print("\n  --> Calling POST http://127.0.0.1:8080/api/v1/sessions/chat...")
            chat_payload = {
                "message": "Hello, I want to plan a CTV campaign for UK with £10000 budget"
            }
            res_chat = client.post(f"{LOCAL_AGENT_BASE_URL}/sessions/chat", json=chat_payload)
            print_result(res_chat.status_code, res_chat.json() if res_chat.status_code == 200 else res_chat.text)
    except Exception as e:
        print(f"  [NOTICE] Local Agent connection: {e}\n  (Make sure 'python -m uvicorn app.main:app --port 8080' is running!)")

def run_all_registry_tests():
    print("\n>>> STARTING VOW PLATFORM REGISTRIES INSPECTION TEST SUITE...\n")
    test_registry_1_choices()
    test_registry_2_deals()
    test_registry_3_audiences()
    test_registry_4_conversions()
    test_registry_5_local_agent()
    print("\n" + "=" * 90)
    print(" >>> ALL REGISTRY INSPECTION TESTS COMPLETED!")
    print("=" * 90 + "\n")

if __name__ == "__main__":
    run_all_registry_tests()
