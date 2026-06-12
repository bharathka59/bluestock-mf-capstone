"""
Bluestock Mutual Fund Analytics Platform

Module:
Live NAV Fetch

Author:
Bharath Kumar KA

Description:
Provides fund exploration and filtering functionality.
"""
import requests
import pandas as pd
import logging
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

AMFI_CODES = [
    125497,
    120503,
    118834,
    120716,
    125354
]

logging.basicConfig(
    filename="nav_fetch.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

for amfi_code in AMFI_CODES:

    try:

        logging.info(
            f"Fetching {amfi_code}"
        )

        url = f"https://api.mfapi.in/mf/{amfi_code}"

        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df["amfi_code"] = amfi_code

        today = datetime.now().strftime("%Y%m%d_%H%M%S")

        output_file = (
            RAW_DIR /
            f"nav_{amfi_code}_{today}.csv"
        )

        nav_df.to_csv(
            output_file,
            index=False
        )

        logging.info(
            f"SUCCESS {amfi_code}"
        )

        print(
            f"SUCCESS: {amfi_code}"
        )

    except Exception as e:

        logging.error(
            f"{amfi_code} : {e}"
        )

        print(
            f"FAILED: {amfi_code}"
        )

        print(e)