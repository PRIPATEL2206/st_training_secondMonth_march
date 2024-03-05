from random import random


def getRandomInt():
    for _ in range(10):
        yield 1+int(random()*100)

print(list(getRandomInt()))