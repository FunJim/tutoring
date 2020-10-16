couleurs = ('CARREAU','COEUR','TREFLE','PIQUE')
noms = ['2','3','4','5','6','7','8','9','10','Valet','Dame','Roi','As']
valeurs = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Valet':11,'Dame':12,'Roi':13,'As':14}

class Carte:
    def __init__ (self,nom,couleur):
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeurs.get(nom)

    def setNom(self,nom):
        self.nom = nom
        self.valeur = valeurs.get(nom)


    def getNom(self):
        return self.nom

    def getCouleur(self):
        return self.couleur

    def getValeur(self):
        return self.valeur



    def eagalite(self,carte):
        if self.valeur == self.carte:
            return true.self
        else:
            return false.self

    def estSuperieureA(self,carte):
        if self.valeur > self.carte:
            return true.self
        else:
            return false.self

    def estInterieureA(self,carte):
        if self.valeur < self.carte:
            return true.self
        else:
            return false.self



##def testCarte():
##    valetCoeur = Carte('Valet','COEUR')
##    print('nom:',valetCoeur.getNom())
##    print('Couleur:',valetCoeur.getCouleur())
##    print('Valeur:',valetCoeur.getValeur())
##    valetCoeur.setNom('Dame')
##    print('Nom modifie:',valetCoeur.getNom())
##    print('Valeur modifiee:',valetCoeur.getValeur())
##
##
##    dameCarreau = Carte('Dame','COooEUR')
##
##testCarte()



