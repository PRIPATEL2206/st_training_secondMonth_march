def getNextVal():
    di=[
        range(65,91),
        range(97,123),
        range(48,58),
        ]
    for r in di:
        for i in r:
            yield chr(i),i
            
dic={}
for key,val in getNextVal():
    dic[key]=val

print(dic)