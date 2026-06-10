import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW = BASE_DIR / "data" / "raw"
PROCESSED = BASE_DIR / "data" / "processed"

PROCESSED.mkdir(exist_ok=True)

files = {
    "fund_master": "01_fund_master.csv",
    "nav_history": "02_nav_history.csv",
    "aum_by_fund_house": "03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv",
    "scheme_performance": "07_scheme_performance.csv",
    "investor_transactions": "08_investor_transactions.csv",
    "portfolio_holdings": "09_portfolio_holdings.csv",
    "benchmark_indices": "10_benchmark_indices.csv"
}

for dataset_name, file_name in files.items():

    print(f"\nProcessing {dataset_name}")

    df = pd.read_csv(RAW / file_name)

    before_rows = len(df)

    df = df.drop_duplicates()

    after_rows = len(df)

    print(f"Removed {before_rows-after_rows} duplicate rows")

    output_path = PROCESSED / file_name

    df.to_csv(output_path, index=False)

    print(f"Saved -> {output_path}")

print("\nETL Completed Successfully")