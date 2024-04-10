import sprawdzarka_warstwa_1 as spr_w_1
import obsluga_wyswietlania as ow
from partytura import Partytura


def wyswietl_czy_liczba_taktow_jest_poprawna(badana_partytura: Partytura) -> bool:
    print("Poprawna liczba taktów: ", end='')
    if spr_w_1.czy_liczba_taktow_jest_poprawna(badana_partytura):
        print(f"{ow.OK}TAK{ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD}NIE{ow.NORMALNY}")
        return False


def wyswietl_nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura: Partytura) -> bool:
    print("Poprawna długość akordów w taktach: ", end='')
    if not spr_w_1.nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura):
        print(f"{ow.OK}TAK{ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD}NIE - błędy w taktach nr: ",
              ow.nr_taktow_w_str(spr_w_1.nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura)), f"{ow.NORMALNY}")
        return False


def wyswietl_sygn_akordow_z_dzwiekami_obcymi(badana_partytura: Partytura) -> bool:
    print("Dźwięki obce w akordach: ", end='')
    if not spr_w_1.sygn_akordow_z_dzwiekami_obcymi(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w akordach nr :",
              ow.sygn_akordow_w_str(spr_w_1.sygn_akordow_z_dzwiekami_obcymi(badana_partytura)),
              f"{ow.NORMALNY}")
        return False


def sprawdz_warstwe_1(badana_partytura: Partytura) -> bool:
    czy_sprawdzenie_poprawne: bool = True
    if not wyswietl_czy_liczba_taktow_jest_poprawna(badana_partytura):
        czy_sprawdzenie_poprawne = False

    if not wyswietl_nr_taktow_z_nieodpowiednimi_dlugosciami(badana_partytura):
        czy_sprawdzenie_poprawne = False

    if not wyswietl_sygn_akordow_z_dzwiekami_obcymi(badana_partytura):
        czy_sprawdzenie_poprawne = False

    return czy_sprawdzenie_poprawne
