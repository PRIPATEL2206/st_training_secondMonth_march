class Obj:
    ob1=0
    obj2=1

ob=Obj()
# 1.
print(hasattr(ob,"ob1"))
print(hasattr(ob,"ob3"))

# 2.
print(ob.ob1)

# 3.
print(ob.obj2)
ob.obj2=2
print(ob.obj2)

# 4.
print(hasattr(ob,"ob1"))
delattr(Obj,"ob1")
print(hasattr(ob,"ob1"))
