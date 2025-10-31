#!/usr/bin/env python3

import sys
import math

def standard_dev(numbers, avarage):
    s = 0
    for number in numbers:
        s += (number - avarage)**2
    return math.sqrt(s/(len(numbers)-1))

def summary(filename):
    numbers = []
    with open(filename, 'r') as f:
        for number in f.readlines():
            try:
                number = float(number.strip())
                numbers.append(number)
            except ValueError:
                pass
    s = sum(numbers)
    a = s/len(numbers)
    s_d = standard_dev(numbers, a)
    return (s,a,s_d)

def main():
    files = sys.argv[1:]
    for file in files:
        a, b, c = summary(file)
        print(f"File: {file} Sum: {a:.6f} Average: {b:.6f} Stddev: {c:.6f}")

if __name__ == "__main__":
    main()
