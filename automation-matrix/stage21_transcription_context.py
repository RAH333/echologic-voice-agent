import json
import re

def compile_clean_transcription_context(prompt_text, terms_list):
    print("=================================================================")
    print("MODULE: AUTOMATED SPEECH TRANSCRIPTION CONTEXT INJECTOR")
    print("=================================================================")
    print("Verifying parameters against Page 21 STT Contextual Specifications...")

    # 1. Enforce length constraints on the transcription prompt
    if len(prompt_text) > 1750:
        print("Validation Failure: Prompt text exceeds the strict 1750 character ceiling.")
        return None

    # 2. Hygiene check on keyterm parameters
    cleaned_terms = []
    for term in terms_list:
        # Strip trailing formatting or punctuation blocks
        clean = re.sub(r'[^\w\s-]', '', term).strip()
        
        # Guard against full phrase injections
        if len(clean.split()) > 3:
            print(f"DILUTION WARNING: Term '{term}' resembles a full sentence phrase.")
            print("   The boosting list acts on a per-term basis. Phrases degrade accuracy.")
            print("-----------------------------------------------------------------")
            continue
            
        if clean:
            cleaned_terms.append(clean)

    # 3. Limit total arrays size boundary
    if len(cleaned_terms) > 100:
        print("Truncation Notice: Trimming keywords array to top 100 elements.")
        cleaned_terms = cleaned_terms[:100]

    # 4. Construct the structured payload matrix block
    input_context_payload = {
        "input": {
            "transcription_prompt": prompt_text,
            "keyterms": cleaned_terms
        }
    }

    print("COMPLIANCE STATUS: Context payload assembled with zero sentence strings.")
    return input_context_payload

if __name__ == "__main__":
    # Test simulation modeling a compliant tech-support context
    sample_prompt = "A high-tech operational infrastructure support call. Engineers discuss system metrics."
    sample_vocabulary = ["EchoLogic", "Vercel Gateway", "FastAPI hook", "This is an instructional sentence that shouldn't be here."]
    
    compiled_data = compile_clean_transcription_context(sample_prompt, sample_vocabulary)
    if compiled_data:
        print(json.dumps(compiled_data, indent=2))
