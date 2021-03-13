f=open("demo","r")
#for lines in f:
    #print(lines)--->#akhil    ajay  vijay    ram
lst=list()
#for lines in f:
    #lst.append(lines)
#print(lst)-->#['akhil\n',ájay\n','vijay\n','ram\n']
for lines in f:
    lst.append(lines.rstrip("\n"))#,rstrip to remove anything from right end of line, here \n
print(lst)



#remove duplicate names                                                 
f=open("demo","r")
name=set()                                                            
for lines in f:
    name.add(lines.rstrip("\n"))
print(name)