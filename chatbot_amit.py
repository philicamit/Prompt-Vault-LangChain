from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": response.content})
    print("AI:", response.content)


print("Chat history:", chat_history)