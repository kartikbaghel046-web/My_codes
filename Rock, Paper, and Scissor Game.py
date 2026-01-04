import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your choice(Rock, paper, Scissor) : ")
user_choice = user_choice.capitalize()
comp_choice = random.choice(item_list)

if user_choice in item_list:
    print()
    print(f"Your choice is {user_choice}, Computer choice is {comp_choice}")
else:

    print("Please follow game's rule by choosing Rock, paper, and Scissor")
    

if user_choice == comp_choice:
    print("It's a tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Coputer Win")
    else:# Scissor
        print("You win")
elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("You Win")
    else: # Scissor
        print("Computer Win")
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Computer Win")
    else: # Paper
        print("You Win")
