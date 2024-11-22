import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/matthew.PNG")

with col2:
    st.title("Matthew")
    content = """Hi, I am Matthew. I am learning to program in Python"""
    st.write(content)

content2 = """Here are some examples of apps that I have created in Python"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"])