import json

class AssemblyAIEventsHandler:
    def __init__(self):
        self.active_session_id = None
        self.current_user_transcript = ""

    def process_incoming_socket_frame(self, raw_event_frame):
        print("=================================================================")
        print("MODULE: WEBSOCKET EVENT FRAME PARSER & LIFECYCLE CONTROLLER")
        print("=================================================================")
        
        try:
            event = json.loads(raw_event_frame)
        except json.JSONDecodeError:
            print("Error: Invalid structural frame parameter.")
            return

        event_type = event.get("type")
        print(f"Intercepted Event Node: [{event_type}]")

        # 1. Enforce strict session validation gates as defined on Page 34
        if event_type == "session.ready":
            self.active_session_id = event.get("session_id")
            print(f"Handshake Complete! Captured Session ID: {self.active_session_id}")
            print("Channel Status: Unlocked. Safe to stream 'input.audio' now.")

        # 2. Enforce the non-incremental delta replacement rule
        elif event_type == "transcript.user.delta":
            incoming_text = event.get("text", "")
            # Strict Page 34 Specification Rule Check: Delta supersedes entirely, do NOT concatenate.
            self.current_user_transcript = incoming_text
            print(f"[Live User Transcript UI Render]: \"{self.current_user_transcript}\"")

        elif event_type == "transcript.user":
            self.current_user_transcript = event.get("text", "")
            print(f"[Final Turn Transcript Locked]: \"{self.current_user_transcript}\"")

        elif event_type == "session.ended":
            print("Teardown Signal Received: Session is dead on the server side.")
            print(f"   Metrics - Duration: {event.get('session_duration_seconds')}s")
            self.active_session_id = None

if __name__ == "__main__":
    handler = AssemblyAIEventsHandler()
    
    # Simulate receiving a progressive delta frame stream sequence
    handler.process_incoming_socket_frame('{"type": "session.ready", "session_id": "sess_abc123"}')
    handler.process_incoming_socket_frame('{"type": "transcript.user.delta", "text": "What is the weather"}')
    handler.process_incoming_socket_frame('{"type": "transcript.user.delta", "text": "What is the weather in Paris?"}') # Replaces previous entirely
