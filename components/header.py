"""
Reusable Page Header
"""

import streamlit as st


def render_header(title: str, subtitle: str = ""):

    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.divider()