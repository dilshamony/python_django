//INHERITANCE
//Single Inheritance


// class Parent{
//     phone(){
//         console.log("inside parent phone");
//     }
// }

// class Child{

// }
// var obj=new Child{}
// obj.phone()

//===>here phone is not a member of child but of parent
//===>hence child should inherit parent


class Child extends Parent{

}
var obj=new Child()
obj.phone()
