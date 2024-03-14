import dzwiek
import partytura
import akord
import tonacja
from enumerations import enum_funkcje, enum_krzyzowania_glosow, enum_metrum, enum_przewroty, \
    enum_zdwojony_skladnik, enum_dzwieki_w_skalach, enum_interwal, enum_bledy
from typing import List, Union

DOPUSZCZALNE_DOMINANTY = [enum_funkcje.Funkcja.DOMINANTA, enum_funkcje.Funkcja.DOMINANTA_SEPTYMOWA]
DOPUSZCZALNE_SUBDOMINANTY = [enum_funkcje.Funkcja.SUBDOMINANTA, enum_funkcje.Funkcja.MOLL_SUBDOMINANTA]
IND_ERR_BLAD_LISTY_AK_MSG = ("Index out of range - Niemożliwe odwołanie się do akordu/znaku końca taktu.\n"
                             "Sprawdź poprawność swojego pliku wejściowego")
TYP_ERR_BLAD_LISTY_AK_MSG = ("Type error - W partyturze wystąpił niedozwolony element. \n "
                             "Sprawdź swój plik wejściowy, a zwłaszcza czy któryś takt nie jest pusty")


def badanie_objetosci_taktow_w_partyturze(badana_partytura: partytura.Partytura) -> List[int]:
    """
    Funkcja sprawdza, czy takty w partyturze mają prawidłową (przewidzianą przez określone metrum) długość.
    :param badana_partytura: partytura, w której szukamy błędów
    :return: Lista intów - indeksów znaczników końca taktu dla tych taktów, których długość nie jest poprawna.
    """
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
    Sprawdza, czy podany dźwięk jest stopniem badanej tonacji.
    :param badany_dzwiek: Dźwięk, który chcemy zbadać
    :param badana_tonacja: Tonacja, dla której chcemy sprawdzić dźwięk
    :return: True - jeśli dźwięk jest stopniem tonacji, False - w przeciwnym wypadku
    """
    try:
        badany_dzwiek.podaj_swoj_stopien(badana_tonacja)
        return True
    except enum_bledy.BladDzwiekPozaTonacja:
        return False


def badanie_wystepowania_dzwiekow_obcych(badana_partytura: partytura.Partytura) -> List[int]:
    """
    Funkcja sprawdza, czy w partyturze nie ma dźwięków obcych dla danej tonacji. W projekcie ich nie uwzględniamy.
    :param badana_partytura: sprawdzana partytura
    :return: Lista intów - indeksów tych akordów, w których występują dźwięki obce. Jeśli dźwięki nie występują,
    lista jest pusta.
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
    Funkcja zwraca informację o interwale między dźwiękami. Kolejność dźwięków nie ma znaczenia.
    :param dzwiek_1: Pierwszy sprawdzany dźwięk
    :param dzwiek_2: Drugi sprawdzany dźwięk
    :param badana_tonacja: tonacja, w której oba dźwięki występują naturalnie.
    :return: Krotka: (<liczba_pełnych_oktaw>, <interwał - enum_interwal.Interwal>)
    """

    try:
        dzwiek_1.podaj_swoj_stopien(badana_tonacja)
        dzwiek_2.podaj_swoj_stopien(badana_tonacja)
    except enum_bledy.BladDzwiekPozaTonacja:
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


def badanie_czy_tonika_na_poczatku_i_koncu(badana_partytura: partytura.Partytura) -> bool:
    """
    Sprawdza, czy na krańcach (pierwszy i ostatni akord) partytury jest tonika.
    :param badana_partytura: partytura do sprawdzenia.
    :return: True - jeśli na pierwszym i ostatnim miejscu jest tonika, False - w przeciwnym razie
    """
    try:
        pierwszy_akord: akord.Akord = badana_partytura.podaj_liste_akordow()[0]
        ostatni_akord: akord.Akord = badana_partytura.podaj_liste_akordow()[-2]
        if (pierwszy_akord.ustal_funkcje(badana_partytura.podaj_tonacje()) == enum_funkcje.Funkcja.TONIKA and
                ostatni_akord.ustal_funkcje(badana_partytura.podaj_tonacje()) == enum_funkcje.Funkcja.TONIKA):
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Niepoprawna tablica akordow")


def badanie_czy_dzwieki_akordu_tworza_funkcje_w_tonacji(badana_partytura: partytura.Partytura) -> List[int]:
    """
    Sprawdza, czy akordy partytury są poprawnymi funkcjami harmonicznymi.
    :param badana_partytura: partytura, której akordy są badane
    :return: Lista indeksów akordów, którym nie można przypisać żadnej funkcji harmonicznej.
    W przypadku braku takich akordów zwracana jest pusta lista.
    """
    wynikowa_lista: List[int] = []
    try:
        for indeks, element in enumerate(badana_partytura.podaj_liste_akordow()):
            if element == 'T':
                continue
            if element.ustal_funkcje(badana_partytura.podaj_tonacje()) == enum_funkcje.Funkcja.BLAD:
                wynikowa_lista.append(indeks)
        return wynikowa_lista

    except IndexError:
        raise enum_bledy.BladListyAkordow(IND_ERR_BLAD_LISTY_AK_MSG)


def badanie_czy_po_dominancie_nie_ma_subdominanty(badana_partytura: partytura.Partytura) -> List[int]:
    """
    Sprawdza, czy po dominancie nie występuje subdominanta.
    :param badana_partytura: badana partytura
    :return: Lista indeksów subdominant występujących po dominancie. Pusta lista oznacza brak błędów.
    """
    wynikowa_lista: List[int] = []
    try:
        lista_akordow = badana_partytura.podaj_liste_akordow()
        for indeks, element in enumerate(lista_akordow):
            if element == 'T':
                continue
            if element.ustal_funkcje(badana_partytura.podaj_tonacje()) in DOPUSZCZALNE_DOMINANTY:
                indeks_nastepnego_akordu = indeks + 1
                if lista_akordow[indeks_nastepnego_akordu] == 'T':
                    indeks_nastepnego_akordu += 1
                nastepny_akord: akord.Akord = lista_akordow[indeks_nastepnego_akordu]
                if nastepny_akord.ustal_funkcje(badana_partytura.podaj_tonacje()) in DOPUSZCZALNE_SUBDOMINANTY:
                    wynikowa_lista.append(indeks_nastepnego_akordu)
        return wynikowa_lista

    except IndexError:
        raise enum_bledy.BladListyAkordow(IND_ERR_BLAD_LISTY_AK_MSG)

    except TypeError:
        raise enum_bledy.BladListyAkordow(TYP_ERR_BLAD_LISTY_AK_MSG)


def badanie_czy_takt_nie_zaczyna_sie_drugim_przewrotem(badana_partytura: partytura.Partytura) -> List[int]:
    """
    Sprawdza, czy takt nie rozpoczyna się funkcją w drugim (słabym) przewrocie. Nie dotyczy dominanty septymowej.
    !!!!!!!!!!!!!!!!!!!!!!!SPRAWDZIĆ, CZY TO TYCZY SIĘ TEŻ D7!!!!!!!!!!!!!!!!!!!!!!!!
    :param badana_partytura: badana partytura
    :return: Lista indeksów akordów w 2. przewrocie na pierwszym miejscu taktu. Pusta lista oznacza brak takich błędów.
    """
    try:
        wynikowa_lista: List[int] = []
        lista_akordow: List[Union[akord.Akord, str]] = badana_partytura.podaj_liste_akordow()
        for indeks, element in enumerate(lista_akordow):
            if indeks == 0 or (indeks > 0 and lista_akordow[indeks - 1] == 'T'):
                if (element.ustal_funkcje(
                        badana_partytura.podaj_tonacje()) != enum_funkcje.Funkcja.DOMINANTA_SEPTYMOWA and
                        element.ustal_przewrot(badana_partytura.podaj_tonacje()) == enum_przewroty.Przewrot.DRUGI):
                    wynikowa_lista.append(indeks)
        return wynikowa_lista
    except IndexError:
        raise enum_bledy.BladListyAkordow(IND_ERR_BLAD_LISTY_AK_MSG)
    except TypeError:
        raise enum_bledy.BladListyAkordow(TYP_ERR_BLAD_LISTY_AK_MSG)
