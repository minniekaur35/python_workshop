# check if 3 sides form a triangle
# formula to check: a + b > c, b + c > a, a + c > b

# code


sideA = input("please enter side A of the trinagle: ")
sideB = input("please enter side B of the triangle: ")
sideC = input("please enter side C of the triangle: ")

if sideA + sideB > sideC and sideB + sideC > sideA or sideA + sideC > sideB:
    print("it is a triangle")
else:
    print("it is not a triangle")



