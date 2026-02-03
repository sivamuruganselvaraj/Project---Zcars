CREATE DATABASE zcars;
USE zcars;

CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

INSERT INTO admin (username, password_hash)
VALUES (
    'siva',
    '$pbkdf2-sha256$29000$Yc3R7f6n...'
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    car_type VARCHAR(50),
    year INT,
    km INT,
    price INT
);

CREATE TABLE enquiries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    phone VARCHAR(15),
    car_name VARCHAR(100)
);

CREATE INDEX idx_car_type ON cars(car_type);
CREATE INDEX idx_username ON users(username);

INSERT INTO cars (name, car_type, year, km, price) VALUES
('swift', 'hatchback', 2019, 14537, 425000),
('datsun', 'hatchback', 2016, 27000, 310000),
('hyundai', 'hatchback', 2022, 8000, 520000),
('chevrolet', 'hatchback', 2014, 19875, 473000),
('baleno', 'hatchback', 2020, 18430, 380000),
('maruti suzuki ciaz', 'sedan', 2019, 14537, 425000),
('skoda slavia', 'sedan', 2016, 27000, 310000),
('hyundai verna', 'sedan', 2022, 8000, 520000),
('honda city', 'sedan', 2014, 19875, 473000),
('maruti suzuki swift dzire', 'sedan', 2020, 18430, 380000),
('mahindra scorpio', 'suv', 2019, 14537, 425000),
('skoda kushaq', 'suv', 2016, 27000, 310000),
('hyundai alcazar', 'suv', 2022, 8000, 520000),
('renault duster', 'suv', 2014, 19875, 473000),
('maruti suzuki fronx', 'suv', 2020, 18430, 380000),
('toyota vellfire', 'mpv', 2019, 14537, 425000),
('mahindra marazzo', 'mpv', 2016, 27000, 310000),
('mahindra thar', 'jeep', 2019, 14537, 425000),
('jeep compass', 'jeep', 2016, 27000, 310000),
('mahindra thar roxx', 'jeep', 2022, 8000, 520000),
('tata curvv ev', 'electric', 2023, 14537, 425000),
('mahindra be 6e', 'electric', 2025, 27000, 310000),
('tesla cyber truck', 'electric', 2024, 8000, 520000),
('mahindra 9e', 'electric', 2024, 19875, 473000),
('mg hector ev', 'electric', 2023, 18430, 380000);

ALTER TABLE enquiries ADD enquiry_type ENUM('buy', 'sell') NOT NULL;
DESCRIBE enquiries;
ALTER TABLE enquiries
ADD enquiry_type ENUM('buy', 'sell') NOT NULL DEFAULT 'buy';

SELECT * FROM cars WHERE car_type = 'jeep';
SELECT * FROM cars WHERE car_type = 'jeep' AND price < 400000;

DESCRIBE admin;
DESCRIBE users;
DESCRIBE cars;
USE zcars;

SELECT * FROM cars;
SELECT * FROM users;
SELECT * FROM admin;
SELECT * FROM enquiries;
INSERT INTO cars (name, car_type, year, km, price) VALUES ('toyota', 'qulis', 2002, 14537, 725000);

SELECT username, LENGTH(password_hash), password_hash FROM admin;
SELECT car_type, COUNT(*) AS total FROM cars GROUP BY car_type;
SELECT car_type, COUNT(*) AS total FROM cars GROUP BY car_type HAVING COUNT(*) > 5

/* --changing the admin password */
ALTER TABLE admin MODIFY password_hash VARCHAR(255) NOT NULL;

DELETE FROM admin WHERE username = 'siva';
Describe admin;
SELECT username, password_hash, LENGTH(password_hash) FROM admin;

INSERT INTO admin (username, password_hash)VALUES 
(
    'siva',
    'scrypt:32768:8:1$1vf3xAiuaqqwwN2J$5238e6f337a2c8b67f219a31aacc4337e439878e3cf6eea5d3850b12e73ea5db84417ffa2e37409b3949a198c65a0eb15538f35859b5c3141d065856b1fcdc01'
);
/* --changing the admin password */
SHOW TABLES;
DESCRIBE admin;
SELECT * FROM admin;


/* --toyota qulis */

INSERT INTO cars (name, car_type, year, km, price) VALUES ('toyota', 'qulis', 2002, 14537, 725000);
DELETE FROM cars WHERE name = 'toyota' AND year = 2002;

SELECT id FROM cars WHERE name = 'toyota' AND year = 2002;
DELETE FROM cars WHERE id IN (27/*eter the car id which you want to delete*/);

/* --toyota qulis */

/* --safe mode on and offf */
SET SQL_SAFE_UPDATES = 0; /*offf */
SET SQL_SAFE_UPDATES = 1; /* onnn */
/* --safe mode on and offf */
