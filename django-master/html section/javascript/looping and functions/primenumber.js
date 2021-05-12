// print prime numbers between 5 and 25

function printPrime(low,upp){  //9,25
    // 9 to 25
    for (let i = low ; i <= upp ; i++ ){
        let flag=0
        //9
        //2 to 8
        for(let j=2;j<low;j++){
            if(i%j==0){
                flag+=1;
                break;
                //prime
            }
        }
        if(flag==0){
            console.log(i)
        }
    }
}
let prime=printPrime(9,25);
console.log(prime)