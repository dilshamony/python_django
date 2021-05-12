var num1=3;
var num2=6;
var num3=8;
if(num1>num2 && num1>num3){
    if(num2>num3){
        largest=num2;
    }
    else{
        largest=num3;
    }
}
else if(num2>num1 && num2>num3){
    if(num1>num3){
        largest=num1;
    }
    else{
        largest=num3;
    }
}
else if(num3>num2 && num3>num1){
    if(num1>num2){
        largest=num1;
    }
    else{
        largest=num2;
    }
}
console.log('second largest is $(largest)');