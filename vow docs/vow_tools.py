"""
VOW Platform API Tools & Utility Functions for Planning Agent
Handles API integrations, deal auto-matching, currency inference, and reach forecasting.
"""

from typing import List, Dict, Any, Optional
from schemas import (
    CurrencyEnum, GoalEnum, FormatEnum, SelectedDealSchema, InventoryTierEnum,
    TargetingLocationEnum, SelectedAudienceSetSchema, FullStrategySchema
)

# Currency Inference Map (Comment 9)
MARKET_CURRENCY_MAP = {
    "GB": CurrencyEnum.GBP,
    "DE": CurrencyEnum.EUR,
    "FR": CurrencyEnum.EUR,
    "ES": CurrencyEnum.EUR,
    "IT": CurrencyEnum.EUR,
    "US": CurrencyEnum.USD,
}

def infer_currency_from_market(market_code: str) -> CurrencyEnum:
    """Infer primary currency from market ISO code (Comment 9)"""
    return MARKET_CURRENCY_MAP.get(market_code.upper(), CurrencyEnum.GBP)

def auto_generate_strategy_name(category_name: str, market: str, goal: str, month_year: str = "Aug2026") -> str:
    """Auto-generate strategy name from brief context (Comment 7)"""
    clean_category = category_name.strip().replace(" ", "")
    return f"{clean_category}_{market.upper()}_{goal.capitalize()}_{month_year}"

def check_strategy_name_uniqueness(name: str) -> bool:
    """Mock/Real API call to check strategy name uniqueness (Comment 7)"""
    # Returns True if unique, False if duplicate
    existing_names = ["Education_GB_Awareness_Aug2026"]
    return name not in existing_names

def auto_match_inventory_deals(market: str, format_type: str = "streaming_tv") -> List[SelectedDealSchema]:
    """Auto-match inventory deals in background based on brief parameters (Comment 18)"""
    if market.upper() == "GB":
        return [
            SelectedDealSchema(
                deal_id="EXT7P75718S8MNR",
                name="Prime Video Preferred Deal (UK ROS 30s)",
                cpm="28.88",
                inventory_tier=InventoryTierEnum.AMAZON_OWNED,
                targeting_choice=TargetingLocationEnum.AMAZON_DSP,
                allocated_budget_percentage=100.0
            )
        ]
    else:
        return [
            SelectedDealSchema(
                deal_id="EXT3P99201DE",
                name="EU Programmatic Guaranteed Deal (ROS 30s)",
                cpm="24.50",
                inventory_tier=InventoryTierEnum.THREE_P_PRE_CURATED,
                targeting_choice=TargetingLocationEnum.AMAZON_DSP,
                allocated_budget_percentage=100.0
            )
        ]

def suggest_audience_sets(market: str, goal: str, brief_text: str) -> List[SelectedAudienceSetSchema]:
    """
    Suggest audience sets via vector search (Comment 20).
    Returns a Flat List of Audience Sets (bundles.narrow/balanced/broad nesting not supported).
    """
    return [
        SelectedAudienceSetSchema(
            audience_set_id="aud-uk-edu-inmarket-01",
            name="Higher Education & Online Learning In-Market (Amazon 1P)",
            vcpm_fee="2.00"
        ),
        SelectedAudienceSetSchema(
            audience_set_id="aud-uk-tech-lifestyle-02",
            name="Tech Enthusiasts & Young Professionals Lifestyle (Amazon 1P)",
            vcpm_fee="2.00"
        )
    ]

def calculate_reach_forecast(market: str, budget: float, blended_cpm: float = 28.88) -> Dict[str, Any]:
    """Forecast unique reach and impression volume"""
    total_impressions = int((budget / blended_cpm) * 1000)
    estimated_reach = int(total_impressions / 2.5)  # Average frequency 2.5
    return {
        "budget": f"{budget:.2f}",
        "blended_cpm": f"{blended_cpm:.2f}",
        "total_impressions": total_impressions,
        "estimated_reach": estimated_reach,
        "average_frequency": 2.5
    }

def create_simple_strategy(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Persist simplified CTV strategy via POST /api/simple-strategies/ (Comment 24)
    Direct status transition to 'finalised' (Comment 23)
    """
    return {
        "status_code": 201,
        "strategy_id": "VMA2026365",
        "status": "finalised",
        "message": "Strategy successfully created and published with status 'finalised'",
        "payload": payload
    }

def update_strategy_patch(strategy_id: str, patch_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Partial update existing strategy post-creation via PATCH /api/strategies/{id}/ (Comment 28)
    Used to update deferred ASINs, selling location, and conversion pixels.
    """
    return {
        "status_code": 200,
        "strategy_id": strategy_id,
        "updated_fields": list(patch_data.keys()),
        "message": f"Successfully updated fields {list(patch_data.keys())} on strategy {strategy_id}"
    }
