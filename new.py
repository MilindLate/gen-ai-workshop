import streamlit as st
import pandas as pd 
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv

def generate_poetry(prompt):
    if prompt:
        msg = st.toast("Gathering inspiration...")
        time.sleep(2)
        msg = st.toast("Crafting verses...")
        time.sleep(2)
        msg = st.toast("Ready!", icon="✨")
        time.sleep(2)
        st.write(f"Creating a poem about: {prompt}")
        time.sleep(1)
        st.write("Here's your poem:")
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(f"Write a beautiful and creative poem about {prompt}")
        st.write(response.text)

# a function to pull up images goes here
# I will write this function later 

if __name__=="__main__":
    load_dotenv()
    API_KEY = os.getenv('GEMINI_API_KEY')
    # initialize the client
    genai.configure(api_key=API_KEY)
    # title 
    st.title("✨ Poetry Generator ✨")
    prompt = st.chat_input("What inspires you today?")
    generate_poetry(prompt)
