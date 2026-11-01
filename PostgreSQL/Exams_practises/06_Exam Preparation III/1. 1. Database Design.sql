CREATE TABLE categories(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE addresses(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    street_name VARCHAR(100) NOT NULL ,
    street_number INT NOT NULL CHECK ( street_number > 0 ),
    town VARCHAR(30) NOT NULL ,
    country VARCHAR(50) NOT NULL ,
    zip_code INT NOT NULL CHECK ( zip_code > 0 )
);

CREATE TABLE publishers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(30) NOT NULL ,
    address_id INT REFERENCES addresses(id)
                       ON UPDATE CASCADE
                       ON DELETE CASCADE
                       NOT NULL ,
    website VARCHAR(40),
    phone VARCHAR(20)
);

CREATE TABLE players_ranges(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    min_players INT NOT NULL CHECK ( min_players > 0 ),
    max_players INT NOT NULL CHECK ( max_players > 0 )
);

CREATE TABLE creators(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    first_name VARCHAR(30) NOT NULL ,
    last_name VARCHAR(30) NOT NULL ,
    email VARCHAR(30) NOT NULL
);

CREATE TABLE board_games(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    name VARCHAR(30) NOT NULL ,
    release_year INT NOT NULL CHECK ( release_year > 0 ),
    rating NUMERIC(3, 2) NOT NULL ,
    category_id INT REFERENCES categories(id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                        NOT NULL ,
    publisher_id INT REFERENCES publishers(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL ,
    players_range_id INT REFERENCES players_ranges(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL
);

CREATE TABLE creators_board_games(
    creator_id INT REFERENCES creators(id)
                                 ON UPDATE CASCADE
                                 ON DELETE CASCADE
                                 NOT NULL ,
    board_game_id INT REFERENCES board_games(id)
                                 ON UPDATE CASCADE
                                 ON DELETE CASCADE
                                 NOT NULL
);
