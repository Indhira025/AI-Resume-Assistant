"""
Reusable Sidebar
"""

import streamlit as st

from config.settings import MODEL_NAME


def render_sidebar():

    with st.sidebar:

        st.title("AI Resume Optimizer")

        st.divider()

        st.success("ATS Analyzer")

        st.success("JD Matcher")

        st.success("Resume Rewriter")

        st.success("Cover Letter")

        st.success("Interview Questions")

        st.success("Learning Roadmap")

        st.divider()

        st.write("Model")

        st.info(MODEL_NAME)