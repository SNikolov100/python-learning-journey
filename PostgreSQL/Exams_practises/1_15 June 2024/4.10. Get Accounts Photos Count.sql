CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INT
AS
$$
    BEGIN
        Return (SELECT
                    COUNT(*)
                FROM accounts_photos AS ap
                JOIN accounts AS a
                ON ap.account_id = a.id
                WHERE a.username = account_username);
    END;

$$
LANGUAGE plpgsql;


SELECT udf_accounts_photos_count('ssantryd') AS photos_count;

CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INT
AS
$$
    DECLARE
        count_photos INT;
    BEGIN
        SELECT COUNT(*) FROM accounts_photos WHERE account_id = (SELECT id FROM accounts WHERE username = account_username)
        INTO count_photos;
        RETURN count_photos;
    END;
$$
LANGUAGE plpgsql;