class Student:
    cname="GEC"
    def __init__(self,rol,name):
        self.rol=rol
        self.name=name
    def print_student(self):
        print(self.rol)
        print(self.name)
        print(Student.cname)
ob1=Student(10,"dilsha")
ob1.print_student()