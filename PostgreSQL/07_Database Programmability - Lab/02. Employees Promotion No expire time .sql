CREATE OR REPLACE PROCEDURE sp_increase_salaries(department_name VARCHAR)
AS
$$
    BEGIN
        UPDATE employees
        SET salary = salary * 1.05
        WHERE department_id = (SELECT department_id FROM departments AS d WHERE d.name = department_name);
    END
$$
LANGUAGE plpgsql;

call sp_increase_salaries('Finance');

SELECT
    first_name,
    salary
FROM employees
WHERE department_id = (select department_id from departments where name = 'Finance')
order by first_name, salary