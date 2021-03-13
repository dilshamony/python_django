import re
rule="[a-zA-Z0-9.]+[@][g][m][a][i][l][.][c][o][m]"#--> *implies any number of characters are allowed but it allow @gmail.com also bcz zero is considering  but its false. so use +
#rule="[a-zA-Z0-9]{1,20}[@][g][m][a][i][l][.][c][o][m]"--->{} implies minimum 1 and maximum 20 number of characters
var_name=input("enter mail id")
matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid mail id")
else:
    print("valid mail id")