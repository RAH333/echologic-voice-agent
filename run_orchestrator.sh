#!/bin/bash
set -e

REPO_DIR=$(pwd)
MATRIX_DIR="$REPO_DIR/automation-matrix"
chmod +x "$MATRIX_DIR"/*.sh 2>/dev/null || true

while true; do
    clear
    echo "================================================================="
    echo "🧠  ECHOLOGIC AI — OPERATIONAL MATRIX CONTROL ROOM"
    echo "================================================================="
    echo "Active Workspace Branch Context: [feature/automation-matrix]"
    echo "-----------------------------------------------------------------"
    echo "Select an independent documentation page module to execute:"
    echo " 1) [Page: Get Started]       Full Clone, Setup & Twilio Linking"
    echo " 2) [Page: Build with AI]     Enforce PCM16 Audio & AEC Rules"
    echo " 3) [Page: Turn Detection]    Deploy Adaptive Silence Patterns"
    echo " 4) [Page: Manage Agents]     Pull Session Histories & Timelines"
    echo " 5) [Page: Supported Langs]   Sync Universal-3.5 Multi-Accents"
    echo " 6) [Page: Create an Agent]   🚀 Run REST Agent Blueprint Creator"
    echo " 7) Exit Matrix Control Room"
    echo "-----------------------------------------------------------------"
    read -p "👉 Choose page module [1-7] and hit Enter: " ORCH_SELECTION

    case $ORCH_SELECTION in
        1) bash "$MATRIX_DIR/stage1_get_started.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        2) bash "$MATRIX_DIR/stage2_audio_constraints.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        3) bash "$MATRIX_DIR/stage3_turn_detection.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        4) bash "$MATRIX_DIR/stage4_session_analytics.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        5) bash "$MATRIX_DIR/stage5_language_matrix.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        6) python3 "$MATRIX_DIR/stage6_create_agent.py"; read -p "🏁 Done. Press Enter..." d ;;
        7) echo "👋 Exiting control room safely."; exit 0 ;;
        *) echo "❌ Invalid option. Press Enter to retry..."; read d ;;
    esac
done
