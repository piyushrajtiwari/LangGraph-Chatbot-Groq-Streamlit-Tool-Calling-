LangGraph Chatbot (Groq + Streamlit)

A conversational AI chatbot using LangGraph, Groq LLMs, and Streamlit, with tool calling, SQLite memory, and multi-threaded conversations.

Features

1. Chat via Groq LLM (qwen/qwen3-32b)
2. Tool calling (DuckDuckGo search)
3. Persistent memory with SQLite
4. Multi-thread conversations
5. Streaming AI responses in Streamlit


Setup:
git clone <repo-url>
cd repo
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt


Create .env with:
GROQ_API_KEY=your_groq_api_key

Run:
streamlit run app.py

Notes

1. Always use messages in state (plural)
2. Append messages, don’t overwrite
3. Tools execute only when requested

License
MIT