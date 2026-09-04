import os
import requests
import json

def fetch_all_completed_sessions_matrix(agent_filter_id=None):
    print("=================================================================")
    print("MODULE: HISTORICAL SESSIONS & TIMELINE EXTRACTOR")
    print("=================================================================")
    print("Initializing token-cursor pagination loop against Page 29 specs...")

    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        try:
            with open(".env", "r") as env_file:
                for line in env_file:
                    if line.startswith("ASSEMBLYAI_API_KEY="):
                        api_key = line.strip().split("=")[1]
                        break
        except Exception:
            pass

    if not api_key:
        print("Security profile token signature missing from workspace.")
        api_key = input("Enter your AssemblyAI API Key to continue: ").strip()
        if not api_key: return

    base_url = "https://assemblyai.com"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    cursor = None
    session_counter = 0
    filters = {"limit": 50, "status": "completed"}
    if agent_filter_id:
        filters["agent_id"] = agent_filter_id

    print("\nLaunching continuous network page lookups...")
    try:
        while True:
            params = filters.copy()
            if cursor:
                params["cursor"] = cursor

            response = requests.get(f"{base_url}/v1/sessions", headers=headers, params=params)
            response.raise_for_status()
            payload_page = response.json()

            sessions_array = payload_page.get("sessions", [])
            for session in sessions_array:
                session_counter += 1
                print(f"  [{session_counter}] ID: {session.get('id')} | Duration: {session.get('duration_seconds')}s | Reason: {session.get('public_close_reason')}")

            # Extract the next cursor signature exactly as taught in the spec sheet
            metadata = payload_page.get("response_metadata", {})
            cursor = metadata.get("next_cursor")

            if not payload_page.get("has_more") or not cursor:
                print("\nEND OF DATA PACKETS: All completed pages parsed cleanly.")
                break
                
    except Exception as err:
        print(f"Connection layer dropped query thread: {str(err)}")

if __name__ == "__main__":
    # Test execution running a mock page request trace
    fetch_all_completed_sessions_matrix()
  
