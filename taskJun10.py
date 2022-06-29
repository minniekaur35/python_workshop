# Find third largest number from a list
# don't use max or sort function (should be an unsorted list)


# def largernumber(list):
#     large_num = list[0]
#     for i in list:
#         if i > list[0]:
#             large_num = i
#     return large_num

listed_nos = [33, 77, 98, 102, 35, 69]
# print(largernumber(list))

# Manpreet method: Formula no. 33
# first_num = list[0]
# second_num = list[0]
# third_num = list[0]

# for i in list:
#     if first_num > third_num and second_num < third_num:
#         third_num = list[0]
#     elif second_num, third_num < first_num:
#         first_num = list[0]
#     else:
#         second_num = list[0]
    
    
print("----"*9)

# Method 1: normal human brain method
# 3rd largest number 
# 1st find largest
# 2nd largest if you find largest ignore find next largest no.
# 3rd largest loop go through each  ignore  numbber found 
Fst_largest = 0
for i in listed_nos:
    if i > Fst_largest:
        Fst_largest = i

print( f"first largest is {Fst_largest}")

Snd_largest = 0
for i in listed_nos:
    if i > Snd_largest and Fst_largest != i:
        Snd_largest = i  


print( f"second largest is {Snd_largest}")


Trd_largest = 0
for i in listed_nos:
    if i > Trd_largest and Fst_largest != i and Snd_largest != i:
        Trd_largest = i


print( f"Third largest is {Trd_largest}")


print("----"*9)

# Method 2: child loops
# Start with first element
# Compare element with all other elements, if any one is larger then I will ignore this no.
# And count how manu  numbers are  bigger than this number
for i in listed_nos:
    print(f"checking for this number: {i}")
    # Start the counting
    count_numbers_bigger_than_i = 0
    # Compare all numbers and find how many numbers are bigger than i
    for j in listed_nos:
        if j > i:
            count_numbers_bigger_than_i += 1
    # if we find count is 2, that means this is the third largest number so print
    if count_numbers_bigger_than_i == 2:
        print(f"Third largest number is {i}")
        break
    
    print(f"count is {count_numbers_bigger_than_i}")



print("----"*9)
listed_nos = [96, 46, 8, 758, 66, 666, 69, 143, 52, 969]
# Method 3: Optimize
# Reduce number of loops - best is to loop only once
# start with smallest number
# Save that number in 3 variables
# Go to each element
# 1 thing assume a smallest number ya ek exact number to start 
smallest_in_list = min(listed_nos)
print(f"starting number: {smallest_in_list}")
Fst_largest = smallest_in_list
Snd_largest = smallest_in_list
Trd_largest = smallest_in_list

for i in listed_nos:
    if i > Fst_largest:
        # print(f"case 1 for {i}")
        Trd_largest = Snd_largest
        Snd_largest = Fst_largest
        Fst_largest = i
    elif i > Snd_largest:
        # print(f"case 2 for {i}")
        Trd_largest = Snd_largest
        Snd_largest = i
    elif i > Trd_largest:
        # print(f"case 3 for {i}")
        Trd_largest = i

print( f"first largest is {Fst_largest}")

print( f"second largest is {Snd_largest}")

print( f"Third largest is {Trd_largest}")