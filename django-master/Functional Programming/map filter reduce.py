#Map
#Filter
#Reduce

#MAP
lst=[1,2,3,4,5,6,7,8,9,10]
squares=list(map(lambda num:num**2,lst))
print(squares)

#covert to upper case
names=["ravi","raju","viji","rinu","harsha","sabu"]
upper=list(map(lambda name:name.upper(),names))
print(upper)

#print new list in which if num>5, print num+1 and if num<5,print num-1
numbers=[4,6,8,9,3,2]
new_numbers=list(map(lambda num:num+1 if num>5 else num-1,numbers))
print(new_numbers)


#convert student names to upper case
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

students=[st,st1,st2,st3]
new=list(map(lambda student:student.name.upper(),students))
print(new)

#give 50 bonus mark to every student
students=[st,st1,st2,st3]
bonus=list(map(lambda student:student.total+50,students))
print(bonus)