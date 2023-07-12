import pygame
running=True
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            print(event.key)
    
    screen.fill([110,220,250])

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()