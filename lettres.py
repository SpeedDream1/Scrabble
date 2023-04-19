import pygame

#Création class lettres
class Lettre (pygame.sprite.Sprite) :
    def __init__(self, lettre) :
        super().__init__()

        image = "assets\lettres\\{}.png".format(lettre)
        image_grise = "assets\\lettres_grises\\{}.png".format(lettre)
        image_defausse = "assets\\lettres_rouges\\{}.png".format(lettre)

        self.image = pygame.image.load(image)
        self.image_grise = pygame.image.load(image_grise)
        self.image_defausse = pygame.image.load(image_defausse)
        self.position = self.image.get_rect()
        self.grise = False

