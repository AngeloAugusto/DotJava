from pkg.Pieces.Rook import Rook
from pkg.Pieces.Knight import Knight
from pkg.Pieces.Bishop import Bishop
from pkg.Pieces.King import King
from pkg.Pieces.Queen import Queen


class Board():

    # Constructor
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    # Constructor
    def __init__(self):
        self.grid_board = [[None]*8, [None]*8, [None]*8,
                           [None]*8, [None]*8, [None]*8, [None]*8, [None]*8]

    def populate_board(self, player):
        self.grid_board[0][0] = Rook(player)
        self.grid_board[0][1] = Knight(player)
        self.grid_board[0][2] = Bishop(player)
        self.grid_board[0][3] = King(player)
        self.grid_board[0][4] = Queen(player)
        self.grid_board[0][5] = Bishop(player)
        self.grid_board[0][6] = Knight(player)
        self.grid_board[0][7] = Rook(player)

    def show_board_in_terminal(self):
        for i in range(8):
            str_line = "|"
            for j in range(8):
                if self.grid_board[i][j] is None:
                    str_line = str_line + "\tClean\t|"
                else:
                    str_line = str_line + " "+self.grid_board[i][j].my_name()+"\t|"
            print(str_line)
            str_line = ""
