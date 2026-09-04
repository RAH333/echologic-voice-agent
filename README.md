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
- 
