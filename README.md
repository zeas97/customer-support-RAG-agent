# Customer Support RAG Agent 🤖

A retrieval-augmented generation (**RAG**) system for customer support using **Google Gemini** and **ChromaDB**.

## Features ✨
- **Retrieval-Augmented Generation (RAG)** for precise responses
- **Semantic search** with **ChromaDB**
- **Google Gemini 2.0 Flash** for AI-powered answers
- **Session-based memory** to maintain context across interactions
- **Secure API key storage** using `.env` file
- **Color-coded command-line interface** for easy interaction

---
## How It Works 🔍
This project combines **semantic search** and **AI response generation** to deliver accurate customer support answers.

1. **ChromaDB** stores **products and policies** as vector embeddings.
2. **User queries** are matched with the most relevant knowledge.
3. **Google Gemini** generates a **natural response** based on retrieved data.
4. **Session memory** ensures the AI remembers recent conversations.

---
## Requirements 👋

Ensure you have the following installed:

- **Python 3.12**
- **Google Gemini API Key**

---
## Installation ⚙️

Follow these steps to set up the project:

### 1. Set Up the Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Obtain and Set Up the Google Gemini API Key
To use **Google Gemini**, you need an API key:

1. Go to [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Navigate to **API Keys**
4. Generate a new API key and copy it
5. **Create a `.env` file in the project root and add:**
   ```sh
   GEMINI_API_KEY=your_api_key_here
   ```

### 4. Run the Customer Support AI Agent
Start the chatbot with:
```sh
python main.py
```

---
## Usage
- Type your **customer support queries** in the terminal.
- The AI will **retrieve knowledge** and generate a response.
- Type **`exit`** to end the session.

---
## Example Questions & Answers 📚

**Q:** "What is the price of the UltraPhone X?"

**A:** "The UltraPhone X costs **$799**. It's available in **Black, Silver, and Blue** colors."

---

**Q:** "What are your shipping options?"

**A:** "We offer **standard shipping (3-5 business days) for $4.99** and **express shipping (1-2 business days) for $12.99**. Orders over $50 qualify for **free shipping**."

---

**Q:** "Can I return an opened item?"

**A:** "Yes, but a **15% restocking fee** may apply. The item must be within the **30-day return period**."

---
## Troubleshooting 🛠️
- **API Key Errors**: Ensure `GEMINI_API_KEY` is correctly set in the `.env` file.
- **Database Issues**: If `chroma_db` is missing, delete it and restart the agent.
- **Missing Dependencies**: Run `pip install -r requirements.txt`.
- **Network Issues**: Check your **internet connection** and **Google API limits**.

---
## Future Improvements 🚀
- **Web API** integration using **FastAPI**
- **Persistent session memory** for longer interactions
- **Enhanced query processing** with fuzzy matching

---

🎉 Enjoy using the **Customer Support RAG AI Agent**! Let Me know if you have any questions. 🚀

