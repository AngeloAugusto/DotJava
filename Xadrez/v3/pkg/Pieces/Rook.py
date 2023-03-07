from pkg.Pieces.Piece import Piece

class Rook(Piece):
    
    def valid_moves(self):
        return "my valid moves"
    
    def my_name(self):
        return self.my_color()+" Rook"