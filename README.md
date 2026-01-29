# 📈 InsightFlow AI: The Intelligent Data Analyst

**InsightFlow AI** is a Generative AI-powered agent that allows business users to query SQL databases using natural language. No SQL knowledge required—just ask your data a question and get an instant, plain-English answer.

## 🌟 Why InsightFlow AI?
In traditional business environments, data insights are locked behind technical barriers. Managers wait hours for Analysts to write SQL. InsightFlow AI removes this friction using **Agentic AI Workflows**.

### ✨ Key Features
- **Natural Language to SQL:** Conversational interface for complex database queries.
- **Self-Healing Agent:** Built with **Self-Correction** logic—the agent detects SQL errors, analyzes them, and fixes itself in real-time.
- **Metadata-Aware:** Intelligently handles multi-table JOINs (e.g., connecting Customers to Music Genres).
- **Dual Interface:** Comes with a **Streamlit Dashboard** for users and a **FastAPI Backend** for enterprise integration.

## 🛠 Tech Stack
- **Orchestration:** LangChain (ReAct Agent logic)
- **LLM:** Meta Llama 3.3-70B (via Groq)
- **Database:** SQLite (Chinook Database schema)
- **API Framework:** FastAPI
- **Frontend:** Streamlit

## 🚀 Getting Started
1. **Clone the repo:** `git clone https://github.com/YOUR_USERNAME/InsightFlow-AI`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set API Key:** Create a `.env` file and add `GROQ_API_KEY=your_key`
4. **Run App:** `streamlit run app.py`

## 📊 Sample Queries
- *"Which artist generated the most revenue?"*
- *"Show me top 5 countries by customer count."*
- *"What is the most popular music genre in the USA?"*
