class Rectangle:
        def __init__(self, longueur=10, largeur=6):
                self.lon = longueur
                self.lar = largeur
                self.nom = "rectangle"
        def surface(self):
                #Retourner la surface d'un rectangle
                return self.lon*self.lar
        def __str__(self):
                #Affichage des caracteristiques d'un rectangle
                return ("\nLe {0} de côtes {1} et {2} a une surface de {3}"
                                .format(self.nom, self.lon, self.lar, self.surface()))
class Carre(Rectangle):
        def __init__(self, cote=10):
                #Constructeur avec valeur par defaut
                Rectangle.__init__(self, cote, cote)
                self.nom = "carre" 
if __name__ == '__main__':
        r = Rectangle(2, 4)
        print(r)
        c = Carre()
        print(c)