CREATE TABLE countries(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE customers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(50) NOT NULL ,
    gender CHAR(1) CHECK ( gender IN ('F','M') ),
    age INT CHECK ( age > 0 ) NOT NULL,
    phone_number CHAR(10) NOT NULL ,
    country_id INT REFERENCES countries(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
                NOT NULL
);

CREATE TABLE products(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(25) NOT NULL ,
    description VARCHAR(250),
    recipe TEXT,
    price NUMERIC(10, 2) CHECK ( price > 0 ) NOT NULL
);

CREATE TABLE feedbacks(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR(255),
    rate NUMERIC(4,2) CHECK ( rate BETWEEN 0 AND 10),
    product_id INT REFERENCES products(id)
                      ON UPDATE CASCADE
                      ON DELETE CASCADE
                      NOT NULL ,
    customer_id INT REFERENCES customers(id)
                      ON UPDATE CASCADE
                      ON DELETE CASCADE
                      NOT NULL
);

CREATE TABLE distributors(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(25) UNIQUE NOT NULL ,
    address VARCHAR(30) NOT NULL ,
    summary VARCHAR(200) NOT NULL ,
    country_id INT REFERENCES countries(id)
                         ON UPDATE CASCADE
                         ON DELETE CASCADE
                         NOT NULL
);

CREATE TABLE ingredients(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(30) NOT NULL ,
    description VARCHAR(200),
    country_id INT REFERENCES countries(id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                        NOT NULL,
    distributor_id INT REFERENCES distributors(id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                        NOT NULL
);


CREATE TABLE products_ingredients(
    product_id INT REFERENCES products(id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE,
    ingredient_id INT REFERENCES ingredients(id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
);
