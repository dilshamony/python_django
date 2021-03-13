#Regular expression pattern matchingh

import re
pattern="ab"
matcher=re.finditer(pattern,"ababbbbbabab")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)