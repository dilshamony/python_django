students={
    1000:{"id":1000,"name":"akhil","course":"django","qualification":"btech"},
    1001:{"id":1001,"name":"viji","course":"django","qualification":"btech"},
    1002:{"id":1002,"name":"ram","course":"django","qualification":"mca"}
}
print(students[1000])    #print details of student of that number
print(students[1001]["qualification"])   #qualification of that particular student
print(students[1002]["name"])

#to check id of students
id=int(input("enter student id"))
if id in students:
    print(students[id]["name"])
else:
    print("not exist")

#add property as course and then find property of student
id=int(input("enter student id"))
property=input("enter student property")
if id in students:
    print(students[id]["name"])
    if property in students[id]:
        print(students[id][property])
    else:
        print("invalid property")
else:
    print("not exist")




)