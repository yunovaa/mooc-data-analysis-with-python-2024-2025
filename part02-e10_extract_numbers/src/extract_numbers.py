#!/usr/bin/env python3

def extract_numbers(s):
    l = s.split()
    a = []
    for item in l:
        try: 
            item = int(item)
            a.append(item)
        except ValueError:
            try:
                item = float(item)
                a.append(item)
            except ValueError:
                pass
    return a

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
