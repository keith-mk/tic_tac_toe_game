import turtle
import game_state

from config import SIZE, CELL, HALF, EMPTY, X, O




# Text UI interactions
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

def show_message(msg):
    text_turtle.clear() #remove previoux tesst drawn by text turtle
    text_turtle.goto(0, SIZE //2 + CELL)
    text_turtle.write(msg, align="center", font= ("Arial", 16, "bold"))




#globals with initialization
board = game_state.create_board()

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


#function for handling mouse clicks, this is also effectively waiting until there's a click even then executing test functions
def handle_click(x, y):
    # turn x, y click coordinates into row / col
    if ( x < -CELL //2):
        col = 1
    elif ( x > CELL //2):
        col = 3
    else:
        col = 2
    if ( y > CELL //2):
        row = 1
    elif ( y < -CELL //2):
        row = 3
    else:
        row = 2
    print(f"Row: ({row}, Column: {col})") # row / col registration test
    #draw_o(row, col)
    draw_x(row,col)



    # Testing Click position
    #    print(f"Clicked at: ({x}, {y})") # test click
    #    turtle.penup()
    #   turtle.goto(x, y)
    #   turtle.dot(10) # draw a dot where clicked

def main ():
    draw_board()
    show_message("Would you like to play a game?")
    turtle.onscreenclick(handle_click)
    turtle.mainloop()
#    turtle.done() # keep the window open until you click - Commenting while I switch to mainloop

if __name__ == "__main__":
    main()
