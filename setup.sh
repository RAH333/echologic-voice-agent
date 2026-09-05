#!/bin/bash

# Ensure terminal exits instantly if an installation step crashes
set -e

echo "===================================================="
echo "ECLOLOGIC AI - AUTOMATED WORKSPACE SETUP ORCHESTRATOR"
echo "===================================================="

# Check if a local .env configuration module already exists
if [ -f .env ]; then
    echo "  An existing local environment configuration file (.env) was detected."
    read -p "Would you like to overwrite it and re-enter your security keys? (y/n): " OVERWRITE
    if [ "$OVERWRITE" != "y" ]; then
        echo "  Skipping key configuration phase. Keeping current secrets safe."
    else
        rm .env
    fi
fi

# Dynamically request critical security configuration parameters
if [ ! -f .env ]; then
    echo " Configuring Project Credentials..."
    read -p " Enter your AssemblyAI API Secret Key: " AAI_KEY
    read -p " Enter your AssemblyAI Voice Agent ID string: " AGENT_ID
    read -p " Enter your localized fulfillment secret key (or hit Enter for default): " WEBHOOK_SEC
    
    if [ -z "$WEBHOOK_SEC" ]; then
        WEBHOOK_SEC="default_secret_key"
    fi

    # Write secrets seamlessly across environment spaces
    echo "Writing environment configurations..."
    cat << EOF > .env
ASSEMBLYAI_API_KEY=$AAI_KEY
NEXT_PUBLIC_ASSEMBLYAI_AGENT_ID=$AGENT_ID
ASSEMBLYAI_WEBHOOK_SECRET=$WEBHOOK_SEC
ENVIRONMENT=development
EOF
    
    # Mirror env layout into backend configurations space
    cp .env backend/.env
    echo " Configuration secrets successfully bound to root and backend paths."
fi

echo "----------------------------------------------------"
echo "Initializing Backend Virtual Space & Packages..."
echo "----------------------------------------------------"
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
cd ..
echo " Python server modules prepared cleanly."

echo "----------------------------------------------------"
echo " Injecting Node.js Frontend Workspace Packages..."
echo "----------------------------------------------------"
cd frontend
npm install
cd ..
echo " Next.js user-interface components successfully prepared."

echo "===================================================="
echo "SETUP COMPLETED WITH ABSOLUTE ZERO ERRORS!"
echo "===================================================="
echo "To start the entire ecosystem moving forward, execute: npm run dev:all or follow the README guide!"
