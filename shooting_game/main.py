import pygame

pygame.init() # Game start 

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Wind's World Game")

walkRight = [pygame.image.load('source/R1.png'), pygame.image.load('source/R2.png'), pygame.image.load('source/R3.png'),
pygame.image.load('source/R4.png'), pygame.image.load('source/R5.png'), pygame.image.load('source/R6.png'),
pygame.image.load('source/R7.png'), pygame.image.load('source/R8.png'), pygame.image.load('source/R9.png')]

walkLeft= [pygame.image.load('source/L1.png'), pygame.image.load('source/L2.png'), pygame.image.load('source/L3.png'),
pygame.image.load('source/L4.png'), pygame.image.load('source/L5.png'), pygame.image.load('source/L6.png'),
pygame.image.load('source/L7.png'), pygame.image.load('source/L8.png'), pygame.image.load('source/L9.png')]

bg = pygame.image.load('source/bg.jpg')
char = pygame.image.load('source/standing.png')

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def move(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        
        else:
            win.blit(char, (self.x,self.y))



def redrawGameWindow():
    win.blit(bg, (0,0))
    haejeok.move(win)
    pygame.display.update()

haejeok = Player(200, 410, 64, 64)
run = True 
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and haejeok.x > haejeok.velocity:
        haejeok.x -= haejeok.velocity
        haejeok.left = True
        haejeok.right = False
    
    elif keys[pygame.K_RIGHT] and haejeok.x < 500 - haejeok.velocity - haejeok.width:
        haejeok.x += haejeok.velocity
        haejeok.left = False 
        haejeok.right = True
    
    else:
        haejeok.right = False
        haejeok.left = False
        haejeok.walkCount = 0

    if not(haejeok.isJump):
        # if keys[pygame.K_UP] and y > velocity:
        #     y -= velocity
        
        # if keys[pygame.K_DOWN] and y < 500 - velocity - height:
        #     y += velocity
        if keys[pygame.K_SPACE]:
            haejeok.isJump = True
            haejeok.right = False 
            haejeok.left = False 
            haejeok.walkCount = 0
    
    else:
        if haejeok.jumpCount >= -10:
            neg = 1
            if haejeok.jumpCount < 0:
                neg = -1
            haejeok.y -= (haejeok.jumpCount ** 2) * 0.5 * neg
            haejeok.jumpCount -= 1
        else:
            haejeok.isJump = False
            haejeok.jumpCount = 10
            
    
    redrawGameWindow()

pygame.quit()