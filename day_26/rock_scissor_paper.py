# 27 - Aug- 2020
# Automate the boring stuff with Python (chapter - 3)
# Rock paper scissor
# I have modified the original code. See the author's website for the original code..

import random, sys

print('Welcome To "ROCK, PAPER, SCISSORS"!')

wins = 0
losses = 0
ties = 0

while True:                 # the main game loop.
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
    while True:             # The player input loop.
        print("Enter your move: enter 'r' for Rock, 'p' for Paper and 's' for Scissors and 'q' for Quit: ")
        player_move = input()
        if player_move == 'q':
            sys.exit()      # Quit the program
        #if player_move == 'r' or player_move == 'p' or player_move == 's':
            break           # break out of the player input loop.
        #print('Type one of r, p, s or q.')
        

# Display what the player chose:
        if player_move == 'r':
            print('ROCK versus...')
        elif player_move == 'p':
            print('PAPER versus...')
        elif player_move == 's':
            print('SCISSORS versus...')


# Display what the computer chose:
        rand_number = random.randint(1, 3)
        if rand_number == 1:
            computer_move = 'r'
            print('ROCK!')
        elif rand_number == 2:
            computer_move = 'p'
            print('PAPER!')
        elif rand_number == 3:
            computer_move = 's'
            print('SCISSORS!')


# Display and record the win/loss/tie:
        if player_move == computer_move:
            print('It is a tie!')
            ties = ties + 1
            print(f"You score is:\nWins: {wins} \nTies: {ties} \nLosses: {losses}")
        elif player_move == 'r' and computer_move == 's':
            print('You win!')
            wins = wins + 1
            print(f"You score is:\nWins: {wins} \nTies: {ties} \nLosses: {losses}")
        elif player_move == 'p' and computer_move == 'r':
            print('You win!')
            wins = wins + 1
            print(f"You score is:\nWins: {wins} \nTies: {ties} \nLosses: {losses}")
        elif player_move == 's' and computer_move == 'p':
            print('You win!')
            wins += 1
            print(f"You score is:\nWins: {wins} \nTies: {ties} \nLosses: {losses}")
        elif player_move == 'r' and computer_move == 'p':
            print('You lose!')
            losses = losses + 1
            print(f"You score is:\nWins: {wins} \nTies: {ties} \nLosses: {losses}")
        elif player_move == 'p' and computer_move == 's':
            print('You lose!')
            losses = losses + 1
            print(f"You score is:\nWins: {wins} \nTies: {ties} \nLosses: {losses}")
        elif player_move == 's' and computer_move == 'r':
            print('You lose!')
            losses = losses + 1
            print(f"You score is:\nWins: {wins} \nTies: {ties} \nLosses: {losses}")