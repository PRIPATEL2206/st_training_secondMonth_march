def isPrime(n:int):
    i=2
    isp=True
    while n//2>i:
        if n%i==0:
            return False
        i+=1
    return True

def getPrime(a,b):
    for i in range(a,b+1):
        if isPrime(i):
            yield i 

print(list(getPrime(1,100)))       
