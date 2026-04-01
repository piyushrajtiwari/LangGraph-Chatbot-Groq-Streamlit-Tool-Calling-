# 🚀 LangGraph Chatbot

**Groq LLM + Streamlit + Tool Calling + Persistent Memory**

An advanced conversational AI chatbot built using **LangGraph**, powered by **Groq LLMs**, with **real-time streaming UI in Streamlit**, **tool integration**, and **persistent multi-thread memory using SQLite**.

---

## ✨ Features

* ⚡ Ultra-fast LLM responses using Groq (`qwen3-32b`)
* 🔗 LangGraph-based agent workflow
* 🧠 Persistent memory with SQLite
* 🧵 Multi-threaded conversations
* 🌐 Tool calling support (DuckDuckGo search)
* 📡 Streaming responses in real-time UI
* 🎯 State-managed conversations (LangGraph best practices)
* 💻 Clean and interactive Streamlit UI

---

## 🏗️ Architecture Overview

User Input → Streamlit UI → LangGraph Agent
→ Tool Execution (if needed)
→ Groq LLM Response
→ SQLite Memory Storage
→ Streamed Output

---

## 🧠 Tech Stack

* **LLM**: Groq (`qwen/qwen3-32b`)
* **Framework**: LangGraph
* **Frontend**: Streamlit
* **Memory**: SQLite
* **Tools**: DuckDuckGo Search API
* **Language**: Python

---

## 📂 Project Structure

```
├── app.py                # Streamlit UI
├── graph.py              # LangGraph workflow
├── tools.py              # Tool definitions (search, etc.)
├── memory.db             # SQLite database (auto-created)
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/piyushrajtiwari/langgraph-chatbot.git
cd langgraph-chatbot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open:
http://localhost:8501

---

## 💡 Usage

* Enter your query in the chat UI
* The agent:

  * Decides whether to call tools
  * Retrieves information if needed
  * Generates a response using Groq
* Conversations are stored and can be resumed (multi-thread support)

---

## ⚠️ Important Notes

* Always use `messages` (plural) in LangGraph state
* Append messages instead of overwriting state
* Tool execution happens only when explicitly triggered by the LLM
* SQLite DB (`memory.db`) is auto-created on first run

---

## 🔥 Example Capabilities

* Ask factual questions → uses search tool
* Continue previous chats → memory retained
* Handle multiple sessions → thread-based memory
* Real-time streaming responses

---

## 🚧 Future Improvements

* 🔍 Add vector database (FAISS / Chroma)
* 🧾 RAG pipeline integration
* 🗂️ File upload & document chat
* 🧠 Long-term memory optimization
* 🌍 Multi-agent workflows

---

## 🤝 Contributing

Contributions are welcome!

```
fork → clone → create branch → commit → push → PR
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🧑‍💻 Use it in your own projects
