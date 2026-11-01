CREATE TABLE search_results (
                                id SERIAL PRIMARY KEY,
                                address_name VARCHAR(50),
                                full_name VARCHAR(100),
                                level_of_bill VARCHAR(20),
                                make VARCHAR(30),
                                condition CHAR(1),
                                category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address(address_name VARCHAR(100))
AS
$$
    BEGIN
        TRUNCATE search_results;
        INSERT INTO search_results(address_name, full_name, level_of_bill, make, condition, category_name)
        SELECT
            ad.name,
            cl.full_name,
            CASE
                WHEN cou.bill <= 20 THEN 'Low'
                WHEN cou.bill <= 30 THEN 'Medium'
                ELSE 'High'
                END,
            ca.make,
            ca.condition,
            cat.name
        FROM addresses AS ad
                 JOIN courses AS cou
                      ON cou.from_address_id = ad.id
                 JOIN clients AS cl
                      ON cl.id = cou.client_id
                 JOIN cars AS ca
                      ON ca.id = cou.car_id
                 JOIN categories AS cat
                      ON cat.id = ca.category_id
        WHERE ad.name = address_name
        ORDER BY ca.make,
                 cl.full_name;
    END;
$$
LANGUAGE plpgsql;

CALL sp_courses_by_address('66 Thompson Drive');
SELECT * FROM search_results;

CALL sp_courses_by_address('700 Monterey Avenue');
SELECT * FROM search_results;





SELECT
    ad.name,
    cl.full_name,
    CASE
        WHEN cou.bill <= 20 THEN 'Low'
        WHEN cou.bill <= 30 THEN 'Medium'
        ELSE 'High'
    END,
    ca.make,
    ca.condition,
    cat.name
FROM addresses AS ad
JOIN courses AS cou
ON cou.from_address_id = ad.id
JOIN clients AS cl
ON cl.id = cou.client_id
JOIN cars AS ca
ON ca.id = cou.car_id
JOIN categories AS cat
ON cat.id = ca.category_id
WHERE ad.name = '66 Thompson Drive'
ORDER BY ca.make,
         cl.full_name;





;

