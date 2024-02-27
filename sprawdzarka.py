import partytura
import akord
import tonacja
from enumerations import enum_funkcje, enum_krzyzowania_glosow, enum_metrum, enum_niepoprawne_stopnie, enum_przewroty, \
    enum_zdwojony_skladnik, enum_dzwieki_w_skalach
from typing import List


def badanie_objetosci_taktow_w_partyturze(badana_partytura: partytura.Partytura) -> List[int]:
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
            return ValueError
    return lista_wyjsciowa
