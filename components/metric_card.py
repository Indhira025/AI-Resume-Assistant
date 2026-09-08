"""
Metric Card
"""

import streamlit as st


def metric(title, value):

    st.metric(
        label=title,
        value=value
    )