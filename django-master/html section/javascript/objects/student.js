//stdent={id:105,name:ram,course:mca}---->question

var Student={
    id:100,
    name:"ram",
    course:"mca"
}



// print student name only
console.log(Student["id"]);

// check for total is present
console.log("total" in Student);

//to print all values
for(let key in Student){
    console.log(Student[key]);
}