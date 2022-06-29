# Create a method: area of circle, area of square, area of triangle, area of sphere, area of cube, area of tetrahedron/pyramid
import fire
from math import pi, sqrt

def circle_area_printer(radius, base, boobs, dick, nose=4, leg=5):
    if isinstance(radius, str):
        radius = int(radius)
    # else:
    #     rad = radius
    if radius > 0:
        areaOfCircle = pi * (radius ** 2)
        print(f"Area is: {areaOfCircle}")
    else:
        print("Radius cannot be a negative value, Area not computed")

def circle_area(radius):
    if isinstance(radius, str):
        rad = int(radius)
    else:
        rad = radius
    # print(dir(rad))
    areaOfCircle = 0
    # compute area of circle
    if rad > 0:
        areaOfCircle = pi * (rad ** 2)
    else:
        print("radius cannot be a negative value")
    return areaOfCircle

def square_area(a):
    # compute area of square
    if a > 0:
        areaOfSquare = a ** 2
    else:
        print("side cannot be negative or 0")
    return areaOfSquare

def triangle_area(a, b):
    # compute area of triangle - a is height and b is base
    if a <=0 and b <=0 :
        print("Cannot return area, invalid input. Please enter a positive value. Value must not be 0")
    else:
        areaOfTriangle  = a * b / 2
    return areaOfTriangle

def sphere_area(a):
    if a <= 0:
        print("Cannot return area, invalid input. Please enter a positive value. Value must not be 0")
    else: 
        areaOfSphere = 4 * pi * (a ** 2)
    return areaOfSphere

def cube_area(a): 
    if a <= 0:
        print("Cannot return area, invalid input. Please enter a positive value. Value must not be 0")
    else:
        areaOfCube = 6 * a ** 2
    return areaOfCube

def tetrahedron_area(a): 
        if a <= 0:
            print("Cannot return area, invalid input. Please enter a positive value. Value must not be 0")
        else: 
            areaOfTetrahedron = sqrt(3) * a ** 2
        return areaOfTetrahedron


if __name__ == '__main__':
    fire.Fire(circle_area_printer)
