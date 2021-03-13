import re
pattern='[abc]'#----> thie square bracket implies either a or b or c
matcher=re.finditer(pattern,"abc _z7KA@")#this pattern is the question
for match in matcher:
    print(match.start())
    print(match.group())



#check lower case alphabets from a to z
import re
pattern='[a-z]'#----> thie square bracket implies alphabets from a to z that too in lower case
matcher=re.finditer(pattern,"abc _z7KA@")#this pattern is the question
for match in matcher:
    print(match.start())
    print(match.group())

#check upper case alphabets fromA to Z
import re
pattern='[A-Z]'
matcher=re.finditer(pattern,"abc _z7KA@")#this pattern is the question
for match in matcher:
    print(match.start())
    print(match.group())


#check lower and upper case alphabets
import re
pattern='[a-zA-Z]'
matcher=re.finditer(pattern,"abc _z7KA@")#this pattern is the question
for match in matcher:
    print(match.start())
    print(match.group())

#check numbers from 0 to 9
import re
pattern='[0-9]'
matcher=re.finditer(pattern,"5abc _z7KA@")#this pattern is the question
for match in matcher:
    print(match.start())#0th position , 7th position
    print(match.group())#5            ,    7

#check alphabets and numbers
import re
pattern='[a-zA-Z0-9]'
matcher=re.finditer(pattern,"abc _z7KA@")#this pattern is the question
for match in matcher:
    print(match.start())
    print(match.group())


import re
pattern='[^a-zA-Z0-9]'#--->  ^this symbpl implies except. so _ & @ will print
matcher=re.finditer(pattern,"abc _z7KA@")#this pattern is the question
for match in matcher:
    print(match.start())
    print(match.group())




#Predefined Characters

import re
#pattern="\s"#-->position of space
#pattern="\d"-->[0-9] ie., digits
#pattern="D"-->[^0-9] ie., except digits
#pattern="\w"-->[a-zA-Z0-9] ie., all words
pattern="\W"#-->[^a-zA-Z09] ie., special characters
matcher=re.finditer(pattern,"abc _z7KA@")#this pattern is the question
for match in matcher:
    print(match.start())
    print(match.group())