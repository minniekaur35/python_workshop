# lambda expression
# take the last name, use title() and sort

from math import pi 


names = ['Morgan Freeman', 'Sara chappelle', 'Emily Rose', 'Roberto Cavalli', 'Amber heard', 'K.S. Makhani', 'Mughli gutti']

# in place edit
# This  is sorting with whole  string
names.sort()
print("normal  sort:", names)

print('-' * 70)

names.sort(reverse=True)
print("reverse  sort:", names)

print('-' * 70)

names.sort(key= lambda name: name.split(" ")[-1].title())
print("last names were sorted using  lambda function: ", names)

print('-' * 70)

for x in names:
    print(x.split(' ')[-1].title())

print('-' * 70)
names.sort()
[print(x.split(' ')[0].title()) for x in names]


print('.' * 72)

def area(r):
    return pi * (r ** 2)

r = [0.9, 12, 1.2, 3.4, 5, 8.9, 6.6, 1.09]

x = list(map(area, r))

print(x)












