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
"""
police_48 = pygame.font.Font(None,48)
police_32 = pygame.font.Font(None,32)
police_20 = pygame.font.Font(None,20)

# Taille écran
with open("options.txt", 'r') as fichier :
    chargement = fichier.readlines()
    format_ecran = int(chargement[0])
if format_ecran == 0 :
    screen_size = (1080,751)
else :
    screen_size = (1080,849)

screen = pygame.display.set_mode(screen_size)


if format_ecran == 0 :
    taille_ecran_text_coordonnees = (100,65)
    taille_ecran_text = police_32.render("Taille de l'écran :",True,(0,0,0))
    taille_ecran_text_rect = taille_ecran_text.get_rect()
    taille_ecran_text_rect.center = taille_ecran_text_coordonnees

    bouton_taille_ecran_849_coordonnees = (250,40)
    bouton_taille_ecran_849_width = 150
    bouton_taille_ecran_849_heigth = 50
    if format_ecran == 0 :
        bouton_taille_ecran_849_color = (160,100,90)
    else :
        bouton_taille_ecran_849_color = (110,145,110)
    bouton_taille_ecran_849_rect = pygame.Rect(bouton_taille_ecran_849_coordonnees[0],bouton_taille_ecran_849_coordonnees[1],bouton_taille_ecran_849_width,bouton_taille_ecran_849_heigth)
    bouton_taille_ecran_849_text = police_32.render("849x1080",True,(0,0,0))
    bouton_taille_ecran_849_text_rect = bouton_taille_ecran_849_text.get_rect(center=bouton_taille_ecran_849_rect.center)


    bouton_taille_ecran_751_coordonnees = (450,40)
    bouton_taille_ecran_751_width = 150
    bouton_taille_ecran_751_heigth = 50
    bouton_taille_ecran_751_rect = pygame.Rect(bouton_taille_ecran_751_coordonnees[0],bouton_taille_ecran_751_coordonnees[1],bouton_taille_ecran_751_width,bouton_taille_ecran_751_heigth)
    bouton_taille_ecran_751_text = police_32.render("751x1080",True,(0,0,0))
    bouton_taille_ecran_751_text_rect = bouton_taille_ecran_751_text.get_rect(center=bouton_taille_ecran_751_rect.center)



    bouton_menu_coordonnees = (850,40)
    bouton_menu_width = 200
    bouton_menu_heigth = 50
    bouton_menu_color = (150,150,150)
    bouton_menu_rect = pygame.Rect(bouton_menu_coordonnees[0],bouton_menu_coordonnees[1],bouton_menu_width,bouton_menu_heigth)
    bouton_menu_text = police_32.render("Menu",True,(0,0,0))
    bouton_menu_text_rect = bouton_menu_text.get_rect(center=bouton_menu_rect.center)


def actualisation_fenetre () :

    pygame.display.flip()

    screen.fill((255,255,255))

    # Couleurs des boutons
    if format_ecran == 0 :
        bouton_taille_ecran_751_color = (110,145,110)
    else :
        bouton_taille_ecran_751_color = (160,100,90)

    screen.blit(taille_ecran_text,taille_ecran_text_rect)

    pygame.draw.rect(screen,bouton_taille_ecran_849_color,bouton_taille_ecran_849_rect,0)
    screen.blit(bouton_taille_ecran_849_text,bouton_taille_ecran_849_text_rect)

    pygame.draw.rect(screen,bouton_taille_ecran_751_color,bouton_taille_ecran_751_rect,0)
    screen.blit(bouton_taille_ecran_751_text,bouton_taille_ecran_751_text_rect)

    pygame.draw.rect(screen,bouton_menu_color,bouton_menu_rect)
    screen.blit(bouton_menu_text,bouton_menu_text_rect)
"""
