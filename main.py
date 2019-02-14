from random import randint
# To generate the random input for the computer's choice.
from time import sleep
# Allows a natural delay to make the game seem more normal.

def choice_logic(num):
    """
    Based on a numeric value this function will assign it 
    to either rock, paper or scissors. And return the option.
    """
    if num == "1":
        return "Paper"
    elif num == "2":
        return "Scissors"
    else:
        return "Rock"

def choice_assigner():
    """
    This function will assign a numeric value to the computer. As 
    well as ask the user for their input. It will then make sure 
    that the input is valid.
    
    It will then assign the input to a choice in the game 
    using the choice_logic() function. It will then return 
    the choices for the computer and the user as a tuple.
    """
    user_choice = 0
    while user_choice not in [str(i) for i in range(0, 4)]:
        user_choice = input("\nPlease enter 1 for paper, 2 for scissors \
and 3 for rock.\n")
        if user_choice in ["1", "2", "3"]:
            break
        else:
            print("\nPlease enter a valid number.")
    
    computer_choice = str(randint(1, 3))
    computer_choice = choice_logic(computer_choice)
    user_choice = choice_logic(user_choice)
    
    sleep(0.75)
    
    print("\nYou chose {!s} and the computer chose {!s}.".format(user_choice,
 computer_choice))
    
    return (user_choice, computer_choice)

def win_decider(comp_and_user_choices):
    """
    Based on the result of the user's choice between rock, paper 
    or scissors, the program will determine who will win in what 
    scenario. And it will return the end result as well as a 
    message based on the result.
    """
    player = comp_and_user_choices[0]
    computer = comp_and_user_choices[1]
    
    message = (("Win", "You win!"), ("Draw", "You both drew!"), ("Loss", "You lose!"))
    if (player, computer) in (("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock")):
        return message[0]
    elif player == computer:
        return message[1]
    else:
        return message[2]

def main():
    tally = {"Win": 0, "Loss": 0, "Draw": 0}
    while True:
        # One while loop to let the user play until they want to stop
        while True:
            # A loop to make sure the user gives valid input
            user_input = input("Write 1 to play and EXIT to quit the game.\n")
            user_input = user_input.lower()
            if user_input == "exit":
                print("\nExiting...\n")
                sleep(0.75)
                return 0
            elif user_input == "1":
                break
            else:
                print("\nYou did not enter a valid answer. Please \
try again!")
        game_choices = choice_assigner()
        sleep(0.75)
        game_result, game_message = win_decider(game_choices)
        tally[game_result] += 1
        print(game_message)
        print("You have won {!s} games, lost {!s} games and drawed {!s} \
games!\n\n\n".format(*tally.values()))

if __name__ == "__main__":
    main()