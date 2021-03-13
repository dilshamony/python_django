class Employee:
    def __init__(self,id,name,desig,exp,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.sal=sal
    def __str__(self):
        return self.name
emplst=[]
f=open("Employees","r")
for lines in f:
    id,name,desig,exp,sal=lines.rstrip("/n").split(",")
    emplst.append(Employee(id,name,desig,exp,sal))
for emp in emplst:
    print(emp)#--->give name only
    print(emp.id)
    print(emp.sal)


#print names of employee whose designation is developer
developer=list(filter(lambda emp:emp.desig=="developer",emplst))
for emp in developer:
    print(emp)


#highest salary
highsal=max(list(map(lambda emp:emp.sal,emplst)))
print(highsal)


#minimum salary
minsal=min(list(map(lambda emp:emp.sal,emplst)))
print(minsal)