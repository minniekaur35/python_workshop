# make a game rock,paper, scissor
""" rock > scissor, paper > rock, scissor > paper"""
import random 

print("Welcome to Rock, Paper, Scissor game :)")

user_input = input("Please enter one of this option: Rock, Paper or Scissor: ")

list_of_inputs =["rock", "paper", "scissor"]

selection = random.choice(list_of_inputs)


if user_input == selection:
    print(f"Its a tie because you selected {user_input} and I have selected {selection}")
elif user_input == "rock":
    if selection == "paper":
        print(f"I chose: {selection}")
        print(f"You chose: {user_input}")
        print("Paper overpowers Rock. I won!")
        print("you are 0 and I'm 1")
    else:
        print(f"I chose: {selection}")
        print(f"You chose: {user_input}")
        print("You are the winner! I'm dead.")
        print("you are 1 and I'm 0")
elif user_input == "paper":
    if selection == "scissor":
        print(f"I chose: {selection}")
        print(f"You chose: {user_input}")
        print("I just tore you up. A winner !")
        print("you are 0 and I'm 1")
    else:
        print(f"I chose: {selection}")
        print(f"You chose: {user_input}")
        print("You tore me up, Congratulations!")
        print("you are 1 and I'm 0")
elif user_input == "scissor":
    if selection == "rock":
        print(f"I chose: {selection}")
        print(f"You chose: {user_input}")
        print("I smashed you. I won")
        print("you are 0 and I'm 1")
    else:
        print(f"I chose: {selection}")
        print(f"You chose: {user_input}")
        print("You are a winner. But you may have taken the game but I'll win!")
        print("you are 1 and I'm 0")
    

