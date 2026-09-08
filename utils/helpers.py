from pathlib import Path
from datetime import datetime

from config.logging_config import setup_logger

logger = setup_logger()


def create_directory(directory_path: str) -> Path:
    """
    Create a directory if it does not exist.

    Args:
        directory_path (str): Directory path.

    Returns:
        Path: Path object of the directory.
    """

    path = Path(directory_path)

    path.mkdir(parents=True, exist_ok=True)

    logger.info(f"Directory ready: {path}")

    return path


def file_exists(file_path: str) -> bool:
    """
    Check whether a file exists.

    Args:
        file_path (str): File path.

    Returns:
        bool
    """

    exists = Path(file_path).is_file()

    logger.info(f"File exists: {exists} -> {file_path}")

    return exists


def get_file_extension(filename: str) -> str:
    """
    Return file extension.

    Args:
        filename (str)

    Returns:
        str
    """

    return Path(filename).suffix.lower().replace(".", "")


def get_current_timestamp() -> str:
    """
    Return current timestamp.

    Returns:
        str
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_text(file_path: str, text: str):
    """
    Save text to a file.
    """

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

    logger.info(f"Saved file: {file_path}")

from pathlib import Path
import streamlit as st


def load_css(css_path: str):
    """
    Load external CSS into Streamlit.

    Parameters
    ----------
    css_path : str
        Path of CSS file.
    """

    css_file = Path(css_path)

    if css_file.exists():

        with open(css_file, "r", encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    else:

        print(f"CSS file not found : {css_path}")

from pathlib import Path
from config.constants import UPLOAD_DIR


def save_uploaded_file(uploaded_file) -> str:
    """
    Save a Streamlit uploaded file.

    Args:
        uploaded_file: UploadedFile object from Streamlit.

    Returns:
        str: Saved file path.
    """

    upload_path = Path(UPLOAD_DIR)
    upload_path.mkdir(parents=True, exist_ok=True)

    file_path = upload_path / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    logger.info(f"Uploaded file saved: {file_path}")

    return str(file_path)