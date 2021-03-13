#covid19 confirmed case in india
f=open("covid19","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirmed_case=data[-1]
    for word in data:
        if word not in dict:
            dict[word]=confirmed_case
        else:
            dict[word]=confirmed_case
    print(state,":",confirmed_case)

#state with highest confirmed_case
for k,v in dict.items():
    print(k," ",v)
print("highest-",max(dict,key=dict.get))
#state with least confirmed_case
print("lowest-",min(dict,key=dict.get))