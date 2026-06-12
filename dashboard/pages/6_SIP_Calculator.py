"""
Bluestock Mutual Fund Analytics Platform

Module:
SIP Calculator

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import streamlit as st

st.title("💰 SIP Calculator")

monthly_investment = st.number_input(
    "Monthly Investment (₹)",
    min_value=500,
    value=5000
)

years = st.slider(
    "Investment Duration (Years)",
    1,
    40,
    10
)

annual_return = st.slider(
    "Expected Annual Return (%)",
    1.0,
    30.0,
    12.0
)

r = annual_return / 100 / 12
n = years * 12

future_value = (
    monthly_investment
    * (((1 + r) ** n - 1) / r)
    * (1 + r)
)

st.metric(
    "Future Value",
    f"₹ {future_value:,.0f}"
)

st.metric(
    "Total Investment",
    f"₹ {monthly_investment * n:,.0f}"
)

st.metric(
    "Estimated Gain",
    f"₹ {future_value - monthly_investment * n:,.0f}"
)