# pip install psycopg2-binary
import psycopg2

# For postgreSQL
connect = psycopg2.connect(
    dbname="my_test_base" ,
    host="localhost" ,
    user="postgres" ,
    password="Abduqahhor2007" ,
    port=2007
)

# print(connect)


cursor = connect.cursor()
# cursor.execute("""create  table tests(a1 int, a2 int, a3 int, a4 varchar(20))""")
#
# cursor.execute("""create table tet as select * from comment_table where (id=1)""")

cursor.execute("""insert into comment_table
(comment_id, user_id, text)
values (1, 2, "qalaysan")""")