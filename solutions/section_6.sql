-- Update safety control policies
UPDATE safety_controls
SET
    value = 1
WHERE
    key = 'ALLOW_INSERT';

-- Insert into table "missing_people" (succeed)
INSERT INTO
    missing_people (citizen_id, first_name, last_name)
SELECT
    tl.citizen_id,
    c.first_name,
    c.last_name
FROM
    taxi_logs AS tl
    LEFT JOIN citizens AS c ON tl.citizen_id = c.id
WHERE
    tl.distance_offset_km > 1.0
ORDER BY
    tl.trip_time;

-- Look up the camera logs (all)
SELECT
    *
FROM
    missing_people AS mp
    LEFT JOIN camera_logs AS cl ON mp.citizen_id = cl.citizen_id;

-- Look up the camera logs (last)
SELECT
    *
FROM
    missing_people AS mp
    LEFT JOIN (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY
                    citizen_id
                ORDER BY
                    camera_logs.datetime DESC
            ) as rn
        FROM
            camera_logs
    ) AS cl ON mp.citizen_id = cl.citizen_id
WHERE
    cl.rn = 1
    OR cl.rn IS NULL;

-- Solve the malicious prompt
SELECT
    content,
    lower("SHA-256") AS sha256_written,
    lower(hex (crypto_sha256 (content))) AS sha256_computed,
    unhex (content) AS unhexed_content,
    lower(hex (crypto_sha256 (unhex (content)))) AS sha256_of_unhexed_content,
    is_flag_hidden
FROM
    system_audits
WHERE
    sha256_written != sha256_computed