import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import base64
from langchain_ollama import ChatOllama
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="SellAPen.com", page_icon="✒️")

# Create columns for title and image
col1, col2 = st.columns([3, 1])

with col1:
    # Use Unicode pen icon directly in the title
    st.image("pen.jpg", width=400)
    st.title("SellAPen.com")

st.write("Get more information by visiting our website")

# Rest of your form code remains the same
with st.form('llm_form', clear_on_submit=True):
    st.markdown("### Ask Your Query")
    text = st.text_area("Enter your query here", height=150, placeholder="Type your question...")
    submit = st.form_submit_button("Submit Query", type="primary")


def generate_response(input_text):
    model=ChatOllama(model="llama3.2:1b",base_url="http://localhost:11434/")
    response=model.invoke(input_text)

    return response.content

import requests


if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]


if submit and text:
    with st.spinner("Generating Response..."): 
        response=generate_response(text)
        st.session_state['chat_history'].append({"user": text, "ollama":response})
        st.write(response)

st.write("## Chat History")
for chat in st.session_state['chat_history']:
    st.write(f"**User**:{chat['user']}")
    st.write(f"**Sales Guide**:{chat['ollama']}")
    st.write("---")