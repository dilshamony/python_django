// find sum of the array?

var arr=[12,32,1,3,2,4,57,5]
var sum=arr.reduce((n1,n2)=>n1+n2)
console.log(sum);

// difference of the array
var arr=[12,32,1,3,2,4,57,5]
var sum=arr.reduce((n1,n2)=>n1-n2)
console.log(sum);

// highest element
var arr=[12,32,1,3,2,4,57,5]
var max=arr.reduce((n1,n2)=>n1>n2?n1:n2)
console.log(max);