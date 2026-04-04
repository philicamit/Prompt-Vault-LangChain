from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{Query}")
])

chat_history = []

#Load chat history
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

# print(chat_history)


#create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'Query':"Where is my refund?"})

print(prompt)