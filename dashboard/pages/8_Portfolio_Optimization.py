"""
Bluestock Mutual Fund Analytics Platform

Module:
Portfolio Optimization

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📊 Portfolio Optimization")

df = pd.read_csv(
    "data/processed/07_scheme_performance.csv"
)

# ---------- Fund Selection ----------

funds = st.multiselect(
    "Select 5 Funds",
    df["scheme_name"].unique(),
    max_selections=5
)

if len(funds) == 5:

    selected = df[
        df["scheme_name"].isin(funds)
    ].copy()

    returns = (
        selected["return_5yr_pct"]
        .fillna(0)
        .values / 100
    )

    volatility = (
        selected["std_dev_ann_pct"]
        .fillna(1)
        .values / 100
    )

    portfolio_returns = []
    portfolio_risk = []
    portfolio_sharpe = []
    portfolio_weights = []

    simulations = 5000

    for _ in range(simulations):

        weights = np.random.random(5)

        weights = weights / np.sum(weights)

        port_return = np.sum(
            returns * weights
        )

        port_risk = np.sqrt(
            np.sum(
                (weights * volatility) ** 2
            )
        )

        sharpe = (
            port_return / port_risk
            if port_risk > 0
            else 0
        )

        portfolio_returns.append(
            port_return
        )

        portfolio_risk.append(
            port_risk
        )

        portfolio_sharpe.append(
            sharpe
        )

        portfolio_weights.append(
            weights
        )

    portfolios = pd.DataFrame({
        "Return": portfolio_returns,
        "Risk": portfolio_risk,
        "Sharpe": portfolio_sharpe
    })

    # ---------- Efficient Frontier ----------

    fig = px.scatter(
        portfolios,
        x="Risk",
        y="Return",
        color="Sharpe",
        title="Efficient Frontier"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------- Best Portfolio ----------

    best_idx = portfolios[
        "Sharpe"
    ].idxmax()

    best_weights = portfolio_weights[
        best_idx
    ]

    st.subheader(
        "🏆 Maximum Sharpe Portfolio"
    )

    allocation = pd.DataFrame({
        "Fund":
        selected["scheme_name"].values,

        "Allocation %":
        np.round(
            best_weights * 100,
            2
        )
    })

    st.dataframe(
        allocation,
        use_container_width=True
    )

    # ---------- Metrics ----------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Expected Return",
            f"{portfolio_returns[best_idx]*100:.2f}%"
        )

    with col2:
        st.metric(
            "Portfolio Risk",
            f"{portfolio_risk[best_idx]*100:.2f}%"
        )

    with col3:
        st.metric(
            "Sharpe Ratio",
            f"{portfolio_sharpe[best_idx]:.2f}"
        )

else:

    st.info(
        "Please select exactly 5 funds."
    )