import akord
import dzwiek
import partytura
import tonacja
from enumerations import enum_metrum
from typing import TextIO


class BladWNaglowku(Exception):
    def __init__(self):
        self.wiadomosc: str = "Błąd w nagłówku partytury?"

    def __str__(self):
        return self.wiadomosc


class BladWCiele(Exception):
    def __init__(self):
        self.wiadomosc: str = "Błąd w ciele partytury."

    def __str__(self):
        return self.wiadomosc


def utworz_partyture(plik: TextIO) -> partytura.Partytura:
    try:
        nowe_metrum: str = plik.readline().replace('\n', '').replace(' ', '')
        nowa_liczba_taktow: int = int(plik.readline().replace('\n', '').replace(' ', ''))
        nowa_tonacja: str = plik.readline().replace('\n', '').replace(' ', '')
        return partytura.Partytura(tonacja.Tonacja(nowa_tonacja), enum_metrum.Metrum(nowe_metrum), nowa_liczba_taktow)
    except TypeError:
        print("Blad co do naglowka partytury")
        raise BladWNaglowku


def wypelnij_partyture_akordami(plik: TextIO, nowa_partytura: partytura.Partytura) -> partytura.Partytura:
    try:
        for linia in plik:
            linia = linia.replace(' ', '').replace('\n', '')
            if linia == "T":
                nowa_partytura.zakoncz_takt()
            else:
                podane_dzwieki = linia.split(',')

                dzwiek_sopranu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[0][-1]),
                                                              podane_dzwieki[0][0:-1].strip())
                dzwiek_altu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[1][-1]), podane_dzwieki[1][0:-1].strip())
                dzwiek_tenoru: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[2][-1]),
                                                             podane_dzwieki[2][0:-1].strip())
                dzwiek_basu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[3][-1]), podane_dzwieki[3][0:-1].strip())

                nowy_akord: akord.Akord = akord.Akord(dzwiek_sopranu, dzwiek_altu, dzwiek_tenoru, dzwiek_basu,
                                                      int(podane_dzwieki[4]))
                nowa_partytura.dodaj_akord(nowy_akord)
        return nowa_partytura
    except IndexError:
        raise BladWCiele()
    except TypeError:
        raise BladWCiele()


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
