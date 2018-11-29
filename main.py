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

block_list = pygame.sprite.Group()
class Invader(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.width = 100
        self.height = 50
        self.color = RED
        self.x = x
        self.y = y
        
    def move(self):
        self.x = self.x + 1

    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),0)

invader1 = Invader(100,100)
block_list.add(invader1)
invader2 = Invader(200,150)
block_list.add(invader2)
invader3 = Invader(300,200)
block_list.add(invader3)
invader4 = Invader(400,400)
block_list.add(invader4)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
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
    for item in block_list:
        item.draw()
        item.move()
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
