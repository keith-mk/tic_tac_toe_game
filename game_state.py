
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

def make_move(board, row, col, player):
    pass #to be implemented

#Checks if a move is legal
#Returns True if the cell is empty, False otherwise
#Prevents overwriting existing moves
def is_valid_move(board, row, col):
    pass #to be implemented


#Detects if someone has won
#Checks all rows, columns, and diagonals
#Returns the winner (X or O) or None if no winner yet

def check_winner(board):
    pass #to be implemented

#Checks for a tie/draw
#Returns True if all cells are filled
#Used to detect cat's game (tie)

def is_board_full(board):
    pass #to be implemented

