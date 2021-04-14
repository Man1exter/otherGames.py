import pygame
import sys

screen = pygame.display.set_mode((1280,720))

def seek():
    print(pygame.__version__)
    while True: 
        for event in pygame.event.get():
            if event.type ++ pygame.QUIT:
                sys.exit(0)