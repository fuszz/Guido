import partytura
import blad
import dzwiek
import sprawdzarka_warstwa_4 as spr
from enumerations.enum_mozliwe_interwaly import MozliweInterwaly


# ================================================================
# Warstwa 2 - błędy pionowe
# ================================================================


def czy_dzwiek_w_skali(badany_dzwiek: dzwiek.Dzwiek, granica_dolna: dzwiek.Dzwiek,
                       granica_gorna: dzwiek.Dzwiek) -> bool:
    """Sprawdza, czy badany_dzwiek leży nie niżej niż  dźwięk granica_dolna i nie wyżej niż dźwięk granica_górna.
    Zwraca True, jeśli dźwięk leży w skali i False, gdy ją przekracza"""

    return (granica_dolna.podaj_swoj_kod_midi() <= badany_dzwiek.podaj_swoj_kod_midi() <=
            granica_gorna.podaj_swoj_kod_midi())


def sygn_i_glosy_akordow_gdzie_glosy_poza_skalami(badana_partytura: partytura.Partytura) -> list[(int, int, str)]:
    """Funkcja sprawdza, czy w podanej partyturze dźwięki nie wykraczają poza skale głosów.
    Zwraca listę tupli postaci (int, int, str), gdzie pierwsza liczba oznacza numer taktu, druga - numer akordu, a str -
    informacje o głosie, w którym nastąpiło naruszenie. Numeracja od 0.
    Pusta lista wynikowa oznacza poprawność partytury."""
    lista_wynikowa = []
    licznik_taktow = 0
    licznik_akordow = 0

    for element in badana_partytura.podaj_liste_akordow():
        przekroczone_glosy = ""
        if element == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        if not (czy_dzwiek_w_skali(element.podaj_sopran(), dzwiek.Dzwiek(4, "c"), dzwiek.Dzwiek(5, "a"))):
            przekroczone_glosy += "S"

        if not (czy_dzwiek_w_skali(element.podaj_alt(), dzwiek.Dzwiek(3, "f"), dzwiek.Dzwiek(5, "d"))):
            przekroczone_glosy += "A"

        if not (czy_dzwiek_w_skali(element.podaj_tenor(), dzwiek.Dzwiek(3, "c"), dzwiek.Dzwiek(4, "a"))):
            przekroczone_glosy += "T"

        if not (czy_dzwiek_w_skali(element.podaj_bas(), dzwiek.Dzwiek(2, "f"), dzwiek.Dzwiek(4, "d"))):
            przekroczone_glosy += "B"

        if przekroczone_glosy:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, przekroczone_glosy))
        licznik_akordow += 1
    return lista_wynikowa


def sygn_akordow_nietworzacych_funkcji(badana_partytura: partytura.Partytura) -> list[(int, int)]:
    """Funkcja sprawdza, czy akordy partytury są w swojej funkcji dobrymi akordami. Zwraca listę par intów, gdzie
    pierwsza liczba oznacza numer taktu, a druga - numer akordu, w którym wystepuje skrzyżowanie. Numeracja od 0.
    Pusta lista wynikowa oznacza poprawność partytury."""
    lista_wynikowa = []
    licznik_akordow = 0
    licznik_taktow = 0

    for element in badana_partytura.podaj_liste_akordow():
        if element == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue

        try:
            element.ustal_funkcje(badana_partytura.podaj_tonacje())

        except blad.BladStopienPozaFunkcja:
            lista_wynikowa.append((licznik_taktow, licznik_akordow))
        licznik_akordow += 1
    return lista_wynikowa


def sygn_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura: partytura.Partytura) -> list[(int, int, str)]:
    """Sprawdza, czy w podanej partyturze nie ma błędów przekraczania max dopuszczalnych odległości między głosami.
    Są to: 8 między S a A, 6 między A i T oraz 15 (2x 8) między T i B. Zwraca listę typli postaci (int, int, str),
    gdzie pierwsze dwie liczby to odpowiednio: numer taktu, numer akordu w tym takcie (numeracja od 0), a str mówi które
    odległości są przekroczone i jaki interwał jest między nimi. Możliwe są: SA, AT i TB + symbol interwału między nimi.
    Pusta lista wynikowa oznacza pozytywny rezultat."""

    lista_wynikowa = []
    licznik_taktow = 0
    licznik_akordow = 0

    for element in badana_partytura.podaj_liste_akordow():
        oznaczenia_glosow = ""
        if element == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        if spr.podaj_interwal(element.podaj_alt(), element.podaj_sopran(), badana_partytura.podaj_tonacje())[0] > 0:
            oznaczenia_glosow += "SA" + str(spr.podaj_interwal(element.podaj_alt(), element.podaj_sopran(),
                                                               badana_partytura.podaj_tonacje()))

        if (spr.podaj_interwal(element.podaj_alt(), element.podaj_tenor(), badana_partytura.podaj_tonacje())[0] > 0 or
                spr.podaj_interwal(element.podaj_alt(), element.podaj_tenor(), badana_partytura.podaj_tonacje())[1] >
                MozliweInterwaly.SEKSTA_WIELKA):
            oznaczenia_glosow += "AT" + str(spr.podaj_interwal(element.podaj_alt(), element.podaj_tenor(),
                                                               badana_partytura.podaj_tonacje()))

        if spr.podaj_interwal(element.podaj_tenor(), element.podaj_bas(), badana_partytura.podaj_tonacje())[0] > 1:
            oznaczenia_glosow += "TB" + str(spr.podaj_interwal(element.podaj_bas(), element.podaj_tenor(),
                                                               badana_partytura.podaj_tonacje()))

        if oznaczenia_glosow:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, oznaczenia_glosow))
        licznik_taktow += 1

    return lista_wynikowa
