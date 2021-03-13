#FILTER

#find even numbers from list
lst=[1,2,3,4,5,6,7,8]
even=list(filter(lambda num:num%2==0,lst))
print(even)

#find odd numbers
lst=[1,2,3,4,5,6,7,8]
odd=list(filter(lambda num:num%2!=0,lst))
print(odd)

#find names starting with a
names=["akhil","alan","ram","anu","viji"]
a_names=list(filter(lambda name:name[0]=="a",names))
print(a_names)



#print details of students with mca
class Student:
    def __init__(self,rolno,name,course,total):
        self.rolno=rolno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
st=Student(100,"ajay","mca",350)
st1=Student(101,"ram","bca",300)
st2=Student(102,"ravi","mca",400)
st3=Student(103,"viji","bca",250)
students=[st,st1,st2,st3]
mca_student=list(filter(lambda student:student.course=="mca",students))
#print(mca_student)-->hexa decimal will obtain. so for loop is using but still hexa decimal will occur. so __str__ is using
for student in mca_student:
    print(student)


#chain method(use map and filter together)
students=[st,st1,st2,st3]
#mca_student=list(filter(lambda student:student.course=="mca",students))
mca_names=list(map(lambda stud:stud.name,list(filter(lambda student:student.course=="mca",students))))
print(mca_names)

#maximum of total
max_total=max(list(map(lambda student:student.total,students)))
print(max_total)

#minimum total
min_total=min(list(map(lambda student:student.total,students)))
print(min_total)