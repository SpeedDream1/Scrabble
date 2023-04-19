import pygame
from main_play import play


pygame.init()

from main_menu_interface import *

running = True
while running :

    pygame.display.flip()

    screen.fill((255,255,255))
    pygame.draw.rect(screen,bouton_play_color,bouton_play_rect,0)
    screen.blit(bouton_play_text,bouton_play_text_rect)

    pygame.draw.rect(screen,bouton_continue_game_color,bouton_continue_game_rect,0)
    screen.blit(bouton_continue_game_text,bouton_continue_game_text_rect)

    pygame.draw.rect(screen,bouton_option_color,bouton_option_rect,0)
    screen.blit(bouton_option_text,bouton_option_text_rect)

    pygame.draw.rect(screen,bouton_exit_color,bouton_exit_rect,0)
    screen.blit(bouton_exit_text,bouton_exit_text_rect)
    

    for event in pygame.event.get() :
        # Quitter le jeu
        if event.type == pygame.QUIT : 
            running = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            if bouton_play_rect.collidepoint(event.pos) :
                play()

            elif bouton_exit_rect.collidepoint(event.pos) :
                running = False
                pygame.quit()