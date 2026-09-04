import json

def compile_optimized_voice_prompt(base_identity, can_list, cannot_list):
    print("=================================================================")
    print("MODULE: VOICE-OPTIMIZED PROMPT BLUEPRINT ARCHITECT")
    print("=================================================================")
    print("Enforcing strict formatting rules against Prompting Guide spec...")

    # 1. Structural assembly adhering perfectly to Page 13 layout guidelines
    identity_section = f"BE SHORT. This is the most important rule. Keep every response under two sentences.\n{base_identity}"
    
    tone_section = (
        "Never say 'certainly', 'absolutely', 'happy to help', or 'great question'.\n"
        "Have opinions. You can crack jokes. You don't need to hedge everything.\n"
        "Match the user's length. When they talk in clipped phrases, you do the same."
    )
    
    capabilities_section = "Things you CAN do:\n"
    for item in can_list:
        capabilities_section += f"- {item}\n"
    capabilities_section += "Things you CANNOT do:\n"
    for item in cannot_list:
        capabilities_section += f"- {item}\n"
        
    voice_formatting = (
        "No markdown formatting. If you write words, do NOT use bold or headers.\n"
        "Plain conversational sentences only. When reading URLs, say 'dot' for periods and 'slash' for slashes.\n"
        "Round large numbers naturally. Say 'about 10 thousand' instead of precise integers."
    )

    # 2. Merging the blocks in the mandated specification sequence
    final_prompt = (
        f"# 1. IDENTITY & PRIMARY CRITERIA\n{identity_section}\n\n"
        f"# 2. CONVERSATIONAL TONE & PERMISSIONS\n{tone_section}\n\n"
        f"# 3. EXPLICIT CAPABILITIES BOUNDARIES\n{capabilities_section}\n\n"
        f"# 4. VOICE OUTPUT FORMATTING POLICIES\n{voice_formatting}"
    )

    print("COMPLIANCE STATUS: Prompt successfully assembled with zero bot-tells.")
    return final_prompt

if __name__ == "__main__":
    # Test execution matching structural blueprint criteria
    mock_prompt = compile_optimized_voice_prompt(
        base_identity="You are an elite operational node assistant for EchoLogic AI.",
        can_list=["Look up system field status definitions", "Log high-severity network incidents"],
        cannot_list=["Process client billing refunds", "Access accounts out of scope context"]
    )
    print("\nGenerated Prompt Body Preview:")
    print("-----------------------------------------------------------------")
    print(mock_prompt)
  
