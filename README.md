# 👋 Hi, I’m Viraj Shinde

🎓 MSc Computer Science Student  
🤖 AI / ML | Automation | Backend  
💡 Interested in building **AI systems that solve real business problems**

I focus on **practical, business-first AI** — not just models, but systems that save time, reduce cost, and improve decisions.

---

## 🧠 My Core Approach (AI + Business)
- Start from a **real-world problem**
- Measure **business impact**
- Use AI only where it adds value
- Build **simple, explainable MVPs**
- Optimize for **reliability over hype**

---

## 🚀 Featured Project: AI Lead Qualification Assistant  
**(LLM + Business Rules)**

### 🔍 Problem
Sales teams often lose revenue because:
- High-intent leads are contacted late
- Time is wasted on low-quality leads
- All leads are treated equally

This results in **low conversion and inefficiency**.

---

### 💡 Solution
An **AI-powered lead qualification system** that automatically classifies leads as:

- 🔥 **Hot**
- 🌤️ **Warm**
- ❄️ **Cold**

using:
- Transparent **rule-based scoring**
- **LLM-based intent analysis (Gemini)** for understanding human language

---

### ⚙️ How It Works
1. Reads lead data from a CSV file
2. Applies business rules:
   - Referral source
   - Budget mentioned
   - Response time
   - High-intent keywords
3. Uses a **Gemini LLM (batch mode)** to detect:
   - Buying intent
   - Urgency
4. Combines both signals
5. Outputs:
   - Lead score
   - Category (Hot / Warm / Cold)
   - Clear reason for classification

---

### 🧩 ArchitectureLeads CSV
↓
Rule-Based Scoring
↓
LLM Intent Analysis (Batch)
↓
Final Score + Category + Reason

---

### 🛠️ Tech Stack
- Python 3.11
- Pandas
- Google Gemini API (LLM)
- CSV-based I/O (MVP-friendly)

---

### 📂 Project Structure
lead-qualification-ai/
│
├── data/leads.csv
├── src/
│ ├── llm_intent.py
│ └── main.py
├── output/qualified_leads.csv
├── generate_leads.py
└── requirements.txt


---

### 📈 Scoring Logic (Simplified)
| Signal | Score |
|------|------|
High-intent keywords | +3 |
Referral source | +2 |
Budget mentioned | +2 |
Fast response | +1 |
LLM High Intent | +3 |
LLM Urgent | +2 |

**Final Classification**
- Hot → Score ≥ 7  
- Warm → Score 4–6  
- Cold → Score ≤ 3  

---

### ✅ Engineering Highlights
- **Batch LLM calls** to handle API rate limits
- **Rule + LLM hybrid design** for reliability
- **Robust parsing** for unpredictable LLM outputs
- Business-first MVP mindset

---

### 📊 Output Example
Rahul → Score: 8 → Hot
Sneha → Score: 9 → Hot
Amit → Score: 2 → Cold


Each lead includes a **clear explanation** of why it was classified that way.

---

### 🧠 Business Impact
- Faster response to high-value leads
- Reduced wasted sales effort
- Improved conversion without increasing team size

---

### 🗣️ How I Explain This Project
> “I built an AI-based lead qualification system that combines transparent business rules with LLM intent analysis to help sales teams focus on high-value leads.”

---

## 🔮 Future Work
- Email alerts for Hot leads
- REST API for CRM integration
- Sales dashboard
- Analytics and caching
- Risk & anomaly detection system

---

## 📫 Let’s Connect
- 📍 Mumbai, India  
- 💼 Open to internships & AI-focused roles  
- 📧 Email: virajshinde911@gmail.com  

---

**I aim to build AI systems that make sense for businesses, not just benchmarks.**

