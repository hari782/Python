import mysql.connector
db = mysql.connector.connect(host = "localhost", db = "py", user = "root", password = "hari@2003")
c = db.cursor()
c.execute("delete from student where regno='st-3' ")
db.commit()