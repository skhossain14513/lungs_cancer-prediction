import streamlit as st 
from pathlib import Path 
 
st.title("Methodology") 
 
def read_markdown_file(markdown_file): 
    return Path(markdown_file).read_text() 
 
methodology_text = read_markdown_file("methodology.md") 
st.markdown(methodology_text) 
