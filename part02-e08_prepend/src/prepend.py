#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, object):
        self.start = object

    def write(self, s):
        print(f"{self.start}{s}")

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
