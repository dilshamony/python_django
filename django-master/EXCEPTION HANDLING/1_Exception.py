#Exception handling devices

#Try   Except   Finally



# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# res=num1/num2
# print(res)
# print("database transaction")
# print("file operation")
#-----> in this when num2=0, error occurs. we have to handle the exception



    #Exception handling
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# try:
#     res=num1/num2
#     print(res)
# except:
#     print("ecxeption occuered")
# print("database transaction")
# print("file operation")
#------> here print exception occured when exception happens.but we cant know what is the exception




num1=int(input("enter num1"))
num2=int(input("enter num2"))
try:
    res=num1/num2
    print(res)
except Exception as e:
    print(e.args)
print("database transaction")
print("file operation")
#----->here type of exception will get as output