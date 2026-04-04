import os
from xml.parsers.expat import model
import streamlit as st
from langchain_groq import ChatGroq  
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.7
)

st.header('Research Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt("template.json")

prompt = template.invoke(
    {'paper_input': paper_input,
     'style_input': style_input,
     'length_input': length_input},
     validate_template=True
     )

if st.button('Summarize'):
    chain = template | llm
    result = chain.invoke(
        {'paper_input': paper_input,
         'style_input': style_input,
         'length_input': length_input},
         validate_template=True
         )
    st.write(result.content)


