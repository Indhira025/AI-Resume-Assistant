import streamlit as st

from utils.roadmap_generator import generate_learning_roadmap
from utils.helpers import save_text


def show_roadmap_page():

    st.header("📚 AI Learning Roadmap")

    resume = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        key="roadmap_resume"
    )

    role = st.text_input(
        "Target Role",
        key="roadmap_role"
    )

    if not (resume and role):
        return

    path = f"uploads/{resume.name}"

    with open(path, "wb") as f:
        f.write(resume.getbuffer())

    if st.button(
        "Generate Roadmap",
        use_container_width=True
    ):

        with st.spinner("Preparing Roadmap..."):

            roadmap = generate_learning_roadmap(
                path,
                role
            )

        st.success("Roadmap Generated")

        st.markdown(roadmap)

        output = "outputs/learning_roadmap.md"

        save_text(output, roadmap)

        with open(output, "rb") as file:

            st.download_button(
                "Download Roadmap",
                file,
                "learning_roadmap.md",
                use_container_width=True
            )