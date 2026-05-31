from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain_openai import ChatOpenAI

def create_buffer_memory():
    return ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

def create_summary_memory(llm):
    return ConversationSummaryMemory(
        llm=llm,
        memory_key="chat_history",
        return_messages=True
    )

def get_llm(api_key: str):
    return ChatOpenAI(
        openai_api_key=api_key,
        model_name="gpt-3.5-turbo",
        temperature=0.7
    )