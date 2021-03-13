#oop-->object oriented programming

#class and object

class Person:
    def set_values(self,age,name):
        self.age=age
        self.name=name
    def print_values(self):
        print(self.age)
        print(self.name)
#now create objects
obj=Person()
obj.set_values(23,"ajay")
obj.print_values()
#we can create as many as objects
obj1=Person()
obj1.set_values(25,"ram")
obj1.print_values()