#single inheritance

class Parent:
    def phone(self):
        print("phone method")
class Child(Parent):
    pass
ch=Child()
ch.phone()
print(ch)

#multilevel inheritance

class Parent:
    def m1(self):
        print("inside parent")
class Child(Parent):
    def m2(self):
        print("inside child")
class Subchild(Child):
    def m3(self):
        print("inside subchild")

sb=Subchild()
sb.m3()
sb.m2()
sb.m1()

ch=Child()
#ch.m3()-->error bcause child id not inherited to sub child ie., downward inheritance is not possible
ch.m2()
ch.m1()
p=Parent()
#p.m3()-->error
#p.m2()-->error
p.m1()

#multiple inheritance
#1
class Parent:
    def m1(self):
        print("inside parent")
class Child:
    def m2(self):
        print("inside child")
class Subchild(Child,Parent):
    def m3(self):
        print("inside subchild")

sb=Subchild()
sb.m1()#sub child is inherited to child and parent
#2
class Parent:
    def m1(self):
        print("inside parent")
class Child:
    def m1(self):
        print("inside child")
class Subchild(Child,Parent):
    def m3(self):
        print("inside subchild")

sb=Subchild()
sb.m1()#m1 is in both child and parent . so the order of inheritance is concerned. subchild inherited child 1sr then only inherited parent