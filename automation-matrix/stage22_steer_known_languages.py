import json

def compile_language_steering_constraints(selected_codes_list):
    print("=================================================================")
    print("MODULE: MULTILINGUAL STT STEERING COMPLIANCE VALIDATOR")
    print("=================================================================")
    print("Validating input tracking constraints against Page 22 ISO Index...")

    # 1. Authoritative 18 language code registry defined in reference specifications
    valid_codes = {
        "en": "English", "es": "Spanish", "fr": "French", "de": "German",
        "it": "Italian", "pt": "Portuguese", "tr": "Turkish", "nl": "Dutch",
        "sv": "Swedish", "da": "Danish", "fi": "Finnish", "hi": "Hindi",
        "vi": "Vietnamese", "ar": "Arabic", "he": "Hebrew", "ja": "Japanese",
        "zh": "Mandarin", "no": "Norwegian"
    }

    if not selected_codes_list:
        print("Language codes list empty. Setting to automatic multilingual detection mode.")
        return {"input": {"language_codes": []}}

    validated_array = []
    for code in selected_codes_list:
        clean_code = str(code).strip().lower()
        if clean_code in valid_codes:
            print(f"Code Verified: [{clean_code}] maps directly to {valid_codes[clean_code]}")
            validated_array.append(clean_code)
        else:
            print(f"Validation Error: [{clean_code}] is not an officially tracked language code.")
            print("     Please consult your reference sheet before mapping this parameter.")
            return None

    # 2. Package into compliant payload JSON block structure
    steering_payload = {
        "input": {
            "language_codes": validated_array
        }
    }
    
    print("\n=================================================================")
    print("STRUCTURE SUCCESS: Steering parameter block mapped perfectly.")
    print("=================================================================")
    print("Deployment Notice: Remember that this setting updates exactly")
    print("   when a new connection opens, mid-session pushes await next reconnect.")
    return steering_payload

if __name__ == "__main__":
    # Test execution simulating a region-pinned Spanish and English bilingual support line
    sample_selections = ["en", "es"]
    compiled_result = compile_language_steering_constraints(sample_selections)
    if compiled_result:
        print(json.dumps(compiled_result, indent=2))
