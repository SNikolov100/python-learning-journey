CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(IN id INT)
AS
$$
    BEGIN
        IF (SELECT salary FROM employees where employee_id = id) IS NULL THEN
            RETURN;
        END IF;
        UPDATE employees Set salary = salary * 1.05 WHERE employee_id = id;
        COMMIT ;

    END;
$$
LANGUAGE plpgsql
;
call sp_increase_salary_by_id(17)
;
SELECT
    salary
FROM employees
WHERE employee_id = 17