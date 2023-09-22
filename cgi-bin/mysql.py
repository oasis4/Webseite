import MySQLdb

db = MySQLdb.connect("localhost","root","")
cursor = db.cursor()
cursor.execute("use it_test")
#cursor.execute("INSERT into test SET name='Anton', email= 'anton@gmail.com', password= '5555', geburtsdatum= '2000-01-01'")
cursor.execute("SELECT * from test")
db.commit()
res = cursor.fetchall()
for row in res:
    print(row)
cursor.close()

