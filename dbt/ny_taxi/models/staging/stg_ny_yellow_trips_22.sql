WITH ny_yellow_trips_22 AS (
    SELECT
        *
    FROM {{ source('ny_taxi_trips_22', 'tlc_yellow_trips_2022') }}
)

SELECT * FROM ny_yellow_trips_22