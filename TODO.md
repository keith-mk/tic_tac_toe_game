

## Dec 26, 2025 Next steps

Next immediate
- game state management setup
    - Tracking where marks have been placed
- considering game phase and menu selection
    - Debating if i want to get into that now

Simple task
- check for cell click location
- setup 2D array of what is in each square
- To add second - check if cell is occupied
- Click in a square an X or 0 is Drawn, centered in that square




Overall tasks 
- click handling inputs
    - User prompt to say who's turn goes first
    - nice to have if there's a "Who goest first" opening prompt
    - clicking an occupied square should return a message "this space already has a " .."
- Add Player selection
    - Play 2 humans
    - play with AI
        - AI intelligence settings
- Draw X or O 
    - generalized X/O drawing function, pass in a cell coordinates?
- Game end
    - Identify when a winner has 3 in a row
    - Nice to have, draw a line through the connection
    - Message to users
- Loop new game
    - Give prompt for user to have the option to start a new game
- Project wrap-up
    - See if there's a way to translate the game into a self container executable
    - Code clean-up commenting

Function break down
    draw board
    Handle clicks - return the position of the click within the row / column of the grid
    Draw XO_input - use row/col as input
        Add error handling later
    
        