import sprawdzarka_warstwa_2 as spr_w_2
import obsluga_wyswietlania as ow
from partytura import Partytura


def wynik_sygn_akordow_gdzie_glosy_poza_skalami(badana_partytura: Partytura) -> str:
    wyjscie = f"Dźwięki głosów poza skalami: "
    wynik = spr_w_2.sygn_i_glosy_akordow_gdzie_glosy_poza_skalami(badana_partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}" + '\n'
    else:
        wyjscie += "{ow.BLAD} WYSTĘPUJĄ w akordach nr :" + ow.sygn_i_glosy_w_str(wynik) + f"{ow.NORMALNY}" + '\n'
    return wyjscie


def wynik_sygn_akordow_nietwarzacych_funkcji(badana_partytura: Partytura) -> str:
    wyjscie = f"Akordy, które nie tworzą funkcji: "
    wynik = spr_w_2.sygn_akordow_nietworzacych_funkcji(badana_partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}" + '\n'
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w akordach nr :" + ow.sygn_akordow_w_str(wynik) + f"{ow.NORMALNY}" + '\n'
    return wyjscie


def wynik_sygnatura_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura: Partytura) -> str:
    wyjscie = f"Akordy, w których przekroczono dopuszczalne odległości między głosami: "
    wynik = spr_w_2.sygn_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}" + '\n'
    else:
        print(ow.sygn_i_glosy_w_str(wynik))
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :" + ow.sygn_i_glosy_w_str(wynik) + f"{ow.NORMALNY}" + '\n'
    return wyjscie


def poprawnosc_warstwy_2(badana_partytura: Partytura) -> bool:
    if not spr_w_2.sygn_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura):
        return False
    if not spr_w_2.sygn_i_glosy_akordow_gdzie_glosy_poza_skalami(badana_partytura):
        return False
    if not spr_w_2.sygn_akordow_nietworzacych_funkcji(badana_partytura):
        return False
    return True


def wyniki_warstwy_2(badana_partytura: Partytura) -> str:
    wynik = f""
    wynik += wynik_sygn_akordow_gdzie_glosy_poza_skalami(badana_partytura) + '\n'
    wynik += wynik_sygnatura_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura) + '\n'
    wynik += wynik_sygnatura_i_glosy_gdzie_przekroczone_odleglosci(badana_partytura) + '\n'
    return wynik
