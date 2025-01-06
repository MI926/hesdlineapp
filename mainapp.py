from transformers import pipeline

summarizer = pipeline("summarization", model="manigupta1/bertheadline")


# print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))

import streamlit as st
st.title("AI assistant")
user_input = st.text_input("You:", "")
if st.button("Send"):
    response = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
    st.text_area("Chatbot:", response, height=100)