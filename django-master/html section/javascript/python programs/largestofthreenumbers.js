var num1=3
var num2=6
var num3=8
if(num1>num2 && num1>num3){
    console.log("num1 is max");
}
else if(num2>num3 && num2>num1){
    console.log("num2 is max");
}
else if(num3>num2 && num3>num1){
    console.log("num3 is max");
}
else{
    console.log("numbers are same");
}



var num1=3
var num2=6
var num3=8
if(num1>num2 && num1>num3){
    largest=num1;
}
else if(num2>num3){
    largest=num2;
}
else{
    largest=num3;
}
console.log('largest is $(largest)');