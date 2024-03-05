class Parent:
    def fun1(self):
        print("function1 of parent")
    
    def fun2(self):
        print("function2 of parent")
class Child(Parent):
    def fun1(self):
        print("function1 of child")

if __name__ == "__main__":
    c:Child=Child()
    p:Parent=Parent()
    p.fun1()
    c.fun1()
    c.fun2()