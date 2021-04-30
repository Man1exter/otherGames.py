import pygame
import sys
class Game(object):

    # initialization the all constructs the game...
    def __init__(self):
        pygame.init()
        pygame.font.init()

        while True: 
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
 
    # ticking the tps and other...
    def tick(self):
        max_tps = 70.0
        clock = pygame.time.Clock()
        delta = 0.0

        delta = clock.tick()
        while delta > 1 / max_tps:
              delta -= 1 / max_tps

    # drawing elements on the screen..
    def drawing(self):
        screen = pygame.display.set_mode((1440,900)) # 1440×900 (16:10)
        background = pygame.image.load("./Programmer Backgrounds 15.jpg").convert()

        player_width = 70
        player_height = 70
        box = pygame.Rect(10,10,player_width,player_height)

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen,(13,255,0),box)
        pygame.display.flip()


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