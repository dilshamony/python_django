#for every student college name is common. so cname is assigning in class
class Student:
    cname="GEC"
    def set_student(self,rol,name):
        self.rol=rol
        self.name=name
    def print_student(self):
        print(self.rol)
        print(self.name)
        print(Student.cname)
obj1=Student()
obj1.set_student(10,"dilsha")
obj1.print_student()

obj2=Student()
obj2.set_student(11,"swetha")
obj2.print_student()

#to acces details outside class
print(obj1.name)
print(obj2.rol)

#to access college name outsude class
print(Student.cname)

#instance variable
#static or class variable