-- Download "sqlean" from https://github.com/nalgeon/sqlean/releases
SELECT
    load_extension ('<path-of-crypto-script>');

-- We need to use "crypto_sha256" function here
SELECT
    content,
    lower("SHA-256") AS sha256_written,
    lower(hex (crypto_sha256 (content))) AS sha256_computed,
    is_flag_hidden
FROM
    system_audits
WHERE
    sha256_written != sha256_computed;