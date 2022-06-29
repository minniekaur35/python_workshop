import areas
import sys

# print(dir(sys))
args = sys.argv
# print(args)


radius = int(args[1])

if len(args) >= 3:
    side = int(args[2])
else:
    side =  radius

base = side + 1
height = side

kuchVariable = areas.circle_area_printer( radius)
print(f"Area of circle with radius {radius} is using printer method : " + str(kuchVariable))

print(f"Area of circle with radius {radius} is : " + str(areas.circle_area(radius)))

print(f"Area of square with side {side} is : " + str(areas.square_area(side)))

print(f"Area of triangle with height {height} and base {base} is : " + str(areas.triangle_area(height, base)))

print(f"Area of sphere with radius {radius} is : " + str(areas.sphere_area(radius)))

print(f"Area of cube with side {side} is : " + str(areas.cube_area(side)))

print(f"Area of tetrahedron with side {side} is : " + str(areas.tetrahedron_area(side)))