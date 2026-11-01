SELECT
    a.name AS address,
    CASE
       WHEN EXTRACT(HOUR FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
           ELSE 'Night'
    END AS day_time,
    co.bill,
    cl.full_name,
    ca.make,
    ca.model,
    cat.name
FROM addresses AS a
JOIN courses AS co
ON a.id = co.from_address_id
JOIN clients AS cl
ON cl.id = co.client_id
JOIN cars AS ca
ON ca.id = co.car_id
JOIN categories AS cat
ON cat.id = ca.category_id
ORDER BY co.id;



