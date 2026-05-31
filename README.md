# Chatbot with Memory

A conversational AI chatbot that remembers what you said earlier in the conversation, built using Python, LangChain, and Streamlit.

## What it does

Most chatbots forget everything after each message. This chatbot stores the full conversation history and sends it along with every new message — so it can refer back to anything you said earlier.

Example: You say "My name is Jyothi" and three messages later ask "What is my name?" — it answers correctly.

## Tech Stack

- Python 3.13
- LangChain
- Ollama (runs AI locally for free)
- Llama 3.2 model
- Streamlit (web UI)

## How to run it

1. Install Python from python.org

2. Install Ollama from ollama.com

3. Pull the model:
   ollama pull llama3.2

4. Install dependencies:
   pip install langchain streamlit langchain-openai python-dotenv langchain-ollama

5. Run the app:
   streamlit run app.py

6. Open your browser at http://localhost:8501

## How memory works

Every time you send a message, the entire conversation history is included in the request to the AI. So the AI always has full context of everything said before.

## What I learned

- How LLMs handle conversation history
- Context window limitations
- How to build a web app with Streamlit
- How to run AI models locally using Ollama
- How to connect Python with LangChain
