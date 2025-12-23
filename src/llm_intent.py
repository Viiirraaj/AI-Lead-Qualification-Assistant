import google.generativeai as genai
import time

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("models/gemini-2.5-flash")

def analyze_intents_batch(messages):
    numbered_msgs = "\n".join(
        [f"{i+1}. {msg}" for i, msg in enumerate(messages)]
    )

    prompt = f"""
You are a sales assistant.

For EACH lead message below, classify:
Intent: High / Medium / Low
Urgency: Urgent / Not Urgent
Reason: short explanation

Messages:
{numbered_msgs}

Return response in SAME ORDER.
Each result separated by a blank line.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("⚠️ LLM unavailable, skipping LLM scoring")
        return None
