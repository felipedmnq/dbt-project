WITH ny_taxi_zones AS (
    SELECT
        *
    FROM {{ source('ny_taxi_trips_22', 'taxi_zone_geom') }}
)

SELECT * FROM ny_taxi_zones