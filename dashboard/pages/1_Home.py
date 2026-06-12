"""
Bluestock Mutual Fund Analytics Platform

Module:
Home Page

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import streamlit as st

st.title("🏠 Dashboard Overview")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Funds",
        "40"
    )

with col2:
    st.metric(
        "NAV Records",
        "64,320"
    )

with col3:
    st.metric(
        "Transactions",
        "32,778"
    )

st.success(
    "Bluestock Mutual Fund Analytics Platform"
)