import random
import time

znaczki = ["♣", "♦", "♥", "♠"]
wartosci = ["11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

karty_gracza = []
karty_przeciwnika = []

def stworz_talie():
    talia = [(wartosc, znaczek) for wartosc in wartosci for znaczek in znaczki]
    random.shuffle(talia)
    return talia

def pobierz_karte(talia):
    return talia.pop(0)

def dobierz_karte_gracz(talia):
    karta = pobierz_karte(talia)
    karty_gracza.append(karta)

def dobierz_karte_przeciwnik(talia):
    karta = pobierz_karte(talia)
    karty_przeciwnika.append(karta)

def obliczanie_punktow(ziomek):
    suma = 0
    for karta in ziomek:
        wartosc = karta[0]
        suma += int(wartosc)
    return suma

def pokaz_karty(ziomek):
    return " ".join(f"{wartosc}{znaczek}" for wartosc, znaczek in ziomek)

def wybor_ruchu():
    while True:
        ruch = input("jaki ruch robisz? (hit/stay): ").lower()
        if ruch == "hit":
            return True
        elif ruch == "stay":
            return False
        else:
            print("cos nie tak kolezko!")

def wykonaj_ruch(talia):
    while True:
        decyzja = wybor_ruchu()
        if decyzja:
            dobierz_karte_gracz(talia)
            print(f"twoje karty: {pokaz_karty(karty_gracza)}, punkty: {obliczanie_punktow(karty_gracza)}")
            if obliczanie_punktow(karty_gracza) > 21:
                print("bust tak zwany")
                return
        else:
            break

def dzialania_przeciwnika(talia):
    while obliczanie_punktow(karty_przeciwnika) < 16:
        dobierz_karte_przeciwnik(talia)
        print(f"przeciwnik wzial karte: {pokaz_karty(karty_przeciwnika)[1:]}, punkty: {obliczanie_punktow(karty_przeciwnika)}")
    print("koniec ruchu przeciwnika")

def __main__():
    global karty_gracza, karty_przeciwnika

    talia = stworz_talie()

    karty_gracza = [pobierz_karte(talia), pobierz_karte(talia)]
    karty_przeciwnika = [pobierz_karte(talia), pobierz_karte(talia)]

    print(f"gracz posiada karte {pokaz_karty([karty_gracza[0]])} i jedną karte nieznana")
    print(f"to twoje karty: {pokaz_karty(karty_gracza)}, punkty {obliczanie_punktow(karty_gracza)}")
    print(f"przeciwnik posiada karte {pokaz_karty([karty_przeciwnika[0]])} i jedna karte nieznana")

    wykonaj_ruch(talia)
    dzialania_przeciwnika(talia)

    print(f"to twoje karty: {pokaz_karty(karty_gracza)}, punkty: {obliczanie_punktow(karty_gracza)}")
    print(f"karty przeciwnika: {pokaz_karty(karty_przeciwnika)}, punkty: {obliczanie_punktow(karty_przeciwnika)}")

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

__main__()
