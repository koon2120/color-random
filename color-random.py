#name : Color Random , version : 1.0

import pygame,random,pyperclip

pygame.init()
pygame.font.init()
screen_size = (500,500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Color Random | version 1.0 | by koon2120")
fg = pygame.surface.Surface((50,50))
fg_color = (255,255,255)
bg_color = (0,0,0)
font = pygame.font.Font(None,32)
running  = True
show_copying = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] or pygame.key.get_pressed()[pygame.K_q]:
            running = False
        if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_RETURN]:
            fg_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
            bg_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
            show_copying = True
            pyperclip.copy("fg : " + str(fg_color) + " bg : " + str(bg_color))
        if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_f]:
            show_copying = True
            pyperclip.copy(str(fg_color))
        if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_b]:
            show_copying = True
            pyperclip.copy(str(bg_color))
    screen.fill(bg_color)
    fg.fill(fg_color)
    screen.blit(fg,fg.get_rect(center=(screen_size[0]/2,screen_size[1]/2)))
    screen.blit(font.render("fg : " + str(fg_color) + " bg : " + str(bg_color),True,fg_color),(20,20))
    if show_copying:
        screen.blit(font.render("COPYING...",True,fg_color),(370,470))
        show_copying = False
    pygame.display.flip()
    clock.tick(25)