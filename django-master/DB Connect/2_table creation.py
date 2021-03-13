import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="home"
)
cursor=db.cursor()
sql="create table member(s_name varchar(120))"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
