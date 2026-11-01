CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(product_name VARCHAR(25))
RETURNS TABLE (customer_id INT,
               customer_name VARCHAR(75),
               feedback_description VARCHAR(255),
               feedback_rate NUMERIC(4,2)
              )
AS
    $$
    BEGIN
        RETURN QUERY (
        SELECT
            c.id AS customer_id,
            C.first_name,
            f.description,
            f.rate
        FROM customers AS c
                 JOIN feedbacks AS f
                      ON f.customer_id = c.id
                 JOIN products as p
                      ON p.id = f.product_id
        WHERE p.name = product_name
        ORDER BY customer_id
        );
    END;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_feedbacks_for_product('Banitsa');

SELECT * FROM fn_feedbacks_for_product('ALCOHOL');

SELECT * FROM fn_feedbacks_for_product('Bread');