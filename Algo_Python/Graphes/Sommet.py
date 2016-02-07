import Arete

class Sommet:
    def __init__(self , val):
        self.val = val
        self.suivants = {}

    def ajout_suivant(self , sommet , poids):
        self.suivants[sommet] = poids

    def afficher(self):
        print str(self.val) + " : "
        for s in self.suivants:
            print "--" + str(s.val) + " : " + str(self.suivants[s])