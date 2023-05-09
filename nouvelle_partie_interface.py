import pygame
pygame.init()
pygame.display.set_caption("Nouvelle Partie")


police_48 = pygame.font.Font(None,48)
police_38 = pygame.font.Font(None,38)
police_20 = pygame.font.Font(None,20)

# Taille écran
with open("options.txt", 'r') as fichier :
    chargement = fichier.readlines()
    format_ecran = int(chargement[0])
if format_ecran == '0' :
    screen_size = (1080,751)
else :
    screen_size = (1080,849)

screen = pygame.display.set_mode(screen_size)
is_save = False

if format_ecran == 0 :

    avertissement_text_coordonnees = (1080,50)
    avertissement_text = police_20.render("En créant une nouvelle partie, vous supprimez l'ancienne !",True,(0,0,0))
    avertissement_text_rect = avertissement_text.get_rect()
    avertissement_text_rect.center = (avertissement_text_coordonnees[0]//2,avertissement_text_coordonnees[1])

    nbr_joueur_text_coordonnees = (1080,200)
    nbr_joueur_text = police_48.render("Nombre de Joueurs :",True,(0,0,0))
    nbr_joueur_text_rect = nbr_joueur_text.get_rect()
    nbr_joueur_text_rect.center = (nbr_joueur_text_coordonnees[0]//2,nbr_joueur_text_coordonnees[1]//2)

    bouton_2_joueurs_coordonnees = (270,200)
    bouton_2_joueurs_width = 540
    bouton_2_joueurs_heigth = 75
    bouton_2_joueurs_color = (150,150,150)
    bouton_2_joueurs_rect = pygame.Rect(bouton_2_joueurs_coordonnees[0],bouton_2_joueurs_coordonnees[1],bouton_2_joueurs_width,bouton_2_joueurs_heigth)
    bouton_2_joueurs_text = police_38.render("2 joueurs",True,(0,0,0))
    bouton_2_joueurs_text_rect = bouton_2_joueurs_text.get_rect(center=bouton_2_joueurs_rect.center)

    bouton_3_joueurs_coordonnees = (270,325)
    bouton_3_joueurs_width = 540
    bouton_3_joueurs_heigth = 75
    bouton_3_joueurs_color = (150,150,150)
    bouton_3_joueurs_rect = pygame.Rect(bouton_3_joueurs_coordonnees[0],bouton_3_joueurs_coordonnees[1],bouton_3_joueurs_width,bouton_3_joueurs_heigth)
    bouton_3_joueurs_text = police_38.render("3 joueurs",True,(0,0,0))
    bouton_3_joueurs_text_rect = bouton_3_joueurs_text.get_rect(center=bouton_3_joueurs_rect.center)

    bouton_4_joueurs_coordonnees = (270,450)
    bouton_4_joueurs_width = 540
    bouton_4_joueurs_heigth = 75
    bouton_4_joueurs_color = (150,150,150)
    bouton_4_joueurs_rect = pygame.Rect(bouton_4_joueurs_coordonnees[0],bouton_4_joueurs_coordonnees[1],bouton_4_joueurs_width,bouton_4_joueurs_heigth)
    bouton_4_joueurs_text = police_38.render("4 joueurs",True,(0,0,0))
    bouton_4_joueurs_text_rect = bouton_4_joueurs_text.get_rect(center=bouton_4_joueurs_rect.center)

if format_ecran == 1 :

    avertissement_text_coordonnees = (1080,50)
    avertissement_text = police_20.render("En créant une nouvelle partie, vous supprimez l'ancienne !",True,(0,0,0))
    avertissement_text_rect = avertissement_text.get_rect()
    avertissement_text_rect.center = (avertissement_text_coordonnees[0]//2,avertissement_text_coordonnees[1])

    nbr_joueur_text_coordonnees = (1080,200)
    nbr_joueur_text = police_48.render("Nombre de Joueurs :",True,(0,0,0))
    nbr_joueur_text_rect = nbr_joueur_text.get_rect()
    nbr_joueur_text_rect.center = (nbr_joueur_text_coordonnees[0]//2,nbr_joueur_text_coordonnees[1]//2)

    bouton_2_joueurs_coordonnees = (270,200)
    bouton_2_joueurs_width = 540
    bouton_2_joueurs_heigth = 75
    bouton_2_joueurs_color = (150,150,150)
    bouton_2_joueurs_rect = pygame.Rect(bouton_2_joueurs_coordonnees[0],bouton_2_joueurs_coordonnees[1],bouton_2_joueurs_width,bouton_2_joueurs_heigth)
    bouton_2_joueurs_text = police_38.render("2 joueurs",True,(0,0,0))
    bouton_2_joueurs_text_rect = bouton_2_joueurs_text.get_rect(center=bouton_2_joueurs_rect.center)

    bouton_3_joueurs_coordonnees = (270,325)
    bouton_3_joueurs_width = 540
    bouton_3_joueurs_heigth = 75
    bouton_3_joueurs_color = (150,150,150)
    bouton_3_joueurs_rect = pygame.Rect(bouton_3_joueurs_coordonnees[0],bouton_3_joueurs_coordonnees[1],bouton_3_joueurs_width,bouton_3_joueurs_heigth)
    bouton_3_joueurs_text = police_38.render("3 joueurs",True,(0,0,0))
    bouton_3_joueurs_text_rect = bouton_3_joueurs_text.get_rect(center=bouton_3_joueurs_rect.center)

    bouton_4_joueurs_coordonnees = (270,450)
    bouton_4_joueurs_width = 540
    bouton_4_joueurs_heigth = 75
    bouton_4_joueurs_color = (150,150,150)
    bouton_4_joueurs_rect = pygame.Rect(bouton_4_joueurs_coordonnees[0],bouton_4_joueurs_coordonnees[1],bouton_4_joueurs_width,bouton_4_joueurs_heigth)
    bouton_4_joueurs_text = police_38.render("4 joueurs",True,(0,0,0))
    bouton_4_joueurs_text_rect = bouton_4_joueurs_text.get_rect(center=bouton_4_joueurs_rect.center)

def actualisation_fenetre () :
    pygame.display.flip()
    screen.fill((255,255,255))

    screen.blit(nbr_joueur_text,nbr_joueur_text_rect)
    
    screen.blit(avertissement_text,avertissement_text_rect)

    pygame.draw.rect(screen,bouton_2_joueurs_color,bouton_2_joueurs_rect,0)
    screen.blit(bouton_2_joueurs_text,bouton_2_joueurs_text_rect)

    pygame.draw.rect(screen,bouton_3_joueurs_color,bouton_3_joueurs_rect,0)
    screen.blit(bouton_3_joueurs_text,bouton_3_joueurs_text_rect)

    pygame.draw.rect(screen,bouton_4_joueurs_color,bouton_4_joueurs_rect,0)
    screen.blit(bouton_4_joueurs_text,bouton_4_joueurs_text_rect)