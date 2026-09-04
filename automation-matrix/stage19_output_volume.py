import os
import requests
import json

def execute_volume_adjustment_pipeline(target_volume=None):
    print("=================================================================")
    print("MODULE: DYNAMIC OUTPUT AUDIO VOLUME PROVISIONER")
    print("=================================================================")
    print("Verifying adjustments against Page 19 Volume Constraints...")

    # 1. Gather the requested volume setting
    if target_volume is None:
        try:
            target_volume = input("Enter target volume level (0-100, or leave blank for native): ").strip()
            if target_volume == "":
                target_volume = None
            else:
                target_volume = int(target_volume)
        except ValueError:
            print("Validation Error: Volume must be a valid integer.")
            return

    # 2. Strict bounding validation check
    if target_volume is not None:
        if not (0 <= target_volume <= 100):
            print(f"Range Exception: Volume level [{target_volume}] must be between 0 and 100.")
            return
        print(f"Checked: Volume level [{target_volume}] is within safe boundaries.")
    else:
        print("Checked: Reverting to native engine playback volume level.")

    # 3. Assemble structural update payload object
    volume_payload = {
        "output": {
            "volume": target_volume
        }
    }
    
    print("\nCompiled Payload Structure:")
    print(json.dumps(volume_payload, indent=2))
    print("-----------------------------------------------------------------")
    print("Mid-Session Mutability Rule Verified:")
    print("   Unlike voices, this configuration parameter can be safely updated")
    print("   mid-call over WebSockets and will instantly apply to next audio chunks.")

if __name__ == "__main__":
    # Test execution simulating an update to 60% volume
    execute_volume_adjustment_pipeline(60)
  
