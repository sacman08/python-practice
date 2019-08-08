def display_board(board):  # Board setup
  print('\n'*100)
  print(board[1] + ' | ' + board[2] + ' | ' + board[3])
  print(board[4] + ' | ' + board[5] + ' | ' + board[6])
  print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def player_input():  # Player assignment - use while loop to keep asking until a valid character is entered

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):   # Allows player to place their marker at specific board index

    board[position] = marker

def win_check(board, mark):  # Check all rows, columns, diagonals for sharing the same marker to check for a winner
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or   # Rows
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or   # Columns
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or   # Diagonals
    (board[3] == mark and board[5] == mark and board[7] == mark))

import random

def choose_first():  # Randomize who goes first

    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):   # Check to see if a space on the board is still available
   return board[position] == ' '

def full_board_check(board):  # Checks to see if board is full resulting in a draw
    for i in range(1,10):
        if space_check(board,i):  # If there is free space, board is NOT full
            return False
    return True

def player_choice(board):  # Asks for the player's next move choice
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9): '))

    return position

def replay():   # Asks if the players want to play again
    choice = input("Play again? Enter Yes or No: ")
    return choice == 'Yes'

# Logic to run the game
# While loop needed to keep running the game
# Need to break out of the while loop on replay()

print ('Welcome to TIC TAC TOE')

while True:
    # Game Setup (Board, Players, Player turns)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n: ')
    if play_game == 'y':
        game_on = True
    else: game_on = False

    # Game Play
    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # Choose a place to move
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player1_marker,position)

            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):  # Check for tie
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:   
            # Show the board
            display_board(the_board)
            # Choose a place to move
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player2_marker,position)

            # Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 1' 

    if not replay():
        break
