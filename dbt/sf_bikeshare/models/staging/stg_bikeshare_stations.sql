-- Casting station id to integer values if the string value is numeric.
-- Droping station ids that are not numeric.

WITH stations_data AS (
    SELECT 
        SAFE_CAST(station_id AS INT64) AS station_id,
        name
    FROM {{ source('sf_bikeshare', 'bikeshare_station_info') }}
    WHERE station_id IS NOT NULL
)

SELECT * FROM stations_data