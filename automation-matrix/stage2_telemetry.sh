#!/bin/bash
set -e
REPO_DIR=$1

echo "================================================================="
echo "RUNNING MODULE: SESSION RECONSTRUCT & TELEMETRY EXTRACTION"
echo "================================================================="

# FIX: Look cleanly inside the targeted repository directory environment layout block
if [ -f "$REPO_DIR/.env" ]; then
    API_KEY=$(grep "ASSEMBLYAI_API_KEY=" "$REPO_DIR/.env" | cut -d'=' -f2 || true)
elif [ -f "$REPO_DIR/voice-agent-starter-js/.env" ]; then
    API_KEY=$(grep "ASSEMBLYAI_API_KEY=" "$REPO_DIR/voice-agent-starter-js/.env" | cut -d'=' -f2 || true)
fi

if [ -z "$API_KEY" ]; then
    echo "Authentication profile missing from environment layout."
    read -p "Please enter your AssemblyAI API Secret Key to continue: " USER_KEY
    API_KEY="$USER_KEY"
fi

echo "-----------------------------------------------------------------"
echo "Select a Core Session Analytics Action to Execute:"
echo "-----------------------------------------------------------------"
echo " 1) Pull Modern Call Logs (List Recent 5 Voice Agent Sessions)"
echo " 2) Extract Live Audio Transcript Artifact Timeline"
echo " 3) Back Out to Core Matrix"
echo "-----------------------------------------------------------------"
read -p "Enter step operation [1-3]: " TELEMETRY_ACTION

case $TELEMETRY_ACTION in
    1)
        echo "Fetching session histories from ://assemblyai.com cloud..."
        curl -s "https://://assemblyai.com/v1/sessions?limit=5" \
          -H "Authorization: $API_KEY" | python3 -m json.tool || echo "Network query dropped or no active sessions found."
        ;;
    2)
        read -p "Paste target Session ID string (e.g., sess_9a648...): " TARGET_SESS_ID
        if [ -z "$TARGET_SESS_ID" ]; then
            echo "Invalid ID parameter. Aborting telemetry lookup tracker."
            exit 1
        fi
        echo "Retrieving time-decay pre-signed S3 download loops for timeline audio tracks..."
        curl -s "https://assemblyai.com" \
          -H "Authorization: $API_KEY" | python3 -m json.tool || echo "Processing error. Verify session string matches dashboard logs."
        ;;
    3)
        echo "Returning to launcher workspace control room..."
        exit 0
        ;;
    *)
        echo "Selection error. Terminating runtime module."
        exit 1
        ;;
esac
