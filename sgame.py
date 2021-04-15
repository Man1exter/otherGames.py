import pygame
import sys

def seek():
    print(pygame.__version__)
    screen = pygame.display.set_mode((1280,720))

    # player = pygame.image.load("./Programmer Backgrounds 15.jpg")

    player_width = 50
    player_height = 50
    box = pygame.Rect(10,50,player_width,player_height)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        pygame.draw.rect(screen,(13,255,0),pygame.Rect(10,50,player_width,player_height))
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
          box.x += 1
        if keys[pygame.K_d]:
          box.y += 1
        if keys[pygame.K_d]:
          box.y -= 1
        if keys[pygame.K_d]:
          box.x -= 1