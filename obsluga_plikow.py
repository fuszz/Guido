import akord
import dzwiek
import partytura
import tonacja
import string
from typing import TextIO


class BladWNaglowku(Exception):
    def __init__(self):
        self.wiadomosc: str = "Błąd w nagłówku pliku. Czy wejście jest poprawne?"

    def __str__(self):
        return self.wiadomosc


class BladWCiele(Exception):
    def __init__(self):
        self.wiadomosc: str = "Błąd w ciele. Czy wejście jest poprawne?"

    def __str__(self):
        return self.wiadomosc


def utworz_partyture(plik: TextIO) -> partytura.Partytura:
    try:
        nowe_metrum: str = None
        nowa_tonacja: tonacja.Tonacja = None
        nowa_liczba_taktow: int = None
        while nowe_metrum is None or nowa_tonacja is None or nowa_liczba_taktow is None:
            linia = plik.readline()
            (klucz, wartosc) = linia.split(":")
            klucz = klucz.replace('\n', '').replace(' ', '')
            wartosc = wartosc.replace('\n', '').replace(' ', '')
            if klucz == "metrum":
                nowe_metrum = wartosc
            elif klucz == "tonacja":
                nowa_tonacja = tonacja.Tonacja(wartosc)
            elif klucz == "takty":
                nowa_liczba_taktow = int(wartosc)
        if nowe_metrum is not None and nowa_tonacja is not None and nowa_liczba_taktow is not None:
            return partytura.Partytura(nowa_tonacja, nowe_metrum, nowa_liczba_taktow)
        else:
            raise BladWNaglowku
    except:
        raise BladWNaglowku


def wypelnij_partyture_akordami(plik: TextIO, nowa_partytura: partytura.Partytura) -> partytura.Partytura:
    try:
        for linia in plik:
            linia = linia.replace(' ', '').replace('\n', '')
            if linia == "T":
                nowa_partytura.zakoncz_takt()
            else:
                podane_dzwieki = linia.split(',')
                dzwiek_sopranu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[0][-1]), podane_dzwieki[0][0:-1].strip())
                dzwiek_altu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[1][-1]), podane_dzwieki[1][0:-1].strip())
                dzwiek_tenoru: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[2][-1]), podane_dzwieki[2][0:-1].strip())
                dzwiek_basu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[3][-1]), podane_dzwieki[3][0:-1].strip())
                nowy_akord: akord.Akord = akord.Akord(dzwiek_sopranu, dzwiek_altu, dzwiek_tenoru, dzwiek_basu,
                                                  float(podane_dzwieki[4]))
                nowa_partytura.dodaj_akord(nowy_akord)
        return nowa_partytura
    except:
        raise BladWCiele


def odczytuj_plik(sciezka_do_pliku: str) -> partytura.Partytura:
    try:
        with open(sciezka_do_pliku, "r") as plik_wejsciowy:
            nowa_partytura: partytura.Partytura = utworz_partyture(plik_wejsciowy)
            nowa_partytura = wypelnij_partyture_akordami(plik_wejsciowy, nowa_partytura)
            if not nowa_partytura.czy_poprawna_liczba_taktow():
                raise ValueError("Blednie podane akordy")
        return nowa_partytura
    except BladWNaglowku:
        print("Błędny nagłówek pliku wejściowego. Niemożliwe utworzenie partytury.")
        raise ValueError("Niepoprawne wczytanie danych. Problem z nagłówkiem pliku.")
    except BladWCiele:
        print("Niepoprawnie podana zawartość partytury. Utworzona partytura jest wadliwa.")
        raise ValueError("Niepoprawne wczytanie danych. Problem z ciałem pliku.")