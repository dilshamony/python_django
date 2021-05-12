students={
    1000:{"id":1000,"name":"akhil","course":"django","qualification":"btech"},
    1001:{"id":1001,"name":"viji","course":"django","qualification":"btech"},
    1002:{"id":1002,"name":"ram","course":"django","qualification":"mca"}
}

def get_students(id):
    if id in students:
        print(students[id]["name"])
get_students(1002)



def get_students(**kwargs):#kwargs={id:1001,property:course}
    id=kwargs["id"]#1001
    prop=kwargs["property"]#course
    if id in students:
        print(students[id]["name"])
        if prop in students[id]:
            print(students[id][prop])
        else:
            print("invalid property")
    else:
        print("student doesnot exist with given id")
get_students(id=1001,property="course")