from pkg.Pieces.Piece import Piece

class Queen(Piece):
    
    def valid_moves(self):
        print("my valid moves")
        
    def my_name(self):
        return self.my_color()+" Queen"