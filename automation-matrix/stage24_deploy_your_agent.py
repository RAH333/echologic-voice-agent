import json

def compile_deployment_session_handshake(agent_id=None, inline_config_dict=None):
    print("=================================================================")
    print("MODULE: DEPLOYMENT INFRASTRUCTURE & LIFECYCLE HANDSHAKER")
    print("=================================================================")
    print("Evaluating session configurations against Page 24 Deployment rules...")

    # 1. Enforce strict mutual exclusion constraint rules as defined on Page 24
    if agent_id and inline_config_dict:
        print("Configuration Error: 'agent_id' is MUTUALLY EXCLUSIVE with inline fields.")
        print("   You cannot bind a stored agent while also passing properties inline.")
        print("Fix: Omit 'agent_id' to configure per session dynamically.")
        return None

    if agent_id:
        print(f"Verified: Binding session straight to cloud-stored agent ID: {agent_id}")
        session_payload = {
            "type": "session.update",
            "session": {
                "agent_id": str(agent_id).strip()
            }
        }
    elif inline_config_dict:
        print("Verified: Assembling custom individual dynamic inline session payload.")
        session_payload = {
            "type": "session.update",
            "session": inline_config_dict
        }
    else:
        print("Error: Missing configuration parameters. Provide an agent ID or inline data.")
        return None

    print("\n=================================================================")
    print("SUCCESS: WebSocket initialization payload compiled cleanly.")
    print("=================================================================")
    print("Lifecycle Billing Reminder:")
    print("   Always execute an explicit 'session.end' payload call when closing.")
    print("   Skipping it drops connection into an expensive 30s grace loop window.")
    return session_payload

if __name__ == "__main__":
    # Test simulation: modeling an un-permitted collision payload setup
    sample_inline_data = {"system_prompt": "You are an assistant."}
    sample_agent_id = "7ad24396-b822-4dca-871a-be9cc4781cf9"
    
    # This will trigger our safety validation check block automatically
    compile_deployment_session_handshake(agent_id=sample_agent_id, inline_config_dict=sample_inline_data)
  
