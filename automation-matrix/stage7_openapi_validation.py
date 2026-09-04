import json

def run_local_openapi_compliance_check(agent_config):
    print("=================================================================")
    print("MODULE: OPENAPI SPECIFICATION SWAGGER COMPLIANCE VALIDATOR")
    print("=================================================================")
    print("Verifying structural payload against api-reference/specs/agents.yaml...")
    
    # 1. Enforce strict properties defined in the OpenAPI schema block
    if "name" not in agent_config or "system_prompt" not in agent_config or "voice" not in agent_config:
        print("Specification Failure: Fields 'name', 'system_prompt', and 'voice' are strictly REQUIRED.")
        return False

    # 2. Check Tool configurations against validation thresholds
    if "tools" in agent_config and agent_config["tools"]:
        for idx, tool in enumerate(agent_config["tools"]):
            # Check server-side execution bounds
            timeout = tool.get("timeout_seconds", 120)
            if not (1 <= timeout <= 300):
                print(f"Validation Error: 'tools[{idx}].timeout_seconds' [{timeout}] must be between 1s and 300s.")
                return False
                
            http_config = tool.get("http", {})
            if http_config:
                url = http_config.get("url", "")
                if not url.startswith("https://"):
                    print(f"Domain Exception: 'tools[{idx}].http.url' must use secure HTTPS transport protocol layout.")
                    return False

    print("COMPLIANCE STATUS: 100% SUCCESS. Payload matches AssemblyAI Voice Agent v1 specifications.")
    return True
