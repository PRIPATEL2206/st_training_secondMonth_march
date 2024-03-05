def sqreOfNum(func):
    return lambda a:func(a*a)

def add10(func):
    return lambda a:func(a+10)


@sqreOfNum
@add10
def printnum(n):
    print(n)

printnum(10)