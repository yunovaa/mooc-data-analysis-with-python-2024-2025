#!/usr/bin/env python3

def sum_equation(L):
    if L:
        sm = f"{L[0]} "
        s = sum(L)
        for i in range(1, len(L)):
            sm+= f"+ {L[i]} "
        return f'{sm}= {s}'
    else:
        return '0 = 0'

def main():
    pass

if __name__ == "__main__":
    main()
