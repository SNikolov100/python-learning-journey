CREATE TABLE owners(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(50) NOT NULL ,
    phone_number VARCHAR(15) NOT NULL ,
    address VARCHAR(50)
);

CREATE TABLE animal_types(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    animal_type VARCHAR(30) NOT NULL
);

CREATE TABLE cages(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    animal_type_id INT REFERENCES animal_types(id)
                  ON UPDATE CASCADE
                  ON DELETE CASCADE
                  NOT NULL
);


CREATE TABLE animals(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(30) NOT NULL ,
    birthdate DATE NOT NULL ,
    owner_id INT REFERENCES owners(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE,
    animal_type_id INT REFERENCES animal_types(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
                    NOT NULL
);

CREATE TABLE volunteers_departments(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    department_name VARCHAR(30) NOT NULL
);

CREATE TABLE volunteers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(50) NOT NULL ,
    phone_number VARCHAR(15) NOT NULL ,
    address VARCHAR(50),
    animal_id INT REFERENCES animals(id)
                       ON UPDATE CASCADE
                       ON DELETE CASCADE ,
    department_id INT REFERENCES volunteers_departments(id)
                       ON UPDATE CASCADE
                       ON DELETE CASCADE
                       NOT NULL
);

CREATE TABLE animals_cages(
    cage_id INT REFERENCES cages(id)
                          ON UPDATE CASCADE
                          ON DELETE CASCADE
                          NOT NULL ,
    animal_id INT REFERENCES animals(id)
                          ON UPDATE CASCADE
                          ON DELETE CASCADE
                          NOT NULL
);