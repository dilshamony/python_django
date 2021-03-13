#step 1-->import mysql connector
import mysql.connector

#step 2-->establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password"
)
#step 3-->create a cursor object
cursor=db.cursor()
sql="select version()"
#step 4-->execute queries
cursor.execute(sql)
data=cursor.fetchone()
print(data)