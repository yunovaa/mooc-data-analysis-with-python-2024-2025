#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.array(np.sqrt((a*a).sum(axis = 1)))

def main():
    a = np.arange(10).reshape(5, 2)
    vector_lengths(a)

if __name__ == "__main__":
    main()
