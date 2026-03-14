SELECT
    *
FROM
    guard_logs
WHERE
    80.616667 <= lon
    AND lon <= 80.62
    AND 28.541667 <= lat
    AND lat <= 28.544167
    AND action_taken IS NULL;