"""
Bluestock Mutual Fund Analytics Platform

Module:
Fund Explorer

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import streamlit as st
import pandas as pd

funds = pd.read_csv(
    "data/processed/01_fund_master.csv"
)

st.title("🔍 Fund Explorer")

selected_fund = st.selectbox(
    "Select Mutual Fund",
    funds["scheme_name"].sort_values()
)

result = funds[
    funds["scheme_name"] == selected_fund
]

st.subheader("Fund Details")

st.dataframe(
    result,
    use_container_width=True
)