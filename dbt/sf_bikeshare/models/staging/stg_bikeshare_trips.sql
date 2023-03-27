WITH trips_data AS (
    SELECT
        *
    {# FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips` #}
    FROM {{ source('sf_bikeshare', 'bikeshare_trips') }}
)

SELECT * FROM trips_data