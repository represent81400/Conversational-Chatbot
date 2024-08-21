from langchain_openai import OpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st
import os 

load_dotenv()

st.set_page_config(page_title='Q&A Chatbot')
st.header("Let's Chat")

#Load OpenAI model


def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm(question)
    return response
    

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)


submit = st.button("Ask the question")

if submit:
    st.write(response)


