import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
EASYGREEN = (0, 182, 49)
DARKGREEN = (58, 121, 62)
RED = (255, 0, 0)
DARKRED = (135, 0, 0)
DARKBROWN = (111, 68, 68)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 255, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
invader_list = pygame.sprite.Group()
groundunit_list = pygame.sprite.Group()
terrain_easy_list = pygame.sprite.Group()
class Invader(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.color = RED
        self.rect.x = random.randint(710,900)
        self.rect.y = random.randint(50,450)
    def move(self):
        self.rect.x += -5


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,speedx,speedy):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.color = BLUE
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx
        self.speedy = speedy
        

class Turret(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.color = GREEN
        self.rect.x = x
        self.rect.y = y
    def move(self):
        self.rect.x += -2

class Mine(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        super().__init__()
        self.image = pygame.Surface([size,size])
        self.image.fill(BLACK)
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.size = size
        self.color = BLACK
        self.rect.x = x
        self.rect.y = y

class Terrain(pygame.sprite.Sprite):
    def __init__(self,x,color):
        super().__init__()
        self.image = pygame.Surface([30,150])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(350,480)
        
    def move(self):
        self.rect.x += -2
        if self.rect.x < -200:
            self.rect.x = 720

class Sky(pygame.sprite.Sprite):
    def __init__(self,x,color):
        super().__init__()
        self.height = random.randint(20,150)
        self.image = pygame.Surface([30,self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
    def move(self):
        self.rect.x += -2
        if self.rect.x<-200:
            self.rect.x=720


#grass1 = Terrain(720,DARKGREEN)


for x in range(-200, 1400, 30):
    
    grass = Terrain(x, EASYGREEN)
    all_sprites_list.add(grass)
    terrain_easy_list.add(grass)

    sky = Sky(x, WHITE)
    all_sprites_list.add(sky)
    terrain_easy_list.add(sky)
    
    




invader1 = Invader(50,25)
all_sprites_list.add(invader1)
invader_list.add(invader1)
invader2 = Invader(50,25)
all_sprites_list.add(invader2)
invader_list.add(invader2)
invader3 = Invader(50,25)
all_sprites_list.add(invader3)
invader_list.add(invader3)
invader4 = Invader(50,25)
all_sprites_list.add(invader4)
invader_list.add(invader4)

turret1 = Turret(400,445,50,35)
all_sprites_list.add(turret1)
groundunit_list.add(turret1)


mine1 = Mine(300,200,20)
all_sprites_list.add(mine1)

player1 = Player(20,250,20,20,0,0)
all_sprites_list.add(player1)
player_list.add(player1)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.speedx = -3
            elif event.key == pygame.K_RIGHT:
                player1.speedx = 3
            elif event.key == pygame.K_UP:
                player1.speedy = -3
            elif event.key == pygame.K_DOWN:
                player1.speedy = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1.speedx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1.speedy = 0
                

    player1.rect.x += player1.speedx
    player1.rect.y += player1.speedy
    
            
 
    # --- Game logic should go here

    # Collisions hit list
    blocks_hit_list = pygame.sprite.groupcollide(player_list, invader_list, True, False)
   # blocks_hit_list = pygame.sprite.spritecollide(player1, terrain_list, True)
    blocks_hit_list = pygame.sprite.groupcollide(player_list, terrain_easy_list, True, False)
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(LIGHTBLUE)


    all_sprites_list.draw(screen)

    for item in invader_list:
        item.move()

    for item in terrain_easy_list:
        item.move()

    for item in groundunit_list:
        item.move()


    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
