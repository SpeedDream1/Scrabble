import pygame

# Lancement de l'interface
pygame.init()
pygame.display.set_caption("Scrabble")

# Police de texte
police_28 = pygame.font.Font(None,28)
police_32 = pygame.font.Font(None,32)
police_48 = pygame.font.Font(None,48)
police_38 = pygame.font.Font(None,38)
# Définition de la fenetre du jeu
if  pygame.display.Info().current_h < 933 : # Taille barre des taches = 84
    screen_size = (1080, 751)
    format_ecran = 0
else :
    screen_size = (1080, 849)
    format_ecran = 1

#screen_size = (1080, 849)
#format_ecran = 1
screen = pygame.display.set_mode(screen_size)

# Définition du plateau
img_plateau = pygame.image.load("assets\plato_scrabble.jpg").convert() # Taille Case 48x48
fond = pygame.Surface(screen.get_size())

# Coordonnées des éléments graphiques
if format_ecran == 0 :
    # plateau
    coord_plateau = (98,0)
    coord_chevalet = (20,0)
    # chevalet
    chevalet_rect = pygame.Rect(coord_chevalet[0] ,coord_chevalet[1], 58, 751) # chevalet
    # bouton valider
    bouton_valider_coordonnees = (875,672)
    bouton_valider_width = 180
    bouton_valider_heigth = 40
    bouton_valider_color = (0,153,102)
    bouton_valider_text = police_48.render("Valider",True,(255,255,255))
    bouton_valider_rect = pygame.Rect(bouton_valider_coordonnees[0],bouton_valider_coordonnees[1],bouton_valider_width,bouton_valider_heigth)
    bouton_valider_text_rect = bouton_valider_text.get_rect(center=bouton_valider_rect.center)
    # bouton defausser
    bouton_defausser_coordonnees = (875,447)
    bouton_defausser_width = 180
    bouton_defausser_heigth = 40
    bouton_defausser_color = (255,0,0)
    bouton_defausser_rect = pygame.Rect(bouton_defausser_coordonnees[0],bouton_defausser_coordonnees[1],bouton_defausser_width,bouton_defausser_heigth)
    bouton_defausser_text = police_48.render("Defausser",True,(255,255,255))
    bouton_defausser_text_rect = bouton_defausser_text.get_rect(center=bouton_defausser_rect.center)
    # bouton ranger les lettres
    bouton_ranger_lettres_coordonnees = (875,522)
    bouton_ranger_lettres_width = 180
    bouton_ranger_lettres_heigth = 40
    bouton_ranger_lettres_color = (0,89,255)
    bouton_ranger_lettres_rect = pygame.Rect(bouton_ranger_lettres_coordonnees[0],bouton_ranger_lettres_coordonnees[1],bouton_ranger_lettres_width,bouton_ranger_lettres_heigth)
    bouton_ranger_lettres_text = police_28.render("Ranger les lettres",True,(255,255,255))
    bouton_ranger_lettres_text_rect = bouton_ranger_lettres_text.get_rect(center=bouton_ranger_lettres_rect.center)
    # bouton passer son tour
    bouton_passer_tour_coordonnees = (875,597)
    bouton_passer_tour_width = 180
    bouton_passer_tour_heigth = 40
    bouton_passer_tour_color = (95,50,25)
    bouton_passer_tour_rect = pygame.Rect(bouton_passer_tour_coordonnees[0],bouton_passer_tour_coordonnees[1],bouton_passer_tour_width,bouton_passer_tour_heigth)
    bouton_passer_tour_text = police_28.render("Passer son tour",True,(255,255,255))
    bouton_passer_tour_text_rect = bouton_passer_tour_text.get_rect(center=bouton_passer_tour_rect.center)

else :
    # plateau
    coord_plateau = (0,0)
    coord_chevalet = (0,771)
    # chevalet
    chevalet_rect = pygame.Rect(coord_chevalet[0] ,coord_chevalet[1] ,752,58) # chevalet
    # bouton valider
    bouton_valider_coordonnees = (805,741)
    bouton_valider_width = 220
    bouton_valider_heigth = 50
    bouton_valider_color = (0,153,102)
    bouton_valider_text = police_48.render("Valider",True,(255,255,255))
    bouton_valider_rect = pygame.Rect(bouton_valider_coordonnees[0],bouton_valider_coordonnees[1],bouton_valider_width,bouton_valider_heigth)
    bouton_valider_text_rect = bouton_valider_text.get_rect(center=bouton_valider_rect.center)
    # bouton defausser
    bouton_defausser_coordonnees = (805,516)
    bouton_defausser_width = 220
    bouton_defausser_heigth = 50
    bouton_defausser_color = (255,0,0)
    bouton_defausser_rect = pygame.Rect(bouton_defausser_coordonnees[0],bouton_defausser_coordonnees[1],bouton_defausser_width,bouton_defausser_heigth)
    bouton_defausser_text = police_48.render("Defausser",True,(255,255,255))
    bouton_defausser_text_rect = bouton_defausser_text.get_rect(center=bouton_defausser_rect.center)
    # bouton ranger les lettres
    bouton_ranger_lettres_coordonnees = (805,666)
    bouton_ranger_lettres_width = 220
    bouton_ranger_lettres_heigth = 50
    bouton_ranger_lettres_color = (0,89,255)
    bouton_ranger_lettres_rect = pygame.Rect(bouton_ranger_lettres_coordonnees[0],bouton_ranger_lettres_coordonnees[1],bouton_ranger_lettres_width,bouton_ranger_lettres_heigth)
    bouton_ranger_lettres_text = police_32.render("Ranger les lettres",True,(255,255,255))
    bouton_ranger_lettres_text_rect = bouton_ranger_lettres_text.get_rect(center=bouton_ranger_lettres_rect.center)
    # bouton passer son tour
    bouton_passer_tour_coordonnees = (805,591)
    bouton_passer_tour_width = 220
    bouton_passer_tour_heigth = 50
    bouton_passer_tour_color = (95,50,25)
    bouton_passer_tour_rect = pygame.Rect(bouton_passer_tour_coordonnees[0],bouton_passer_tour_coordonnees[1],bouton_passer_tour_width,bouton_passer_tour_heigth)
    bouton_passer_tour_text = police_32.render("Passer son tour",True,(255,255,255))
    bouton_passer_tour_text_rect = bouton_passer_tour_text.get_rect(center=bouton_passer_tour_rect.center)

# Création liste des coordonnées de toute les cases
coord_case_plateau = [[(coord_plateau[0]+1+50*i , coord_plateau[1]+1+50*j) for j in range(15)] for i in range(15)] # plateau
coord_case_chevalet = [((coord_chevalet[0]+5 , coord_chevalet[1]+52+100*i) if format_ecran == 0 else
                                (coord_chevalet[0]+52+100*i, coord_chevalet[1]+5)) for i in range(7)] # chevalet

    
# Parametres
bouton_parametres = pygame.Rect(1050,5,25,25)
parametres = False
image_bouton_parametres = pygame.image.load("assets//image_parametres.png")


# Score
def affichage_score(joueurs,tour) :
    score = [(i,joueurs[i][0]) for i in range(1,len(joueurs))]
    score.sort(key=lambda j:j[-1],reverse=1)
    couleur_classement = {
        1 : (250,155,0),
        2 : (120,120,120),
        3 : (170,80,30)
    }
    if format_ecran==0 :
        y = 0
        score_joueur_coord = {}
        for i in range(1,len(joueurs)) :
            arriere_plan_score_coordonnees = (879,0+y)
            score_joueur_coord[i] = arriere_plan_score_coordonnees
            arriere_plan_score_width = 201
            arriere_plan_score_heigth = 50
            if i == tour :
                arriere_plan_score_color = (75,75,75)
            else :
                arriere_plan_score_color = (255,255,255)
            arriere_plan_score_rect = pygame.Rect(arriere_plan_score_coordonnees[0],arriere_plan_score_coordonnees[1],arriere_plan_score_width,arriere_plan_score_heigth)
            score_joueur_text = police_38.render(f"Joueur {i} : {joueurs[i][0]}",True,(0,0,0))
            score_joueur_text_rect = score_joueur_text.get_rect(center=arriere_plan_score_rect.center)
            pygame.draw.rect(screen,arriere_plan_score_color,arriere_plan_score_rect)
            screen.blit(score_joueur_text,score_joueur_text_rect)
            y+=50
        y=0
        j=1
        for i in score :
            y = i[0]*50-50
            classement_coord = (849,y)
            classement_width = 30
            classement_heigth = 50
            if j<=3 :
                classement_color = couleur_classement[j]
            else :
                classement_color = (220,220,220)
            classement_rect = pygame.Rect(classement_coord[0],classement_coord[1],classement_width,classement_heigth)
            classement_text = police_38.render(f"{j}.",True,(0,0,0))
            classement_text_rect = classement_text.get_rect(center=classement_rect.center)
            pygame.draw.rect(screen,classement_color,classement_rect)
            screen.blit(classement_text,classement_text_rect)
            y+=50
            j+=1

    else :
        y = 0
        score_joueur_coord = {}
        for i in score :
            arriere_plan_score_coordonnees = (781,0+y)
            score_joueur_coord[i[0]] = arriere_plan_score_coordonnees
            arriere_plan_score_width = 299
            arriere_plan_score_heigth = 50
            if i[0] == tour :
                arriere_plan_score_color = (75,75,75)
            else :
                arriere_plan_score_color = (255,255,255)
            arriere_plan_score_rect = pygame.Rect(arriere_plan_score_coordonnees[0],arriere_plan_score_coordonnees[1],arriere_plan_score_width,arriere_plan_score_heigth)
            score_joueur_text = police_48.render(f"Joueur {i[0]} : {i[1]}",True,(0,0,0))
            score_joueur_text_rect = score_joueur_text.get_rect(center=arriere_plan_score_rect.center)
            pygame.draw.rect(screen,arriere_plan_score_color,arriere_plan_score_rect)
            screen.blit(score_joueur_text,score_joueur_text_rect)
            y+=50
        
        y=0
        j=1
        for i in score :
            y = i[0]*50-50
            classement_coord = (751,y)
            classement_width = 30
            classement_heigth = 50
            if j<=3 :
                classement_color = couleur_classement[j]
            else :
                classement_color = (220,220,220)
            classement_rect = pygame.Rect(classement_coord[0],classement_coord[1],classement_width,classement_heigth)
            classement_text = police_38.render(f"{j}.",True,(0,0,0))
            classement_text_rect = classement_text.get_rect(center=classement_rect.center)
            pygame.draw.rect(screen,classement_color,classement_rect)
            screen.blit(classement_text,classement_text_rect)
            y+=50
            j+=1
    

    
    