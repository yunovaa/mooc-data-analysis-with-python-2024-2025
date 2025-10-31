#!/usr/bin/env python3
import numpy as np
from functools import reduce
def mult(a, n):
    li = (a for i in range(n))
    return reduce(lambda x, y: x@y, li)

def matrix_power(a, n):
    if n == 0:
        return np.eye(np.shape(a)[0])
    b = mult(a, abs(n))
    if n > 0:
        return b
    else:
        return np.linalg.inv(b)

def main():
    a = np.array([[1, 6, 7],
        [7, 8, 1],
        [5, 9, 8]])
    print(matrix_power(a, -1))

if __name__ == "__main__":
    main()
