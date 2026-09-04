cd ..
#!/bin/bash
cd
# Exit immediately if any individual installation step fails
set -e

echo "================================================================="
echo " ECHOLOGIC AI - AUTOMATED ASSEMBLYAI TEMPLATE ORCHESTRATOR"
echo "================================================================="

# Navigate up to place the AssemblyAI repository side-by-side
cd ..

TARGET_DIR="voice-agent-starter-js"

if [ -d "$TARGET_DIR" ]; then
    echo "  The official AssemblyAI starter folder already exists."
    read -p "Would you like to wipe it and perform a clean re-installation? (y/n): " REINSTALL
    if [ "$REINSTALL" == "y" ]; then
        rm -rf "$TARGET_DIR"
    else
        echo " Skipping download. Proceeding directly to environmental updates..."
    fi
fi

# Clone the official core AssemblyAI Voice Agent template repository
if [ ! -d "$TARGET_DIR" ]; then
    echo "Cloning official AssemblyAI Voice Agent workspace from GitHub..."
    git clone https://github.com
fi

cd "$TARGET_DIR"

echo " Synchronizing local configuration modules..."
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        cp .env.example .env
    else
        touch .env
    fi
fi

# Extract API Keys safely from the main application's environment configuration
# checks your main app profile first so you don't have to re-type keys manually
MAIN_APP_ENV="../echologic-voice-agent/.env"
EXISTING_KEY=""
EXISTING_AGENT=""

if [ -f "$MAIN_APP_ENV" ]; then
    EXISTING_KEY=$(grep "ASSEMBLYAI_API_KEY=" "$MAIN_APP_ENV" | cut -d'=' -f2)
    EXISTING_AGENT=$(grep "NEXT_PUBLIC_ASSEMBLYAI_AGENT_ID=" "$MAIN_APP_ENV" | cut -d'=' -f2)
fi

# Verify or request the AssemblyAI Master API Access Key
if [ -z "$EXISTING_KEY" ]; then
    echo " Security profile token missing from local workspace."
    read -p " Enter your AssemblyAI API Secret Key: " USER_KEY
    EXISTING_KEY="$USER_KEY"
fi

# Write keys securely to the AssemblyAI configuration ecosystem
sed -i.bak "/^ASSEMBLYAI_API_KEY=/d" .env 2>/dev/null || true
echo "ASSEMBLYAI_API_KEY=$EXISTING_KEY" >> .env

echo " Installing Node.js system dependencies and core engines..."
npm install

# Verify if an existing custom cloud agent requires publishing
echo "-----------------------------------------------------------------"
echo " Syncing Voice Configuration Definitions to AssemblyAI Cloud..."
echo "-----------------------------------------------------------------"
# Default publish executes the built-in minimal json schema context 
npm run publish

echo "================================================================="
echo " ASSEMBLYAI INFRASTRUCTURE AUTOMATION COMPLETED SUCCESSFULLY!"
echo "================================================================="
echo " To run the default AssemblyAI browser instance, execute: npm start"
echo " Back out and return to your main development center using: cd ../echologic-voice-agent"
