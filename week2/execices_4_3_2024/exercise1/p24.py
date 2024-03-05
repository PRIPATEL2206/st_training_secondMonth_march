

class C1:
    def __init__(self) -> None:
        pass
    def c1(self):
        print("c1")
class C2:
    def __init__(self) -> None:
        pass
    def c2(self):
        print("c2")
class C3:
    def __init__(self) -> None:
        pass
    def c3(self):
        print("c3")

# multi-level inheritance.
class M1(C1):
    pass
class M2(M1):
    pass
class M3(M2):
    pass

# multiple inheritance

class M(C1,C2,C3):
    pass

   