from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
        ("system", "You are a helpful {domain} assistant."),
        ("human", "Explain in simple terms what {topic} is.")
    ])

prompt = chat_template.invoke({"domain": "programming", "topic": "Python"})

print(prompt)