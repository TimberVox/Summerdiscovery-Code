import pygame

key_A=97
key_D=100
key_W=119
ground=450
mario_pos=[0,ground]
mario_size=[360,251]
mario_vel=[0,0]

mario_image = pygame.image.load("/Users/TINTIN/Desktop/oc们/狮鹫2.png")
mario_image = pygame.transform.scale(mario_image,mario_size)
mario_image = pygame.transform.flip(mario_image,True,False)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


dt=0

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key == key_A:
                mario_vel[0] = -600
                mario_image = pygame.transform.flip(mario_image,True,False)
            if event.key == key_D:
                mario_vel[0] = 600 
            if event.key == key_W:
                mario_vel[1] = -500
        if event.type == pygame.KEYUP:
            if event.key == key_A:
                mario_vel[0] = 0
                mario_image = pygame.transform.flip(mario_image,True,False)
            if event.key == key_D:
                mario_vel[0] = 0
            if event.key ==key_W:
                mario_vel[1] = 0
    
    mario_vel[1] +=1000*dt

    if mario_pos[1]>ground:
        mario_pos[1]=ground
        mario_vel[1]=0

    mario_pos[0] += mario_vel[0]*dt
    mario_pos[1] += mario_vel[1]*dt

    screen.fill([110,220,250])
    screen.blit(mario_image,mario_pos)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()