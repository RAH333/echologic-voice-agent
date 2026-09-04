import os
import requests
import json

def fetch_master_key():
    # Attempt to automatically locate keys from local workspace .env configurations
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        try:
            with open(".env", "r") as env_file:
                for line in env_file:
                    if line.startswith("ASSEMBLYAI_API_KEY="):
                        return line.strip().split("=")[1]
        except FileNotFoundError:
            pass
    return api_key

def manage_agents_lifecycle():
    api_key = fetch_master_key()
    if not api_key:
        print("Security profile token missing from environment data.")
        api_key = input("Please paste your AssemblyAI API Secret Key: ").strip()
        if not api_key:
            return

    base_url = "https://assemblyai.com"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    while True:
        print("\n=================================================================")
        print("PAGE MODULE: REUSABLE VOICE AGENT MANAGEMENT CENTER (REST)")
        print("=================================================================")
        print(" 1) [POST]   Create a Stored Support Agent Object")
        print(" 2) [GET]    List All Active Agent ID & Name Summaries")
        print(" 3) [GET ID] Retrieve Full Configuration Fields for an Agent")
        print(" 4) [PUT]    Update Specific Properties on a Live Agent")
        print(" 5) [DELETE] Wipe an Agent Permanent out of Cloud Registry")
        print(" 6) Back Out to Master Launcher Control Room")
        print("-----------------------------------------------------------------")
        try:
            choice = int(input("Select REST method action [1-6]: "))
        except ValueError:
            continue

        if choice == 1:
            payload = {
                "name": "EchoLogic Support Assistant",
                "system_prompt": "You are a friendly operational voice support agent.",
                "greeting": "Hi, welcome to the EchoLogic hub. How can I help you?",
                "voice": { "voice_id": "alba" }
            }
            resp = requests.post(base_url, headers=headers, json=payload)
            print(f"\nResponse Status: {resp.status_code}")
            print(json.dumps(resp.json(), indent=2))

        elif choice == 2:
            resp = requests.get(base_url, headers=headers)
            print(f"\nResponse Status: {resp.status_code}")
            print(json.dumps(resp.json(), indent=2))

        elif choice == 3:
            agent_id = input("Enter the target Agent ID to retrieve: ").strip()
            if agent_id:
                resp = requests.get(f"{base_url}/{agent_id}", headers=headers)
                print(f"\nResponse Status: {resp.status_code}")
                print(json.dumps(resp.json(), indent=2))

        elif choice == 4:
            agent_id = input("Enter the target Agent ID to modify: ").strip()
            if agent_id:
                print("Updating greeting field as defined in documentation spec...")
                payload = { "greeting": "Thanks for calling Acme. What can I do for you?" }
                resp = requests.put(f"{base_url}/{agent_id}", headers=headers, json=payload)
                print(f"\nResponse Status: {resp.status_code}")
                print(json.dumps(resp.json(), indent=2))

        elif choice == 5:
            agent_id = input("WARNING: Enter Agent ID to permanently delete: ").strip()
            if agent_id:
                resp = requests.delete(f"{base_url}/{agent_id}", headers=headers)
                print(f"\nResponse Status: {resp.status_code} (204 means successful deletion)")

        elif choice == 6:
            break

if __name__ == "__main__":
    manage_agents_lifecycle()
  
