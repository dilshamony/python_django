import re
#pattern="a"--->single number of a
#pattern="a+"--->one or more number of a
#pattern="a*"--->any number of a including other numbers also
#pattern="a{2}"--->pair of a
pattern="a{2,3}"-->minimum 2 and maximum 3 number of a
matcher=re.finditer(pattern,"aaaaaabbbaabbbaaaabbbaa _Z7K@")
for match in matcher:
    print(match.start())
    print(match.group())


