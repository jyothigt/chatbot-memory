import streamlit as st
from langchain_ollama import ChatOllama

st.set_page_config(page_title="Chatbot with Memory", page_icon="🧠")
st.title("🧠 Chatbot with Memory")

with st.sidebar:
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                llm = ChatOllama(model="llama3.2")
                st.session_state.history.append({"role": "user", "content": user_input})
                messages = [{"role": "system", "content": "You are a helpful and friendly AI assistant with a good memory."}]
                messages += st.session_state.history
                response = llm.invoke(messages)
                answer = response.content
                st.session_state.history.append({"role": "assistant", "content": answer})
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {e}")