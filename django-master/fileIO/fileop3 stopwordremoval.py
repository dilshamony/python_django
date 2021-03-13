#stop word removal

f=open("demo3","r")
dict={}
stopwords=["the","were","than","are","is","was","at","by","on"]
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if word in stopwords:
            pass
        else:
            if word not in stopwords:
                dict[word]=1
            else:
                dict[word]+=1
print(dict)
