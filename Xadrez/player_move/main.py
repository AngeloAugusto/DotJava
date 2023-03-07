import pygame
import sys

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
        
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Chess V2')
pygame.display.flip()
player = Player()
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))

    player.draw(screen)
    player.handle_keys()
        
    pygame.display.update()
    pygame.time.Clock().tick(60)