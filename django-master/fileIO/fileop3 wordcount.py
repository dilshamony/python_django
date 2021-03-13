#word count

f=open("demo3","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    #[hello,hai,how,are]
    for word in words:
        #hello
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
print(dict)