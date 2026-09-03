# echologic-voice-agent
An autonomous, real-time voice agent built with AssemblyAI's Voice Agent API, WebSocket streaming, Next.js, and FastAPI for intelligent tool calling.

graph TD
    User([🗣️ User Audio Input]) -->|WebSockets / Microphone| FE[💻 Next.js Frontend Client]
    FE -->|Streaming Audio / Binary| AAI_API{🎙️ AssemblyAI Voice Agent API}
    
    subgraph AssemblyAI Pipeline
        AAI_API -->|Real-time STT / Universal-3 Pro| LLM[🧠 LLM Routing & Voice Layout]
        LLM -->|Identify Action Needed| ToolsCall[🛠️ JSON-Schema Tool Calling]
    end

    ToolsCall -->|Secure Webhook Request| BE[⚙️ FastAPI Backend Server]
    BE -->|Execute Local Action / DB Query| BE
    BE -->|JSON Response Context| ToolsCall
    
    LLM -->|Synthesized TTS Response| FE
    FE -->|🔊 Low-Latency Audio Playback| User
    
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
