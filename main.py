import pygame ,sys

class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.image.fill('White')
        self.rect = self.image.get_rect(topleft=(pos_x,pos_y))


pygame.init()


screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('sprite-Animations')
clock = pygame.time.Clock()

moving_sprites = pygame.sprite.Group()
player = Player(200,200)
moving_sprites.add(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.fill('black')
    
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.update()
    
    clock.tick(60)        
    