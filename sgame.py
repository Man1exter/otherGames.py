import pygame
import sys

def seek():
    print(pygame.__version__)
    screen = pygame.display.set_mode((1280,720))
    box = pygame.Rect(10,10,50,50)

    background = pygame.image.load("./Programmer Backgrounds 15.jpg").convert()

    player_width = 50
    player_height = 50

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        #moving..
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
          box.x += 1
        if keys[pygame.K_s]:
          box.y += 1
        if keys[pygame.K_w]:
          box.y -= 1
        if keys[pygame.K_a]:
          box.x -= 1

        #drawing...
        screen.blit(background, [0, 0])
        #screen.fill((0,0,0))
        pygame.draw.rect(screen,(13,255,0),pygame.Rect(10,50,player_width,player_height))
        pygame.display.flip()

def keyboard():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pass # d += 1
    if keys[pygame.K_d]:
        pass # s += y
    if keys[pygame.K_d]:
        pass # w -= y
    if keys[pygame.K_d]:
        pass # a -= x