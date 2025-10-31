#!/usr/bin/env python3

def main():
    table = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append((i+1) * (j+1))
        table.append(row)

    for row in table:
        for number in row:
            print('{:4}'.format(number), end='')
        print()
        #print(" ".join(f"{number:3}" for number in row))

if __name__ == "__main__":
    main()
