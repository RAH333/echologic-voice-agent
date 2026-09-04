import json

def compile_audio_format_specification(input_encoding, output_encoding, chosen_sample_rate=None):
    print("=================================================================")
    print("🔊 MODULE: RAW AUDIO FORMAT COMPLIANCE VALIDATOR")
    print("=================================================================")
    print("Evaluating streaming configuration arrays against Page 27 constraints...")

    # 1. Authoritative encoding directory validation rules defined in specifications
    valid_encodings = {
        "audio/pcm": {"default_rate": 24000, "bit_depth": "16-bit Little-Endian"},
        "audio/pcmu": {"default_rate": 8000, "bit_depth": "8-bit mu-law"},
        "audio/pcma": {"default_rate": 8000, "bit_depth": "8-bit A-law"}
    }

    clean_in = str(input_encoding).strip().lower()
    clean_out = str(output_encoding).strip().lower()

    if clean_in not in valid_encodings or clean_out not in valid_encodings:
        print("Encoding Exception: Selected type does not match allowed specs.")
        print("   Valid parameters are: 'audio/pcm', 'audio/pcmu', or 'audio/pcma'.")
        return None

    # 2. Extract or infer matching sample rates automatically
    in_rate = chosen_sample_rate if chosen_sample_rate else valid_encodings[clean_in]["default_rate"]
    out_rate = chosen_sample_rate if chosen_sample_rate else valid_encodings[clean_out]["default_rate"]

    print("Codec Validation Mapping Summary:")
    print(f"Input  Format: {clean_in} at {in_rate}Hz ({valid_encodings[clean_in]['bit_depth']})")
    print(f"Output Format: {clean_out} at {out_rate}Hz ({valid_encodings[clean_out]['bit_depth']})")

    # 3. Assemble structural JSON configuration block
    audio_format_payload = {
        "input": {
            "format": {
                "encoding": clean_in,
                "sample_rate": in_rate
            }
        },
        "output": {
            "format": {
                "encoding": clean_out,
                "sample_rate": out_rate
            }
        }
    }

    print("\n=================================================================")
    print("SUCCESS: Binary audio configuration properties compiled.")
    print("=================================================================")
    print("Immutability Warning: Remember that inline output format arrays")
    print("   become completely frozen and un-patchable after 'session.ready'.")
    return audio_format_payload

if __name__ == "__main__":
    # Test simulation: assembling a native 8kHz telephony support line setup
    compiled_result = compile_audio_format_specification("audio/pcmu", "audio/pcmu")
    if compiled_result:
        print(json.dumps(compiled_result, indent=2))
