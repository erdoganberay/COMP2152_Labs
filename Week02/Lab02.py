import random

choices = ["Rock", "Paper", "Scissors"]

player_choice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissors): ") # 1, 2, 3

player_choice = int(player_choice)

if player_choice < 1 or player_choice > 3:
    print("Error: Choice should be between 1 and 3!")
else:
    computer_choice = random.randint(1, 3)

#    player_choiceIndex = choices[player_choice - 1] # ==> 0, 1, 2
#    computer_choiceIndex = choices[computer_choice - 1]
#    print(player_choiceIndex,  computer_choiceIndex)

    # Determine the winner logic using if/elif/else
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 1 and computer_choice == 3:
        print("Rock beats Scissors - You win!")
    elif player_choice == 2 and computer_choice == 1:
        print("Paper beats Rock - You win!")
    elif player_choice == 3 and computer_choice == 2:
        print("Scissors beats Paper - You win!")     
    else:
        print("You lose!")   
