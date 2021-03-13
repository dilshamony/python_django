#num=2,2+22=24

num=int(input("enter number"))
sum=0
tot=0
# for i in range(1,num+1):
#     data=str(num)*i
#     sum=sum+int(data)
# print(sum)
for j in range(1,num+1):
    sum=sum*10+num
    print(sum)
    tot=tot+sum
print(tot)