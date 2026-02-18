import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# -------------------------------
# SET YOUR API KEY
# -------------------------------

# load environment variables
load_dotenv()

# get api key from .env file
api_key = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=api_key)

# Use Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')



st.title("💬 Gemini Chat App")

# Initialize chat history
# without sessions, chats are not stored
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display previous messages
for message in st.session_state.chat.history:
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Chat input
if prompt := st.chat_input("Type your message..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.chat.send_message(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.text)
