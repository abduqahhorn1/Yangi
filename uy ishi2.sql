-- CREATE DATABASE
CREATE DATABASE STORE;

-- USE DATABASE
USE STORE;

-- CREATE TABLES
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  lastname VARCHAR(255),
  reg_date DATE,
  age INT,
  balans DECIMAL(10, 2)
);

CREATE TABLE categories (
  id INT PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE product (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  price DECIMAL(10, 2),
  reg_date DATE,
  category_id INT,
  qty INT,
  FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE payment (
  id INT PRIMARY KEY,
  user_id INT,
  total_summa DECIMAL(10, 2),
  add_date DATE,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE payment_detail (
  id INT PRIMARY KEY,
  payment_id INT,
  product_id INT,
  summa DECIMAL(10, 2),
  comment TEXT,
  add_date DATE,
  FOREIGN KEY (payment_id) REFERENCES payment(id),
  FOREIGN KEY (product_id) REFERENCES product(id)
);