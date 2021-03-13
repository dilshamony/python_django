text="hello,hai,hello,hai,how,how,are,hello"
words=text.split(",")
print(words)
dict={}
for word in words:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
print(dict)

#to find highest occuring word
data=sorted(dict,key=dict.get,reverse=True)
print(data)
maxword=max(dict,key=dict.get)
print(maxword)


#to find least occuring word
minword=min(dict,key=dict.get)
print(minword)