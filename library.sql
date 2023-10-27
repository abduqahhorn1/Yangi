CREATE TABLE student (
    id SERIAL NOT NULL,
    name VARCHAR(60) NOT NULL,
    univer VARCHAR(30),
    course INT,
    address VARCHAR(70) NOT NULL,
    p_number VARCHAR(30) NOT NULL,
    is_active BOOLEAN
);
