CREATE TABLE IF NOT EXISTS cars (
    id SERIAL PRIMARY KEY,
    car_model VARCHAR(50),
    year VARCHAR(50),
    color VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS drivers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    gender VARCHAR(50),
    ip_address VARCHAR(20),
    car_id INT NULL REFERENCES cars (id)

);

-- INSERT INTO cars (id, car_model, year, color) VALUES (1, 'Honda' , 2009, 'Blue');
-- INSERT INTO cars (id, car_model, year, color) VALUES (2, 'Kia' , 2005, 'Black');
-- INSERT INTO cars (id, car_model, year, color) VALUES (3, 'Tayota' , 2011, 'Red');
-- INSERT INTO cars (id, car_model, year, color) VALUES (4, 'Chevrole' , 2015, 'White');

-- INSERT INTO drivers (id, first_name, last_name, email, gender, ip_address, car_id) VALUES (1,'Tommie', 'Hanscomb',
-- 'tomh@imgur.com', 'male', '67.92.10.159', 4);
-- INSERT INTO drivers (id, first_name, last_name, email, gender, ip_address, car_id) VALUES (2,'Arm', 'Hans',
-- 'arm@imgur.com', 'female', '69.92.19.159', 1);
-- INSERT INTO drivers (id, first_name, last_name, email, gender, ip_address, car_id) VALUES (3,'Alisa', 'scomb',
-- 'alisa@imgur.com', 'Female', '67.94.10.153', 3);
-- INSERT INTO drivers (id, first_name, last_name, email, gender, ip_address, car_id) VALUES (4,'djhs', 'kkdkek',
-- 'djhs@imgur.com', 'male', '64.94.10.169', 1);
-- INSERT INTO drivers (id, first_name, last_name, email, gender, ip_address, car_id) VALUES (5,'Tom', 'Hajk',
-- 'tom@imgur.com', 'male', '63.42.10.159', 2);
-- INSERT INTO drivers (id, first_name, last_name, email, gender, ip_address, car_id) VALUES (6,'Tnew', 'djsd',
-- 'tnew@imgur.com', 'male', '64.82.10.159', 4);

SELECT drivers.first_name, drivers.last_name, cars.car_id as mashina  FROM cars join drivers on cars.id = drivers.car_id