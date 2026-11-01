CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR
AS
    $$
    DECLARE
        full_name VARCHAR;
    BEGIN
        full_name := CONCAT(INITCAP(first_name), ' ',INITCAP(last_name));
        IF (first_name IS NULL)
            AND
           last_name IS NULL
            then
            full_name := 'null';
        END IF;
        RETURN full_name;
    END;
    $$
LANGUAGE plpgsql;


SELECT fn_full_name('fred', 'sanford');

select fn_full_name('JOHN', '');

select fn_full_name(NULL, NULL);
