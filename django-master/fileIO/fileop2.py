f=open("demo2","r")
names=set()
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        names.add(word)
for word in names:
    print(word)
