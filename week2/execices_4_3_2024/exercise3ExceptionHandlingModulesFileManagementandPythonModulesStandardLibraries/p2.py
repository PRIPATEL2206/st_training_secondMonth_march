# 1.
try:
    print(1/0)
except Exception as e:
    print(e)
# 2.
try:
    arr=[12,34]
    print(arr[3])
except Exception as e:
    print(e)

# 3.
try:
    print(int("s23"))
except Exception as e:
    print(e)

# 4.
try:
    print(5+"ok")
except Exception as e:
    print(e)

# 5.
try:
    di={
     "ok":1
     }
    print(di["Ok"])

except Exception as e:
    print(e)