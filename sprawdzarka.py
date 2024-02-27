import dzwiek
import partytura
import akord
import tonacja
from enumerations import enum_funkcje, enum_krzyzowania_glosow, enum_metrum, enum_niepoprawne_stopnie, enum_przewroty, \
    enum_zdwojony_skladnik, enum_dzwieki_w_skalach
from typing import List


def badanie_objetosci_taktow_w_partyturze(badana_partytura: partytura.Partytura) -> List[int]:
    """Funkcja zwraca pustą listę, jeśli długości taktów są OK.
    Funkcja zwraca listę indeksów znaków kończących takty o niepoprawnej długości.
    Funkcja zwraca ValueError, jeśli jest inny element niż akord lub 'T'"""
    suma = 0
    lista_wyjsciowa = []
    for indeks, element in enumerate(badana_partytura.podaj_liste_akordow()):
        if element == 'T':  # Koniec taktu
            if suma != badana_partytura.podaj_metrum().podaj_pozadana_wartosc_nut_w_takcie():
                lista_wyjsciowa.append(indeks)
            suma = 0

        elif isinstance(element, akord.Akord):
            suma += element.podaj_dlugosc().value
        else:
            raise ValueError
    return lista_wyjsciowa


def badanie_czy_dzwiek_jest_w_tonacji(badany_dzwiek: dzwiek.Dzwiek, badana_tonacja: tonacja.Tonacja) -> bool:
    try:
        badany_dzwiek.podaj_swoj_stopien(badana_tonacja)
        return True
    except ValueError:
        return False


def badanie_wystepowania_dzwiekow_obcych(badana_partytura: partytura.Partytura) -> List[int]:
    """Nie zajmujemy się analizą dźwięków obcych - ich występowanie jest błędem.
    Funkcja zwraca listę indeksów akordów, które zawierają dźwięk obcy"""
    lista_wyjsciowa = []
    for indeks, element in enumerate(badana_partytura.podaj_liste_akordow()):
        if element == 'T':
            continue

        if not (badanie_czy_dzwiek_jest_w_tonacji(element.podaj_sopran(), badana_partytura.podaj_tonacje()) and
                badanie_czy_dzwiek_jest_w_tonacji(element.podaj_alt(), badana_partytura.podaj_tonacje()) and
                badanie_czy_dzwiek_jest_w_tonacji(element.podaj_tenor(), badana_partytura.podaj_tonacje()) and
                badanie_czy_dzwiek_jest_w_tonacji(element.podaj_bas(), badana_partytura.podaj_tonacje())):
            lista_wyjsciowa.append(indeks)

    return lista_wyjsciowa
