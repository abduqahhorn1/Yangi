CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    order_id INT PRIMARY KEY,
    quantity INT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    type_id INT,
    price INT,
);

CREATE TABLE product_types (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(40)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    email VARCHAR(30)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT NOW(),
    customer_id INT
);