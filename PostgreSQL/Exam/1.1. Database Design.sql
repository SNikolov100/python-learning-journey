CREATE TABLE brands(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE classifications(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE customers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    address VARCHAR(150) NOT NULL,
    phone VARCHAR(30) NOT NULL UNIQUE ,
    loyalty_card BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE items(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(50) NOT NULL ,
    quantity INT NOT NULL CHECK ( quantity >= 0 ),
    price DECIMAL(12,2) NOT NULL CHECK ( price> 0.00 ),
    description TEXT,
    brand_id INT REFERENCES brands(id)
                  ON UPDATE CASCADE
                  ON DELETE CASCADE
                  NOT NULL,
    classification_id INT REFERENCES classifications(id)
                  ON UPDATE CASCADE
                  ON DELETE CASCADE
                  NOT NULL
);

CREATE TABLE orders(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    customer_id INT REFERENCES customers(id)
                   ON UPDATE CASCADE
                   ON DELETE CASCADE
                   NOT NULL
);

CREATE TABLE reviews(
    customer_id INT REFERENCES customers(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
                    NOT NULL ,
    item_id INT REFERENCES items
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
                    NOT NULL ,
    PRIMARY KEY (customer_id, item_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    rating DECIMAL(3,1) NOT NULL DEFAULT 0.0 CHECK ( rating <= 10.0 )
);

CREATE TABLE orders_items(
    order_id INT REFERENCES orders(id)
                         ON UPDATE CASCADE
                         ON DELETE CASCADE
                         NOT NULL ,
    item_id INT REFERENCES items(id)
                         ON UPDATE CASCADE
                         ON DELETE CASCADE
                         NOT NULL,
    PRIMARY KEY (order_id, item_id),
    quantity INT NOT NULL CHECK ( quantity>= 0 )

);

