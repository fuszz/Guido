import sprawdzarka_warstwa_2 as spr_w_2
import obsluga_wyswietlania as ow
from partytura import Partytura


def wyswietl_sygn_akordow_gdzie_glosy_poza_skalami(badana_partytura: Partytura) -> bool:
    print("Dźwięki głosów poza skalami: ", end='')
    if not spr_w_2.sygn_i_glosy_akordow_gdzie_glosy_poza_skalami(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w akordach nr :",
              ow.sygn_i_glosy_w_str(spr_w_2.sygn_i_glosy_akordow_gdzie_glosy_poza_skalami(badana_partytura)),
              f"{ow.NORMALNY}")
        return False


def wyswietl_sygn_akordow_nietwarzacych_funkcji(badana_partytura: Partytura) -> bool:
    print("Akordy, które nie tworzą funkcji: ", end='')
    if not spr_w_2.sygn_akordow_nietworzacych_funkcji(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w akordach nr :",
              ow.sygn_akordow_w_str(spr_w_2.sygn_akordow_nietworzacych_funkcji(badana_partytura)),
              f"{ow.NORMALNY}")
        return False


def wyswietl_sygnatura_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura: Partytura) -> bool:
    print("Akordy, w których przekroczono dopuszczalne odległości między głosami: ", end='')
    if not spr_w_2.sygn_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :",
              ow.sygn_i_glosy_w_str(spr_w_2.sygn_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura)),
              f"{ow.NORMALNY}")
        return False


def sprawdz_warstwe_2(badana_partytura: Partytura) -> bool:
    czy_sprawdzenie_poprawne = True

    if not wyswietl_sygn_akordow_nietwarzacych_funkcji(badana_partytura):
        return False

    if not wyswietl_sygn_akordow_gdzie_glosy_poza_skalami(badana_partytura):
        czy_sprawdzenie_poprawne = False

    if not wyswietl_sygnatura_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura):
        czy_sprawdzenie_poprawne = False

    return czy_sprawdzenie_poprawne
