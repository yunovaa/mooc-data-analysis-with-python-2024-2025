#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    return [row.reshape(1,row.shape[0]) for row in a]

def get_column_vectors(a):
    return [row.reshape(row.shape[0],1) for row in a.T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
