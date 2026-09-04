import json

def validate_mid_session_update_mutability(incoming_update_json, is_session_ready=True):
    print("=================================================================")
    print("MODULE: MID-SESSION UPDATE MUTABILITY POLICING SYSTEM")
    print("=================================================================")
    print("Evaluating delta property mutations against Page 33 Handshake rules...")

    try:
        payload = json.loads(incoming_update_json)
    except json.JSONDecodeError:
        print("Error: Invalid JSON string payload syntax.")
        return False

    session_delta = payload.get("session", {})

    # 1. Check for mutual exclusion traps upfront
    if "agent_id" in session_delta and len(session_delta.keys()) > 1:
        print("Configuration Exception: 'agent_id' is strictly MUTUALLY EXCLUSIVE with inline parameters.")
        return False

    # 2. Define immutable properties as specified on Page 33
    immutable_fields = ["greeting"]
    immutable_output_fields = ["voice", "format"]

    if is_session_ready:
        print("ℹ️Session State: [READY]. Checking for immutable field violations...")
        
        # Check top-level immutable blocks
        for field in immutable_fields:
            if field in session_delta:
                print(f"session.error [immutable_field]: Modification to 'session.{field}' is FORBIDDEN after session.ready.")
                return False
                
        # Check nested output immutable arrays
        output_block = session_delta.get("output", {})
        for out_field in immutable_output_fields:
            if out_field in output_block:
                print(f"session.error [immutable_field]: Modification to 'session.output.{out_field}' is FORBIDDEN after session.ready.")
                return False

    print("\n=================================================================")
    print("COMPLIANCE STATUS: Delta update passed mutability validations.")
    print("=================================================================")
    print("Execution Rule Met: Modified properties can safely stream downstream.")
    return True

if __name__ == "__main__":
    # Test simulation: client attempts an invalid mutation by modifying the voice mid-call
    invalid_mid_call_update = """
    {
      "type": "session.update",
      "session": {
        "system_prompt": "Updated behavior prompt.",
        "output": {
          "voice": "george"
        }
      }
    }
    """
    # This will trigger our safety validation check block automatically
    validate_mid_session_update_mutability(invalid_mid_call_update, is_session_ready=True)
  
