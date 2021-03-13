lst=[3,4,6,7,8]
elist=[]
olist=[]

for num in lst:
    if num%2==0:
        elist.append(num)
    else:
        olist.append(num)
print(elist)
print(olist)