#!/usr/bin/env python3


def triple(a):
    return 3*a
def square(a):
    return a**2
def main():
    for i in range(1, 11):
        a = square(i)
        b = triple(i)
        if a> b:
            break
        print(f"triple({i})=={b} square({i})=={a}")

if __name__ == "__main__":
    main()
