from JeuDeCarte import *
from carte import *

class Joueur():
    def __init__(self,nom,nbCartes):
        self.nom = nom
        self.nbCartes = nbCartes
        self.mainJoueur = []

    def setMain(self,main):
        self.mainJoueur = main
        self.nbCartes=len(self.mainJoueur)

    def getNom(self):
        return self.nom

    def getNbCartes(self):
        return self.nbCartes

    def jouerCarte(self):
        if len(self.mainJoueur)>0:
            c= self.mainJoueur[0]
            del self.mainJoueur[0]
            self.nbCartes-=1
            return c
        else:
            return None

    def insererMain(self,listecarte):
        self.mainJoueur += listecarte
        self.nbCartes = len(self.mainJoueur)


def testJoueur():
    J1=Joueur('bob',5)
    J2=Joueur('Kane',6)
    print ("J1 NBC: ",J1.getNbCartes(), "nom: ",J1.getNom())
    print ("J2 NBC: ",J2.getNbCartes(), "nom: ",J2.getNom())





testJoueur()




