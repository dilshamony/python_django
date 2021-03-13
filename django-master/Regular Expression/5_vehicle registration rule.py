#find valid or invalid for vehicle registration
#form of regostration is KL98BN5645

import re
rule="[K][L][0-9]{2}[a-zA-Z]{2}[0-9]{4}"
veh_reg=input("enter registration")
matcher=re.fullmatch(rule,veh_reg)
if matcher==None:
    print("invalid registration")
else:
    print("valid registration")