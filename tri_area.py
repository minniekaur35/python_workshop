# _______imports _________
import math
import sys

# _______Functions________

def triangle_area(b, h):
    #this functions compute the area of a triangle
    area = (1.0/2.0) * b * h
    return area

# ________ Main method ________

if __name__ == '__main__':
    b = input("please enter a base of a triangle: ")
    h = input("please enter height of a triangle: ")
    base = int(b)
    height = int(h)
    print("AREA of triangle is ",  triangle_area(base, height))
