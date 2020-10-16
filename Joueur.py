from JeuDeCarte import*
from carte import*

class Joueur():
    def __init___(self,nom,nbCartes):
        self.nom = nom
        self.nbcartes = nbcartes
        self.mainJoueur = []

    def setMain(self,main):
        self.mainJoueur = main

    def getNom(self):
        return self.nom

    def getNbCartes(self):
        return self.nbcartes

    def jouerCarte(self):
        if len(self.mainJoueur)>0:
            c=mainJoueur[0]
            del mainJoueur[0]
            self.nbcartes-=1
            return c
        else:
            return None

    def insererMain(self,listecarte):
        self.listecarte = mainJoueur
        for loop in range(len(mainJoueur)):                   """boucle en fonction du nombre de carte récupérer"""
                                                 """append de chaque carte DANS la main du joueur du joueur"""
                                                         """incremente le nb carte"""


def testJoueur()
    J1=Joueur('bob',5)
    J2=Joueur('Kane',6)
    print ("J1 NBC: ",J1.getNbCartes, "nom: ",J1.getNom)
     print ("J2 NBC: ",J2.getNbCartes, "nom: ",J2.getNom)





testJoueur()




