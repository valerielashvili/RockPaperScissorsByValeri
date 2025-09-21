import random

# ANSI color codes
blue = "\033[0;34m"
green = "\033[0;32m"
yellow = "\033[1;33m"
red = "\033[0;31m"
reset = "\033[0m"

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
restart_game = ""

while restart_game != "no":
    # Take user input and assign user moves
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    # Randomize and assign computer moves
    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"{blue}The computer chose {computer_move}.{reset}")

    # Check the winner
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == scissors):
        print(f"{green}You win!{reset}")
    elif (player_move == rock and computer_move == rock) or \
            (player_move == paper and computer_move == paper) or \
            (player_move == scissors and computer_move == scissors):
        print(f"{yellow}Draw{reset}")
    else:
        print(f"{red}You lose!{reset}")

    restart_game = input("Type [yes] to Play Again or [no] to quit: ")

    if restart_game == 'yes':
        continue
    elif restart_game == 'no':
        print("Thank you for playing!")
        break
    else:
        raise SystemExit("Invalid input. Try again...")