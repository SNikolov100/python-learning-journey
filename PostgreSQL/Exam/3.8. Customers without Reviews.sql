SELECT
    c.id AS customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    COUNT(*) AS total_orders,
    CASE
        WHEN loyalty_card THEN 'Loyal Customer'
        ELSE 'Regular Customer'
    END AS loyalty_status
FROM customers AS c
JOIN orders AS o
ON c.id = o.customer_id
WHERE c.id NOT IN (SELECT customer_id FROM reviews)
GROUP BY c.id,
         full_name
ORDER BY total_orders DESC,
         c.id;

