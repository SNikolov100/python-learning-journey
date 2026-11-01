CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT
AS
$$

    BEGIN
        RETURN (
        SELECT
            COUNT(co.id)
        FROM courses AS co
        RIGHT JOIN clients AS cl
        ON cl.id = co.client_id
        WHERE cl.phone_number = phone_num
        GROUP BY cl.id);
    END;
$$
LANGUAGE plpgsql;

SELECT fn_courses_by_client('(831) 1391236');
SELECT fn_courses_by_client('(704) 2502909');


SELECT
    COUNT(co.id)
FROM courses AS co
JOIN clients AS cl
ON cl.id = co.client_id
WHERE cl.phone_number = '(831) 1391236'
GROUP BY cl.id
