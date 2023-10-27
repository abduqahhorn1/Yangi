CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    price INT,
    name VARCHAR(50),
    qty INT,
    color VARCHAR(50),
    min_qty INT,
    likes INT DEFAULT 0,
    reg_date DATE DEFAULT NOW()
);

INSERT INTO product ( price, name, qty, color, min_qty, likes)
VALUES ( 1455, 'Gugurt', 73, 'Purple', 10,5);

INSERT INTO product ( price, name, qty, color, min_qty, likes)
VALUES ( 5860 'Silver Water', 45, 'Transparent', 5,50);

INSERT INTO product ( price, name, qty, color, min_qty, likes)
VALUES ( 9850, 'Coco-cola', 35, 'Black', 10,102);

INSERT INTO product ( price, name, qty, color, min_qty, likes)
VALUES ( 1050, 'Fanta', 45, 'Yellow', 5,105);

INSERT INTO product ( price, name, qty, color, min_qty, likes)
VALUES ( 11200, 'Choco-cream', 10, 'Black', 3,20);

INSERT INTO product ( price, name, qty, color, min_qty, likes)
VALUES ( 11200, 'Pepsi', 67, 'Black', 10,200);

INSERT INTO product ( price, name, qty, color, min_qty, likes)
VALUES ( 14200, 'Shakar', 105, 'White', 10,21);

