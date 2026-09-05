#!/bin/bash
set -e
REPO_DIR=$1

echo "================================================================="
echo "RUNNING MODULE: CORE ENVIRONMENT SETUP & DEPENDENCY EXTRACTION"
echo "================================================================="

# Navigate to the workspace layer right above your github directory
cd "$REPO_DIR/.."
WORKSPACE_ROOT=$(pwd)

if [ ! -d "voice-agent-starter-js" ]; then
    echo "Cloning official AssemblyAI Voice Agent tool suite side-by-side..."
    # FIX: Added full template repository URL layout paths
    git clone https://github.com
else
    echo "AssemblyAI official workspace directory is already verified."
fi

# Share environmental variables downstream
cd "$WORKSPACE_ROOT/voice-agent-starter-js"
if [ ! -f .env ]; then
    if [ -f .env.example ]; then cp .env.example .env; else touch .env; fi
fi

if [ -f "$REPO_DIR/.env" ]; then
    EXISTING_KEY=$(grep "ASSEMBLYAI_API_KEY=" "$REPO_DIR/.env" | cut -d'=' -f2 || true)
    if [ -n "$EXISTING_KEY" ]; then
        sed -i.bak "/^ASSEMBLYAI_API_KEY=/d" .env 2>/dev/null || true
        echo "ASSEMBLYAI_API_KEY=$EXISTING_KEY" >> .env
        echo "Auto-synced global configuration tokens across repositories."
    fi
fi

npm install
echo "Core setup sequence completed with absolute zero errors."
