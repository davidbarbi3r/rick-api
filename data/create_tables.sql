CREATE TABLE IF NOT EXISTS characters (
    id INT PRIMARY KEY,
    name VARCHAR NOT NULL,
    status VARCHAR,
    species VARCHAR,
    type VARCHAR,
    gender VARCHAR
);

CREATE TABLE IF NOT EXISTS episodes (
    id INT PRIMARY KEY,
    name VARCHAR NOT NULL,
    air_date DATE,
    episode VARCHAR
);

-- combinaison des deux qui est unique
CREATE TABLE IF NOT EXISTS characters_episodes (
    id_characters INT,
    id_episodes INT,
    PRIMARY KEY (id_characters, id_episodes),
    FOREIGN KEY (id_characters) REFERENCES characters (id),
    FOREIGN KEY (id_episodes) REFERENCES episodes (id)
);

