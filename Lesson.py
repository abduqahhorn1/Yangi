import psycopg2

# Data base shop

# Table products
    # ID
    # product_name
    # product_price
    # product_image
    # reg_date
    # quantity


conn = psycopg2.connect(
    dbname="shop",
    password="Abduqahhor2007",
    user="postgres",
    host="localhost",
    port=2007
)   
conn.autocommit = True


cursor = conn.cursor()


cursor.execute(""" CREATE TABLE IF NOT EXISTS product (
               id SERIAL PRIMARY KEY ,
               product_name VARCHAR(25) NOT NULL ,
               product_image VARCHAR(125) NOT NULL ,
               pruduct_price NUMERIC(15,2) NOT NULL ,
               reg_date DATE DEFAULT '2023-09-11' ,
               quantity SMALLINT DEFAULT 1 

)""")