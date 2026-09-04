#!/bin/bash
set -e

REPO_DIR=$(pwd)
MATRIX_DIR="$REPO_DIR/automation-matrix"

# Dynamically ensure all stage scripts carry flawless execution clearance
chmod +x "$MATRIX_DIR"/*.sh 2>/dev/null || true

while true; do
    clear
    echo "================================================================="
    echo "🎛️  ECHOLOGIC AI — COMPOSABLE HACKATHON WORKSPACE MATRIX"
    echo "================================================================="
    echo "Active Branch Environment Context: [feature/automation-matrix]"
    echo "-----------------------------------------------------------------"
    echo "Select an isolated full-page documentation module to execute:"
    echo "  1) [Page 1-5]  Core Application Cloners, Installers & Server Provisioners"
    echo "  2) [Page 6-11] REST Agent Management Lifecycle (CRUD OpenAPI Specs)"
    echo "  3) [Page 12-14] Prompting architecture, Tone Rules & Immutable TTS Greetings"
    echo "  4) [Page 15-17] Hold vs Interactive Tooling Frameworks & Client State Sync"
    echo "  5) [Page 18-20] Audio Accents Catalog, Mutable Volume & Turn Barge-In Rules"
    echo "  6) [Page 21-23] Keyterms Vocabulary Boosting, ISO Steering & Voice Focus"
    echo "  7) [Page 24-25] Browser token Flow handshakes & Worklet Resample Engines"
    echo "  8) [Page 26-28] Twilio Elastic SIP Trunking & Bluejay CHIRP Simulations"
    echo "  9) [Page 29-32] S3 Artifact Timeline Extractors & Session Deletion Schema"
    echo " 10) [Page 33-35] WebSocket Mutability Policing & AEC Feedback Troubleshooting"
    echo " 11) [Page 36-39] Canonical Protocol State Machine & Token Error Parsers"
    echo " 12) EXIT CORE WORKSPACE"
    echo "-----------------------------------------------------------------"
    read -p "👉 Choose targeted automation chapter number [1-12]: " CHAPTER

    case $CHAPTER in
        1)
            echo "--- Executing Core Setup Steps [Pages 1 to 5] ---"
            bash "$MATRIX_DIR/stage1_get_started.sh" "$REPO_DIR"
            ;;
        2)
            echo "--- Launching REST Agent Specifications CRUD Hub [Pages 6 to 11] ---"
            echo "Select action: 6) CRUD Guide, 7) Create Spec, 8) List Spec, 9) Retrieve Spec, 10) Update Spec, 11) Delete Spec"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 6 ]; then python3 "$MATRIX_DIR/stage6_manage_agents.py";
            elif [ "$sub_choice" -eq 7 ]; then python3 "$MATRIX_DIR/stage7_create_agent_spec.py";
            elif [ "$sub_choice" -eq 8 ]; then python3 "$MATRIX_DIR/stage8_list_agents_spec.py";
            elif [ "$sub_choice" -eq 9 ]; then python3 "$MATRIX_DIR/stage9_retrieve_agent_spec.py";
            elif [ "$sub_choice" -eq 10 ]; then python3 "$MATRIX_DIR/stage10_update_agent_spec.py";
            elif [ "$sub_choice" -eq 11 ]; then python3 "$MATRIX_DIR/stage11_delete_agent_spec.py"; fi
            ;;
        3)
            echo "--- Launching Prompt & Greeting Managers [Pages 12 to 14] ---"
            echo "Select action: 12) LLM Custom Gateways, 13) Prompt Architect, 14) TTS Greeting Configurator"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 12 ]; then python3 "$MATRIX_DIR/stage12_connect_your_own_llm.py";
            elif [ "$sub_choice" -eq 13 ]; then python3 "$MATRIX_DIR/stage13_prompting_guide.py";
            elif [ "$sub_choice" -eq 14 ]; then python3 "$MATRIX_DIR/stage14_greeting_manager.py"; fi
            ;;
        4)
            echo "--- Launching Functional Tool Sync Matrices [Pages 15 to 17] ---"
            echo "Select action: 15) Latency Bounding, 16) Server HTTP tools, 17) Client reply.done handlers"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 15 ]; then python3 "$MATRIX_DIR/stage15_tools_core_framework.py";
            elif [ "$sub_choice" -eq 16 ]; then python3 "$MATRIX_DIR/stage16_http_tools_server_side.py";
            elif [ "$sub_choice" -eq 17 ]; then python3 "$MATRIX_DIR/stage17_client_side_function_tools.py"; fi
            ;;
        5)
            echo "--- Launching Audio Properties & Turn Barge-In Systems [Pages 18 to 20] ---"
            echo "Select action: 18) Dialect Maps, 19) Volume Scales, 20) Interruption Flushers"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 18 ]; then python3 "$MATRIX_DIR/stage18_voices_and_accents.py";
            elif [ "$sub_choice" -eq 19 ]; then python3 "$MATRIX_DIR/stage19_output_volume.py";
            elif [ "$sub_choice" -eq 20 ]; then python3 "$MATRIX_DIR/stage20_turn_detection_spec.py"; fi
            ;;
        6)
            echo "--- Launching STT Context & Environmental Suppression Systems [Pages 21 to 23] ---"
            echo "Select action: 21) Keyterms Jargon Boost, 22) ISO Codes Steering, 23) Voice Focus Filters"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 21 ]; then python3 "$MATRIX_DIR/stage21_transcription_context.py";
            elif [ "$sub_choice" -eq 22 ]; then python3 "$MATRIX_DIR/stage22_steer_known_languages.py";
            elif [ "$sub_choice" -eq 23 ]; then python3 "$MATRIX_DIR/stage23_isolate_callers_voice.py"; fi
            ;;
        7)
            echo "--- Launching Client Deployment Node Handshakes [Pages 24 to 25] ---"
            echo "Select action: 24) Mutual Exclusion Check, 25) Launch Serverless Token Minting Router"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 24 ]; then python3 "$MATRIX_DIR/stage24_deploy_your_agent.py";
            elif [ "$sub_choice" -eq 25 ]; then node "$MATRIX_DIR/stage25_browser_integration.js"; fi
            ;;
        8)
            echo "--- Launching Telephony Trunks & Stress Simulation Bridges [Pages 26 to 28] ---"
            echo "Select action: 26) Twilio Trunk Verification, 27) Little-Endian Audio specifications, 28) Bluejay CHIRP Setup"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 26 ]; then python3 "$MATRIX_DIR/stage26_twilio_sip_telephony.py";
            elif [ "$sub_choice" -eq 27 ]; then python3 "$MATRIX_DIR/stage27_audio_format.py";
            elif [ "$sub_choice" -eq 28 ]; then python3 "$MATRIX_DIR/stage28_bluejay_simulations.py"; fi
            ;;
        9)
            echo "--- Launching S3 Artifact Downloaders & Log Deleters [Pages 29 to 32] ---"
            echo "Select action: 29) Endless Pagination Loop, 30) List Session Schemas, 31) Retrieve Session Object, 32) Soft-Delete Engine"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 29 ]; then python3 "$MATRIX_DIR/stage29_recordings_and_transcripts.py";
            elif [ "$sub_choice" -eq 30 ]; then python3 "$MATRIX_DIR/stage30_list_sessions_spec.py";
            elif [ "$sub_choice" -eq 31 ]; then python3 "$MATRIX_DIR/stage31_retrieve_session_spec.py";
            elif [ "$sub_choice" -eq 32 ]; then python3 "$MATRIX_DIR/stage32_delete_session_spec.py"; fi
            ;;
        10)
            echo "--- Launching Real-time Mutability & AEC Diagnostics [Pages 33 to 35] ---"
            echo "Select action: 33) Update Mutability Police, 34) Delta Overwrites, 35) Feedback Telemetry"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 33 ]; then python3 "$MATRIX_DIR/stage33_inline_configuration.py";
            elif [ "$sub_choice" -eq 34 ] || [ "$sub_choice" -eq 35 ]; then python3 "$MATRIX_DIR/stage35_troubleshooting.py"; fi
            ;;
        11)
            echo "--- Launching Protocol Sequence State Machines [Pages 36 to 39] ---"
            echo "Select action: 36) Sequence Policer, 37) AsyncAPI Verification, 38) Token Window Scale, 39) Code Exception Handler"
            read -p "👉 Choose step: " sub_choice
            if [ "$sub_choice" -eq 36 ]; then python3 "$MATRIX_DIR/stage36_message_sequence.py";
            elif [ "$sub_choice" -eq 37 ]; then python3 "$MATRIX_DIR/stage37_websocket_asyncapi_spec.py";
            elif [ "$sub_choice" -eq 38 ]; then python3 "$MATRIX_DIR/stage38_generate_token_spec.py";
            elif [ "$sub_choice" -eq 39 ]; then python3 "$MATRIX_DIR/stage39_token_error_spec.py"; fi
            ;;
        12)
            echo "👋 Closing workspace orchestrator safely. Outstanding job this hackathon!"
            exit 0
            ;;
        *)
            echo "❌ Invalid choice."
            ;;
    esac
    echo ""
    read -p "🏁 Chapter block task complete. Press [Enter] to return to the core Master Menu loop..." dummy
done
