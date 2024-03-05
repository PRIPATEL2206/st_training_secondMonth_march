import random

def getRandom2(func):
    def wrapper(*args, **kwargs):
        random_value1 = random.randint(1, 10)
        random_value2 = random.randint(1, 10)
        result = func(random_value1, random_value2, *args, **kwargs)
        return result
    return wrapper


@getRandom2
def add(x, y):
    return x + y

@getRandom2
def sub(x, y):
    return x - y

@getRandom2
def mul(x, y):
    return x * y

@getRandom2
def div(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

print("Addition Result:", add())
print("Subtraction Result:", sub())
print("Multiplication Result:", mul())
print("Division Result:", div())
