from random import randrange
import pygame

from data import *
from trouver_mot import *
from lettres import *

# ______________________________________[préparation de la partie]__________________________________________



nb_joueur = 2 # int(input("nombre de joueurs: "))

pioche = []  # initialisation de la pioche
for key, value in QTT_LETTRES.items():
    pioche.extend([str(key)]*value)

def piocher():
    return pioche.pop(randrange(len(pioche)))

# initialisation des joueurs: [score, lettres]
joueurs = [''] + [[0, [piocher() for _ in range(7)]] for i in range(nb_joueur)]

# initialisation du plateau
plateau = [list(i) for i in PLATEAU_DEPART]

# Trouver un mot à partir des coordonnés d'une case et de la direction
def get_mot(coord, sens): 
    ligne = coord[0]   
    colonne = coord[1]

    if sens == 0: # cas horizontal
        while colonne > 0: # trouver la colonne de la 1ere lettre du mot
            if plateau[ligne][colonne-1] != '/':
                colonne -= 1
            else:
                break
        coord_min = colonne
        while colonne < 14: # parcourir le mot
            if plateau[ligne][colonne+1] != '/':
                colonne += 1
            else:
                break
        coord_max = colonne
        mot = plateau[ligne][coord_min:coord_max+1]
        # mot = get_lettres(ligne, coord_min, sens, coord_max-coord_min+1)
    
    else: # cas vertical
        while ligne > 0: # trouver la colonne de la 1ere lettre du mot
            if plateau[ligne-1][colonne] != '/':
                ligne -= 1
            else:
                break
        coord_min = ligne

        while ligne < 14: # parcourir le mot
            if plateau[ligne+1][colonne] != '/':
                ligne += 1
            else:
                break
        coord_max = ligne
        mot = [i[colonne] for i in plateau[coord_min:coord_max+1]] 
        # mot = get_lettres(coord_min, colonne, sens, coord_max-coord_min+1)
    return mot

premier_tour = True
new_tour = True
defaussage = False
tour = 0
J_lettres = []



# ______________________________________[préparation de l'interface]__________________________________________



from interface import *

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

# Variables essentielles au lancement du jeu
running = True
mvt_lettre = (False,0)
lettres_grises = []


# ______________________________________[Lancement de la fenêtre]__________________________________________


def afficher_plateau(): # fonction pour visualiser le plateau
    print('\n   ', end='')
    for i in range(15):
        print((str(i)+' ')[:2], end='')
    print()
    for i in range(15):
        print((str(i)+' ')[:2], *plateau[i], sep = ' ')


while running :

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



    # Si c'est un nouveau tour
    if new_tour:
        if '^' in J_lettres: # si il y a des lettres à remplacer
            i = 0
            for l in J_lettres: # on décale les lettres qui restent à gauche
                if l != '^':
                    joueurs[tour][1][i] = l
                    i += 1

            while i < 7: # puis puis on pioche pour completer sa main
                if len(pioche) > 0:
                    joueurs[tour][1][i] = piocher()
                else:
                    joueurs[tour][1][i] = "_" # lettre vide si la pioche est vide
                i += 1

        else: 
            for i in range(len(J_lettres)):
                lettre = J_lettres[i] # ranger les lettres
                if type(lettre) == tuple:
                    plateau[lettre[0]][lettre[1]] = '/'

        tour = tour%nb_joueur + 1 # au joueur suivant

        J_lettres = list(joueurs[tour][1]) # récuperer les lettres du joueur
        J_lettres_img = [Lettre(i) if i != '_' else '_' for i in J_lettres]
        for i, lettre in enumerate(J_lettres_img):
            if lettre != '_':
                placer_lettre(J_lettres_img[i],"chevalet",(i,))
        new_tour = False

    # Placement des lettres
    for img in lettres_grises:
        screen.blit(img.image_grise , img.position)
    for img in J_lettres_img:
        if img != '_' and (not mvt_lettre[0] or img != mvt_lettre[1]):
            screen.blit(img.image , img.position)
    if mvt_lettre[0]: # on met la lettre tenue au premier plan
        img = J_lettres_img[mvt_lettre[1]]
        screen.blit(img.image , img.position)


    # Evenements
    for event in pygame.event.get() :
        # Quitter le jeu
        if event.type == pygame.QUIT : 
            running = False
            pygame.quit()
        
        # Placement d'une lettre
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # clic gauche relevé
            x, y = pygame.mouse.get_pos()
            if mvt_lettre[0] : # Si on est en train de déplacer une lettre

                i_lettre = mvt_lettre[1]
                emplacement, coord = convert_px_coord(x, y)

                if emplacement == "chevalet": # si on place la lettre sur le chevalet
                    pos = int(max(coord))

                    if type(J_lettres[i_lettre]) == tuple: # si la lettre était sur le plateau
                        plateau[J_lettres[i_lettre][0]][J_lettres[i_lettre][1]] = '/'
                        J_lettres[i_lettre] = joueurs[tour][1][i_lettre] # on la remet d'abord sur le chevalet
                        placer_lettre(J_lettres_img[i_lettre], "chevalet", (i_lettre,))

                    if type(J_lettres[pos]) == tuple: # si l'autre est sur le plateau
                        plateau[J_lettres[pos][0]][J_lettres[pos][1]] = str(i_lettre) # on l'échange
                        
                    if i_lettre != pos: # puis on échange
                        placer_lettre(J_lettres_img[i_lettre], "chevalet", (pos,))
                        if type(J_lettres[pos]) != tuple: # si l'autre lettre est sur le chevalet
                            placer_lettre(J_lettres_img[pos], "chevalet", (i_lettre,))
                        J_lettres[i_lettre], J_lettres[pos] = J_lettres[pos], J_lettres[i_lettre]
                        J_lettres_img[i_lettre], J_lettres_img[pos] = J_lettres_img[pos], J_lettres_img[i_lettre]
                        joueurs[tour][1][i_lettre], joueurs[tour][1][pos] = joueurs[tour][1][pos], joueurs[tour][1][i_lettre]

                if emplacement == "plateau" and plateau[coord[0]][coord[1]] == "/": # si on place la lettre sur le plateau
                    
                    if type(J_lettres[i_lettre]) == tuple: # si la lettre est sur le plateau
                        old_coord = J_lettres[i_lettre]
                        plateau[old_coord[0]][old_coord[1]] = '/'
                    J_lettres[i_lettre] = coord  # remplace la lettre par ses coordonnés
                    plateau[coord[0]][coord[1]] = str(i_lettre)
                    placer_lettre(J_lettres_img[i_lettre], "plateau", coord)

                else: # si on place la lettre hors du cadre ou sur une case occupée elle revient a sa position
                    if type(J_lettres[i_lettre]) == tuple: # si elle était sur le plateau
                        placer_lettre(J_lettres_img[i_lettre], "plateau", J_lettres[i_lettre])
                    else: # si elle etait sur son chevalet
                        placer_lettre(J_lettres_img[i_lettre], "chevalet", (i_lettre,))

                mvt_lettre = (False,0)

        # Clic gauche pressé 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 : 
            for i, lettre in enumerate(J_lettres_img):
                if lettre.position.collidepoint(event.pos): # Si le curseur est sur une lettre
                    if defaussage:
                        if J_lettres[i] != '^':
                            J_lettres[i] = '^' # lettres à remplacer
                        else:
                            J_lettres[i] = joueurs[tour][1][i]
                    else: # Sinon la lettre est prise
                        mvt_lettre = (True,i)
                    break
            
            # validation du mot
            if bouton_valider_rect.collidepoint(event.pos):

                valide = True

                lettres_placees = [i for i in J_lettres if type(i) == tuple]
                lettres_placees.sort()

                if len(lettres_placees) < 1:
                    print("Vous devez placer au moins une lettre")
                    valide = False
                    continue
                
                # si il y a un joker
                jokers = ['']*7
                for i, lettre in enumerate(J_lettres):
                    if type(lettre) == tuple and joueurs[tour][1][i] == '*':
                        jokers[i] = input("* = ")

                # au premier tour la case du milieu doit être recouverte
                if premier_tour:
                    if not (7, 7) in lettres_placees:
                        print("Vous devez placer votre mot sur la case du milieu")
                        valide = False
                        continue

                # vérification que toutes les lettres soit alignées
                sens = 1 # 0: horizontal, 1: vertical
                for lettre in lettres_placees:
                    if lettre[1] != lettres_placees[0][1]: # s'il n'est pas vertical
                        sens = 0
                        for lettre in lettres_placees:
                            if lettre[0] != lettres_placees[0][0]: # s'il n'est pas horizontal non plus
                                valide = False
                                break 
                        break
                if not valide:
                    print("les lettres doivent être alignés")
                    continue
                
                # recuperation du mot
                mot = get_mot(lettres_placees[0], sens)

                # verification que le mot est continu
                if len([i for i in mot if i.isdigit()]) != len(lettres_placees):
                    print("les lettres doivent former un mot continu")
                    valide = False
                    continue

                # récupération des mots formés
                mots = [mot] if len(mot) > 1 else []
                for lettre in lettres_placees:
                    mot = get_mot(lettre, (sens+1)%2)
                    if len(mot) > 1:
                        mots.append(mot)

                # vérification qu'un des mots est formé sur une lettre placée
                if not premier_tour:
                    valide = False
                    for mot in mots:
                        for lettre in mot:
                            if not lettre.isdigit():
                                valide = True
                                break
                if not valide:
                    print("Vous devez inclure une lettre déjà placée")
                    continue

                # formatage des mots + detection des cases speciales
                mult_cases = [[] for _ in range(len(mots))]
                for i in range(len(mots)):
                    for u in range(len(mots[i])):
                        c = mots[i][u]

                        if c.isdigit():
                            coord = J_lettres[int(c)]
                            fond_case = PLATEAU_CASE[coord[0]][coord[1]]

                            if jokers[int(c)] != '': # si la lettre est un joker
                                mots[i][u] = jokers[int(c)]
                                if fond_case not in ['/', 'd', 't']:
                                    mult_cases[i].append((u,fond_case+'*'))
                                else:
                                    mult_cases[i].append((u,'*'))

                            else:
                                mots[i][u] = joueurs[tour][1][int(c)]
                                if fond_case != '/':
                                    mult_cases[i].append((u,fond_case))

                    mots[i] = "".join(mots[i])

                # verification des mots
                for mot in mots:
                    if not mot_existe(mot):
                        print(f"le mot {mot} n'est pas valide !")
                        valide = False
                        break
                if not valide:
                    continue
                
                # -> tout est validé

                # comptage des points
                points = 0
                for i in range(len(mots)):
                    points_mot = 0

                    for lettre in mots[i]:
                        points_mot += POINT_LETTRE[lettre]

                    for case, mult in mult_cases[i]: # lettre compte x2/3
                        if mult == 'd':
                            points_mot += POINT_LETTRE[mots[i][case]]
                        elif mult == 't':
                            points_mot += POINT_LETTRE[mots[i][case]]*2
                        elif '*' in mult:
                            points_mot -= POINT_LETTRE[mots[i][case]]
                        
                    for case, mult in mult_cases[i]: # mot compte x2/3
                        if mult == 'D' or mult == 'D*':
                            points_mot *= 2
                        elif mult == 'T' or mult == 'T*':
                            points_mot *=3
                    points += points_mot
                print("points gagnés:", points)
                joueurs[tour][0] += points

                # remplacement des lettres placées
                for i, lettre in enumerate(J_lettres):
                    if type(lettre) == tuple:
                        if jokers[i] != "":
                            plateau[lettre[0]][lettre[1]] = jokers[i]
                            # a faire
                        else:
                            plateau[lettre[0]][lettre[1]] = list(joueurs[tour][1])[i]
                            lettres_grises.append(J_lettres_img[i])
                        J_lettres[i] = '^' # lettres à remplacer

                new_tour = True
                if premier_tour:
                    premier_tour = False

            entree = 0
            # Defausser des lettres
            if bouton_defausser_rect.collidepoint(event.pos):
                if defaussage == False:
                    defaussage = True
                    for i in range(7):
                        lettre = J_lettres[i]
                        if type(lettre) == tuple: # ranger les lettres
                            plateau[lettre[0]][lettre[1]] = '/'
                            placer_lettre(J_lettres_img[i],"chevalet",(i,))
                    J_lettres = list(joueurs[tour][1])

                else:
                    defaussage = False
                    new_tour = True


            # Ranger les lettres
            if bouton_ranger_lettres_rect.collidepoint(event.pos):
                for i in range(7):
                    lettre = J_lettres[i]
                    if type(lettre) == tuple:
                        plateau[lettre[0]][lettre[1]] = '/'
                        placer_lettre(J_lettres_img[i],"chevalet",(i,))
                J_lettres = list(joueurs[tour][1])


            # Passer son tour
            if bouton_passer_tour_rect.collidepoint(event.pos):
                new_tour = True


            # Commandes admin
            if 0:
                command = input("Admin: V - vider pioche : ").upper()

                if command == 'V': # vider la pioche
                    nb = int(input("nb: "))
                    for i in range(nb):
                        piocher()

        # déplacer la lettre
        if mvt_lettre[0]:
            (x, y) = pygame.mouse.get_pos()
            J_lettres_img[mvt_lettre[1]].position.topleft = (x, y)
