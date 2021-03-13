#print even numbers from a list

limit=int(input("enter limit"))
lowerl=int(input("enter lower limit"))
for i in range(lowerl,limit):
    if i%2==0:
        print(i)