class Employee{
    constructor(id,name,desig,sal){
        this.id=id;
        this.name=name;
        this.desig=desig;
        this.sal=sal
    }
    printEmp(){
        console.log(this.id+this.name);
    }
}
var obj1=new Employee(100,"ram","developer",25000)
var obj2=new Employee(101,"viji","qa",35000)
var obj3=new Employee(102,"sinu","developer",23000)
var obj4=new Employee(103,"aji","developer",33000)
var obj5=new Employee(104,"manu","qa",40000)
var employees=[]
employees.push(obj1)
employees.push(obj2)
employees.push(obj3)
employees.push(obj4)
employees.push(obj5)

// console.log(employees);=====>print the given datas

//1) print employee name only?
var names=employees.map(emp=>emp.name)
console.log(names);

//2) print employee details whose designation is developer?
var dvlpr=employees.filter(emp=>emp.desig=="developer")
console.log(dvlpr);

//3) print employee details whose salary is greater than 30000?
var salary=employees.filter(emp=>emp.sal>30000)
console.log(salary);

// 4) sort the employees in their salary order?
employees.sort((emp1,emp2)=>emp1.sal-emp2.sal)
console.log(employees);
// or====-> (in descending order)
employees.sort((emp1,emp2)=>emp1.sal>emp2.sal?-1:1)
console.log(employees);

//5) employee having highest salary?
var highsal=employees.reduce((emp1,emp2)=>emp1.sal>emp2.sal?emp1:emp2)
console.log(highsal);

//6) employee having lowest salary?
var lowsal=employees.reduce((emp1,emp2)=>emp1.sal>emp2.sal?emp2:emp1)
console.log(lowsal);