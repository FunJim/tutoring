from carte import *
import random

class JeuCartes():
    def __init__(self,nbCartes=52):
        self.jeu = []
        self.TailleJeu = nbCartes


    def getTailleJeu(self):
        return self.TailleJeu


    def creerJeu(self):
        listeJeu = []
        for i in range(len(noms)):
            for j in range(len(couleurs)):
                listeJeu.append(Carte(noms[i],couleurs[j]))
        self.jeu = listeJeu


    def getJeu(self):
        return self.jeu


    def melanger(self):
        return random.shuffle(self.jeu)


    def distribuerCarte(self):
        premcarte=self.jeu[0]
        self.jeu.pop(0)
        return premcarte


    def distribuerJeu(self,nbJoueurs,nbCartes):
        Lc = []
        for loop in range(nbJoueurs):
            J = []
            for loop in range(nbCartes):
                J.append(self.distribuerCarte())
            Lc.append(J)
        return Lc



##Fonction de test
##def testJeuCartes():
##    jeu52 = JeuCartes(52)
##    jeu52.creerJeu()
##    print(jeu52.getJeu())
##    print("####################")
##    jeu52.melanger()
##    print("####################")
##    carte=jeu52.distribuerCarte()
##    print("valeur :",carte.getValeur()," couleur : ",carte.getCouleur())
##    print("####################")
##    carte=jeu52.distribuerCarte()
##    print("valeur :",carte.getValeur()," couleur : ",carte.getCouleur())


##
##def testJeuCartes():
##    jeu52 = JeuCartes(52)
##    jeu52.creerJeu()
##    jeu52.melanger()
##    L = jeu52.getJeu()
##
##    carte = L[2] #le 3e carte
##    print('Nom:',carte.getNom())
##    print('Couleur:',carte.getCouleur())
##    print('Valeur:',carte.getValeur())
##
##    # Distribution de 4 cartes à 3 joueurs
##    distribution_3j_4c = jeu52.distribuerJeu(3,4)
##    for i in range(3):
##        print('Joueur',i + 1,':')
##        listeCartes = distribution_3j_4c[i]
##        for c in listeCartes:
##            print(c.getNom(),'de',c.getCouleur())
##
##testJeuCartes()

    # Distribution de 10 cartes à 6 joueurs pour générer une exception(6X10>52)


