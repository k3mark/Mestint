
class kancso_feladat:
    def __init__(self, ke, c):
        self.kezdo = ke
        self.cel = c
        self.Max1 = 3
        self.Max2 = 5
        self.Max3 = 8

    def celteszt(self, allapot):
        return allapot[1] == self.cel or allapot[2] == self.cel

    def rakovetkezo(self, allapot):
        a1,a2,a3 = allapot
        gyerekek = []

        #tolt 1->2
        if a1 != 0 and a2 != self.Max2:
            T = min(a1, self.Max2-a2)
            uj_allapot = (a1-T, a2+T,a3)
            gyerekek.append(("1->2", uj_allapot))

        # tolt 1->3
        if a1 != 0 and a3 != self.Max2:
            T = min(a1, self.Max3 - a3)
            uj_allapot = (a1 - T, a2 , a3+T)
            gyerekek.append(("1->3", uj_allapot))

        # tolt 2->1
        if a2 != 0 and a1 != self.Max1:
            T = min(a2, self.Max1 - a1)
            uj_allapot = (a1 +T, a2 - T, a3)
            gyerekek.append(("2->1", uj_allapot))

        # tolt 2->3
        if a2 != 0 and a3 != self.Max3:
            T = min(a2, self.Max3 - a3)
            uj_allapot = (a1, a2 - T, a3+T)
            gyerekek.append(("2->3", uj_allapot))

        # tolt 3->1
        if a3 != 0 and a1 != self.Max1:
            T = min(a3, self.Max1 - a1)
            uj_allapot = (a1 + T, a2 , a3-T)
            gyerekek.append(("3->1", uj_allapot))

        # tolt 3->2
        if a3 != 0 and a2 != self.Max2:
            T = min(a3, self.Max2 - a2)
            uj_allapot = (a1, a2 + T, a3-T)
            gyerekek.append(("3->2", uj_allapot))

        return gyerekek

    def rekovetkezo2(self,allapot):
        a1, a2, a3=allapot
        gyerekek=[]
        korsok = [a1, a2, a3]
        maxok = [self.Max1, self.Max2, self.Max3]

        for honnan in range(0,3):
            for hova in range(0,3):
                if korsok[honnan]!=0 and korsok[hova]!=maxok[hova] and korsok[honnan]!=korsok[hova]:
                    T=min(korsok[honnan], maxok[hova]-korsok[hova])
                    uj_allapot = list(korsok)
                    uj_allapot[honnan] -= T
                    uj_allapot[hova] += T
                    gyerekek.append((f"{honnan + 1}->{hova + 1}", tuple(uj_allapot)))

        return gyerekek



if __name__ == "__main__":
    kancso_problema = kancso_feladat((0,0,8), 4)