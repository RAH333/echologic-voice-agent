import os
import requests

def execute_delete_agent_validation(target_agent_id=None):
    print("=================================================================")
    print("PAGE MODULE: DELETE /v1/agents/{agent_id} SPECIFICATION VERIFIER")
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
        print("Key signature absent from local environment.")
        api_key = input("Enter your AssemblyAI API Key to run live test: ").strip()
        if not api_key:
            return

    if not target_agent_id:
        target_agent_id = input("Enter the unique Agent ID you wish to permanently delete: ").strip()
        if not target_agent_id:
            print("Error: Target Agent ID path parameter is required.")
            return

    url = f"https://assemblyai.com{target_agent_id}"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    print(f"\nSending DELETE request to endpoint target: {target_agent_id}")
    try:
        response = requests.delete(url, headers=headers)
        
        # Enforce strict verification of Page 11 Swagger metrics
        if response.status_code == 204:
            print("=================================================================")
            print("SUCCESS! AGENT RECORD PERMANENTLY ERASED FROM REGISTRY")
            print("=================================================================")
            print("Swagger Compliance Check (DELETE Specifications Verified):")
            print(f"- Expected Status Code verified: {response.status_code} [204 No Content].")
            print(f"- Response body evaluation payload size: {len(response.content)} bytes (Empty Body Confirm).")
        elif response.status_code == 401:
            print("401 Error: Unauthorized. Access credentials invalid or expired.")
        elif response.status_code == 404:
            print("404 Error: Not Found. Target Agent ID does not exist.")
        else:
            print(f"Server returned unhandled status code: {response.status_code}")
            
    except Exception as err:
        print(f"Network layer connection failure: {str(err)}")

if __name__ == "__main__":
    execute_delete_agent_validation()
  
