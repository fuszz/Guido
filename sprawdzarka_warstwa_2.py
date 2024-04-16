from partytura import Partytura
import blad
from interwal import Interwal
from dzwiek import Dzwiek
from enumerations.enum_nazwy_interwalow import NazwyInterwalow

# ================================================================
# Warstwa 2 - błędy pionowe
# ================================================================

MAKS_INTERWAL_SA = Interwal(1, NazwyInterwalow.PRYMA_CZYSTA)
MAKS_INTERWAL_AT = Interwal(0, NazwyInterwalow.SEKSTA_WIELKA)
MAKS_INTERWAL_TB = Interwal(2, NazwyInterwalow.PRYMA_CZYSTA)


def czy_dzwiek_w_skali(badany_dzwiek: Dzwiek, granica_dolna: Dzwiek, granica_gorna: Dzwiek) -> bool:
    """Sprawdza, czy badany_dzwiek leży nie niżej niż  dźwięk granica_dolna i nie wyżej niż dźwięk granica_górna.
    Zwraca True, jeśli dźwięk leży w skali i False, gdy ją przekracza"""

    return (granica_dolna.podaj_swoj_kod_midi() <= badany_dzwiek.podaj_swoj_kod_midi() <=
            granica_gorna.podaj_swoj_kod_midi())


def sygn_i_glosy_akordow_gdzie_glosy_poza_skalami(badana_partytura: Partytura) -> list[(int, int, str)]:
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
        if not (czy_dzwiek_w_skali(element.podaj_sopran(), Dzwiek(4, "c"), Dzwiek(5, "a"))):
            przekroczone_glosy += "S"

        if not (czy_dzwiek_w_skali(element.podaj_alt(), Dzwiek(3, "f"), Dzwiek(5, "d"))):
            przekroczone_glosy += "A"

        if not (czy_dzwiek_w_skali(element.podaj_tenor(), Dzwiek(3, "c"), Dzwiek(4, "a"))):
            przekroczone_glosy += "T"

        if not (czy_dzwiek_w_skali(element.podaj_bas(), Dzwiek(2, "f"), Dzwiek(4, "d"))):
            przekroczone_glosy += "B"

        if przekroczone_glosy:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, przekroczone_glosy))
        licznik_akordow += 1
    return lista_wynikowa


def sygn_akordow_nietworzacych_funkcji(badana_partytura: Partytura) -> list[(int, int)]:
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


def sygn_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura: Partytura) -> list[(int, int, str)]:
    """Sprawdza, czy w podanej partyturze nie ma błędów przekraczania max dopuszczalnych odległości między głosami.
    Są to: 8 między S a A, 6 między A i T oraz 15 (2x 8) między T i B. Zwraca listę typli postaci (int, int, str),
    gdzie pierwsze dwie liczby to odpowiednio: numer taktu, numer akordu w tym takcie (numeracja od 0), a str mówi które
    odległości są przekroczone i jaki interwał jest między nimi. Możliwe są: SA, AT i TB + symbol interwału między nimi.
    Pusta lista wynikowa oznacza pozytywny rezultat."""

    lista_wynikowa = []
    licznik_taktow = 0
    licznik_akordow = 0
    tonacja = badana_partytura.podaj_tonacje()

    for element in badana_partytura.podaj_liste_akordow():
        wynik_glosow = ""
        if element == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue

        (dzwiek_s, dzwiek_a, dzwiek_t, dzwiek_b) = element.podaj_krotke_dzwiekow_z_akordu()
        interwal_sa = Interwal.stworz_z_dzwiekow(dzwiek_s, dzwiek_a, tonacja)
        interwal_at = Interwal.stworz_z_dzwiekow(dzwiek_a, dzwiek_t, tonacja)
        interwal_tb = Interwal.stworz_z_dzwiekow(dzwiek_t, dzwiek_b, tonacja)

        if interwal_sa > MAKS_INTERWAL_SA:
            wynik_glosow += "SA (" + str(interwal_sa) + "), "

        if interwal_at > MAKS_INTERWAL_AT:
            wynik_glosow += "AT (" + str(interwal_at) + "), "

        if interwal_tb > MAKS_INTERWAL_TB:
            wynik_glosow += "TB (" + str(interwal_tb) + "), "

        if wynik_glosow:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, wynik_glosow))
        licznik_taktow += 1

    return lista_wynikowa
