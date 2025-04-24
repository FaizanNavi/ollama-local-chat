from tempfile import template
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
formatted_prompt = prompt.format(context="", question="hey i am studing research paper by the name of Attention is all you need can you give me brief on it")

def handle_conversation():
    context = ""
    print("hello")

result = model.invoke(formatted_prompt)
print(result)
