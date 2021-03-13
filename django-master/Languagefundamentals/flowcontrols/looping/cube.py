num=int(input("enter number"))
cube=0
while(num!=0):
    rev=num%10
    num=num//10
    cube+=(rev*rev*rev)
print(cube)

