SELECT
    CONCAT(first_name, ' ', last_name) AS frull_name,
    age,
    hire_date
FROM players
WHERE first_name LIKE 'M%'
ORDER BY age DESC,
         frull_name;
