import streamlit as st
from config.settings import APP_NAME, MODEL_NAME

def show_home():

    st.title(APP_NAME)

    st.caption("Production Ready AI Resume Optimizer")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("AI Model", MODEL_NAME)

    with c2:
        st.metric("Modules", "6")

    st.markdown("---")

    st.subheader("Features")

    st.success("📄 ATS Resume Analyzer")
    st.success("🎯 JD Matcher")
    st.success("✍ Resume Rewriter")
    st.success("📝 Cover Letter Generator")
    st.success("🎤 Interview Questions")
    st.success("📚 Learning Roadmap")