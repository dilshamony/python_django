for i in range(0,10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,2,-1):
    print(i)


limit=int(input("enter limit"))
for i in range(0,limit,2):
    print(i)

limit=int(input("enter limit"))
for i in range(0,limit):
    if i%2==0:
        print(i)