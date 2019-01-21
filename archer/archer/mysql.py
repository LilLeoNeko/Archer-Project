import mysql.connector

mydb = mysql.connector.connect(
	host="localhost"
	user="Leo"
	pwd="123456"
)

print(mydb)