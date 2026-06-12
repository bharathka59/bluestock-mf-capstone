"""
Bluestock Mutual Fund Analytics Platform

Module:
Fund Comparison

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

performance = pd.read_csv(
    BASE_DIR / "data/processed/07_scheme_performance.csv"
)

st.title("⚖️ Fund Comparison")

fund1 = st.selectbox(
    "Fund 1",
    performance["scheme_name"],
    key="f1"
)

fund2 = st.selectbox(
    "Fund 2",
    performance["scheme_name"],
    key="f2"
)

compare = performance[
    performance["scheme_name"].isin(
        [fund1, fund2]
    )
]

st.dataframe(
    compare,
    use_container_width=True
)