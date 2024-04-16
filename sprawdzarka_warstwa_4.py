from akord import Akord
from dzwiek import Dzwiek
from enumerations.enum_nazwy_interwalow import NazwyInterwalow
from funkcja import Funkcja
from partytura import Partytura
from interwal import Interwal

# W RAZIE ROZBUDOWY PROGRAMU NALEŻY UZUPEŁNIĆ PONIŻSZE ZMIENNE GLOBALNE:
PRZEWIDZIANE_TONIKI = [Funkcja.TONIKA,  Funkcja.MOLL_TONIKA]
PRZEWIDZIANE_SUBDOMINANTY = [Funkcja.SUBDOMINANTA,  Funkcja.MOLL_SUBDOMINANTA]
PRZEWIDZIANE_DOMINANTY = [Funkcja.DOMINANTA,  Funkcja.DOMINANTA_SEPTYMOWA]
PRZEWIDZIANE_TROJDZWIEKI = [Funkcja.TONIKA, Funkcja.MOLL_TONIKA, Funkcja.SUBDOMINANTA, Funkcja.MOLL_SUBDOMINANTA,
                            Funkcja.DOMINANTA]
PRZEWIDZIANE_CZTERODZWIEKI = [Funkcja.DOMINANTA_SEPTYMOWA]
KOLEJNOSC_INTERWALOW_MIEDZY_GLOSAMI = ["SA,", "ST,", "SB,", "AT,", "AB,", "TB,"]
KOLEJNOSC_GLOSOW = ["S", "A", "T", "B"]

""" Moduł sprawdzarki będzie opierać sie na czterech (?) warstwach sprawdzania poprawności partytury. Będą to:
    1. Sprawdzenie, czy wprowadzone dane są kompletne i czy dane nie zostały uszkodzone. Należą tu:
        a. Czy wprowadzono zadeklarowaną w partyturze liczbę taktów - OK
        b. Czy pojemność poszczególnych taktów odpowiada wymogom obranego metrum - OK
        a. Czy w partyturze nie występują dźwięki obce - OK
        itp.
        
    2. Sprawdzenie, czy w partyturze nie ma pionowych błędów, czyli takich, które nie dotyczą kolejności 
       ani łączenia akordów ze sobą. A zatem:

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
       e. Czy ostateczne rozwiązanie nie jest w drugim (słabym) przewrocie - OK
       itd.
       
    4. Sprawdzenie poprawności łączeń akordów. Będą to:
        a. Sprawdzenie, czy w partyturze występują kwinty równoległe - OK
        b. Sprawdzenie, czy są oktawy równoległe - OK
        c. Sprawdzenie, czy nie ma ruchu wszystkich głosów w tym samym kierunku - OK
        d. Sprawdzenie, czy nie występują skoki o zbyt duży interwał - OK
        e. Sprawdzenie, czy nie występuje ruch o interwał zwiększony - OK
        f. ...
        itp.
        
    Jeśli we wcześniejszych warstwach testy wykażą błędy, sprawdzanie zakończy się, bo niemożliwe będzie osiągnięcie
    pozytywnych wyników w testach późniejszych, co wynika z prawideł harmonii. Użytkownik będzie informowany 
    o występowaniu poszczególnych błędów. Niektóre funkcje, w razie wystąpienia błędów, z tego samego powodu będą 
    przerywać dalsze poszukiwanie błędów.
"""


def podaj_interwaly_w_akordzie(badany_akord: Akord, badana_tonacja) -> \
        ((int, NazwyInterwalow), (int, NazwyInterwalow), (int, NazwyInterwalow), (int, NazwyInterwalow),
         (int, NazwyInterwalow), (int, NazwyInterwalow)):
    """Zwraca krotkę odległości pomiędzy głosami w następującej kolejności:
        S-A, S-T, S-B, A-T, A-B, T-B. Krotka ma postać par intów i Interwałów, gdzie int oznacza liczbę pełnych oktaw.
    """
    return (Interwal.stworz_z_dzwiekow(badany_akord.podaj_sopran(), badany_akord.podaj_alt(), badana_tonacja),
            Interwal.stworz_z_dzwiekow(badany_akord.podaj_sopran(), badany_akord.podaj_tenor(), badana_tonacja),
            Interwal.stworz_z_dzwiekow(badany_akord.podaj_sopran(), badany_akord.podaj_bas(), badana_tonacja),
            Interwal.stworz_z_dzwiekow(badany_akord.podaj_alt(), badany_akord.podaj_tenor(), badana_tonacja),
            Interwal.stworz_z_dzwiekow(badany_akord.podaj_alt(), badany_akord.podaj_bas(), badana_tonacja),
            Interwal.stworz_z_dzwiekow(badany_akord.podaj_tenor(), badany_akord.podaj_bas(), badana_tonacja))


# ===================================================================================================
# Warstwa 4 - sprawdzenie poprawności połączeń akordów
# ===================================================================================================


def daj_krotke_dzwiekow_z_akordu(badany_akord: Akord) -> (Dzwiek, Dzwiek, Dzwiek, Dzwiek):
    """Zwraca dźwięki składowe akordu w postaci czteroelementowej krotki obiektów klasy Dźwięk w kolejności:
    (sopran, alt, tenor, bas)"""
    return badany_akord.podaj_sopran(), badany_akord.podaj_alt(), badany_akord.podaj_tenor(), badany_akord.podaj_bas()


def sygn_i_glosy_z_polaczeniem_kwintami_rownoleglymi(badana_partytura: Partytura) -> list[(int, int, str)]:
    """Bada połączenia akordów i sprawdza, czy nie występują kwinty równoległe. Zwraca listę tupli postaci
    (int, int, str), gdzie inty to kolejno numer taktu i numer akordu w tym takcie, który jest drugim w którym jest
    kwinta równoległa, a str wskazuje na głosy, między którymi wykryto kwinty. Pusta lista wynikowa oznacza brak kwint.
    Takty i akordy numerowane są od 0.
    """

    lista_wynikowa: list[(int, int, str)] = []
    licznik_taktow = 0
    licznik_akordow = 0
    poprzedni_akord: Akord = badana_partytura.podaj_liste_akordow()[0]

    for obecny_akord in badana_partytura.podaj_liste_akordow()[1:]:
        if obecny_akord == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        licznik_akordow += 1
        interwaly_w_obecn_akrd = podaj_interwaly_w_akordzie(obecny_akord, badana_partytura.podaj_tonacje())
        interwaly_w_poprz_akrd = podaj_interwaly_w_akordzie(poprzedni_akord, badana_partytura.podaj_tonacje())
        glosy_z_kwintami = ""
        for i in range(6):
            if (interwaly_w_obecn_akrd[i][1] == NazwyInterwalow.KWINTA_CZYSTA and
                    interwaly_w_poprz_akrd[i][1] == NazwyInterwalow.KWINTA_CZYSTA):
                glosy_z_kwintami += KOLEJNOSC_INTERWALOW_MIEDZY_GLOSAMI[i]

        if glosy_z_kwintami:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, glosy_z_kwintami))

    return lista_wynikowa


def sygn_i_glosy_z_polaczeniem_oktawami_rownoleglymi(badana_partytura: Partytura) -> list[(int, int, str)]:
    """Bada połączenia akordów i sprawdza, czy nie występują oktawy równoległe. Zwraca listę tupli postaci
    (int, int, str), gdzie inty to kolejno numer taktu i numer akordu w tym takcie, który jest drugim w którym jest
    oktawa równoległa, a str wskazuje na głosy, między którymi wykryto oktawy. Pusta lista wynikowa oznacza brak błędów.
    Takty i akordy numerowane są od 0.
    """

    lista_wynikowa: list[(int, int, str)] = []
    licznik_taktow = 0
    licznik_akordow = 0
    interwaly_w_poprz_akrd: list[Interwal] = podaj_interwaly_w_akordzie(badana_partytura.podaj_liste_akordow()[0],
                                                                        badana_partytura.podaj_tonacje())

    for obecny_akord in badana_partytura.podaj_liste_akordow()[1:]:
        if obecny_akord == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
            
        licznik_akordow += 1
        interwaly_w_obecn_akrd: list[Interwal] = podaj_interwaly_w_akordzie(obecny_akord, badana_partytura.podaj_tonacje())
        glosy_z_oktawami = ""
        
        for i in range(6):
            if (interwaly_w_obecn_akrd[i].podaj_liczbe_oktaw() > 0 and interwaly_w_obecn_akrd[i].podaj_interwal() == NazwyInterwalow.PRYMA_CZYSTA and
                    interwaly_w_poprz_akrd[i][0] > 0 and interwaly_w_poprz_akrd[i][1] == NazwyInterwalow.PRYMA_CZYSTA):
                glosy_z_oktawami += KOLEJNOSC_INTERWALOW_MIEDZY_GLOSAMI[i]

        if glosy_z_oktawami:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, glosy_z_oktawami))

    return lista_wynikowa


def sygn_gdzie_ruch_glosow_w_tym_samym_kierunku(badana_partytura: Partytura) -> list[(int, int)]:
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
        if ((all(d1 > d2 for d1, d2 in zip(kody_midi_dzwiekow_poprzedniego_akordu, kody_midi_dzwiekow_obecnego_akordu)))
                or (all(d1 < d2 for d1, d2 in
                        zip(kody_midi_dzwiekow_poprzedniego_akordu, kody_midi_dzwiekow_obecnego_akordu)))):
            lista_wynikowa.append((licznik_taktow, licznik_akordow))
    return lista_wynikowa


def sygn_i_glosy_gdzie_ruch_glosu_o_interwal_zwiekszony(badana_partytura: Partytura) -> list[(int, int, str)]:
    """ Sprawdza, czy w którymś połączeniu głos nie porusza się o interwał zwiększony. Zwraca listę tupli
        postaci (int, int, str), gdzie pierwsza liczba to numer taktu, druga - numer akordu w takcie tego akordu, a str
        daje info o głosie, w którym miał miejsce niedozwolony ruch. Wskazywany jest akord wadliwie połączony z
        poprzednikiem. Liczniki pracują od 0. Pusta lista wynikowa oznacza brak błędu. Nie sprawdza, czy interwał nie
        jest zbyt wielki."""

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
        dzwieki_poprzedniego_akordu = poprzedni_akord.podaj_krotke_dzwiekow_z_akordu()
        dzwieki_obecnego_akordu = obecny_akord.podaj_krotke_dzwiekow_z_akordu()
        wadliwe_glosy = ""
        for i in range(4):
            if Interwal.stworz_z_dzwiekow(dzwieki_poprzedniego_akordu[i], dzwieki_obecnego_akordu[i],
                                          badana_partytura.podaj_tonacje()).podaj_interwal().czy_interwal_zwiekszony:
                wadliwe_glosy += KOLEJNOSC_GLOSOW[i]

        if wadliwe_glosy:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, wadliwe_glosy))

    return lista_wynikowa


def sygn_i_glosy_gdzie_ruch_o_zbyt_duzy_interwal(badana_partytura: Partytura) -> list[(int, int, str)]:
    """ Sprawdza, czy w którymś połączeniu głos nie porusza się o zbyt duży interwał. Zwraca listę tupli
        postaci (int, int, str), gdzie pierwsza liczba to numer taktu, druga - numer akordu w takcie tego akordu, a str
        daje info o głosie, w którym miał miejsce niedozwolony ruch. Wskazywany jest akord wadliwie połączony z
        poprzednikiem. Liczniki pracują od 0. Pusta lista wynikowa oznacza brak błędu."""

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
        dzwieki_poprzedniego_akordu = poprzedni_akord.podaj_krotke_dzwiekow_z_akordu()
        dzwieki_obecnego_akordu = obecny_akord.podaj_krotke_dzwiekow_z_akordu()
        wadliwe_glosy = ""
        for i in range(4):
            ruch_w_glosie = Interwal.stworz_z_dzwiekow(dzwieki_poprzedniego_akordu[i], dzwieki_obecnego_akordu[i],
                                                       badana_partytura.podaj_tonacje())
            if ruch_w_glosie.podaj_liczbe_oktaw() > 0 or ruch_w_glosie.podaj_interwal() > NazwyInterwalow.SEKSTA_WIELKA:
                wadliwe_glosy += KOLEJNOSC_GLOSOW[i]

        if wadliwe_glosy:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, wadliwe_glosy))

    return lista_wynikowa
