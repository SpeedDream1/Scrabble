import pygame

#Création class lettres
class Lettre (pygame.sprite.Sprite) :
    def __init__(self, lettre) :
        super().__init__()

        if lettre == '*':
            self.lettre = 'joker'
        else:
            self.lettre = lettre
        image = "assets\lettres\\{}.png".format(self.lettre)
        image_grise = "assets\\lettres_grises\\{}.png".format(self.lettre)
        image_defausse = "assets\\lettres_rouges\\{}.png".format(self.lettre)

        self.image = pygame.image.load(image)
        self.image_grise = pygame.image.load(image_grise)
        self.image_defausse = pygame.image.load(image_defausse)
        self.position = self.image.get_rect()
        self.grise = False

    def joker_lettre_selection(self, lettre):
        self.lettre = lettre
        image_grise = "assets\\lettres_grises\\{}.png".format(lettre)
        self.image_grise = pygame.image.load(image_grise)