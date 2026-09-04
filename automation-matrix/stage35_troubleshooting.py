import base64
import json

def diagnose_voice_agent_exception(error_event_json=None, ws_close_code=None):
    print("=================================================================")
    print("MODULE: AUTOMATED ARCHITECTURAL TROUBLESHOOTING TELEMETRY")
    print("=================================================================")
    print("Evaluating error conditions against Page 35 reference matrices...")

    # 1. Evaluate explicit WebSocket infrastructure close codes [INDEX: 0.1.62]
    if ws_close_code is not None:
        if ws_close_code == 1008:
            print("Telemetry Alert: [Close Code 1008 - Policy Violation]")
            print("Cause: API key or bearer session token is missing, expired, or invalid.")
            print("Fix: Fetch a fresh token immediately before each connection loop.")
            return "REFRESH_AUTH_TOKEN"
        elif ws_close_code == 1006:
            print("Telemetry Alert: [Close Code 1006 - Abnormal Disconnect]")
            print("Cause: Likely token expiry or network drop before handshake established.")
            return "CHECK_NETWORK_OR_TOKEN"

    # 2. Evaluate runtime session error responses [INDEX: 0.1.61, 0.1.63]
    if error_event_json:
        try:
            event = json.loads(error_event_json)
            code = event.get("code")
            
            if code == "invalid_audio":
                print("Telemetry Alert: [session.error - invalid_audio]")
                print("Cause: Failed base64 decode or non-PCM16 little-endian constraints.")
                print("Fix: Confirm audio is raw bytes, int16 mono, 24kHz, stripped of WAV headers.")
                return "FIX_AUDIO_ENCODING"
            elif code in ["session_not_found", "session_expired"]:
                print(f"Telemetry Alert: [session.error - {code}]")
                print("Cause: Reconnection failed because the 30-second billable grace window elapsed.")
                print("Fix: Fall back immediately. Start a fresh connection without session.resume.")
                return "START_FRESH_SESSION"
        except json.JSONDecodeError:
            pass

    print("System Health Normal. No active pipeline faults identified.")
    return "STATUS_OK"

if __name__ == "__main__":
    # Test simulation: intercepting an expired session recovery frame [INDEX: 0.1.63]
    mock_error_frame = '{"type": "session.error", "code": "session_expired", "detail": "Session grace elapsed."}'
    diagnose_voice_agent_exception(error_event_json=mock_error_frame)
  
