import json

def validate_token_request_parameters(expires_in_seconds, max_session_duration_seconds=10800):
    print("=================================================================")
    print("MODULE: VOICE AGENT DYNAMIC TOKEN SECURITY POLICING ENGINE")
    print("=================================================================")
    print("Validating transaction bounds against Page 38 OpenAPI schema...")

    # 1. Enforce token redemption window integer bounds [INDEX: 0.1.68]
    if not (1 <= expires_in_seconds <= 600):
        print(f"Range Exception: Token expiry window [{expires_in_seconds}s] out of bounds.")
        print("Constraint requirement: Must be an integer value between 1 and 600 seconds.")
        return False

    # 2. Enforce total call session duration limits [INDEX: 0.1.68, 0.1.69]
    if not (60 <= max_session_duration_seconds <= 10800):
        print(f"Range Exception: Session cap [{max_session_duration_seconds}s] out of bounds.")
        print("Constraint requirement: Must be an integer value between 60 and 10800 seconds.")
        return False

    print("Parameter Compliance Mapping Summary:")
    print(f"Redemption Gate Limit : {expires_in_seconds} seconds [VALID]")
    print(f"Max Call Run Duration : {max_session_duration_seconds} seconds [VALID]")
    
    print("\n=================================================================")
    print("COMPLIANCE STATUS: Parameters match token swagger requirements.")
    print("=================================================================")
    print("Client Lifecycle Warning: There is no 'closing soon' warning event.")
    print("   You must run a local timer script loop to gracefully drop state.")
    return True

if __name__ == "__main__":
    # Test simulation matching standard operational limits [INDEX: 0.1.68]
    validate_token_request_parameters(expires_in_seconds=300, max_session_duration_seconds=3600)
