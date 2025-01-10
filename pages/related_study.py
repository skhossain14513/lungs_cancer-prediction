import streamlit as st 
from pathlib import Path 
 
st.title("Related Study") 
 
def read_markdown_file(markdown_file): 
    return Path(markdown_file).read_text() 
 
related_study_text = read_markdown_file("related_study.md") 
st.markdown(related_study_text) 
