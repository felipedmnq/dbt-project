from dataclasses import dataclass


@dataclass(frozen=True)
class Configs:
    GCP_SERVICE_ACCOUNT_PATH: str = "/Users/felipedemenechvasconcelos/repos/service_account_keys"
    GCP_SERVICE_ACCOUNT_NAME: str = "light-reality-344611-37981b155600.json"
    DATA_URL: str = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
    BQ_TABLE_PATH: str = "dbt_fvasconcelos.covid_latest"
