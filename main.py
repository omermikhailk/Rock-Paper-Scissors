from random import randint
# To generate the random input for the computer's choice.
from sys import exit
# Allows program to exit.
from time import sleep
# Allows a natural delay to make the game seem more normal.

# Will assign a number to a decision in the game.
def choice_assigner(num):
    if num == 1:
        return "Paper"
    elif num == 2:
        return "Scissors"
    else:
        return "Rock"

def win_decider(player, computer):
    scenarios = ["It's a draw!", "You win!", 
    "The computer wins!"]
    if player == computer:
        return scenarios[0]
    elif player == "Rock":
        if computer == "Scissors":
            return scenarios[1]
        else:
            return scenarios[2]
    elif player == "Scissors":
        if computer == "Paper":
            return scenarios[1]
        else:
            return scenarios[2]
    elif player == "Paper":
        if computer == "Rock":
            return scenarios[1]
        else:
            return scenarios[2]

def main():
    tally = [0, 0, 0]
    while True:
        # Continuous loop until user exits. Allows it to repeat infinitely.
        while True:
            # Loop to make sure that the user enters 1 or exit.
            user_input = input("Write 1 to play and EXIT to exit the game.\n")
            user_input = user_input.lower()
            if user_input not in ["1", "exit"]:
                print("\nYour input was invalid. Please try again.")
                continue
            elif user_input == "exit":
                print("\nExiting...")
                sleep(0.75)
                exit()
            else:
                break
        computer_choice = randint(1, 3)
        computer_choice = choice_assigner(computer_choice)
        print("\nWhat would you like to be?")
        sleep(0.75)
        while True:
            # Loop for the choice of the user.
            try:
                player_choice = input(
                "Please enter 1 for paper, 2 for scissors and 3 for rock.\n")
                for i in player_choice:
                    if i == ".":
                        raise ValueError(
                        "You did not enter an integer. ")
                if player_choice not in ["1", "2", "3"]:
                    raise ValueError(
                    "You cannot enter a string, list, float or dictionary. Or a number which is \
not 1, 2 or 3.")
                else:
                    break
            except ValueError as ValErr:
                print("\nERROR: ", ValErr, "Please try again.\n")
            continue

        player_choice = choice_assigner(int(player_choice))
        
        sleep(1)
        print(
        "\nYou chose {} and the computer chose {}.".format(player_choice.lower(), computer_choice.lower()))
        sleep(0.25)
        if win_decider(player_choice, computer_choice)[-2] == "n":
            tally[0] += 1
            # Win
        elif win_decider(player_choice, computer_choice)[-2] == "w":
            tally[1] += 1
            # Draw
        else:
            tally[2] += 1
            # Loss
        print(win_decider(player_choice, computer_choice))
        sleep(0.75)
        print(
        "You have won {!s} games, lost {!s} games and drawed {!s} games.\n\n\n".format(tally[0], tally[2], tally[1]))
        # This is the win counter
        continue

main()