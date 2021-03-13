num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if(num1>num2) & (num1>num3):
    if(num2>num3):
        print("num2 is 2nd max")
    else:
        print("num3 is 2nd max")
elif(num2>num3) & (num2>num1):
    if(num1>num3):
        print("num1 is 2nd max")
    else:
        print("num3 is 2nd max")
elif(num3>num1) & (num3>num2):
    if(num1>num2):
        print("num1 is 2nd max")
    else:
        print("num2 is 2nd max")