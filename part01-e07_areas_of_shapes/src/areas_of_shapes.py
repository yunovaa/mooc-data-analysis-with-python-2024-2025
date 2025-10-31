#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    shape = input('Choose a shape (triangle, rectangle, circle): ')
    while shape!='':
        if shape=='triangle':
            base = float(input('Give base of the triangle: '))
            height = float(input('Give height of the triangle: '))
            print('The area is {:.6f}'.format(base*height/2))
        elif shape=='rectangle':
            width = float(input('Give width of the rectangle: '))
            height = float(input('Give height of the rectangle: '))
            print('The area is {:.6f}'.format(width*height))
        elif shape=='circle':
            radius = float(input('Give radius of the circle: '))
            print('The area is {:.6f}'.format(math.pi*radius**2))
        else:
            print('Unknown shape!')
        shape = input('Choose a shape (triangle, rectangle, circle): ')



if __name__ == "__main__":
    main()
