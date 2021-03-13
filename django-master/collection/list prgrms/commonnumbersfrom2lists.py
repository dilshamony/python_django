lst1=[1,2,3,4,9]
lst2=[1,2,7,8,9]
lst1.sort()
lst2.sort()
i=0
j=0
cnt=0
for i in lst1:
    for j in lst2:
        cnt+=1
        if i==j:
            print(i)
        elif i>j:
            j+=1
        elif i<j:
            i+=1
print()
print(cnt)#count:to find how many times loop works

#another method
lst1=[1,2,3,4,9]
lst2=[1,2,7,8,9]
lst1.sort()
lst2.sort()
i=0
j=0
while(pos1<len(lst1))&(pss2<len(lst2)):
    if (lst1[pos1]==lst2[pos2]):
        pos1+=1
        pos2+=1
        print(lst1[pos1])
    elif (lst1[pos1]>lst2[pos2]):
        pos2+=1
    elif lst[pos1]<lst2[pos2]):
        pos1+=1
pending