#class vecteur2D
class vecteur2D:
    #un constructeur par défaut et paramétrer à la fois
     def __init__(self,x1=0, y1=0):
           self.x = x1
           self.y = y1
     #une méthode d'affichage les attributs 
     def display(self):
            print("x: %d \ny: %d" % (self.x, self.y))
     #une méthode de surcharge d’addition      
     def __add__(self,other):
         x1 = self.x + other.x
         y1 = self.y + other.y
         p = vecteur2D(x1 , y1)
         return  p
     #une méthode d'affichage de l'addition
     def showadd(self):
      
         return"la somme de deux vecteurs V3(" +str(self.x)+","+str(self.y)+")"
#instanciez V0,V1,V2 et les afficher
print("le vecteur V0")
V0= vecteur2D()
V0.display()
print("le vecteur V1")
V1= vecteur2D(4,3)
V1.display()
print("le vecteur V2")
V2= vecteur2D(7,5)
V2.display()
#additoner les deus vecteurs
V3=V1+V2
#afficher la somme
print(V3.showadd())