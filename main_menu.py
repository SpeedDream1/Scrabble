import pygame
from game import play_game
from interface_main_menu import *

pygame.init()


running = True
while running :

    try:
        with open("sauvegarde.txt", mode='r') as fichier:
            texte = fichier.read()
            if  texte == "None":
                is_save = False
            else:
                is_save = True
    except FileNotFoundError:
        is_save = False

    actualisation_fenetre(is_save)

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