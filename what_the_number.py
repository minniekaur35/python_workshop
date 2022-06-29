""" 
What’s the number?
Concepts needed: print, while loop, if/else statements, random function, input/ output

This is a guessing game that the user plays with the program/computer. The program generates a random number using the random function. The user tries to guess it by inputting a value. The program then indicates whether the guess is right or not. If it is wrong, then the program should tell how off the guess was. If it is right, there should be another positive indicator. You can place a limit on the number of guesses allowed. 
"""

import random

print("This is a guessing game. Enter a number to guess if you were able to guess the number computer had selected")
    
number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = input("Guess a number from 1 to 10:  ")
    guess = int(guess)
    
    if guess == number:
        print("Congratulations! You guessed it")
        break
    elif guess > number:
        print("Try with a smaller number")
        
    else:
        print("Sorry! Try again with a bigger number")