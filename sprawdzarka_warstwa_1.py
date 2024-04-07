import partytura
import obsluga_wyswietlania as ow
import blad
import akord
import tonacja


# ===============================================================
# Warstwa 1. sprawdzarki --> Poprawność i kompletność wprowadzenia danych:
# ===============================================================
def czy_liczba_taktow_jest_poprawna(badana_partytura: partytura.Partytura) -> bool:
    """Zwraca true, jeśli liczba znaków końca taktu jest taka sama, jak zadeklarowana liczba taktów. W przeciwnym razie
    zwraca false."""
    return badana_partytura.czy_poprawna_liczba_taktow()


def wyswietl_czy_liczba_taktow_jest_poprawna(badana_partytura: partytura.Partytura) -> bool:
    print("Poprawna liczba taktów: ", end='')
    if czy_liczba_taktow_jest_poprawna(badana_partytura):
        print(f"{ow.OK}TAK{ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD}NIE{ow.NORMALNY}")
        return False


def nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura: partytura.Partytura) -> list[int]:
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

def wyswietl_nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura: partytura.Partytura) -> bool:
    print("Poprawna długość akordów w taktach: ", end='')
    if not nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura):
        print(f"{ow.OK}TAK{ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD}NIE - błędy w taktach nr: ",
              ow.nr_taktow_w_str(nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura)), f"{ow.NORMALNY}")
        return False

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


def sygn_akordow_z_dzwiekami_obcymi(badana_partytutra: partytura.Partytura) -> list[(int, int)]:
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



def wyswietl_sygn_akordow_z_dzwiekami_obcymi(badana_partytura: partytura.Partytura) -> bool:
    print("Dźwięki obce w akordach: ", end='')
    if not sygn_akordow_z_dzwiekami_obcymi(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w akordach nr :", ow.sygn_akordow_w_str(sygn_akordow_z_dzwiekami_obcymi(badana_partytura)),
              f"{ow.NORMALNY}")
        return False

def sprawdz_warstwe_1(badana_partytura: partytura.Partytura) -> bool:
    czy_sprawdzenie_poprawne: bool = True
    if not wyswietl_czy_liczba_taktow_jest_poprawna(badana_partytura):
        czy_sprawdzenie_poprawne = False

    if not wyswietl_nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura):
        czy_sprawdzenie_poprawne = False

    if not wyswietl_sygn_akordow_z_dzwiekami_obcymi(badana_partytura):
        czy_sprawdzenie_poprawne = False

    return czy_sprawdzenie_poprawne
