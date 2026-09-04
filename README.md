# echologic-voice-agent
An autonomous, real-time voice agent built with AssemblyAI's Voice Agent API, WebSocket streaming, Next.js, and FastAPI for intelligent tool calling.

graph TD
    User([User Audio Input]) -->|WebSockets / Microphone| FE[Next.js Frontend Client]
    FE -->|Streaming Audio / Binary| AAI_API{AssemblyAI Voice Agent API}
    
    subgraph AssemblyAI Pipeline
        AAI_API -->|Real-time STT / Universal-3 Pro| LLM[LLM Routing & Voice Layout]
        LLM -->|Identify Action Needed| ToolsCall[JSON-Schema Tool Calling]
    end

    ToolsCall -->|Secure Webhook Request| BE[FastAPI Backend Server]
    BE -->|Execute Local Action / DB Query| BE
    BE -->|JSON Response Context| ToolsCall
    
    LLM -->|Synthesized TTS Response| FE
    FE -->|Low-Latency Audio Playback| User
    
```
echologic-voice-agent/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   └── tools.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   └── components/
│   │       └── VoiceInterface.tsx
│   ├── package.json
│   ├── next.config.js
│   └── vercel.json
├── .gitignore
└── README.md
```
```
echologic-voice-agent/                 <-- Root folder of your custom GitHub Repository
│
├── .github/
│   └── workflows/
│       └── deploy.yml                 # CI/CD file to validate compiling states
│
├── backend/                           # Your Python Fulfillment System
│   ├── app/
│   │   ├── __init__.py                # Package initializer file
│   │   ├── config.py                  # Pydantic global environment variables settings
│   │   ├── main.py                    # FastAPI server entry point and endpoint routers
│   │   └── tools.py                   # Custom tool schema execution declarations
│   ├── Dockerfile                     # Container instructions for your backend cloud server
│   └── requirements.txt               # Backend Python dependency listing
│
├── frontend/                          # Your Vercel Next.js User Interface
│   ├── public/                        # Static assets, icons, and logos
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx             # Main HTML framing wrapper component
│   │   │   └── page.tsx               # Primary user-facing dashboard template
│   │   ├── components/
│   │   │   └── VoiceInterface.tsx     # The interactive WebSockets mic control center
│   │   └── config/
│   │       └── env.ts                 # Dynamic URL router matching Vercel to your backend
│   ├── next.config.js                 # Core configurations for Next.js execution loops
│   ├── package.json                   # Node.js third-party package dependencies mapping
│   └── vercel.json                    # Configuration variables telling Vercel how to compile
│
├── automation-matrix/                 # 📁 THE AUTOMATION MODULE CONTAINER FOLDER
│   ├── stage1_setup.sh                # Script: Handles side-by-side repo cloning & npm installs
│   ├── stage2_twilio.sh               # Script: Handles interactive phone & SIP trunk credentials
│   └── stage3_agent_api.sh            # Script: Handles advanced AssemblyAI streaming adjustments
│
├── .gitignore                         # Protects keys (.env) and excludes massive cache folders
├── README.md                          # Interactive documentation containing your system flowchart
└── run_orchestrator.sh                # 🎛️ THE MASTER MANAGER LAUNCHER SCRIPT

```
```
echologic-voice-agent/                 <-- 🌿 Your Custom GitHub Repository Branch
│
├── .github/workflows/
│   └── deploy.yml                     # Validates compiling build states on push
│
├── backend/                           # Your Python Tool Fulfillment Microservice
│   ├── app/
│   │   ├── __init__.py                
│   │   ├── config.py                  # Pydantic global environment variables settings
│   │   ├── main.py                    # FastAPI server entry point and endpoint routers
│   │   └── tools.py                   # Automated tool schema execution declarations
│   ├── Dockerfile                     # Container instructions for your backend cloud server
│   └── requirements.txt               # Backend Python dependency listing
│
├── frontend/                          # Your Vercel Next.js User Interface
│   ├── public/                        
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx             # Main HTML framing wrapper component
│   │   │   └── page.tsx               # Primary user-facing dashboard template
│   │   ├── components/
│   │   │   └── VoiceInterface.tsx     # The interactive WebSockets mic control center
│   │   └── config/
│   │       └── env.ts                 # Dynamic URL router matching Vercel to your backend
│   ├── next.config.js                 
│   ├── package.json                   # Node.js third-party package dependencies mapping
│   └── vercel.json                    # Configuration variables telling Vercel how to compile
│
├── automation-matrix/                 # 📁 INDEPENDENT FULL-PAGE CODE SEGMENTS
│   ├── stage1_get_started.sh          # [Page 1] Core Clone, Dependency Setup & Start
│   ├── stage2_voice_agent_api.sh      # [Page 2] Architectural Flow & Overview Logs
│   ├── stage3_build_with_ai.sh        # [Page 3] Enforce Initial Audio & AEC Parameters
│   ├── stage4_supported_languages.sh  # [Page 4] Provision Universal-3.5 Multi-Accents
│   ├── stage5_create_agent.sh         # [Page 5] Deploy Full Configuration JSON Body
│   ├── stage6_manage_agents.py        # [Page 6] Walkthrough Full CRUD REST Endpoints
│   ├── stage7_create_agent_spec.py    # [Page 7] Run OpenAPI Creation Schema Checker
│   ├── stage8_list_agents_spec.py     # [Page 8] Fetch Account Registry Agent Lists
│   ├── stage9_retrieve_agent_spec.py   # [Page 9] Inspect Masked Write-Only Token Headers
│   ├── stage10_update_agent_spec.py   # [Page 10] Transmit Optional Delta-Field Patches
│   ├── stage11_delete_agent_spec.py   # [Page 11] Verify REST 204 Empty Body Success Codes
│   ├── stage12_connect_your_own_llm.py # [Page 12] Configure Custom HTTPS Model Gateways
│   ├── stage13_prompting_guide.py     # [Page 13] Structural Prompt Builders (No-Hedges)
│   ├── stage14_greeting_manager.py    # [Page 14] Manage Direct Immutable TTS Hello Strings
│   ├── stage15_tools_core_framework.py # [Page 15] Validate Hold vs Interactive Latencies
│   ├── stage16_http_tools_server_side.py # [Page 16] Manage Server-Side 8 KiB Body Limits
│   ├── stage17_client_side_function_tools.py # [Page 17] Run Sequential reply.done Idle Loops
│   ├── stage18_voices_and_accents.py  # [Page 18] Inspect British vs American Dialects
│   ├── stage19_output_volume.py       # [Page 19] Enforce Mutable 0-100 Audio Scaling
│   ├── stage20_turn_detection_spec.py # [Page 20] Dynamic Transcription Mode Toggling
│   ├── stage21_transcription_context.py # [Page 21] Inject Keyterms Vocabulary Boosts
│   ├── stage22_steer_known_languages.py # [Page 22] Constrain ISO Multi-lingual Pining
│   ├── stage23_isolate_callers_voice.py # [Page 23] Near vs Far-Field Suppressions
│   ├── stage24_deploy_your_agent.py   # [Page 24] Mutual Exclusion Validation Handshakes
│   ├── stage25_browser_integration.js # [Page 25] Token Minting & Linear Resample Worklets
│   ├── stage26_twilio_sip_telephony.py # [Page 26] Twilio Inbound Numbers & Trunk Setup
│   ├── stage27_audio_format.py        # [Page 27] Base64 PCM16 Little-Endian 24kHz Sync
│   ├── stage28_bluejay_simulations.py # [Page 28] CHIRP Audio Pacing 200ms Gating Locks
│   ├── stage29_recordings_and_transcripts.py # [Page 29] pre-signed Artifact Downloads & S3 links
│   ├── stage30_list_sessions_spec.py  # [Page 30] SessionListItem Schema Verification
│   ├── stage31_retrieve_session_spec.py # [Page 31] SessionResponse Enum Mapping Checking
│   ├── stage32_delete_session_spec.py # [Page 32] 204 Soft Deletion Response Testers
│   ├── stage33_inline_configuration.py # [Page 33] WebSocket Mutability Validation Matrix
│   ├── stage34_events_reference.py    # [Page 34] Non-Incremental Text Replacement
│   ├── stage35_troubleshooting.py     # [Page 35] AEC Feedback & PortAudio Exception Fixes
│   ├── stage36_message_sequence.py    # [Page 36] Canonical WebSocket Loop State Machine
│   ├── stage37_websocket_asyncapi_spec.py # [Page 37] Bearer Auth vs ?token= Upgrade Constraints
│   ├── stage38_generate_token_spec.py # [Page 38] Token Redemption Window Hard Bounds
│   └── stage39_token_error_spec.py    # [Page 39] Programmatic code Error Payload Parsing
│
├── .gitignore                         # Protects keys (.env) and excludes massive cache folders
├── README.md                          # Interactive documentation containing your system flowchart
└── run_orchestrator.sh                # 🎛️ THE CENTRAL MASTER COMPOSABLE AUTOMATION HUB
```

# EchoLogic AI — Voice Agent Platform

An autonomous, low-latency operational voice agent workspace built for field engineers using **AssemblyAI's Voice Agent API**, **Universal-3 Pro Streaming STT**, **FastAPI**, and **Next.js**, deployed effortlessly via **Vercel**.

## System Pipeline Flowchart

```mermaid
graph TD
    User([User Audio Input]) -->|WebSockets / Microphone| FE[Next.js Frontend Client]
    FE -->|Streaming Audio / Binary| AAI_API{AssemblyAI Voice Agent API}
    
    subgraph AssemblyAI Cloud Pipeline
        AAI_API -->|Real-time STT / Universal-3 Pro| LLM[LLM Routing & Voice Layout]
        LLM -->|Identify Action Needed| ToolsCall[JSON-Schema Tool Calling]
    end

    ToolsCall -->|Secure Webhook Request| BE[FastAPI Backend Server]
    BE -->|Execute Local Action / DB Query| BE
    BE -->|JSON Response Context| ToolsCall
    
    LLM -->|Synthesized TTS Response| FE
    FE -->|Low-Latency Audio Playback| User
```

---

## Fast-Track First Time Installation

If you are cloning or downloading this repository workspace for the very first time, run our completely automated configuration controller sequence to link your API secrets and install code dependencies across the ecosystem.

```bash
# 1. Give execution clearance permissions to the engine automation file
chmod +x setup.sh

# 2. Run the interactive deployment orchestrator script
./setup.sh
```
*The installer tool will automatically prompt you for your keys and safely write your environment configs across directories without errors.*

---

## Daily Startup Routine (Subsequent Runs)

Once you have completed the automated installation phase using `./setup.sh` above, **do not run the setup routine again.** Simply use the runtime scripts below to initiate the local execution servers immediately:

### Step 1: Fire Up Your Tool Fulfillment Engine (Backend)
Open a fresh root terminal path and launch your Python server environment:
```bash
# Enter backend folder space
cd backend

# Engage your insulated python runtime loop
source venv/bin/activate

# Execute production local hot-reloader 
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Step 2: Fire Up Your Interactive Operator Interface (Frontend)
Open a separate terminal window and launch your UI development workspace:
```bash
# Enter frontend visual project folder space
cd frontend

# Engage local web execution loop
npm run dev
```
Open your secure web space browser interface at `http://localhost:3000` to interact directly with your workspace portal!

## 🎛️ Automated Development & Deployment Launcher

This repository includes a modular automation framework located right in the codebase directory. Users do not need to install tools manually or handle complex global path variables.

### How to Download and Run (For Your Team & Judges)
```bash
# 1. Clone your main custom project repository
git clone https://github.com

# 2. Open the project folder
cd echologic-voice-agent

# 3. Grant administrative execution privileges to the launcher tool
chmod +x run_orchestrator.sh

# 4. Fire up the dashboard menu to choose your setup module
./run_orchestrator.sh
```

### Code Segment Checklist
- **Stage 1:** Clones official helper templates right next to this project directory, injects keys, and compiles workspace dependencies.
- **Stage 2:** Configures optional cellular network endpoints and connects active phone routing channels.
- **Stage 3 (Agent API Segment):** Configures streaming web-socket properties, modifies real-time audio thresholds, and updates server parameters.

# EchoLogic AI Framework Console 🎙️

Welcome to the unified core repository platform for EchoLogic AI. Our architecture includes an active, composable automation dashboard that maps 39 core documentation pages 1-to-1 onto isolated, zero-error test modules.

## ⚡ Setup and Operation Instructions

To launch the multi-stage developer control room and evaluate any documentation segment safely, run this single root-level orchestrator:

```bash
# 1. Access your local custom cloned feature directory branch
cd echologic-voice-agent

# 2. Grant administrative script launch configuration clearance
chmod +x run_orchestrator.sh

# 3. Fire up the looping dashboard control room
./run_orchestrator.sh
```

## Multi-Stage Compilation Registry
Our architecture is organized across 39 separate script files inside the `automation-matrix/` directory. Each file completely isolates its variables, safeguarding your workspace against sequence compile bugs or out-of-order execution errors.

