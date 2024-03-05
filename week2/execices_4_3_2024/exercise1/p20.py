class Rectangle:
    def __init__(self,l,b) -> None:
        self.l=l
        self.b=b
    def area(self):
        return self.l* self.b
    def printArea(self):
        print(f"area of rac is {self.area()}")

rec=Rectangle(2,4)
rec.printArea()
