import streamlit as st

from utils.cover_letter import generate_cover_letter
from utils.helpers import save_text
from utils.analytics import increase_cover_letter

def show_cover_letter_page():

    st.header("📝 AI Cover Letter Generator")

    resume = st.file_uploader(
        "Resume",
        type=["pdf"],
        key="cover_resume"
    )

    company = st.text_input("Company")

    role = st.text_input("Job Role")

    jd = st.text_area(
        "Job Description",
        height=250
    )

    if not (resume and company and role and jd):
        return

    path = f"uploads/{resume.name}"

    with open(path, "wb") as f:
        f.write(resume.getbuffer())

    if st.button("Generate Cover Letter", use_container_width=True):

        with st.spinner("Generating..."):

            letter = generate_cover_letter(
                path,
                company,
                role,
                jd
            )

            from utils.analytics import increase_cover_letter

            increase_cover_letter()

        st.success("Completed")

        st.text_area(
            "Cover Letter",
            letter,
            height=500
        )

        output = "outputs/cover_letter.txt"

        save_text(output, letter)

        with open(output, "rb") as file:

            st.download_button(
                "Download",
                file,
                "cover_letter.txt",
                use_container_width=True
            )