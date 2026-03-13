-- Write down missing people (failed)
CREATE TABLE
    missing_people (citizen_id TEXT, first_name TEXT, last_name TEXT);

INSERT INTO
    missing_people
VALUES
    ('202705138264', 'Gary', 'Smith'),
    ('202311179921', 'Billy', 'Miller'),
    ('201604105300', 'Tracy', 'Cooper'),
    ('203312216529', 'Peggy', 'Giggs'),
    ('204205220083', 'Joe', 'Sullivan');

-- Find their trips
WITH
    missing_people (citizen_id, first_name, last_name) AS (
        VALUES
            ('202705138264', 'Gary', 'Smith'),
            ('202311179921', 'Billy', 'Miller'),
            ('201604105300', 'Tracy', 'Cooper'),
            ('203312216529', 'Peggy', 'Giggs'),
            ('204205220083', 'Joe', 'Sullivan')
    ),
    ranked_logs AS (
        SELECT
            t.*,
            m.first_name,
            m.last_name,
            ROW_NUMBER() OVER (
                PARTITION BY
                    t.citizen_id
                ORDER BY
                    t.trip_time DESC
            ) as rn
        FROM
            taxi_logs t
            INNER JOIN missing_people m ON t.citizen_id = m.citizen_id
    )
SELECT
    *
FROM
    ranked_logs
WHERE
    rn = 1;

-- Find their identities
WITH
    missing_people (citizen_id, first_name, last_name) AS (
        VALUES
            ('202705138264', 'Gary', 'Smith'),
            ('202311179921', 'Billy', 'Miller'),
            ('201604105300', 'Tracy', 'Cooper'),
            ('203312216529', 'Peggy', 'Giggs'),
            ('204205220083', 'Joe', 'Sullivan')
    )
SELECT
    *
FROM
    citizens
WHERE
    id IN (
        SELECT
            citizen_id
        FROM
            missing_people
    );

-- Find all victims
SELECT
    taxi_logs.*,
    c.first_name,
    c.last_name,
    c.social_credit
FROM
    taxi_logs
    LEFT JOIN citizens AS c ON taxi_logs.citizen_id = c.id
WHERE
    taxi_logs.distance_offset_km > 1.0
ORDER BY
    taxi_logs.trip_time;