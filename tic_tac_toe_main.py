import turtle

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

    size = 300 #size of the board
    cell = size //3 # size of each cell = 100
    half = size //2 

#Vertical Lines
    draw_line( -cell //2, half, -cell // 2, -half ) # left vertical
    draw_line( cell //2, half, cell //2, -half) # right vertical

#horizontal lines
    draw_line (-half, cell //2 , half, cell //2 ) #top horizontal line
    draw_line (-half, -cell //2 , half, -cell //2) #bottom horizontal line

def main ():
    draw_board()
    turtle.done() # keep the window open until you click

if __name__ == "__main__":
    main()
