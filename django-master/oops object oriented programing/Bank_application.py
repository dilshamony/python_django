class Bank:
    bname="SBK"
    def create_account(self,acno,pname,minbal):
        self.account_number=acno
        self.person_name=pname
        self.balance=minbal
    def deposit(self,amount):
        self.balance+=amount
        print("account credited with amount",amount,"available balance is",self.balance )
        print(Bank.bname)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
            print(Bank.bname)
        else:
            self.balance-=amount
            print("account debited with amount", amount, "available balance is", self.balance)
            print(Bank.bname)
ob1=Bank()
ob1.create_account(100,"anu",1000)
ob1.deposit(2000)

ob2=Bank()
ob2.create_account(101,"viji",2000)
ob2.withdraw(3000)

ob3=Bank()
ob3.create_account(102,"ravi",5000)
ob3.withdraw(3000)