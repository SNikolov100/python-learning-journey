CREATE TABLE gift_recipients(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(76),
    country_id INT,
    gift_sent BOOLEAN DEFAULT FALSE
);

INSERT INTO gift_recipients(name, country_id, gift_sent)
SELECT
    CONCAT(first_name, ' ', last_name),
    country_id,
    country_id in (7,8,14,17,26)
FROM customers;
