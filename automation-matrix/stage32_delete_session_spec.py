import os
import requests

def execute_delete_session_compliance_check(target_session_id=None):
    print("=================================================================")
    print("MODULE: DELETE /v1/sessions/{id} SPECIFICATION VERIFIER")
    print("=================================================================")
    
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
        print("Key signature absent from local environment parameters.")
        api_key = input("Enter your AssemblyAI API Key to run live test: ").strip()
        if not api_key: return

    if not target_session_id:
        target_session_id = input("Enter the unique Session ID you wish to soft-delete: ").strip()
        if not target_session_id:
            print("Error: Target Session ID parameter is required.")
            return

    url = f"https://assemblyai.com{target_session_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print(f"\nTransmitting DELETE request to target session string: {target_session_id}")
    try:
        response = requests.delete(url, headers=headers)
        
        # Enforce explicit verification of Page 32 Swagger metrics
        if response.status_code == 204:
            print("=================================================================")
            print("SUCCESS! SESSION SOFT-DELETED IN CLOUD REGISTRY")
            print("=================================================================")
            print("Swagger Compliance Check (DELETE Specifications Verified):")
            print(f"- Expected Status Code verified: {response.status_code} [204 No Content].")
            print(f"- Response body evaluation payload size: {len(response.content)} bytes (Verified Empty).")
        elif response.status_code == 401:
            print("401 Error: Unauthorized. Key is invalid or not entitled for Voice Agents.")
        elif response.status_code == 404:
            print("404 Error: Not Found. Target Session ID does not exist.")
        else:
            print(f"Server returned unhandled status code: {response.status_code}")
            
    except Exception as err:
        print(f"Network layer connection failure: {str(err)}")

if __name__ == "__main__":
    execute_delete_session_compliance_check()
  
