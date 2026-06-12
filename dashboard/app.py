import streamlit as st
import sqlite3
from pathlib import Path

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Bluestock MF Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------
# DATABASE CONNECTION
# ----------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data/db/bluestock_mf.db"

fund_count = 0
nav_count = 0
transaction_count = 0

try:
    conn = sqlite3.connect(DB_PATH)

    fund_count = conn.execute(
        "SELECT COUNT(*) FROM dim_fund"
    ).fetchone()[0]

    nav_count = conn.execute(
        "SELECT COUNT(*) FROM fact_nav"
    ).fetchone()[0]

    transaction_count = conn.execute(
        "SELECT COUNT(*) FROM fact_transactions"
    ).fetchone()[0]

    conn.close()

except Exception:
    pass

# ----------------------------------
# HEADER
# ----------------------------------

st.title("📈 Bluestock Mutual Fund Analytics")

st.markdown("""
### AI Powered Mutual Fund Analytics Platform

Analyze mutual funds, compare performance, evaluate risks,
and generate intelligent recommendations using advanced analytics.
""")

st.divider()

# ----------------------------------
# KPI SECTION
# ----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📂 Funds Covered",
        value=f"{fund_count:,}"
    )

with col2:
    st.metric(
        label="📈 NAV Records",
        value=f"{nav_count:,}"
    )

with col3:
    st.metric(
        label="💳 Transactions",
        value=f"{transaction_count:,}"
    )

st.divider()

# ----------------------------------
# OVERVIEW SECTION
# ----------------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("📊 Platform Overview")

    st.markdown("""
Bluestock Mutual Fund Analytics is a comprehensive platform
designed to help investors evaluate, compare and analyze mutual funds.

The platform leverages performance analytics, risk metrics,
and recommendation algorithms to support informed investment decisions.
""")

    st.success(
        "System Status: Online ✅"
    )

with right:

    st.subheader("🚀 Capabilities")

    st.markdown("""
- Fund Discovery
- Fund Comparison
- Risk Analytics
- Recommendation Engine
- SIP Planning
- Portfolio Insights
- Performance Tracking
- Risk Measurement
""")

st.divider()

# ----------------------------------
# FEATURES
# ----------------------------------

st.subheader("📌 Available Modules")

feature1, feature2 = st.columns(2)

with feature1:

    st.info("""
### 🔍 Fund Explorer

Explore mutual funds and view:

- Fund House
- Category
- Benchmark
- Launch Date
- Scheme Information
""")

    st.info("""
### ⚖️ Fund Comparison

Compare multiple funds using:

- CAGR
- Sharpe Ratio
- Fund Scores
- Categories
- Performance Metrics
""")

    st.info("""
### 🎯 Recommendation Engine

Get intelligent recommendations based on:

- Risk Appetite
- Fund Score
- Sharpe Ratio
- Category Preference
""")

with feature2:

    st.warning("""
### ⚠️ Risk Analytics

Analyze advanced risk metrics:

- Alpha
- Beta
- VaR
- CVaR
- Sortino Ratio
- Maximum Drawdown
""")

    st.success("""
### 💰 SIP Calculator

Estimate:

- Future Value
- Total Investment
- Wealth Generated
- Long-Term Returns
""")

    st.success("""
### 📈 Performance Analytics

Track:

- CAGR
- Rolling Returns
- Fund Rankings
- Risk Adjusted Returns
""")

st.divider()

# ----------------------------------
# PROJECT SUMMARY
# ----------------------------------

st.subheader("🏆 Project Highlights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Fund Schemes",
        "40+"
    )

with col2:
    st.metric(
        "NAV Records",
        "64K+"
    )

with col3:
    st.metric(
        "Transactions",
        "32K+"
    )

with col4:
    st.metric(
        "Analytics Reports",
        "10+"
    )

st.divider()

# ----------------------------------
# FOOTER
# ----------------------------------

st.caption(
    "Bluestock Mutual Fund Analytics Platform | Built using Python, Pandas, SQLite, Plotly and Streamlit"
)