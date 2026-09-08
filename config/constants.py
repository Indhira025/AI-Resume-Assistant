'''SUPPORTED_FILE_TYPES = [
    "pdf"
]

DEFAULT_ENCODING = "utf-8"

APP_VERSION = "1.0.0"

AUTHOR = "Indhira Rongali"  '''

"""
Application Constants
"""

# -----------------------------
# Supported Files
# -----------------------------

SUPPORTED_FILE_TYPES = [
    "pdf"
]

# -----------------------------
# Directories
# -----------------------------

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
LOG_DIR = "logs"
PROMPT_DIR = "prompts"

# -----------------------------
# AI Model
# -----------------------------

DEFAULT_MODEL = "llama3.2"

# -----------------------------
# ATS
# -----------------------------

MIN_ATS_SCORE = 0
MAX_ATS_SCORE = 100

# -----------------------------
# File Names
# -----------------------------

ATS_PROMPT = "ats_prompt.txt"
JD_PROMPT = "jd_prompt.txt"
REWRITE_PROMPT = "rewrite_prompt.txt"
COVER_PROMPT = "cover_letter_prompt.txt"
INTERVIEW_PROMPT = "interview_prompt.txt"
ROADMAP_PROMPT = "roadmap_prompt.txt"

# -----------------------------
# Export Files
# -----------------------------

REWRITTEN_RESUME = "rewritten_resume.txt"
COVER_LETTER = "cover_letter.txt"
ROADMAP_FILE = "learning_roadmap.md"

# -----------------------------
# UI
# -----------------------------

APP_TITLE = "AI Resume Optimizer"