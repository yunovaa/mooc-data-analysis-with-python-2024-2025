#!/usr/bin/env python3

import numpy as np
import math
#import scipy.linalg

def vector_angles(X, Y):
    mexrec = np.sqrt(np.sum(X**2, axis = 1)*np.sum(X**2, axis = 1))
    return np.array(180*np.arccos(np.clip(np.sum(X*Y, axis = 1)/mexrec, -1., 1.))/math.pi)

def main():
    a = np.arange(10).reshape(2,5)
    b = np.arange(2,12,1).reshape(2,5)
    
    print(vector_angles(a,b))

if __name__ == "__main__":
    main()


# a = np.array([[1,2], [3,4], [4,5]])
# b = np.array([[6,7], [8,9], [10,11]])
# c = np.array([10, 20, 5])
# print(np.sum(a*b, axis=1)/c)

