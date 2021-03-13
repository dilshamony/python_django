lst=[4,3,5]#8,9,7
new=list()
total=0
for num in lst:
    total+=num
for num in lst:
    new.append(total-num)
print(new)


