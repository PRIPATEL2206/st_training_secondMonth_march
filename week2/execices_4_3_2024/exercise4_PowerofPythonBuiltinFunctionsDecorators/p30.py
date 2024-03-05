def addition(a,b):
    if (isinstance(a,int) and isinstance(b,int)) or (isinstance(a,float) and isinstance(b,float)):
        return a+b
    raise Exception("is instance must be same of both")

print(addition(10,1))
print(addition(10,1.1))