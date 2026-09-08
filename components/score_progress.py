"""
Progress Bar
"""

import streamlit as st


def score(score: int):

    score = max(
        0,
        min(score, 100)
    )

    st.progress(
        score / 100
    )

    st.metric(
        "Score",
        f"{score}%"
    )