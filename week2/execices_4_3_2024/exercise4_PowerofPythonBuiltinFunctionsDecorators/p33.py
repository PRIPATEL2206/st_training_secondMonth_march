def mulDecorater(a,b):
    return lambda func:lambda x,y: func(a*x,y*b)
@mulDecorater(5,4)
def printab(a,b):print(a,b)

printab(10,10)