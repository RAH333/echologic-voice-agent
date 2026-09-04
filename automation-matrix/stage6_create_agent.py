import os
import sys
import requests
import json

def run_agent_creation_pipeline():
    print("=================================================================")
    print("MODULE: REST API STORED AGENT COMPONENT CREATOR")
    print("=================================================================")

    # 1. Autodetect keys securely from local repository configurations
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        # Fall back to checking the primary repository hidden .env layout file
        try:
            with open(".env", "r") as env_file:
                for line in env_file:
                    if line.startswith("ASSEMBLYAI_API_KEY="):
                        api_key = line.strip().split("=")[1]
                        break
        except FileNotFoundError:
            pass

    if not api_key:
        print("Security profile token missing from environment.")
        api_key = input("Please paste your AssemblyAI API Secret Key: ").strip()

    if not api_key:
        print("Error: API Key is required to compile endpoints. Aborting.")
        return

    # 2. Build the exact full-page JSON payload blueprint from the specification sheet
    agent_blueprint = {
        "name": "EchoLogic Support Assistant",
        "system_prompt": "You are an expert real-time voice operations assistant. Keep your replies friendly, precise, and under two short sentences. Answer what was asked, lead with the direct answer, and skip the preamble. No exclamation marks.",
        "greeting": "System initialized. EchoLogic operational node standing by, how can I help you today?",
        "voice": {
            "voice_id": "alba"
        },
        "input": {
            "format": { "encoding": "audio/pcm", "sample_rate": 24000 },
            "keyterms": ["AssemblyAI", "Universal-3", "EchoLogic", "Vercel Gateway"],
            "turn_detection": {
                "vad_threshold": 0.5,
                "min_silence": 1400,
                "max_silence": 4000,
                "interrupt_response": True
            }
        },
        "output": {
            "voice": "alba",
            "format": { "encoding": "audio/pcm", "sample_rate": 24000 },
            "volume": 100
        },
        "tools": [
            {
                "name": "get_weather",
                "description": "Get current weather conditions for an exact coordinate location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "latitude": { "type": "number" },
                        "longitude": { "type": "number" }
                    },
                    "required": ["latitude", "longitude"]
                },
                "http": {
                    "url": "https://example.com",
                    "http_method": "GET"
                }
            }
        ],
        "llm": [
            {
                "base_url": "https://assemblyai.com",
                "model": "claude-sonnet-4-6",
                "api_key": api_key
            }
        ]
    }

    # 3. Transmit the payload securely to the AssemblyAI infrastructure servers
    url = "https://assemblyai.com"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    print("\nTransmitting configuration blueprint payload to AssemblyAI cloud...")
    try:
        response = requests.post(url, headers=headers, json=agent_blueprint)
        response.raise_for_status()
        response_data = response.json()
        
        generated_agent_id = response_data.get("id")
        print("\n=================================================================")
        print("SUCCESS! BLUAPRINT DEPLOYED AND AGENT SECURELY CREATED")
        print("=================================================================")
        print(f"Stored Agent ID: {generated_agent_id}")
        print("-----------------------------------------------------------------")
        print("You can now deploy this exact ID anywhere: across your frontend,")
        print("   your Vercel serverless configurations, or your Twilio phone number.")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"REST API Compilation Failure: {http_err}")
        if response.text:
            print(f"📋 Server details: {response.text}")
    except Exception as err:
        print(f"Execution error: {str(err)}")

if __name__ == "__main__":
    run_agent_creation_pipeline()
  
