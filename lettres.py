import pygame

#Création class lettres
class Lettre (pygame.sprite.Sprite) :
    def __init__(self, lettre) :
        super().__init__()

        if lettre in ['I', 'O', 'Q', 'W']:
            format_img = "png"
        else:
            format_img = "jpg"

        image = "assets\lettres\\{}.{}".format(lettre, format_img)
        image_grise = "assets\\lettres_grises\\{}.{}".format(lettre, format_img)

        self.image = pygame.image.load(image)
        self.image_grise = pygame.image.load(image_grise)
        self.position = self.image.get_rect()
        self.grise = False

#Création des lettres
"""A1 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")
A2 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")
A3 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")
A4 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")
A5 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")
A6 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")
A7 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")
A8 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")
A9 = lettre("A" ,1 , "assets\lettres\\A.jpg","assets\\lettres_grises\\A.jpg")

B1 = lettre ("B" ,3, "assets\lettres\\B.jpg ","assets\\lettres_grises\\B.jpg")
B2 = lettre ("B" ,3, "assets\lettres\\B.jpg ","assets\\lettres_grises\\B.jpg")

C1= lettre ("C" ,3, "assets\lettres\\C.jpg ","assets\\lettres_grises\\C.jpg")
C2= lettre ("C" ,3, "assets\lettres\\C.jpg ","assets\\lettres_grises\\C.jpg")

D1= lettre ("D" ,2, "assets\lettres\\D.jpg ","assets\\lettres_grises\\D.jpg")
D2= lettre ("D" ,2, "assets\lettres\\D.jpg ","assets\\lettres_grises\\D.jpg")
D3= lettre ("D" ,2, "assets\lettres\\D.jpg ","assets\\lettres_grises\\D.jpg")

E1= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E2= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E3= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E4= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E5= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E6= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E7= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E8= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E9= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E10= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E11= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E12= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E13= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E14= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")
E15= lettre ("E" ,1, "assets\lettres\\E.jpg ","assets\\lettres_grises\\E.jpg")

F1= lettre ("F" ,4, "assets\lettres\\F.jpg ","assets\\lettres_grises\\F.jpg")
F2= lettre ("F" ,4, "assets\lettres\\F.jpg ","assets\\lettres_grises\\F.jpg")

G1= lettre ("G" ,2, "assets\lettres\\G.jpg ","assets\\lettres_grises\\G.jpg")
G2= lettre ("G" ,2, "assets\lettres\\G.jpg ","assets\\lettres_grises\\G.jpg")

H1= lettre ("H" ,4, "assets\lettres\\H.jpg ","assets\\lettres_grises\\H.jpg")
H2= lettre ("H" ,4, "assets\lettres\\H.jpg ","assets\\lettres_grises\\H.jpg")

I1= lettre ("I" ,1, "assets\lettres\\I.png ","assets\\lettres_grises\\I.png")
I2= lettre ("I" ,1, "assets\lettres\\I.png ","assets\\lettres_grises\\I.png")
I3= lettre ("I" ,1, "assets\lettres\\I.png ","assets\\lettres_grises\\I.png")
I4= lettre ("I" ,1, "assets\lettres\\I.png ","assets\\lettres_grises\\I.png")
I5= lettre ("I" ,1, "assets\lettres\\I.png ","assets\\lettres_grises\\I.png")
I6= lettre ("I" ,1, "assets\lettres\\I.png ","assets\\lettres_grises\\I.png")
I7= lettre ("I" ,1, "assets\lettres\\I.png ","assets\\lettres_grises\\I.png")
I8= lettre ("I" ,1, "assets\lettres\\I.png ","assets\\lettres_grises\\I.png")

J1= lettre ("J" ,8, "assets\lettres\\J.jpg ","assets\\lettres_grises\\J.jpg")

K1= lettre ("K" ,10, "assets\lettres\\K.jpg ","assets\\lettres_grises\K.jpg")

L1= lettre ("L" ,1, "assets\lettres\\L.jpg ","assets\\lettres_grises\\L.jpg")
L2= lettre ("L" ,1, "assets\lettres\\L.jpg ","assets\\lettres_grises\\L.jpg")
L3= lettre ("L" ,1, "assets\lettres\\L.jpg ","assets\\lettres_grises\\L.jpg")
L4= lettre ("L" ,1, "assets\lettres\\L.jpg ","assets\\lettres_grises\\L.jpg")
L5= lettre ("L" ,1, "assets\lettres\\L.jpg ","assets\\lettres_grises\\L.jpg")

M1= lettre ("M" ,2, "assets\lettres\\M.jpg ","assets\\lettres_grises\\M.jpg")
M2= lettre ("M" ,2, "assets\lettres\\M.jpg ","assets\\lettres_grises\\M.jpg")
M3= lettre ("M" ,2, "assets\lettres\\M.jpg ","assets\\lettres_grises\\M.jpg")

N1= lettre ("N" ,1, "assets\lettres\\N.jpg ","assets\\lettres_grises\\N.jpg")
N2= lettre ("N" ,1, "assets\lettres\\N.jpg ","assets\\lettres_grises\\N.jpg")
N3= lettre ("N" ,1, "assets\lettres\\N.jpg ","assets\\lettres_grises\\N.jpg")
N4= lettre ("N" ,1, "assets\lettres\\N.jpg ","assets\\lettres_grises\\N.jpg")
N5= lettre ("N" ,1, "assets\lettres\\N.jpg ","assets\\lettres_grises\\N.jpg")
N6= lettre ("N" ,1, "assets\lettres\\N.jpg ","assets\\lettres_grises\\N.jpg")

O1= lettre ("O" ,1, "assets\lettres\\O.png ","assets\\lettres_grises\\O.png")
O2= lettre ("O" ,1, "assets\lettres\\O.png ","assets\\lettres_grises\\O.png")
O3= lettre ("O" ,1, "assets\lettres\\O.png ","assets\\lettres_grises\\O.png")
O4= lettre ("O" ,1, "assets\lettres\\O.png ","assets\\lettres_grises\\O.png")
O5= lettre ("O" ,1, "assets\lettres\\O.png ","assets\\lettres_grises\\O.png")
O6= lettre ("O" ,1, "assets\lettres\\O.png ","assets\\lettres_grises\\O.png")

P1= lettre ("P" ,3, "assets\lettres\\P.jpg ","assets\\lettres_grises\\P.jpg")
P2= lettre ("P" ,3, "assets\lettres\\P.jpg ","assets\\lettres_grises\\P.jpg")

Q1= lettre ("Q" ,8, "assets\lettres\\Q.png ","assets\\lettres_grises\\Q.png")

R1= lettre ("R" ,1, "assets\lettres\\R.jpg ","assets\\lettres_grises\\R.jpg")
R2= lettre ("R" ,1, "assets\lettres\\R.jpg ","assets\\lettres_grises\\R.jpg")
R3= lettre ("R" ,1, "assets\lettres\\R.jpg ","assets\\lettres_grises\\R.jpg")
R4= lettre ("R" ,1, "assets\lettres\\R.jpg ","assets\\lettres_grises\\R.jpg")
R5= lettre ("R" ,1, "assets\lettres\\R.jpg ","assets\\lettres_grises\\R.jpg")
R6= lettre ("R" ,1, "assets\lettres\\R.jpg ","assets\\lettres_grises\\R.jpg")

S1= lettre ("S" ,1, "assets\lettres\\S.jpg ","assets\\lettres_grises\\S.jpg")
S2= lettre ("S" ,1, "assets\lettres\\S.jpg ","assets\\lettres_grises\\S.jpg")
S3= lettre ("S" ,1, "assets\lettres\\S.jpg ","assets\\lettres_grises\\S.jpg")
S4= lettre ("S" ,1, "assets\lettres\\S.jpg ","assets\\lettres_grises\\S.jpg")
S5= lettre ("S" ,1, "assets\lettres\\S.jpg ","assets\\lettres_grises\\S.jpg")
S6= lettre ("S" ,1, "assets\lettres\\S.jpg ","assets\\lettres_grises\\S.jpg")

T1= lettre ("T" ,1, "assets\lettres\\T.jpg ","assets\\lettres_grises\\T.jpg")
T2= lettre ("T" ,1, "assets\lettres\\T.jpg ","assets\\lettres_grises\\T.jpg")
T3= lettre ("T" ,1, "assets\lettres\\T.jpg ","assets\\lettres_grises\\T.jpg")
T4= lettre ("T" ,1, "assets\lettres\\T.jpg ","assets\\lettres_grises\\T.jpg")
T5= lettre ("T" ,1, "assets\lettres\\T.jpg ","assets\\lettres_grises\\T.jpg")
T6= lettre ("T" ,1, "assets\lettres\\T.jpg ","assets\\lettres_grises\\T.jpg")

U1= lettre ("U" ,1, "assets\lettres\\U.jpg ","assets\\lettres_grises\\U.jpg")
U2= lettre ("U" ,1, "assets\lettres\\U.jpg ","assets\\lettres_grises\\U.jpg")
U3= lettre ("U" ,1, "assets\lettres\\U.jpg ","assets\\lettres_grises\\U.jpg")
U4= lettre ("U" ,1, "assets\lettres\\U.jpg ","assets\\lettres_grises\\U.jpg")
U5= lettre ("U" ,1, "assets\lettres\\U.jpg ","assets\\lettres_grises\\U.jpg")
U6= lettre ("U" ,1, "assets\lettres\\U.jpg ","assets\\lettres_grises\\U.jpg")

V1= lettre ("V" ,4, "assets\lettres\\V.jpg ","assets\\lettres_grises\\V.jpg")
V2= lettre ("V" ,4, "assets\lettres\\V.jpg ","assets\\lettres_grises\\V.jpg")

W1= lettre ("W" ,10, "assets\lettres\\W.png ","assets\\lettres_grises\\W.png")

X1= lettre ("X" ,10, "assets\lettres\\X.jpg ","assets\\lettres_grises\\X.jpg")
Y1= lettre ("Y" ,10, "assets\lettres\\Y.jpg ","assets\\lettres_grises\\Y.jpg")

Z1= lettre ("Z" ,10, "assets\lettres\\Z.jpg ","assets\\lettres_grises\\Z.jpg")

"""