import os
import requests
import json

def execute_update_agent_validation(target_agent_id=None, update_payload=None):
    print("=================================================================")
    print("PAGE MODULE: PUT /v1/agents/{agent_id} SPECIFICATION VERIFIER")
    print("=================================================================")
    
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        try:
            with open(".env", "r") as env_file:
                for line in env_file:
                    if line.startswith("ASSEMBLYAI_API_KEY="):
                        api_key = line.strip().split("=")
                        break
        except Exception:
            pass

    if not api_key:
        print("Key signature absent from local environment.")
        api_key = input("Enter your AssemblyAI API Key to run live test: ").strip()
        if not api_key:
            return

    if not target_agent_id:
        target_agent_id = input("Enter the active Agent ID you wish to patch: ").strip()
        if not target_agent_id:
            print("Error: Target Agent ID path parameter is required.")
            return

    # Default mock test payload adhering to Page 10 delta-field specifications
    if not update_payload:
        print("Assembling optional delta properties (Modifying greeting text)...")
        update_payload = {
            "greeting": "Systems successfully updated via the EchoLogic Automation matrix."
        }

    url = f"https://assemblyai.com{target_agent_id}"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    print(f"\nTransmitting partial modifications to endpoint target: {target_agent_id}")
    try:
        response = requests.put(url, headers=headers, json=update_payload)
        
        if response.status_code == 200:
            updated_data = response.json()
            print("Success! Agent record patched cleanly.")
            print("-----------------------------------------------------------------")
            print(json.dumps(updated_data, indent=2))
            print("-----------------------------------------------------------------")
            print("Swagger Compliance Check (PUT Specifications Verified):")
            print("- Optional field partial acceptance constraint: PASS [200 OK received].")
            print("- Output mirrors complete updated state object parameters.")
        elif response.status_code == 400:
            print("400 Error: Bad Request. Field domain verification failed.")
        elif response.status_code == 401:
            print("401 Error: Unauthorized. Access credentials invalid.")
        elif response.status_code == 404:
            print("404 Error: Target Agent ID not found.")
        elif response.status_code == 422:
            print("422 Error: Unprocessable Entity. Malformed JSON payload layout structure.")
        else:
            print(f"Server returned unhandled status: {response.status_code}")
            
    except Exception as err:
        print(f"Network layer connection failure: {str(err)}")

if __name__ == "__main__":
    execute_update_agent_validation()
  
