
# File to keep track of games states and game logic

from config import SIZE, CELL, HALF, EMPTY, X, O


def create_board():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]


# Updates the board with a player's move
# Takes the board, position, and which player (X or O)
# Modifies the board at that position

make_move(board, row, col, player):


#Checks if a move is legal
#Returns True if the cell is empty, False otherwise
#Prevents overwriting existing moves
is_valid_move(board, row, col):



#Detects if someone has won
#Checks all rows, columns, and diagonals
#Returns the winner (X or O) or None if no winner yet

check_winnder(board)


#Checks for a tie/draw
#Returns True if all cells are filled
#Used to detect cat's game (tie)
is_board_full(board):


