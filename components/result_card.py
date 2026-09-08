"""
Result Card
"""

import streamlit as st


def show_list(title, data, icon="✅"):

    with st.expander(
        title,
        expanded=True
    ):

        if data:

            for item in data:

                st.write(
                    icon,
                    item
                )

        else:

            st.info("No Data")