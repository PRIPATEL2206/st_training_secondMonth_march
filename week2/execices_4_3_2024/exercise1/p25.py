class Printer:
    def __init__(self,*arr) -> None:
        self.arr=arr
    def print(self,a=None):
        if a:
            print(f"with {a}")
        print(*self.arr)

pr=Printer(11.33,5,6)
pr.print(2)
