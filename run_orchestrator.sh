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
    echo " 1) [Page 1: Quickstart]       Clone Workspace & Verify Environment"
    echo " 2) [Page 2: Telephony]        Configure Live Twilio SIP Trunks"
    echo " 3) [Page 3: Audio Constraints] Enforce PCM16 Audio & Client AEC Rules"
    echo " 4) [Page 4: Session History]  Fetch Presigned Audio & Call Transcripts"
    echo " 5) [Page 5: Supported Langs]  Provision Universal-3.5 Multi-Accents"
    echo " 6) [Page 6: Manage Agents]    🚀 Run Full Agent REST Lifecycle (CRUD)"
    echo " 7) Exit Matrix Control Room"
    echo "-----------------------------------------------------------------"
    read -p "👉 Choose documentation page module [1-7]: " ORCH_SELECTION

    case $ORCH_SELECTION in
        1) bash "$MATRIX_DIR/stage1_get_started.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        2) bash "$MATRIX_DIR/stage2_twilio_telephony.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        3) bash "$MATRIX_DIR/stage3_audio_constraints.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        4) bash "$MATRIX_DIR/stage4_session_analytics.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        5) bash "$MATRIX_DIR/stage5_supported_languages.sh" "$REPO_DIR"; read -p "🏁 Done. Press Enter..." d ;;
        6) python3 "$MATRIX_DIR/stage6_manage_agents.py"; read -p "🏁 Done. Press Enter..." d ;;
        7) echo "👋 Exiting control room safely."; exit 0 ;;
        *) echo "❌ Invalid option. Press Enter to retry..."; read d ;;
    esac
done
