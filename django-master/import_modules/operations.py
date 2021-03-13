#importing a module from another module or .py file
import MathModule #import module_name
addres=MathModule.add(100,200) #module_name.function_name(argument)
print(addres)
subres=MathModule.sub(100,200)
print(subres)
mulres=MathModule.mul(100,200)
print(mulres)
divres=MathModule.div(100,200)
print(divres)

#method 2
from MathModule import *
addres=add(*500,50)
print(addres)
subres=sub(800,500)
print(subres)
mulres=muk(50,10)
print(mulres)
divres=div(55,5)
print(divres)

#method 3
import MathModule as mp
addres=mp.add(100,200) #mp.function_name(argument)
print(addres)
subres=mp.sub(100,200)
print(subres)
mulres=mp.mul(100,200)
print(mulres)
divres=mp.div(100,200)
print(divres)
#importing from another directory
#import directory_name.module_name