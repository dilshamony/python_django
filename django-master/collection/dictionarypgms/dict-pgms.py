#person={"id":100,"name":"ajay","gender":"male"}
#print(person["name"])
#if "total" in student:
student={"rol":1000,"name":"ajay","course":"mca"}
print(student["name"])
#to add a new key value pair
if "total" in student:
    print("exist")
else:
    student["total"]=150
print(student)
#to increment total number pf students
student["total"]+=50
print(student["total"])
#to decrement total number of students
student["total"]-=50
print(student["total"])
