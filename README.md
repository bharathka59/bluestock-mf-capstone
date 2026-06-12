Bluestock Mutual Fund Analytics Platform

Overview

Interactive analytics dashboard for mutual fund performance, risk assessment, recommendation systems, portfolio optimization and forecasting.

Features

* Fund Explorer
* Fund Comparison
* Recommendation Engine
* Risk Analytics
* SIP Calculator
* Monte Carlo Simulation
* Portfolio Optimization

Technology Stack

* Python
* Pandas
* NumPy
* SQLite
* Streamlit
* Plotly

Project Architecture

Raw Data → ETL → Processed Data → SQLite → Dashboard

Installation
pip install -r requirements.txt

Run Dashboard
streamlit run dashboard/app.py

Run ETL
python scripts/etl_pipeline.py

Project Structure
data/
dashboard/
scripts/
sql/
reports/
notebooks/

Author

Bharath Kumar KA

Guide

Yash Kale

# Dashboard Preview

## Home Page

![Home](screenshots/home.png)

## Recommendation Engine

![Recommendation](screenshots/recommendation.png)

## Risk Analytics

![Risk](screenshots/risk.png)

## Monte Carlo Simulation

![Monte Carlo](screenshots/montecarlo.png)

## Portfolio Optimization

![Portfolio](screenshots/portfolio.png)