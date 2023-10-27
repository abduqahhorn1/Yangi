import psycopg2
class DB:
    def __init__(self, )
        con = psycopg2.connect(
            dbname="shop",
            user="postgres",
            password="Abduqahhor2007",
            host="localhost",
            port=2007
)
        con.autocommit = True
        cursor = con.cursor()
        self.cursor = cursor

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS users(
                id SERIAL
        

    )"""
           
        