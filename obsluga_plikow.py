import akord
import dzwiek
import partytura
import tonacja
from enumerations import enum_metrum, enum_bledy, enum_wartosci_nut
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


def utworz_partyture(plik: TextIO) -> partytura.Partytura:  # Skończone :)
    try:
        oznaczenie_metrum: str = plik.readline().replace('\n', '').replace(' ', '')
        liczba_taktow: int = int(plik.readline().replace('\n', '').replace(' ', ''))
        nazwa_tonacji: str = plik.readline().replace('\n', '').replace(' ', '')
        nowa_tonacja: tonacja.Tonacja = tonacja.Tonacja(nazwa_tonacji)
        nowe_metrum: enum_metrum.Metrum = enum_metrum.Metrum(oznaczenie_metrum)
        return partytura.Partytura(nowa_tonacja, nowe_metrum, liczba_taktow)

    except enum_bledy.BladTworzeniaTonacji:
        raise enum_bledy.BladWczytywaniaZPliku("Sprawdź, czy poprawnie podałeś nazwę tonacji.")
    except enum_bledy.BladTworzeniaMetrum:
        raise enum_bledy.BladWczytywaniaZPliku("Sprawdź, czy poprawnie oznaczyłeś metrum.")
    except enum_bledy.BladTworzeniaPartytury:
        raise enum_bledy.BladWczytywaniaZPliku("Sprawdź, czy liczba taktów jest poprawna (co najmniej 1)")
    except IOError:
        raise enum_bledy.BladWczytywaniaZPliku("Nieznany błąd pliku. Sprawdź plik i spróbuj ponownie")


def wypelnij_partyture_akordami(plik: TextIO, nowa_partytura: partytura.Partytura) -> partytura.Partytura:
    licznik_linii: int = 4  # Licznik linii umożliwi bardziej szczegółowe informowanie o miejscu wystąpienia błędu
    #                         Pierwsze 3 linie były poświęcone na nagłówek pliku, zaczynamy od linii 4.
    try:
        for linia in plik:
            linia = linia.replace(' ', '').replace('\n', '')
            if linia == "T":
                nowa_partytura.zakoncz_takt()
                print("T")
            else:
                podane_dzwieki = linia.split(',')
                dzwiek_sopranu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[0][-1]),
                                                              podane_dzwieki[0][0:-1].strip())
                dzwiek_altu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[1][-1]), podane_dzwieki[1][0:-1].strip())

                dzwiek_tenoru: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[2][-1]),
                                                             podane_dzwieki[2][0:-1].strip())
                dzwiek_basu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[3][-1]), podane_dzwieki[3][0:-1].strip())
                wartosc: enum_wartosci_nut = enum_wartosci_nut.WartosciNut(int(podane_dzwieki[4]))
                nowy_akord: akord.Akord = akord.Akord(dzwiek_sopranu, dzwiek_altu, dzwiek_tenoru, dzwiek_basu, wartosc)
                nowa_partytura.dodaj_akord(nowy_akord)
                licznik_linii += 1
        return nowa_partytura

    except enum_bledy.BladTworzeniaDzwieku:
        raise enum_bledy.BladWczytywaniaZPliku("Nieudane utworzenie dźwięku z zapisu linii " + str(licznik_linii) + ".")
    except enum_bledy.BladTworzeniaAkordu:
        raise enum_bledy.BladWczytywaniaZPliku("Nieudane utworzenie akordu z zapisu linii " + str(licznik_linii) + ".")
    except IndexError:
        raise enum_bledy.BladWczytywaniaZPliku("Niepoprawna struktura linijki " + str(licznik_linii) + ".")
    except TypeError:
        raise enum_bledy.BladWczytywaniaZPliku("TypeError - zastosowano niewłaściwy typ" + str(licznik_linii) + ".")
    except ValueError:
        raise enum_bledy.BladWczytywaniaZPliku("ValueError - nieprawidłowa wartość" + str(licznik_linii) + ".")


def wczytaj_z_pliku(sciezka_do_pliku: str) -> partytura.Partytura:
    try:
        with open(sciezka_do_pliku, "r") as plik_wejsciowy:
            nowa_partytura: partytura.Partytura = utworz_partyture(plik_wejsciowy)
            nowa_partytura = wypelnij_partyture_akordami(plik_wejsciowy, nowa_partytura)

    except FileNotFoundError:  # Plik nie istnieje
        raise enum_bledy.BladWczytywaniaZPliku("Plik wskazany do wczytania partytury nie istnieje.")
    except PermissionError:  # Brak permisji do odczytu pliku
        raise enum_bledy.BladWczytywaniaZPliku("Brak uprawnień do odczytu wskazanego pliku.")

    if not nowa_partytura.czy_poprawna_liczba_taktow():
        raise enum_bledy.BladListyAkordow("Błędna liczba taktów w partyturze. Podaj poprawną liczbę taktów w pliku.")
    return nowa_partytura
