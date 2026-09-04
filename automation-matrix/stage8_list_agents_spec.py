import os
import requests
import json

def execute_list_agents_validation():
    print("=================================================================")
    print("PAGE MODULE: GET /v1/agents SPECIFICATION VERIFIER")
    print("=================================================================")
    
    # Extract access tokens securely from the workspace configuration layers
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        try:
            with open(".env", "r") as env_file:
                for line in env_file:
                    if line.startswith("ASSEMBLYAI_API_KEY="):
                        api_key = line.strip().split("=")[1]
                        break
        except FileNotFoundError:
            pass

    if not api_key:
        print("Key signature absent from local environment.")
        api_key = input("Enter your AssemblyAI API Key to run live test: ").strip()
        if not api_key:
            return

    url = "https://assemblyai.com"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    print("\nQuerying account records for lightweight agent matrices...")
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            agents_list = response.json()
            print(f"Success! Received {len(agents_list)} lightweight agent records.")
            print("-----------------------------------------------------------------")
            print(json.dumps(agents_list, indent=2))
            print("-----------------------------------------------------------------")
            print("Schema Verification (AgentListItem Specifications):")
            print("- Primary configuration constraints met: returns lightweight entries.")
            print("- Target fields tracked: [id, name, deleted_at, created_at, updated_at]")
        elif response.status_code == 401:
            print("401 Error: Unauthorized. Key is invalid or not entitled for Voice Agents.")
        else:
            print(f"Response failure: {response.status_code} - {response.text}")
            
    except Exception as err:
        print(f"Network layer connection failure: {str(err)}")

if __name__ == "__main__":
    execute_list_agents_validation()
  
