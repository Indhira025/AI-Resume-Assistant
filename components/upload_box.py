"""
Upload Component
"""

import streamlit as st


def pdf_upload(key):

    return st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        key=key
    )