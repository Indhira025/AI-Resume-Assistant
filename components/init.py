from .header import render_header
from .footer import render_footer
from .sidebar import render_sidebar
from .metric_card import metric
from .score_progress import score
from .upload_box import pdf_upload
from .result_card import show_list
from .loading import spinner
from .styles import load_css

from components import *

load_css()

render_sidebar()

render_header(
    "ATS Resume Analyzer",
    "Analyze your resume using AI"
)

resume = pdf_upload("ats")

if resume:

    with spinner("Analyzing..."):

        result = ATSService.analyze(path)

    score(result["ats_score"])

    show_list(
        "Strengths",
        result["strengths"]
    )

    show_list(
        "Weaknesses",
        result["weaknesses"],
        "❌"
    )

render_footer()