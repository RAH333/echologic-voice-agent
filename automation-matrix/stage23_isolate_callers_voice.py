import json

def compile_voice_focus_suppression_block(model_type, sensitivity_threshold=None):
    print("=================================================================")
    print("🔊 MODULE: BACKGROUND AUDIO NOISE SUPPRESSION VALIDATOR")
    print("=================================================================")
    print("Evaluating environmental voice focus arrays against Page 23 rules...")

    # 1. Enforce specific model token choices
    model_clean = str(model_type).strip().lower()
    if model_clean not in ["near-field", "far-field"]:
        print(f"Configuration Exception: Type [{model_clean}] is unmapped.")
        print("   Valid choices are strictly limited to 'near-field' or 'far-field'.")
        return None

    # 2. Check bounding coordinates of the suppression aggressiveness knob
    payload_input = {
        "voice_focus": model_clean
    }

    if sensitivity_threshold is not None:
        try:
            threshold_float = float(sensitivity_threshold)
            if not (0.0 <= threshold_float <= 1.0):
                print(f"Threshold Out of Bounds: Value [{threshold_float}] must be 0.0 to 1.0.")
                return None
            
            payload_input["voice_focus_threshold"] = threshold_float
            print(f"Verified: Suppression threshold locked at aggression index: {threshold_float}")
        except ValueError:
            print("Validation Exception: Threshold must be a floating point number.")
            return None
    else:
        print("Verified: Using factory default aggression index (0.85).")

    # 3. Assemble structural container block matching API specs
    voice_focus_payload = {
        "input": payload_input
    }

    print("\n=================================================================")
    print("SUCCESS: Environmental background focus criteria compiled.")
    print("=================================================================")
    return voice_focus_payload

if __name__ == "__main__":
    # Test execution modeling a high-suppression drive-thru loudspeaker setup
    compiled_block = compile_voice_focus_suppression_block("far-field", 0.8)
    if compiled_block:
        print(json.dumps(compiled_block, indent=2))
