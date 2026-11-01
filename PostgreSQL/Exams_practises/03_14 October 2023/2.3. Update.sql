UPDATE coaches AS c
SET salary = salary * c.coach_level
WHERE c.first_name LIKE 'C%'
AND c.id IN (
    SELECT
        pc.coach_id
    FROM players_coaches AS pc
    GROUP BY pc.coach_id
    HAVING count(*) > 0
);
