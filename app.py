import streamlit as st

from config.settings import APP_NAME, MODEL_NAME
from config.logging_config import setup_logger

from utils.helpers import (
    create_directory,
    load_css
)

from views.home import show_home
from views.ats_page import show_ats_page
from views.jd_page import show_jd_page
from views.rewrite_page import show_resume_rewriter_page
from views.cover_letter_page import show_cover_letter_page
from views.interview_page import show_interview_page
from views.roadmap_page import show_roadmap_page
from views.about import show_about_page

# ---------------------------------------------------
# Logger
# ---------------------------------------------------

logger = setup_logger()

# ---------------------------------------------------
# Create directories
# ---------------------------------------------------

create_directory("uploads")
create_directory("outputs")
create_directory("logs")

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Load CSS
# ---------------------------------------------------

load_css("assets/style.css")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.image(
        "assets/logo.png",
        width=130
    )

    st.title("AI Resume Optimizer")

    st.caption(
        "Production Ready AI Project"
    )

    page = st.radio(

        "Navigation",

        [

            "🏠 Home",

            "📄 ATS Resume Analyzer",

            "🎯 JD Matcher",

            "✍ Resume Rewriter",

            "📝 Cover Letter",

            "🎤 Interview Questions",

            "📚 Learning Roadmap",

            "ℹ About"

        ]

    )

    st.markdown("---")

    st.success(
        f"Model : {MODEL_NAME}"
    )

    st.markdown("---")

    st.caption(
        "Version 1.0"
    )

# ---------------------------------------------------
# Pages
# ---------------------------------------------------

if page == "🏠 Home":

    show_home()

elif page == "📄 ATS Resume Analyzer":

    show_ats_page()

elif page == "🎯 JD Matcher":

    show_jd_page()

elif page == "✍ Resume Rewriter":

    show_resume_rewriter_page()

elif page == "📝 Cover Letter":

    show_cover_letter_page()

elif page == "🎤 Interview Questions":

    show_interview_page()

elif page == "📚 Learning Roadmap":

    show_roadmap_page()

elif page == "ℹ About":

    show_about_page()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("---")

st.caption(
    "AI Resume Optimizer & Interview Assistant"
)

st.caption(
    "Powered by Python • Streamlit • Ollama • Prompt Engineering"
)