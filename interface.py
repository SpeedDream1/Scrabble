import pygame

# Lancement de l'interface
pygame.init()
pygame.display.set_caption("Scrabble")

# Définition de la fenetre du jeu
if  pygame.display.Info().current_h < 933 : # Taille barre des taches = 84
    screen_size = (1080, 751)
    format_ecran = 0
else :
    screen_size = (1080, 849)
    format_ecran = 1
screen = pygame.display.set_mode(screen_size)

# Définition du plateau
img_plateau = pygame.image.load("assets\plato_scrabble.jpg").convert() # Taille Case 48x48
fond = pygame.Surface(screen.get_size())

# Coordonnées des éléments graphiques
if format_ecran == 0 :
    coord_plateau = (98,0)
    coord_chevalet = (20,0)
    chevalet_rect = pygame.Rect(coord_chevalet[0] ,coord_chevalet[1], 58, 751) # chevalet
    bouton_valider_rect = pygame.Rect(915,701,100,40)
else :
    coord_plateau = (0,0)
    coord_chevalet = (0,771)
    chevalet_rect = pygame.Rect(coord_chevalet[0] ,coord_chevalet[1] ,752,58) # chevalet
    bouton_valider_rect = pygame.Rect(915,701,100,40)

# Création liste des coordonnées de toute les cases
coord_case_plateau = [[(coord_plateau[0]+1+50*i , coord_plateau[1]+1+50*j) for j in range(15)] for i in range(15)] # plateau
coord_case_chevalet = [((coord_chevalet[0]+5 , coord_chevalet[1]+52+100*i) if format_ecran == 0 else
                                (coord_chevalet[0]+52+100*i, coord_chevalet[1]+5)) for i in range(7)] # chevalet

    
# Parametres
bouton_parametres = pygame.Rect(1050,5,25,25)
parametres = False
image_bouton_parametres = pygame.image.load("assets//image_parametres.png")