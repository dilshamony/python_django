#print the output: 123=1^3+2^3+3^3=36

num=int(input("enter number"))
sum=0
while num!=0:
    digit=num%10
    print(digit)
    sum=(digit**3)+sum
    num=num//10
print(sum)