import pygame
import random
from Piece import Piece

chess_square_size = 60
window = None
selected_piece = None
old_piece_x=-1
old_piece_y=-1
pieces = {"TOWER": "t","BISHOP":"b","HORSE":"h","KING":"k","QUEEN":"q","PAWN":"p"}
players = ["b","w"]
transparent = (0, 0, 0, 0)
loading_game = True
player_turn = None
board_pieces = [[None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8]

def load_window():
    pygame.init()
    screen = pygame.display.set_mode((8*chess_square_size, 8*chess_square_size))
    pygame.display.set_caption('Chess V2')
    pygame.display.flip()
    return screen

def draw_board(window, player):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (100, 100, 100)
            pygame.draw.rect(width=100, surface=window, color=color, rect=pygame.Rect(
                chess_square_size*(i), chess_square_size*(j), chess_square_size, chess_square_size))
            if loading_game:
                set_start_pieces(i,j,window,player)
            else:
                update_board(window)
    pygame.display.flip()
    
def update_board(window):
    for i in range(8):
        for j in range(8):
            if board_pieces[i][j] != None:
                board_pieces[i][j].draw(window)

def set_start_pieces(i, j, screen, player):
    if j == 0:
        first_and_last_row(i,j,screen,player)
        
    elif j == 1:
        create_piece(i, j, "PAWN", screen, player)
        
    elif j == 6:
        create_piece(i, j, "PAWN", screen, 1 if player == 0 else 0)
        
    elif j == 7:
        first_and_last_row(i,j,screen,1 if player == 0 else 0)

def first_and_last_row(i,j,screen,player):
    if i == 0 or i == 7:
        create_piece(i, j, "TOWER", screen, player)
    elif i == 1 or i == 6:
        create_piece(i, j, "HORSE", screen, player)
    elif i == 2 or i == 5:
        create_piece(i, j, "BISHOP", screen, player)
    elif (i == 3 and player == 0) or (i == 4 and player == 1):
        create_piece(i, j, "QUEEN", screen, player)
    elif (i == 3 and player == 1) or (i == 4 and player == 0):
        create_piece(i, j, "KING", screen, player) 
    
def create_piece(i, j, name, screen, player):
    piece = Piece(name,j*chess_square_size,i*chess_square_size,players[1 if player== 0 else 0]+pieces[name], player)
    piece.draw(screen)
    place_piece(i, j, piece)

def place_piece(i, j, piece):
    board_pieces[j][i]=piece

def calculate_possible_moves():
    print("calculating")

def board_cliked():
    global selected_piece
    global old_piece_x
    global old_piece_y
    global board_pieces
    global player_turn
    
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
        
    # print("x:"+str(cont_x)+ " y:"+str(cont_y))
    

    if board_pieces[cont_y][cont_x] != None and board_pieces[cont_y][cont_x].belongs_to_player(player_turn):
        selected_piece = board_pieces[cont_y][cont_x]
        old_piece_x = cont_x
        old_piece_y = cont_y
        calculate_possible_moves()
        
        # print("piece: "+board_pieces[cont_y][cont_x].name+ " "+str(board_pieces[cont_y][cont_x].x))
        
    if selected_piece != None and board_pieces[cont_y][cont_x] == None:
        print("now here")
        board_pieces[cont_y][cont_x] = selected_piece
        board_pieces[old_piece_y][old_piece_x] = None
        selected_piece.moveOneDown()
        selected_piece.moveOneDown()
        draw_board(window, player_turn)
        player_turn = 1 if player_turn == 0 else 0
        pygame.display.update()
        pygame.time.Clock().tick(60)
        selected_piece = None
        old_piece_x=-1
        old_piece_y=-1
        
        
    return (cont_x, cont_y)

if __name__ == "__main__":
    print("Chess v2")
    window = load_window()
    player = random.randint(0, 1)
    player_turn = 1 if player == 0 else 0
    draw_board(window, player)
    loading_game = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                x,y = board_cliked()
        
        pygame.display.update()
        pygame.time.Clock().tick(60)
                
        