import pygame

# Lancement de l'interface
pygame.init()
pygame.display.set_caption("Menu")

# Police de texte
police_28 = pygame.font.Font(None,28)
police_32 = pygame.font.Font(None,32)
police_48 = pygame.font.Font(None,48)
police_38 = pygame.font.Font(None,38)

# Taille écran
# Taille écran
with open("options.txt", 'r') as fichier :
    chargement = fichier.readlines()
    format_ecran = int(chargement[0])
if format_ecran == 0 :
    screen_size = (1080,751)
else :
    screen_size = (1080,849)

screen = pygame.display.set_mode(screen_size)
is_save = False

# Coordonnées des éléments graphiques
if format_ecran == 0 :
    bouton_play_coordonnees = (290,115)
    bouton_play_width = 500
    bouton_play_heigth = 100
    bouton_play_color = (0,130,30)
    bouton_play_rect = pygame.Rect(bouton_play_coordonnees[0],bouton_play_coordonnees[1],bouton_play_width,bouton_play_heigth)
    bouton_play_text = police_48.render("Nouvelle Partie",True,(255,255,255))
    bouton_play_text_rect = bouton_play_text.get_rect(center=bouton_play_rect.center)

    bouton_continue_game_coordonnees = (290,325)
    bouton_continue_game_width = 500
    bouton_continue_game_heigth = 100
    bouton_continue_game_color = (0,80,20)
    bouton_continue_game_rect = pygame.Rect(bouton_continue_game_coordonnees[0],bouton_continue_game_coordonnees[1],bouton_continue_game_width,bouton_continue_game_heigth)
    bouton_continue_game_text = police_48.render("Reprendre la Partie",True,(255,255,255))
    bouton_continue_game_text_rect = bouton_continue_game_text.get_rect(center=bouton_continue_game_rect.center)

    """
    bouton_option_coordonnees = (290,410)
    bouton_option_width = 500
    bouton_option_heigth = 100
    bouton_option_color = (80,80,80)
    bouton_option_rect = pygame.Rect(bouton_option_coordonnees[0],bouton_option_coordonnees[1],bouton_option_width,bouton_continue_game_heigth)
    bouton_option_text = police_48.render("Options",True,(255,255,255))
    bouton_option_text_rect = bouton_option_text.get_rect(center=bouton_option_rect.center)
    """
    bouton_exit_coordonnees = (290,535)
    bouton_exit_width = 500
    bouton_exit_heigth = 100
    bouton_exit_color = (175,0,0)
    bouton_exit_rect = pygame.Rect(bouton_exit_coordonnees[0],bouton_exit_coordonnees[1],bouton_exit_width,bouton_exit_heigth)
    bouton_exit_text = police_48.render("Quitter",True,(255,255,255))
    bouton_exit_text_rect = bouton_exit_text.get_rect(center=bouton_exit_rect.center)

else :
    
    bouton_play_coordonnees = (290,140)
    bouton_play_width = 500
    bouton_play_heigth = 100
    bouton_play_color = (0,130,30)
    bouton_play_rect = pygame.Rect(bouton_play_coordonnees[0],bouton_play_coordonnees[1],bouton_play_width,bouton_play_heigth)
    bouton_play_text = police_48.render("Nouvelle Partie",True,(255,255,255))
    bouton_play_text_rect = bouton_play_text.get_rect(center=bouton_play_rect.center)

    bouton_continue_game_coordonnees = (290,375)
    bouton_continue_game_width = 500
    bouton_continue_game_heigth = 100
    bouton_continue_game_color = (0,80,20)
    bouton_continue_game_rect = pygame.Rect(bouton_continue_game_coordonnees[0],bouton_continue_game_coordonnees[1],bouton_continue_game_width,bouton_continue_game_heigth)
    bouton_continue_game_text = police_48.render("Reprendre la Partie",True,(255,255,255))
    bouton_continue_game_text_rect = bouton_continue_game_text.get_rect(center=bouton_continue_game_rect.center)
    """
    bouton_option_coordonnees = (290,470)
    bouton_option_width = 500
    bouton_option_heigth = 100
    bouton_option_color = (80,80,80)
    bouton_option_rect = pygame.Rect(bouton_option_coordonnees[0],bouton_option_coordonnees[1],bouton_option_width,bouton_continue_game_heigth)
    bouton_option_text = police_48.render("Options",True,(255,255,255))
    bouton_option_text_rect = bouton_option_text.get_rect(center=bouton_option_rect.center)
    """
    bouton_exit_coordonnees = (290,610)
    bouton_exit_width = 500
    bouton_exit_heigth = 100
    bouton_exit_color = (175,0,0)
    bouton_exit_rect = pygame.Rect(bouton_exit_coordonnees[0],bouton_exit_coordonnees[1],bouton_exit_width,bouton_exit_heigth)
    bouton_exit_text = police_48.render("Quitter",True,(255,255,255))
    bouton_exit_text_rect = bouton_exit_text.get_rect(center=bouton_exit_rect.center)

def set_bouton_continue():
    global bouton_continue_game_color
    global bouton_continue_game_text
    global bouton_continue_game_text_rect

    try:
        with open("sauvegarde.txt", mode='r') as fichier:
            texte = fichier.read()
            if  texte == "None":
                is_save = False
            else:
                is_save = True
    except FileNotFoundError:
        is_save = False

    if is_save:
        bouton_continue_game_color = (0,80,20)
        bouton_continue_game_text = police_48.render("Reprendre la Partie",True,(255,255,255))
        bouton_continue_game_text_rect = bouton_continue_game_text.get_rect(center=bouton_continue_game_rect.center)
    else:
        bouton_continue_game_color = (110,140,120)
        bouton_continue_game_text = police_48.render("Pas de partie sauvegardée",True,(255,255,255))
        bouton_continue_game_text_rect = bouton_continue_game_text.get_rect(center=bouton_continue_game_rect.center)
    
    return is_save

def actualisation_fenetre():
    pygame.display.flip()

    screen.fill((255,255,255))
    pygame.draw.rect(screen,bouton_play_color,bouton_play_rect,0)
    screen.blit(bouton_play_text,bouton_play_text_rect)

    pygame.draw.rect(screen,bouton_continue_game_color,bouton_continue_game_rect,0)
    screen.blit(bouton_continue_game_text,bouton_continue_game_text_rect)
    """
    pygame.draw.rect(screen,bouton_option_color,bouton_option_rect,0)
    screen.blit(bouton_option_text,bouton_option_text_rect)
    """
    pygame.draw.rect(screen,bouton_exit_color,bouton_exit_rect,0)
    screen.blit(bouton_exit_text,bouton_exit_text_rect)