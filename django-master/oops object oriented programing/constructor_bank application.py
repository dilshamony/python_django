class Bank:
    def __init__(self,acno,pname,minbal):
        self.account_number = acno
        self.person_name = pname
        self.balance = minbal
    def deposit(self,amount):
        self.balance+=amount
        print("account credited with amount",amount,"available balance is",self.balance )
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("account debited with amount", amount, "available balance is", self.balance)
ob1=Bank(100,"anu",1000)
ob1.deposit(2000)

ob2=Bank(101,"viji",2000)
ob2.withdraw(3000)

ob3=Bank(102,"ravi",5000)
ob3.withdraw(3000)