import json
import re

def validate_tool_schema_compliance(tool_definition):
    print("=================================================================")
    print("MODULE: TOOLS MATRIX PARAMETER & EXECUTION SYSTEM CHECKER")
    print("=================================================================")
    print("Verifying schema constraints against Page 15 Tools Core Documentation...")

    name = tool_definition.get("name", "unknown")
    execution_mode = tool_definition.get("execution_mode", "interactive")
    params = tool_definition.get("parameters", {}).get("properties", {})

    # 1. Enforce strict spoken digit sequence optimization warning rules
    for param_name, param_details in params.items():
        desc = param_details.get("description", "").lower()
        pattern = param_details.get("pattern", "")
        
        # Check if the param is a long number sequence (card, account number, ID)
        if any(keyword in desc for keyword in ["card", "account", "id", "number"]):
            if pattern and "\\d" in pattern and " *" not in pattern:
                print(f"BRITTLE PATTERN DETECTED for '{param_name}': [{pattern}]")
                print("   Callers read long numbers with spaces (e.g. '4 2 4 2 ...').")
                print("   An exact pattern will trap users in a re-ask loop.")
                print("Fix suggestion: Use spaces allowance regex like: ' *([0-9] *){13,19}'")
                print("-----------------------------------------------------------------")

    # 2. Check conversational safety limits on execution modes
    if execution_mode == "hold":
        timeout = tool_definition.get("timeout_seconds", 120)
        print(f"[Hold Mode detected on '{name}']: Audio streams and user caption deltas")
        print(f"   will temporarily pause for up to {timeout} seconds during execution.")
    else:
        print(f"[Interactive Mode detected on '{name}']: Optimized for sub-5 second responses.")

    print("\nSCHEMA REVIEW COMPLETED: Validation suggestions output above successfully.")

if __name__ == "__main__":
    # Test layout mapping a brittle mock payload matching documentation warning triggers
    sample_brittle_tool = {
        "name": "verify_credit_card",
        "execution_mode": "interactive",
        "parameters": {
            "type": "object",
            "properties": {
                "card_number": {
                    "type": "string",
                    "description": "The customer credit card primary account number sequence",
                    "pattern": "\\d{16}" # Brittle format trigger rule check
                }
            }
        }
    }
    validate_tool_schema_compliance(sample_brittle_tool)
