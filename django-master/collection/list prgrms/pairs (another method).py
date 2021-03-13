lst=[1,2,3,4]
num=int(input("enter number"))#6
low=0
up=len(lst)-1
for i in range(0,len(lst)):
    sums=lst[low]+lst[up]#sums=1+4=5
    if(sums==num):#5==6
        print("pairs",lst[low],lst[up])
        low+=1
    elif(sums<num):#5<6
        low+=1
    else:
        up-=1
