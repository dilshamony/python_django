class Student:
    def __init__(self,rolno,name,course,total):
        self.rolno=rolno
        self.name=name
        self.course=course
        self.total=total
st=Student(100,"ajay","mca",350)
st1=Student(101,"ram","bca",300)
st2=Student(102,"ravi","mca",400)
st3=Student(103,"viji","bca",250)

#print names of student studying mca
students=[]
students.append(st)
students.append(st1)
students.append(st2)
students.append(st3)
for student in students:
    if student.course=="mca":
        print(student.name)

#print student with highest total
total=[]
total.append(st)
total.append(st1)
total.append(st2)
total.append(st3)
for student in students:

#pending