import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("✨ AI Personal Brand Statement Generator")

user_input = st.text_area("Tell me briefly about your skills, experiences, interests, and career goals:")

if st.button("Generate Brand Statement"):
    if user_input:
        prompt = f"""
        Based on the details provided, generate a concise, engaging, and professional personal brand statement suitable for a LinkedIn profile.

        User Details:
        "{user_input}"

        Keep it professional, engaging, and limited to around 50-60 words.
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.8
        )

        statement = response['choices'][0]['message']['content']
        st.subheader("Your Personal Brand Statement 🚀")
        st.write(statement)

        st.success("Copy and share your new statement on LinkedIn!")
    else:
        st.warning("Please enter details about yourself!")
