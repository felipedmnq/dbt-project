from pathlib import Path

import pandas as pd
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials

from configs import Configs

# GCP_SERVICE_ACCOUNT_PATH = Path("/Users/felipedemenechvasconcelos/repos/service_account_keys")
# GCP_SERVICE_ACCOUNT_NAME = "light-reality-344611-37981b155600.json"
# SERVICE_ACCOUNT_FULL_PATH = GCP_SERVICE_ACCOUNT_PATH / GCP_SERVICE_ACCOUNT_NAME
# DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
# BQ_TABLE_PATH = "dbt_fvasconcelos.covid_latest"

service_account_path = Path(Configs.GCP_SERVICE_ACCOUNT_PATH)
service_account_path = service_account_path / Configs.GCP_SERVICE_ACCOUNT_NAME

credentials = service_account.Credentials.from_service_account_file(service_account_path)

def get_dataframe_from_csv(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)

def load_to_bq(df: pd.DataFrame, credentials: Credentials) -> None:
    """Load DataFrame to BigQuery dataset"""

    df.to_gbq(
        destination_table=Configs.BQ_TABLE_PATH, 
        project_id="light-reality-344611", 
        credentials=credentials,
        if_exists="replace"
    )

def main():
    try:
        df = get_dataframe_from_csv(Configs.DATA_URL)
    except Exception as e:
        print(f"\033[91m[ERROR] - Create DataFrame failed.\n[MESSAGE] - {e}\033[0m")

    try:
        load_to_bq(df, credentials)
    except Exception as e:
        print(f"\033[91m[ERROR] - Load DataFrame to BigQuery failed.\n[MESSAGE] - {e}\033[0m")

    print(f"\033[92mData[SUCCESS] - CSV: {Configs.DATA_URL.split('/')[-1]} ingested to {Configs.BQ_TABLE_PATH}\033[0m")

if __name__ == "__main__":
    main()
