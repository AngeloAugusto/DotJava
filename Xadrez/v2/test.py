import pygame
import sys
import time
import random
from Piece import Piece

chess_square_size = 60

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((64, 54, 16, 16))
        self.sprite = pygame.image.load('./imgs/wp.png')

    def handle_keys(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 1)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)
        
def load_window():
    pygame.init()
    screen = pygame.display.set_mode((8*chess_square_size, 8*chess_square_size))
    pygame.display.set_caption('Chess V2')
    pygame.display.flip()
    return screen

def prepare_board(window, player):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (100, 100, 100)
            pygame.draw.rect(width=100, surface=window, color=color, rect=pygame.Rect(
                chess_square_size*(i), chess_square_size*(j), chess_square_size, chess_square_size))
            # set_start_pieces(i,j,window,player)
    pygame.display.update()
    
def board_cliked():
    cont_size = chess_square_size
    cont_x = 0
    cont_y = 0
    while pygame.mouse.get_pos()[0] > cont_size:
        cont_size = chess_square_size + cont_size
        cont_x = 1 + cont_x
        
    cont_size = chess_square_size
    while pygame.mouse.get_pos()[1] > cont_size:
        cont_size = chess_square_size + cont_size
        cont_y = 1 + cont_y
        
    

window = load_window()
piece = Piece("peca",60,60,'wp')

piece2 = Piece("peca",120,60,'wp')
player = random.randint(0, 1)
prepare_board(window, player)
running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        left, middle, right = pygame.mouse.get_pressed()
        # if right:
            # piece.moveOneUp()
        if left:
            x,y = board_cliked(window)
            # piece.moveOneDown()
    # window.fill((255, 255, 255))
    prepare_board(window, player)

    piece.draw(window)
    piece2.draw(window)
    # piece.handle_keys()
    
        
    pygame.display.update()
    pygame.time.Clock().tick(120)