import requests
import pandas as pd

AMFI_CODE = 125497

url = f"https://api.mfapi.in/mf/{AMFI_CODE}"

response = requests.get(url)

data = response.json()

print(data["meta"]["scheme_name"])

nav_df = pd.DataFrame(data["data"])

print(nav_df.head())