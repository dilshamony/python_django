import re
valid=[]
rule="[Kk][Ll] [0-9]{2} [a-zA-Z]{2} [0-9]{4}"
#rule="[kK][Ll]\d{2}[a-zA-Z]{2}\d{4}"
f=open("vehicle","r")
for numbers in f:
    number=numbers.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        valid.append(number)
print(valid)