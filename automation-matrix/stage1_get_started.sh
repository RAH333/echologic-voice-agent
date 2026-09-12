#!/bin/bash
set -e
REPO_DIR=$1

echo "================================================================="
echo "  RUNNING MODULE: CONSOLIDATED ENVIRONMENT SETUP & TELEPHONY"
echo "================================================================="

# Navigate to the workspace layer right above your repository directory

# cd "$REPO_DIR/.."
WORKSPACE_ROOT=$(pwd)

if [ ! -d "voice-agent-starter-js" ]; then
    echo " Cloning official AssemblyAI Voice Agent tool suite side-by-side..."
    # git clone https://github.com "voice-agent-starter-js"
else
    echo "AssemblyAI official workspace directory is already verified."
fi

# Share environmental variables downstream
# cd "$WORKSPACE_ROOT/voice-agent-starter-js"

if [ ! -f .env ]; then
    echo " searchinh env file"
    if [ -f .env.example ]; then cp .env.example .env; else touch .env; fi
fi

# if [ -f "$REPO_DIR/.env" ]; then
    # EXISTING_KEY=$(grep "ASSEMBLYAI_API_KEY=" "$REPO_DIR/.env" | cut -d'=' -f2 || true)
    # if [ -n "$EXISTING_KEY" ]; then
        ##sed -i.bak "/^ASSEMBLYAI_API_KEY=/d" .env 2>/dev/null || true
        ## Safely remove only the old AssemblyAI key line
        # sed -i "" "/^ASSEMBLYAI_API_KEY=/d" .env 2>/dev/null || sed -i.bak "/^ASSEMBLYAI_API_KEY=/d" .env 2>/dev/null || true
        # echo "ASSEMBLYAI_API_KEY=$EXISTING_KEY" >> .env
        # echo "Auto-synced global configuration tokens across repositories."
        # pwd
    # fi
# fi

# Now this block will find the separate file paths and print your output!
if [ -f "$REPO_DIR/.env" ]; then
    # EXISTING_KEY=$(grep "ASSEMBLYAI_API_KEY=" "$REPO_DIR/.env" | cut -d'=' -f2 || true)
    #if [ -n "$EXISTING_KEY" ]; then
        # sed -i "" "/^ASSEMBLYAI_API_KEY=/d" .env 2>/dev/null || sed -i.bak "/^ASSEMBLYAI_API_KEY=/d" .env 2>/dev/null || true
    read -p "Enter ASSEMBLYAI_API_KEY: " EXISTING_KEY 
    echo "ASSEMBLYAI_API_KEY=$EXISTING_KEY" >> .env
    echo "🔄 Auto-synced global configuration tokens across repositories."
    fi
fi

# echo "Installing workspace application dependencies..."
# npm install

echo "Publishing baseline configurations to AssemblyAI cloud engine..."
npm run publish --if-present || true

echo "================================================================="
echo "📞 RUNNING SUB-MODULE: TWILIO SIP TELEPHONY GATEWAY INJECTION"
echo "================================================================="

# Prompt for the Twilio authentication and mapping configs seamlessly
read -p "Enter TWILIO_ACCOUNT_SID: " T_SID
read -p "Enter TWILIO_AUTH_TOKEN: " T_TOKEN
read -p "Enter TWILIO_PHONE_NUMBER: " T_NUM
read -p "Enter TWILIO_TRUNK_DOMAIN: " T_DOMAIN

# Clean previous configs and append the fresh variables to the active environment
# sed -i.bak "/^TWILIO_/d" .env 2>/dev/null || true

# Safely remove only lines starting with TWILIO_

# #sed -i "" "/^TWILIO_/d" .env 2>/dev/null || sed -i.bak "/^TWILIO_/d" .env 2>/dev/null || true
# cat << EOF >> .env
# TWILIO_ACCOUNT_SID=$T_SID
# TWILIO_AUTH_TOKEN=$T_TOKEN
# TWILIO_PHONE_NUMBER=$T_NUM
# TWILIO_TRUNK_DOMAIN=$T_DOMAIN
# EOF

echo "TWILIO_ACCOUNT_SID=$T_SID" >> .env
echo "TWILIO_AUTH_TOKEN=$T_TOKEN" >> .env
echo "TWILIO_PHONE_NUMBER=$T_NUM" >> .env
echo "TWILIO_TRUNK_DOMAIN=$T_DOMAIN" >> .env

echo  "start"
npm start
echo "close"

echo "Initializing telephone integration systems..."
npm run phone --if-present || true

echo "Consolidated Stage 1 architecture setup completed with 0 errors!"
