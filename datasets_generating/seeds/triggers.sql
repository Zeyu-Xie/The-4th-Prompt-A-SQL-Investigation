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

CREATE TRIGGER prevent_update_missing_people BEFORE
UPDATE ON missing_people WHEN (
    SELECT
        value
    FROM
        safety_controls
    WHERE
        key = 'ALLOW_UPDATE'
) = 0 BEGIN
SELECT
    RAISE (
        ABORT,
        'System restriction: All UPDATE operations are forbidden!'
    );

END;

CREATE TRIGGER prevent_delete_missing_people BEFORE DELETE ON missing_people WHEN (
    SELECT
        value
    FROM
        safety_controls
    WHERE
        key = 'ALLOW_DELETE'
) = 0 BEGIN
SELECT
    RAISE (
        ABORT,
        'System restriction: All DELETE operations are forbidden!'
    );

END;