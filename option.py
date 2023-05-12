"""
import pygame
from interface_option import *

pygame.display.set_caption("Options")

with open("options.txt") as fichier :
    table = fichier.readlines()


def option () :
    
    running = True
    
    while running :

        actualisation_fenetre()

        for event in pygame.event.get() :
        # Quitter le jeu
            if event.type == pygame.QUIT : 
                running = False
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if bouton_menu_rect.collidepoint(event.pos) :
                    running = False
            
                elif bouton_taille_ecran_751_rect.collidepoint(event.pos) :
                    with open("options.txt", 'w') as fichier :
                        fichier.write(str(0)+"\n")
                elif bouton_taille_ecran_849_rect.collidepoint(event.pos) :
                    with open("options.txt", 'w') as fichier :
                        fichier.write(str(1)+"\n")

        
        


"""