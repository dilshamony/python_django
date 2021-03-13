#REDUCE

from functools import reduce
lst=[1,2,3,4,5,6,7]
sum=reduce(lambda num1,num2:num1+num2,lst)
print(sum)

max=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(max)

min=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(min)