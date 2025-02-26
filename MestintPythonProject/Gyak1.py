


def leap_year(ev):
    if ev % 4 == 0 and ev % 100 != 0 or ev % 400 == 0:
        return True
    else:
        return False

def leap_year_between(ev1, ev2):
    leap_years = []
    for i in range(ev1,ev2+1):
        if leap_year(i):
            leap_years.append(i)
    return leap_years

def leap_year_between2(ev1, ev2):
    return [i for i in range(ev1,ev2+1) if leap_year(i)]

def even_or_odd():
    while True:
        x = int(input("Kérem a következőt: "))
        if x == 0:
            break
        print("Páros" if x % 2== 0 else "Páratlan")

class Hallgato:
    def __init__(self,n,nk):
        self.nev = n
        self.neptun_kod = nk
        self.jegyek = []

    def add_jegy(self, jegy):
        if 1 <= jegy <= 5:
            self.jegyek.append(jegy)
        else:
            print("Hibás jegy")

    @property
    def atlag(self):
        return sum(self.jegyek)/len(self.jegyek) if self.jegyek else 0

    def __str__(self):
        return f"{self.nev}: ({self.atlag})"

def lista_example():
    my_list = [1,-5, 3]
    print(f"eredeti lista: {my_list}")

    my_list.reverse()
    print(f"fordított lista {my_list}")

    my_list.sort(reverse= True)
    print(f"Csökkenő sorrend {my_list}")

    my_list.sort(reverse=False)
    print(f"Növekvő sorrend {my_list}")

if __name__ == "__main__":
    ##print(f"Szökő év-e: {leap_year(2024)}")
    ##print(f"Szökő évek: {leap_year_between(1888,1910)}")
    ##print(f"Szökő évek: {leap_year_between2(1888, 1910)}")
    ##even_or_odd()

    h = Hallgato("Deb Ella", "TZ23SD")
    h.add_jegy(2)
    h.add_jegy(3)
    print(h)

    print(lista_example())
