#!/bin/bash
set -e

REPO_DIR=$(pwd)
MATRIX_DIR="$REPO_DIR/automation-matrix"

# Ensure all downstream file scripts are executable instantly
chmod +x "$MATRIX_DIR"/*.sh 2>/dev/null || true

while true; do
    clear
    echo "================================================================="
    echo "🧠  ECHOLOGIC AI — OPERATIONAL RE-LOOPING MANAGEMENT CONSOLE"
    echo "================================================================="
    echo "Active Branch Environment Context: [feature/automation-matrix]"
    echo "-----------------------------------------------------------------"
    echo "Select an independent documentation stage script block to execute:"
    echo " 1)  [Page 1]  Get Started (Clone & Install) | 14) [Page 14] Greeting Manager"
    echo " 2)  [Page 2]  Voice Agent API Core Overview | 15) [Page 15] Tools Core Framework"
    echo " 3)  [Page 3]  Build with AI Coding Tools    | 16) [Page 16] HTTP Tools Server-Side"
    echo " 4)  [Page 4]  Supported Languages Matrix    | 17) [Page 17] Client Side Function Tools"
    echo " 5)  [Page 5]  Create an Agent Guide Body    | 18) [Page 18] Voices and Accent Profiles"
    echo " 6)  [Page 6]  Manage Agents CRUD Framework  | 19) [Page 19] Output Volume Controls"
    echo " 7)  [Page 7]  Create Agent OpenAPI Spec     | 20) [Page 20] Turn Detection & Barge-In"
    echo " 8)  [Page 8]  List Active Agents Records    | 21) [Page 21] Transcription Context"
    echo " 9)  [Page 9]  Retrieve Stored Agent Fields  | 22) [Page 22] Steer Known Languages"
    echo " 10) [Page 10] Update Agent Delta Fields     | 23) [Page 23] Isolate Caller's Voice"
    echo " 11) [Page 11] Delete Agent Validation Path   | 24) [Page 24] Deploy Your Agent Gateway"
    echo " 12) [Page 12] Connect Custom LLM Gateways   | 25) [Page 25] Browser Integration Nodes"
    echo " 13) [Page 13] Voice Prompting Guide Rules   | 26) [EXIT WORKSPACE]"
    echo "-----------------------------------------------------------------"
    read -p "👉 Choose targeted automation stage number [1-26]: " SELECTION

    case $SELECTION in
        1) bash "$MATRIX_DIR/stage1_get_started.sh" "$REPO_DIR" ;;
        2) bash "$MATRIX_DIR/stage2_voice_agent_api.sh" "$REPO_DIR" ;;
        3) bash "$MATRIX_DIR/stage3_build_with_ai.sh" "$REPO_DIR" ;;
        4) bash "$MATRIX_DIR/stage4_supported_languages.sh" "$REPO_DIR" ;;
        5) bash "$MATRIX_DIR/stage5_create_agent.sh" "$REPO_DIR" ;;
        6) python3 "$MATRIX_DIR/stage6_manage_agents.py" ;;
        7) python3 "$MATRIX_DIR/stage7_create_agent_spec.py" ;;
        8) python3 "$MATRIX_DIR/stage8_list_agents_spec.py" ;;
        9) python3 "$MATRIX_DIR/stage9_retrieve_agent_spec.py" ;;
        10) python3 "$MATRIX_DIR/stage10_update_agent_spec.py" ;;
        11) python3 "$MATRIX_DIR/stage11_delete_agent_spec.py" ;;
        12) python3 "$MATRIX_DIR/stage12_connect_your_own_llm.py" ;;
        13) python3 "$MATRIX_DIR/stage13_prompting_guide.py" ;;
        14) python3 "$MATRIX_DIR/stage14_greeting_manager.py" ;;
        15) python3 "$MATRIX_DIR/stage15_tools_core_framework.py" ;;
        16) python3 "$MATRIX_DIR/stage16_http_tools_server_side.py" ;;
        17) python3 "$MATRIX_DIR/stage17_client_side_function_tools.py" ;;
        18) python3 "$MATRIX_DIR/stage18_voices_and_accents.py" ;;
        19) python3 "$MATRIX_DIR/stage19_output_volume.py" ;;
        20) python3 "$MATRIX_DIR/stage20_turn_detection_spec.py" ;;
        21) python3 "$MATRIX_DIR/stage21_transcription_context.py" ;;
        22) python3 "$MATRIX_DIR/stage22_steer_known_languages.py" ;;
        23) python3 "$MATRIX_DIR/stage23_isolate_callers_voice.py" ;;
        24) python3 "$MATRIX_DIR/stage24_deploy_your_agent.py" ;;
        25) node "$MATRIX_DIR/stage25_browser_integration.js" ;;
        26) echo "👋 Closing management control console safely. Build strong!"; exit 0 ;;
        *) echo "❌ Option unmapped.";;
    esac
    echo ""
    read -p "🏁 Stage execution completed. Press [Enter] to cycle back to Matrix..." dummy
done
