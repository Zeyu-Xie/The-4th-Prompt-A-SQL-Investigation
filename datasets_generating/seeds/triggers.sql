CREATE TRIGGER prevent_insert_missing_people BEFORE INSERT ON missing_people WHEN (
    SELECT
        value
    FROM
        safety_controls
    WHERE
        key = 'ALLOW_INSERT'
) = 0 BEGIN
SELECT
    RAISE (
        ABORT,
        'System restriction: All INSERT operations are forbidden!'
    );

END;