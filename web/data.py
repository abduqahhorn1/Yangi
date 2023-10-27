# import psycopg2
# from conf import *

# conn = psycopg2.connect(
#     dbname="lesson_3" ,
#     host="localhost" ,
#     user="postgres" ,
#     password="Abduqahhor2007" ,
#     port=2007
# )


# create_table = """
#     CREATE TABLE IF NOT EXISTS users(
#         id SERIAL PRIMARY KEY NOT NULL,
    
#         name VARCHAR(21) 
#         NOT NULL,
#         lastname VARCHAR(21) NOT NULL,
#         phone VARCHAR(13) NOT NULL
#     )
# """
# cursor = conn.cursor()

# # cursor.execute("ALTER TABLE comments RENAME TO comment")
# # cursor.execute(create_table)

# # cursor.execute("ALTER TABLE comment RENAME COLUMN text TO comment_text")

# # cursor.execute("ALTER TABLE comment ADD COLUMN time VARCHAR(12) NULL")

# # cursor.execute("ALTER TABLE comment DROP COLUMN lastnmae")

# cursor.execute("ALTER TABLE comment COLUMN user_id TYPE INT")
# cursor.execute(create_table)

# conn.commit()


import eel
import random

eel.init("web")

@eel.expose
def get_random_word():
    return str(random.randint(1, 100))

eel.start("index.html")