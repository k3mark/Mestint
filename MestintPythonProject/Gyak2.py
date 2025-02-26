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
        return allapot


if __name__ == "__main__":
    kancso_problema = kancso_feladat((0,0,8), 4)