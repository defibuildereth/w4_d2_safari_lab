DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS staff;


CREATE TABLE staff(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date VARCHAR(255),
    department VARCHAR(255),
    performance_rating INT
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    species VARCHAR(255),
    age INT,
    staff_id INT REFERENCES staff(id)
);