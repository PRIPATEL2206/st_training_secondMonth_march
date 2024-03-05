a,b= ['a','b','c','d','e'],[1,2,3,4,5]
di={}
list(map(lambda a,b:di.update({a:b}),a,b))
print(di)