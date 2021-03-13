import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="mydb"
)
cursor=db.cursor()
f=open("employee","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into employees values(%s,%s,%s,%s);"
    cursor.execute(sql,data)
    db.commit()