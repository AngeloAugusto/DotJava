import pygame

class Piece(object):
    
    def __init__(self, name, y, x, abreviation, player):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.player = player
        self.abreviation = abreviation
        self.sprite = pygame.image.load('./imgs/'+abreviation+'.png')
        # self.rect = pygame.rect.Rect((y, x, 60, 60))
        self.rect = pygame.rect.Rect((x, y, 60, 60))
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 128), self.rect)
        surface.blit(self.sprite,self.rect)
        
        
        # def blit_alpha(self, target, source, x,y, opacity):
    #     self.rect = pygame.Surface((source.get_width(), source.get_height())).convert()
    #     self.rect.blit(target, (-x, -y))
    #     self.rect.blit(source, (0, 0))
    #     self.rect.set_alpha(opacity)        
    #     target.blit(self.rect, (x,y))

    # def draw(self, surface):
    #     pygame.draw.rect(surface, (0, 255, 128, 0), self.rect)
    #     surface.blit(self.sprite,self.rect)
        # self.blit_alpha(surface,self.sprite,self.x, self.y, 255)
        
    def moveOneUp(self):
        self.rect.move_ip(0, -60)
        print(self.name)
    
    def moveOneDown(self):
        self.rect.move_ip(0, 60)
        print(self.name)
        
    def moveOneLeft(self):
        self.rect.move_ip(-60, 0)
        print(self.name)
        
    def moveOneRight(self):
        self.rect.move_ip(60, 0)
        print(self.name)
    
    def belongs_to_player(self, player):
        return True if self.player == player else False