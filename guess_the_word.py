# Concepts needed: strings, variables, random function, variables, input/ output

"""
Similar to ‘What’s the Number?’, this name focuses on the user having to guess the randomly generated word. You can create a list from which the word would have to be guessed and also set a cap on the number of guesses allowed. 

After this, you can create the rules yourself! When the user inputs the word, you can indicate whether the alphabet written appears in this particular position or not. You will need a function to check if the user is inputting alphabets or numbers and to display error messages appropriately. 
"""

import random

list_of_words = ["hello", "lotus", "mochi", "price", "cutie", "mango", "apple", "siren"]

chosen = random.choice(list_of_words)

print("Welcome to the 'guess a word' game. You will be given 5 lives. Once your lives are finished, the game will be over")
print('\033[1m' + "Good Luck !" + '\033[0m')
#  guess = input("Enter a five letter word: ") # (Use in method 2 & method 3 only)

guess = "" # this should be used for 'for' loop

try_ = 5



# method 1

for a_try in range(try_):
    # word = chosen
    if guess != chosen:
        if guess != "":
            print("You lost a life. Try again!")
        guess = input("Enter a five letter word: ")
    else:
        print("Hurray! You have guessed it with tries to spare.")
        break

if guess != chosen:
    print("You have used all of your lives. Game Over x_x")
else:
    print("You cracked the word. You won!")







# method = 2
# while guess != chosen:
#     if try_ > 1:
#         try_ -= 1
#         print(f"incorrect, you have {try_}/5 life. Better luck next time ...")
#         guess = input("Enter a five letter word: ")
#     else:
#         print("used up all your lives, you are dead x_x")
#         break
        

# if guess == chosen:
#     print("You've guessed it. That was the correct word. You WON!!")
# else:
#     print("Game Over!!")

# method = 3

# while try_ > 1:
#     try_ -= 1

#     if guess != chosen:
#         print(f"you have lost 1 life. Your remaining lives are {try_}. Keep trying !")
#         guess = input("Enter a five letter word: ")
    
#     else:
#         print("Hurray! You found the word.")
#         break

# if try_ == 1:
#     print("GAME OVER !!")


