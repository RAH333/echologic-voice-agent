import json

def process_interruption_event_stream(incoming_raw_event):
    print("=================================================================")
    print("MODULE: ADAPTIVE TURN DETECTION & AUDIO FLUSH ENGINE")
    print("=================================================================")
    
    event = json.loads(incoming_raw_event)
    event_type = event.get("type")
    
    # 1. Enforce snappy barge-in flushing as specified on Page 20
    if event_type == "input.speech.started":
        print("[Barge-In Detected!]: User started speaking mid-sentence.")
        print("ACTION: Instantly flushing playback audio queues.")
        return "FLUSH_AUDIO_BUFFER"
        
    elif event_type == "reply.done" and event.get("status") == "interrupted":
        print("[Server Handshake]: Agent was cut off mid-thought by user speech.")
        print("ACTION: Clear queued speech buffers and synchronize timelines.")
        return "SYNC_TIMELINE_TRUNCATION"
        
    elif event_type == "session.update_mode":
        # Toggle configuration profile based on current workflow task context
        target_mode = event.get("mode", "balanced")
        print(f"[Transcription Mode Update]: Switching to '{target_mode}'.")
        payload = {
            "input": {
                "transcription_mode": target_mode
            }
        }
        return payload
        
    print("Event processed cleanly. No turn adjustments required.")
    return "CONTINUE_STREAM"

if __name__ == "__main__":
    # Test simulation: client intercepts user cutting in out loud
    mock_event = '{"type": "input.speech.started"}'
    process_interruption_event_stream(mock_event)
  
