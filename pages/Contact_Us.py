import streamlit as st
from send_email import sent_email

st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    subject_line = st.text_input("Email subject line")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: {subject_line}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        sent_email(message)
        st.info("Your email was sent successfully")