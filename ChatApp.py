from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st

st.title("Langchain-DeepSeek-R1 app")
template1 = """Question: {question}
              Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template1)

modelUsed = OllamaLLM(model="deepseek-r1:1.5b")

chain = prompt | modelUsed

question = st.chat_input("Enter your question here")
if question: 
    st.write(chain.invoke({"question": question}))
