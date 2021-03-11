# lets create a board object ot represent the minesweeper game
# this is so that we can just say "create a new board object", or "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set() # if we dig at 0,0 this self.dug = {(0,0)}

# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: Create the board and plant the bombs
    # Step 2: Show the user the board and ask where they would like to dig
    # Step 3a: If location is a bomb, show game over
    # Step 3b: If location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig
    pass
