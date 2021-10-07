import pygame
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  
 
HEIGHT = 500
WIDTH = 500
FPS = 120
STEPS = 350

 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game V1")  


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.add_x = 0
        self.add_y = 0 
        self.pos = vec((10, 385))



    def move(self):
        
        

        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.add_x = -WIDTH/STEPS
            self.add_y = 0
            
        elif pressed_keys[K_RIGHT]:
            self.add_x = WIDTH/STEPS
            self.add_y = 0
        elif pressed_keys[K_UP]:
            self.add_x = 0
            self.add_y = -WIDTH/STEPS
        elif pressed_keys[K_DOWN]:
            self.add_x = 0
            self.add_y = WIDTH/STEPS



        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT


        self.pos.x = self.pos.x  + self.add_x
        self.pos.y = self.pos.y + self.add_y  

        self.rect.midbottom = self.pos


    def collision(self):
        print("coll")





Game = Game()

all_sprites = pygame.sprite.Group()
all_sprites.add(Game)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    displaysurface.fill((0,0,0))
    
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    
    Game.move()

    pygame.display.update()
    FramePerSec.tick(FPS)