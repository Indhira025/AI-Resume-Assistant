''' from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Resume Optimizer")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2:latest")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", 10)) '''


"""
Application Settings

Author : AI Resume Optimizer
"""

from pathlib import Path

# -------------------------------------------------
# Application
# -------------------------------------------------

APP_NAME = "AI Resume Optimizer & Interview Assistant"

APP_VERSION = "2.0.0"

# -------------------------------------------------
# AI Model
# -------------------------------------------------

MODEL_NAME = "llama3.2"

OLLAMA_URL = "http://localhost:11434/api/generate"

TEMPERATURE = 0.2

MAX_TOKENS = 2048

# -------------------------------------------------
# Project Paths
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"

OUTPUT_DIR = BASE_DIR / "outputs"

LOG_DIR = BASE_DIR / "logs"

PROMPT_DIR = BASE_DIR / "prompts"

ASSET_DIR = BASE_DIR / "assets"

CACHE_DIR = OUTPUT_DIR / "cache"

# -------------------------------------------------
# Export
# -------------------------------------------------

PDF_EXPORT = True

MARKDOWN_EXPORT = True

# -------------------------------------------------
# UI
# -------------------------------------------------

PAGE_ICON = "📄"

LAYOUT = "wide"

SIDEBAR = "expanded"

# -------------------------------------------------
# Logging
# -------------------------------------------------

LOG_LEVEL = "INFO"

LOG_FILE = LOG_DIR / "resume_optimizer.log"