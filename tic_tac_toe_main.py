import turtle

size = 300 #size of the board
cell = size //3 # size of each cell = 100
half = size //2 

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
    draw_line( -cell //2, half, -cell // 2, -half ) # left vertical
    draw_line( cell //2, half, cell //2, -half) # right vertical

    #horizontal lines
    draw_line (-half, cell //2 , half, cell //2 ) #top horizontal line
    draw_line (-half, -cell //2 , half, -cell //2) #bottom horizontal line


def handle_click(x, y):
    # turn x, y click coordinates into row / col
    if ( x < -cell //2):
        col = 1
    elif ( x > cell //2):
        col = 3
    else:
        col = 2
    if ( y > cell //2):
        row = 1
    elif ( y < -cell //2):
        row = 3
    else:
        row = 2

    print(f"Row: ({row}, Column: {col})") # row / col registration test

    



    # Testing Click position
    #    print(f"Clicked at: ({x}, {y})") # test click
    #    turtle.penup()
    #   turtle.goto(x, y)
    #   turtle.dot(10) # draw a dot where clicked

def main ():
    draw_board()
    turtle.onscreenclick(handle_click)
    turtle.mainloop()
#    turtle.done() # keep the window open until you click - Commenting while I switch to mainloop

if __name__ == "__main__":
    main()
