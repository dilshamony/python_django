import re
rule="[0-9]{10}"  #or "\d{10}"
var_name=input("enter phone number")
matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid phone number")
else:
    print("valid phone number")