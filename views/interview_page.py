import streamlit as st

from utils.interview_generator import generate_interview_questions

from utils.analytics import increase_interview
def section(title, questions):

    st.subheader(title)

    for q in questions:

        with st.expander(q["question"]):

            st.write("### Answer")

            st.write(q["answer"])

            st.caption(
                f"Difficulty : {q['difficulty']}"
            )


def show_interview_page():

    st.header("🎤 AI Interview Question Generator")

    resume = st.file_uploader(
        "Resume",
        type=["pdf"],
        key="interview_resume"
    )

    role = st.text_input(
        "Job Role",
        key="interview_role"
    )

    if not (resume and role):
        return

    path = f"uploads/{resume.name}"

    with open(path, "wb") as f:
        f.write(resume.getbuffer())

    if st.button(
        "Generate Questions",
        use_container_width=True
    ):

        with st.spinner("Generating..."):

            data = generate_interview_questions(
                path,
                role
            )

            from utils.analytics import increase_interview

            increase_interview()

        tabs = st.tabs([
            "Technical",
            "HR",
            "Projects",
            "Scenario"
        ])

        with tabs[0]:
            section(
                "Technical Questions",
                data["technical_questions"]
            )

        with tabs[1]:
            section(
                "HR Questions",
                data["hr_questions"]
            )

        with tabs[2]:
            section(
                "Project Questions",
                data["project_questions"]
            )

        with tabs[3]:
            section(
                "Scenario Questions",
                data["scenario_questions"]
            )