pattern="AABBCD"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
#print(dict)#A:2  B:2 C:1 D:1
for k,v in dict.items():
    #print(k,v)--> A 2   B 2    C 1      D 1
    if v==1:
        print(k)#C  D