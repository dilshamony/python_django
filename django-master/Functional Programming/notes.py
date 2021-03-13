# def add(num1,num2):
#     return num1+num2
# print(add(10,20))
# to add numbers

#LAMBDA
#Reduce length of program
#function=lambda arg1,arg2,...:function

#addition
add=lambda num1,num2:num1+num2
print(add(10,20))#30

#subtraction
sub=lambda num1,num2:num1-num2
print(sub(20,10))#10

#Multiplication
mul=lambda num1,num2:num1*num2
print(mul(2,3))#6

#Division
div=lambda num1,num2:num1/num2
print(div(20,10))#2

#cube
cube=lambda num:num**3
print(cube(3))#27

#to find even numbers
even=lambda num:num%2==0
print(even(4))#Truem
print(even(3))#False

#to find odd numbers
odd=lambda num:num%2!=0
print(odd(4))
print(odd(3))