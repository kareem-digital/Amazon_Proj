import requests
import json

# ==============================================================================
# VOW PLATFORM - STRATEGY MODULE API TEST SUITE
# ==============================================================================
# Instructions: Fill in your active staging sessionid and csrftoken below.
# ==============================================================================

BASE_URL = "https://staging.vowmade.dev/api"
ADVERTISER_ID = "353eea43-bc42-456f-ba4f-3d3e20ea6bc8"

COOKIES = {
    "sessionid": "YOUR_SESSIONID_HERE",
    "csrftoken": "YOUR_CSRFTOKEN_HERE"
}

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Referer": "https://staging.vowmade.dev/",
    "X-CSRFToken": COOKIES["csrftoken"]
}

def call_api(name, endpoint, method="GET", params=None, json_data=None):
    """Generic API Request Wrapper for VOW Staging Endpoints"""
    url = BASE_URL + endpoint

    print("\n" + "=" * 80)
    print(f"       TESTING API: [{name}]")
    print("=" * 80)
    print(f"  METHOD : {method}")
    print(f"  URL    : {url}")
    if params:
        print(f"  PARAMS : {params}")
    if json_data:
        print(f"  PAYLOAD: {json.dumps(json_data, indent=2)}")

    try:
        response = requests.request(
            method=method,
            url=url,
            headers=HEADERS,
            cookies=COOKIES,
            params=params,
            json=json_data,
            timeout=30
        )

        print(f"  STATUS : {response.status_code}")
        
        if response.status_code in [200, 201]:
            data = response.json()
            print("  RESPONSE SUMMARY:")
            print(json.dumps(data, indent=2)[:1000] + ("..." if len(str(data)) > 1000 else ""))
            return data
        else:
            print(f"  ERROR RESPONSE: {response.text[:500]}")
            return None

    except Exception as e:
        print(f"  EXCEPTION OCCURRED: {e}")
        return None

# ==============================================================================
# STRATEGY MODULE 6-STEP API TEST WORKFLOW
# ==============================================================================

def run_strategy_api_tests():
    print("\n🚀 STARTING STRATEGY MODULE API TEST SUITE...\n")

    # --------------------------------------------------------------------------
    # STEP 1 APIs: Strategy Details Setup
    # --------------------------------------------------------------------------
    print("\n--- [STEP 1] TESTING STRATEGY DETAILS APIS ---")
    
    # 1. Fetch Choices
    call_api("1. Fetch Choices", "/strategies/choices/")

    # 2. Check Strategy Name Uniqueness
    call_api("2. Check Name Uniqueness", "/strategies/check_strategy_name_uniqueness/", params={"name": "Test_VOW_Agent_PythonTest"})

    # 3. ASIN Validation (GB Market)
    call_api("3. ASIN Validation", "/contextual-targeting/GB/asin-validation/", method="POST", json_data={"asins": ["B08N5WRWNW"]})

    # 4. Product Categories (GB Market)
    call_api("4. Product Categories", "/contextual-targeting/GB/product-categories/")

    # --------------------------------------------------------------------------
    # STEP 2 APIs: Goal, KPI & Bid Allocation
    # --------------------------------------------------------------------------
    print("\n--- [STEP 2] TESTING GOAL, KPI & CONVERSIONS APIS ---")

    # 5. Conversion Pixel Definitions
    call_api("5. Ad Tag Conversions", "/conversions/definitions/", params={"selected_advertiser_id": ADVERTISER_ID})

    # --------------------------------------------------------------------------
    # STEP 3 APIs: Deals Selection
    # --------------------------------------------------------------------------
    print("\n--- [STEP 3] TESTING DEALS APIS ---")

    # 6. List Deals (Prime Video in GB)
    call_api("6. List Deals", "/deals/", params={"markets": "GB", "formats": "prime_video", "page_size": 25})

    # 7. Deal Filter Properties
    call_api("7. Deal Filter Properties", "/deals/filter-properties/", params={"markets": "GB", "formats": "prime_video"})

    # --------------------------------------------------------------------------
    # STEP 4 APIs: Audience Sets
    # --------------------------------------------------------------------------
    print("\n--- [STEP 4] TESTING AUDIENCE SETS APIS ---")

    # 8. List Pre-curated Audience Sets
    call_api("8. List Audience Sets", "/audience-sets/", params={"markets": "GB", "page_size": 25})

    # 9. Suggest Audience Bundles
    call_api("9. Suggest Audiences", "/audience-sets/suggest/", method="POST", json_data={
        "market": "GB",
        "goal": "AWARENESS",
        "product_categories": [1],
        "brief_text": "Education platform awareness campaign"
    })

    # --------------------------------------------------------------------------
    # STEP 5 APIs: Creatives Binding
    # --------------------------------------------------------------------------
    print("\n--- [STEP 5] TESTING CREATIVES & ASSETS APIS ---")

    # 10. List Media Assets
    call_api("10. List Assets", "/assets/", params={"page_size": 25})

    # 11. Validate Approved Amazon DSP Creatives
    call_api("11. Approved Creatives", "/creatives/", params={"approval_status": "APPROVED", "markets": "GB"})

    # --------------------------------------------------------------------------
    # STEP 6 APIs: Forecasting & Strategy Creation
    # --------------------------------------------------------------------------
    print("\n--- [STEP 6] TESTING FORECASTING & CREATION APIS ---")

    # 12. Strategy Reach Forecast
    call_api("12. Reach Forecast", "/strategies/reach-forecast/", method="POST", json_data={
        "markets": ["GB"],
        "budget": "10000.00",
        "base_bid": "30.00",
        "formats": ["prime_video"],
        "flight_dates": {"lower": "2026-08-01", "upper": "2026-08-31"}
    })

    # 13. Save Strategy Draft
    call_api("13. Save Draft", "/strategies/draft/", method="POST", json_data={
        "name": "Test_VOW_Agent_Draft",
        "advertiser_id": ADVERTISER_ID,
        "channel_type": "dsp",
        "primary_currency": "GBP"
    })

    print("\n✅ STRATEGY MODULE API TEST SUITE COMPLETED!\n")

if __name__ == "__main__":
    run_strategy_api_tests()
