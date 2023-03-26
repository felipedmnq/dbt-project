{{
  config(
    materialized = 'view',
    )
}}

WITH stations_data AS (
    SELECT 
        *
    FROM {{ source('sf_bike', 'bikeshare_station_info') }}
)

SELECT * FROM stations_data