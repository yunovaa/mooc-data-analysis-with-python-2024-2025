#!/usr/bin/env python3

def interleave(*lists):
    a = list(zip(*lists))
    l = len(a)
    x = list(a[0])
    for i in range(1, l):
    	x.extend(list(a[i]))
    
    return x


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
