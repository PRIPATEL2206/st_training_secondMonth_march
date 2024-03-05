l=[1,2,3,4]
d={1:"a",2:"b",3:"c"}
s={1,4,5}
t=(1,4,6)

ld={i:j for i,j in enumerate(l)}
print(f"list to dict : {ld}")
print(f"list to set : {set(ld)}")
print(f"list to tuple : {tuple(ld)}")
print()

print(f"dict to list : {list(d)}")
print(f"dict to set : {set(d)}")
print(f"dict to tuple : {tuple(d)}")
print()


print(f"set to list : {list(s)}")
print(f"set to tuple : {tuple(s)}")
print()


print(f"tuple to list : {list(t)}")
print(f"tuple to set : {set(t)}")