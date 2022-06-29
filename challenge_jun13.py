# fix a num
# from the num, multiply the previous numbers
# multiply recursively from the range
# factorial = 1 * 2 * 3 ....... 18

# def FirstFactorial(num):
# for i in range(1, 19):
#     i = i * i+1
#     print(i)
# print(FirstFactorial(18))

def FirstFactorial(num):
    if num == 1:
        return 1
    return num * FirstFactorial(num - 1)

print(FirstFactorial(18))



