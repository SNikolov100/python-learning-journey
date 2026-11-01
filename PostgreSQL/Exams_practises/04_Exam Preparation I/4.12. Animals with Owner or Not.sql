CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT name_owner VARCHAR(50))
AS
$$
    BEGIN
        SELECT
            o.name
        INTO name_owner
        FROM animals AS a
        JOIN owners AS o
        ON o.id = a.owner_id
        WHERE a.name = animal_name;
        IF name_owner IS NULL THEN
            name_owner := 'For adoption';
        END IF;
    END;
$$
LANGUAGE plpgsql;

CALL sp_animals_with_owners_or_not('Pumpkinseed Sunfish','');


SELECT
    o.name
FROM animals AS a
JOIN owners AS o
ON o.id = a.owner_id
WHERE a.name = 'Hippo';


    CALL sp_animals_with_owners_or_not('Pumpkinseed Sunfish');