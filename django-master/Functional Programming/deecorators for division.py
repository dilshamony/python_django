def div_smart(fun):#fun=div
    def inner(num1,num2):#10,20
        if num1<num2:#10<20
            num1,num2=num2,num1#20,10
        return fun(num1,num2)#div(20,10)
    return inner
@div_smart
def div(num1,num2):
    return num1/num2
print(div(10, 20))