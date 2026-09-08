from utils.analytics import get_statistics

stats = get_statistics()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Average ATS",
        stats["avg_ats"]
    )

    st.metric(
        "Best ATS",
        stats["best_ats"]
    )

with col2:
    st.metric(
        "Resume Analyzed",
        stats["resume_count"]
    )

    st.metric(
        "Cover Letters",
        stats["cover_letters"]
    )

st.metric(
    "Interview Questions",
    stats["interviews"]
)

st.metric(
    "Resume Rewrites",
    stats["rewrite_count"]
)