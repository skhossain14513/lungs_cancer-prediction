import streamlit as st
from pathlib import Path

# Function to read markdown files


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


# Dictionary to map page names to their respective files
pages = {
    "Home": "pages/home.py",
    "Motivation": "pages/motivation.py",
    "Objectives": "pages/objectives.py",
    "Related Study": "pages/related_study.py",
    "Methodology": "pages/methodology.py",
    "Results": "pages/results.py",
    "Prediction": "pages/prediction.py"
}

# Streamlit sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
page = pages[selection]
exec(Path(page).read_text())
