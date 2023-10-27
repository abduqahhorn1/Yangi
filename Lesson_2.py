# import calendar

# c = calendar.HTMLCalendar(0)
# print(c.formatyear(2023))

# with open("calendar1.html", "w") as f:
#     f.write(c.formatyear(2023))

# import psycopg2
# from datetime import timedelta

# conn = psycopg2.connect(
#     dbname='postgres',
#     user='postgres',
#     host='localhost',
#     password='Abduqahhor2007'
# )
# conn.autocommit = True
# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS books (
#                ID SERIAL PRIMARY KEY,
#                title text,
#                author text,
#                reg_date date
# )""")

# def add_book(title, author,reg_date):
#     today = date.today()
#     reg_date = str(today - timedelta(days=1))
#     cursor.execute("""INSERT INTO books (title,author, reg_date))
#                    VALUES (%s, %s, %s)""", (title,author,reg_date))

# add_book('Python','Ivan')

# from decimal import Decimal, ROUND_HALF_EVEN

# n = Decimal("0.1")
# n2 = Decimal("0.2")
# n3 = Decimal("0.3")

x = 12.34567
print(str(x).split('.')[0]+ "."+ str(x).split('.')[1][0])

