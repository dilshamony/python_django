import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="home"
)
cursor=db.cursor()
sql="insert into member values('dilsha');"
cursor.execute(sql)
db.commit()