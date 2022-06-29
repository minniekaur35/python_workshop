stuffInMyRoom = {
    "bed": "blanket",
    "table": "TV", 
    "Wardrobe": "clothes" 
    }

""" put '=' when using a contructor """ # another method of commenting # docstring

bathroom = dict(deb= 'huhlu', toiletseat= 'hotseat') 
print(type(stuffInMyRoom))
print(bathroom)

# check isinstance to check if data type is dict
print(isinstance(stuffInMyRoom,dict))
print(isinstance(stuffInMyRoom,list))

# constructor of a datatype 
# poto = list('a', 'b' , 'c', 878, 9887)
# print(poto)

for key in bathroom.keys():
    value = bathroom[key]
    print(key, ":", value)

print(bathroom.values())

try:
    print(bathroom['puttu'])

except KeyError:
    print("caution! error")

dope = bathroom.get('copy', None)
print(dope)


print(80*"?")


# print("the size of list:", sys.getsizeof(list))
# print("the size of tuple:", sys.getsizeof(tuple))

# testL = timeit.timeit(stmt = "[1, 2, 3]", number = 34)
# testT = timeit.timeit(stmt = "(1, 2, 3)", number = 34)


import logging
dir(logging) # ALL CAPS - Constants, First Cap - Classes. All Lower - Methods