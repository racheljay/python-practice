class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(0)] # we will use a single list to represent 3x3 board
        self.current_winner = None # keep track of winner

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')

    # static method: a method that does not take a self or cls parameter. It cannot modify state and has limited data access
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')
    
    def available_moves(self):
        moves = []
        for (i, x) in enumerate(self.board):
            