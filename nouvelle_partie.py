import pygame
from nouvelle_partie_interface import *


def new_game() :
    running = True
    while running :
        actualisation_fenetre()

        for event in pygame.event.get() :
            # Quitter le jeu
            if event.type == pygame.QUIT : 
                running = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if bouton_2_joueurs_rect.collidepoint(event.pos) :
                    return 2
                elif bouton_3_joueurs_rect.collidepoint(event.pos) :
                    return 3
                elif bouton_4_joueurs_rect.collidepoint(event.pos) :
                    return 4