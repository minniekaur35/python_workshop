
# This program converts the dec number to hex 
import math
askTheNumber = input("please enter a number :")
number = int(askTheNumber)
hexN = hex(number)

print(hexN)

# check if the number is even or odd
# multiply the number from 1 to 10

if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

x = []

for i in range(1, 11):
    x = number * i

    print(x)
