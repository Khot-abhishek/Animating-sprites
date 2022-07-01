import pygame ,sys

class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('attack_1.png'))
        self.sprites.append(pygame.image.load('attack_2.png'))
        self.sprites.append(pygame.image.load('attack_3.png'))
        self.sprites.append(pygame.image.load('attack_4.png'))
        self.sprites.append(pygame.image.load('attack_5.png'))
        self.sprites.append(pygame.image.load('attack_6.png'))
        self.sprites.append(pygame.image.load('attack_7.png'))
        self.sprites.append(pygame.image.load('attack_8.png'))
        self.sprites.append(pygame.image.load('attack_9.png'))
        self.sprites.append(pygame.image.load('attack_10.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft=(pos_x,pos_y))

    def animate(self):
        self.is_animating = True
    
    def update(self):
        if self.is_animating:
            self.current_sprite += 0.25   # adjust the animation speed by changing this number
            print('current_sprite: ',self.current_sprite)
            if self.current_sprite >= len(self.sprites):
                print('NSb-current_sprite: ',self.current_sprite)
                self.current_sprite = 0
                self.is_animating = False
                print('NSA-current_sprite: ',self.current_sprite)
            self.image = self.sprites[int(self.current_sprite)] 


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

        if event.type == pygame.KEYDOWN:
            player.animate()
    
    screen.fill('black')
    
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.update()
    
    clock.tick(60)        
    