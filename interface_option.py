import pygame

def init_option () :
    # Définition de la fenetre du jeu
    if  pygame.display.Info().current_h < 933 : # Taille barre des taches = 84
        screen_size = (1080, 751)
        format_ecran = 0
    else :
        screen_size = (1080, 849)
        format_ecran = 1
    with open("options.txt", 'w') as fichier :
            fichier.write(str(format_ecran)+"\n")



def save_option (format_ecran) :
    with open("options.txt", 'w') as fichier :
        fichier.write(str(format_ecran)+"\n")