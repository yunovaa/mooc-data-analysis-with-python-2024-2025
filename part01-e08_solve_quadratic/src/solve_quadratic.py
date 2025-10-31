#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    sq = math.sqrt(b**2 - 4*a*c)
    root_1 = (-b+sq)/(2*a)
    root_2 = (-b-sq)/(2*a)
    return (root_1,root_2)


def main():
    print(solve_quadratic(1, -3, 2))
    print(solve_quadratic(1, 2, 1))

if __name__ == "__main__":
    main()
