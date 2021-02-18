
import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="webdata",
    user="postgres",
    password="postgres",
    port=5432)
cur = con.cursor()

cur.execute("select * from raidforums")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]}  name {r[1]} by {r[2]} date {r[3]} scrape {r[4]}")

con.commit()
# closr the cursor
cur.close()
# close connection
con.close()
