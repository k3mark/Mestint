class Hanoi_problema:
    def __init__(self,ke,c):
        self.kezdo = ke
        self.cel = c


    def celteszt(self,allapot):
        return allapot == self.cel

    def rakovetkezo(self,allapot):
        gyerekek = []

        for melyiket in range(0,3):
            for hova in ['P', 'Q', 'R']:



if __name__ == "__main__":
    h = Hanoi_problema(('P','P','P'), ('R','R','R'))