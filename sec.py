import pygame
import sys
class Game(object):

    # initialization the all constructs the game...
    def __init__(self):
        pass
 
    # ticking the tps and other...
    def tick(self):
        pass

    # drawing elements on the screen..
    def drawing(self):
        pass


class Player(object):

    # initialization the all constructs the game...
    def __init__(self):
        pass
 
    # ticking the tps and other...
    def tick(self):
        pass

    # drawing elements on the screen..
    def drawing(self):

        # ..moving WASD from keyboard..

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
          self.x += 1
        if keys[pygame.K_s]:
          self.y += 1
        if keys[pygame.K_w]:
          self.y -= 1
        if keys[pygame.K_a]:
          self.x -= 1

        # ..moving ARROWS from keyboard..

        if keys[pygame.K_RIGHT]:
          self.x += 1
        if keys[pygame.K_DOWN]:
          self.y += 1
        if keys[pygame.K_UP]:
          self.y -= 1
        if keys[pygame.K_LEFT]:
          self.x -= 1


class Beer(object):
    
    # initialization the all constructs the game...
    def __init__(self):
        pass
 
    # ticking the tps and other...
    def tick(self):
        pass

    # drawing elements on the screen..
    def drawing(self):
        pass


if __name__ == "__main__":
    Game()