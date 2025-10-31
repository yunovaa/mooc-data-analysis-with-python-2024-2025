#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, 'r') as f:
        lines = [line for line in f.readlines()]
        words = [word for line in lines for word in line.split()]
        chars = sum([len(line) for line in lines])
    return (len(lines), len(words), chars)

def main():
    #file_count('src/test.txt')
    
    files = sys.argv[1:]
    for file in files:
        a, b, c = file_count(file)
        print(f"{a}\t{b}\t{c}\t{file}")
    

if __name__ == "__main__":
    main()
