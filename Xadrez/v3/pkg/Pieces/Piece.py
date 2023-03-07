from abc import ABC, abstractmethod

class Piece(ABC):
    
    # Constructor
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    # Constructor
    def __init__(self, player):
        self.player = "Black" if player == 1 else "White"
        
    def my_color(self):
        return self.player