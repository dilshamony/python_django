class Parent{
    phone(){
        console.log("inside parent phone method");
    }
}
class Child extends Parent{
    phone(){
        console.log("inside child phone method");
    }
}
var obj=new Child()
obj.phone()