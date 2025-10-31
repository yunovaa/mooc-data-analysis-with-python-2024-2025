#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    l = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if not line.strip().startswith('!')]
        for line in lines:
            mo = re.search(r'(\d+)\s*(\d+)\s*(\d+)\s*(.*)', line)
            l.append(f"{mo.group(1)}\t{mo.group(2)}\t{mo.group(3)}\t{mo.group(4)}")
    return l

def main():
    red_green_blue()

if __name__ == "__main__":
    main()
