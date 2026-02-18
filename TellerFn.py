import streamlit as st
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv

def generate_story(prompt, author):
    if prompt and author:
        msg = st.toast("Gathering inspiration...")
        time.sleep(1)
        msg = st.toast("Crafting your story...")
        time.sleep(1)
        
        st.write(f"**Story Topic:** {prompt}")
        st.write(f"**Author Style:** {author}")
        st.write("---")
        
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content([
                f"Write a captivating short story about: {prompt}",
                f"Write it in the style of {author}"
            ])
            st.toast("Story ready!", icon="📖")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error generating story: {e}")

if __name__=="__main__":
    load_dotenv()
    API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=API_KEY)
    
    st.title("📖 AI Story Teller")
    st.markdown("Create stories in the style of your favorite authors")
    
    col1, col2 = st.columns(2)
    
    with col1:
        prompt = st.text_input("Story topic:", placeholder="e.g., A lost treasure in the mountains")
    
    with col2:
        author = st.text_input("Author style:", placeholder="e.g., Ruskin Bond, Edgar Allan Poe")
    
    if st.button("Generate Story", type="primary"):
        if prompt and author:
            generate_story(prompt, author)
        else:
            st.warning("Please enter both story topic and author style!")
