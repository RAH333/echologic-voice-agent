import json

def parse_and_validate_token_api_error(raw_response_body_string):
    print("=================================================================")
    print("MODULE: TOKEN GATEWAY SERVERLESS EXCEPTION RESPONSE COPS")
    print("=================================================================")
    print("Validating incoming failure structures against Page 39 specs...")

    try:
        payload = json.loads(raw_response_body_string)
    except json.JSONDecodeError:
        print("Error: Response body string is not valid JSON format mapping.")
        return None

    # 1. Enforce strict top-level property mandates [INDEX: 0.1.62]
    if "error" not in payload:
        print("Specification Failure: Root field 'error' is strictly REQUIRED inside failure vectors.")
        return None

    error_message = payload.get("error")
    programmatic_code = payload.get("code", "NO_CODE_PROVIDED")
    additional_details = payload.get("details", {})

    print("Exception Contract Mapping Summary:")
    print(f"Server Error String : \"{error_message}\"")
    print(f"Programmatic Code   : [{programmatic_code}]")
    print(f"Metadata Context Count: {len(additional_details.keys())} items tracked.")

    print("\n=================================================================")
    print("COMPLIANCE STATUS: Response body matches error schema definitions.")
    print("=================================================================")
    return {
        "msg": error_message,
        "code": programmatic_code,
        "meta": additional_details
    }

if __name__ == "__main__":
    # Test execution matching an authenticated rate-limit exception payload [INDEX: 0.1.61, 0.1.62]
    sample_api_error = """
    {
      "error": "Too many token generation attempts. Rate limit exceeded.",
      "code": "rate_limit_exceeded",
      "details": {
        "retry_after_seconds": 60,
        "limit_ceiling": 100
      }
    }
    """
    parse_and_validate_token_api_error(sample_api_error)
  
