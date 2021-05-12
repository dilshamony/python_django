class Person {
    constructor(id, name, age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
    printPerson() {
        console.log(this.id + this.name + this.age);
    }
}

var obj1 = new Person(100, "ram", 23);
obj1.printPerson()

