import random
import time
import copy

talia_kart = ["11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

pula_kart = []
karty_gracza = []
karty_przeciwnika = []

def tasowanie_kart():
    tmp_pula_kart = copy.deepcopy(talia_kart)
    random.shuffle(tmp_pula_kart)
    print("karty zostaly potasowane!")
    return tmp_pula_kart

def pobierz_karte():
    return pula_kart.pop(0)

def dobierz_karte(ziomek):
    karta = pobierz_karte()
    ziomek.append(karta)

def obliczanie_punktow(ziomek, ukryta=False):
    if ukryta:
        return sum(int(karta) for karta in ziomek[1:])
    return sum(int(karta) for karta in ziomek)

def pokaz_karty(ziomek, ukryta=False):
    if ukryta:
        return "?, " + ", ".join(map(str, ziomek[1:])) if len(ziomek) > 1 else "?"
    return ", ".join(map(str, ziomek))

def wybor_ruchu():
    while True:
        ruch = input("co robisz? (hit/stay): ").lower()
        if ruch in ["hit", "stay"]:
            return ruch == "hit"
        print("chyba jestes autysta")


def dzialania_przeciwnika():
    while obliczanie_punktow(karty_przeciwnika) < 16:
        time.sleep(1)
        print(f"przeciwnik wzial karte: {pokaz_karty(karty_przeciwnika, ukryta=True)}, punkty: {obliczanie_punktow(karty_przeciwnika)}")
        time.sleep(1)
    print("koniec ruchu przeciwnika")


def __main__():
    global karty_gracza, karty_przeciwnika
    global pula_kart
    pula_kart = tasowanie_kart()
    time.sleep(1)

    karty_gracza = [pobierz_karte(), pobierz_karte()]
    karty_przeciwnika = [pobierz_karte(), pobierz_karte()]

    print(f"twoje karty: {pokaz_karty(karty_gracza)}, punkty: {obliczanie_punktow(karty_gracza)}")
    print(f"karty przeciwnika: {pokaz_karty(karty_przeciwnika, ukryta=True)}, punkty: niewiadoma + {obliczanie_punktow(karty_przeciwnika, ukryta=True)}")

    gracz_zakonczyl = False
    przeciwnik_zakonczyl = False

    while not (gracz_zakonczyl and przeciwnik_zakonczyl):

        if not gracz_zakonczyl:
            if wybor_ruchu():
                dobierz_karte(karty_gracza)
                print(f"twoje karty: {pokaz_karty(karty_gracza)}, punkty: {obliczanie_punktow(karty_gracza)}")
                time.sleep(1)
            else:
                print("zakonczyles swoj ruch")
                gracz_zakonczyl = True

        if not przeciwnik_zakonczyl:
            if obliczanie_punktow(karty_przeciwnika) < 16:
                dobierz_karte(karty_przeciwnika)
                print(f"przeciwnik dobral karte: {pokaz_karty(karty_przeciwnika, ukryta=True)}, punkty: niewiadoma + {obliczanie_punktow(karty_przeciwnika, ukryta=True)}")
                time.sleep(1)
            else:
                print(f"przeciwnik wybiera stay, punkty: niewiadoma + {obliczanie_punktow(karty_przeciwnika, ukryta=True)}")
                przeciwnik_zakonczyl = True

    time.sleep(1)
    print("koniec gry!!")
    time.sleep(1)
    print(f"twoje karty: {pokaz_karty(karty_gracza)}, punkty: {obliczanie_punktow(karty_gracza)}")
    time.sleep(1)
    print(f"karty przeciwnika: {pokaz_karty(karty_przeciwnika)}, punkty: {obliczanie_punktow(karty_przeciwnika)}")
    time.sleep(1)

    if obliczanie_punktow(karty_gracza) > 21:
        print("LLL bust")
    elif obliczanie_punktow(karty_przeciwnika) > 21:
        print("przciwnik mial tak zwany bust!")
    elif obliczanie_punktow(karty_gracza) > obliczanie_punktow(karty_przeciwnika):
        print("www sigma")
    elif obliczanie_punktow(karty_gracza) < obliczanie_punktow(karty_przeciwnika):
        print("LLLL przegrales")
    else:
        print("remis")

    time.sleep(1)
    nowa = input("chcesz jeszcze raz (tak/nie) (zostaniesz hazardzista!): ").lower()
    if nowa == "tak":
        __main__()
    elif nowa == "nie":
      print("a to nara")
    else:
       print("no niepelnosprytny")


__main__()
