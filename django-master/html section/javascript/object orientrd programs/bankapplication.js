// // Bank
// create account(accno,name.bal)
// withdrawal(amount)
// deposit(amount)

class Bank{
    //bname="SBK"
    create_account(acno,pname,minbal){
        this.account_number=acno;
        this.person_name=pname;
        this.balance=minbal
    }
    deposit(amount){
        this.balance+=amount
        console.log("account credited with amount",amount,"available balance is",this.balance);
        //console.log(Bank.bname);
    }
    withdraw(amount){
        if (amount>this.balance){
            console.log("insufficient balance");
            //console.log(Bank.bname);
        }
        else{
            this.balance-=amount
            console.log("account debited with amount", amount, "available balance is", this.balance);
            //console.log(Bank.bname);
        }
    }
        printBank(){
            console.log(this.account_number + this.person_name + this.balance);
        }
    }
var ob1=new Bank()
ob1.create_account(100,"anu",1000)
ob1.deposit(2000)
ob1.printBank()

ob2=new Bank()
ob2.create_account(101,"viji",2000)
ob2.withdraw(3000)
ob2.printBank()

ob3=new Bank()
ob3.create_account(102,"ravi",5000)
ob3.withdraw(3000)
ob3.printBank()