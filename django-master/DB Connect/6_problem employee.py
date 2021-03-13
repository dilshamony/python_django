import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="mydb"
)
cursor=db.cursor()
sql="create table employees(e_id int,name varchar(120),desig varchar(80),salary int)"
cursor.execute(sql)
data=cursor.fetchone()
print(data)