import os
import sys
from backend.app.agent_manager import create_new_voice_feature_agent

# Standard optimized Voice Feature Blueprint from your documentation guidelines
HACKATHON_AGENT_BLUEPRINT = {
    "name": "EchoLogic Core Matrix Agent",
    "system_prompt": "You are a senior automated real-time voice guide. Speak naturally. Never read out structural markdown or code signatures.",
    "greeting": "System online. Real-time voice feature automation matrix is ready. How can I help you scale today?",
    "voice": { "voice_id": "alba" },
    "input": {
        "format": { "encoding": "audio/pcm", "sample_rate": 24000 },
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
            "name": "query_system_status",
            "description": "Check the core automated staging parameters of the deployment pipeline.",
            "parameters": {
                "type": "object",
                "properties": {
                    "matrix_stage": { "type": "integer", "examples": [15] }
                },
                "required": ["matrix_stage"]
            }
        }
    ],
    "llm": [
        {
            "base_url": "https://assemblyai.com",
            "model": "claude-sonnet-4-6",
            "api_key": os.getenv("ASSEMBLYAI_API_KEY")
        }
    ]
}

if __name__ == "__main__":
    if not os.getenv("ASSEMBLYAI_API_KEY"):
        print("ERROR: Missing ASSEMBLYAI_API_KEY env parameter.")
        sys.exit(1)
    
    print("Initializing automatic voice architecture generation...")
    agent_id = create_new_voice_feature_agent(HACKATHON_AGENT_BLUEPRINT)
    
    # Save the generated agent ID to a local configuration file for the web client to ingest
    with open(".env.production", "a") as env_file:
        env_file.write(f"\nNEXT_PUBLIC_ASSEMBLYAI_AGENT_ID={agent_id}\n")
    print("Local pipeline parameters updated successfully.")
  
