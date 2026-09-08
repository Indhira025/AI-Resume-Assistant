import streamlit as st

def show_about_page():

    st.title("About")

    st.markdown("""
## AI Resume Optimizer & Interview Assistant

Version **1.0**

### Built With

- Python
- Streamlit
- Ollama
- Prompt Engineering
- Pydantic
- PyMuPDF

### Features

- ATS Analysis
- JD Matching
- Resume Rewrite
- Cover Letter
- Interview Questions
- Learning Roadmap
""")