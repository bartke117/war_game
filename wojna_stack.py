from random import shuffle
from time import sleep

karty = {"dwójka karo": 2, "dwójka pik": 2, "dwójka trefl": 2, "dwójka kier": 2,
         "trójka karo": 3, "trójka pik": 3, "trójka trefl": 3, "trójka kier": 3,
         "czwórka karo": 4, "czwórka pik": 4, "czwórka trefl": 4, "czwórka kier": 4,
         "piątka karo": 5, "piątka pik": 5, "piątka trefl": 5, "piątka kier": 5,
         "szóstka karo": 6, "szóstka pik": 6, "szóstka trefl": 6, "szóstka kier": 6,
         "siódemka karo": 7, "siódemka pik": 7, "siódemka trefl": 7, "siódemka kier": 7,
         "ósemka karo": 8, "ósemka pik": 8, "ósemka trefl": 8, "ósemka kier": 8,
         "dziewiątka karo": 9, "dziewiątka pik": 9, "dziewiątka trefl": 9, "dziewiątka kier": 9,
         "dziesiątka karo": 10, "dziesiątka pik": 10, "dziesiątka trefl": 10, "dziesiątka kier": 10,
         "walet karo": 11, "walet pik": 11, "walet trefl": 11, "walet kier": 11,
         "dama karo": 12, "dama pik": 12, "dama trefl": 12, "dama kier": 12,
         "król karo": 13, "król pik": 13, "król trefl": 13, "król kier": 13,
         "as karo": 14, "as pik": 14, "as trefl": 14, "as kier": 14,
         }


class StosKart:
    """
    Klasa StosKart, która w konstruktorze zamienia powyższy słownik kart (kluczem jest karta a wartością jej moc) na listę kart.
    Posiada metodę tasuj, która tasuje listę kart wykorzystując metodę shuffle z biblioteki random,
    oraz metodę 'talia_na_pol', która dzieli potasowaną talię (listę kart) na pół, po 26 kart każda.

    """

    def __init__(self, karty):
        print("""\n 
         ██████╗ ██████╗  █████╗     ██╗    ██╗    ██╗    ██╗ ██████╗      ██╗███╗   ██╗███████╗
        ██╔════╝ ██╔══██╗██╔══██╗    ██║    ██║    ██║    ██║██╔═══██╗     ██║████╗  ██║██╔════╝
        ██║  ███╗██████╔╝███████║    ██║ █╗ ██║    ██║ █╗ ██║██║   ██║     ██║██╔██╗ ██║█████╗  
        ██║   ██║██╔══██╗██╔══██║    ██║███╗██║    ██║███╗██║██║   ██║██   ██║██║╚██╗██║██╔══╝  
        ╚██████╔╝██║  ██║██║  ██║    ╚███╔███╔╝    ╚███╔███╔╝╚██████╔╝╚█████╔╝██║ ╚████║███████╗
         ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝      ╚══╝╚══╝  ╚═════╝  ╚════╝ ╚═╝  ╚═══╝╚═══██═╝
                                                                                        """)
        print("Tworzenie talii kart...")
        self.wszystkie_karty = list(karty.items())
        # sleep(1)

    def tasuj(self):
        print("Tasowanie talii kart...")
        shuffle(self.wszystkie_karty)
        # sleep(1)
        print()

    def talia_na_pol(self):
        return self.wszystkie_karty[:26], self.wszystkie_karty[26:]


class Reka:
    """
    Klasa Ręka z kartami każdego gracza jako implementacja stosów,
    metoda 'dodaj_karte' i 'usun_karte' analogia do push i pop
    """
    def __init__(self, karty):
        self.karty = karty

    def dodaj_karte(self, dodane_karty):
        self.karty.extend(dodane_karty)

    def usun_karte(self):
        return self.karty.pop(0)


class Gracz:
    """
    Klasa Gracz zawierająca pole z imieniem gracza, oraz pole z ręką w której znajdują się karty gracza(lista),
    metodą 'graj' służącą do pobrania karty i wyłożenia jej na stół,
    metodą 'zbierz_wojna', umożliwającą zebranie kart wygranych w czasie
    trwania wojny (wojna inicjuje się gdy obaj gracze wyłożą karty o tej samej randze),
    metodą 'posiada_karty', sprawdzającą czy gracz ma jeszcze jakieś karty w ręce.
    """

    def __init__(self, imie, reka):
        self.imie = imie
        self.reka = reka

    def graj(self):
        dobierz_karte = self.reka.usun_karte()
        print("{} wyłożył: {}".format(self.imie, dobierz_karte[0]))
        return dobierz_karte

    def zbierz_wojna(self):
        wojna = []
        if len(self.reka.karty) < 3:
            return wojna
        else:
            for x in range(3):
                wojna.append(self.reka.karty.pop())
            return wojna

    def posiada_karty(self):
        return len(self.reka.karty) != 0


def main():
    d = StosKart(karty)
    d.tasuj()
    talia1, talia2 = d.talia_na_pol()

    print("Gracz nr 1")
    gracz1 = Gracz(input("Jak masz na imię? "), Reka(talia1))

    print("Gracz nr 2")
    gracz2 = Gracz(input("Jak masz na imię? "), Reka(talia2))

    rundy = 0
    wojna_rundy = 0

    while gracz1.posiada_karty() and gracz2.posiada_karty():
        rundy += 1
        # sleep(3)
        print(f"\nRozpoczynamy {rundy}. rundę!")
        print("Aktualna klasyfikacja graczy: ")
        print(gracz1.imie + " - liczba kart: " + str(len(gracz1.reka.karty)))
        print(gracz2.imie + " - liczba kart: " + str(len(gracz2.reka.karty)))
        print("\nGracze wykładają kartę!")

        # lista reprezentująca karty znajdujące się na placu gry
        plac_gry = []
        g1_karty = gracz1.graj()
        g2_karty = gracz2.graj()

        # dodanie kart obu graczy do placu gry
        plac_gry.append(g1_karty)
        plac_gry.append(g2_karty)

        # sprawdzenie czy wojna
        if g1_karty[1] == g2_karty[1]:
            if len(gracz1.reka.karty) < 4 or len(gracz2.reka.karty) < 4:
                break
            wojna_rundy += 1
            print("\nGracze wyłożyli takie same karty, czas na WOJNĘ!")
            print("Każdy gracz kładzie 3 karty twarzą do dołu i jedną twarzą do góry!\n")
            plac_gry.extend(gracz1.zbierz_wojna())
            plac_gry.extend(gracz2.zbierz_wojna())

            # wyłożenie karty na stół (usunięcie z ręki i dodanie do placu gry)
            g1_karty = gracz1.graj()
            g2_karty = gracz2.graj()

            plac_gry.append(g1_karty)
            plac_gry.append(g2_karty)

            # sprawdzenie kto miał wyższą kartę
            if karty[g1_karty[0]] > karty[g2_karty[0]]:
                print(gracz1.imie + " ma wyższą kartę i zabiera karty przeciwnika do swojej talii.")
                gracz1.reka.dodaj_karte(plac_gry)
            else:
                print(gracz2.imie + " ma wyższą kartę i zabiera karty przeciwnika do swojej talii.")
                gracz2.reka.dodaj_karte(plac_gry)

        else:
            if karty[g1_karty[0]] > karty[g2_karty[0]]:
                print(gracz1.imie + " ma wyższą kartę i zabiera kartę przeciwnika do swojej talii.")
                gracz1.reka.dodaj_karte(plac_gry)
            else:
                print(gracz2.imie + " ma wyższą kartę i zabiera kartę przeciwnika do swojej talii.")
                gracz2.reka.dodaj_karte(plac_gry)

    if len(gracz1.reka.karty) > len(gracz2.reka.karty):
        print(f"\n═══ Koniec gry! {gracz1.imie} zwycięża! ═══ ".upper())
    elif len(gracz1.reka.karty) < len(gracz2.reka.karty):
        print(f"\n═══ Koniec gry! {gracz2.imie} zwycięża! ═══ ".upper())
    else:
        print(f"\n═══ Koniec gry! Gra kończy się remisem! ═══ ".upper())
    print(f"\nLiczba rund jaką rozegrano: {str(rundy)}")
    if wojna_rundy <= 1:
        print(f"Do wojny doszło {str(wojna_rundy)} raz.")
    else:
        print(f"Do wojny doszło {str(wojna_rundy)} razy.")


if __name__ == "__main__":
    main()
