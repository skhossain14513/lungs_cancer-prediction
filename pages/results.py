import streamlit as st 
from pathlib import Path 
 
st.title("Results") 
 
def read_markdown_file(markdown_file): 
    return Path(markdown_file).read_text() 
 
results_text = read_markdown_file("results.md") 
st.markdown(results_text) 
