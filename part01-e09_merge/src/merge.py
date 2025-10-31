#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):  
        print(f"L: {L}, i: {i}, j: {j}")
        if L1[i] <= L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    while i < len(L1):
        print(f"L: {L}, i: {i}, j: {j}")
        L.append(L1[i])
        i += 1
    while j < len(L2):
        print(f"L: {L}, i: {i}, j: {j}")
        L.append(L2[j])
        j += 1
    return L

def main():
    L1 = [1, 2, 3]
    L2 = [2, 3, 4, 5, 5]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
