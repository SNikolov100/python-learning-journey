UPDATE products
SET price = price * 1.1
WHERE id IN (
    SELECT product_id
    FROM feedbacks
    WHERE rate > 8);


UPDATE products AS p
SET price = p.price * 1.1
FROM feedbacks AS f
WHERE f.product_id = p.id
    AND f.rate > 8;