import requests
import json

# Import runner from test_strategy_apis
from test_strategy_apis import call_api, run_strategy_api_tests

if __name__ == "__main__":
    print("=" * 80)
    print("VOW PLATFORM - API TEST RUNNER")
    print("=" * 80)
    
    # Simple check calls
    call_api("User Info", "/user")
    call_api("Strategy Choices", "/strategies/choices/")
    
    # Run full Strategy Module test pipeline
    # run_strategy_api_tests()