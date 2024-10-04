import sprawdzarka_warstwa_1 as spr_w_1
import obsluga_wyswietlania as ow
from partytura import Partytura


def wynik_czy_liczba_taktow_jest_poprawna(badana_partytura: Partytura) -> str:
    wynik = f""
    wynik += f"Poprawna liczba taktów: "
    if spr_w_1.czy_liczba_taktow_jest_poprawna(badana_partytura):
        wynik += f"{ow.OK}TAK{ow.NORMALNY}"
    else:
        wynik += f"{ow.BLAD}NIE{ow.NORMALNY}"
    return wynik


def wynik_nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura: Partytura) -> str:
    wynik = f"Poprawna długość akordów w taktach: "
    if not spr_w_1.nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura):
        wynik += f"{ow.OK}TAK{ow.NORMALNY}"
    else:
        wynik += (f"{ow.BLAD}NIE - błędy w taktach nr: " +
                  ow.nr_taktow_w_str(
                      spr_w_1.nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura)) + f"{ow.NORMALNY}")
    return wynik


def wynik_sygn_akordow_z_dzwiekami_obcymi(badana_partytura: Partytura) -> str:
    wynik = f"Dźwięki obce w akordach: "
    if not spr_w_1.sygn_akordow_z_dzwiekami_obcymi(badana_partytura):
        wynik += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wynik += (f"{ow.BLAD} WYSTĘPUJĄ w akordach nr :" +
                  ow.sygn_akordow_w_str(spr_w_1.sygn_akordow_z_dzwiekami_obcymi(badana_partytura)) +
                  f"{ow.NORMALNY}")
    return wynik


def poprawnosc_warstwy_1(badana_partytura: Partytura) -> bool:
    """Zwraca True, jeśli partytura poprawna, w przeciwnym razie False"""
    czy_sprawdzenie_poprawne: bool = True
    if not spr_w_1.czy_liczba_taktow_jest_poprawna(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if spr_w_1.nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if spr_w_1.sygn_akordow_z_dzwiekami_obcymi(badana_partytura):
        czy_sprawdzenie_poprawne = False
    return czy_sprawdzenie_poprawne


def wyniki_warstwy_1(badana_partytura: Partytura) -> str:
    wynik = f""
    wynik += f"{wynik_czy_liczba_taktow_jest_poprawna(badana_partytura)} \n"
    wynik += f"{wynik_nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura)} \n"
    wynik += f"{wynik_sygn_akordow_z_dzwiekami_obcymi(badana_partytura)} \n \n"
    return wynik
