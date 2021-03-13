f=open("moviedata","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    if data[2] not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(sorted(dict,key=dict.get))