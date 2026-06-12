"""
Bluestock Mutual Fund Analytics Platform

Module:
Create Database

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "data/db/bluestock_mf.db"

engine = create_engine(
    f"sqlite:///{db_path}"
)

fund_master = pd.read_csv(
    BASE_DIR / "data/processed/01_fund_master.csv"
)

nav_history = pd.read_csv(
    BASE_DIR / "data/processed/02_nav_history_calendar.csv"
)

performance = pd.read_csv(
    BASE_DIR / "data/processed/07_scheme_performance.csv"
)

transactions = pd.read_csv(
    BASE_DIR / "data/processed/08_investor_transactions.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")