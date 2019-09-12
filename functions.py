#!/bin/python3

import math
import Matrix

def exp(matrix):
    result = Matrix.create_empty_matrix(matrix.size)
    for i in range(100):
        result += matrix**i / math.factorial(i)
    return result

def cos(matrix):
    result = Matrix.create_empty_matrix(matrix.size)
    for i in range(50):
        result += matrix**(i * 2) / math.factorial(i * 2) * (-1)**i
    return result

def cosh(matrix):
    result = Matrix.create_empty_matrix(matrix.size)
    for i in range(50):
        result += matrix**(i * 2) / math.factorial(i * 2)
    return result

def sin(matrix):
    result = Matrix.create_empty_matrix(matrix.size)
    for i in range(50):
        result += ((-1)**i) / math.factorial(2 * i + 1) * matrix**(2 * i + 1)
    return result

def sinh(matrix):
    result = Matrix.create_empty_matrix(matrix.size)
    for i in range(50):
        result += 1 / math.factorial(2 * i + 1) * matrix**(2 * i + 1)
    return result

def square(matrix):
    return matrix**2

def cube(matrix):
    return matrix**3

def identity(matrix):
    return matrix.get_identity()

operations = {
        "EXP": exp,
        "COS": cos,
        "COSH": cosh,
        "SIN": sin,
        "SINH": sinh,
        "SQUARE": square,
        "CUBE": cube,
        "ID": identity
}