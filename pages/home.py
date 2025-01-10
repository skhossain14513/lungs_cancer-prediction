import streamlit as st
from pathlib import Path

st.title("Home")


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


home_text = read_markdown_file("home.md")
st.markdown(home_text)
