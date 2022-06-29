# # calculate the distance between empire state and times square
# import geopy
# print(help(geopy.Location))
# # from geopy.geocoders import Nominatim


def findvolume(length=1, width=1, depth=1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    value = length * width * depth
    print(f"the value is {value}")
 
print(findvolume(1, 2, 3))
findvolume(length=5, depth=2, width=4)

def square_point(x, y, z):
  x_squared = x * x
  y_squared = y * y * x
  z_squared = z * z * y
  # Return all three values:
  return x_squared, y_squared, z_squared
 
three_squared, four_squared, five_squared = square_point(3, 4, 5)
print(three_squared)
print(four_squared)


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent )
  if budget < food_bill + electricity_bill + internet_bill + rent: 
    return True
  else: 
    return False