CREATE OR REPLACE PROCEDURE udp_update_loyalty_status(min_orders INT)
AS
$$
    BEGIN
        UPDATE customers
        SET loyalty_card = TRUE
        WHERE id IN (
            SELECT
                c.id
            FROM customers AS c
            JOIN orders AS o
            ON c.id = o.customer_id
            GROUP BY c.id
            HAVING count(*) >= min_orders);
    END;
$$
LANGUAGE plpgsql;

CALL udp_update_loyalty_status(4);






SELECT
    c.id
FROM customers AS c
JOIN orders AS o
ON c.id = o.customer_id
GROUP BY c.id
HAVING count(*) >= 4

