class My_parent_class:
    res1=0
    res2=0
    def __init__(self,a=1,b=2) -> None:
        self.a=a
        self.b=b
    def add(self):
        self.res1=self.a+self.b
    def sub(self):
        self.res2=self.a-self.b
    def  print_result(self):
        print(f"res1 = {self.res1}\nres2 = {self.res2}")

class My_child_class(My_parent_class):
    def __init__(self, a=1, b=2,c=3) -> None:
        super().__init__(a, b)
        self.c=c
    def add(self):
        super().add()
        self.res1+=self.c   
    def sub(self):
        self.res2=self.a*self.b*self.c

if __name__=="__main__":
    c=My_child_class(10,5)
    p=My_parent_class(20,5)
    c.add()
    c.sub()
    c.print_result()
    p.add()
    p.sub()
    p.print_result()