import os
import requests
import json

def execute_llm_override_pipeline():
    print("=================================================================")
    print("MODULE: CONNECT YOUR OWN LLM CONFIGURATION PROVISIONER")
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
        api_key = input("Enter your AssemblyAI API Key: ").strip()
        if not api_key: return

    agent_id = input("Enter the unique Agent ID you wish to re-configure: ").strip()
    if not agent_id:
        print("Error: Target Agent ID is required.")
        return

    print("\nSelect an LLM Routing Model Strategy:")
    print(" 1) Revert to AssemblyAI Managed Default Model")
    print(" 2) Route via AssemblyAI LLM Gateway (e.g., Claude Sonnet 4.6)")
    print(" 3) Bind External Custom OpenAI-Compatible Endpoint Host")
    print("-----------------------------------------------------------------")
    try:
        selection = int(input("Choose option index [1-3]: "))
    except ValueError:
        return

    llm_payload = []
    if selection == 2:
        print("Configuring direct cloud LLM Gateway proxy routes...")
        llm_payload = [{
            "base_url": "https://assemblyai.com",
            "model": "claude-sonnet-4-6",
            "api_key": api_key
        }]
    elif selection == 3:
        print("Gathering external custom server parameters...")
        custom_url = input("Enter HTTPS base URL (e.g., https://openai.com): ").strip()
        custom_model = input("Enter model name (e.g., gpt-5-mini): ").strip()
        custom_key = input("Enter provider secret API key: ").strip()
        
        if not custom_url.startswith("https://"):
            print("Validation Exception: Custom endpoints must use secure HTTPS protocol layouts.")
            return
            
        llm_payload = [{
            "base_url": custom_url,
            "model": custom_model,
            "api_key": custom_key
        }]
    elif selection == 1:
        print("Clearing custom structures. Reverting to factory managed engine.")
        llm_payload = []

    url = f"https://assemblyai.com{agent_id}"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.put(url, headers=headers, json={"llm": llm_payload})
        if response.status_code == 200:
            print("\n=================================================================")
            print("SUCCESS! CONVERSATIONAL BRAIN COMPLEMENTED")
            print("=================================================================")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Execution Failure: {response.status_code} - {response.text}")
    except Exception as err:
        print(f"Network layer connection failure: {str(err)}")

if __name__ == "__main__":
    execute_llm_override_pipeline()
