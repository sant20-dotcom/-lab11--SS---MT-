#https://github.com/sant20-dotcom/-lab11--SS---MT-

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def logarithm(a, b):
    if a <= 0:
        raise ValueError
    if b <= 0 or b == 1:
        raise ValueError
    return math.log(a, b)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)
