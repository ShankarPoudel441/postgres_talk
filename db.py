import psycopg2
import pandas
import os
from sqlalchemy import create_engine


# connect to db
con = psycopg2.connect(
    host="localhost",
    database="stockdata",
    user="postgres",
    password="postgres",
    port=5432)

cur = con.cursor()

cur.execute("select * from thing1")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]}  name {r[1]}")

# cur.execute("insert into thing1 (id, name) values (%s,%s)", (3, 'Shankar11'))

con.commit()


# closr the cursor
cur.close()
# close connection
con.close()


# create table raidforums(id int primary key not null,
#                         post_name varchar not null,
#                         post_by varchar not null,
#                         post_date varchar not null,
#                         scrap_date timestamp not null)

# post_by

# insert into raidforums(id, post_name, post_by, post_date, scrap_date)
# values(1, 'sdfsdfdsf', 'sdfsdf', 'February 18, 2021 at 07:33 AM',
#        '2021-02-18 21:21:04.172106')
