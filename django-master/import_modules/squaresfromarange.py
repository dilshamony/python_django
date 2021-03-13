num=int(input("enter number"))
lowl=int(input("enter lower limit"))
uppl=int(input("enter upper limit"))
def sqr(a,b,c):
    for i in range(1,uppl+1):
        res=i**num
        for j in range(lowl,uppl+1):
            if(j==res):
                print(res)
#sqr(num,lowl,uppl)