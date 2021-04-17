import pygame
import sys

def seek():
    pygame.init()
    print(pygame.__version__)
    screen = pygame.display.set_mode((1440,900)) # 1440×900 (16:10)

    background = pygame.image.load("./Programmer Backgrounds 15.jpg").convert()
    
    player_width = 70
    player_height = 70
    score = 0
    box = pygame.Rect(10,10,player_width,player_height)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # ..moving WASD..
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
          box.x += 1
        if keys[pygame.K_s]:
          box.y += 1
        if keys[pygame.K_w]:
          box.y -= 1
        if keys[pygame.K_a]:
          box.x -= 1

        # ..moving ARROWS from keyboard..

        if keys[pygame.K_RIGHT]:
          box.x += 1
        if keys[pygame.K_DOWN]:
          box.y += 1
        if keys[pygame.K_UP]:
          box.y -= 1
        if keys[pygame.K_LEFT]:
          box.x -= 1

        #ticking..
        scoreOfBeer = pygame.font.Font.render(pygame.font.SysFont("Noto Sans",52,f"WYPIŁEŚ {score} RULONDÓW",False,(252, 252, 3)))

        #drawing...
        screen.blit(scoreOfBeer,[0, 0])
        screen.blit(background, [0, 0])
        pygame.draw.rect(screen,(13,255,0),box)
        pygame.display.flip()


