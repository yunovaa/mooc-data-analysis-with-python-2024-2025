#!/usr/bin/env python3
import re
def file_extensions(filename):
    l = []
    d = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            mo = re.findall(r'[.]([A-Za-z]*)', line.strip())
            if mo:
                d.setdefault(mo[-1], []).append(line.strip())
            else:
                l.append(line.strip())
    return (l, d)

def main():
    a, b = file_extensions('src/filenames.txt')
    print(f"{len(a)} files with no extension")
    for k, v in b.items():
        print(f"{k} {len(v)}")

if __name__ == "__main__":
    main()
