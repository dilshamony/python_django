//Polymorphism
//many forms

//1) Method overloading
class Math{
    add(){
        console.log("inside no arg method");
    }
    add(num1,num2){
        console.log("inside 2 arg method");
    }
    add(num1,num2,num3){
        console.log("inside 3 arg method");
    }
}
var obj=new Math()
obj.add(10,20)