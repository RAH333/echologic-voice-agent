#!/bin/bash
set -e
REPO_DIR=$1

echo "================================================================="
echo "RUNNING MODULE: ADVANCED AGENT API CODE ROUTER ACTIONS"
echo "================================================================="

cd "$REPO_DIR/.."
if [ ! -d "voice-agent-starter-js" ]; then
    echo "Operational starter templates missing. Run Stage 1 first!"
    exit 1
fi

cd "voice-agent-starter-js"

echo "Injecting Advanced Agent API streaming overrides..."
# This modifies or creates files inside the template repository to handle customized turn-taking 
# and real-time streaming sockets without requiring manual adjustments to your local environment
cat << 'EOF' > agent-api-custom-config.json
{
  "agent_features": {
    "realtime_streaming": true,
    "websocket_transport": "native",
    "audio_sample_rate": 16000,
    "turn_taking_threshold_ms": 400
  }
}
EOF

echo "Publishing newly injected Agent API configurations to cloud engine..."
npm run publish

echo "Agent API script segment configured and pushed cleanly to your project workspace!"
