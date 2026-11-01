SELECT
    f.product_id,
    f.rate,
    f.description,
    f.customer_id,
    c.age,
    c.gender
FROM feedbacks AS f
JOIN customers AS c
ON f.customer_id = c.id
WHERE f.rate < 5.0
            AND
    (gender = 'F' AND age > 30)
ORDER BY product_id DESC ;
