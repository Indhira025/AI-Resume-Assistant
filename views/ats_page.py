import streamlit as st

from utils.ats import analyze_resume
from utils.helpers import save_uploaded_file

from utils.analytics import add_ats_score


def show_ats_page():

    st.header("📄 ATS Resume Analyzer")

    resume = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        key="ats_resume"
    )

    if resume is None:
        return

    resume_path = save_uploaded_file(resume)

    if st.button(
        "Analyze Resume",
        type="primary"
    ):

        with st.spinner("Analyzing Resume..."):

            try:

                report = analyze_resume(resume_path)

                # Save score for dashboard analytics
                add_ats_score(
                    report["ats_score"]
                )

            except Exception as e:

                st.error(str(e))
                return

        st.success("Analysis Completed Successfully")

        # -----------------------------
        # ATS Score
        # -----------------------------

        st.metric(
            "ATS Score",
            f'{report["ats_score"]}%'
        )

        st.progress(
            max(
                min(report["ats_score"], 100),
                0
            ) / 100
        )

        st.divider()

        col1, col2 = st.columns(2)

        # -----------------------------
        # Left Column
        # -----------------------------

        with col1:

            st.subheader("✅ Strengths")

            if report["strengths"]:

                for item in report["strengths"]:
                    st.success(item)

            else:
                st.info("No strengths found.")

            st.subheader("⚠ Missing Skills")

            if report["missing_skills"]:

                for item in report["missing_skills"]:
                    st.warning(item)

            else:
                st.info("No missing skills found.")

        # -----------------------------
        # Right Column
        # -----------------------------

        with col2:

            st.subheader("❌ Weaknesses")

            if report["weaknesses"]:

                for item in report["weaknesses"]:
                    st.error(item)

            else:
                st.info("No weaknesses found.")

            st.subheader("📝 Grammar Issues")

            if report["grammar_issues"]:

                for item in report["grammar_issues"]:
                    st.info(item)

            else:
                st.info("No grammar issues found.")

        st.divider()

        st.subheader("🚀 Recommendations")

        if report["recommendations"]:

            for item in report["recommendations"]:
                st.write("✅", item)

        else:

            st.info("No recommendations available.")