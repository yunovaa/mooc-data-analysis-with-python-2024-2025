#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m = np.shape(a)[1]
    # print(m)
    sum_first = np.sum(a[:, :int(m/2)], axis=1)
    sum_sec = np.sum(a[:,int(m/2):], axis=1)
    # print(sum_first)
    # print(sum_sec)
    return a[sum_first>sum_sec]

def main():
    a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
    first_half_second_half(a)

if __name__ == "__main__":
    main()
