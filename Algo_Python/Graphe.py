import Sommet
import Arete

class Graphe:
    def __init__(self):
        self.sommets = []

    def parcours_djikstra(self , s1 , s2):
        s_min = s1
        poids = 0.0
        sommets_tester = {}
        for s in self.sommets:
            sommets_tester.s = 0.0

        while s_min != s2:
            act_val = 0.0
            for s in sommets_tester:
                if s.key() == s_min:
                    act_val = s.val()
                    break

            for a in s_min.aretes:
                c = a.poids
                s_fin = a.s2
                valeurTab = -1.0
                for s in sommets_tester:
                    if s.key == s_fin:
                        valeurTab = s.val
                        break
                if valeurTab == 0 or valeurTab > act_val + c:
                    valeurTab = act_val + c

        for s in sommets_tester:
            if s.key == s2:
                poids = s.val
                break

        return poids