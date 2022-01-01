class Vecteur2D:
        #"""Les Vecteurs plans."""
        def __init__(self, x0=0, y0=0):
               # """Constructeur avec parametres par defaut."""
                self.x = x0  # initialisation de x et y, attributs d'instance
                self.y = y0
        def __str__(self):
                #""" Utilisation du print """
                return "x = %d, y = %d" % (self.x,self.y)
if __name__ == '__main__':
        print(" une instance par defaut ")
        print (Vecteur2D())
        print(" une instance initialisee ")
        print (Vecteur2D(-5.2, 4.1))
      