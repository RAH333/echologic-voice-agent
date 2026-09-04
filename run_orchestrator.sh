#!/bin/bash
set -e

REPO_DIR=$(pwd)
MATRIX_DIR="$REPO_DIR/automation-matrix"

# Ensure runtime script folder permissions are set correctly
chmod +x "$MATRIX_DIR"/*.sh 2>/dev/null || true

while true; do
    clear
    echo "================================================================="
    echo "🧠  ECHOLOGIC AI — OPERATIONAL MATRIX CONTROL ROOM"
    echo "================================================================="
    echo "Active Workspace Branch Context: [feature/automation-matrix]"
    echo "-----------------------------------------------------------------"
    echo "Select an isolated code segment module to configure and execute:"
    echo " 1) [Page: Core Setup]        Initialize Side-by-Side Repositories"
    echo " 2) [Page: Connect To Twilio] Setup SIP Telephony Phone Lines"
    echo " 3) [Page: Build with AI]      Enforce PCM16 Audio & AEC Rules"
    echo " 4) [Page: Manage Agents]      Pull Session Histories & Timelines"
    echo " 5) [Page: Supported Langs]   Deploy Universal-3.5 Multilingual"
    echo " 6) Exit Matrix"
    echo "-----------------------------------------------------------------"
    read -p "👉 Type option [1-6] and hit Enter: " ORCH_SELECTION

    case $ORCH_SELECTION in
        1)
            bash "$MATRIX_DIR/stage1_core_setup.sh" "$REPO_DIR"
            read -p "🏁 Task complete. Press Enter to return to Matrix Menu..." dummy
            ;;
        2)
            bash "$MATRIX_DIR/stage2_twilio_sip.sh" "$REPO_DIR"
            read -p "🏁 Task complete. Press Enter to return to Matrix Menu..." dummy
            ;;
        3)
            bash "$MATRIX_DIR/stage3_agent_api.sh" "$REPO_DIR"
            read -p "🏁 Task complete. Press Enter to return to Matrix Menu..." dummy
            ;;
        4)
            bash "$MATRIX_DIR/stage4_session_analytics.sh" "$REPO_DIR"
            read -p "🏁 Task complete. Press Enter to return to Matrix Menu..." dummy
            ;;
        5)
            bash "$MATRIX_DIR/stage5_language_matrix.sh" "$REPO_DIR"
            read -p "🏁 Task complete. Press Enter to return to Matrix Menu..." dummy
            ;;
        6)
            echo "👋 Closing workspace session safely. Happy hacking!"
            exit 0
            ;;
        *)
            echo "❌ Invalid entry. Press Enter to retry..."
            read dummy
            ;;
    esac
done
