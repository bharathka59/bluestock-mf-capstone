"""
Bluestock Mutual Fund Analytics Platform

Module:
Recommendation Engine

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import streamlit as st
import pandas as pd
from pathlib import Path

st.title("🎯 Recommendation Engine")

BASE_DIR = Path(__file__).resolve().parent.parent.parent

recommendations = pd.read_csv(
    BASE_DIR / "data/processed/recommendation_table.csv"
)

risk_profile = st.selectbox(
    "Select Risk Profile",
    ["Low", "Moderate", "High"]
)

filtered = recommendations[
    recommendations["risk_appetite"] == risk_profile
]

filtered = filtered.sort_values(
    "fund_score",
    ascending=False
)

st.subheader("Recommended Funds")

st.dataframe(
    filtered[
        [
            "scheme_name",
            "category",
            "sharpe_ratio",
            "fund_score"
        ]
    ],
    use_container_width=True
)