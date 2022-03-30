import pygame

pygame.init() # Game start 

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Python Movement Practice")

x = 50
y = 50
width = 40
height = 60
velocity = 15

isJump = False
jumpCount = 10

run = True 
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    
    if keys[pygame.K_RIGHT] and x < 500 - velocity - width:
        x += velocity
    
    if not(isJump):
        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        
        if keys[pygame.K_DOWN] and y < 500 - velocity - height:
            y += velocity

        if keys[pygame.K_SPACE]:
            isJump = True
    
    else:
        if jumpCount >= -10:
            y = y - (jumpCount * abs(jumpCount)) * 0.1
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    
    win.fill((0,0,0)) # (R,G,B) -> black
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update() # Reload

pygame.quit()