CREATE OR REPLACE FUNCTION udf_classification_items_count(classification_name VARCHAR(30))
RETURNS TEXT
AS
$$
    DECLARE
        item_count INT;
        out_massage TEXT;
    BEGIN
        item_count := (SELECT
            COUNT(*)
        FROM classifications AS c
                 JOIN items AS i
                      ON c.id = i.classification_id
        WHERE c.name = classification_name);
        IF item_count = 0 THEN out_massage := 'No items found.';
        ELSE out_massage := CONCAT('Found ', item_count, ' items.');
        END if;
        RETURN out_massage;
    END;
$$
LANGUAGE plpgsql;

SELECT udf_classification_items_count('Nonexistent') AS message_text;

SELECT udf_classification_items_count('Laptops') AS message_text;





SELECT
    COUNT(*)
FROM classifications AS c
JOIN items AS i
ON c.id = i.classification_id
WHERE c.name = 'Nonexistent'





