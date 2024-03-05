def add(a,b,c=0):
    return a+b+c
def subtact(a,b,c=0):
    return a-b-c
def multy(a,b,c=1):
    return a*b*c
def division(a,b):
    return a/b
def florDivision(a,b):
    return a//b
def exponent(a,b):
    return a**b

def calculate(opr:str,opre:list) -> None:
    has2=len(opre)>2
    ans=0
    match opr:
        case "1":
            ans=add(opre[0],opre[1],opre[2] if has2 else 0)
        case "2":
            ans=subtact(opre[0],opre[1],opre[2] if has2 else 0)
        case "3":
            ans=multy(opre[0],opre[1],opre[2] if has2 else 1)
        case "4":
            ans=division(opre[0],opre[1])
        case "5":
            ans=exponent(opre[0],opre[1])
        case "6":
            ans=florDivision(opre[0],opre[1])
        case _:
            print("enter valid input")
            return
    print(ans)



if __name__ == "__main__":
    opr=input("1=Addition\n 2=Subtraction\n 3=Multiplication\n 4=Division\n 5=Exponent\n6=Floor Division : \n")
    oprends=list(map(int,input("enter values : ").split()))
    calculate(opr,oprends)
