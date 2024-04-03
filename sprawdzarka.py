import akord
import blad
import dzwiek
import enumerations.enum_interwal as intr
import enumerations.enum_przewroty as prz
import funkcja
import partytura
import tonacja

# W RAZIE ROZBUDOWY PROGRAMU NALEŻY UZUPEŁNIĆ PONIŻSZE ZMIENNE GLOBALNE:
PRZEWIDZIANE_TONIKI = [funkcja.Funkcja.TONIKA, funkcja.Funkcja.MOLL_TONIKA]
PRZEWIDZIANE_SUBDOMINANTY = [funkcja.Funkcja.SUBDOMINANTA, funkcja.Funkcja.MOLL_SUBDOMINANTA]
PRZEWIDZIANE_DOMINANTY = [funkcja.Funkcja.DOMINANTA, funkcja.Funkcja.DOMINANTA_SEPTYMOWA]

PRZEWIDZIANE_TROJDZWIEKI = [funkcja.Funkcja.TONIKA, funkcja.Funkcja.MOLL_TONIKA, funkcja.Funkcja.SUBDOMINANTA,
                            funkcja.Funkcja.MOLL_SUBDOMINANTA, funkcja.Funkcja.DOMINANTA]
PRZEWIDZIANE_CZTERODZWIEKI = [funkcja.Funkcja.DOMINANTA_SEPTYMOWA]
KOLEJNOSC_INTERWALOW_MIEDZY_GLOSAMI = ["SA,", "ST,", "SB,", "AT,", "AB,", "TB,"]

""" Moduł sprawdzarki będzie opierać sie na czterech (?) warstwach sprawdzania poprawności partytury. Będą to:
    1. Sprawdzenie, czy wprowadzone dane są kompletne i czy dane nie zostały uszkodzone. Należą tu:
        a. Czy wprowadzono zadeklarowaną w partyturze liczbę taktów - OK
        b. Czy pojemność poszczególnych taktów odpowiada wymogom obranego metrum - OK
        c. ... 
        itp.
        
    2. Sprawdzenie, czy w partyturze nie ma pionowych błędów, czyli takich, które nie dotyczą kolejności 
       ani łączenia akordów ze sobą. A zatem:
        a. Czy w partyturze nie występują dźwięki obce - OK
        b. Czy w partyturze nie występują krzyżowania głosów - OK
        c. Czy w poszczególnych głosach dźwięki pozostają w swoich skalach - OK
        d. Czy dźwięki tworzą w podanej tonacji sensowne funkcje harmoniczne  - OK
        e. Czy nie są przekroczone odległości pomiędzy głosami - OK
        f. ...
        itp.
        
    3. Sprawdzenie, czy kolejność akordów jest poprawna, ale na razie bez wnikania w sposób łączenia ich ze sobą. 
       Tutaj analizujemy
       a. Czy w partyturze na pierwszym i ostatnim miejscu występuje akord toniczny - OK
       b. Czy w partyturze po dominancie nie występuje subdominanta - OK
       c. Czy w partyturze na mocnej części taktu (na "raz") nie występuje akord w słabym (drugim) przewrocie - OK
       d. Czy w partyturze nie przetrzymano akordu przez kreskę taktową (błąd!) - OK
       e. Czy ostateczne rozwiązanie nie jest w drugim (słabym) przewrocie - jeszcze testy
       itd.
       
    4. Sprawdzenie poprawności łączeń akordów. Będą to:
        a. Sprawdzenie, czy w partyturze występują kwinty równoległe
        b. Sprawdzenie, czy są oktawy równoległe
        c. Sprawdzenie, czy nie ma ruchu wszystkich głosów w tym samym kierunku
        d. Sprawdzenie, czy nie występują skoki o zbyt duży interwał
        e. Sprawdzenie, czy nie występuje ruch o interwał zwiększony
        f. ...
        itp.
        
    Jeśli we wcześniejszych warstwach testy wykażą błędy, sprawdzanie zakończy się, bo niemożliwe będzie osiągnięcie
    pozytywnych wyników w testach późniejszych, co wynika z prawideł harmonii. Użytkownik będzie informowany 
    o występowaniu poszczególnych błędów. Niektóre funkcje, w razie wystąpienia błędów, z tego samego powodu będą 
    przerywać dalsze poszukiwanie błędów.
"""

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


def podaj_interwal(dzwiek_a: dzwiek.Dzwiek, dzwiek_b: dzwiek.Dzwiek, badana_tonacja: tonacja.Tonacja) -> (
        int, intr.Interwal):
    """
    Podaje, jaki interwał leży pomiędzy dźwiękami a i b. Nieczuły na kolejność dźwięków. Dźwięki muszą znajdować się w
    tonacji badana_tonacja, w przeciwnym razie podniesie BladDzwiekPozaTonacją.
    :param dzwiek_a: dzwiek a, dzwiek.Dzwiek
    :param dzwiek_b: dzwiek b, dzwiek.Dzwiek
    :param badana_tonacja: tonacja, w ktorej leżą oba dźwięki, instancja tonacja.Tonacja.
    :return: (int, Interwal), gdzie int jest liczbą pełnych oktaw znajdujących się między dźwiękami,
    a Interwał to instancja klasy enum_interwal.Interwal.
    """

    if dzwiek_a.podaj_swoj_kod_midi() > dzwiek_b.podaj_swoj_kod_midi():
        dzwiek_a, dzwiek_b = dzwiek_b, dzwiek_a
    pelnych_oktaw = (dzwiek_b.podaj_swoj_kod_midi() - dzwiek_a.podaj_swoj_kod_midi()) // 12

    stopien_a = dzwiek_a.podaj_swoj_stopien(badana_tonacja)
    stopien_b = dzwiek_b.podaj_swoj_stopien(badana_tonacja)
    symbol = INTERWALY_DUR[stopien_a][stopien_b] if badana_tonacja.czy_dur() else INTERWALY_MOLL[stopien_a][stopien_b]
    return pelnych_oktaw, intr.Interwal.interwal_z_symbolu(symbol)


def podaj_interwaly_w_akordzie(badany_akord: akord.Akord, badana_tonacja) -> \
        ((int, intr.Interwal), (int, intr.Interwal), (int, intr.Interwal), (int, intr.Interwal),
         (int, intr.Interwal), (int, intr.Interwal)):
    """Zwraca krotkę odległości pomiędzy głosami w następującej kolejności:
        S-A, S-T, S-B, A-T, A-B, T-B. Krotka ma postać par intów i Interwałów, gdzie int oznacza liczbę pełnych oktaw.
    """
    return (podaj_interwal(badany_akord.podaj_sopran(), badany_akord.podaj_alt(), badana_tonacja),
            podaj_interwal(badany_akord.podaj_sopran(), badany_akord.podaj_tenor(), badana_tonacja),
            podaj_interwal(badany_akord.podaj_sopran(), badany_akord.podaj_bas(), badana_tonacja),
            podaj_interwal(badany_akord.podaj_alt(), badany_akord.podaj_tenor(), badana_tonacja),
            podaj_interwal(badany_akord.podaj_alt(), badany_akord.podaj_bas(), badana_tonacja),
            podaj_interwal(badany_akord.podaj_tenor(), badany_akord.podaj_bas(), badana_tonacja))


# ===============================================================
# Warstwa 1 --> Poprawność i kompletność wprowadzenia danych:
# ===============================================================
def czy_liczba_taktow_jest_poprawna(badana_partytura: partytura.Partytura) -> bool:
    """Zwraca true, jeśli liczba znaków końca taktu jest taka sama, jak zadeklarowana liczba taktów. W przeciwnym razie
    zwraca false."""
    return badana_partytura.czy_poprawna_liczba_taktow()


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


# ================================================================
# Warstwa 2 - błędy pionowe
# ================================================================
def czy_w_partyturze_sa_dzwieki_obce(badana_partytutra: partytura.Partytura) -> list[(int, int)]:
    """ Sprawdza, czy w podanej partyturze znajdują się dźwięki obce.
    Zwraca listę par intów, w której 1-sza liczba to numer taktu, a druga to numer akordu w tym takcie. Numeracja od 0.
    Jeśli lista jest pusta, to znaczy, że wynik sprawdzenia jest pozytywny."""
    licznik_akordow = 0
    licznik_taktow = 0
    lista_wynikowa = []
    for element in badana_partytutra.podaj_liste_akordow():
        if element == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        if czy_w_akordzie_sa_dzwieki_obce(element, badana_partytutra.podaj_tonacje()):
            lista_wynikowa.append((licznik_taktow, licznik_akordow))
        licznik_akordow += 1
    return lista_wynikowa


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


def czy_glosy_nie_sa_skrzyzowane(badana_partytura: partytura.Partytura) -> list[(int, int)]:
    """Funkcja sprawdza, czy w podanej partyturze nie występują skrzyżowania głosów. Zwraca listę par intów, gdzie
    pierwsza liczba oznacza numer taktu, a druga - numer akordu, w którym wystepuje skrzyżowanie. Numeracja od 0.
    Pusta lista wynikowa oznacza poprawność partytury."""
    licznik_akordow = 0
    licznik_taktow = 0
    lista_wynikowa = []
    for element in badana_partytura.podaj_liste_akordow():
        if element == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        if not (
                element.podaj_sopran().podaj_swoj_kod_midi() >= element.podaj_alt().podaj_swoj_kod_midi()
                >= element.podaj_tenor().podaj_swoj_kod_midi() >= element.podaj_bas().podaj_swoj_kod_midi()
        ):
            lista_wynikowa.append((licznik_taktow, licznik_akordow))
        licznik_akordow += 1
    return lista_wynikowa


def czy_dzwiek_w_zadanej_skali(badany_dzwiek: dzwiek.Dzwiek, granica_dolna: dzwiek.Dzwiek,
                               granica_gorna: dzwiek.Dzwiek) -> bool:
    """Sprawdza, czy badany_dzwiek leży nie niżej niż  dźwięk granica_dolna i nie wyżej niż dźwięk granica_górna.
    Zwraca True, jeśli dźwięk leży w skali i False, gdy ją przekracza"""

    return (granica_dolna.podaj_swoj_kod_midi() <= badany_dzwiek.podaj_swoj_kod_midi() <=
            granica_gorna.podaj_swoj_kod_midi())


def czy_glosy_w_swoich_skalach(badana_partytura: partytura.Partytura) -> list[(int, int, str)]:
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
        if not (czy_dzwiek_w_zadanej_skali(element.podaj_sopran(), dzwiek.Dzwiek(4, "c"), dzwiek.Dzwiek(5, "a"))):
            przekroczone_glosy += "sopran "

        if not (czy_dzwiek_w_zadanej_skali(element.podaj_alt(), dzwiek.Dzwiek(3, "f"), dzwiek.Dzwiek(5, "d"))):
            przekroczone_glosy += "alt "

        if not (czy_dzwiek_w_zadanej_skali(element.podaj_tenor(), dzwiek.Dzwiek(3, "c"), dzwiek.Dzwiek(4, "a"))):
            przekroczone_glosy += "tenor "

        if not (czy_dzwiek_w_zadanej_skali(element.podaj_bas(), dzwiek.Dzwiek(2, "f"), dzwiek.Dzwiek(4, "d"))):
            przekroczone_glosy += "bas "

        if przekroczone_glosy:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, przekroczone_glosy))
        licznik_akordow += 1
    return lista_wynikowa


def czy_dzwieki_tworza_sensowne_funkcje_w_tonacji(badana_partytura: partytura.Partytura) -> list[(int, int)]:
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


def czy_odleglosci_glosow_nie_sa_przekroczone(badana_partytura: partytura.Partytura) -> list[(int, int, str)]:
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
        if podaj_interwal(element.podaj_alt(), element.podaj_sopran(), badana_partytura.podaj_tonacje())[0] > 0:
            oznaczenia_glosow += "SA" + str(podaj_interwal(element.podaj_alt(), element.podaj_sopran(),
                                                           badana_partytura.podaj_tonacje()))

        if (podaj_interwal(element.podaj_alt(), element.podaj_tenor(), badana_partytura.podaj_tonacje())[0] > 0 or
                podaj_interwal(element.podaj_alt(), element.podaj_tenor(), badana_partytura.podaj_tonacje())[1] >
                intr.Interwal.SEKSTA_WIELKA):
            oznaczenia_glosow += "AT" + str(podaj_interwal(element.podaj_alt(), element.podaj_tenor(),
                                                           badana_partytura.podaj_tonacje()))

        if podaj_interwal(element.podaj_tenor(), element.podaj_bas(), badana_partytura.podaj_tonacje())[0] > 1:
            oznaczenia_glosow += "TB" + str(podaj_interwal(element.podaj_bas(), element.podaj_tenor(),
                                                           badana_partytura.podaj_tonacje()))

        if oznaczenia_glosow:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, oznaczenia_glosow))
        licznik_taktow += 1

    return lista_wynikowa


# ================================================================================================
# WARSTWA 3 - Sprawdzenie, czy kolejność akordów jest poprawna
# ================================================================================================

def czy_pierwsza_i_ostatnia_tonika(badana_partytura: partytura.Partytura) -> bool:
    """Sprawdza, czy pierwszym i ostatnim akordem parytury jest tonika.
    Jeśli tak, zwraca True. W przeciwnym razie false"""

    if badana_partytura.podaj_liste_akordow()[0].ustal_funkcje(
            badana_partytura.podaj_tonacje()) not in PRZEWIDZIANE_TONIKI:
        return False

    if badana_partytura.podaj_liste_akordow()[-2].ustal_funkcje(
            badana_partytura.podaj_tonacje()) not in PRZEWIDZIANE_TONIKI:
        return False
    return True


def czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura: partytura.Partytura) -> bool:
    """Sprawdza, czy ostateczne rozwiązanie (ostatnia tonika w partyturze) jest w innym niż drugi przewrocie. Jeśli tak,
    zwraca True. W przeciwnym razie zwraca False. Funkcja przyjmuje, że ostatni akord to zawsze przedostatni
    element listy akordów"""

    return (badana_partytura.podaj_liste_akordow()[-2].ustal_przewrot(badana_partytura.podaj_tonacje()) !=
            prz.Przewrot.DRUGI)


def czy_po_dominancie_nie_ma_subdominanty(badana_partytura: partytura.Partytura) -> list[(int, int)]:
    """Sprawdza, czy po dominancie nie występuje gdzieś subdominanta (co jest poważnym błędem).
    Zwraca listę par (int, int), gdzie pierwsza liczba to numer taktu, a druga - numer akordu (numeracja od 0).
    Pozytywny wynik testu, gdy rezultat jest pustą listą.
    UWAGA! Funkcja nie sprawdza, czy na pierwszym miejscu partytury znajduje się tonika, ani czy jako pierwszy nie
    występuje znak końca taktu.
    """
    lista_wynikowa = []
    licznik_taktow = 0
    licznik_akordow = 0
    ostatni_akord = badana_partytura.podaj_liste_akordow()[0]

    for element in badana_partytura.podaj_liste_akordow():
        if element == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue

        if (element.ustal_funkcje(badana_partytura.podaj_tonacje()) in PRZEWIDZIANE_SUBDOMINANTY and
                ostatni_akord.ustal_funkcje(badana_partytura.podaj_tonacje()) in PRZEWIDZIANE_DOMINANTY):
            lista_wynikowa.append((licznik_taktow, licznik_akordow))

        licznik_akordow += 1
        ostatni_akord = element

    return lista_wynikowa


def czy_na_raz_nie_ma_drugiego_przewrotu(badana_partytura: partytura.Partytura) -> list[int]:
    """Sprawdza, czy na mocnej części taktu (czyli na 1) nie ma trójdźwięku (tj. nie rozważamy D7)
     w słabym (tj. drugiem) przewrocie. Zwraca listę intów - numerów taktów (numeracja od 0), które zaczynają się
     słabym przewrotem akordu. Pusta lista wynikowa oznacza pozytywny rezultat testu.
     UWAGA: funkcja nie uwzględnia istnienia pustych taktów. Należy przed nią wykonać testy z warstwy 1."""

    lista_wynikowa: list[int] = []
    licznik_taktow: int = 0
    czy_pierwszy_akord_taktu: bool = True

    for element in badana_partytura.podaj_liste_akordow():

        if czy_pierwszy_akord_taktu:
            czy_pierwszy_akord_taktu = False

            if (element.ustal_funkcje(badana_partytura.podaj_tonacje()) in PRZEWIDZIANE_TROJDZWIEKI and
                    element.ustal_przewrot(badana_partytura.podaj_tonacje()) == prz.Przewrot.DRUGI):
                lista_wynikowa.append(licznik_taktow)

        if element == "T":
            czy_pierwszy_akord_taktu = True
            licznik_taktow += 1
    return lista_wynikowa


def czy_funkcja_nie_przetrzymana_przez_kreske_taktowa(badana_partytura: partytura.Partytura) -> list[int]:
    """Sprawdza, czy funkcja nie jest przetrzymana przez kreskę taktową. Zwraca numer taktu, który zaczyna się na
    ten sam akord, co zakończył się akord poprzedni. Pusta lista świadczy o poprawności rozwiązania."""
    licznik_taktow = 0
    czy_poczatek_taktu = False
    lista_wynikowa: list[int] = []
    ostatni_akord: akord.Akord = badana_partytura.podaj_liste_akordow()[0]

    for element in badana_partytura.podaj_liste_akordow():
        if element == "T":
            czy_poczatek_taktu = True
            licznik_taktow += 1
            continue

        if czy_poczatek_taktu:
            czy_poczatek_taktu = False
            if (element.ustal_funkcje(badana_partytura.podaj_tonacje()) ==
                    ostatni_akord.ustal_funkcje(badana_partytura.podaj_tonacje())):
                lista_wynikowa.append(licznik_taktow)
        ostatni_akord = element
    return lista_wynikowa


# ===================================================================================================
# Warstwa 3 - sprawdzenie poprawności połączeń akordów
# ===================================================================================================


def daj_krotke_dzwiekow_z_akordu(badany_akord: akord.Akord) -> (
        dzwiek.Dzwiek, dzwiek.Dzwiek, dzwiek.Dzwiek, dzwiek.Dzwiek):
    """Zwraca dźwięki składowe akordu w postaci czteroelementowej krotki obiektów klasy Dźwięk w kolejności:
    (sopran, alt, tenor, bas)"""
    return badany_akord.podaj_sopran(), badany_akord.podaj_alt(), badany_akord.podaj_tenor(), badany_akord.podaj_bas()


def czy_sa_kwinty_rownolegle(badana_partytura: partytura.Partytura) -> list[(int, int, str)]:
    """Bada połączenia akordów i sprawdza, czy nie występują kwinty równoległe. Zwraca listę tupli postaci
    (int, int, str), gdzie inty to kolejno numer taktu i numer akordu w tym takcie, który jest drugim w którym jest
    kwinta równoległa, a str wskazuje na głosy, między którymi wykryto kwinty. Pusta lista wynikowa oznacza brak kwint.
    Takty i akordy numerowane są od 0.
    """

    lista_wynikowa: list[(int, int, str)] = []
    licznik_taktow = 0
    licznik_akordow = 0
    poprzedni_akord: akord.Akord = badana_partytura.podaj_liste_akordow()[0]

    for obecny_akord in badana_partytura.podaj_liste_akordow()[1:]:
        if obecny_akord == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        licznik_akordow += 1
        obecne_interwaly = podaj_interwaly_w_akordzie(obecny_akord, badana_partytura.podaj_tonacje())
        poprzednie_interwaly = podaj_interwaly_w_akordzie(poprzedni_akord, badana_partytura.podaj_tonacje())
        glosy_z_kwintami = ""
        for i in range(6):
            if (obecne_interwaly[i][1] == intr.Interwal.KWINTA_CZYSTA and
                    poprzednie_interwaly[i][1] == intr.Interwal.KWINTA_CZYSTA):
                glosy_z_kwintami += KOLEJNOSC_INTERWALOW_MIEDZY_GLOSAMI[i]

        if glosy_z_kwintami:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, glosy_z_kwintami))

    return lista_wynikowa


def czy_sa_oktawy_rownolegle(badana_partytura: partytura.Partytura) -> list[(int, int, str)]:
    """Bada połączenia akordów i sprawdza, czy nie występują oktawy równoległe. Zwraca listę tupli postaci
    (int, int, str), gdzie inty to kolejno numer taktu i numer akordu w tym takcie, który jest drugim w którym jest
    oktawa równoległa, a str wskazuje na głosy, między którymi wykryto oktawy. Pusta lista wynikowa oznacza brak błędów.
    Takty i akordy numerowane są od 0.
    """

    lista_wynikowa: list[(int, int, str)] = []
    licznik_taktow = 0
    licznik_akordow = 0
    poprzedni_akord: akord.Akord = badana_partytura.podaj_liste_akordow()[0]

    for obecny_akord in badana_partytura.podaj_liste_akordow()[1:]:
        if obecny_akord == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        licznik_akordow += 1
        obecne_interwaly = podaj_interwaly_w_akordzie(obecny_akord, badana_partytura.podaj_tonacje())
        poprzednie_interwaly = podaj_interwaly_w_akordzie(poprzedni_akord, badana_partytura.podaj_tonacje())
        glosy_z_oktawami = ""
        for i in range(6):
            if (obecne_interwaly[i][0] > 0 and obecne_interwaly[i][1] == intr.Interwal.PRYMA_CZYSTA and
                    poprzednie_interwaly[i][0] > 0 and poprzednie_interwaly[i][1] == intr.Interwal.PRYMA_CZYSTA):
                glosy_z_oktawami += KOLEJNOSC_INTERWALOW_MIEDZY_GLOSAMI[i]

        if glosy_z_oktawami:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, glosy_z_oktawami))

    return lista_wynikowa


def czy_wszystkie_glosy_poszly_w_jednym_kierunku(badana_partytura: partytura.Partytura) -> list[(int, int)]:
    """ Sprawdza, czy w którymś połączeniu wszystkie głosy nie poruszają się w tym samym kierunku. Zwraca listę tupli
    postaci (int, int), gdzie pierwsza liczba to numer taktu, a druga - numer akordu w takcie tego akordu, który został
    połączony wadliwie ze swoim poprzednikiem. Liczniki pracują od 0. Pusta lista wynikowa oznacza brak błędu"""

    lista_wynikowa = []
    licznik_akordow = 0
    licznik_taktow = 0
    poprzedni_akord = badana_partytura.podaj_liste_akordow()[0]
    for obecny_akord in badana_partytura.podaj_liste_akordow()[1:]:
        if obecny_akord == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        licznik_akordow += 1
        kody_midi_dzwiekow_poprzedniego_akordu = tuple(map(lambda d: d.podaj_swoj_kod_midi(),
                                                           poprzedni_akord.podaj_krotke_dzwiekow_z_akordu()))
        kody_midi_dzwiekow_obecnego_akordu = tuple(map(lambda d: d.podaj_swoj_kod_midi(),
                                                       obecny_akord.podaj_krotke_dzwiekow_z_akordu()))
        if (all(d1 > d2 for d1, d2 in
                zip(kody_midi_dzwiekow_poprzedniego_akordu, kody_midi_dzwiekow_obecnego_akordu)) or
                all(d1 < d2 for d1, d2 in
                    zip(kody_midi_dzwiekow_poprzedniego_akordu, kody_midi_dzwiekow_obecnego_akordu))):
            lista_wynikowa.append((licznik_taktow, licznik_akordow))
    return lista_wynikowa
 # TESTY DO TEGO