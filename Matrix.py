#!/bin/python3

import math
import error
import copy

def create_empty_matrix(size):
        coefs = list()
        for i in range(size**2):
                coefs.append(0)
        matrix = SquareMatrix(coefs)
        return matrix

class SquareMatrix:
        """Square matrix object"""

        def __init__(self, coefs):
                nb_coefs = len(coefs)
                self.size = int(math.sqrt(len(coefs)))
                self.lines = list()
                for i in range(self.size):
                        self.lines.append(list())
                        for j in range(self.size):
                                self.lines[i].append(float(coefs[i * self.size + j]))

        def display(self):
                for i in self.lines:
                        for j in i[:len(i) - 1]:
                                print("%.2f" % j, end='\t')
                        print("%.2f" % i[-1])

        def get_identity(self):
                identity = copy.deepcopy(self)
                for i in range(identity.size):
                        for j in range(identity.size):
                                if i == j:
                                        identity.lines[i][j] = 1
                                else:
                                        identity.lines[i][j] = 0
                return identity

        def __iadd__(self, matrix_add):
                for i in range(self.size):
                        for j in range(self.size):
                                self.lines[i][j] += matrix_add.lines[i][j]
                return self

        def __add__(self, matrix_add):
                if self.size is not matrix_add.size:
                        raise "Matrixes must of the same size"
                new_matrix = copy.deepcopy(self)
                new_matrix += matrix_add
                return new_matrix

        def __mul__(self, mul):
                result = create_empty_matrix(self.size)
                if not isinstance(mul, SquareMatrix):
                        for i in range(self.size):
                                for j in range(self.size):
                                        result.lines[i][j] = self.lines[i][j] * mul
                else:
                        for i in range(self.size):
                                for j in range(self.size):
                                        for k in range(self.size):
                                                result.lines[i][j] += self.lines[k][j] * mul.lines[i][k]
                return result

        def __rmul__(self, mul):
                return self * mul

        def __imul__(self, mul):
                self = self * mul
                return self

        def __itruediv__(self, div):
                if not isinstance(div, SquareMatrix):
                        for i in range(self.size):
                                for j in range(self.size):
                                        self.lines[i][j] /= div
                return self

        def __truediv__(self, div):
                result = copy.deepcopy(self)
                if not isinstance(div, SquareMatrix):
                        result /= div
                return result

        def __ipow__(self, pow):
                cpy = copy.deepcopy(self)
                if pow == 0:
                        return self.get_identity()
                for i in range(1, pow):
                        self *= cpy
                return self

        def __pow__(self, pow):
                new_matrix = copy.deepcopy(self)
                new_matrix **= pow
                return new_matrix
