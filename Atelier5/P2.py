class étudiant:
      def __init__(self, nom, prenom , age, CNE, moyenne):
               self.n = nom
               self.p = prenom
               self.a = age
               self.c = CNE
               self.m = moyenne
     # creating list
list = []
# appending instances to list
list.append( étudiant('Ellas', 'Imane', 20, 'P124', 15) )
list.append( étudiant('Oula','Anas', 21,'P367', 19 ) )
list.append( étudiant('Ramze','Ilyas', 22,  'P145', 12 ) )
for obj in list:
  print( obj.n, obj.p, obj.a, obj.c, obj.m, sep =' ' )
  print("***la liste trier par age***\n")
list.sort(key=lambda x: x.a)
for obj in list:
     print( "nom: ",obj.n," prenom: " ,obj.p," age: " ,obj.a," cne: ",obj.c," moyenne: ",obj.m ,sep =' ' )
print("\n")
#afficher la liste trier par moyenne
print("***la liste trier par moyenne***\n")
list.sort(key=lambda x: x.m)
for obj in list:
      print( "nom: ",obj.n," prenom: " ,obj.p," age: " ,obj.a," cne: ",obj.c," moyenne: ",obj.m ,sep =' ' )

