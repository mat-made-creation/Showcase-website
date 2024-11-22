import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/matthew.PNG")

with col2:
    st.title("Matthew")
    content = """Hi, I am Matthew. I am learning to program in Python"""
    st.write(content)