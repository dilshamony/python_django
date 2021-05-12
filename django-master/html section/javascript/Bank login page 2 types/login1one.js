class Bank {
    static getAccountDetails() {
        var accountdetails = {
            1000: { name: "ajay", acno: 1000, password: "testone", balance: 5000 },
            1001: { name: "vijay", acno: 1001, password: "testtwo", balance: 7000 },
            1002: { name: "suni", acno: 1002, password: "testthree", balance: 3000 },
            1003: { name: "rani", acno: 1003, password: "testfour", balance: 9000 },
            1004: { name: "jaya", acno: 1004, password: "testfive", balance: 4000 }
        }
        return accountdetails;
    }

    static authenticate(acno, password) {
        let accountdetails = Bank.getAccountDetails()
        if (acno in accountdetails) {
            if (password == accountdetails[acno]["password"]) {
                // console.log("login success");
                return 1;
            }
            else {
                // console.log("incorrect password");
                return -1;
            }
        }

        else {
            // console.log("invalid account number");
            return 0;
        }
    }

    static login() {
        let acno = document.querySelector("#acno").value
        let pwd = document.querySelector("#pwd").value
        let user = Bank.authenticate(acno, pwd)

        if (user == 1) {
            alert("Login success");
            window.location.href = "login2.html"
        }
        else if (user == -1) {
            alert("Incorrect password");
        }
        else {
            alert("Invalid account number");
        }
    }
    static deposit() {
        let acno = document.querySelector("#acno").value
        let pwd = document.querySelector("#pwd").value
        let amt = Number(document.querySelector("#amt").value)
        let user = Bank.authenticate(acno, pwd, amt)
        if (user == 1) {
            let bal=Bank.getAccountDetails()
            bal[acno]["balance"]+=amt;
            alert("current balance is"+ bal[acno]["balance"]);
            alert("Deposit Success")
        }
        else{
            alert("Deposit failed")
        }
    }
    static withdraw(){
        let acno=document.querySelector("#acno").value
        let pwd = document.querySelector("#pwd").value
        let amt = Number(document.querySelector("#amt").value)
        let user = Bank.authenticate(acno, pwd, amt)
        if (user == 1) {
            let bal=Bank.getAccountDetails()
            bal[acno]["balance"]-=amt;
            alert("current balance is"+ bal[acno]["balance"]);
            alert("withdraw Success")
        }
        else{
            alert("withdraw failed")
        }
    }
}