from akord import Akord
from dzwiek import Dzwiek
from enumerations.enum_nazwy_interwalow import NazwaInterwalu
from funkcja import Funkcja
from partytura import Partytura
from interwal import Interwal
from tonacja import Tonacja
from enumerations.enum_nazwy_interwalow import NazwaInterwalu
from enumerations.enum_skladnik_funkcji import SkladnikFunkcji

# W RAZIE ROZBUDOWY PROGRAMU NALEŻY UZUPEŁNIĆ PONIŻSZE ZMIENNE GLOBALNE:
PRZEWIDZIANE_TONIKI = [Funkcja.TONIKA, Funkcja.MOLL_TONIKA]
PRZEWIDZIANE_SUBDOMINANTY = [Funkcja.SUBDOMINANTA, Funkcja.MOLL_SUBDOMINANTA]
PRZEWIDZIANE_DOMINANTY = [Funkcja.DOMINANTA, Funkcja.DOMINANTA_SEPTYMOWA]
PRZEWIDZIANE_TROJDZWIEKI = [Funkcja.TONIKA, Funkcja.MOLL_TONIKA, Funkcja.SUBDOMINANTA, Funkcja.MOLL_SUBDOMINANTA,
                            Funkcja.DOMINANTA]
PRZEWIDZIANE_CZTERODZWIEKI = [Funkcja.DOMINANTA_SEPTYMOWA]
KOLEJNOSC_INTERWALOW_MIEDZY_GLOSAMI = ["SA", "ST", "SB", "AT", "AB", "TB"]
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


# ===================================================================================================
# Warstwa 4 - sprawdzenie poprawności połączeń akordów
# ===================================================================================================

def id_niesprawdzanych_interwalow(poprzedni_akord: Akord, akord: Akord) -> list[int]:
    """Zwraca listę indeksów interwałów wg tablicy KOLEJNOSC_INTERWALOW, które nie są sprawdzane pod kątem równoległości,
    bo przynajmniej jeden z głosów nie poruszył się."""

    niesprawdzane_id = []
    if poprzedni_akord.podaj_sopran() == akord.podaj_sopran():
        niesprawdzane_id.extend([0, 1, 2])
    if poprzedni_akord.podaj_alt() == akord.podaj_alt():
        niesprawdzane_id.extend([0, 3, 4])
    if poprzedni_akord.podaj_tenor() == akord.podaj_tenor():
        niesprawdzane_id.extend([1, 3, 5])
    if poprzedni_akord.podaj_bas() == akord.podaj_bas():
        niesprawdzane_id.extend([2, 4, 5])
    niesprawdzane_id = list(set(niesprawdzane_id))
    niesprawdzane_id.sort()
    return niesprawdzane_id


def sygn_i_glosy_z_rownoleglosciami(partytura: Partytura, nazwa_interwalu: NazwaInterwalu) -> list[(int, int, str)]:
    """Zwraca listę trójek (nr_taktu, nr_akordu, nazwy_glosow), które opisują połączenia w których mają miejsce
    równoległości o zadany interwał (NazwaInterwalu.Kwinta dla kwint równoległych i NazwaInterwalu.Pryma dla oktaw)"""

    lista_wynikowa = []
    nr_taktu = 0
    nr_akordu = 1
    poprzedni_akord = partytura.podaj_liste_akordow()[0]
    tonacja = partytura.podaj_tonacje()

    for akord in partytura.podaj_liste_akordow()[1:]:
        if akord == "T":
            nr_taktu += 1
            nr_akordu = 0
            continue

        interwaly_poprzedniego_akordu = Interwal.podaj_interwaly_w_akordzie(poprzedni_akord, tonacja)
        interwaly_obecnego_akordu = Interwal.podaj_interwaly_w_akordzie(akord, tonacja)
        id_niesprawdzanych = id_niesprawdzanych_interwalow(poprzedni_akord, akord)
        glosy = ""
        for i in range(len(interwaly_poprzedniego_akordu)):
            if (interwaly_obecnego_akordu[i].podaj_nazwe() == nazwa_interwalu and
                    interwaly_poprzedniego_akordu[i].podaj_nazwe() == nazwa_interwalu and
                    i not in id_niesprawdzanych):
                glosy += f"{KOLEJNOSC_INTERWALOW_MIEDZY_GLOSAMI[i]} "
        if glosy:
            lista_wynikowa.append((nr_taktu, nr_akordu, glosy))
        nr_akordu += 1
        poprzedni_akord = akord
    return lista_wynikowa


def sygn_gdzie_ruch_glosow_w_tym_samym_kierunku(partytura: Partytura) -> list[(int, int)]:
    """ Sprawdza, czy w którymś połączeniu wszystkie głosy nie poruszają się w tym samym kierunku. Zwraca listę tupli
    postaci (int, int), gdzie pierwsza liczba to numer taktu, a druga - numer akordu w takcie tego akordu, który został
    połączony wadliwie ze swoim poprzednikiem. Liczniki pracują od 0. Pusta lista wynikowa oznacza brak błędu"""

    lista_wynikowa = []
    licznik_akordow = 1
    licznik_taktow = 0

    poprzedni_akord = partytura.podaj_liste_akordow()[0]
    for akord in partytura.podaj_liste_akordow()[1:]:
        if akord == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        midi_dzwiekow_poprzedniego_ak = poprzedni_akord.podaj_kody_midi_skladnikow()
        midi_dzwiekow_obecnego_ak = akord.podaj_kody_midi_skladnikow()

        if (all(d1 > d2 for d1, d2 in zip(midi_dzwiekow_poprzedniego_ak, midi_dzwiekow_obecnego_ak)) or
                all(d1 < d2 for d1, d2 in zip(midi_dzwiekow_poprzedniego_ak, midi_dzwiekow_obecnego_ak))):
            lista_wynikowa.append((licznik_taktow, licznik_akordow))
        licznik_akordow += 1
        poprzedni_akord = akord
    return lista_wynikowa


def sygn_i_glosy_gdzie_ruch_glosu_o_interwal_zwiekszony(partytura: Partytura) -> list[(int, int, str)]:
    """ Sprawdza, czy w którymś połączeniu głos nie porusza się o interwał zwiększony. Zwraca listę tupli
        postaci (int, int, str), gdzie pierwsza liczba to numer taktu, druga - numer akordu w takcie tego akordu, a str
        daje info o głosie, w którym miał miejsce niedozwolony ruch. Wskazywany jest akord wadliwie połączony z
        poprzednikiem. Liczniki pracują od 0. Pusta lista wynikowa oznacza brak błędu. Nie sprawdza, czy interwał nie
        jest zbyt wielki."""

    lista_wynikowa = []
    licznik_akordow = 1
    licznik_taktow = 0
    tonacja = partytura.podaj_tonacje()
    poprzedni_akord = partytura.podaj_liste_akordow()[0]
    for akord in partytura.podaj_liste_akordow()[1:]:
        if akord == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        dzwieki_poprz_ak = poprzedni_akord.podaj_krotke_skladnikow()
        dzwieki_ob_ak = akord.podaj_krotke_skladnikow()
        wadliwe_glosy = ""
        for i in range(4):
            if Interwal.stworz_z_dzwiekow(dzwieki_poprz_ak[i], dzwieki_ob_ak[i],
                                          tonacja).podaj_nazwe().czy_interwal_zwiekszony:
                wadliwe_glosy += KOLEJNOSC_GLOSOW[i]
        if wadliwe_glosy:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, wadliwe_glosy))
        licznik_akordow += 1
        poprzedni_akord = akord
    return lista_wynikowa


def sygn_i_glosy_gdzie_ruch_o_zbyt_duzy_interwal(partytura: Partytura) -> list[(int, int, str)]:
    """ Sprawdza, czy w którymś połączeniu głos nie porusza się o zbyt duży interwał. Zwraca listę tupli
        postaci (int, int, str), gdzie pierwsza liczba to numer taktu, druga - numer akordu w takcie tego akordu, a str
        daje info o głosie, w którym miał miejsce niedozwolony ruch. Wskazywany jest akord wadliwie połączony z
        poprzednikiem. Liczniki pracują od 0. Pusta lista wynikowa oznacza brak błędu."""

    lista_wynikowa = []
    licznik_akordow = 1
    licznik_taktow = 0
    poprzedni_akord = partytura.podaj_liste_akordow()[0]
    for akord in partytura.podaj_liste_akordow()[1:]:
        if akord == "T":
            licznik_taktow += 1
            licznik_akordow = 0
            continue
        dzwieki_poprzedniego_akordu = poprzedni_akord.podaj_krotke_skladnikow()
        dzwieki_obecnego_akordu = akord.podaj_krotke_skladnikow()
        wadliwe_glosy = ""
        for i in range(4):
            ruch_w_glosie = Interwal.stworz_z_dzwiekow(dzwieki_poprzedniego_akordu[i], dzwieki_obecnego_akordu[i],
                                                       partytura.podaj_tonacje())
            if ruch_w_glosie.podaj_liczbe_oktaw() > 0 or ruch_w_glosie.podaj_nazwe() > NazwaInterwalu.SEKSTA_WIELKA:
                wadliwe_glosy += KOLEJNOSC_GLOSOW[i]

        if wadliwe_glosy:
            lista_wynikowa.append((licznik_taktow, licznik_akordow, wadliwe_glosy))
        licznik_akordow += 1
        poprzedni_akord = akord
    return lista_wynikowa


def czy_rozwiazanie_dominanty_jest_poprawne(dominanta: Akord, rozwiazanie: Akord, tonacja: Tonacja) -> bool:
    """Zwraca True, jeśli poprawnie rozwiązano dominantę i False, gdy rozwiązanie nie jest poprawne"""
    for (dzwiek_dominanty, dzwiek_rozwiazania) in zip(dominanta.podaj_krotke_skladnikow(),
                                                      rozwiazanie.podaj_krotke_skladnikow()):
        if (Funkcja.DOMINANTA.stopien_tonacji_w_skladnik(dzwiek_dominanty.podaj_swoj_stopien(tonacja)) ==
                SkladnikFunkcji.TERCJA_WIELKA):
            if (tonacja.czy_dur() and not Funkcja.TONIKA.stopien_tonacji_w_skladnik(
                    dzwiek_rozwiazania.podaj_swoj_stopien(tonacja)) == SkladnikFunkcji.PRYMA):
                return False
            elif (not tonacja.czy_dur() and not Funkcja.MOLL_TONIKA.stopien_tonacji_w_skladnik(
                    dzwiek_rozwiazania.podaj_swoj_stopien(tonacja)) == SkladnikFunkcji.PRYMA):
                return False
    return True


def czy_rozwiazanie_d7_jest_poprawne(d7: Akord, rozwiazanie: Akord, tonacja: Tonacja) -> bool:
    """Zwraca True, jeśli poprawnie rozwiązano dominantę septymową i False, gdy rozwiązanie nie jest poprawne"""
    for (dzwiek_dominanty, dzwiek_rozwiazania) in zip(d7.podaj_krotke_skladnikow(),
                                                      rozwiazanie.podaj_krotke_skladnikow()):
        if (Funkcja.DOMINANTA_SEPTYMOWA.stopien_tonacji_w_skladnik(dzwiek_dominanty.podaj_swoj_stopien(tonacja)) ==
                SkladnikFunkcji.TERCJA_WIELKA):
            if (tonacja.czy_dur() and not Funkcja.TONIKA.stopien_tonacji_w_skladnik(
                    dzwiek_rozwiazania.podaj_swoj_stopien(tonacja)) == SkladnikFunkcji.PRYMA):
                return False
            elif (not tonacja.czy_dur() and not Funkcja.MOLL_TONIKA.stopien_tonacji_w_skladnik(
                    dzwiek_rozwiazania.podaj_swoj_stopien(tonacja)) == SkladnikFunkcji.PRYMA):
                return False
        elif (Funkcja.DOMINANTA_SEPTYMOWA.stopien_tonacji_w_skladnik(dzwiek_dominanty.podaj_swoj_stopien(tonacja)) ==
                SkladnikFunkcji.SEPTYMA):
            if (tonacja.czy_dur() and not Funkcja.TONIKA.stopien_tonacji_w_skladnik(
                    dzwiek_rozwiazania.podaj_swoj_stopien(tonacja)) == SkladnikFunkcji.TERCJA_WIELKA):
                return False
            elif (not tonacja.czy_dur() and not Funkcja.MOLL_TONIKA.stopien_tonacji_w_skladnik(
                    dzwiek_rozwiazania.podaj_swoj_stopien(tonacja)) == SkladnikFunkcji.TERCJA_MALA):
                return False
    return True


def sygn_niepoprawnych_rozwiazan_dominant(partytura: Partytura) -> list[(int, int)]:
    """Zwraca listę sygnatur niepoprawnych rozwiązań dominant"""
    nr_taktu = 0
    nr_akordu = 0
    lista_wyjsciowa: list[(int, int)] = []
    poprzedni_akord: Akord = partytura.podaj_liste_akordow()[0]
    czy_poprzednia_dominanta: bool = False
    tonacja_partytury = partytura.podaj_tonacje()

    for akord in partytura.podaj_liste_akordow():
        if akord == "T":
            nr_taktu += 1
            nr_akordu = 0
            continue

        if akord.ustal_funkcje(partytura.podaj_tonacje()) == Funkcja.DOMINANTA:
            czy_poprzednia_dominanta = True

        elif akord.ustal_funkcje(partytura.podaj_tonacje()) == Funkcja.TONIKA and czy_poprzednia_dominanta:
            czy_poprzednia_dominanta = False
            czy_rozwiazanie_dominanty_jest_poprawne(poprzedni_akord, akord, tonacja_partytury)

        poprzedni_akord = akord
        nr_akordu += 1

    return lista_wyjsciowa


def sygn_niepoprawnych_rozwiazan_dominant_septymowych(partytura: Partytura) -> list[(int, int)]:
    """Zwraca listę sygnatur niepoprawnych rozwiązań dominant septymowych"""
    nr_taktu = 0
    nr_akordu = 0
    lista_wyjsciowa: list[(int, int)] = []

    poprzedni_akord: Akord = partytura.podaj_liste_akordow()[0]
    czy_poprzednia_dominanta_septymowa: bool = False
    tonacja_partytury = partytura.podaj_tonacje()

    for akord in partytura.podaj_liste_akordow():
        if akord == "T":
            nr_taktu += 1
            nr_akordu = 0
            continue

        if akord.ustal_funkcje(partytura.podaj_tonacje()) == Funkcja.DOMINANTA_SEPTYMOWA:
            czy_poprzednia_dominanta_septymowa = True

        elif akord.ustal_funkcje(partytura.podaj_tonacje()) == Funkcja.TONIKA and czy_poprzednia_dominanta_septymowa:
            czy_poprzednia_dominanta_septymowa = False
            czy_rozwiazanie_d7_jest_poprawne(poprzedni_akord, akord, tonacja_partytury)

        poprzedni_akord = akord
        nr_akordu += 1

    return lista_wyjsciowa
