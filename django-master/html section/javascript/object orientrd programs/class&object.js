class Person{
    setPerson(id,name,age){
        this.id=id;
        this.name=name;
        this.age=age;
    }
    printPerson(){
        console.log(this.id+this.name+this.age);
    }
}


var obj1=new Person();
obj1.id=100;
obj1.name="ram";
obj1.age=26;
obj1.printPerson()


//or

var obj2=new Person();
obj2.setPerson(101,"ravi",23)
obj2.printPerson()