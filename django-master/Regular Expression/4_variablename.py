#check the variable is valid or not which should have the following properties
#         *start with alphabet from a to k
#         *second character should be a digit and it is divisible by 3(ie., 3, 6, 9)
#         *any numbers of character

import re
rule="[a-k][369][a-zA-Z]*"
var_name=input("enter variable name")
matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid variable")
else:
    print("valid variable")