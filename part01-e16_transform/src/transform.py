#!/usr/bin/env python3

def transform(s1, s2):
    l1 = s1.split()
    l2 = s2.split()
    return list(map(lambda i: int(i[0])*int(i[1]), list(zip(l1, l2))))
def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
