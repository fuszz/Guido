import sprawdzarka as spr
import partytura
from enumerations import enum_przewroty as prz
import akord
import obsluga_wyswietlania as ow

# ================================================================================================
# WARSTWA 3 - Sprawdzenie, czy kolejność akordów jest poprawna
# ================================================================================================

def czy_pierwsza_i_ostatnia_tonika(badana_partytura: partytura.Partytura) -> bool:
    """Sprawdza, czy pierwszym i ostatnim akordem parytury jest tonika.
    Jeśli tak, zwraca True. W przeciwnym razie false"""

    if badana_partytura.podaj_liste_akordow()[0].ustal_funkcje(
            badana_partytura.podaj_tonacje()) not in spr.PRZEWIDZIANE_TONIKI:
        return False

    if badana_partytura.podaj_liste_akordow()[-2].ustal_funkcje(
            badana_partytura.podaj_tonacje()) not in spr.PRZEWIDZIANE_TONIKI:
        return False
    return True

def wyswietl_czy_pierwsza_i_ostatnia_tonika(badana_partytura: partytura.Partytura) -> bool:
    print("Tonika jako pierwszy i ostatni akord: ", end='')
    if czy_pierwsza_i_ostatnia_tonika(badana_partytura):
        print(f"{ow.OK} TAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} NIE {ow.NORMALNY}")
        return False

def czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura: partytura.Partytura) -> bool:
    """Sprawdza, czy ostateczne rozwiązanie (ostatnia tonika w partyturze) jest w innym niż drugi przewrocie. Jeśli tak,
    zwraca True. W przeciwnym razie zwraca False. Funkcja przyjmuje, że ostatni akord to zawsze przedostatni
    element listy akordów"""

    return (badana_partytura.podaj_liste_akordow()[-2].ustal_przewrot(badana_partytura.podaj_tonacje()) !=
            prz.Przewrot.DRUGI)

def wyswietl_czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura: partytura.Partytura) -> bool:
    print("Ostateczne rozwiązanie w drugim przewrocie", end='')
    if czy_pierwsza_i_ostatnia_tonika(badana_partytura):
        print(f"{ow.OK} NIE {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} TAK {ow.NORMALNY}")
        return False

def sygn_subdominant_po_dominancie(badana_partytura: partytura.Partytura) -> list[(int, int)]:
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

        if (element.ustal_funkcje(badana_partytura.podaj_tonacje()) in spr.PRZEWIDZIANE_SUBDOMINANTY and
                ostatni_akord.ustal_funkcje(badana_partytura.podaj_tonacje()) in spr.PRZEWIDZIANE_DOMINANTY):
            lista_wynikowa.append((licznik_taktow, licznik_akordow))

        licznik_akordow += 1
        ostatni_akord = element

    return lista_wynikowa


def wyswietl_sygn_subdominant_po_dominancie(badana_partytura: partytura.Partytura) -> bool:
    print("Subdominanty umieszczone bezpośrednio po dominancie: ", end='')
    if not sygn_subdominant_po_dominancie(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :",
              ow.sygn_akordow_w_str(sygn_subdominant_po_dominancie(badana_partytura)),
              f"{ow.NORMALNY}")
        return False

def nr_taktu_gdzie_drugi_przewrot_na_raz(badana_partytura: partytura.Partytura) -> list[int]:
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

            if (element.ustal_funkcje(badana_partytura.podaj_tonacje()) in spr.PRZEWIDZIANE_TROJDZWIEKI and
                    element.ustal_przewrot(badana_partytura.podaj_tonacje()) == prz.Przewrot.DRUGI):
                lista_wynikowa.append(licznik_taktow)

        if element == "T":
            czy_pierwszy_akord_taktu = True
            licznik_taktow += 1
    return lista_wynikowa

def wyswietl_numery_taktow_gdzie_drugi_przewrot_na_raz(badana_partytura: partytura.Partytura) -> bool:
    print("Takty, w których na \"raz\" występuje drugi przewrót akordu: ", end='')
    if not nr_taktu_gdzie_drugi_przewrot_na_raz(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :",
              ow.nr_taktow_w_str(nr_taktu_gdzie_drugi_przewrot_na_raz(badana_partytura)),
              f"{ow.NORMALNY}")
        return False

def nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura: partytura.Partytura) -> list[int]:
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

def wyswietl_nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura: partytura.Partytura) -> bool:
    print("Takty, do których przez kreskę taktową przetrzymano funkcję ", end='')
    if not nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :",
              ow.nr_taktow_w_str(nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura)),
              f"{ow.NORMALNY}")
        return False

def sprawdz_warstwe_3(badana_partytura: partytura.Partytura) -> bool:
    czy_sprawdzenie_poprawne = True
    if not wyswietl_sygn_subdominant_po_dominancie(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_czy_pierwsza_i_ostatnia_tonika(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_numery_taktow_gdzie_drugi_przewrot_na_raz(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura):
        czy_sprawdzenie_poprawne = False
    return czy_sprawdzenie_poprawne