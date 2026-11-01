SELECT
    *
FROM animals
WHERE owner_id IS NULL;

UPDATE animals
SET owner_id = 4
WHERE owner_id IS NULL;