"""
Custom CSS
"""

import streamlit as st


def load_css():

    st.markdown(
        """
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="metric-container"]{

    border-radius:15px;

    padding:15px;

    background:#f8f9fa;

    border:1px solid #ddd;
}

.stButton>button{

    width:100%;

    border-radius:10px;

    height:45px;

    font-weight:bold;
}

</style>
""",
        unsafe_allow_html=True
    )