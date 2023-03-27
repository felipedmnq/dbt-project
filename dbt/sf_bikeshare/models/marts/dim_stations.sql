-- trips by station by day

SELECT
    station_id,
    stations.name,
    DATE(trips.start_date) AS date,
    COUNT(trips.trip_id) AS n_trips,
FROM {{ ref('stg_bikeshare_stations') }} AS stations
JOIN {{ ref('stg_bikeshare_trips') }} AS trips
ON stations.station_id = trips.start_station_id
GROUP BY 1, 2, 3