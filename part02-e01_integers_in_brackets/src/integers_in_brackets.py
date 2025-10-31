#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    l = re.findall(r'\[\s*([-+]?\d+)\s*\]', s)
    return  list(map(lambda x: int(x), l))

def main():
    print(integers_in_brackets(" afd 56 [asd] [ 12 ] [a34] [ -43]tt [+12]xxx"))

if __name__ == "__main__":
    main()
