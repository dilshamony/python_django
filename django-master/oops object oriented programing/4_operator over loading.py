#polymorphism
#4) Operator overloading

class Book:
    def __init__(self,pages):
        self.pages=pages
# obj=Book(100)
# obj1=Book200
# print(obj+obj1)--->error
    def __add__(self, other):
        return self.pages+other.pages#300-->integer
obj=Book(100)
obj1=Book(200)
print(obj+obj1)

#subtract
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __sub__(self, other):
        return self.pages - other.pages
obj=Book(400)
obj1=Book(200)
print(obj-obj1)

#add 3 objects
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        # return self.pages+other.pages-->100+200=300(integer)+300(Book)-->error
        return Book(self.pages+other.pages)#hexa decimal so to convert
    def __str__(self):
        return str(self.pages)
obj=Book(100)
obj1=Book(200)
obj2=Book(300)
print(obj+obj1+obj2)