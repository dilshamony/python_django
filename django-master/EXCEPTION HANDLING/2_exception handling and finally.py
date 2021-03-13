num1=int(input("enter num1"))
num2=int(input("enter num2"))
try:
    res=num1/num2
    print(res)
except Exception as e:
    print(e.args)
print("database transaction")
print("file operation")
#pending