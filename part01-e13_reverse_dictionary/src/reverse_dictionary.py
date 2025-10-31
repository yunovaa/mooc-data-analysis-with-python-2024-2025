#!/usr/bin/env python3

def reverse_dictionary(d):
    r_d = {}
    for a, b in d.items():
        for i in b:
            x = r_d.get(i, list())
            x.append(a)
            r_d[i] = x
    return r_d

def main():
    pass

if __name__ == "__main__":
    main()
