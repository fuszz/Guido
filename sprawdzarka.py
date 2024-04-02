import akord
import blad
import dzwiek
import enumerations.enum_interwal as intr
import funkcja
import partytura
import tonacja

""" Moduł sprawdzarki będzie opierać sie na czterech (?) warstwach sprawdzania poprawności partytury. Będą to:
    1. Sprawdzenie, czy wprowadzone dane są kompletne i czy dane nie zostały uszkodzone. Należą tu:
        a. Czy wprowadzono zadeklarowaną w partyturze liczbę taktów
        b. Czy pojemność poszczególnych taktów odpowiada wymogom obranego metrum
        c. ... 
        itp.
        
    2. Sprawdzenie, czy w partyturze nie ma pionowych błędów, czyli takich, które nie dotyczą kolejności 
       ani łączenia akordów ze sobą. A zatem:
        a. Czy w partyturze nie występują dźwięki obce
        b. Czy w partyturze nie występują krzyżowania głosów
        c. Czy w poszczególnych głosach dźwięki pozostają w swoich skalach
        d. Czy dźwięki tworzą w podanej tonacji sensowne funkcje harmoniczne 
        e. Czy nie są przekroczone odległości pomiędzy głosami
        f. ...
        itp.
        
    3. Sprawdzenie, czy kolejność akordów jest poprawna, ale na razie bez wnikania w sposób łączenia ich ze sobą. 
       Tutaj analizujemy
       a. Czy w partyturze na pierwszym i ostatnim miejscu występuje akord toniczny
       b. Czy w partyturze po dominancie nie występuje subdominanta
       c. Czy w partyturze na mocnej części taktu (na "raz") nie występuje akord w słabym (drugim) przewrocie ->>> to sprawdzić z Sikorskim!!!
       d. Czy w partyturze nie przetrzymano akordu przez kreskę taktową (błąd!) 
       e. ...
       itd.
       
    4. Sprawdzenie poprawności łączeń akordów. Będą to:
        a. Sprawdzenie, czy w partyturze występują kwinty równoległe
        b. Sprawdzenie, czy są oktawy równoległe
        c. Sprawdzenie, czy nie ma ruchu wszystkich głosów w tym samym kierunku
        d. Sprawdzenie, czy nie występują skoki o niedozwolony (zbyt duży lub zwiększony) interwał
        e. ...
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
                element.podaj_sopran().podaj_swoj_kod_bezwzgledny() >= element.podaj_alt().podaj_swoj_kod_bezwzgledny()
                >= element.podaj_tenor().podaj_swoj_kod_bezwzgledny() >= element.podaj_bas().podaj_swoj_kod_bezwzgledny()
        ):
            lista_wynikowa.append((licznik_taktow, licznik_akordow))
        licznik_akordow += 1
    return lista_wynikowa


def czy_glosy_w_swoich_skalach(badana_partytura: partytura.Partytura) -> list[(int, int, str)]:
    """Funkcja sprawdza, czy w podanej partyturze dźwięki nie wykraczają poza skale głosów.
    Zwraca listę tupli postaci (int, int, str), gdzie pierwsza liczba oznacza numer taktu, druga - numer akordu, a str -
    informacje o głosie, w którym nastąpiło naruszenie. Numeracja od 0.
    Pusta lista wynikowa oznacza poprawność partytury."""
    lista_wynikowa = []
    licznik_taktow = 0
    licznik_akordow = 0
    przekroczone_glosy = ""
    for element in badana_partytura.podaj_liste_akordow():
        if element == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        if not (dzwiek.Dzwiek(5, "a").podaj_swoj_kod_bezwzgledny() >=
                element.podaj_sopran().podaj_swoj_kod_bezwzgledny() >=
                dzwiek.Dzwiek(4, "c").podaj_swoj_kod_bezwzgledny()):
            przekroczone_glosy += "sopran "

        if not (dzwiek.Dzwiek(5, "d").podaj_swoj_kod_bezwzgledny() >=
                element.podaj_alt().podaj_swoj_kod_bezwzgledny() >=
                dzwiek.Dzwiek(3, "f").podaj_swoj_kod_bezwzgledny()):
            przekroczone_glosy += "alt "

        if not (dzwiek.Dzwiek(4, "a").podaj_swoj_kod_bezwzgledny() >=
                element.podaj_tenor().podaj_swoj_kod_bezwzgledny() >=
                dzwiek.Dzwiek(3, "c").podaj_swoj_kod_bezwzgledny()):
            przekroczone_glosy += "tenor "

        if not (dzwiek.Dzwiek(4, "d").podaj_swoj_kod_bezwzgledny() >=
                element.podaj_bas().podaj_swoj_kod_bezwzgledny() >=
                dzwiek.Dzwiek(2, "f").podaj_swoj_kod_bezwzgledny()):
            przekroczone_glosy += "bas "

        if len(przekroczone_glosy) > 0:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, przekroczone_glosy))
            przekroczone_glosy = ""
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
