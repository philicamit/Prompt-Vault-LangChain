import streamlit as st
from langchain_openai import ChatOpenAI
import os

# --- Page Config ---
st.set_page_config(page_title="Amit's AI Chatbot", page_icon="🤖")
st.title("💬 LangChain Chatbot with Memory")
st.markdown("This chatbot remembers our conversation! Try telling it your name.")

# --- API Key Setup ---
# When deployed, Streamlit gets keys from "Secrets", not .env
api_key = st.secrets["OPENAI_API_KEY"]
model = ChatOpenAI(openai_api_key=api_key)

# --- Session State (The "Memory" for Web) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Say something..."):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        response = model.invoke(st.session_state.messages)
        full_response = response.content
        st.markdown(full_response)
    
    # Add assistant message to state
    st.session_state.messages.append({"role": "assistant", "content": full_response})