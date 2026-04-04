import streamlit as st
import os
import datetime
from streamlit_gsheets import GSheetsConnection
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# --- Configuration ---
st.set_page_config(page_title="AI Memory & Tracker", layout="centered")
st.title("🤖 AI Assistant with Cloud Logging")

# Initialize Keys
api_key = st.secrets["OPENAI_API_KEY"]
SHEET_URL = "https://docs.google.com/spreadsheets/d/1RkfZQrMsnCOL-ta4br9nCin8ypaTeKm_KwXy-9iW8Ac/edit?usp=sharing" # Paste your link here
DB_PATH = "chat_history_db"

model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=api_key)
embeddings = OpenAIEmbeddings(openai_api_key=api_key)

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# --- Helper Functions ---
def get_vector_store():
    if os.path.exists(DB_PATH):
        return FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    return None

# --- User Identification (Recruiter Tracker) ---
with st.sidebar:
    st.header("Visitor Log")
    user_identity = st.text_input("Enter your Name/Company to start:", placeholder="e.g., Google Recruiter")

if not user_identity:
    st.warning("Please enter your name in the sidebar to enable the chat.")
    st.stop()

# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # 1. FAISS Retrieval (Memory)
    vector_store = get_vector_store()
    context = ""
    if vector_store:
        docs = vector_store.similarity_search(prompt, k=3)
        context = "\n".join([doc.page_content for doc in docs])

    # 2. AI Response
    full_prompt = f"Past Context:\n{context}\n\nCurrent Question: {prompt}"
    response = model.invoke(full_prompt).content
    
    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # 3. Save to Google Sheets (Cloud Logging)
    new_row = {
        "Timestamp": str(datetime.datetime.now()),
        "Name": user_identity,
        "User_Message": prompt,
        "AI_Response": response
    }
    # Append the data to the sheet
    conn.create(spreadsheet=SHEET_URL, data=[new_row])

    # 4. Save to FAISS (Local Vector Storage)
    new_doc = Document(page_content=f"User: {prompt}\nAI: {response}")
    if vector_store:
        vector_store.add_documents([new_doc])
    else:
        vector_store = FAISS.from_documents([new_doc], embeddings)
    vector_store.save_local(DB_PATH)