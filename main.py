import turtle
import game_state

from config import SIZE, CELL, HALF, EMPTY, X, O

from ui_board import draw_board, draw_o, draw_x, cell_center, draw_line

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
