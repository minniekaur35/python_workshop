# Concepts needed: strings, concatenation, variables, print. 

""" 

The program first prompts the user to enter a series of inputs. These can be an adjective, a preposition, a proper noun, etc. Once all the inputs are in place, they are placed in a premade story template using concatenation. In the end, the full story is printed out to read some misintended madness!

"""
import random 
print("WELCOME TO SPIN A YARN TO CREATE A STORY WITH YOUR CHOSEN WORDS")

adjective = input("Enter an adjective of your choice: ")
preposition = input("Enter a preposition: ")
proper_noun = input("Now, enter a proper noun: ")
just_a_choice = ["home", "beach", "theatre", "Mars", "Jupiter", "Cemetery", "Love Island", "Your Granny", "Mommy"]
name = ["Britney Spears","Donald Duck", "Sandy", "Mandy", "Randy", "Karen", "Sasha", "Gummy Bear", "Ludo","Trisha", "Kelly", "Molly", "Polly", "Schnappi"]
action_choice = ["kill", "kiss", "slap", "drink", "sleep","ride", "work", "cook", "serve", "hide", "throw", "dance", "plan", "share", "clean", "serve", "count"]
action = random.choice(action_choice)
choices = random.choice(just_a_choice)
name_choice = random.choice(name)
he_or_she = ["he", "she", "they", "them"]
pronouns = random.choice(he_or_she)
txt = ("Once upon a time, there was {0} named {4} who lived  in a {2}. {6} used to eat {2} {1} {3}. Because {6} was very {0}, nobody wanted to take {4} to {3}. This is quite a rubbish story because I'm {1} {3}.  I'm not going to stop until you {5} {1} {4}. {6} was {3} {5}. ")

print(txt.format(adjective, preposition, proper_noun, choices, name_choice, action, pronouns))