#!/bin/bash
set -e
REPO_DIR=$1

echo "================================================================="
echo "MODULE: MULTILINGUAL CODE-SWITCHING VOICE PROVISIONER"
echo "================================================================="
echo "Targeting core engine: Universal-3.5 Pro Streaming Model"
echo "-----------------------------------------------------------------"
echo "Select a production language profile to apply to your Voice Agent:"
echo " 1) English Native Accent Cluster (alba, eve, george, jane, anna)"
echo " 2) Spanish Regional Accent Module (lola)"
echo " 3) Italian Regional Accent Module (giovanni)"
echo " 4) German Regional Accent Module (juergen)"
echo " 5) French Regional Accent Module (estelle)"
echo " 6) Portuguese Regional Accent Module (rafael)"
echo "================================================================="
read -p "Choose targeted output accent index [1-6]: " LANG_CHOICE

SELECTED_VOICE="anna" # Default fallback voice accent profile

case $LANG_CHOICE in
    1) SELECTED_VOICE="anna" ;;
    2) SELECTED_VOICE="lola" ;;
    3) SELECTED_VOICE="giovanni" ;;
    4) SELECTED_VOICE="juergen" ;;
    5) SELECTED_VOICE="estelle" ;;
    6) SELECTED_VOICE="rafael" ;;
    *) echo "Invalid choice. Defaulting back to base English (anna).";;
esac

cd "$REPO_DIR/.."
if [ -d "voice-agent-starter-js" ]; then
    cd "voice-agent-starter-js"
    
    echo "Updating local workspace configuration parameters..."
    # Modifies your runtime configurations with the new model settings
    cat << EOF > agents/multilingual-agent.jsonc
{
  "name": "EchoLogic Multilingual Voice Agent",
  "system_prompt": "You are an expert real-time operations assistant. Speak naturally. Use the language the user speaks.",
  "voice": { "voice_id": "$SELECTED_VOICE" },
  "greeting": "System online. Listening for incoming real-time audio streams.",
  "streaming_config": {
    "engine": "universal-3.5-pro-streaming",
    "native_code_switching": true
  }
}
EOF
    echo "Syncing new agent layout with voice target [$SELECTED_VOICE] to AssemblyAI cloud..."
    AGENT=multilingual-agent npm run publish || echo "Could not push config. Verify internet status."
else
    echo "Dependencies missing. Please run Option 1 from the main menu first!"
fi
