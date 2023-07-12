# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    pygame.draw.line(screen,[0,0,0],(240,0),(240,720),10)
    pygame.draw.line(screen,[0,0,0],(480,0),(480,720),10)
    pygame.draw.line(screen,[0,0,0],(0,240),(720,240),10)
    pygame.draw.line(screen,[0,0,0],(0,480),(720,480),10)
    
    keys = pygame.key.get_pressed()

    chacha=keys[pygame.K_3]
    quanquan=keys[pygame.K_4]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame:
            
            if chacha==True:
                pygame.draw.line(screen,[0,0,0],(113,60),(313,180),80)
                pygame.draw.line(screen,[0,0,0],(313,60),(113,180),80)
            if quanquan==True:
                pygame.draw.circle(screen,[20,80,10],(640,120),60,1)

    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
