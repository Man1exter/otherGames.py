import pygame
import sys

def seek():
    print(pygame.__version__)
    screen = pygame.display.set_mode((1280,720))

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        pygame.draw.rect(screen,(0,150,200),pygame.Rect(10,50,150,200))
        pygame.display.flip()