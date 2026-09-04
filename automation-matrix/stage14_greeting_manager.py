import os
import requests
import json

def configure_agent_greeting_matrix():
    print("=================================================================")
    print("MODULE: REAL-TIME TTS GREETING PROVISIONING SYSTEM")
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
        print("Key signature absent from local environment data.")
        api_key = input("Enter your AssemblyAI API Key: ").strip()
        if not api_key: return

    agent_id = input("Enter the unique Agent ID you wish to update: ").strip()
    if not agent_id:
        print("❌ Error: Target Agent ID parameter is required.")
        return

    print("\nSelect a Greeting Execution Mode:")
    print(" 1) Inject Direct Spoken Greeting (Agent Speaks First)")
    print(" 2) Omit Greeting / Listen First (User Speaks First, ideal for IVRs)")
    print("-----------------------------------------------------------------")
    choice = input("Choose option index [1-2]: ").strip()

    if choice == "1":
        print("\nNote: Do not write meta-instructions. Type the exact spoken text.")
        greeting_text = input("Enter greeting string: ").strip()
        payload = {"greeting": greeting_text}
    elif choice == "2":
        print("Setting greeting parameter to null. Agent will listen first...")
        payload = {"greeting": None}
    else:
        return

    url = f"https://assemblyai.com{agent_id}"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.put(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("\n=================================================================")
            print("SUCCESS! GREETING PROFILE SYNCED WITH CLOUD TTS PIPELINE")
            print("=================================================================")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Execution Failure: {response.status_code} - {response.text}")
    except Exception as err:
        print(f"Network layer connection failure: {str(err)}")

if __name__ == "__main__":
    configure_agent_greeting_matrix()
  
