#prime number fron 1-num

num=int(input("enter limit"))
for i in range(1,num+1):#i=1,2
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
        else:
            pass
    if(flag==0):
        print(i,"is prime number")
    else:
        print(i,"is not prime number")