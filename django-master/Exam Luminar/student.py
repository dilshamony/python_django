class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
stdntlst=[]
f=open("student","r")
for lines in f:
    rollno,name,course,total=lines.rstrip("/n").split(",")
    stdntlst.append(Student(rollno,name,course,total))
for stdnt in stdntlst:
    print(stdnt.rollno)
highmark=max(list(map(lambda stdnt:stdnt.total,stdntlst)))
print(highmark)

def get_stdntlst(**kwargs):
    rollno=kwargs["rollno"]
    prop=kwargs["property"]
    if rollno in stdntlst:
        print(stdntlst[rollno]["name"])
        if prop in stdntlst[rollno]:
            print(stdntlst[rollno][prop])
        else:
            print("invalid property")
    else:
        print("student doesnot exist with given id")
get_stdntlst(rollno=102,property="course")