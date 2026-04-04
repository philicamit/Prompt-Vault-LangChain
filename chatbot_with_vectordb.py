import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

load_dotenv()

# 1. Initialize Model and Embeddings
model = ChatOpenAI(model="gpt-4o-mini")
embeddings = OpenAIEmbeddings()

# 2. Setup Vector Store Path
DB_PATH = "chat_history_db"

def get_vector_store():
    if os.path.exists(DB_PATH):
        return FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    return None

print("System: Chatbot is ready. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # 3. Retrieve Relevant Past Context
    vector_store = get_vector_store()
    context = ""
    if vector_store:
        # Search for top 3 most relevant past messages
        docs = vector_store.similarity_search(user_input, k=3)
        context = "\n".join([doc.page_content for doc in docs])

    # 4. Construct Prompt with Memory
    full_prompt = f"Past Context:\n{context}\n\nCurrent User Question: {user_input}"
    
    response = model.invoke(full_prompt)
    ai_response = response.content
    print(f"AI: {ai_response}")

    # 5. Save the Interaction to Vector DB
    new_data = f"User: {user_input}\nAssistant: {ai_response}"
    new_doc = Document(page_content=new_data)
    
    if vector_store:
        vector_store.add_documents([new_doc])
    else:
        vector_store = FAISS.from_documents([new_doc], embeddings)
    
    # Save locally to disk
    vector_store.save_local(DB_PATH)