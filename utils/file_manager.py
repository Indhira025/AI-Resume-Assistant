"""
File Manager Utility

Handles all file operations used
throughout the application.

Author : AI Resume Optimizer
"""

from pathlib import Path
from typing import Optional
import shutil

from config.logging_config import setup_logger

logger = setup_logger()


# ---------------------------------------------------
# Create Folder
# ---------------------------------------------------

def create_directory(directory: str) -> Path:
    """
    Create a directory if it doesn't exist.

    Args:
        directory (str)

    Returns:
        Path
    """

    path = Path(directory)

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    logger.info(
        f"Directory ready : {path}"
    )

    return path


# ---------------------------------------------------
# Save Uploaded File
# ---------------------------------------------------

def save_uploaded_file(
    uploaded_file,
    upload_dir: str = "uploads"
) -> str:
    """
    Save a Streamlit uploaded file.

    Args:
        uploaded_file
        upload_dir

    Returns:
        Saved file path
    """

    create_directory(upload_dir)

    file_path = Path(upload_dir) / uploaded_file.name

    with open(file_path, "wb") as file:

        file.write(
            uploaded_file.getbuffer()
        )

    logger.info(
        f"File saved : {file_path}"
    )

    return str(file_path)


# ---------------------------------------------------
# Save Text File
# ---------------------------------------------------

def save_text_file(
    text: str,
    filename: str,
    output_dir: str = "outputs"
) -> str:
    """
    Save AI output as text file.

    Args:
        text
        filename
        output_dir

    Returns:
        File path
    """

    create_directory(output_dir)

    file_path = Path(output_dir) / filename

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

    logger.info(
        f"Text saved : {file_path}"
    )

    return str(file_path)


# ---------------------------------------------------
# Read Text File
# ---------------------------------------------------

def read_text_file(
    file_path: str
) -> str:
    """
    Read a text file.

    Args:
        file_path

    Returns:
        str
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    logger.info(
        f"Read file : {file_path}"
    )

    return text


# ---------------------------------------------------
# Delete File
# ---------------------------------------------------

def delete_file(
    file_path: str
) -> bool:
    """
    Delete a file.

    Args:
        file_path

    Returns:
        bool
    """

    path = Path(file_path)

    if path.exists():

        path.unlink()

        logger.info(
            f"Deleted : {file_path}"
        )

        return True

    logger.warning(
        f"File not found : {file_path}"
    )

    return False


# ---------------------------------------------------
# Copy File
# ---------------------------------------------------

def copy_file(
    source: str,
    destination: str
) -> str:
    """
    Copy file.

    Args:
        source
        destination

    Returns:
        Destination path
    """

    shutil.copy2(
        source,
        destination
    )

    logger.info(
        f"Copied {source} -> {destination}"
    )

    return destination


# ---------------------------------------------------
# Move File
# ---------------------------------------------------

def move_file(
    source: str,
    destination: str
) -> str:
    """
    Move file.

    Args:
        source
        destination

    Returns:
        Destination path
    """

    shutil.move(
        source,
        destination
    )

    logger.info(
        f"Moved {source} -> {destination}"
    )

    return destination


# ---------------------------------------------------
# File Exists
# ---------------------------------------------------

def file_exists(
    file_path: str
) -> bool:
    """
    Check file exists.

    Args:
        file_path

    Returns:
        bool
    """

    exists = Path(file_path).exists()

    logger.info(
        f"Exists ({exists}) : {file_path}"
    )

    return exists


# ---------------------------------------------------
# Get Extension
# ---------------------------------------------------

def get_extension(
    file_path: str
) -> str:
    """
    Return file extension.

    Args:
        file_path

    Returns:
        str
    """

    return Path(file_path).suffix.lower()


# ---------------------------------------------------
# Get File Name
# ---------------------------------------------------

def get_filename(
    file_path: str
) -> str:
    """
    Return filename.

    Args:
        file_path

    Returns:
        str
    """

    return Path(file_path).name


# ---------------------------------------------------
# Get File Size
# ---------------------------------------------------

def get_file_size(
    file_path: str
) -> float:
    """
    File size in MB.

    Args:
        file_path

    Returns:
        float
    """

    size = (
        Path(file_path).stat().st_size
        / (1024 * 1024)
    )

    return round(size, 2)


# ---------------------------------------------------
# Clear Folder
# ---------------------------------------------------

def clear_directory(
    directory: str
):
    """
    Delete all files inside a folder.

    Args:
        directory
    """

    folder = Path(directory)

    if not folder.exists():
        return

    for item in folder.iterdir():

        if item.is_file():

            item.unlink()

    logger.info(
        f"Cleared : {directory}"
    )