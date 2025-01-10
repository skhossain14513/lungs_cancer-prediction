import streamlit as st 
from pathlib import Path 
 
st.title("Motivation") 
 
def read_markdown_file(markdown_file): 
    return Path(markdown_file).read_text() 
 
motivation_text = read_markdown_file("motivation.md") 
st.markdown(motivation_text) 
