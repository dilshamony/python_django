employees=[
    [100,"akhil","developer",2,50000,1989,1995],
    [101,"anu","developer",2,45000,1970,1990],
    [102,"abin","qa",1,30000,1989,1991],
    [103,"james","ba",1,45000,1990,1999]
]
#print employees name only
for emp in employees:
    print(emp[1])

#print employees salary only
for emp in employees:
    print(emp[4])

#print details of developers only
for emp in employees:
    if emp[2]=="developer":
        print (emp)

#print sum of salaries
sum=0
for emp in employees:
    sum+=emp[4]
print(sum)

#print highest salary
salary=[]
for emp in employees:
    salary.append(emp[4])
print("maximum salary is",max(salary))

#print employees worked in 1990's
#for emp in employees:
    #if emp[5]>=1990 & emp[6]>=1999:
        #print(emp)

#print experience of each employee
for emp in employees:
    print(emp[6]-emp[5])

#print high experienced employee details
exp=[]
for emp in employees:
    exp.append(emp[6]-emp[5])
high=(max(exp))
for emp in employees:
    exp=emp[6]-emp[5]
    if (high==exp):
        print(emp)
