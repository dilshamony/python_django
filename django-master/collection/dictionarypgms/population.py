population={"ind":100,"china":200,"nz":10,"wi":40,"aus":35}
print(population["ind"])
print(population.get("ind"))
data=sorted(population,key=population.get)#to print key in ascending order of value
print(data)
data=sorted(population,key=population.get,reverse=True)#to print key in descending order of value
print(data)