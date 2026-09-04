#!/bin/bash
set -e
clear

REPO_DIR=$(pwd)
MATRIX_DIR="$REPO_DIR/automation-matrix"

echo "================================================================="
echo "ECHOLOGIC AI — CORE AUTOMATION & COMPONENT RUNTIME PLATFORM"
echo "================================================================="
echo "1) STAGE 1: Fresh Installation & Local Dependency Setup"
echo "2) STAGE 2: Advanced Telephony (Twilio SIP Gateway Integration)"
echo "3) STAGE 3: Agent API Custom Code Segment Configurations"
echo "4) STAGE 4: Session History Analytics & Transcript Extraction" # Added
echo "5) EXIT"
echo "-----------------------------------------------------------------"
read -p "Choose a code segment block to initialize [1-5]: " MODULAR_CHOICE

case $MODULAR_CHOICE in
    1)
        chmod +x "$MATRIX_DIR/stage1_setup.sh"
        bash "$MATRIX_DIR/stage1_setup.sh" "$REPO_DIR"
        ;;
    2)
        chmod +x "$MATRIX_DIR/stage2_twilio.sh"
        bash "$MATRIX_DIR/stage2_twilio.sh" "$REPO_DIR"
        ;;
    3)
        chmod +x "$MATRIX_DIR/stage3_agent_api.sh"
        bash "$MATRIX_DIR/stage3_agent_api.sh" "$REPO_DIR"
        ;;
    4)
        chmod +x "$MATRIX_DIR/stage4_session_analytics.sh"
        bash "$MATRIX_DIR/stage4_session_analytics.sh" "$REPO_DIR"
        ;;
    5)
        echo "Exiting configuration environment safely."
        exit 0
        ;;
    *)
        echo "Selection error. Please run the script again."
        exit 1
        ;;
esac
