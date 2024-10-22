import math

# functions for manipulating tuple vectors
def muli(vector, scale):
    return tuple(x * scale for x in vector)

def addi(vector_a, vector_b):
    return tuple(sum(s) for s in zip(vector_a,vector_b))

def subi(vector_a, vector_b):
    return tuple(s[0] - s[1] for s in zip(vector_a,vector_b))

def divi(vector, scale):
    return tuple(x/scale for x in vector)

def doti(vector_a, vector_b):
    product = lambda v: v[0] * v[1] 
    return sum(tuple(product(s) for s in zip(vector_a,vector_b)))

def magi(vector):
    return math.sqrt(sum([x**2 for x in vector]))

def norm(vector):
    return divi(vector, magi(vector))

def setX(vector, x):
    return (x, vector[1])

def setY(vector, y):
    return (vector[0], y)