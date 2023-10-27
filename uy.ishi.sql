CREATE TABLE users (
    id SERIAL NOT NULL,
    tg_id INT,
    username VARCHAR(30) NOT NULL,
    reg_date DATE DEFAULT NOW(),
    status VALUES(40)
);

CREATE TABLE payment (
    id SERIAL NOT NULL,
    user_id INT,
    summa INT,
    reg_date DATE DEFAULT NOW()
);


CREATE TABLE category (
    id SERIAL NOT NULL,
    name VARCHAR(30)
);

CREATE TABLE books (
    id SERIAL NOT NULL,
    name VARCHAR(40),
    file VARCHAR(40),
    add_date DATE DEFAULT NOW(),
    category_id INT
);