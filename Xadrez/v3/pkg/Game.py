import pygame
import random
from pkg.Board import Board

# Here we take care of view and controller


class Game:

    chess_square_size = 60

    # Constructor
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    # Constructor
    def __init__(self, title):
        # Create window
        pygame.init()
        self.screen = pygame.display.set_mode(
            (8*self.chess_square_size, 8*self.chess_square_size))
        pygame.display.set_caption(title)
        pygame.display.flip()
        
        # Create board
        self.board = Board()
        
        # Define what player (color) you are
        player = random.randint(0, 1) # if its 1 then its black, if 0 then white
        
        # Populate board
        self.board.populate_board(player=player)
        self.board.show_board_in_terminal()
        

