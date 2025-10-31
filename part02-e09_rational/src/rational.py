#!/usr/bin/env python3

class Rational(object):

    def __init__(self,sur,mex):
        self.sur = sur
        self.mex = mex
    
    def __add__(self, other):
        return Rational(self.sur*other.mex + self.mex*other.sur, self.mex*other.mex)
    
    def __sub__(self, other):
        return Rational(self.sur*other.mex - self.mex*other.sur, self.mex*other.mex)
    
    def __mul__(self, other):
        return Rational(self.sur*other.sur, self.mex*other.mex)
    
    def __truediv__(self, other):
        if other.sur == 0:
            raise ValueError("Division by zero")
        return Rational(self.sur * other.mex, self.mex * other.sur)
    
    def __eq__(self, other):
        return self.sur/self.mex == other.sur/other.mex
    
    def __lt__(self, other):
        return self.sur * other.mex < other.sur * self.mex

    def __gt__(self, other):
        return self.sur * other.mex > other.sur * self.mex
    
    def __str__(self):
        return f"{self.sur}/{self.mex}"    

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

main()

# if __name__ == "__main__":
#     main()
