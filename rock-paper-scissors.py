import random

# ANSI color codes
blue = "\033[0;34m"
green = "\033[0;32m"
yellow = "\033[1;33m"
red = "\033[0;31m"
reset = "\033[0m"

# Game variables
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
restart_game = ''
score = {'user': {'win': 0, 'loss': 0, 'rank': 0}, 'computer': {'win': 0, 'loss': 0, 'rank': 0}}
draw_count = 0

while restart_game != 'no':
    # Take user input & assign user moves
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    # Randomize & assign computer moves
    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"{blue}The computer chose {computer_move}.{reset}")

    # Check the winner & assign scores
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        score['user']['win'] += 1
        score['computer']['loss'] += 1
        print(f"{green}You win!{reset}\n")

    elif (player_move == rock and computer_move == rock) or \
            (player_move == paper and computer_move == paper) or \
            (player_move == scissors and computer_move == scissors):
        draw_count += 1
        print(f"{yellow}Draw{reset}\n")
    else:
        score['user']['loss'] += 1
        score['computer']['win'] += 1
        print(f"{red}You lose!{reset}\n")

    restart_game = input("Type [yes] to Play Again or [no] to quit: ")

    if restart_game == 'yes':
        continue
    elif restart_game == 'no':

        # Assign score ranks
        if score['user']['win'] > score['computer']['win']:
            score['user']['rank'] = 1
            score['computer']['rank'] = 2

        elif score['computer']['win'] > score['user']['win']:
            score['computer']['rank'] = 1
            score['user']['rank'] = 2
        else:
            score['user']['rank'] = 1
            score['computer']['rank'] = 1

        # Sort players by rank
        score = dict(sorted(score.items(), key=lambda item: item[1]["rank"]))
        output_lines = []

        # Format output
        for player, stats in score.items():
            space_num = " " * (6 if player == 'user' else 2)
            output_lines.append(
                f"{stats['rank']}     {player}{space_num}{stats['win']}     {stats['loss']}\n"
                f"----------------------------"
            )
        score_stats = "\n".join(output_lines)
        score_board = f"\nThank you for playing!\n\n"\
                      f"Latest Scores:\n\n"\
                      f"RANK  NAME      WINS  LOSSES\n"\
                      f"============================\n"\
                      f"{score_stats}\n"\
                      f"Draws: {draw_count}"
        print(score_board)
        break
    else:
        raise SystemExit("Invalid input. Try again...")
