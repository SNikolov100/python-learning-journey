CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT
AS
$$
    BEGIN
        RETURN (
            SELECT
                COUNT(*)
            FROM volunteers_departments AS vd
                     JOIN volunteers AS v
                          ON v.department_id = vd.id
            WHERE vd.department_name = searched_volunteers_department
        );
    END;
$$
LANGUAGE plpgsql;

SELECT
    COUNT(*)
FROM volunteers_departments AS vd
JOIN volunteers AS v
ON v.department_id = vd.id
WHERE vd.department_name = 'Education program assistant';

SELECT fn_get_volunteers_count_from_department('Education program assistant');