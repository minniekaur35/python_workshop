# Problem
# Chef wants to appear in a competitive exam. 
# To take the exam, there are following requirements:

# Minimum age limit is XX (i.e. Age should be greater than or equal to XX).
# Age should be strictly less than YY.
# Chef's current Age is AA. 
# Find whether he is currently eligible to take the exam or not.

# Input Format
# First line will contain TT, number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing three integers X, Y,X,Y, and AA as mentioned in the statement.



# age = input("Please enter your age to see if you are eligible for the competition: ")


def competition(age):
    if int(age) >= 30:
        print("Yes, you are eligible for the competition")
    elif int(age) < 30:
            print("Sorry! you are not eligible for the competition")
    
print(competition(2))
