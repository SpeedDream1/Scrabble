import pygame

# Lancement de l'interface
pygame.init()
pygame.display.set_caption("Scrabble")

# Police de texte
police_28 = pygame.font.Font(None,28)
police_32 = pygame.font.Font(None,32)
police_48 = pygame.font.Font(None,48)
police_38 = pygame.font.Font(None,38)
police_64 = pygame.font.Font(None,64)

# Taille écran
with open("options.txt", 'r') as fichier :
    chargement = fichier.readlines()
    format_ecran = int(chargement[0])
if format_ecran == 0 :
    screen_size = (1080,751)
else :
    screen_size = (1080,849)

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
        for i in range(1,len(joueurs)) :
            arriere_plan_score_coordonnees = (781,0+y)
            score_joueur_coord[i] = arriere_plan_score_coordonnees
            arriere_plan_score_width = 299
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


# Changer les boutons pour le mode defaussage
def set_mode_defaussage(set=True):
    if set:
        global bouton_defausser_text
        global bouton_defausser_text_rect
        global bouton_passer_tour_text
        global bouton_passer_tour_text_rect
        global bouton_ranger_lettres_color

        bouton_defausser_text = police_48.render("Annuler",True,(255,255,255))
        bouton_defausser_text_rect = bouton_defausser_text.get_rect(center=bouton_defausser_rect.center)
        bouton_passer_tour_text = police_28.render("Annuler et passer",True,(255,255,255))
        bouton_passer_tour_text_rect = bouton_passer_tour_text.get_rect(center=bouton_passer_tour_rect.center)
        bouton_ranger_lettres_color = (200,200,255)

    else:

        bouton_defausser_text = police_48.render("Defausser",True,(255,255,255))
        bouton_defausser_text_rect = bouton_defausser_text.get_rect(center=bouton_defausser_rect.center)
        bouton_passer_tour_text = police_32.render("Passer son tour",True,(255,255,255))
        bouton_passer_tour_text_rect = bouton_passer_tour_text.get_rect(center=bouton_passer_tour_rect.center)
        bouton_ranger_lettres_color = (0,89,255)
            


# Changer les boutons pour le mode de selection de lettre du joker
def set_mode_joker(set=True):
    if set:
        global bouton_defausser_color
        global bouton_passer_tour_color
        global bouton_ranger_lettres_color
        global bouton_valider_color

        bouton_valider_color = (137,182,167)
        bouton_defausser_color = (255,170,170)
        bouton_ranger_lettres_color = (200,200,255)
        bouton_passer_tour_color = (143,112,95)

    else:

        bouton_valider_color = (0,153,102)
        bouton_defausser_color = (255,0,0)
        bouton_ranger_lettres_color = (0,89,255)
        bouton_passer_tour_color = (95,50,25)


# Fonction affichage d'une lettre
def placer_lettre (lettre, lieu, coord) :
    if lieu == "chevalet" :  # placer_lettre (lettre,"chevalet",(n,))
        lettre.position.topleft = coord_case_chevalet[coord[0]]
    elif lieu == "plateau" :  #placer_lettre (lettre,"plateau",(x,y))
        lettre.position.topleft = coord_case_plateau[coord[1]][coord[0]] # car coord inversées

# Une fois qu'une lettre est placée et ne peux plus être bougée
def griser_lettre (lettre) :
    lettre.grise = True
    screen.blit(lettre.image_grise, lettre.position)
    
# convertie des coordonnée en pixel en coordonnée de la case la plus proche
def convert_px_coord(x, y) :
    if coord_plateau[0] < x < coord_plateau[0]+751 and coord_plateau[1] < y < coord_plateau[1]+751 :
        x -= coord_plateau[0]
        y -= coord_plateau[1]
        x = round(x/50)
        y = round(y/50)
        if x == 15 :
            x = 14
        if y == 15 :
            y = 14
        return "plateau", (y, x)  # car coord inversées
    elif format_ecran == 0 and coord_chevalet[0] < x < coord_chevalet[0]+58 and coord_chevalet[1] < y < coord_chevalet[1]+751:
        y -= coord_chevalet[1]
        if y > 652 :
            y = 652
        return "chevalet", (0, y//100)
    elif format_ecran == 1 and coord_chevalet[0] < x < coord_chevalet[0]+752 and coord_chevalet[1] < y < coord_chevalet[1]+58:
        x -= coord_chevalet[0]
        if x > 652 :
            x = 652
        return "chevalet", (0, x//100)
    else:
        return "en dehors", 0   
    
    
def actualisation_fenetre():
    pygame.display.flip() # MaJ de la fenêtre
        
    # Affichage de la fenêtre
    screen.fill((255,255,255))
    # Plateau
    screen.blit(img_plateau,coord_plateau)
    # Chevalet
    pygame.draw.rect(screen,(100,100,100),chevalet_rect,0)
    # Bouton Valider
    pygame.draw.rect(screen,bouton_valider_color,bouton_valider_rect,0)
    screen.blit(bouton_valider_text,bouton_valider_text_rect)
    # Bouton parametres
    pygame.draw.rect(screen,(255,255,255),bouton_parametres,0)
    screen.blit(image_bouton_parametres,(1050,5))
    # Bouton Rangement des lettres
    pygame.draw.rect(screen,bouton_ranger_lettres_color,bouton_ranger_lettres_rect,0)
    screen.blit(bouton_ranger_lettres_text,bouton_ranger_lettres_text_rect)
    # Bouton Deffausser les lettres
    pygame.draw.rect(screen,bouton_defausser_color,bouton_defausser_rect,0)
    screen.blit(bouton_defausser_text,bouton_defausser_text_rect)
    # Bouton Passer son tour
    pygame.draw.rect(screen,bouton_passer_tour_color,bouton_passer_tour_rect,0)
    screen.blit(bouton_passer_tour_text,bouton_passer_tour_text_rect)