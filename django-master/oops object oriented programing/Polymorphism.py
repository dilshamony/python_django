#POLYMORPHISM

#method overloading
#method overriding
#operator overloading
#duck typing

#1) Method overloading
class Maths:
    def add(self):
        print("inside no arg method")
    def add(self,num1):
        print("inside 1 arg method")
    def add(self,num1,num2):
        print("inside 2 arg method")
math=Maths()
math.add(10,20)
#math.add(10)-->error
#math.add()-->error
#ie., one method(here is add) and different number of arguements
#but only work the recently added method.

#2) Method overriding
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name
p=Person("ajay",25)
print(p)

#3) Duck typing
#if it walks like a duck and quacks like a duck, then it must be a duck-to determinre
#eg 1
class Swift:
    def start(self):
        print("swift car starts")
    def accelerate(self):
        print("swift car accelerates")
    def stop(self):
        print("swift car stops")
class Maruti:
    def start(self):
        print("maruti car starts")
    def accelerate(self):
        print("maruti car accelerates")
    def stop(self):
        print("maruti car stops")
class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stop()
sw=Swift()
p=Person()
p.drive(sw)
#for another car
sw=Maruti()
p=Person()
p.drive(sw)

#eg: 2
class Pycharm:
    def start(self):
        print("started with pycharm ide")
class Vscode:
    def start(self):
        print("")
class Django:
    def execute(self,ide):
        ide.start()
py=Pycharm()
dj=Django()
dj.execute(py)
#now if the person need to execute with vccode , there is no need to change the method of person
#only change the object code
#ie.,
py=Vscode()
dj=Django()
dj.execute(py)

#4) Operator overloading