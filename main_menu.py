import pygame
from game import play_game
from interface_main_menu import *
from nouvelle_partie import new_game

pygame.init()
is_save = set_bouton_continue()

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
                nbJoueurs = new_game()
                play_game(nbJoueurs)
                is_save = set_bouton_continue()
                

            elif bouton_continue_game_rect.collidepoint(event.pos):
                nbJoueurs = 4
                if is_save:
                    play_game(nbJoueurs, charger=True)
                    is_save = set_bouton_continue()

            elif bouton_exit_rect.collidepoint(event.pos) :
                running = False
                pygame.quit()