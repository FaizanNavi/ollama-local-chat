from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

templates = """

Answer the question below.

here is conversation : {context}

question: {question}

answer:
"""

model = OllamaLLM(model='phi3')

prompt = ChatPromptTemplate.from_template(templates)

chain = prompt | model


def handle_converstations():
    context = ""
    print("welcome to customer support BOT")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context,"question": user_input})
        print("Bot: ",result)
        context += f"\nUser: {user_input}\n\nBot: {result}"

if __name__ == "__main__":
    handle_converstations()