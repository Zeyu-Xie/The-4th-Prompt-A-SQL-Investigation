-- First lookup: Find multiple Billy Millers
SELECT
    taxi_logs.trip_id,
    taxi_logs.citizen_id,
    taxi_logs.trip_time,
    citizens.first_name AS first_name,
    citizens.last_name AS last_name,
    citizens.age AS age
FROM
    taxi_logs
    LEFT JOIN citizens ON taxi_logs.citizen_id = citizens.id
WHERE
    first_name = 'Billy'
    AND last_name = 'Miller';

-- Second lookup: find the missing Billy Miller
SELECT
    taxi_logs.trip_id,
    taxi_logs.citizen_id,
    taxi_logs.trip_time,
    citizens.first_name AS first_name,
    citizens.last_name AS last_name,
    citizens.age AS age
FROM
    taxi_logs
    LEFT JOIN citizens ON taxi_logs.citizen_id = citizens.id
WHERE
    first_name = 'Billy'
    AND last_name = 'Miller'
    AND age = 53;

-- Third lookup: find Tracy Cooper
SELECT
    taxi_logs.trip_id,
    taxi_logs.citizen_id,
    taxi_logs.trip_time,
    citizens.first_name AS first_name,
    citizens.last_name AS last_name,
    citizens.age AS age
FROM
    taxi_logs
    LEFT JOIN citizens ON taxi_logs.citizen_id = citizens.id
WHERE
    first_name = 'Tracy'
    AND last_name = 'Cooper'
    AND age = 61;