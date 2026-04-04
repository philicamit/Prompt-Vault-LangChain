# 🤖 Conversational AI Assistant
### A LangChain-Powered Chatbot with Session Memory

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://langchainprompt-chat.streamlit.app/)

## 🚀 Live Demo
**Access the deployed application here:** [https://langchainprompt-chat.streamlit.app/](https://langchainprompt-chat.streamlit.app/)

## 📌 Project Overview
This repository contains a functional implementation of a Large Language Model (LLM) interface using the LangChain framework. The primary objective of this project is to demonstrate **Conversational Memory Management** in a cloud-native environment, allowing for coherent multi-turn dialogue.

## 🛠️ Technical Stack
* **Language:** Python 3.14
* **Orchestration:** [LangChain](https://www.langchain.com/)
* **Model:** OpenAI GPT-4o-mini
* **Interface:** [Streamlit](https://streamlit.io/)
* **Deployment:** Streamlit Community Cloud
* **Version Control:** Git / GitHub

## 🧠 Core Functionality
* **State Persistence:** Utilizes `st.session_state` to store and inject message history into the model prompt, ensuring the AI retains context.
* **Security:** Configured with encrypted API key management via Streamlit Secrets to ensure environment variable safety.
* **Scalability:** Modular Python structure allowing for easy integration of additional tools or vector databases.

## 📂 Repository Structure
* `app.py`: The production entry point for the Streamlit application.
* `chatbot_amit.py`: A CLI-based script for local testing and development.
* `requirements.txt`: Comprehensive list of Python dependencies for environment reproduction.

---
**Developed by Amit Rastogi**