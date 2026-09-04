#!/bin/bash
set -e
REPO_DIR=$1

echo "================================================================="
echo "📞 RUNNING MODULE: TWILIO SIP TELEPHONY GATEWAY INJECTION"
echo "================================================================="

cd "$REPO_DIR/.."
if [ ! -d "voice-agent-starter-js" ]; then
    echo " Dependencies missing. Please run Stage 1 setup module first!"
    exit 1
fi

cd "voice-agent-starter-js"
read -p " Enter TWILIO_ACCOUNT_SID: " T_SID
read -p " Enter TWILIO_AUTH_TOKEN: " T_TOKEN
read -p " Enter TWILIO_PHONE_NUMBER: " T_NUM
read -p " Enter TWILIO_TRUNK_DOMAIN: " T_DOMAIN

sed -i.bak "/^TWILIO_/d" .env 2>/dev/null || true
cat << EOF >> .env
TWILIO_ACCOUNT_SID=$T_SID
TWILIO_AUTH_TOKEN=$T_TOKEN
TWILIO_PHONE_NUMBER=$T_NUM
TWILIO_TRUNK_DOMAIN=$T_DOMAIN
EOF

npm run phone
echo " Telephony integrations linked successfully."
