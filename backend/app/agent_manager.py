import os
import httpx
from typing import Dict, Any

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
BASE_URL = "https://assemblyai.com"

headers = {
    "Authorization": ASSEMBLYAI_API_KEY,
    "Content-Type": "application/json"
}

def create_new_voice_feature_agent(agent_config: Dict[str, Any]) -> str:
    """Automates creation of a brand new real-time voice feature matrix"""
    with httpx.Client() as client:
        response = client.post(BASE_URL, headers=headers, json=agent_config)
        response.raise_for_status()
        agent_data = response.json()
        print(f"🚀 SUCCESS: Stored Agent Created with ID: {agent_data['id']}")
        return agent_data["id"]

def update_active_voice_agent(agent_id: str, updated_fields: Dict[str, Any]):
    """Dynamically scales or modifies an agent's prompt, tools, or language sets instantly"""
    url = f"{BASE_URL}/{agent_id}"
    with httpx.Client() as client:
        response = client.put(url, headers=headers, json=updated_fields)
        response.raise_for_status()
        print(f"🔄 SUCCESS: Agent {agent_id} updated perfectly with new features.")
