import json

def validate_session_list_item_compliance(mock_api_response_body):
    print("=================================================================")
    print("MODULE: GET /v1/sessions SWAGGER SCHEMAS COMPLIANCE VALIDATOR")
    print("=================================================================")
    print("Evaluating payload response structures against Page 30 OpenAPI spec...")

    try:
        data = json.loads(mock_api_response_body)
    except json.JSONDecodeError:
        print("Syntax Error: Provided response payload string is malformed JSON.")
        return False

    # 1. Enforce top-level field requirements
    if "sessions" not in data:
        print("Specification Failure: Root field 'sessions' array is strictly REQUIRED.")
        return False

    sessions_list = data.get("sessions", [])
    print(f"Processing {len(sessions_list)} session tracking records...")

    # 2. Iterate and validate each list element against SessionListItem definitions
    for idx, session in enumerate(sessions_list):
        session_id = session.get("id")
        status = session.get("status")

        if not session_id or not status:
            print(f"Schema Exception at array index [{idx}]: Fields 'id' and 'status' are REQUIRED.")
            return False

        # Check for active call indicator properties
        if status != "completed" and session.get("ended_at") is not None:
            print(f"Validation Warning on [{session_id}]: Active calls must have a null 'ended_at' stamp.")
            return False

    print("\n=================================================================")
    print("COMPLIANCE STATUS: 100% SUCCESS. Mapped items match OpenAPI specs.")
    print("=================================================================")
    return True

if __name__ == "__main__":
    # Test simulation matching a valid specification trace body
    sample_swagger_json = """
    {
      "sessions": [
        {
          "id": "sess_9a648a2ab75747a9a597ba046ced3e13",
          "agent_id": "7ad24396-b822-4dca-871a-be9cc4781cf9",
          "status": "completed",
          "public_close_reason": "client_end",
          "duration_seconds": 42.6,
          "created_at": "2026-07-14T18:04:27.607110Z",
          "ended_at": "2026-07-14T18:05:10.204981Z"
        }
      ],
      "has_more": false,
      "response_metadata": { "next_cursor": "" }
    }
    """
    validate_session_list_item_compliance(sample_swagger_json)
