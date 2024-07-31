import mysql.connector
db = mysql.connector.connect(host = "localhost", db = "py", user = "root", password = "hari@2003")
c = db.cursor()
#c.execute("create table student (name varchar(100), regno varchar(50), dept varchar(100))")
c.execute("insert into student values ('ghi','st-3','cse')")
db.commit()