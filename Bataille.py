from JeuDeCarte import *
from carte import *
from Joueur import *

class Bataille():
    def __init__(self):
        # Instancier un jeu de carte
        # melanger les cartes
        self.jeu = JeuCartes(52)
        self.jeu.creerJeu()
        self.jeu.melanger()

    def jouer(self, nbTours):
        # Distribution de 26 cartes à 2 joueurs
        distribution_2j_26c = self.jeu.distribuerJeu(2, 26)

        # Creer 2 joueurs
        joueur1=Joueur('Joueur1',26)
        listeCartes1=distribution_2j_26c[0]
        joueur1.setMain(listeCartes1)

        joueur2=Joueur('Joueur2',26)
        listeCartes2=distribution_2j_26c[1]
        joueur2.setMain(listeCartes2)

        # Debut du jeu
        print('Debut: ', joueur1.getNbCartes(), joueur2.getNbCartes())

        # Jouer nbTours tours
        for i in range(nbTours):
            carte_joueur1 = joueur1.jouerCarte()
            carte_joueur2 = joueur2.jouerCarte()

            print('La carte du jouer', joueur1.getNom(), 'est:', carte_joueur1.getNom(), 'de', carte_joueur1.getCouleur())
            print('La carte du jouer', joueur2.getNom(), 'est:', carte_joueur2.getNom(), 'de', carte_joueur2.getCouleur())

            # Si la carte de joueur 1 est plus fort que celle de joueur 2
            # Joueur 1 recupere sa carte ainsi que la carte de joueur 2
            if carte_joueur1.estSuperieureA(carte_joueur2):
                print('Le joueur', joueur1.getNom(), 'a gagne ce tour')
                joueur1.insererMain([carte_joueur1, carte_joueur2])
            # Si la carte de joueur 1 est moins fort que celle de joueur 2
            # Joueur 2 recupere sa carte ainsi que la carte de joueur 1
            elif carte_joueur1.estInferieureA(carte_joueur2):
                print('Le joueur', joueur2.getNom(), 'a gagne ce tour')
                joueur2.insererMain([carte_joueur1, carte_joueur2])
            # Si l'egalite des cartes de deux joueurs
            # Chacun recupere sa carte
            elif carte_joueur1.egalite(carte_joueur2):
                print('Egalite!')
                joueur1.insererMain([carte_joueur1])
                joueur2.insererMain([carte_joueur2])

            print('Nombre de carte en sortie du dernier coup:')
            print('NbCarte de', joueur1.getNom(), joueur1.getNbCartes())
            print('NbCarte de', joueur2.getNom(), joueur2.getNbCartes())

            # Fin du jeu si l'un des joueurs n'a plus de carte
            if joueur1.getNbCartes() == 0 or joueur2.getNbCartes() == 0:
                print('Fin du jeu !')
                break


bataille = Bataille()
# Jouer 10 tours
bataille.jouer(10)

