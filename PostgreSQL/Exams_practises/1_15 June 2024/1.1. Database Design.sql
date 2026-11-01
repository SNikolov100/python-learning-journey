CREATE TABLE accounts(
                         id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                         username VARCHAR(30) NOT NULL UNIQUE ,
                         password VARCHAR(30) NOT NULL ,
                         email VARCHAR(50) NOT NULL ,
                         gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
                         age INT NOT NULL,
                         job_title VARCHAR(40) NOT NULL,
                         ip VARCHAR(30) NOT NULL
);
CREATE TABLE addresses(
                          id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                          street VARCHAR(30) NOT NULL,
                          town VARCHAR(30) NOT NULL,
                          country VARCHAR(30) NOT NULL,
                          account_id INT REFERENCES accounts(id)
                              ON DELETE CASCADE
                              ON UPDATE CASCADE
                              NOT NULL
);

CREATE TABLE photos(
                       id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                       description text,
                       capture_date TIMESTAMP NOT NULL ,
                       views INT DEFAULT 0
                           CHECK ( views >= 0 )
                                              NOT NULL
);

CREATE TABLE comments(
                         id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                         content VARCHAR NOT NULL,
                         published_on TIMESTAMP NOT NULL,
                         photo_id INT REFERENCES photos(id)
                             ON DELETE CASCADE
                             ON UPDATE CASCADE
                             NOT NULL
);

CREATE TABLE accounts_photos(
                                account_id INT REFERENCES accounts(id)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE
                                    NOT NULL ,
                                photo_id INT REFERENCES photos(id)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE
                                    NOT NULL ,
                                PRIMARY KEY (account_id, photo_id)
);

CREATE TABLE likes(
                      id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                      photo_id INT REFERENCES photos(id)
                          ON DELETE CASCADE
                          ON UPDATE CASCADE
                          NOT NULL,
                      account_id INT REFERENCES accounts(id)
                          ON DELETE CASCADE
                          ON UPDATE CASCADE
                          NOT NULL
);





