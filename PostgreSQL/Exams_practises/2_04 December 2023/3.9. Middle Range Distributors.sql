SELECT
    d.name AS distributor_name,
    i.name AS ingredient_name,
    p.name AS product_name,
    AVG(f.rate) AS average_rate
FROM distributors AS d
JOIN ingredients AS i
ON d.id = i.distributor_id
JOIN products_ingredients AS pi
ON i.id = pi.ingredient_id
JOIN products AS p
ON p.id = pi.product_id
JOIN feedbacks AS f
ON f.product_id = p.id
GROUP BY d.name,
         i.name,
         p.name
HAVING AVG(f.rate) BETWEEN 5 AND 8
ORDER BY distributor_name,
         ingredient_name,
         product_name
;

SELECT
    d.name AS distributor_name,
    i.name AS ingredient_name,
    p.name AS product_name,
    ff.average_rate
FROM products AS p
JOIN (
    SELECT
        f.product_id,
        AVG(f.rate) AS average_rate
    FROM feedbacks AS f
    GROUP BY f.product_id
    HAVING AVG(f.rate) BETWEEN 5 AND 8
) AS ff
    ON p.id = ff.product_id
JOIN products_ingredients AS pi
ON pi.product_id = p.id
JOIN ingredients AS i
ON i.id = pi.ingredient_id
JOIN distributors AS d
ON d.id =i.distributor_id
ORDER BY distributor_name,
         ingredient_name,
         product_name
;
