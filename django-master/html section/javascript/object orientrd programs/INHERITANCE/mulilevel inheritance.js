//Multilevel Inheritance

class Parent{
    m1(){
        console.log("inside parent phone");
    }
}
class Child extends Parent{
    m2(){
        console.log("m2");
    }

}
class SubChild extends Child{
    m3(){
        console.log("m3");
    }
}
var obj1=new SubChild()
obj1.m3()
obj1.m2()
obj1.m1()


//Multiple inheritance is not possible in javascript