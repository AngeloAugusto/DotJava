import pygame
import random
import time

chess_square_size = 60

transparent = (0, 0, 0, 0)

pieces = {"TOWER": "t","BISHOP":"b","HORSE":"h","KING":"k","QUEEN":"q","PAWN":"p"}
players = ["b","w"]
board = [
            [ "oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo" ],
            [ "oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo" ],
            [ "oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo" ],
            [ "oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo" ],
            [ "oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo" ],
            [ "oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo" ],
            [ "oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo" ],
            [ "oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo" ],
    ]

selected_piece = ""
old_piece_x=-1
old_piece_y=-1
test = ""

def load_window():
    screen = pygame.display.set_mode((8*chess_square_size, 8*chess_square_size))
    pygame.display.set_caption('Chess')
    # screen.fill((234, 212, 252))
    pygame.display.flip()
    return screen

def prepare_board(screen, player):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (100, 100, 100)
            pygame.draw.rect(width=100, surface=screen, color=color, rect=pygame.Rect(
                chess_square_size*(i), chess_square_size*(j), chess_square_size, chess_square_size))
            set_start_pieces(i,j,screen,player)
                    
    
    pygame.display.flip()
    
def set_start_pieces(i, j, screen, player):
    piece_name=""
    if j == 0:
        if i == 0:
            piece_name = players[player]+pieces["TOWER"]
        elif i == 1:
            piece_name = players[player]+pieces["HORSE"]
        elif i == 2:
            piece_name = players[player]+pieces["BISHOP"]
        elif i == 3 and player == 0:
            piece_name = players[player]+pieces["QUEEN"]
        elif i == 3 and player == 1:
            piece_name = players[player]+pieces["KING"]
        elif i == 4 and player == 0:
            piece_name = players[player]+pieces["KING"]
        elif i == 4 and player == 1:
            piece_name = players[player]+pieces["QUEEN"]
        elif i == 5:
            piece_name = players[player]+pieces["BISHOP"]
        elif i == 6:
            piece_name = players[player]+pieces["HORSE"]
        elif i == 7:
            piece_name = players[player]+pieces["TOWER"]
        board[j][i]=piece_name
        draw_piece(screen,i,j,piece_name)
        
    elif j == 1:
        piece_name = players[player]+pieces["PAWN"]
        board[j][i]=piece_name
        draw_piece(screen,i,j,piece_name)
        
    elif j == 6:
        piece_name = players[1 if player== 0 else 0]+pieces["PAWN"]
        board[j][i]=piece_name
        draw_piece(screen,i,j,piece_name)
        
        
    elif j == 7:
        if i == 0:
            piece_name = players[1 if player== 0 else 0]+pieces["TOWER"]
        elif i == 1:
            piece_name = players[1 if player== 0 else 0]+pieces["HORSE"]
        elif i == 2:
            piece_name = players[1 if player== 0 else 0]+pieces["BISHOP"]
        elif i == 3 and player == 0:
            piece_name = players[1 if player== 0 else 0]+pieces["QUEEN"]
        elif i == 3 and player == 1:
            piece_name = players[1 if player== 0 else 0]+pieces["KING"]
        elif i == 4 and player == 0:
            piece_name = players[1 if player== 0 else 0]+pieces["KING"]
        elif i == 4 and player == 1:
            piece_name = players[1 if player== 0 else 0]+pieces["QUEEN"]
        elif i == 5:
            piece_name = players[1 if player== 0 else 0]+pieces["BISHOP"]
        elif i == 6:
            piece_name = players[1 if player== 0 else 0]+pieces["HORSE"]
        elif i == 7:
            piece_name = players[1 if player== 0 else 0]+pieces["TOWER"]
        board[j][i]=piece_name
        draw_piece(screen,i,j,piece_name)
        
    

def draw_piece(screen, i, j, piece_name):
    # print(str(i)+" "+str(j))
    global test
    piece = pygame.image.load('./imgs/'+piece_name+'.png')
    test = piece
    screen.blit(piece,(chess_square_size*(i),chess_square_size*(j)))
    
# def show_possible_moves(y,x):
#     piece = board[y][x]
#     print(piece)
#     if list(piece)[1] == 'p' and y==6:
#         print("Can go 2 or 1 up")
        

def board_cliked():
    global selected_piece
    global old_piece_x
    global old_piece_y
    global board
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
        
    print("x:"+str(cont_x)+ " y:"+str(cont_y)+" piece:"+board[cont_y][cont_x])
    if board[cont_y][cont_x] != 'oo':
        selected_piece = board[cont_y][cont_x]
        old_piece_x = cont_x
        old_piece_y = cont_y
    
    if selected_piece != "" and board[cont_y][cont_x] == 'oo':
        board[cont_y][cont_x] = selected_piece
        board[old_piece_y][old_piece_x] = 'oo'
        selected_piece = ""
        old_piece_x=-1
        old_piece_y=-1
        test.image.fill(transparent)
        
        
    # show_possible_moves(cont_y,cont_x)
    return (cont_x, cont_y)

            
if __name__ == "__main__":
    window = load_window()
    player = random.randint(0, 1)
    prepare_board(window, player)
    
    # print(board)
    running = True
    while running:
        for event in pygame.event.get():
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                x,y = board_cliked()
                # print(pygame.mouse.get_pos())
            elif right:
                print("reset")
                time.sleep(1)
                window.blit(window, (0, 0))
                time.sleep(1)
                pygame.display.update()
                time.sleep(1)
                window.fill((255,255,255))
                time.sleep(1)
                print("fim")
                prepare_board(window, player)
                
            elif event.type == pygame.QUIT:
                running = False