num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if(num1==num2) & (num2==num3):
    print("numbers are equal")
elif(num1>num2):
    if(num2>num3):
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)
else:
    if(num1>num3):
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)
