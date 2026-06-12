"""
Bluestock Mutual Fund Analytics Platform

Module:
Risk Analytics

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import streamlit as st
import pandas as pd
from pathlib import Path

st.title("⚠️ Risk Analytics")

BASE_DIR = Path(__file__).resolve().parent.parent.parent

var_cvar = pd.read_csv(
    BASE_DIR / "data/processed/var_cvar_report.csv"
)

alpha_beta = pd.read_csv(
    BASE_DIR / "data/processed/alpha_beta.csv"
)

performance = pd.read_csv(
    BASE_DIR / "data/processed/performance_metrics.csv"
)

risk_df = (
    performance
    .merge(alpha_beta, on="amfi_code")
    .merge(var_cvar, on="amfi_code")
)

st.subheader("Risk Metrics Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Sharpe Ratio",
        round(
            risk_df["sharpe_ratio_calc"].mean(),
            2
        )
    )

with col2:
    st.metric(
        "Average Beta",
        round(
            risk_df["beta"].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Average VaR",
        round(
            risk_df["VaR_95"].mean(),
            2
        )
    )

st.subheader("Complete Risk Analysis")

st.dataframe(
    risk_df,
    use_container_width=True
)

st.subheader("Top Funds by Sharpe Ratio")

top_sharpe = risk_df.sort_values(
    "sharpe_ratio_calc",
    ascending=False
)

st.dataframe(
    top_sharpe.head(10),
    use_container_width=True
)

st.subheader("Highest Risk Funds (VaR)")

high_risk = risk_df.sort_values(
    "VaR_95",
    ascending=False
)

st.dataframe(
    high_risk.head(10),
    use_container_width=True
)