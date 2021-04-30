import pygame
import sys
class Game(object):

    # initialization the all constructs the game...
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.max_tps = 75.0
        self.screen = pygame.display.set_mode((1440,900)) # 1440×900 (16:10)
        self.clock = pygame.time.Clock()
        self.delta_tps = 0.0

        while self.delta > 1 / self.max_tps:
              self.delta -= 1 / self.max_tps

        while True: 
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            # ticking...

            # drawing...
            self.background = pygame.image.load("./Programmer Backgrounds 15.jpg").convert()
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()

 
    # ticking the tps and other...
    def tick(self):

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

    # drawing elements on the screen..
    def drawing(self):
        pygame.draw.rect(self.screen,(13,255,0),self.box)

if __name__ == "__main__":
    Game()