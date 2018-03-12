#!/bin/python3

import math
import Matrix

def exp(matrix):
    exponential = Matrix.create_empty_matrix(matrix.size)
    for i in range(100):
        exponential += matrix**i / math.factorial(i)
    return exponential