try:
    a=10/0
except Exception as e :
    print(e)
else:
    print(a)
finally:
    print("finaly executed")

print()
try:
    a=10/1
except Exception as e :
    print(e)
else:
    print(a)
finally:
    print("finaly executed")

