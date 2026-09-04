import json

def prevalidate_tool_schema_compliance(sample_tools_array):
    print("=================================================================")
    print("MODULE: CLIENT-SIDE ASYNCAPI SCHEMA COMPLEXITY SECURITY GATE")
    print("=================================================================")
    print("Enforcing strict parameter verification metrics against Page 37...")

    if not sample_tools_array:
        print("Status: Tools array empty. Skipping schema parsing boundaries.")
        return True

    for idx, tool in enumerate(sample_tools_array):
        tool_name = tool.get("name", f"index_{idx}")
        parameters_block = tool.get("parameters", {})
        properties = parameters_block.get("properties", {})
        
        # Strict Page 37 Specification check: server doesn't validate schemas on connect!
        if not properties:
            print(f"Validation Error on tool '{tool_name}': Missing properties dictionary constraint.")
            print("   Malformed schemas are accepted by the server but break model calling logic.")
            return False
            
        for param, details in properties.items():
            description = details.get("description", "").strip()
            # Enforce descriptive parameter contexts to maximize extraction accuracy
            if len(description) < 15:
                print(f"BRITTLE SCHEMA WARNING: Parameter '{param}' on tool '{tool_name}' description is too short.")
                print("   The model relies on descriptions to extract variables from live speech.")
                print("-----------------------------------------------------------------")

    print("=================================================================")
    print("STATUS: Pre-flight tool validations completed successfully.")
    print("=================================================================")
    return True

if __name__ == "__main__":
    # Test simulation modeling a brittle schema configuration structure [INDEX: 0.1.70]
    sample_malformed_tools = [{
        "name": "get_account_balance",
        "parameters": {
            "type": "object",
            "properties": {
                "account_id": {
                    "type": "string",
                    "description": "Short." # Triggers our warning block rule cleanly
                }
            }
        }
    }]
    prevalidate_tool_schema_compliance(sample_malformed_tools)
  
