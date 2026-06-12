"""
Bluestock Mutual Fund Analytics Platform

Module:
Monte Carlo Simulation

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("📈 Monte Carlo NAV Projection")

# Load data
nav_df = pd.read_csv("data/processed/02_nav_history_calendar.csv")
fund_df = pd.read_csv("data/processed/01_fund_master.csv")

# Merge scheme names
merged = nav_df.merge(
    fund_df[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

# Fund selector
fund_name = st.selectbox(
    "Select Mutual Fund",
    sorted(merged["scheme_name"].dropna().unique())
)

investment = st.number_input(
    "Investment Amount (₹)",
    value=100000,
    step=10000
)

years = st.slider(
    "Projection Period (Years)",
    1,
    10,
    5
)

# Filter fund
fund_data = merged[
    merged["scheme_name"] == fund_name
].copy()

fund_data["date"] = pd.to_datetime(fund_data["date"])
fund_data = fund_data.sort_values("date")

# Calculate daily returns
fund_data["returns"] = fund_data["nav"].pct_change()
returns = fund_data["returns"].dropna()

mu = returns.mean()
sigma = returns.std()

current_nav = fund_data["nav"].iloc[-1]

# Monte Carlo
simulations = 1000
days = years * 252

paths = np.zeros((days, simulations))

for i in range(simulations):
    prices = [current_nav]

    for d in range(days):
        next_price = prices[-1] * (
            1 + np.random.normal(mu, sigma)
        )
        prices.append(next_price)

    paths[:, i] = prices[1:]

# Percentiles
median_path = np.percentile(paths, 50, axis=1)
upper_band = np.percentile(paths, 95, axis=1)
lower_band = np.percentile(paths, 5, axis=1)

# Plot
fig = go.Figure()

for i in range(30):
    fig.add_trace(
        go.Scatter(
            y=paths[:, i],
            mode="lines",
            opacity=0.2,
            showlegend=False
        )
    )

fig.add_trace(
    go.Scatter(
        y=median_path,
        name="Expected NAV",
        line=dict(width=4)
    )
)

fig.add_trace(
    go.Scatter(
        y=upper_band,
        name="95% Upper Band"
    )
)

fig.add_trace(
    go.Scatter(
        y=lower_band,
        name="5% Lower Band"
    )
)

fig.update_layout(
    title="5-Year Monte Carlo NAV Projection",
    xaxis_title="Trading Days",
    yaxis_title="Projected NAV",
    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Results
expected_nav = median_path[-1]
best_case = upper_band[-1]
worst_case = lower_band[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Expected NAV",
        f"{expected_nav:.2f}"
    )

with col2:
    st.metric(
        "Best Case",
        f"{best_case:.2f}"
    )

with col3:
    st.metric(
        "Worst Case",
        f"{worst_case:.2f}"
    )

# Investment projection
future_value = investment * (expected_nav / current_nav)

st.success(
    f"Projected Investment Value after {years} years: ₹{future_value:,.0f}"
)