print("\n using for loop")
for i in  range(10,0,-1):
    if i%2==0:
        continue
    print(i,end=",")

print("\n using while loop")
n=11
while n>1:
    n-=1
    if n%2==0:
        continue
    print(n,end=",")