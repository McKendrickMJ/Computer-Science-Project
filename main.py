import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
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
invader_list = pygame.sprite.Group()
class Invader(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.color = RED
        self.x = x
        self.y = y
        self.image = pygame.Surface([width,height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
    def move(self):
        self.x = self.x + 1

    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),0)

   # def draw(self):
    #    pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),0)

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,speedx,speedy):
        super().__init__()
        self.width = width
        self.height = height
        self.color = BLACK
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),0)

class Turret(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.color = GREEN
        self.x = x
        self.y = y
        self.image = pygame.Surface([width,height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),0)

class Mine(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        super().__init__()
        self.size = size
        self.color = GREEN
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),0)



invader1 = Invader(100,100,50,25)
all_sprites_list.add(invader1)
invader_list.add(invader1)
invader2 = Invader(200,150,50,25)
all_sprites_list.add(invader2)
invader_list.add(invader2)
invader3 = Invader(300,200,50,25)
all_sprites_list.add(invader3)
invader_list.add(invader3)
invader4 = Invader(400,400,50,25)
all_sprites_list.add(invader4)
invader_list.add(invader4)

turret1 = Turret(300,200,100,50)
all_sprites_list.add(turret1)

player1 = Player(20,20,20,20,0,0)
all_sprites_list.add(player1)

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
                

    player1.x += player1.speedx
    player1.y += player1.speedy
    
            
 
    # --- Game logic should go here

    # Collisions hit list
    blocks_hit_list = pygame.sprite.spritecollide(player1, invader_list, True)
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

##    invader1.draw()
##    invader2.draw()
##    invader3.draw()
##    invader4.draw()
##    
##    invader1.move()
##    invader2.move()
##    invader3.move()
##    invader4.move()
    #for item in block_list:
     #   item.draw()
      #  item.move()

   # player1.draw()

  #  turret1.draw()

  #  all_sprites_list.draw(screen)
    for item in all_sprites_list:
        item.draw()

    for item in invader_list:
        item.move()

    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
