class Utilisateur():
    def __init__(self):
        self.nom = "INAS"
        self.email = "inasinas@email.com"
        self.mot_de_passe = "Citroen"
        self.genre = "F"
        self.age = 20
class Professeur(Utilisateur):
    def __init__(self):
         Utilisateur.__init__(self)
         self.ppr = "PP"
         self.grade = "x++"
class Module():
    def __init__(self):
         self.nom = "Info"
         self.volume = "x"
         self.semestre = "s4"
         self.mat =matière()
class Etudiant(Utilisateur):
    def __init__(self):
         Utilisateur.__init__(self)
         self.code_massar = "P146789"
class matière():
    def __init__(self):
        self.nom = "Citizen-Band"
        self.pourcentage = 30
