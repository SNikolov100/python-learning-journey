SELECT
    i.name AS name,
    CONCAT(UPPER(b.name), '/', LOWER(c.name)) AS promotion,
    CONCAT('On sale: ', description) AS description,
    i.quantity AS quantity
FROM items AS i
JOIN brands AS b
ON b.id = i.brand_id
JOIN classifications AS c
ON c.id = i.classification_id
WHERE i.id NOT IN (SELECT item_id FROM orders_items)
ORDER BY quantity DESC,
         name;
