import pygame
from game import play_game
from interface_main_menu import *

pygame.init()


running = True
while running :

    actualisation_fenetre()

    for event in pygame.event.get() :
        # Quitter le jeu
        if event.type == pygame.QUIT : 
            running = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            if bouton_play_rect.collidepoint(event.pos) :
                nbJoueurs = 4
                play_game(nbJoueurs)
            
            elif bouton_continue_game_rect.collidepoint(event.pos):
                nbJoueurs = 4
                play_game(nbJoueurs, charger=True)

            elif bouton_exit_rect.collidepoint(event.pos) :
                running = False
                pygame.quit()