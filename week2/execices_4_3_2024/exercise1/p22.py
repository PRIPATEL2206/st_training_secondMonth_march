class Parent:
    def __init__(self) -> None:
        self.obj="Parent"
    def fun1(self):
        print(f"function1 of {self.obj}")
    def fun2(self):
        print(f"function2 of {self.obj}")
    def __del__(self):
        self.obj=None
        print("desructoring")

class Child(Parent):
    def __init__(self) -> None:
        self.obj="Child"
    def fun1(self):
        print(f"function1 of {self.obj}")
    

if __name__ == "__main__":
    c:Child=Child()
    p:Parent=Parent()
    p.fun1()
    c.fun1()
    c.fun2()