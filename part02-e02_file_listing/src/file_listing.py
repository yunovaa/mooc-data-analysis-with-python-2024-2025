#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    l=[]
    with open(filename, 'r') as f:
        for line in f.readlines():
            mo = re.search(r'(\d+)\s+([a-zA-Z]{3,})\s+(\d+)\s+(\d+)\s*:\s*(\d+)\s+(.*)', line)   
            m = []
            for item in list(mo.groups()):
                try:
                    item = int(item)
                except:
                    pass
                finally:
                    m.append(item)
            l.append(tuple(m))
    return l
    
def main():
    file_listing()

if __name__ == "__main__":
    main()
