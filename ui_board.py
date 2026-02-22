# 

import turtle
from config import SIZE, CELL, HALF, EMPTY, X, O


# function draws an o at the input row and column center
def draw_o(row,col):
    radius = CELL //2
    cx, cy = cell_center(row, col)
    turtle.penup()
    turtle.goto(cx, cy - radius)
    turtle.pendown()
    turtle.circle(radius)

# function draws an o at the input row and column center
def draw_x(row,col):
    cx, cy = cell_center(row, col)
    turtle.penup()
    turtle.goto(cx - CELL /2, cy + CELL //2) # go to top left of cell
    turtle.pendown()
    turtle.goto(cx + CELL /2, cy - CELL //2) # draw to bottom right
    turtle.penup()
    turtle.goto(cx + CELL /2, cy + CELL //2) # go to bottom left of cell
    turtle.pendown()
    turtle.goto(cx - CELL /2, cy - CELL //2) # draw to top right


def cell_center(row, col):
    cx = -(SIZE //2 + CELL //2) + col * CELL
    cy = (SIZE //2 + CELL //2) - row * CELL
    print(f"cx = {cx} cy= {cy}")
    return cx, cy

# Fucntion draw a lin between points
def draw_line (x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Function to draw a 3x 3 tic tac toe board
def draw_board():
    turtle.speed(0) # fastest drawing speed
    turtle.hideturtle() # hide the turtle cursor

    #Vertical Lines
    draw_line( -CELL //2, HALF, -CELL // 2, -HALF ) # left vertical
    draw_line( CELL //2, HALF, CELL //2, -HALF) # right vertical

    #horizontal lines
    draw_line (-HALF, CELL //2 , HALF, CELL //2 ) #top horizontal line
    draw_line (-HALF, -CELL //2 , HALF, -CELL //2) #bottom horizontal line