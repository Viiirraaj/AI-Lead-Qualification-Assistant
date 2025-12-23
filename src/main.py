import pandas as pd
from llm_intent import analyze_intents_batch

df = pd.read_csv("C:/Users/VIRAJ/OneDrive/Desktop/lead-qualification-ai/data/leads.csv")

def keyword_intent(text):
    keywords = ["urgent", "price", "demo", "call", "buy", "pricing"]
    return any(k in text.lower() for k in keywords)

# ---------- LLM BATCH CALL ----------
messages = df["message"].tolist()
llm_text = analyze_intents_batch(messages)

llm_results = {}

def parse_block(block):
    intent = "Medium"
    urgency = "Not Urgent"
    reason = "LLM analysis unavailable"

    for line in block.split("\n"):
        if "Intent:" in line:
            intent = line.split("Intent:")[1].strip()
        elif "Urgency:" in line:
            urgency = line.split("Urgency:")[1].strip()
        elif "Reason:" in line:
            reason = line.split("Reason:")[1].strip()

    return intent, urgency, reason

if llm_text:
    blocks = llm_text.strip().split("\n\n")
    for i, block in enumerate(blocks):
        intent, urgency, reason = parse_block(block)
        llm_results[i] = {
            "intent": intent,
            "urgency": urgency,
            "reason": reason
        }

# ---------- SCORING ----------
def score_lead(idx, row):
    score = 0
    reasons = []

    if keyword_intent(row["message"]):
        score += 3
        reasons.append("Keywords detected")

    if row["source"].lower() == "referral":
        score += 2
        reasons.append("Referral source")

    if row["budget"].lower() == "yes":
        score += 2
        reasons.append("Budget mentioned")

    if row["response_time_minutes"] < 10:
        score += 1
        reasons.append("Quick response")

    if idx in llm_results:
        if llm_results[idx]["intent"] == "High":
            score += 3
            reasons.append("LLM: High intent")

        if llm_results[idx]["urgency"] == "Urgent":
            score += 2
            reasons.append("LLM: Urgent")

    return score, ", ".join(reasons)

def classify(score):
    if score >= 7:
        return "Hot"
    elif score >= 4:
        return "Warm"
    return "Cold"

df[["score", "reason"]] = [
    score_lead(i, row) for i, row in df.iterrows()
]

df["category"] = df["score"].apply(classify)

df.to_csv("C:/Users/VIRAJ/OneDrive/Desktop/lead-qualification-ai/output/qualified_leads.csv", index=False)

print(df[["name", "score", "category"]])

