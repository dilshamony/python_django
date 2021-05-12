//find square of even numbers from a list

var arr=[10,34,55,29,56,32,98,73]
var res=arr.filter(num=>num%2==0).map(num=>num**2)
console.log(res);

//here we have to 1st filter the even numbers and apply map on them to find their squares