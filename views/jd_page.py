import streamlit as st

from utils.jd_matcher import match_resume_with_jd
from utils.analytics import increase_jd_match

def show_jd_page():

    st.header("🎯 Resume vs Job Description")

    resume = st.file_uploader(
        "Resume",
        type=["pdf"],
        key="jd_resume"
    )

    jd = st.text_area(
        "Paste Job Description",
        height=250,
        key="jd_text"
    )

    if not resume or not jd:
        return

    path = f"uploads/{resume.name}"

    with open(path, "wb") as f:
        f.write(resume.getbuffer())

    if st.button("Analyze Match", use_container_width=True):

        with st.spinner("Matching..."):

            result = match_resume_with_jd(path, jd)

            increase_jd_match()

        st.metric(
            "Match Score",
            f"{result['match_score']}%"
        )

        st.progress(result["match_score"] / 100)

        c1, c2 = st.columns(2)

        with c1:

            st.subheader("Matching Skills")

            for item in result["matching_skills"]:
                st.success(item)

            st.subheader("Strengths")

            for item in result["strengths"]:
                st.info(item)

        with c2:

            st.subheader("Missing Skills")

            for item in result["missing_skills"]:
                st.warning(item)

            st.subheader("Weaknesses")

            for item in result["weaknesses"]:
                st.error(item)

        st.subheader("Recommendations")

        for item in result["recommendations"]:
            st.write("✅", item)