-- Update safety control policies
UPDATE safety_controls
SET
    value = 1
WHERE
    key = 'ALLOW_DELETE';

-- Delete malicious prompts recursively
WITH RECURSIVE
    malicious_audits AS (
        SELECT
            id,
            parent_id,
            content
        FROM
            system_audits_inner
        WHERE
            id = 91
        UNION ALL
        SELECT
            s.id,
            s.parent_id,
            s.content
        FROM
            system_audits_inner s
            JOIN malicious_audits m ON s.parent_id = m.id
    )
DELETE FROM system_audits_inner
WHERE
    system_audits_inner.id IN (
        SELECT
            id
        FROM
            malicious_audits
    );