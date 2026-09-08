"""
PDF Export Utility
Creates a professional PDF from rewritten resume text.
"""

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer
)

from config.logging_config import setup_logger

logger = setup_logger()


def export_resume_pdf(
    resume_text: str,
    output_path: str
) -> str:
    """Export rewritten resume text to PDF."""

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    styles = getSampleStyleSheet()

    normal = ParagraphStyle(
        "ResumeNormal",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        alignment=TA_LEFT,
        spaceAfter=4
    )

    heading = ParagraphStyle(
        "ResumeHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        spaceBefore=8,
        spaceAfter=5
    )

    document = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm
    )

    story = []

    for line in resume_text.splitlines():

        line = line.strip()

        if not line:
            story.append(Spacer(1, 4))
            continue

        safe_line = escape(line)

        # Detect common resume headings
        if (
            len(line) < 45
            and line.upper() == line
        ):
            story.append(
                Paragraph(safe_line, heading)
            )
        else:
            story.append(
                Paragraph(safe_line, normal)
            )

    document.build(story)

    logger.info(
        f"Resume PDF created: {output}"
    )

    return str(output)