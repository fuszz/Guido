import akord
import dzwiek
import partytura
import tonacja
import blad
from enumerations import enum_metrum, enum_wartosci_nut
from typing import TextIO


# NIE TYKAĆ!!!

def utworz_partyture(plik: TextIO) -> partytura.Partytura:
    try:
        linia: str = plik.readline().replace('\n', '').replace(' ', '')
        nowe_metrum: enum_metrum.Metrum = enum_metrum.Metrum(linia)
    except blad.BladTworzeniaMetrum:
        raise blad.BladWczytywaniaZPliku("Niepoprawne metrum")
    except IOError:
        raise blad.BladWczytywaniaZPliku("Nieznany błąd pliku. Sprawdź plik")

    try:
        nowa_liczba_taktow: int = int(plik.readline().replace('\n', '').replace(' ', ''))
        if nowa_liczba_taktow < 1:
            raise blad.BladWczytywaniaZPliku("Niepoprawna liczba taktów")
    except (blad.BladTworzeniaMetrum, ValueError, TypeError):
        raise blad.BladWczytywaniaZPliku("Niepoprawna liczba taktów")
    except IOError:
        raise blad.BladWczytywaniaZPliku("Nieznany błąd pliku. Sprawdź plik")

    try:
        linia: str = plik.readline().replace('\n', '').replace(' ', '')
        nowa_tonacja: tonacja.Tonacja = tonacja.Tonacja.tonacja_z_symbolu(linia)
    except blad.BladTworzeniaTonacji:
        raise blad.BladWczytywaniaZPliku("Niepoprawna nazwa tonacji")
    except IOError:
        raise blad.BladWczytywaniaZPliku("Nieznany błąd pliku. Sprawdź plik")

    return partytura.Partytura(nowa_tonacja, nowe_metrum, nowa_liczba_taktow)


def wypelnij_partyture_akordami(plik: TextIO, nowa_partytura: partytura.Partytura) -> partytura.Partytura:
    licznik_linii: int = 4  # Licznik linii umożliwi bardziej szczegółowe informowanie o miejscu wystąpienia błędu
    #                         Pierwsze 3 linie były poświęcone na nagłówek pliku, zaczynamy od linii 4.

    for linia in plik:
        linia = linia.replace(' ', '').replace('\n', '')
        if linia == "T":
            nowa_partytura.zakoncz_takt()
        else:
            try:
                podane_dzwieki = linia.split(',')
                dzwiek_sopranu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[0][-1]),
                                                              podane_dzwieki[0][0:-1].strip())
                dzwiek_altu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[1][-1]),
                                                           podane_dzwieki[1][0:-1].strip())
                dzwiek_tenoru: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[2][-1]),
                                                             podane_dzwieki[2][0:-1].strip())
                dzwiek_basu: dzwiek.Dzwiek = dzwiek.Dzwiek(int(podane_dzwieki[3][-1]),
                                                           podane_dzwieki[3][0:-1].strip())

            except blad.BladTworzeniaDzwieku:
                raise blad.BladWczytywaniaZPliku("Niepoprawny dźwięk w linii " + str(licznik_linii) + ".")
            except IndexError:
                raise blad.BladWczytywaniaZPliku("Niepoprawna struktura linii " + str(licznik_linii) + ".")
            except TypeError:
                raise blad.BladWczytywaniaZPliku(
                    "TypeError - zastosowano niewłaściwy typ" + str(licznik_linii) + ".")

            try:
                wartosc: enum_wartosci_nut = enum_wartosci_nut.WartosciNut(int(podane_dzwieki[4]))
            except (ValueError, TypeError):
                raise blad.BladWczytywaniaZPliku(
                    "Niepoprawna długość dźwięku w linii " + str(licznik_linii) + ".")

            try:
                nowy_akord: akord.Akord = akord.Akord(dzwiek_sopranu, dzwiek_altu, dzwiek_tenoru, dzwiek_basu, wartosc)
            except blad.BladTworzeniaAkordu:
                raise blad.BladWczytywaniaZPliku("Uszkodzony akord w linii " + str(licznik_linii) + ".")

            nowa_partytura.dodaj_akord(nowy_akord)
            licznik_linii += 1
    return nowa_partytura


def wczytaj_z_pliku(sciezka_do_pliku: str) -> partytura.Partytura:
    try:
        with open(sciezka_do_pliku, "r") as plik_wejsciowy:
            nowa_partytura: partytura.Partytura = utworz_partyture(plik_wejsciowy)
            nowa_partytura = wypelnij_partyture_akordami(plik_wejsciowy, nowa_partytura)

    except FileNotFoundError:  # Plik nie istnieje
        raise blad.BladWczytywaniaZPliku("Plik nie istnieje")
    except PermissionError:  # Brak permisji do odczytu pliku
        raise blad.BladWczytywaniaZPliku("Brak uprawnień do odczytu wskazanego pliku")

    if not nowa_partytura.czy_poprawna_liczba_taktow():
        raise blad.BladWczytywaniaZPliku("Błędna liczba taktów w partyturze")
    return nowa_partytura
