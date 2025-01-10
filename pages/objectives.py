import streamlit as st 
from pathlib import Path 
 
st.title("Objectives") 
 
def read_markdown_file(markdown_file): 
    return Path(markdown_file).read_text() 
 
objectives_text = read_markdown_file("objectives.md") 
st.markdown(objectives_text) 
