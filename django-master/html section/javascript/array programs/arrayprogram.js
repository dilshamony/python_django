//indexing is possible

var numbers=[10,70,20,30,40,50];
console.log(numbers[1]);//20



// //itration
for (let num of numbers){
    console.log(num);
}


// //inserting a new number (push)
numbers.push(60);
for (let num of numbers){
    console.log(num);
}



// //removing last added number  is poping
numbers.pop();
for (let num of numbers){
    console.log(num);
}




//sorting the array
numbers.sort()
for (let num of numbers){
    console.log(num);
}


//sorting array in ascending order
var arr=[100,10,111,1,2,3];
arr.sort((i,j)=>i-j)
for (let num of arr){
    console.log(num)
}



// sorting array im descending order
var arr=[100,10,111,1,2,3];
arr.sort((i,j)=>j-i)
for (let num of arr){
    console.log(num)
}



//ascending
var array=[200,10,1011,1,2,3];
array.sort((i,j)=>i<j?-1:1)
for (let num of array){
    console.log(num)
}


//descending
var array=[200,10,1011,1,2,3];
array.sort((i,j)=>j<i?-1:1)
for (let num of array){
    console.log(num)
}