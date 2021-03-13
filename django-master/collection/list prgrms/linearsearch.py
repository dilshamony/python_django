arr=[10,11,12,13,14,15,16,18]
element=int(input("enter element"))
flag=0
for i in arr:
    if(i==element):
        flag=1
        break
    else:
        pass
if flag==1:
    print("found")
else:
    print("not found")