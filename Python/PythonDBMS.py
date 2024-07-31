import mysql.connector

db = mysql.connector.connect(host = "localhost", db = "py", user = "root", password = "hari@2003")
c = db.cursor()
c.execute("select * from employees")
res = c.fetchall()
for res1 in res:
    print(res1)
db.commit()
