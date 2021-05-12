var accountdetails = {
    1000: { name: "ajay", acno: 1000, password: "testone", balance: 5000 },
    1001: { name: "vijay", acno: 1001, password: "testtwo", balance: 7000 },
    1002: { name: "suni", acno: 1002, password: "testthree", balance: 3000 },
    1003: { name: "rani", acno: 1003, password: "testfour", balance: 9000 },
    1004: { name: "jaya", acno: 1004, password: "testfive", balance: 4000 }
}


function authenticate(acno, password) {
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
var acno = 1002;
var pwd = "testthree";
var user = authenticate(acno, pwd)
if (user == 1) {
    console.log("Login success");
}
else if (user == -1) {
    console.log("Incorrect password");
}
else {
    console.log("Invalid account number");
}


// link this to html to see thr result.
// noe the another one is linked