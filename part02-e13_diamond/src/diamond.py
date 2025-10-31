#!/usr/bin/env python3

import numpy as np

def diamond(n):
    base_eye = np.eye(n, dtype=int)
    if n == 1:
        return base_eye
    else:
        upper = np.concatenate((base_eye[::-1], base_eye[:, 1:]), axis=1)
        return np.concatenate((upper[:-1,:], upper[::-1]))

def main():
    test = diamond(3)
    print(test)

if __name__ == "__main__":
    main()



