import random


arr=[random.choice([1,0]) for i in range(10)]
c1=arr.count(1)
c0=arr.count(0)

if len(arr)==c1:
    print("ALL")
if len(arr)==c0:
    print("NONE")
else:
    print("ANY")