import akord
import blad
import dzwiek
import enumerations.enum_interwal as intr
import funkcja
import partytura
import tonacja

INTERWALY_DUR = [['1', '2', '3', '4', '5', '6', '7'],
                 ['7', '1', '2', '3>', '4', '5', '6'],
                 ['6>', '7', '1', '2>', '3>', '4', '5'],
                 ['5', '6', '7<', '1', '2', '3', '4<'],
                 ['4', '5', '6', '7', '1', '2', '3'],
                 ['3>', '4', '5', '6>', '7', '1', '2'],
                 ['2>', '3>', '4', '5>', '6', '7', '1']]

INTERWALY_MOLL = [['1', '2', '3>', '4', '5', '6>', '7<'],
                  ['7', '1', '2>', '3>', '4', '5>', '6'],
                  ['6', '7', '1', '2', '3', '4', '5<'],
                  ['5', '6', '7', '1', '2', '3>', '4<'],
                  ['4', '5', '6>', '7', '1', '2>', '3'],
                  ['3', '4<', '5', '6', '7<', '1', '2<'],
                  ['2>', '3>', '4>', '5>', '6>', '7>', '1']]


def podaj_interwal(dzwiek_a: dzwiek.Dzwiek, dzwiek_b: dzwiek.Dzwiek, badana_tonacja: tonacja.Tonacja) -> \
        (int, intr.Interwal):
    """
    Podaje, jaki interwał leży pomiędzy dźwiękami a i b. Nieczuły na kolejność dźwięków. Dźwięki muszą znajdować się w
    tonacji badana_tonacja, w przeciwnym razie podniesie BladDzwiekPozaTonacją.
    :param dzwiek_a: dzwiek a, dzwiek.Dzwiek
    :param dzwiek_b: dzwiek b, dzwiek.Dzwiek
    :param badana_tonacja: tonacja, w ktorej leżą oba dźwięki, instancja tonacja.Tonacja.
    :return: (int, Interwal), gdzie int jest liczbą pełnych oktaw znajdujących się między dźwiękami,
    a Interwał to instancja klasy enum_interwal.Interwal.
    """

    if dzwiek_a.podaj_swoj_kod_bezwzgledny() > dzwiek_b.podaj_swoj_kod_bezwzgledny():
        dzwiek_a, dzwiek_b = dzwiek_b, dzwiek_a
    pelnych_oktaw = (dzwiek_b.podaj_swoj_kod_bezwzgledny() - dzwiek_a.podaj_swoj_kod_bezwzgledny()) // 12

    stopien_a = dzwiek_a.podaj_swoj_stopien(badana_tonacja)
    stopien_b = dzwiek_b.podaj_swoj_stopien(badana_tonacja)
    symbol = INTERWALY_DUR[stopien_a][stopien_b] if badana_tonacja.czy_dur() else INTERWALY_MOLL[stopien_a][stopien_b]
    return pelnych_oktaw, intr.Interwal(symbol)


def czy_w_akordzie_sa_dzwieki_obce(badany_akord: akord.Akord, badana_tonacja: tonacja.Tonacja) -> bool:
    """
    Sprawdza, czy w podanym akordzie znajdują się dźwięki obce względem podanej tonacji. Jeśli tak, zwraca True,
    w przeciwnym razie - zwraca False.
    """
    try:
        badany_akord.podaj_sopran().podaj_swoj_stopien(badana_tonacja)
        badany_akord.podaj_alt().podaj_swoj_stopien(badana_tonacja)
        badany_akord.podaj_tenor().podaj_swoj_stopien(badana_tonacja)
        badany_akord.podaj_bas().podaj_swoj_stopien(badana_tonacja)
    except blad.BladDzwiekPozaTonacja:
        return True
    return False


def czy_w_partyturze_sa_dzwieki_obce(badana_partytutra: partytura.Partytura) -> bool:
    """ Sprawdza, czy w podanej partyturze znajdują się dźwięki obce.
    Jeśli tak, zwraca True, a w przeciwnym razie False"""
    for element in badana_partytutra.podaj_liste_akordow():
        if element == "T":
            pass
        if czy_w_akordzie_sa_dzwieki_obce(element, badana_partytutra.podaj_tonacje()):
            return True
    return False


def czy_pierwsza_i_ostatnia_tonika(badana_partytura: partytura.Partytura) -> bool:
    """Sprawdza, czy pierwszym i ostatnim akordem parytury jest tonika.
    Jeśli tak, zwraca True. W przeciwnym razie false"""

    if badana_partytura.podaj_liste_akordow()[0].ustal_funkcje(badana_partytura.podaj_tonacje()) not in (
            funkcja.Funkcja.TONIKA, funkcja.Funkcja.MOLL_TONIKA):
        return False

    if badana_partytura.podaj_liste_akordow()[-2].ustal_funkcje(badana_partytura.podaj_tonacje()) not in (
            funkcja.Funkcja.TONIKA, funkcja.Funkcja.MOLL_TONIKA):
        return False
    return True


def czy_takty_maja_odpowiednie_dlugosci(badana_partytura: partytura.Partytura) -> list[int]:
    """Sprawdza, czy takty partytury mają odpowiednie długości. Zwraca listę numerów (licząc od 0) tych taktów,
    których długość jest niepoprawna. Pusta lista oznacza pozytywny wynik testu."""
    lista_wynikowa = []
    licznik_dlugosci = 0
    licznik_taktow = 0
    for element in badana_partytura.podaj_liste_akordow():
        if element == "T":
            if licznik_dlugosci != badana_partytura.podaj_metrum().podaj_pozadana_wartosc_nut_w_takcie():
                lista_wynikowa.append(licznik_taktow)
            licznik_taktow += 1
            licznik_dlugosci = 0
        else:
            licznik_dlugosci += element.podaj_dlugosc().value
    return lista_wynikowa


def czy_liczba_taktow_jest_poprawna(badana_partytura: partytura.Partytura) -> bool:
    """Zwraca true, jeśli liczba znaków końca taktu jest taka sama, jak zadeklarowana liczba taktów. W przeciwnym razie
    zwraca false."""
    return badana_partytura.czy_poprawna_liczba_taktow()
