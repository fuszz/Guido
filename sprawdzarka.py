import dzwiek
import partytura
import akord
import tonacja
from enumerations import enum_funkcje, enum_krzyzowania_glosow, enum_metrum, enum_przewroty, \
    enum_zdwojony_skladnik, enum_dzwieki_w_skalach, enum_interwal
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
    """
    Funkcja zwraca informację, czy dźwięk jest stopniem w zadanej tonacji.
    :param badany_dzwiek: dźwięk, który chcemy sprawdzić
    :param badana_tonacja: tonacja, w której chcemy ustalić, czy należy do niej dźwięk
    :return: wartość logiczna True/False
    """
    try:
        badany_dzwiek.podaj_swoj_stopien(badana_tonacja)
        return True
    except ValueError:
        return False


def badanie_wystepowania_dzwiekow_obcych(badana_partytura: partytura.Partytura) -> List[int]:
    """
    Nie zajmujemy się analizą dźwięków obcych - ich występowanie jest błędem.
    Funkcja zwraca listę indeksów akordów, które zawierają dźwięk obcy
    """
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


def podaj_interwal_miedzy_dzwiekami(dzwiek_1: dzwiek.Dzwiek, dzwiek_2: dzwiek.Dzwiek, badana_tonacja: tonacja.Tonacja
                                    ) -> (int, enum_interwal.Interwal):
    """
    Funkcja zwróci informację o interwale pomiędzy dwoma dzwiekami. Kolejność podania ich do funkcji nie ma znaczenia.
    :param dzwiek_1: Dźwięk 1.
    :param dzwiek_2: Dźwięk 2.
    :param badana_tonacja: tonacja, w której znajdują się oba dźwięki
    :return: Krotka: (<liczba_pełnych_oktaw>, <interwał - enum_interwal.Interwal>)
    """

    try:
        dzwiek_1.podaj_swoj_stopien(badana_tonacja)
        dzwiek_2.podaj_swoj_stopien(badana_tonacja)
    except ValueError:
        raise ValueError("Podane dźwięki nie należą do podanej tonacji")

    if dzwiek_1.podaj_swoj_kod_bezwzgledny() > dzwiek_2.podaj_swoj_kod_bezwzgledny():
        (dzwiek_1, dzwiek_2) = (dzwiek_2, dzwiek_1)

    liczba_pelnych_oktaw: int = (dzwiek_2.podaj_swoj_kod_bezwzgledny() -
                                 dzwiek_1.podaj_swoj_kod_bezwzgledny()) // 12

    odleglosc_w_poltonach: int = ((dzwiek_2.podaj_swoj_kod_bezwzgledny() - liczba_pelnych_oktaw * 12)
                                  - (dzwiek_1.podaj_swoj_kod_bezwzgledny() - liczba_pelnych_oktaw * 12))

    interwal: enum_interwal.Interwal = enum_interwal.Interwal.PRYMA_CZYSTA

    if odleglosc_w_poltonach == 3:
        print(dzwiek_1.podaj_swoj_stopien(badana_tonacja))
        if not badana_tonacja.czy_dur() and dzwiek_1.podaj_swoj_stopien(badana_tonacja) == 5:
            interwal = enum_interwal.Interwal.SEKUNDA_ZWIEKSZONA
        else:
            return liczba_pelnych_oktaw, enum_interwal.Interwal.TERCJA_MALA

    elif odleglosc_w_poltonach == 6:
        if ((dzwiek_1.podaj_swoj_stopien(badana_tonacja), dzwiek_2.podaj_swoj_stopien(badana_tonacja)) == (1, 6) or
                (dzwiek_1.podaj_swoj_stopien(badana_tonacja), dzwiek_2.podaj_swoj_stopien(badana_tonacja)) == (6, 1)):
            interwal = enum_interwal.Interwal.KWINTA_ZMNIEJSZONA
        else:
            interwal = enum_interwal.Interwal.KWARTA_ZWIEKSZONA

    elif odleglosc_w_poltonach == 8:
        if ((dzwiek_1.podaj_swoj_stopien(badana_tonacja), dzwiek_2.podaj_swoj_stopien(badana_tonacja)) == (2, 7) or
                (dzwiek_1.podaj_swoj_stopien(badana_tonacja), dzwiek_2.podaj_swoj_stopien(badana_tonacja)) == (7, 2)):
            interwal = enum_interwal.Interwal.KWINTA_ZWIEKSZONA
        else:
            interwal = enum_interwal.Interwal.SEKSTA_MALA
    else:
        interwal = enum_interwal.Interwal.interwal_z_odleglosci(odleglosc_w_poltonach)
    return liczba_pelnych_oktaw, interwal


print(podaj_interwal_miedzy_dzwiekami(dzwiek.Dzwiek(1, 'd'), dzwiek.Dzwiek(1, 'g#'), tonacja.Tonacja('a')))
print(podaj_interwal_miedzy_dzwiekami(dzwiek.Dzwiek(1, 'd'), dzwiek.Dzwiek(1, 'e'), tonacja.Tonacja('C')))
print(podaj_interwal_miedzy_dzwiekami(dzwiek.Dzwiek(1, 'd'), dzwiek.Dzwiek(1, 'f'), tonacja.Tonacja('C')))
print(podaj_interwal_miedzy_dzwiekami(dzwiek.Dzwiek(1, 'd'), dzwiek.Dzwiek(1, 'g'), tonacja.Tonacja('C')))
print(podaj_interwal_miedzy_dzwiekami(dzwiek.Dzwiek(1, 'd'), dzwiek.Dzwiek(1, 'a'), tonacja.Tonacja('C')))
print(podaj_interwal_miedzy_dzwiekami(dzwiek.Dzwiek(1, 'd'), dzwiek.Dzwiek(1, 'h'), tonacja.Tonacja('C')))
print(podaj_interwal_miedzy_dzwiekami(dzwiek.Dzwiek(1, 'd#'), dzwiek.Dzwiek(2, 'c#'), tonacja.Tonacja('C#')))
print("____________________________________________")
print(podaj_interwal_miedzy_dzwiekami(dzwiek.Dzwiek(1, 'c'), dzwiek.Dzwiek(1, 'd'), tonacja.Tonacja('C')))

