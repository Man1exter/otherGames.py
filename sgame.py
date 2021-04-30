import pygame
import sys

def seek():
  
    pygame.init()
    pygame.font.init()

    print(pygame.__version__)
    screen = pygame.display.set_mode((1440,900)) # 1440×900 (16:10)

    max_tps = 70.0
    clock = pygame.time.Clock()
    delta = 0.0

    background = pygame.image.load("./Programmer Backgrounds 15.jpg").convert()
    player_img = pygame.image.load('./rulon223223.png').convert()

    # IMAGE = pg.image.load('an_image.png').convert()  # or .convert_alpha()
    # Create a rect with the size of the image.
    # rect = IMAGE.get_rect()
    # rect.center = (200, 300)
    #screen.blit(IMAGE, rect)
    
    player_width = 70
    player_height = 70
    score = 0 # to sum points in all time the game life..
    box = pygame.Rect(10,10,player_width,player_height)


    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # ..time section TPS..
        delta = clock.tick()
        while delta > 1 / max_tps:
              delta -= 1 / max_tps

        # ..moving WASD from keyboard..
        
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
        # ...need to push into a background z-index : 1....  #font_to_score = pygame.font.SysFont('helvetica', 55)
        #font_easy = font_to_score.render("HEY RULONIKOS",
                                #True, (248, 252, 3))

        #drawing...
        #screen.blit(font_easy, (50, 50))

        # rulonik image
        rect_player = player_img.get_rect()
        rect_player.center = (50, 50) # position
        screen.blit(player_img, rect_player)

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen,(13,255,0),box)
        pygame.display.flip()


if __name__ =="__main__":
  seek()