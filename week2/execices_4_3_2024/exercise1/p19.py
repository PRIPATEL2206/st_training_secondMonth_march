def func(a,b,c=None,d=None,e=None):
    if e!=None:
        print((a*b)+(c*d*e))
    elif d!=None:
        print(sum(a,b,c,d))
    elif c!=None:
        print(a,b,c)
    else:
        print(a*b)

arr=list(map(int,input().split()))
func(*arr)