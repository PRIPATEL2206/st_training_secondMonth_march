import random

lis=[random.randint(1,100)  for  i in range(10)]

odd=filter(lambda a:a%2!=0,lis)
even=filter(lambda a:a%2==0,lis)

print(list(odd))
print(list(even))