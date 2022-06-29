# # check if the number is prime

from math import sqrt
from math import floor
import time

# """ Version 1 of checking prime number """

def is_prime_v1(num):
    if num == 1:
        return False

    for n in range(2, num):
        print(f"Checking if {num} is divisble by {n}")
        if num % n == 0:
            return False
    return True
    print("it's a prime")

# print(is_prime_v1(2777))

""" Version 2 with sqrt method """

def is_prime_v2(num):
    if num == 1:
        return False

    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    

    mirror_spot = int(sqrt(num))

    # check until mirror_spot

    for n in range(2, mirror_spot):
        # print(f"Checking if {num} is divisble by {n}")
        if num % n == 0:
            return  False
    return True


# main method


def printer(n):
    print(f"{n}: {is_prime_v2(n)}")


[  printer(n)  for n in range(3, 10000) ]

time_check = time.time()

for n in range(1, 10000):
    is_prime_v2(n)

time_check1 = time.time()

print(time_check1 - time_check)

