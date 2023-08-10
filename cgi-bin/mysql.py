import mysql.connector
from mysql.connector import Error
print(Error)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)