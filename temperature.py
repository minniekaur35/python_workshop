
cities = [("Brampton", 34), ("Windsor", 36), ("Sydney", 9), ("Cambridge", 33), ("Thunder Bay", 32), ("New York City", 26), ("Canton", 35)]


c_to_f = lambda data: (data[0], 9/5 * data[1] + 32)

new_Data = list(map(c_to_f, cities))
print(new_Data)

print("<>" * 33)

# filter the cities that has temp higher than 30


temp = list(filter(lambda data: data[1] > 30, cities ))
print(temp)



print('abc. DEP'.capitalize())

try:
    print(1)
except:
    print(2)
finally:
    print(3)



