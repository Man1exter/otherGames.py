import pygame
import sys

def seek():
    print(pygame.__version__)
    screen = pygame.display.set_mode((1280,720))

    # player = pygame.image.load("./Programmer Backgrounds 15.jpg")

    player_width = 50
    player_height = 50
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        pygame.draw.rect(screen,(13,255,0),pygame.Rect(10,50,player_width,player_height))
        pygame.display.flip()